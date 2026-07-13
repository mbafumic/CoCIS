"""create pazienti, contatti_pz, ricoveri

Revision ID: d8c87d4e55d9
Revises:
Create Date: 2026-07-13 16:28:04.250696

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d8c87d4e55d9"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "pazienti",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nome", sa.String(length=100), nullable=False),
        sa.Column("cognome", sa.String(length=100), nullable=False),
        sa.Column("data_nascita", sa.Date(), nullable=False),
        sa.Column("codice_fiscale", sa.String(length=16), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index("ix_pazienti_codice_fiscale", "pazienti", ["codice_fiscale"], unique=True)

    op.create_table(
        "contatti_pz",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("paziente_id", sa.Integer(), sa.ForeignKey("pazienti.id"), nullable=False),
        sa.Column("tipo_contatto", sa.String(length=50), nullable=False),
        sa.Column("data_apertura", sa.Date(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index("ix_contatti_pz_paziente_id", "contatti_pz", ["paziente_id"])

    op.create_table(
        "ricoveri",
        sa.Column("id", sa.Integer(), sa.ForeignKey("contatti_pz.id"), primary_key=True),
        sa.Column("reparto", sa.String(length=100), nullable=False),
        sa.Column("data_ricovero", sa.Date(), nullable=False),
        sa.Column("data_dimissione", sa.Date(), nullable=True),
        sa.Column("stato", sa.String(length=20), nullable=False, server_default="aperto"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("ricoveri")
    op.drop_index("ix_contatti_pz_paziente_id", table_name="contatti_pz")
    op.drop_table("contatti_pz")
    op.drop_index("ix_pazienti_codice_fiscale", table_name="pazienti")
    op.drop_table("pazienti")
