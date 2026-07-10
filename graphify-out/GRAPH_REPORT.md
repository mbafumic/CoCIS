# Graph Report - C:\Users\OMONAC~1.DRO\AppData\Local\Temp\claude\c--Users-OMONACO-DROMONACO-CoCIS\72dad8ad-6bab-4f4f-8cd3-76fa10315bfa\scratchpad\cocis_schema  (2026-07-10)

## Corpus Check
- 1 files · ~94,305 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 751 nodes · 1245 edges · 176 communities (35 shown, 141 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Magazzino & Approvvigionamento
- Farmacia - Catalogo Farmaci (ATC)
- Programmazione Sala Operatoria
- Anagrafica Paziente
- Accettazione & Ricovero
- Fatturazione & Ambulatorio
- Cartella Clinica - Diario
- Referti & Consulti
- DevExpress XPO - Metadata Attributi
- Esami Diagnostici & Certificati
- Parametri Vitali & Protocolli Lab
- Gestione Documentale
- DevExpress XPO - Metadata Classi
- DevExpress - Permessi (Policy)
- DevExpress - Sicurezza & Audit
- Cartella Cardiochirurgia (CEC)
- Anagrafica Generica (Party Model)
- Cartella Infermieristica - Dimissione TI
- Microbiologia & Laboratorio
- DevExpress - Reporting & Dashboard
- DevExpress - Audit Trail
- Lettera di Dimissione & Riabilitazione
- DRG - Classificazione Ricoveri
- Codifica Procedure ICD9-CM
- Codifica Diagnosi ICD9/ICD10
- Gestione Posti Letto
- Risk Management - Eventi Avversi
- DevExpress - Utenti & Ruoli
- DevExpress XPO - Metadata Collezioni
- KPI & Scorecard
- SDO - Scheda Dimissione Ospedaliera
- Fisiokinesiterapia (FKT)
- DevExpress XPO - State Machine
- Esami Batteriologici
- Terapia Farmacologica
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

## God Nodes (most connected - your core abstractions)
1. `dipendenti` - 92 edges
2. `schederic` - 76 edges
3. `ricoveri` - 70 edges
4. `reparti` - 59 edges
5. `presidiosp` - 43 edges
6. `xpobjecttype` - 35 edges
7. `medici` - 32 edges
8. `contattipz` - 29 edges
9. `fornitori` - 27 edges
10. `procedureeffettuate` - 27 edges

## Surprising Connections (you probably didn't know these)
- `accessidh` --references--> `ricoveri`  [EXTRACTED]
  C:/Users/OMONACO.DROMONACO/CoCIS/cocisdb_vuoto.sql → C:/Users/OMONACO.DROMONACO/CoCIS/cocisdb_vuoto.sql  _Bridges community 23 → community 6_
- `alertsricovero` --references--> `reparti`  [EXTRACTED]
  C:/Users/OMONACO.DROMONACO/CoCIS/cocisdb_vuoto.sql → C:/Users/OMONACO.DROMONACO/CoCIS/cocisdb_vuoto.sql  _Bridges community 10 → community 0_
- `allegaticc` --references--> `ricoveri`  [EXTRACTED]
  C:/Users/OMONACO.DROMONACO/CoCIS/cocisdb_vuoto.sql → C:/Users/OMONACO.DROMONACO/CoCIS/cocisdb_vuoto.sql  _Bridges community 7 → community 6_
- `allergiepaziente` --references--> `principiattivi`  [EXTRACTED]
  C:/Users/OMONACO.DROMONACO/CoCIS/cocisdb_vuoto.sql → C:/Users/OMONACO.DROMONACO/CoCIS/cocisdb_vuoto.sql  _Bridges community 3 → community 1_
- `articoli` --references--> `xpobjecttype`  [EXTRACTED]
  C:/Users/OMONACO.DROMONACO/CoCIS/cocisdb_vuoto.sql → C:/Users/OMONACO.DROMONACO/CoCIS/cocisdb_vuoto.sql  _Bridges community 1 → community 19_

## Import Cycles
- None detected.

## Communities (176 total, 141 thin omitted)

### Community 0 - "Magazzino & Approvvigionamento"
Cohesion: 0.05
Nodes (105): affiancamenti, altricarichi, articolixfornitore, articolixmarca, barcodesarticoli, calendariorichiestemag, carichi, carichiordservizio (+97 more)

### Community 1 - "Farmacia - Catalogo Farmaci (ATC)"
Cohesion: 0.07
Nodes (45): articoli, atcl1, atcl2, atcl3, atcl4, atcl5, categorie, categorieprodottiservice (+37 more)

### Community 2 - "Programmazione Sala Operatoria"
Cohesion: 0.08
Nodes (43): altreprocedureeff, altreprocedureeffmag, categorieprocedure, codiciiva, consumiprocedura, daysweekprogop, dettprogop, disdettaprenotazione (+35 more)

### Community 3 - "Anagrafica Paziente"
Cohesion: 0.07
Nodes (41): allergieintolleranze, allergiepaziente, altridatipz, asp, categoriepaziente, comuni, contatti, contattipz (+33 more)

### Community 4 - "Accettazione & Ricovero"
Cohesion: 0.06
Nodes (31): accessivenosi, accettpropostaricovero, accettpropriclgriab, arrivoti, barthelindex, checklistingressodh, checklistso, checklistuscitadh (+23 more)

### Community 5 - "Fatturazione & Ambulatorio"
Cohesion: 0.09
Nodes (28): bloccoprenotazioni, casse, definizionitiposcheda, event, farmaciricovero, fatture, fattureassicurazioni, giorniambulatorio (+20 more)

### Community 6 - "Cartella Clinica - Diario"
Cohesion: 0.11
Nodes (22): consegnetemp, diarioclinico, diarioclinicofisiokinesiterapia, diarioclinicoinfermieristico, diarioclinicomedico, liquidiinpaziente, medicazioni, modalitadimissione (+14 more)

### Community 7 - "Referti & Consulti"
Cohesion: 0.13
Nodes (21): allegaticc, consultoprenatale, controllochirurgico, filesystemstoreobject, prestazioniambulatoriali, refertimdw, refertionline, refertogenericoamb (+13 more)

### Community 8 - "DevExpress XPO - Metadata Attributi"
Cohesion: 0.11
Nodes (19): persistentaggregatedattribute, persistentattributeinfo, persistentcustomattribute, persistentdefaultclassoptionsattribute, persistentkeyattribute, persistentmapinheritanceattribute, persistentmodeldefaultattribute, persistentpersistentaliasattribute (+11 more)

### Community 9 - "Esami Diagnostici & Certificati"
Cohesion: 0.15
Nodes (18): certificatocremazione, certificatonecroscopico, dosiecodobutamina, ecodipiridamolo, ecodobutamina, esamedicomdett, esamidicom, refertoangiografico (+10 more)

### Community 10 - "Parametri Vitali & Protocolli Lab"
Cohesion: 0.15
Nodes (17): alertsricovero, categoriavariabili, discipline, esamirichiesta, parametrivitali, propostariclgriab, protocollilaboratorio, protocollilabvariabili (+9 more)

### Community 11 - "Gestione Documentale"
Cohesion: 0.16
Nodes (17): allegati, bozze, destinataridocumento, destinatariorgdocumento, documenti, documentiprocesso, filesystemstoreobjectglobal, linkeddoc (+9 more)

### Community 12 - "DevExpress XPO - Metadata Classi"
Cohesion: 0.16
Nodes (17): classescheda, interfaceinfo, persistentassemblyattributeinfo, persistentassemblydatastoreattribute, persistentassemblydatastoreattributeinfo, persistentassemblyinfo, persistentassemblyversionattributeinfo, persistentassociationattribute (+9 more)

### Community 13 - "DevExpress - Permessi (Policy)"
Cohesion: 0.12
Nodes (16): additionalviewcontrolsoperationpermissionpolicydata, anonymousloginoperationpermissionpolicydata, audittrailoperationpermissionpolicypolicydata, devexpress_persistent_baseimpl_permissionpolicy_permiss_55bc50f0, mydetailsoperationpermissionpolicydata, permissionpolicyactionpermissionobject, permissionpolicydata, permissionpolicymemberpermissionsobject (+8 more)

### Community 14 - "DevExpress - Sicurezza & Audit"
Cohesion: 0.14
Nodes (15): anonymousloginoperationpermissiondata, audittrailoperationpermissiondata, dashboarddefinition, devexpress_expressapp_security_strategy_securitysystemr_aace67df, mydetailsoperationpermissiondata, roledashboarddefinitiondashboarddefinitions, securitysystemmemberpermissionsobject, securitysystemobjectpermissionsobject (+7 more)

### Community 15 - "Cartella Cardiochirurgia (CEC)"
Cohesion: 0.15
Nodes (13): calcolorischio, cannulecec, cardioplegia, cartellacec, emogascec, farmacicec, liquidioutcec, osservazionianestesiologiche (+5 more)

### Community 16 - "Anagrafica Generica (Party Model)"
Cohesion: 0.17
Nodes (12): address, country, organization, party, persistentpermission, person, phonenumber, role (+4 more)

### Community 17 - "Cartella Infermieristica - Dimissione TI"
Cohesion: 0.17
Nodes (12): cartellainfermieristica, categoriaintervento, dimissioneti, ecodopplervascolare, esamidiagesternipaziente, refertointchir, rulli, schedaantibioticoprofilassi (+4 more)

### Community 18 - "Microbiologia & Laboratorio"
Cohesion: 0.18
Nodes (12): certificati, esamimicrobiologici, esitomicrobiologico, modalitaaccesso, prericoveri, provenienze, refertilaboratorio, richieste (+4 more)

### Community 19 - "DevExpress - Reporting & Dashboard"
Cohesion: 0.20
Nodes (11): codetemplate, codetemplateinfo, dashboarddata, persistentrulebaseproperties, persistentrulerangeproperties, persistenttypeinfo, reportdatav2, reportfatturazioneasp (+3 more)

### Community 20 - "DevExpress - Audit Trail"
Cohesion: 0.24
Nodes (10): auditdataitempersistent, auditedobjectweakreference, propertybag, propertybagdescriptor, propertydescriptor, propertydescriptorpropertydescriptors_propertybagdescri_3ef9c1ed, propertyvalue, xpandauditdataitempersistent (+2 more)

### Community 21 - "Lettera di Dimissione & Riabilitazione"
Cohesion: 0.22
Nodes (9): checklistdimissione, esamiletteradimissione, intestfirmedip, letteradimissione, letteradimissioneriabcard, letteradimissioneriabfunz, procedureletteradimissione, progettoriabilitativorilevazioni (+1 more)

### Community 22 - "DRG - Classificazione Ricoveri"
Cohesion: 0.25
Nodes (9): drg, drg_dx_px, drginfo, drginfodettdx, drginfodettpx, errorigrouper, mdc, subclass (+1 more)

### Community 23 - "Codifica Procedure ICD9-CM"
Cohesion: 0.25
Nodes (8): accessidh, cipi, icd9i_cm, riepilogoprocedure, rubricheicd9i, sezionicipi, sezioniicd9i, sottorubricheicd9i

### Community 24 - "Codifica Diagnosi ICD9/ICD10"
Cohesion: 0.29
Nodes (7): blocchiicd9, capitoliicd9, categorieicd9, diagnosi, icd10_im, icd10_im_old, icd9_cm

### Community 25 - "Gestione Posti Letto"
Cohesion: 0.29
Nodes (7): camere, consegnereparto, dislocazioni, letti, statusletti, tipocamera, trasferimentiletto

### Community 26 - "Risk Management - Eventi Avversi"
Cohesion: 0.29
Nodes (7): dannievento, eventoavverso, eventoazioni, eventofattori, eventoprevenzione, presentievento, tipievento

### Community 27 - "DevExpress - Utenti & Ruoli"
Cohesion: 0.29
Nodes (7): permissiondata, permissionscontainer, securitystrategyrole, securityuser, securityuserbase, securityuserwithrolesbase, securityuserwithrolesbaseusers_securitystrategyroleroles

### Community 28 - "DevExpress XPO - Metadata Collezioni"
Cohesion: 0.40
Nodes (5): extendedcollectionmemberinfo, extendedcoretypememberinfo, extendedmemberinfo, extendedorphanedcollection, extendedreferencememberinfo

### Community 29 - "KPI & Scorecard"
Cohesion: 0.50
Nodes (5): kpidefinition, kpihistoryitem, kpiinstance, kpiscorecard, kpiscorecardscorecards_kpiinstanceindicators

### Community 30 - "SDO - Scheda Dimissione Ospedaliera"
Cohesion: 0.40
Nodes (5): oneridegenza, proceduresdo, proceduresdo10, sdo, sdo10

### Community 31 - "Fisiokinesiterapia (FKT)"
Cohesion: 0.67
Nodes (4): fkt, mobilitaartifkt, rxtoracefkt, valutazionemobilitafkt

### Community 32 - "DevExpress XPO - State Machine"
Cohesion: 0.67
Nodes (4): xpostate, xpostateappearance, xpostatemachine, xpotransition

### Community 33 - "Esami Batteriologici"
Cohesion: 0.67
Nodes (3): antibioticiesamibatteriologici, dettaglioesamibatteriologici, esamibatteriologici

### Community 34 - "Terapia Farmacologica"
Cohesion: 0.67
Nodes (3): farmaciterapiadimissione, farmaciterapiafarmacologica, terapiafarmacologica

## Knowledge Gaps
- **321 isolated node(s):** `accessivenosi`, `accettpropostaricovero`, `accettpropriclgriab`, `additionalviewcontrolsoperationpermissionpolicydata`, `allegati` (+316 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **141 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ricoveri` connect `Cartella Clinica - Diario` to `Magazzino & Approvvigionamento`, `Farmacia - Catalogo Farmaci (ATC)`, `Programmazione Sala Operatoria`, `Anagrafica Paziente`, `Parametri Vitali & Protocolli Lab`, `Cartella Infermieristica - Dimissione TI`, `Microbiologia & Laboratorio`, `DRG - Classificazione Ricoveri`, `Codifica Diagnosi ICD9/ICD10`, `Gestione Posti Letto`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **Why does `schederic` connect `Accettazione & Ricovero` to `Programmazione Sala Operatoria`, `Fatturazione & Ambulatorio`, `Cartella Clinica - Diario`, `Referti & Consulti`, `Microbiologia & Laboratorio`?**
  _High betweenness centrality (0.012) - this node is a cross-community bridge._
- **Why does `contattipz` connect `Anagrafica Paziente` to `Magazzino & Approvvigionamento`, `DevExpress - Reporting & Dashboard`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **What connects `accessivenosi`, `accettpropostaricovero`, `accettpropriclgriab` to the rest of the system?**
  _321 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Magazzino & Approvvigionamento` be split into smaller, more focused modules?**
  _Cohesion score 0.051648351648351645 - nodes in this community are weakly interconnected._
- **Should `Farmacia - Catalogo Farmaci (ATC)` be split into smaller, more focused modules?**
  _Cohesion score 0.07474747474747474 - nodes in this community are weakly interconnected._
- **Should `Programmazione Sala Operatoria` be split into smaller, more focused modules?**
  _Cohesion score 0.07751937984496124 - nodes in this community are weakly interconnected._