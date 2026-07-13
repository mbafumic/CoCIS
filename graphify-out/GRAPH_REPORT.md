# Graph Report - C:\Users\OMONACO.DROMONACO\CoCIS\oldsystem  (2026-07-13)

## Corpus Check
- 926 files · ~248,905 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3337 nodes · 6254 edges · 239 communities (230 shown, 9 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 33 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
- Community 16
- Community 17
- Community 18
- Community 19
- Community 20
- Community 21
- Community 22
- Community 23
- Community 24
- Community 25
- Community 26
- Community 27
- Community 28
- Community 29
- Community 30
- Community 31
- Community 32
- Community 33
- Community 34
- Community 35
- Community 36
- Community 37
- Community 38
- Community 39
- Community 40
- Community 41
- Community 42
- Community 43
- Community 44
- Community 45
- Community 46
- Community 47
- Community 48
- Community 49
- Community 50
- Community 51
- Community 52
- Community 53
- Community 54
- Community 55
- Community 56
- Community 57
- Community 58
- Community 59
- Community 60
- Community 61
- Community 62
- Community 63
- Community 64
- Community 65
- Community 66
- Community 67
- Community 68
- Community 69
- Community 70
- Community 71
- Community 72
- Community 73
- Community 74
- Community 75
- Community 76
- Community 77
- Community 78
- Community 79
- Community 80
- Community 81
- Community 82
- Community 83
- Community 84
- Community 85
- Community 86
- Community 87
- Community 88
- Community 89
- Community 90
- Community 91
- Community 92
- Community 93
- Community 94
- Community 95
- Community 96
- Community 97
- Community 98
- Community 99
- Community 100
- Community 101
- Community 102
- Community 103
- Community 104
- Community 105
- Community 106
- Community 107
- Community 108
- Community 109
- Community 110
- Community 111
- Community 112
- Community 113
- Community 114
- Community 115
- Community 116
- Community 117
- Community 118
- Community 119
- Community 120
- Community 121
- Community 122
- Community 123
- Community 124
- Community 125
- Community 126
- Community 127
- Community 128
- Community 129
- Community 130
- Community 131
- Community 132
- Community 133
- Community 134
- Community 135
- Community 136
- Community 137
- Community 138
- Community 139
- Community 140
- Community 141
- Community 142
- Community 143
- Community 144
- Community 145
- Community 146
- Community 147
- Community 148
- Community 149
- Community 150
- Community 151
- Community 152
- Community 153
- Community 154
- Community 155
- Community 156
- Community 157
- Community 158
- Community 159
- Community 160
- Community 161
- Community 162
- Community 163
- Community 164
- Community 165
- Community 166
- Community 167
- Community 168
- Community 169
- Community 170
- Community 171
- Community 172
- Community 173
- Community 174
- Community 175
- Community 176
- Community 177
- Community 178
- Community 179
- Community 180
- Community 181
- Community 182
- Community 183
- Community 184
- Community 185
- Community 186
- Community 187
- Community 188
- Community 190
- Community 191
- Community 192
- Community 193
- Community 194
- Community 195
- Community 196
- Community 197
- Community 198
- Community 199
- Community 200
- Community 201
- Community 202
- Community 203
- Community 204
- Community 205
- Community 206
- Community 207
- Community 208
- Community 209
- Community 210
- Community 211
- Community 212
- Community 213
- Community 214
- Community 215
- Community 216
- Community 217
- Community 218
- Community 219
- Community 220
- Community 221
- Community 222
- Community 223
- Community 224
- Community 225
- Community 226
- Community 227
- Community 228
- Community 229
- Community 230
- Community 231
- Community 232
- Community 233
- Community 234
- Community 235
- Community 236
- Community 237
- Community 238

## God Nodes (most connected - your core abstractions)
1. `AccettazioneModule.BusinessObjects.Degenza` - 181 edges
2. `AccettazioneModule.BusinessObjects` - 176 edges
3. `Ricoveri` - 169 edges
4. `GlobalModule.BusinessObjects` - 125 edges
5. `BooleanEnum` - 114 edges
6. `AccettazioneModule.BusinessObjects.Runtime` - 103 edges
7. `Dipendenti` - 97 edges
8. `Rulli` - 88 edges
9. `SchedeRic` - 78 edges
10. `ContattiPz` - 71 edges

## Surprising Connections (you probably didn't know these)
- `Prenotazioni` --references--> `ClassePrioritaEnum`  [EXTRACTED]
  AccettazioneModule/BusinessObjects/Prenotazione/Prenotazioni.bo.cs → GlobalModule/Enumerations.cs
- `AltreProcedureEff` --references--> `Procedure`  [EXTRACTED]
  AccettazioneModule/BusinessObjects/AltreProcedureEff.bo.cs → GlobalClinModule/BusinessObjects/Procedure.bo.cs
- `AltreProcedureEff` --references--> `Medici`  [EXTRACTED]
  AccettazioneModule/BusinessObjects/AltreProcedureEff.bo.cs → GlobalModule/BusinessObjects/Medici.bo.cs
- `CategoriaIntervento` --references--> `BooleanEnum`  [EXTRACTED]
  AccettazioneModule/BusinessObjects/CategoriaIntervento.bo.cs → GlobalClinModule/Enumerations.cs
- `CategoriaIntervento` --references--> `Discipline`  [EXTRACTED]
  AccettazioneModule/BusinessObjects/CategoriaIntervento.bo.cs → GlobalModule/BusinessObjects/Discipline.bo.cs

## Import Cycles
- None detected.

## Communities (239 total, 9 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (23): DipendentiDaGlobalModule, ReportFatturazioneASP, DateTime, MediciDaGlobalModule, String, ModalitaDimissione, String, ProcedureDaGlobalModule (+15 more)

### Community 1 - "Community 1"
Cohesion: 0.07
Nodes (27): DettagliFarmacoMag, bool, int, Int32, String, UInt16, ushort, ATCL1Mag (+19 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (23): ContattiPz, bool, Boolean, DateTime, Int16, Int32, Single, String (+15 more)

### Community 3 - "Community 3"
Cohesion: 0.06
Nodes (34): PAI, DateTime, string, UInt16, ushort, XPCollection, AlimentazioneEnum, AusiliProtesiEnum (+26 more)

### Community 4 - "Community 4"
Cohesion: 0.08
Nodes (17): CheckListDimissione, String, EsamiLetteraDimissione, DateTime, String, LetteraDimissione, Boolean, DateTime (+9 more)

### Community 5 - "Community 5"
Cohesion: 0.06
Nodes (21): CategoriaIntervento, RefertoIntChir, bool, Boolean, Decimal, Double, String, UInt16 (+13 more)

### Community 6 - "Community 6"
Cohesion: 0.07
Nodes (18): ModalitaAccesso, String, DisdettaPrenotazione, String, Prenotazioni, bool, Boolean, DateTime (+10 more)

### Community 7 - "Community 7"
Cohesion: 0.06
Nodes (18): ProvaFiledata, FileData, Provenienze, String, UInt16, AccessiDH, Boolean, DateTime (+10 more)

### Community 8 - "Community 8"
Cohesion: 0.08
Nodes (18): GlobalClinModule, GlobalClinModule.BusinessObjects, Boolean, string, CIPI, string, ICD10_IM, double (+10 more)

### Community 9 - "Community 9"
Cohesion: 0.08
Nodes (17): Dicom_Nodes, string, UInt16, ushort, Dicom_PACS, string, uint, UInt16 (+9 more)

### Community 10 - "Community 10"
Cohesion: 0.08
Nodes (14): RefertoRXAmmissione, Modelli, string, Type, ProceduraReferto, Type, MedicazioneAmbienteProtetto, SangueOutCEC (+6 more)

### Community 11 - "Community 11"
Cohesion: 0.09
Nodes (15): AccettazioneModule.BusinessObjects.Degenza.LungoDegenza, GlobalModule.BusinessObjects, String, XPCollection, CategorieMedici, String, XPCollection, CategorieParamedici (+7 more)

### Community 12 - "Community 12"
Cohesion: 0.08
Nodes (16): CategoriaServizi, CategoriaVariabili, String, XPCollection, IntestazioniFirma, String, MyDashboards, Byte (+8 more)

### Community 13 - "Community 13"
Cohesion: 0.07
Nodes (20): LiquidiINPaziente, Boolean, DateTime, UInt32, CartellaCEC, DateTime, Double, Int32 (+12 more)

### Community 14 - "Community 14"
Cohesion: 0.07
Nodes (20): ParametriVitali, UInt16, ProtocolliRilevazione, bool, Boolean, DateTime, String, UInt16 (+12 more)

### Community 15 - "Community 15"
Cohesion: 0.09
Nodes (18): GlobalModule.BusinessObjects.GlobalClin, String, UInt16, ushort, XPCollection, CategorieProcedure, int, String (+10 more)

### Community 16 - "Community 16"
Cohesion: 0.07
Nodes (18): DosiEcoDobutamina, UInt16, ushort, AccessiVenosi, DateTime, String, CannuleCEC, String (+10 more)

### Community 17 - "Community 17"
Cohesion: 0.08
Nodes (9): DiarioClinicoFisiokinesiterapia, bool, Boolean, DiarioClinicoInfermieristico, bool, Boolean, TodoBoard, ICustomSave (+1 more)

### Community 18 - "Community 18"
Cohesion: 0.07
Nodes (18): AttivitaSuiPazienti, DateTime, EsamiRichiedibili, String, ImportEsamiXA, DateTime, RicoveratixSpecialista, bool (+10 more)

### Community 19 - "Community 19"
Cohesion: 0.08
Nodes (16): MediciHeartTeamTemp, Boolean, NonPersistentObject, IObjectSpace, String, RilevazioniTemp, DateTime, Double (+8 more)

### Community 20 - "Community 20"
Cohesion: 0.08
Nodes (17): String, UInt16, ASP, Int32, String, Comuni, Int32, String (+9 more)

### Community 21 - "Community 21"
Cohesion: 0.11
Nodes (14): ArticoliMag, String, XPCollection, CategorieMag, String, ClassiMag, String, PresidiArticoliMag (+6 more)

### Community 22 - "Community 22"
Cohesion: 0.07
Nodes (18): Casse, string, Fatture, bool, Boolean, DateTime, Decimal, Double (+10 more)

### Community 23 - "Community 23"
Cohesion: 0.08
Nodes (17): GruppiSanguigni, String, Parenti, String, XPCollection, Pazienti, bool, Boolean (+9 more)

### Community 24 - "Community 24"
Cohesion: 0.09
Nodes (18): PersistentRuleBaseProperties, bool, string, Type, PersistentRulePropertyValueProperties, string, PersistentRuleRangeProperties, ICollection (+10 more)

### Community 25 - "Community 25"
Cohesion: 0.09
Nodes (12): PropostaRicovRiabDH, DateTime, string, XPCollection, ValutazioneDoloreOrto, bool, Boolean, string (+4 more)

### Community 26 - "Community 26"
Cohesion: 0.09
Nodes (13): CloneIXPSimpleObjectHelper, Dictionary, Session, CoreTypes, EventArgs, Type, CloneObjectViewController, CustomizePopupWindowParamsEventArgs (+5 more)

### Community 27 - "Community 27"
Cohesion: 0.08
Nodes (15): RevisioniSchede, DateTime, FileData, FileSystemStoreObject, String, UInt16, Schede, bool (+7 more)

### Community 28 - "Community 28"
Cohesion: 0.09
Nodes (12): CartellaInfermieristica, Boolean, DateTime, NotifyCollectionChangedEventArgs, ObservableCollection, String, UInt16, ScalaDolore (+4 more)

### Community 29 - "Community 29"
Cohesion: 0.10
Nodes (11): FarmaciEsterni, string, UInt16, ushort, FarmaciPreanestesia, FarmaciTerapiaDimissione, String, VieSommFormFarm (+3 more)

### Community 30 - "Community 30"
Cohesion: 0.10
Nodes (15): BloccoPrenotazioni, DateTime, String, GiorniAmbulatorio, DateTime, string, UInt16, MediciAmbulatorioProgressivi (+7 more)

### Community 31 - "Community 31"
Cohesion: 0.09
Nodes (6): CertificatoCremazione, CertificatoNecroscopico, RefertoGenerico, IList, String, IModello

### Community 32 - "Community 32"
Cohesion: 0.09
Nodes (18): EcoDipiridamolo, float, Single, string, UInt16, ushort, XPCollection, EcoDobutamina (+10 more)

### Community 33 - "Community 33"
Cohesion: 0.09
Nodes (13): ArrivoTI, String, UInt16, DimissioneTI, Double, Single, String, UInt16 (+5 more)

### Community 34 - "Community 34"
Cohesion: 0.11
Nodes (13): ConsultoPrenatale, String, PrestazioniAmbulatoriali, DateTime, Int32, VisitaCardiologica, String, TestErgometrico (+5 more)

### Community 35 - "Community 35"
Cohesion: 0.09
Nodes (15): OrariPrescrizione, DateTime, RichiesteLaboratorio, bool, Boolean, DateTime, double, IList (+7 more)

### Community 36 - "Community 36"
Cohesion: 0.11
Nodes (15): LinkFieldsMdw, String, RefertiAmbMdw, DateTime, FileSystemStoreObject, string, RefertiMdw, Boolean (+7 more)

### Community 37 - "Community 37"
Cohesion: 0.13
Nodes (11): FKT, double, Single, String, UInt16, XPCollection, MobilitaArtiFKT, String (+3 more)

### Community 38 - "Community 38"
Cohesion: 0.09
Nodes (15): DettProgOp, DateTime, Int16, String, XPCollection, MediciProgOp, Color, Int32 (+7 more)

### Community 39 - "Community 39"
Cohesion: 0.10
Nodes (9): CheckListIngressoDH, bool, DateTime, string, XPCollection, ProfilassiTVP, UInt16, XPCollection (+1 more)

### Community 40 - "Community 40"
Cohesion: 0.10
Nodes (10): CheckListUscitaDH, bool, XPCollection, ValutazioneDolore, String, SchedeRic, Boolean, DateTime (+2 more)

### Community 41 - "Community 41"
Cohesion: 0.10
Nodes (11): RefertoECO, Boolean, Double, IList, Single, String, UInt16, EnumExtensions (+3 more)

### Community 42 - "Community 42"
Cohesion: 0.12
Nodes (11): AntibioticiEsamiBatteriologici, String, DettaglioEsamiBatteriologici, Int16, Single, EsitoMicrobiologico, String, ProtocolliLabVariabili (+3 more)

### Community 43 - "Community 43"
Cohesion: 0.12
Nodes (13): PresentiEvento, string, TipiEvento, TipoEvento, bool, Boolean, string, TipoPresentiEvento (+5 more)

### Community 44 - "Community 44"
Cohesion: 0.10
Nodes (16): Somministrazioni, bool, Boolean, DateTime, double, float, Int16, Int32 (+8 more)

### Community 45 - "Community 45"
Cohesion: 0.10
Nodes (18): RicoveratiReparto, DateTime, bool, Boolean, Color, DateTime, int, Int16 (+10 more)

### Community 46 - "Community 46"
Cohesion: 0.10
Nodes (13): IPersistentRuleCriteriaAttribute, IPersistentRuleRangeAttribute, PersistentCustomAttribute, AttributeInfoAttribute, string, PersistentRuleCriteriaAttribute, AttributeInfoAttribute, string (+5 more)

### Community 47 - "Community 47"
Cohesion: 0.13
Nodes (11): EsamiDiagEsterniPaziente, DateTime, String, Patologie, String, XPCollection, TipiFattoriRischio, String (+3 more)

### Community 48 - "Community 48"
Cohesion: 0.12
Nodes (13): BarthelIndex, String, UInt16, XPCollection, PrevInfezioneOsp, DateTime, string, XPCollection (+5 more)

### Community 49 - "Community 49"
Cohesion: 0.10
Nodes (10): RefertoCVG, Boolean, String, UInt16, VisitaAnestesiologicaPreoperatoria, DateTime, Double, ObservableCollection (+2 more)

### Community 50 - "Community 50"
Cohesion: 0.11
Nodes (8): DiarioClinico, Boolean, DateTime, String, DiarioClinicoMedico, bool, Boolean, String

### Community 51 - "Community 51"
Cohesion: 0.11
Nodes (11): LetteraDimissioneRiabFunz, Boolean, DateTime, short, String, XPCollection, ProgettoRiabilitativoPrescrizione, Boolean (+3 more)

### Community 52 - "Community 52"
Cohesion: 0.11
Nodes (13): RichiesteValutazioniEsami, bool, Boolean, DateTime, IList, String, uint, UInt32 (+5 more)

### Community 53 - "Community 53"
Cohesion: 0.11
Nodes (15): FarmaciPrescrizione, bool, Boolean, DateTime, decimal, float, IList, Single (+7 more)

### Community 54 - "Community 54"
Cohesion: 0.11
Nodes (15): IRilevazioni, DateTime, Double, UInt16, Variabili, bool, Boolean, DateTime (+7 more)

### Community 55 - "Community 55"
Cohesion: 0.11
Nodes (14): ProcedureSDO10, bool, Boolean, DateTime, UInt16, ushort, ProcedureSDO, bool (+6 more)

### Community 56 - "Community 56"
Cohesion: 0.11
Nodes (17): Ricoveri, bool, Boolean, DateTime, Double, IList, Int16, Int32 (+9 more)

### Community 57 - "Community 57"
Cohesion: 0.12
Nodes (10): ConsegneReparto, bool, Boolean, DateTime, String, String, XPCollection, Dislocazioni (+2 more)

### Community 58 - "Community 58"
Cohesion: 0.12
Nodes (11): RefertoAngiografico, Boolean, String, UInt16, EsamiDICOM, Boolean, DateTime, Int32 (+3 more)

### Community 59 - "Community 59"
Cohesion: 0.12
Nodes (15): Parametri, bool, Boolean, DateTime, Double, int, Int16, Session (+7 more)

### Community 60 - "Community 60"
Cohesion: 0.11
Nodes (11): Sdo, bool, Boolean, DateTime, ListChangedEventArgs, Single, String, UInt16 (+3 more)

### Community 61 - "Community 61"
Cohesion: 0.12
Nodes (10): RuleCriteriaPersistent, Dictionary, ICollection, Type, RuleRequiredFieldPersistent, Dictionary, ICollection, Type (+2 more)

### Community 62 - "Community 62"
Cohesion: 0.12
Nodes (10): String, XPCollection, RubricheICD9I, String, XPCollection, SezioniICD9I, String, XPCollection (+2 more)

### Community 63 - "Community 63"
Cohesion: 0.12
Nodes (10): RefertoGenericoRMN, String, XPCollection, Prestazioni, Double, Int32, String, UInt16 (+2 more)

### Community 64 - "Community 64"
Cohesion: 0.12
Nodes (8): EcoDopplerVascolare, String, EcgHolter, String, UInt16, ValutazionePsicologica, String, Medici&gt;

### Community 65 - "Community 65"
Cohesion: 0.12
Nodes (10): StoriaClinica, Boolean, DateTime, IList, Session, short, String, UInt16 (+2 more)

### Community 66 - "Community 66"
Cohesion: 0.12
Nodes (12): Prericoveri, bool, Boolean, DateTime, Int16, Int32, List, Session (+4 more)

### Community 67 - "Community 67"
Cohesion: 0.12
Nodes (11): Rad_esito, Boolean, DateTime, Single, UInt16, ushort, String, XPCollection (+3 more)

### Community 68 - "Community 68"
Cohesion: 0.12
Nodes (11): Certificati, Boolean, String, Richieste, Boolean, DateTime, String, TipoAltroRichiedenteEnum (+3 more)

### Community 69 - "Community 69"
Cohesion: 0.12
Nodes (9): AccettPropostaRicovero, string, XPCollection, PropostaRicovRiabCard, DateTime, string, XPCollection, EmotivitaEnum (+1 more)

### Community 70 - "Community 70"
Cohesion: 0.12
Nodes (10): VelocitaInfusionali, DateTime, decimal, Decimal, bool, Boolean, DateTime, decimal (+2 more)

### Community 71 - "Community 71"
Cohesion: 0.14
Nodes (9): ListaDiAttesaOperatore, Boolean, DateTime, Int32, ListChangedEventArgs, Object, String, XPCollection (+1 more)

### Community 72 - "Community 72"
Cohesion: 0.13
Nodes (11): PrenotazioniAmbulatorio, bool, Boolean, DateTime, int, Int32, Object, String (+3 more)

### Community 73 - "Community 73"
Cohesion: 0.14
Nodes (10): double, ConsumiProceduraMag, DateTime, Double, UInt16, MagRepartiMag, DateTime, Double (+2 more)

### Community 74 - "Community 74"
Cohesion: 0.13
Nodes (9): AllergieIntolleranze, String, AllergiePaziente, Boolean, DateTime, String, TipoAllergieEnum, TipoIntolleranzaEnum (+1 more)

### Community 75 - "Community 75"
Cohesion: 0.13
Nodes (8): AccettPropRicLgRiab, Boolean, string, XPCollection, PropostaRicLgRiab, DateTime, string, XPCollection

### Community 76 - "Community 76"
Cohesion: 0.13
Nodes (6): RefertoTAC, Boolean, IList, String, IEsameVarioTipo, IList

### Community 77 - "Community 77"
Cohesion: 0.13
Nodes (9): RichiesteSacche, bool, Boolean, DateTime, String, UInt16, ushort, XPCollection (+1 more)

### Community 78 - "Community 78"
Cohesion: 0.14
Nodes (8): DRGInfoDettDX, DRGInfoDettPX, GlobalFattModule, String, UInt16, DRG_DX_PX, DRGDXPXValEnum, TipoOperazioneIVAEnum

### Community 79 - "Community 79"
Cohesion: 0.13
Nodes (11): FattureASP, DateTime, Double, FileData, Int16, Int32, short, String (+3 more)

### Community 80 - "Community 80"
Cohesion: 0.13
Nodes (10): ProcedurePreviste, bool, Boolean, DateTime, int, Int32, String, UInt16 (+2 more)

### Community 81 - "Community 81"
Cohesion: 0.15
Nodes (8): ListaDiAttesa, Boolean, DateTime, Int32, ListChangedEventArgs, Object, String, XPCollection

### Community 82 - "Community 82"
Cohesion: 0.14
Nodes (9): DaysWeekProgOp, DateTime, XPCollection, SelWeekProgOp, Int16, WeekProgOp, Int16, String (+1 more)

### Community 83 - "Community 83"
Cohesion: 0.13
Nodes (10): DefinizioniTipoScheda, bool, Boolean, String, Type, UInt16, SchedeLock, DateTime (+2 more)

### Community 84 - "Community 84"
Cohesion: 0.14
Nodes (8): String, XPCollection, BlocchiICD9, String, XPCollection, CategorieICD9, String, XPCollection

### Community 85 - "Community 85"
Cohesion: 0.15
Nodes (10): bool, Boolean, Byte, DateTime, int, Int32, String, XPCollection (+2 more)

### Community 86 - "Community 86"
Cohesion: 0.15
Nodes (9): IList, String, XPCollection, Processi, RelazioneProcessi, String, XPCollection, SottoProcessi (+1 more)

### Community 87 - "Community 87"
Cohesion: 0.14
Nodes (7): FattoriRischio, Int32, String, FattoriRischioPaziente, DateTime, String, FattoriRischioDisciplina

### Community 88 - "Community 88"
Cohesion: 0.14
Nodes (10): DocumentiCartella, Int16, short, string, UInt16, XPCollection, StampaCartella, UInt16 (+2 more)

### Community 89 - "Community 89"
Cohesion: 0.14
Nodes (8): EsamiMicrobiologici, bool, Boolean, DateTime, String, UInt32, XPCollection, IAuthentication

### Community 90 - "Community 90"
Cohesion: 0.14
Nodes (9): TrasfusioniPaziente, bool, Boolean, DateTime, Double, Int16, String, UInt16 (+1 more)

### Community 91 - "Community 91"
Cohesion: 0.15
Nodes (10): EsamiDICOMnodef, DateTime, string, XPCollection, EsamiDICOMnodefDett, DateTime, Int16, short (+2 more)

### Community 92 - "Community 92"
Cohesion: 0.14
Nodes (8): ArticolixMarcaMagRep, Double, Int16, Int32, String, MarcheMag, String, XPCollection

### Community 93 - "Community 93"
Cohesion: 0.14
Nodes (9): ProgrammaOperatorio, Boolean, DateTime, Double, Int32, Object, String, UInt32 (+1 more)

### Community 94 - "Community 94"
Cohesion: 0.19
Nodes (10): PresenzeTirocini, DateTime, string, XPCollection, Tirocinanti, Boolean, DateTime, string (+2 more)

### Community 95 - "Community 95"
Cohesion: 0.15
Nodes (9): OsservazioniAnestesiologiche, Double, Int32, Single, String, uint, UInt16, UInt32 (+1 more)

### Community 96 - "Community 96"
Cohesion: 0.15
Nodes (7): TimingIntervento, Boolean, double, Session, string, XPCollection, ProcedurePreviste&gt;

### Community 97 - "Community 97"
Cohesion: 0.18
Nodes (4): ValutazioneFinaleRiabilitazione, Boolean, ValutazioniOltre7ggRiabilitazione, AccettazioneModule.BusinessObjects.Degenza.Riabilitazione

### Community 98 - "Community 98"
Cohesion: 0.15
Nodes (8): RiabilitazioneFunzionale, bool, DateTime, string, UInt16, ushort, XPCollection, ValutazioneFisiatricaEnum

### Community 99 - "Community 99"
Cohesion: 0.15
Nodes (11): ValutazioneRiabFunz, Boolean, string, UInt16, ushort, XPCollection, Ausili1Enum, Ausili2Enum (+3 more)

### Community 100 - "Community 100"
Cohesion: 0.17
Nodes (9): EventoAvverso, TrattamentiEnum, bool, Boolean, decimal, string, UInt16, ushort (+1 more)

### Community 101 - "Community 101"
Cohesion: 0.15
Nodes (9): FarmaciRicovero, bool, Boolean, Color, Int16, Int32, short, string (+1 more)

### Community 102 - "Community 102"
Cohesion: 0.17
Nodes (7): VociFattura, Boolean, DateTime, Double, Int16, String, XPCollection

### Community 103 - "Community 103"
Cohesion: 0.15
Nodes (7): PresidixMarcaMag, Double, Int16, Int32, String, UConfMag, String

### Community 104 - "Community 104"
Cohesion: 0.19
Nodes (6): IPrenotazioniRicoveri, PrenotazioniDayService, Boolean, PrenotazioniDH, AccettazioneModule.BusinessObjects.Prenotazione, MotivoDHEnum

### Community 105 - "Community 105"
Cohesion: 0.18
Nodes (5): FollowupChirurgico, DateTime, WeekProgOpInitialized, DateTime, AccettazioneModule.BusinessObjects.Ricovero.ProOp.Scheduler

### Community 106 - "Community 106"
Cohesion: 0.18
Nodes (7): GlobalFattModule.BusinessObjects, Int16, String, CodiciIVA, String, UInt16, RegioniDRG

### Community 107 - "Community 107"
Cohesion: 0.17
Nodes (8): InterventiPregressi, String, IntPregressiPaziente, Boolean, DateTime, String, UInt16, TipoInterventoEnum

### Community 108 - "Community 108"
Cohesion: 0.17
Nodes (7): AlertsRicovero, Dictionary, String, Type, UInt16, LivelloRicercaAlert, SortingDirection

### Community 109 - "Community 109"
Cohesion: 0.17
Nodes (5): RefertoRX, Boolean, IList, String, TipoRefertoRX

### Community 110 - "Community 110"
Cohesion: 0.18
Nodes (6): FarmaciTerapiaFarmacologica, String, TerapiaFarmacologica, String, UInt16, XPCollection

### Community 111 - "Community 111"
Cohesion: 0.17
Nodes (5): IndicazioniInterventistiche, bool, ObservableCollection, String, PropertyChangedEventArgs

### Community 112 - "Community 112"
Cohesion: 0.17
Nodes (8): ValutazioniGiornaliere, bool, Boolean, DateTime, Int16, short, string, XPCollection

### Community 113 - "Community 113"
Cohesion: 0.17
Nodes (6): RefertoElettrofisiologia, Boolean, string, UInt16, ushort, XPCollection

### Community 114 - "Community 114"
Cohesion: 0.18
Nodes (8): ValutazioneRiabilitazione, Boolean, DateTime, String, Type, UInt16, ushort, XPCollection

### Community 115 - "Community 115"
Cohesion: 0.17
Nodes (7): StoriaClinicaRiab, DateTime, short, string, UInt16, ushort, XPCollection

### Community 116 - "Community 116"
Cohesion: 0.18
Nodes (7): PresentiReparto, DateTime, UInt16, ushort, StatiPz, string, AccettazioneModule.BusinessObjects.Ricovero

### Community 117 - "Community 117"
Cohesion: 0.17
Nodes (10): RuntimeAppearanceRule, bool, Color, Dictionary, Int32, String, Type, FontStyle (+2 more)

### Community 118 - "Community 118"
Cohesion: 0.21
Nodes (6): GlobalModule.BusinessObjects.Qualita, FileData, Allegati, Bozze, DestinatariDocumento, StatiBozzaEnum

### Community 119 - "Community 119"
Cohesion: 0.17
Nodes (8): Boolean, DestinatariOrgDocumento, Boolean, String, XPCollection, Organigramma, IBindingList, ITreeNode

### Community 120 - "Community 120"
Cohesion: 0.18
Nodes (8): bool, Boolean, String, XPCollection, Documenti, String, XPCollection, TipoDocumenti

### Community 121 - "Community 121"
Cohesion: 0.18
Nodes (5): RefertoGenericoAmb, String, XPCollection, String, IntestFirmeDip

### Community 122 - "Community 122"
Cohesion: 0.18
Nodes (7): CategoriePaziente, String, Servizi, Int16, short, string, XPCollection

### Community 123 - "Community 123"
Cohesion: 0.20
Nodes (9): RiepilogoRicoveri, DateTime, double, int, Int16, Int32, short, string (+1 more)

### Community 124 - "Community 124"
Cohesion: 0.18
Nodes (8): VisitaPneumologica, FileData, Single, String, UInt16, UInt32, ObesitaAsmaAllergieEnum, TerapiaDiabeticaEnum

### Community 125 - "Community 125"
Cohesion: 0.18
Nodes (9): ProtocolliLaboratorio, bool, Boolean, DateTime, String, UInt16, ushort, GradoUrgenzaRichiestaLabEnum (+1 more)

### Community 126 - "Community 126"
Cohesion: 0.18
Nodes (8): Medicazioni, bool, Boolean, DateTime, string, XPCollection, DisinfettantiEnum, PresidiEnum

### Community 127 - "Community 127"
Cohesion: 0.18
Nodes (6): RefertoPTCA, Boolean, DateTime, String, UInt16, XPCollection

### Community 128 - "Community 128"
Cohesion: 0.18
Nodes (8): LetteraDimissioneRiabCard, Boolean, DateTime, short, string, UInt16, ushort, XPCollection

### Community 129 - "Community 129"
Cohesion: 0.18
Nodes (7): PlanningRiabilitazione, bool, Boolean, DateTime, String, UInt16, ushort

### Community 130 - "Community 130"
Cohesion: 0.20
Nodes (7): EventoFattori, string, FattoriEvento, TipoLegame, bool, Boolean, string

### Community 131 - "Community 131"
Cohesion: 0.18
Nodes (7): DiluenteFarmacoPrescritto, Single, XPCollection, UMSomministrazione, double, string, TipoUMEnum

### Community 132 - "Community 132"
Cohesion: 0.18
Nodes (6): Prescrizioni, bool, Boolean, DateTime, String, XPCollection

### Community 133 - "Community 133"
Cohesion: 0.22
Nodes (7): LogPrenAmb, DateTime, string, LogRicoveri, DateTime, string, AccettazioneModule.BusinessObjects.Logs

### Community 134 - "Community 134"
Cohesion: 0.18
Nodes (7): StatusLetti, DateTime, bool, String, UInt16, ushort, Discipline

### Community 135 - "Community 135"
Cohesion: 0.18
Nodes (7): DashboardsxUser, byte, DashboardData, Byte, Prova1, byte, String

### Community 136 - "Community 136"
Cohesion: 0.20
Nodes (7): GruppiSezione, String, XPCollection, SezioniCartella, String, UInt16, XPCollection

### Community 137 - "Community 137"
Cohesion: 0.18
Nodes (7): bool, Boolean, String, XPCollection, ICD9I_CM, String, XPCollection

### Community 138 - "Community 138"
Cohesion: 0.18
Nodes (7): String, UInt16, XPCollection, MDC, String, UInt16, XPCollection

### Community 139 - "Community 139"
Cohesion: 0.18
Nodes (10): ClassePrioritaEnum, MesiEnum, StatiDocEnum, StatoFSEEnum, TipoCompensoEnum, TipoDivulgazioneEnum, TipoFirma, TipoMagazzinoEnum (+2 more)

### Community 140 - "Community 140"
Cohesion: 0.22
Nodes (8): MediciAmbulatorio, int, Int32, String, UInt16, XPCollection, TipoFatturazioneAmb, BooleanEnum

### Community 141 - "Community 141"
Cohesion: 0.20
Nodes (6): TariffeAmbulatorio, Double, RicoveroAlerts, DateTime, double, String

### Community 142 - "Community 142"
Cohesion: 0.22
Nodes (5): String, DanniEvento, string, TipoDanno, string

### Community 143 - "Community 143"
Cohesion: 0.20
Nodes (5): RefertoRMN, IList, string, XPCollection, Prestazioni&gt;

### Community 144 - "Community 144"
Cohesion: 0.20
Nodes (6): EsameChimicoFisico, Boolean, string, UInt16, ushort, XPCollection

### Community 145 - "Community 145"
Cohesion: 0.20
Nodes (7): PrevenzioneRischioTrombo, bool, Boolean, Double, string, UInt16, XPCollection

### Community 146 - "Community 146"
Cohesion: 0.20
Nodes (7): TAVI, Boolean, Double, Session, String, UInt16, ValveInValveEnum

### Community 147 - "Community 147"
Cohesion: 0.20
Nodes (4): ProgettoRiabilitativoMultidisciplinare, DateTime, String, UInt16

### Community 148 - "Community 148"
Cohesion: 0.20
Nodes (6): ProgettoRiabilitativoRilevazioni, Boolean, DateTime, String, XPCollection, PeriodoEnum

### Community 149 - "Community 149"
Cohesion: 0.20
Nodes (6): AzioniEvento, bool, Boolean, string, EventoAzioni, string

### Community 150 - "Community 150"
Cohesion: 0.20
Nodes (6): EventoPrevenzione, string, FattoriPrevenzione, bool, Boolean, string

### Community 151 - "Community 151"
Cohesion: 0.24
Nodes (5): Assicurazioni, String, DrgxArea, string, AccettazioneModule.BusinessObjects.Fatturazione

### Community 152 - "Community 152"
Cohesion: 0.20
Nodes (7): ArticolixFornitoreMag, Double, Int16, Int32, Single, String, TipoOrdine

### Community 153 - "Community 153"
Cohesion: 0.20
Nodes (8): String, UInt16, XPCollection, DRG, Double, Single, String, UInt16

### Community 154 - "Community 154"
Cohesion: 0.20
Nodes (6): String, UInt16, XPCollection, Camere, String, TipoCamera

### Community 155 - "Community 155"
Cohesion: 0.22
Nodes (6): String, XPCollection, CategorieTecAmm, String, XPCollection, TecnicoAmministrativi

### Community 156 - "Community 156"
Cohesion: 0.20
Nodes (7): Boolean, DateTime, FileData, Int16, String, XPCollection, RevisioniDocumento

### Community 157 - "Community 157"
Cohesion: 0.22
Nodes (6): String, XPCollection, Specializzazioni, String, XPCollection, TipoDipendenti

### Community 158 - "Community 158"
Cohesion: 0.22
Nodes (5): Presidi, String, PresidiPaziente, DateTime, String

### Community 159 - "Community 159"
Cohesion: 0.22
Nodes (6): CalcoloRischio, Boolean, Double, float, Single, UInt16

### Community 160 - "Community 160"
Cohesion: 0.22
Nodes (6): Consegnetemp, Boolean, DateTime, string, ValidaConsegneInf, IList

### Community 161 - "Community 161"
Cohesion: 0.22
Nodes (3): Consulenza, IList, String

### Community 162 - "Community 162"
Cohesion: 0.22
Nodes (4): EsamiBatteriologici, DateTime, String, XPCollection

### Community 163 - "Community 163"
Cohesion: 0.22
Nodes (6): RefertoPTA, Boolean, DateTime, String, UInt16, XPCollection

### Community 164 - "Community 164"
Cohesion: 0.22
Nodes (5): ArticolixMarcaMag, Double, Int16, Int32, String

### Community 165 - "Community 165"
Cohesion: 0.22
Nodes (5): MotiviRinvio, String, Rinvii, Boolean, DateTime

### Community 166 - "Community 166"
Cohesion: 0.22
Nodes (6): RichiesteDocumentazione, Boolean, DateTime, String, XPCollection, TipoDocumentazioneEnum

### Community 167 - "Community 167"
Cohesion: 0.22
Nodes (4): Operatori, XPCollection, SaleOpResource, Resource

### Community 168 - "Community 168"
Cohesion: 0.28
Nodes (7): sdo_R, PosDiagPrimaSecEnum, PosDiagSecEnum, bool, Boolean, short, string

### Community 169 - "Community 169"
Cohesion: 0.22
Nodes (5): TrasferimentiLetto, Boolean, DateTime, String, XPCollection

### Community 170 - "Community 170"
Cohesion: 0.25
Nodes (3): RiepilogoCVG, string, AccettazioneModule.BusinessObjects.Statistiche

### Community 171 - "Community 171"
Cohesion: 0.22
Nodes (5): String, XPCollection, CapitoliICD9, String, XPCollection

### Community 172 - "Community 172"
Cohesion: 0.22
Nodes (5): String, XPCollection, SottoRubricheICD9I, String, XPCollection

### Community 173 - "Community 173"
Cohesion: 0.22
Nodes (5): String, FunzioniOrganigramma, String, XPCollection, MembriOrganigramma

### Community 174 - "Community 174"
Cohesion: 0.25
Nodes (5): PatologiePaziente, Boolean, DateTime, String, gradoPatologiaEnum

### Community 175 - "Community 175"
Cohesion: 0.25
Nodes (4): SchedeAnamnesi, Dictionary, String, Type

### Community 176 - "Community 176"
Cohesion: 0.25
Nodes (5): AllegatiCC, bool, DateTime, FileSystemStoreObject, string

### Community 177 - "Community 177"
Cohesion: 0.25
Nodes (5): RefertiLaboratorio, Boolean, DateTime, FileSystemStoreObject, String

### Community 178 - "Community 178"
Cohesion: 0.25
Nodes (3): SchedaAntibioticoProfilassi, DateTime, String

### Community 179 - "Community 179"
Cohesion: 0.25
Nodes (4): ProgettoRiabilitativoRiepilogo, DateTime, string, XPCollection

### Community 180 - "Community 180"
Cohesion: 0.25
Nodes (6): DosiPrescrizione, bool, Boolean, DateTime, Single, string

### Community 181 - "Community 181"
Cohesion: 0.25
Nodes (4): DRGInfo, Double, Int32, XPCollection

### Community 182 - "Community 182"
Cohesion: 0.25
Nodes (5): TabulatiCassa, DateTime, FileSystemStoreObject, String, XPCollection

### Community 183 - "Community 183"
Cohesion: 0.25
Nodes (5): Sdo10, bool, Boolean, ListChangedEventArgs, XPCollection

### Community 184 - "Community 184"
Cohesion: 0.25
Nodes (4): DefinizioniSchede, String, Type, PersistentClassInfo

### Community 185 - "Community 185"
Cohesion: 0.25
Nodes (8): RiepilogoTAVI, DateTime, double, float, Single, string, UInt16, ushort

### Community 186 - "Community 186"
Cohesion: 0.29
Nodes (4): ControlloChirurgico, DateTime, string, XPCollection

### Community 187 - "Community 187"
Cohesion: 0.29
Nodes (5): RefertiOnline, DateTime, FileSystemStoreObject, string, UnitOfWork

### Community 188 - "Community 188"
Cohesion: 0.29
Nodes (5): DettaglioPreanestesia, DateTime, IList, Int16, UMSomministrazione&gt;

### Community 191 - "Community 191"
Cohesion: 0.29
Nodes (4): ICF, string, XPCollection, StadiazioneCondensataEnum

### Community 192 - "Community 192"
Cohesion: 0.29
Nodes (5): CentriRicavo, string, UInt16, ushort, XPCollection

### Community 193 - "Community 193"
Cohesion: 0.29
Nodes (6): FattureAssicurazioni, Boolean, DateTime, decimal, double, string

### Community 194 - "Community 194"
Cohesion: 0.33
Nodes (5): ParametriFSE, string, UInt16, ushort, AccettazioneModule.BusinessObjects.FSE

### Community 195 - "Community 195"
Cohesion: 0.29
Nodes (6): IConfirmationAsked, MyConfirmationEventArgs, bool, ConfirmationResult, ConfirmationType, EventArgs

### Community 196 - "Community 196"
Cohesion: 0.29
Nodes (5): Eslab, double, int, Int32, string

### Community 197 - "Community 197"
Cohesion: 0.29
Nodes (5): PersistentCalculatedType, string, DBColumnType, IPersistentCoreTypeMemberInfo, PersistentMemberInfo

### Community 198 - "Community 198"
Cohesion: 0.29
Nodes (4): ColorValueConverter, Type, AccettazioneModule, ValueConverter

### Community 199 - "Community 199"
Cohesion: 0.29
Nodes (3): String, Diagnosi, String

### Community 200 - "Community 200"
Cohesion: 0.33
Nodes (4): Boards, Color, Int32, string

### Community 201 - "Community 201"
Cohesion: 0.33
Nodes (4): ConsulenzaNefrologica, Single, String, UInt16

### Community 202 - "Community 202"
Cohesion: 0.33
Nodes (4): EmogasCEC, DateTime, Single, UInt16

### Community 203 - "Community 203"
Cohesion: 0.33
Nodes (3): Preanestesia, XPCollection, ArticoliMag&gt;

### Community 204 - "Community 204"
Cohesion: 0.33
Nodes (4): SangueInCEC, DateTime, String, UInt16

### Community 205 - "Community 205"
Cohesion: 0.33
Nodes (3): VasiPTCA, String, UInt16

### Community 206 - "Community 206"
Cohesion: 0.33
Nodes (4): RepartiDegenza, DateTime, String, XPCollection

### Community 207 - "Community 207"
Cohesion: 0.33
Nodes (4): RiepilogoProcedure, Boolean, DateTime, UInt16

### Community 208 - "Community 208"
Cohesion: 0.33
Nodes (4): LuogoEvento, bool, Boolean, string

### Community 209 - "Community 209"
Cohesion: 0.33
Nodes (4): PrestazioneEvento, bool, Boolean, string

### Community 210 - "Community 210"
Cohesion: 0.33
Nodes (4): EsameDICOMDett, DateTime, Int16, String

### Community 211 - "Community 211"
Cohesion: 0.33
Nodes (4): GradiUrgenza, Color, Int32, String

### Community 212 - "Community 212"
Cohesion: 0.33
Nodes (3): PrenotazioniPreRic, Boolean, DateTime

### Community 213 - "Community 213"
Cohesion: 0.33
Nodes (4): ProtocolliPrescrizione, DateTime, String, UInt16

### Community 214 - "Community 214"
Cohesion: 0.33
Nodes (6): RiepilogoCCH, DateTime, double, string, UInt16, ushort

### Community 215 - "Community 215"
Cohesion: 0.33
Nodes (3): FileSystemStoreObjectGlobal, string, LinkedDoc

### Community 216 - "Community 216"
Cohesion: 0.33
Nodes (4): DateTime, Double, String, TariffariDRG

### Community 217 - "Community 217"
Cohesion: 0.40
Nodes (3): AltreProcedureEff, bool, Boolean

### Community 218 - "Community 218"
Cohesion: 0.40
Nodes (3): EsamiRichiesta, Int32, string

### Community 219 - "Community 219"
Cohesion: 0.40
Nodes (3): LiquidiOutCEC, DateTime, UInt32

### Community 220 - "Community 220"
Cohesion: 0.40
Nodes (3): ParametriCEC, DateTime, Single

### Community 221 - "Community 221"
Cohesion: 0.40
Nodes (3): VasiPTA, String, UInt16

### Community 222 - "Community 222"
Cohesion: 0.50
Nodes (3): EsitiEvento, TipoEsitoEvento, string

### Community 225 - "Community 225"
Cohesion: 0.50
Nodes (3): ChecklistSO, string, AccettazioneModule.BusinessObjects.Ricovero.ProOp

### Community 226 - "Community 226"
Cohesion: 0.40
Nodes (4): ProgOpWeek, DateTime, String, TipoCasellaPzEnum

### Community 228 - "Community 228"
Cohesion: 0.40
Nodes (3): ClasseNYHA, Int16, String

### Community 229 - "Community 229"
Cohesion: 0.40
Nodes (3): StatoPostOp, Int16, String

### Community 230 - "Community 230"
Cohesion: 0.40
Nodes (3): String, UInt16, ErroriGrouper

### Community 231 - "Community 231"
Cohesion: 0.40
Nodes (3): String, UInt16, SubClass

### Community 232 - "Community 232"
Cohesion: 0.40
Nodes (3): DateTime, String, DistribuzioneDocumenti

### Community 233 - "Community 233"
Cohesion: 0.40
Nodes (3): XPCollection, ProcessiTipoDocumento, TipoDocumentoProcessoEnum

## Knowledge Gaps
- **25 isolated node(s):** `IgieneEnum`, `RiposoEnum`, `RespirazioneEnum`, `AlimentazioneEnum`, `EliminazioneUrinariaEnum` (+20 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Ricoveri` connect `Community 56` to `Community 0`, `Community 2`, `Community 132`, `Community 133`, `Community 6`, `Community 5`, `Community 7`, `Community 136`, `Community 134`, `Community 139`, `Community 140`, `Community 13`, `Community 14`, `Community 16`, `Community 17`, `Community 148`, `Community 20`, `Community 23`, `Community 153`, `Community 28`, `Community 32`, `Community 35`, `Community 36`, `Community 40`, `Community 169`, `Community 44`, `Community 45`, `Community 176`, `Community 177`, `Community 50`, `Community 52`, `Community 57`, `Community 60`, `Community 189`, `Community 192`, `Community 66`, `Community 68`, `Community 70`, `Community 199`, `Community 77`, `Community 207`, `Community 79`, `Community 80`, `Community 85`, `Community 88`, `Community 89`, `Community 90`, `Community 227`, `Community 101`, `Community 237`, `Community 112`, `Community 123`, `Community 126`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Why does `SchedeRic` connect `Community 40` to `Community 2`, `Community 66`, `Community 70`, `Community 136`, `Community 140`, `Community 56`, `Community 27`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._
- **Why does `ContattiPz` connect `Community 2` to `Community 0`, `Community 32`, `Community 58`, `Community 7`, `Community 74`, `Community 107`, `Community 140`, `Community 141`, `Community 174`, `Community 47`, `Community 17`, `Community 23`, `Community 20`, `Community 22`, `Community 87`, `Community 85`, `Community 122`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **What connects `IgieneEnum`, `RiposoEnum`, `RespirazioneEnum` to the rest of the system?**
  _25 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.05142857142857143 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.07087486157253599 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._