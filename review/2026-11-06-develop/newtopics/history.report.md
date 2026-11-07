# New-topic report: history

Status: DONE. 23 new topics written, 16 proposed edges into existing topics.

## 1. Syllabi compared against

| Course | Syllabus compared against |
|---|---|
| ancient-civilizations | Standard world-history survey textbooks, "foundations" chapters (to c. 600 CE): e.g. Bentley & Ziegler, *Traditions & Encounters*; Strayer, *Ways of the World*. (AP World History: Modern starts at 1200 CE, so the textbook table of contents is the reference here.) |
| medieval-world | AP World History: Modern CED, Unit 1 (The Global Tapestry, 1200-1450) and Unit 2 (Networks of Exchange). AP European History has no pre-1450 unit. |
| early-modern-period | AP World Units 3-4 (Land-Based Empires; Transoceanic Interconnections, 1450-1750) and the opening topics of Unit 5 (Enlightenment; Nationalism and Revolutions); AP European History Units 1-5 (to 1815); AP US History Periods 1-3 (1491-1800). |
| modern-history | AP World Units 5-9 (1750-present); AP European History Units 6-9; AP US History Periods 4-9 (1800-present). |
| then-and-now, historical-methods, historiography, history-of-science, economic-social-history | Not survey courses. Coverage is dense (often duplicated), so no gaps proposed. |

Method: read every `title:` line in `domains/history/` (about 700 topics), then grepped the whole `domains/` tree (titles and bodies) for the key names of each candidate unit before writing it.

Note on placement: the domain has no US history course. APUSH gaps were placed in `early-modern-period` (to 1800) and `modern-history` (after 1800), matching where `american-revolution` and `civil-rights-movement` already sit.

## 2. New topics

| new id | course | why it is a gap (syllabus unit) | prerequisites |
|---|---|---|---|
| greco-persian-wars | ancient-civilizations | Textbook classical-Greece chapter: Persian Wars (Marathon, Thermopylae, Salamis, Delian League). No topic. Only a passing mention of Thermopylae in a historiography topic. | persian-empire (hard), ancient-greece-polis (hard), athenian-democracy-origins (soft) |
| maurya-and-gupta-empires | ancient-civilizations | Textbook "Classical India" chapter (Maurya, Ashoka, Gupta). No topic anywhere mentions Maurya, Ashoka or Gupta. | origins-of-world-religions, indus-valley-civilization, hellenistic-period, persian-empire (all soft) |
| rise-of-christianity-roman-empire | ancient-civilizations | Textbook Rome chapter: early Christianity, persecution, Constantine, Theodosius. origins-of-world-religions covers the Axial Age only, not Christianity's spread. | roman-empire-rise (hard); origins-of-world-religions, ancient-mystery-religions-cults, hellenistic-period (soft) |
| olmec-and-maya-civilizations | ancient-civilizations | Textbook "Early Americas" chapter. No history topic on the Olmec or Maya (only an art-history topic on Mesoamerican visual expression). | ancient-civilization-characteristics, ancient-urbanization, ancient-writing-systems-comparison (soft) |
| kingdoms-of-kush-and-aksum | ancient-civilizations | Textbook "Early African civilizations" (Kush, Meroë, Aksum). No mention of Kush, Meroë or Aksum anywhere in the graph. | egyptian-civilization, new-kingdom-egypt, iron-age-metalworking-technology, ancient-world-trade-networks (soft) |
| aztec-mexica-empire | medieval-world | AP World 1.4 (State Building in the Americas): Mexica. Only incidental mentions of Tenochtitlan in conquest topics. | olmec-and-maya-civilizations, ancient-urbanization (soft) |
| inca-empire | medieval-world | AP World 1.4: Inca, mit'a, khipu. No topic. | ancient-civilization-characteristics, ancient-urbanization (soft) |
| indian-ocean-trade-network | medieval-world | AP World 2.3 (Exchange in the Indian Ocean) and 1.5 (Swahili city-states). Only a passing mention of Kilwa in ancient-trade-networks. | silk-road-medieval-era, rise-of-islam, great-zimbabwe, song-dynasty-china, kingdoms-of-kush-and-aksum (soft) |
| delhi-sultanate | medieval-world | AP World 1.3 (Developments in South and Southeast Asia). Not mentioned anywhere. | rise-of-islam (hard); islamic-caliphates, maurya-and-gupta-empires, mongol-empire (soft) |
| safavid-empire | early-modern-period | AP World 3.1-3.3 (Ottoman, Safavid, Mughal). The Safavids are never mentioned in the graph. | islamic-caliphates (hard); ottoman-empire-early-modern, military-revolution-gunpowder-warfare, mongol-conquest-effects (soft) |
| tokugawa-japan | early-modern-period | AP World 3.1 and 4.x (Tokugawa shogunate, maritime restrictions). medieval-japan stops at 1600. | medieval-japan (hard); early-modern-missionary-activity, ming-qing-china (soft) |
| rise-of-russian-empire | early-modern-period | AP World 3.1 (Russian expansion); AP European History Unit 3 (Absolutism and Constitutionalism: Peter the Great) and Unit 4 (Catherine the Great as enlightened absolutist). No mention of Ivan IV, Peter or the Romanovs anywhere. | mongol-conquest-effects, byzantine-orthodox-christianity, absolutism-and-monarchy, enlightenment-origins (soft) |
| british-north-american-colonies | early-modern-period | APUSH Period 2 (1607-1754). No topic on the thirteen colonies, Jamestown, Puritans or King Philip's War. | age-of-exploration, joint-stock-corporations-trade, protestant-reformation, mercantilism, atlantic-racialized-slavery (soft) |
| creating-the-us-constitution | early-modern-period | APUSH Period 3 (Articles of Confederation, Constitutional Convention, ratification debates). american-revolution gives the Constitution one sentence; political-science topics are generic. | american-revolution (hard); separation-of-powers-doctrine, john-locke-liberal-political-thought, roman-republic-constitution, constitutionalism (soft) |
| napoleonic-era | early-modern-period | AP European History Unit 5 (Napoleon's Rise, Dominance and Defeat). french-revolution-origins gives Napoleon one closing paragraph. | french-revolution-origins (hard); absolutism-and-monarchy, military-revolution-gunpowder-warfare (soft) |
| latin-american-independence | early-modern-period | AP World Unit 5 (Nationalism and Revolutions, 1750-1900): Latin American independence. Bolívar, Hidalgo, San Martín not mentioned anywhere. | spanish-colonial-empire (hard); napoleonic-era, haitian-revolution, american-revolution, enlightenment-natural-rights-theory (soft) |
| american-civil-war | modern-history | APUSH Period 5 (1844-1877): sectional crisis and Civil War. No topic; the war appears only in passing in cotton-economy-slavery and a methods example. | creating-the-us-constitution, abolition-movement, cotton-economy-slavery, industrial-revolution (soft) |
| reconstruction-era-united-states | modern-history | APUSH Period 5 (Reconstruction and its failure). No topic. | american-civil-war (hard), creating-the-us-constitution (soft) |
| meiji-restoration | modern-history | AP World Unit 5 (Industrialization: Government's Role, which names Meiji Japan). Only passing mentions in economic-history topics. | tokugawa-japan (hard); imperialism-asia-opium-wars, industrial-revolution, nationalism-and-nation-states (soft) |
| progressive-era-united-states | modern-history | APUSH Period 7 (the Progressives). No topic. | second-industrial-revolution-electricity, industrial-urbanization-cities, labor-movements-collective-action, feminist-suffrage-movement, reconstruction-era-united-states (soft) |
| mexican-revolution | modern-history | AP World Unit 7 (Shifting Power after 1900, which uses the Mexican Revolution as an example of internal upheaval) and standard 20th-century survey chapters on Latin America. No topic. | latin-american-independence, economic-imperialism, labor-movements-collective-action (soft) |
| apartheid-south-africa | modern-history | AP World Unit 8 (decolonization; resistance to established power, including apartheid). Only passing comparisons inside civil-rights topics. | scramble-africa, imperialism-and-colonialism, decolonization, civil-rights-movement (soft) |
| european-integration-eu | modern-history | AP European History Unit 9 (Cold War and Contemporary Europe: European integration). No topic on the ECSC, EEC, Maastricht or the euro. | world-war-ii-origins, cold-war-origins, international-organizations, end-of-cold-war, globalization-economic-integration (soft) |

All 23 topics: stage `formal-systems` (the stage of their courses; no hard prerequisite is above it), status `validated`. Every prerequisite and builds-toward id was confirmed to exist with Glob, and every new id is unique across `domains/`. The proposed edges below were checked against the prerequisite lists of the target topics and the new topics' own prerequisites, so none creates a cycle.

## Proposed edges into existing topics

Each line means: the existing topic should list the new topic as a prerequisite. All match a `builds-toward` entry in the new file, so applying them clears the builds-toward consistency warnings.

```
ADD	greco-persian-wars	peloponnesian-war-city-states	soft	The Delian League formed after the Persian Wars grew into the Athenian empire that Sparta fought.
ADD	greco-persian-wars	hellenistic-period	soft	Alexander's conquest of Persia was framed as revenge for Xerxes' invasion; the wars set up the Greek-Persian relationship.
ADD	rise-of-christianity-roman-empire	byzantine-orthodox-christianity	soft	Byzantine Christianity starts from Constantine, Nicaea and the Theodosian settlement.
ADD	rise-of-christianity-roman-empire	medieval-church-power	soft	Papal and episcopal authority grew out of the late Roman church.
ADD	aztec-mexica-empire	conquistador-conquest-colonization	soft	The conquest of Mexico cannot be understood without the tribute empire and its resentful subject peoples.
ADD	inca-empire	conquistador-conquest-colonization	soft	Pizarro's conquest depended on the Inca civil war and epidemic.
ADD	indian-ocean-trade-network	early-modern-global-trade-networks	soft	Early modern European trade entered an existing Indian Ocean network.
ADD	indian-ocean-trade-network	age-of-exploration	soft	Portuguese voyages aimed at, and disrupted, Indian Ocean trade.
ADD	delhi-sultanate	mughal-empire	soft	Babur founded the Mughal Empire by defeating the last Delhi sultan at Panipat (1526).
ADD	british-north-american-colonies	american-revolution	soft	The Revolution arose from colonial self-government and the post-1763 tightening of British control.
ADD	napoleonic-era	congress-of-vienna	hard	The Congress of Vienna was the settlement of the Napoleonic Wars.
ADD	napoleonic-era	nationalism-and-nation-states	soft	Resistance to Napoleonic rule and his redrawing of German and Italian borders fed nineteenth-century nationalism.
ADD	reconstruction-era-united-states	civil-rights-movement	soft	The civil rights movement relied on the Fourteenth and Fifteenth Amendments and fought the Jim Crow order that followed Reconstruction.
ADD	meiji-restoration	axis-expansion-world-war-ii	soft	Japanese expansion in the 1930s grew from the Meiji state's industrial and imperial project.
ADD	progressive-era-united-states	great-depression	soft	The New Deal response built on Progressive-era ideas of federal regulation.
```

(The new files also list one another in builds-toward: olmec-and-maya-civilizations -> aztec-mexica-empire; maurya-and-gupta-empires -> delhi-sultanate; kingdoms-of-kush-and-aksum -> indian-ocean-trade-network; tokugawa-japan -> meiji-restoration; napoleonic-era -> latin-american-independence -> mexican-revolution; creating-the-us-constitution -> american-civil-war -> reconstruction-era-united-states. These are already consistent. rise-of-russian-empire lists russian-revolution in builds-toward; see the edge below.)

```
ADD	rise-of-russian-empire	russian-revolution	soft	Tsarist autocracy and serfdom, built from Peter to Catherine, are the background to 1917.
```

That makes 16 ADD lines in total.

## 4. Gaps considered and rejected

Already covered:
- New Deal: covered by `great-depression` (modern-history) and `great-depression-causes-responses`.
- German and Italian unification: covered by `nation-state-consolidation-19th-century` (Bismarck, Cavour, Garibaldi).
- Indian Rebellion of 1857 and the British Raj: covered by `british-east-india-company-colonialism` and `imperialism-and-colonialism`.
- Ancient Israelites and Judaism: covered by `origins-of-world-religions` and `ancient-religions-and-worldviews`.
- Women's suffrage: `feminist-suffrage-movement`. Abolition: `abolition-movement`. US civil rights: `civil-rights-movement`, `civil-rights-activism-american`.
- Opium Wars: `imperialism-asia-opium-wars`. Chinese revolution: `chinese-communist-revolution`. Partition of India: `indian-partition-independence`.
- Renaissance Italy, Reformation, absolutism, Scientific Revolution, Enlightenment, French and Haitian Revolutions, Industrial Revolution, both world wars, Cold War, decolonization: all have one or more topics.
- Mongols, Mali, Great Zimbabwe, Song and Tang China, Byzantium, the caliphates, feudal Japan, trans-Saharan trade, Silk Roads: all covered in medieval-world.
- Shang, Zhou, Qin and Han China, Egypt, Mesopotamia, Indus, Persia, Greece, Rome: all covered in ancient-civilizations.

Considered but not added in this pass (weaker as stand-alone syllabus units, or usually taught as examples inside a larger topic):
- Southeast Asian states (Khmer/Angkor, Srivijaya, Majapahit): AP World 1.3 example; no topic exists. A reasonable next candidate.
- Ottoman decline and Tanzimat reforms; Taiping Rebellion; Armenian genocide; Arab-Israeli conflict; US westward expansion and Manifest Destiny; Gilded Age politics: each appears in AP syllabi, but mainly as illustrative examples. Worth a second pass if the domain wants APUSH and AP World coverage at the example level.
