from app.db import Base
from app.models.asp import Asp
from app.models.categoria_paziente import CategoriaPaziente
from app.models.comune import Comune
from app.models.contatto_pz import ContattoPz
from app.models.diagnosi import Diagnosi
from app.models.dipendente import Dipendente
from app.models.disciplina import Disciplina
from app.models.disdetta_prenotazione import DisdettaPrenotazione
from app.models.grado_urgenza import GradoUrgenza
from app.models.gruppo_sanguigno import GruppoSanguigno
from app.models.livello_istruzione import LivelloIstruzione
from app.models.medico import Medico
from app.models.medico_esterno import MedicoEsterno
from app.models.modalita_accesso import ModalitaAccesso
from app.models.paziente import Paziente
from app.models.posizione_professionale import PosizioneProfessionale
from app.models.prenotazione import Prenotazione
from app.models.prericovero import Prericovero
from app.models.presidio_osp import PresidioOsp
from app.models.professione import Professione
from app.models.provenienza import Provenienza
from app.models.rapporto_dipendenza import RapportoDipendenza
from app.models.regione import Regione
from app.models.reparto import Reparto, reparti_dipendenti
from app.models.ricovero import Ricovero
from app.models.stato import Stato
from app.models.stato_civile import StatoCivile
from app.models.tipo_dipendente import TipoDipendente
from app.models.tipo_documento import TipoDocumento
from app.models.titolo import Titolo

__all__ = [
    "Base",
    "Asp",
    "CategoriaPaziente",
    "Comune",
    "ContattoPz",
    "Diagnosi",
    "Dipendente",
    "Disciplina",
    "DisdettaPrenotazione",
    "GradoUrgenza",
    "GruppoSanguigno",
    "LivelloIstruzione",
    "Medico",
    "MedicoEsterno",
    "ModalitaAccesso",
    "Paziente",
    "PosizioneProfessionale",
    "Prenotazione",
    "Prericovero",
    "PresidioOsp",
    "Professione",
    "Provenienza",
    "RapportoDipendenza",
    "Regione",
    "Reparto",
    "reparti_dipendenti",
    "Ricovero",
    "Stato",
    "StatoCivile",
    "TipoDipendente",
    "TipoDocumento",
    "Titolo",
]
