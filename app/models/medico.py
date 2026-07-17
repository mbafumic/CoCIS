from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING, Literal

from sqlalchemy import Boolean, Date, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.dipendente import Dipendente

if TYPE_CHECKING:
    pass


class Medico(Dipendente):
    """Medico: sottotipo concreto di Dipendente (joined-table inheritance).

    Nel legacy `Medici : Dipendenti` con PK condivisa (`medici.Oid → dipendenti.Oid`).
    Il discriminatore XPO (`ObjectType`) stava sulla radice `PermissionPolicyUser`,
    infrastruttura di sicurezza che non migriamo: qui il discriminatore è
    `Dipendente.tipo_personale`.

    `tutor_spec_id` è un self-riferimento: il medico tutor di uno specializzando.
    """

    __tablename__ = "medici"

    id: Mapped[int] = mapped_column(ForeignKey("dipendenti.id"), primary_key=True)

    n_empam: Mapped[str | None] = mapped_column(String(10), default=None)
    codice_regionale: Mapped[str | None] = mapped_column(String(16), default=None)
    codice_lis: Mapped[str | None] = mapped_column(String(10), default=None)
    chirurgo: Mapped[bool] = mapped_column(Boolean, default=False)
    revisore_cc: Mapped[bool] = mapped_column(Boolean, default=False)
    no_validazione_rilascio: Mapped[bool] = mapped_column(Boolean, default=False)

    font_referti: Mapped[str | None] = mapped_column(String(100), default=None)
    sigla_prog_op: Mapped[str | None] = mapped_column(String(3), default=None)

    # compenso ambulatoriale
    percentuale_ambulatorio: Mapped[Decimal | None] = mapped_column(Numeric(28, 8), default=None)
    percentuale_ambulatorio_prec: Mapped[Decimal | None] = mapped_column(
        Numeric(28, 8), default=None
    )
    data_variazione_percentuale: Mapped[date | None] = mapped_column(Date, default=None)
    tipo_compenso: Mapped[Literal["Fattura", "BustaPaga", "Altro"] | None] = mapped_column(
        String(20), default=None
    )

    # specializzandi
    specializzando: Mapped[bool] = mapped_column(Boolean, default=False)
    tutor_spec_id: Mapped[int | None] = mapped_column(ForeignKey("medici.id"), default=None)
    anno_corso: Mapped[str | None] = mapped_column(String(100), default=None)

    tutor_spec: Mapped["Medico | None"] = relationship(
        remote_side=[id], foreign_keys=[tutor_spec_id]
    )

    __mapper_args__ = {
        "polymorphic_identity": "medico",
        "inherit_condition": id == Dipendente.id,
    }

    @property
    def firma_referti(self) -> str:
        """Riga di firma per i referti. Calcolata, non persistita (era un
        PersistentAlias che concatenava titolo, cognome, nome e codice regionale)."""
        parti = [p for p in (self.cognome, self.nome) if p]
        nominativo = " ".join(parti)
        if self.codice_regionale:
            return f"{nominativo} - {self.codice_regionale}"
        return nominativo
