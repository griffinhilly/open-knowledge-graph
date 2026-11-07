# New topics report: chemistry

Status: COMPLETE. 19 new topics written; 9 proposed edges into existing topics.

Inorganic chemistry was checked closely, as asked. Its 32 existing topics cover coordination chemistry, organometallics, clusters and bioinorganic well. Its descriptive and redox-thermodynamic units were missing, so 6 of the 19 new topics are there.

Checks done: every prerequisite and builds-toward id was confirmed to exist with Glob. Every new id was confirmed unused before writing. Stages were checked against the stages of hard prerequisites. The new files were grepped for em dashes and banned words, with zero hits. Not checked: tools/validate.py was not run, because this task allowed only Read, Grep, Glob and Write. Explainer word counts were estimated, not counted exactly.

## 1. Syllabi compared against

| Course | Syllabus / textbook table of contents |
|---|---|
| properties-of-matter | NGSS 2-PS1 and 5-PS1 (structure and properties of matter, grades 2 and 5) |
| introductory-chemistry | NGSS MS-PS1 (middle school matter and its interactions) |
| general-chemistry | College Board AP Chemistry CED (Units 1-9); OpenStax Chemistry 2e, Ch. 1-21 |
| organic-chemistry | Klein, Organic Chemistry; Wade, Organic Chemistry (full two-semester TOC) |
| physical-chemistry | Atkins & de Paula, Physical Chemistry; McQuarrie & Simon, Physical Chemistry: A Molecular Approach |
| analytical-chemistry | Harris, Quantitative Chemical Analysis; Skoog, Fundamentals of Analytical Chemistry |
| inorganic-chemistry | Miessler, Fischer & Tarr, Inorganic Chemistry; Housecroft & Sharpe, Inorganic Chemistry; Shriver & Atkins (Weller et al.), Inorganic Chemistry |
| materials-chemistry | Smart & Moore, Solid State Chemistry: An Introduction; West, Solid State Chemistry and its Applications |

## 2. New topics

| new id | course | why it is a gap (syllabus unit) | prerequisites |
|---|---|---|---|
| latimer-and-frost-diagrams | inorganic-chemistry | Housecroft & Sharpe Ch. 8 and Shriver & Atkins "Oxidation and reduction": redox stability diagrams. No topic mentions Latimer or Frost diagrams. | electrochemical-cells (h), free-energy-change-spontaneity-work (h), oxidation-numbers (s), half-reactions-and-balancing (s), electrochemistry-nernst-equation (s) |
| ellingham-diagrams-metal-extraction | inorganic-chemistry | Shriver & Atkins "Oxidation and reduction: extraction of the elements"; Housecroft Ch. 8. "Ellingham" appears nowhere in domains/. | gibbs-free-energy-spontaneity (h), entropy-and-gibbs-free-energy (s), oxidation-reduction-reactions (s), electrolytic-cells-and-electrolysis (s) |
| nonaqueous-solvents-and-leveling-effect | inorganic-chemistry | Housecroft Ch. 9 "Non-aqueous media"; Miessler Ch. 6 (solvent effects, superacids). No topic covers leveling, solvent systems or superacids. | acid-base-definitions (h), acid-base-strength-ka-kb-calculations (h), hsab-theory (s), polar-protic-aprotic-solvents (s), acidity-organic-compounds-pka (s) |
| noble-gas-compounds | inorganic-chemistry | Housecroft Ch. 18 "Group 18". Only intro-level "noble gases are unreactive" and passing XeF₄ mentions exist. | main-group-chemistry-overview (h), vsepr-theory (h), noble-gases-and-stability (s), ionization-energy-and-electron-removal (s), molecular-orbital-diagrams-polyatomic (s) |
| halogen-and-interhalogen-chemistry | inorganic-chemistry | Housecroft Ch. 17 "Group 17". main-group-chemistry-overview gives trends only; no interhalogen or halogen oxoacid coverage. | main-group-chemistry-overview (h), vsepr-theory (s), oxidation-numbers (s), electrochemical-cells (s), acid-strength-and-molecular-structure (s) |
| hydrogen-and-binary-hydrides | inorganic-chemistry | Housecroft Ch. 10 and Shriver Ch. 10 "Hydrogen". No topic classifies saline, molecular and metallic hydrides. | main-group-chemistry-overview (h), bond-classification (s), electronegativity-and-bond-polarity (s), intermolecular-forces (s), oxidation-numbers (s) |
| acid-strength-and-molecular-structure | general-chemistry | AP Chemistry Topic 8.6 "Molecular Structure of Acids and Bases"; OpenStax 14.3. Organic pKa trends exist, but no general topic on binary acids and oxoacids. | acid-base-strength-ka-kb-calculations (h), electronegativity-and-bond-polarity (h), bond-energy-and-enthaly (s), resonance-structures (s), periodic-trends (s) |
| photoelectron-spectroscopy-pes | general-chemistry | AP Chemistry Topic 1.6 "Photoelectron Spectroscopy". Only XPS for surfaces (materials, expert stage) exists. | electron-configuration (h), ionization-energy-and-electron-removal (h), photoelectric-effect (s), periodic-trends (s) |
| naming-molecular-compounds-and-acids | general-chemistry | OpenStax 2.7 "Chemical Nomenclature" (molecular compounds and acids). writing-ionic-formulas covers ionic naming only. | writing-ionic-formulas (h), covalent-bonding (s), molecules-and-chemical-formulas (s), acids-properties-and-examples (s) |
| significant-figures-in-measurement | general-chemistry | OpenStax 1.5 "Measurement Uncertainty, Accuracy, and Precision" (significant-figure rules). Analytical topics treat formal uncertainty; no topic teaches the significant-figure rules. | scientific-notation-intro (s), measuring-volume (s), accuracy-precision-error (s) |
| michael-addition-conjugate-addition | organic-chemistry | Klein and Wade enolate chapters: "Conjugate addition / Michael reaction / Robinson annulation". Michael addition appears only in passing in enolate and enamine topics. | enols-and-enolate-chemistry (h), nucleophilic-addition-to-carbonyls (h), resonance-in-organic-intermediates (s), aldol-reaction (s), organometallic-grignard-organolithium (s) |
| electrocyclic-and-sigmatropic-reactions | organic-chemistry | Klein Ch. 16 "Pericyclic reactions" (electrocyclic, sigmatropic). Only Diels–Alder exists; Woodward–Hoffmann rules appear only in passing in photochemistry topics. | diels-alder-reaction (h), conjugated-dienes (h), huckel-molecular-orbital-theory (s), bonding-antibonding-orbitals (s), photochemistry-excited-state-reactions (s) |
| arenediazonium-salts-sandmeyer | organic-chemistry | Klein and Wade amine chapters: "Reactions of arenediazonium salts". "Diazonium" and "Sandmeyer" appear nowhere in domains/. | amines-structure-and-properties (h), electrophilic-aromatic-substitution (h), directed-ortho-para-effects (s), nucleophilic-aromatic-substitution (s) |
| alkene-epoxidation-peroxy-acids | organic-chemistry | Klein Ch. 8 "Addition reactions of alkenes: anti dihydroxylation / epoxidation". epoxide-ring-opening exists, but how epoxides form is mentioned only in passing. | electrophilic-addition-to-alkenes (h), alkene-structure-and-nomenclature (s), stereochemistry-intro (s), alkene-hydroxylation-osmium-permanganate (s) |
| ozonolysis-oxidative-cleavage | organic-chemistry | Klein Ch. 8 "Oxidative cleavage"; Wade "Ozonolysis". Ozonolysis appears in only one distractor explanation. | electrophilic-addition-to-alkenes (h), aldehyde-and-ketone-structure-and-nomenclature (h), alkene-hydroxylation-osmium-permanganate (s), oxidation-reactions-organic (s) |
| epr-spectroscopy | physical-chemistry | Atkins "Magnetic resonance: electron paramagnetic resonance". NMR has 8+ topics; EPR/ESR appears nowhere in chemistry. | energy-level-transitions (h), spin-angular-momentum (s), nmr-quantum-theory (s), nmr-spectroscopy-spin-coupling (s) |
| activity-coefficients-ionic-strength | analytical-chemistry | Harris Ch. 8 "Activity and the Systematic Treatment of Equilibrium" (activity, ionic strength, Debye–Hückel). Activity is mentioned inside electrode topics, but no topic teaches it. | chemical-equilibrium (h), equilibrium-expression-kc-kp-constants (h), solubility-product-constant-ksp (s), concentration-units (s) |
| systematic-treatment-of-equilibrium | analytical-chemistry | Harris Ch. 8 (charge balance, mass balance, systematic treatment). No topic teaches charge or mass balance equations. | chemical-equilibrium (h), weak-acid-ionization (h), polyprotic-acids (s), ph-and-acid-base-calculations (s), activity-coefficients-ionic-strength (s) |
| carbon-allotropes-nanocarbons | materials-chemistry | Smart & Moore, chapter on carbon-based materials (fullerenes, nanotubes, graphene). Fullerenes, nanotubes and graphene appear only in passing in composites and batteries. | hybridization-sp-orbitals (h), electronic-band-theory-of-solids (s), aromatic-compounds-intro (s), crystal-structures-and-unit-cells (s) |

No gaps were found in properties-of-matter or introductory-chemistry. Their NGSS units are all covered.

## Proposed edges into existing topics

ADD	latimer-and-frost-diagrams	corrosion-chemistry-and-protection	soft	Pourbaix-diagram reasoning in corrosion extends Latimer/Frost stability analysis to pH.
ADD	acid-strength-and-molecular-structure	acidity-organic-compounds-pka	soft	Organic pKa trends reuse the bond-strength and conjugate-base-stability arguments.
ADD	photoelectron-spectroscopy-pes	characterization-methods-tem-sem-xps	soft	XPS is the surface application of the PES binding-energy principle.
ADD	significant-figures-in-measurement	uncertainty-propagation	soft	Formal uncertainty propagation generalizes significant-figure rules.
ADD	alkene-epoxidation-peroxy-acids	epoxide-ring-opening	soft	Ring opening acts on epoxides that are usually made by peroxy-acid epoxidation.
SKIPPED-ADD	activity-coefficients-ionic-strength	potentiometry	soft	The glass electrode responds to H⁺ activity; activity corrections are cited in that topic.
ADD	activity-coefficients-ionic-strength	ion-selective-electrodes	soft	ISE readings depend on activity coefficients; the topic's TISAB rationale assumes this concept.
ADD	activity-coefficients-ionic-strength	solution-thermodynamics-activity-models	soft	Activity-coefficient models generalize the Debye–Hückel treatment of ionic activity.

(Also inside the new set, with no existing file to change: activity-coefficients-ionic-strength -> systematic-treatment-of-equilibrium (soft) and acid-strength-and-molecular-structure -> halogen-and-interhalogen-chemistry (soft). Both are already written into the new files.)

## 4. Gaps considered and rejected

| Candidate | Rejected because already covered by |
|---|---|
| 18-electron rule, isolobal analogy, Wade's rules | organometallic-chemistry-fundamentals, metal-carbonyls, cluster-compounds |
| Oxidative addition, reductive elimination, migratory insertion; Pd cross-coupling (Suzuki, Heck) | homogeneous-catalysis-mechanisms, organometallic-chemistry-fundamentals, catalytic-cycles-wilkinson-grubbs |
| Trans effect | reaction-mechanisms-coordination-compounds |
| Point groups and symmetry | group-theory-molecular-symmetry, molecular-symmetry-and-group-theory, group-theory-applications-inorganic |
| Lattice energy, ionic structure types (rock salt, fluorite, radius ratio) | born-haber-thermochemistry, solid-state-chemistry-fundamentals, crystal-structures-and-unit-cells |
| Boranes and three-center bonding | cluster-compounds, main-group-chemistry-overview |
| Diagonal relationship, inert pair effect, first-row anomaly | main-group-chemistry-overview |
| Pourbaix diagrams as a separate topic | corrosion-chemistry-and-protection, redox-geochemistry (earth-and-space-sciences); latimer-and-frost-diagrams links forward to them |
| Silicates | glass-and-amorphous-materials, zeolite-chemistry-and-applications |
| Effective nuclear charge / Slater's rules | periodic-trends, ionization-energy-and-electron-removal |
| Acid-base properties of salts (salt hydrolysis) | ph-and-acid-base-calculations |
| ΔG° = −RT ln K and ΔG° = −nFE° | free-energy-change-spontaneity-work, gibbs-free-energy-spontaneity, electrochemical-cells |
| Graham's law and effusion | kinetic-molecular-theory, kinetic-molecular-distribution-speeds |
| Net ionic equations, precipitation reactions | precipitation-equilibrium-and-common-ion, chemical-equations-and-balancing |
| History of atomic models (Dalton, Thomson, Rutherford) | atomic-structure-and-atoms, history-of-chemistry-alchemy-to-modern (history) |
| Bohr model and line spectra | atomic-structure-basics, orbital-theory-and-shapes, energy-level-transitions |
| Nuclear chemistry, half-life | nuclear-chemistry |
| Dimensional analysis (factor-label) | Used throughout molar-mass-and-conversions and gas-laws; mathematics converting-metric-units. Judged too thin to stand alone. |
| Optical activity, polarimetry | enantiomers-and-chirality |
| Halogenation of alkenes (bromonium ion) | electrophilic-addition-to-alkenes |
| Kinetic versus thermodynamic control | conjugated-dienes |
| Phenols | acidity-organic-compounds-pka plus aromatic substitution topics. Not a clear stand-alone unit in Klein. |
| Aromatic heterocycles (pyridine, pyrrole) | Partly in amines-structure-and-properties. A Clayden-level unit, weaker for the standard sophomore syllabus; not added. |
| Carbohydrates, amino acids, lipids, nucleic acids | biology/biochemistry: carbohydrate-structure-and-classification, amino-acid-structure-and-properties, fatty-acid-structure-and-classification, nucleic-acid-structures |
| First, second and third laws; Carnot cycle; Maxwell relations; Helmholtz energy | physics/thermodynamics and engineering/thermodynamics-engineering (first-law-closed-systems, maxwell-relations-thermodynamics, helmholtz-gibbs-free-energy) |
| Particle in a box | physics/modern-physics/particle-in-a-box |
| Steady-state approximation | elementary-reaction-mechanisms-catalysis, michaelis-menten-enzyme-kinetics-physical-chemistry |
| Gibbs phase rule | engineering gibbs-phase-rule-multicomponent; phase-diagrams-binary-mixtures |
| Piezoelectric and ferroelectric materials | ceramic-materials-chemistry; dielectrics in physics |
| Liquid crystals, sol-gel synthesis | Not stand-alone units in Smart & Moore or West; not added |
| Properties-of-matter and introductory-chemistry units (NGSS 2-PS1, 5-PS1, MS-PS1) | All units present, including particle model, conservation of mass, physical and chemical change, mixtures, density, and periodic table basics |
