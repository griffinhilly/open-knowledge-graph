# Expert-Level Coverage Gap Scoping

Generated: 2026-03-29
Baseline: 13,153 topics, 19 domains, 197 courses

This document scopes the ~60 topic areas identified as missing across all domains,
primarily at the expert (graduate/research) level. For each gap, it determines
whether to create a new course or extend an existing one, estimates topic count,
and assigns a priority tier.

**Priority definitions:**
- **P0 (fundamental)**: Core subdiscipline entirely missing, or graduate-level gap in a foundational area
- **P1 (important)**: Significant gap that limits the domain's usefulness at the expert level
- **P2 (nice-to-have)**: Specialized area that would improve completeness but isn't critical

---

## Mathematics

Existing courses: 27 (kindergarten through measure-theory-and-functional-analysis).
Key advanced/expert courses: differential-equations (48 topics), real-analysis, abstract-algebra (68),
topology (99), complex-analysis, number-theory (67), probability-and-mathematical-statistics (50),
numerical-analysis (41), graph-theory-and-combinatorics (55), measure-theory-and-functional-analysis (59).

### P0 -- Fundamental Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Algebraic topology | NEW COURSE `algebraic-topology` (expert) | 30-35 | Topology course (99 topics) covers fundamental group, covering spaces, homotopy, but has zero homology/cohomology content. This is a core graduate math course that requires its own course. |
| Partial differential equations | NEW COURSE `partial-differential-equations` (advanced/expert) | 30-35 | DEs course has only 3-5 PDE topics (heat, wave, Laplace, separation of variables). A proper PDE course (elliptic/parabolic/hyperbolic classification, Sobolev spaces, weak solutions, Green's functions, distribution theory) is a standard graduate requirement. |
| Differential geometry | NEW COURSE `differential-geometry` (advanced/expert) | 30-35 | Entirely absent. No manifolds, tangent bundles, Riemannian geometry, connections, curvature tensors. Critical for physics (GR, gauge theory) and pure math. Topology has `topological-manifolds-introduction` as a seed. |

### P1 -- Important Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Commutative algebra | NEW COURSE `commutative-algebra` (expert) | 25-30 | Abstract algebra (68 topics) covers groups extensively and has rings/fields, but lacks Noetherian rings, localization, modules over PIDs, primary decomposition, completions. Essential for algebraic geometry and number theory. |
| Stochastic processes | EXTEND `probability-and-mathematical-statistics` + possibly NEW COURSE | 20-25 | Prob-math-stats (50 topics) has martingales, Markov chains. Missing: Brownian motion, Ito calculus, SDEs, stochastic integration, Levy processes. Could extend if kept under 75 topics, or spin off a new `stochastic-processes` course. Recommend: NEW COURSE. |
| Representation theory | NEW COURSE `representation-theory` (expert) | 25-30 | Entirely absent. Group representations, character theory, modules, Lie algebra representations. Bridges abstract algebra, linear algebra, and physics. |
| Logic and set theory (advanced) | EXTEND `set-theory` (formal-sciences) or CROSS-DOMAIN | 15-20 | Formal sciences has set-theory (96 topics) and model-theory (74 topics). ZFC axioms likely present; check for forcing, large cardinals, independence results. May need 15-20 expert-level additions to set-theory rather than a new course. |

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Advanced combinatorics / algebraic combinatorics | EXTEND `graph-theory-and-combinatorics` | 15-20 | Course has 55 topics including matroids, Ramsey theory, generating functions. Add: algebraic combinatorics (symmetric functions, Young tableaux, Polya enumeration, Schur polynomials). |
| Category theory (math side) | CROSS-DOMAIN (formal-sciences `category-theory` has 94 topics) | 10-15 | Formal sciences already has a substantial category theory course. Math-specific additions (homological algebra, derived categories, sheaves) could go there or in a new math course. Recommend extending formal-sciences course. |
| Advanced numerical methods | EXTEND `numerical-analysis` | 15-20 | Course has 41 topics covering basics. Missing: FEM, spectral methods, multigrid, parallel algorithms, adaptive mesh refinement. |

---

## Computer Science

Existing courses: 10 (programming-fundamentals through distributed-systems).
Key advanced/expert: theory-of-computation (73), artificial-intelligence (122), compilers,
distributed-systems (56), data-structures-and-algorithms (74), databases (79),
computer-architecture (79).

### P0 -- Fundamental Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Machine learning theory | NEW COURSE `machine-learning-theory` (expert) | 25-30 | AI course (122 topics) covers practical ML/DL but lacks formal theory: PAC learning, VC dimension, statistical learning theory, Rademacher complexity, approximation-estimation tradeoffs, kernel theory proofs. Zero results for PAC/VC searches. |
| Cryptography (theoretical) | NEW COURSE `cryptography` (advanced/expert) | 30-35 | Entirely absent. No formal crypto content (the networking search returned general security topics, not computational hardness/protocols). Needs: symmetric/asymmetric primitives, computational security, zero-knowledge proofs, secure computation, lattice-based crypto. |
| Quantum computing | NEW COURSE `quantum-computing` (advanced/expert) | 25-30 | Zero topics found. Needs: qubits, quantum gates, quantum circuits, Shor's/Grover's algorithms, quantum error correction, quantum complexity classes, quantum information. |

### P1 -- Important Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Information theory | NEW COURSE `information-theory` (advanced/expert) | 25-30 | No dedicated coverage. Statistical mechanics has `information-theory-entropy` and music has `information-theory-music`, but no Shannon entropy, channel capacity, source coding, rate-distortion theory. Foundational for CS and communications. |
| Advanced algorithms | EXTEND `data-structures-and-algorithms` or NEW COURSE | 20-25 | DSA (74 topics) covers standard algorithms. Missing: randomized algorithms, streaming/sketching, online algorithms, approximation algorithms (formal), parameterized complexity, competitive analysis. Recommend: NEW COURSE `advanced-algorithms` at expert stage. |
| Program verification / formal methods | NEW COURSE `formal-methods` (expert) | 20-25 | Zero results for Hoare logic, model checking, program verification. Compilers has `programming-language-semantics` as a seed. Needs: Hoare logic, separation logic, model checking, theorem provers, refinement types, abstract interpretation. |

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Database theory | EXTEND `databases` | 10-15 | Databases (79 topics) covers practical. Add formal theory: relational algebra proofs, query complexity, dependency theory, datalog, database repair, consistent query answering. |
| Programming language semantics (formal) | EXTEND `compilers` | 10-15 | Compilers already has `programming-language-semantics`, `hindley-milner-type-system`, `domain-specific-language-design`. Add: denotational semantics, operational semantics, domain theory, linear types, effect systems. |
| Advanced computer architecture | EXTEND `computer-architecture` | 10-15 | Course has 79 topics. Missing graduate-level: out-of-order execution details, memory consistency models, GPU architecture, VLIW, hardware security, cache coherence (some in distributed-systems). |
| Systems research | EXTEND `operating-systems` + `distributed-systems` | 10-15 | Split across existing courses. Add: storage systems, file system design patterns, kernel bypass, RDMA, disaggregated memory, serverless architecture. |

---

## Physics

Existing courses: 10 (physical-science through statistical-mechanics).
Key advanced/expert: modern-physics (119), quantum-mechanics (84), electrodynamics (89),
statistical-mechanics (100).

### P0 -- Fundamental Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Quantum field theory | NEW COURSE `quantum-field-theory` (expert) | 30-35 | A few QFT-adjacent topics exist in QM (path integrals, creation/annihilation operators) and stat-mech (renormalization group), but no actual QFT course. Needs: canonical quantization, Feynman diagrams, QED, gauge theories, renormalization, Standard Model intro. Core graduate physics. |
| General relativity | NEW COURSE `general-relativity` (expert) | 25-30 | Entirely absent -- zero search results. Needs: curved spacetime, Einstein field equations, Schwarzschild solution, geodesics, gravitational waves, black holes, cosmological models. Core graduate physics. |
| Condensed matter physics | NEW COURSE `condensed-matter-physics` (expert) | 30-35 | Stat-mech has BCS superconductivity, Bose-Einstein condensation, phonons, Ising model. But no dedicated condensed matter: band theory (only `band-theory-intro` in modern-physics), Bloch theorem, Fermi liquid theory, quantum Hall effect, topological insulators, magnetic ordering. |

### P1 -- Important Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Advanced classical mechanics | EXTEND `classical-mechanics` | 15-20 | Classical mechanics (92 topics) has `lagrangian-mechanics-intro` and `hamiltonian-mechanics-intro` plus `phase-space-trajectories`. Need full graduate treatment: canonical transformations, Hamilton-Jacobi theory, Poisson brackets, action-angle variables, Noether's theorem (rigorous), continuum mechanics. |
| Nonlinear dynamics and chaos | NEW COURSE `nonlinear-dynamics` (advanced/expert) | 20-25 | DEs has `bifurcation-in-odes` and `autonomous-equations`. Physics has `phase-space-trajectories`. But no dedicated chaos content: Lyapunov exponents, strange attractors, fractals, routes to chaos, KAM theorem, pattern formation. Cross-disciplinary importance. |
| Particle physics / Standard Model | NEW COURSE `particle-physics` (expert) | 25-30 | Modern physics (119 topics) covers basics (pair creation, nuclear physics). No dedicated particle physics: quark model, electroweak theory, Higgs mechanism, deep inelastic scattering, neutrino physics, BSM physics. |

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Plasma physics | NEW COURSE `plasma-physics` (expert) | 20-25 | Absent. Magnetohydrodynamics, Debye shielding, plasma waves, Vlasov equation, fusion physics. |
| AMO physics | NEW COURSE `atomic-molecular-optical` (expert) | 20-25 | QM covers quantum theory but not experimental AMO: laser physics, trapping/cooling, spectroscopy methods, quantum optics, atom interferometry. |
| Nuclear physics (graduate) | EXTEND `modern-physics` | 10-15 | Modern physics already has nuclear content. Add: nuclear structure models (shell, collective), nuclear reactions (cross sections, compound nucleus), nuclear astrophysics. |
| Astrophysics / cosmology | EXTEND `astronomy` (earth-and-space-sciences) or NEW COURSE in physics | 15-20 | Earth & space has `astronomy` (87 topics) with some astrophysics. Physics-level content (stellar structure equations, nucleosynthesis, FLRW cosmology, dark matter/energy) could extend that course or create a physics-domain course. Recommend: EXTEND existing astronomy course. |

---

## Chemistry

Existing courses: 6 (properties-of-matter through analytical-chemistry).
Physical chemistry (125), analytical (127), organic (133), general (130).

### P0 -- Fundamental Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Inorganic chemistry | NEW COURSE `inorganic-chemistry` (formal-systems/advanced) | 30-35 | ENTIRELY ABSENT. The single biggest content gap in the graph. Only `coordination-chemistry-basics` and `complex-ions-and-stability` in general chemistry. Needs: coordination chemistry (full), crystal field/ligand field theory, organometallics, bioinorganic, solid-state, main group chemistry, symmetry/group theory applications. |

### P1 -- Important Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Biochemistry (expanded) | CROSS-DOMAIN (biology `biochemistry` has 85 topics) | 10-15 | Biology domain has a biochemistry course (85 topics) covering enzymes, metabolism, protein structure. Chemistry-side biochemistry (enzyme kinetics formalism, bioorganic mechanisms, nucleic acid chemistry, chemical biology) could extend the existing bio course or create a chemistry-side complement. Recommend: EXTEND biology biochemistry course. |
| Materials chemistry / solid-state chemistry | NEW COURSE `materials-chemistry` (advanced/expert) | 20-25 | Absent from chemistry. Engineering has materials-science (102 topics) covering metallurgy/polymers. Chemistry side needs: crystal structure/symmetry, defect chemistry, electronic materials, nanomaterials synthesis, ceramic chemistry, thin films. |
| Advanced organic synthesis | EXTEND `organic-chemistry` | 15-20 | Organic (133 topics) covers mechanisms well. Missing graduate-level: retrosynthetic analysis, named reactions (systematic), asymmetric synthesis, total synthesis strategy, protecting group strategy, C-H activation. |

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Graduate spectroscopy | EXTEND `analytical-chemistry` or `physical-chemistry` | 10-15 | Physical chemistry has NMR, electronic spectroscopy, fluorescence. Missing: 2D NMR techniques, mass spec fragmentation theory, X-ray crystallography, Raman spectroscopy theory, CD spectroscopy. Split across p-chem and analytical. |
| Computational chemistry methods | EXTEND `physical-chemistry` | 10-15 | Physical chemistry has Hartree-Fock, post-HF, DFT references. Missing: basis set theory, molecular dynamics methods, QM/MM, semiempirical methods, machine learning potentials. |
| Environmental chemistry | NEW COURSE `environmental-chemistry` (advanced) | 15-20 | Absent. Atmospheric chemistry of pollutants, water chemistry, soil chemistry, toxicology basics, environmental fate. |
| Advanced electrochemistry | EXTEND `physical-chemistry` or `analytical-chemistry` | 10-15 | General chemistry has `electrochemical-cells`. Missing: electrode kinetics (Butler-Volmer), mass transport, EIS, batteries/fuel cells chemistry, corrosion science. |
| Advanced chemical thermodynamics | EXTEND `physical-chemistry` | 10-12 | Physical chemistry (125 topics) already covers thermo well. Add: non-ideal solution theory (activity models exist), phase equilibria (multi-component), statistical thermo (partially covered). Smaller gap than others. |
| Surface science | EXTEND `physical-chemistry` | 8-12 | Physical chemistry has `surface-chemistry-and-catalysis`, `surface-thermodynamics-adsorption`, `BET-theory`. Add: surface characterization (XPS, AES, STM), self-assembled monolayers, thin film deposition theory. |

---

## Biology

Existing courses: 11 (living-things through immunology).
Genetics-and-molecular-biology (109), ecology-and-evolution (121), evolutionary-biology (77),
biochemistry (85), cell-biology (110), microbiology (101), neuroscience (92), immunology (74),
physiology (109).

### P0 -- Fundamental Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Genomics and bioinformatics | NEW COURSE `genomics-and-bioinformatics` (advanced/expert) | 25-30 | Genetics has `genomics-overview`, `next-generation-sequencing-ngs`, and scattered molecular tools. But no dedicated bioinformatics: sequence alignment algorithms, genome assembly, RNA-seq analysis, variant calling pipelines, comparative genomics, metagenomics, phylogenomics. This is a core modern biology discipline. |

### P1 -- Important Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Systems biology / network biology | NEW COURSE `systems-biology` (expert) | 20-25 | Absent. Needs: biological network analysis, metabolic flux analysis, gene regulatory networks, synthetic gene circuits modeling, multi-omics integration, systems pharmacology. |
| Developmental biology | NEW COURSE `developmental-biology` (advanced/expert) | 25-30 | Only scattered references: `hox-genes-body-plan`, `cell-differentiation-development`, `evolutionary-developmental-biology`. No dedicated course for: morphogen gradients, gastrulation, organogenesis, axis formation, stem cell niche, regeneration. |
| Structural biology methods | NEW COURSE `structural-biology` (expert) | 20-25 | Absent. X-ray crystallography, cryo-EM, NMR spectroscopy (protein), structure determination pipelines, molecular modeling, structure-based drug design. |
| Population genetics | CROSS-DOMAIN (extensive coverage across ecology-and-evolution + evolutionary-biology) | 5-10 | Surprisingly well-covered: Hardy-Weinberg (intro + advanced), genetic drift, effective population size, coalescent theory, selection models, Wahlund effect, etc. across ~90 topics in two courses. May need only a few expert additions (diffusion theory, structured coalescent). Small gap. |
| Epigenetics | EXTEND `genetics-and-molecular-biology` | 10-15 | Already has `epigenetics-intro`, `dna-methylation-and-epigenetic-silencing`, `genomic-imprinting`, `histone-modifications-epigenetic`, `chromatin-remodeling-swi-snf`. Missing: transgenerational epigenetics, epitranscriptomics, single-cell epigenomics, environmental epigenetics. Smaller gap than initially assessed. |

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Synthetic biology | EXTEND `genetics-and-molecular-biology` or NEW COURSE | 15-20 | Genetics has CRISPR content. Missing: genetic circuit design, metabolic engineering, directed evolution, standardized biological parts, cell-free systems, biosafety. Could be new course or extend genetics. |
| Stem cell biology | EXTEND `cell-biology` | 8-12 | Cell biology has `stem-cells-pluripotency`. Add: induced pluripotent stem cells, stem cell niche, organoids, tissue engineering, stem cell therapy approaches, asymmetric division. |
| Virology | CROSS-DOMAIN (microbiology covers virology extensively) | 5-10 | Microbiology (101 topics) has substantial virology: viral replication strategies, capsid structure, pathogenesis, classification, RNA/DNA polymerases, attachment/entry. May need only expert additions: viral evolution, emerging viruses, antivirals. Small gap. |
| Proteomics | EXTEND `biochemistry` (biology domain) | 10-15 | Missing: mass spectrometry-based proteomics, protein-protein interaction networks, post-translational modification profiling, quantitative proteomics, structural proteomics pipelines. |

---

## Earth & Space Sciences

Existing courses: 9 (earth-and-weather through geophysics).
Geophysics (90), geology (75), astronomy (87), climate-science (91),
meteorology-and-climate (87), oceanography (76), planetary-science (76).

### P1 -- Important Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Remote sensing and GIS | NEW COURSE `remote-sensing-and-gis` (advanced) | 25-30 | Absent as a dedicated topic area. Geophysics/geology reference satellite data but lack: remote sensing principles, image classification, LiDAR, radar, GIS spatial analysis, cartographic methods, geospatial data science. Important applied earth science discipline. |
| Isotope geochemistry | NEW COURSE `geochemistry` (expert) | 25-30 | Geology has `radiometric-dating` and climate-science has `oxygen-isotope-paleothermometry`, but no systematic geochemistry: stable isotope systematics, radiogenic isotopes (Rb-Sr, Sm-Nd, U-Pb), trace elements, mantle geochemistry, cosmochemistry. Recommend combined `geochemistry` course. |
| Volcanology | EXTEND `geology` | 10-15 | Geology (75 topics) has `volcanic-hazards-assessment` and `subduction-magmatism-arc-volcanism`. Missing: eruption dynamics, volcanic monitoring, magma chamber processes, pyroclastic flows, volcanic gas chemistry. |

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Sedimentology and stratigraphy | EXTEND `geology` | 10-15 | Geology has `stratigraphy`, `sedimentary-rocks`, `sediment-transport-and-deposition`, `sedimentary-depositional-environments`. Missing expert-level: sequence stratigraphy, basin analysis, facies models, carbonate sedimentology. |
| Glaciology | EXTEND `geology` or `climate-science` | 8-12 | Referenced in `erosion-agents-fluvial-glacial-coastal`. Missing: ice sheet dynamics, glacier flow models, ice core analysis, glacial geomorphology, ice-climate feedbacks. |
| Atmospheric chemistry | EXTEND `climate-science` or `meteorology-and-climate` | 10-15 | Climate science (91 topics) has aerosol forcing but lacks: ozone chemistry, photochemistry, aerosol microphysics, air quality modeling, stratospheric dynamics. |
| Space weather / magnetospheric physics | EXTEND `geophysics` or `astronomy` | 8-12 | Geophysics has geomagnetic field topics. Missing: solar wind, magnetosphere structure, auroral physics, space weather forecasting, radiation belts. |
| Astrobiology | EXTEND `planetary-science` | 8-10 | Missing: habitability criteria, biosignature detection, extremophile biology, origin of life chemistry, exoplanet characterization. |
| Geochronology | EXTEND `geology` or include in `geochemistry` | 8-10 | Geology has `radiometric-dating`. Missing: U-Pb geochronology, Ar-Ar dating, cosmogenic nuclide dating, luminescence dating, detrital zircon analysis. Recommend: include in proposed `geochemistry` course. |

---

## Health & Human Development

Existing courses: 8 (my-body through epidemiology).
Epidemiology (85), public-health (79), pathophysiology (109).

### P1 -- Important Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Biostatistics methods | NEW COURSE `biostatistics` (advanced/expert) | 25-30 | Epidemiology has study design topics but lacks formal biostatistics: survival analysis, longitudinal data analysis, clinical trial design, multiple comparisons, meta-analysis methods, causal inference methods, Bayesian clinical statistics. |
| Clinical trials methodology | EXTEND `epidemiology` or include in `biostatistics` | 10-15 | Missing: RCT design, randomization methods, blinding, adaptive trials, interim analysis, non-inferiority trials, pragmatic trials. Recommend: include in proposed biostatistics course. |
| Health economics | NEW COURSE `health-economics` (advanced) | 20-25 | Absent. Cost-effectiveness analysis, QALY/DALY, health insurance economics, healthcare market structure, pharmacoeconomics, economic evaluation methods. Cross-links to economics domain. |

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Health informatics | EXTEND `epidemiology` or `public-health` | 10-15 | Missing: EHR data analysis, health data standards (HL7/FHIR), clinical decision support, health information systems, medical imaging informatics. |
| Implementation science | EXTEND `public-health` | 8-12 | Missing: dissemination frameworks, RE-AIM, adoption/fidelity measures, knowledge translation, quality improvement science. |
| Pharmacoepidemiology | EXTEND `epidemiology` | 8-10 | Missing: drug safety surveillance, pharmacovigilance, prescription databases, signal detection, drug utilization studies. |
| Genetic epidemiology | EXTEND `epidemiology` | 8-10 | Missing: GWAS methodology, linkage analysis, Mendelian randomization, polygenic risk scores, gene-environment interaction. |
| Occupational health | EXTEND `public-health` | 8-10 | Missing: occupational exposure assessment, industrial hygiene, ergonomics, occupational disease classification. |
| Maternal/reproductive health | EXTEND `public-health` or `pathophysiology` | 8-10 | Missing: maternal mortality, reproductive epidemiology, perinatal health, family planning evidence base. |
| Aging and geriatrics | EXTEND `pathophysiology` or `public-health` | 8-10 | Missing: geriatric assessment, frailty syndrome, polypharmacy, age-related disease mechanisms, healthy aging. |

---

## Psychology

Existing courses: 8 (research-methods through clinical-psychology).
Clinical (80), cognitive-neuroscience (67), psychometrics (73), biological (88),
cognitive (88), social (88), research-methods (90), developmental (86).

### P1 -- Important Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Industrial-organizational psychology | NEW COURSE `industrial-organizational-psychology` (advanced) | 20-25 | Absent. Job analysis, personnel selection, organizational behavior, leadership research, work motivation, training/development, organizational justice. A major applied psychology subdiscipline. |
| Behavioral genetics | EXTEND `biological-psychology` | 10-15 | Biological psychology (88 topics) covers neuroscience. Missing: twin studies, heritability estimation, gene-behavior pathways, molecular behavioral genetics, epigenetics of behavior. |

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Neuropsychological assessment | EXTEND `cognitive-neuroscience` or `clinical-psychology` | 8-12 | Missing: neuropsych test batteries, lesion studies methods, cognitive rehabilitation, brain-behavior relationships (clinical), forensic neuropsychology. |
| Psychotherapy process research | EXTEND `clinical-psychology` | 8-10 | Missing: therapeutic alliance research, common factors, treatment mechanisms, process-outcome linkage, psychotherapy integration. |
| Quantitative methods (psychology) | EXTEND `psychometrics` or `research-methods-psychology` | 10-15 | Psychometrics (73 topics) covers test theory. Missing: SEM, multilevel modeling, meta-analysis in psychology, Bayesian methods in psychology, missing data methods. Could extend either course. |

---

## Economics

Existing courses: 7 (microeconomics through development-economics).
Econometrics (105), advanced-micro (76), advanced-macro (59), financial (111),
development (64), micro (109), macro (101).

### P1 -- Important Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Behavioral/experimental economics | NEW COURSE `behavioral-economics` (advanced) | 20-25 | Advanced micro has `prospect-theory`; financial economics has behavioral finance topics. But no systematic treatment: experimental methodology, bounded rationality, heuristics and biases (formal), nudge theory, neuroeconomics, social preferences. |
| Public economics / optimal taxation | EXTEND `advanced-microeconomics` | 12-15 | Missing: optimal tax theory, public goods (formal), mechanism design for public policy, fiscal federalism, social insurance economics. Natural extension of advanced micro. |
| Labor economics | NEW COURSE `labor-economics` (advanced) | 20-25 | Absent. Human capital theory, search and matching, wage determination, labor market discrimination, immigration economics, minimum wage economics. |

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Environmental/resource economics | NEW COURSE `environmental-economics` (advanced) | 15-20 | Absent. Externalities (formal), Pigouvian taxes, cap-and-trade, natural resource management, sustainability economics, climate economics. |
| Health economics | CROSS-DOMAIN (see Health & Human Development) | 0 | Covered in health domain proposal above. Cross-link rather than duplicate. |

---

## Social Sciences

Existing courses: 7 (sociology through international-relations-theory).
Sociology (75), anthropology (76), political-science (58), research-methods (78),
human-geography (74), sociological-theory (63), international-relations (62).

### P1 -- Important Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Comparative politics | EXTEND `political-science` | 12-15 | Political science (58 topics) covers basics. Missing: regime types (systematic), democratization theory, electoral systems comparison, party systems, political institutions comparison, state capacity. |
| Demography | NEW COURSE `demography` (advanced) | 20-25 | Absent. Population dynamics, fertility/mortality analysis, life tables, migration models, population projections, demographic transition theory. Cross-links to economics and health. |

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Urban sociology | EXTEND `sociology` | 8-12 | Missing: urban spatial theory, gentrification, urban poverty, neighborhood effects, urban political economy. Human geography has `informal-settlements-slums`. |
| STS (science and technology studies) | EXTEND `sociological-theory` or `research-methods-social-science` | 8-10 | Missing: social construction of technology, actor-network theory, laboratory studies, science policy, technoscience. |
| Advanced ethnographic methods | EXTEND `research-methods-social-science` | 8-10 | Research methods (78 topics) has basics. Missing: multi-sited ethnography, digital ethnography, autoethnography, visual methods, participatory research. |

---

## Literature

Existing courses: 6 (literary-analysis through comparative-literature).
Critical-theory (98), comparative-literature (71), literary-analysis (75),
fiction (80), poetry (80), drama (79).

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Creative writing | NEW COURSE `creative-writing` (advanced) | 20-25 | Absent. Craft of fiction, poetry workshop theory, revision processes, voice and style, workshop pedagogy, publishing industry, MFA culture. |
| Rhetoric and narrative theory | EXTEND `critical-theory` or `literary-analysis` | 10-12 | Critical theory (98 topics) covers theoretical frameworks. Missing: narratology (Genette, Bal), rhetorical theory (beyond basics), discourse analysis of literature, cognitive narratology. |
| Digital humanities | EXTEND `comparative-literature` or `critical-theory` | 8-10 | Missing: text mining for literature, distant reading, digital archives, computational stylistics, corpus-based literary analysis. |
| Book history / print culture | EXTEND `comparative-literature` | 6-8 | Missing: history of the book, material text studies, reception history, censorship history, publishing history. |
| Translation studies | EXTEND `comparative-literature` | 8-10 | Missing: translation theory, domestication/foreignization, cultural transfer, machine translation and literature, world literature theory. |

---

## History

Existing courses: 6 (historical-methods through historiography).
Historiography (93), historical-methods (102), modern (101), early-modern (100),
medieval (104), ancient (102).

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Area studies (expert depth) | EXTEND existing period courses | 15-20 | Coverage is chronological not regional. Missing: South Asian history depth, African history depth, Latin American history depth, East Asian history depth. Distribute across existing period courses rather than new courses. |
| Digital history | EXTEND `historiography` or `historical-methods` | 6-8 | Missing: digital archives, GIS for historians, computational text analysis, digital public history. |
| Environmental history | EXTEND `historiography` or `modern-history` | 8-10 | Missing: environmental history methodology, climate history, conservation history, energy history. |
| Public history | EXTEND `historiography` | 6-8 | Missing: museum studies, oral history methods, heritage management, community history, historical memory. |
| Cliometrics | EXTEND `historiography` or `historical-methods` | 6-8 | Missing: quantitative history methods, economic history methodology, historical demography methods, time-series analysis for history. |

---

## Philosophy

Existing courses: 9 (logic-and-critical-thinking through applied-rationality).
Ethics (94), metaphysics (95), epistemology (93), philosophy-of-mind (92),
philosophy-of-science (56), philosophy-of-language (73), political-philosophy (89),
applied-rationality (30), logic-and-critical-thinking (93).

### P1 -- Important Gaps

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Continental philosophy | NEW COURSE `continental-philosophy` (advanced/expert) | 25-30 | Existing courses have scattered references (Heidegger in aesthetics, phenomenology mentions). Missing systematic treatment: phenomenology (Husserl, Merleau-Ponty), existentialism, hermeneutics, critical theory (Frankfurt School), post-structuralism, deconstruction. A major philosophical tradition entirely unrepresented as a course. |
| Advanced logic | CROSS-DOMAIN (formal-sciences has propositional-and-predicate-logic (96), model-theory (74)) | 10-15 | Formal sciences covers this well. May need additions: non-classical logics (paraconsistent, fuzzy, relevance), philosophical logic, modal logic (if not already covered). Check formal-sciences coverage before adding. |

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Bioethics (expanded) | EXTEND `ethics` | 8-10 | Ethics (94 topics) has `bioethics`, `moral-status`, `applied-ethics-frameworks`. Missing: research ethics, neuroethics, genetic ethics, end-of-life ethics, reproductive ethics, environmental ethics (philosophical). |
| Philosophy of religion | EXTEND `metaphysics` or `epistemology` | 10-12 | Missing: arguments for/against God's existence, problem of evil, religious epistemology, faith and reason, divine attributes, religious pluralism. |
| Aesthetics (cross-domain) | CROSS-DOMAIN (arts `aesthetic-theory` has 74 topics) | 5-8 | Arts domain has substantial aesthetic theory. Philosophy side may want: analytic aesthetics, philosophy of music, philosophy of film, beauty and sublimity (philosophical). Small additions. |

---

## Arts & Aesthetics

Existing courses: 5 (visual-elements through aesthetic-theory).
Aesthetic-theory (74), art-history (90), design-principles (91),
drawing-and-painting (91), visual-elements (91).

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Film studies | NEW COURSE `film-studies` (advanced) | 20-25 | Absent. Film theory, cinematography analysis, montage theory, documentary theory, film genre studies, auteur theory, national cinemas. Art history has some photography/film references. |
| Studio art (expanded) | EXTEND `drawing-and-painting` | 8-12 | Drawing-and-painting (91 topics) covers 2D. Missing: sculpture, printmaking methods, installation art, mixed media, digital art techniques. |
| Architecture theory | EXTEND `design-principles` or `aesthetic-theory` | 10-12 | Missing: architectural theory, spatial design, urban design theory, architectural history (as theory), sustainable design philosophy. |
| Curatorial studies | EXTEND `art-history` or `aesthetic-theory` | 6-8 | Missing: exhibition design, museum studies, collection management, contemporary curation, public art commissioning. |
| Photography theory | EXTEND `art-history` or `aesthetic-theory` | 6-8 | Art history has `photography-and-modernism`. Missing: photographic theory, documentary photography, digital photography theory, image ethics. |

---

## Music

Existing courses: 6 (music-theory-fundamentals through advanced-music-theory).
Advanced-music-theory (96), composition (105), music-history (97),
harmony (94), ear-training (98), music-theory-fundamentals (99).

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Ethnomusicology | NEW COURSE `ethnomusicology` (advanced) | 20-25 | Music history has `global-music-systems-and-exchange`, `folk-traditions-and-art-music`. Missing systematic: world music systems, fieldwork methods, music and cultural identity, music and politics, non-Western music theory. |
| Music cognition | EXTEND `advanced-music-theory` | 8-10 | Advanced theory has `psychoacoustics-perception-theory`. Missing: music and emotion (cognitive), rhythm cognition, pitch perception models, music and memory, developmental music cognition. |
| Music technology | EXTEND `composition` or NEW COURSE | 12-15 | Composition (105 topics) may cover some. Missing: digital audio theory, synthesis methods, music information retrieval, live electronics, spatial audio, music production theory. |
| Music pedagogy | EXTEND `music-theory-fundamentals` | 6-8 | Missing: music education methods, Kodaly/Orff/Suzuki, instrumental pedagogy, assessment in music, music curriculum design. |
| Popular music studies | EXTEND `music-history` | 8-10 | Music history has jazz, blues, rock-and-roll. Missing: hip-hop studies, electronic dance music, popular music theory, cultural studies of pop, music industry economics. |

---

## Language & Communication

Existing courses: 6 (early-language-foundations through advanced-linguistics).
Linguistics (102), advanced-linguistics (88), rhetoric-and-composition (105).

### P2 -- Nice to Have

| Gap Area | Action | Est. Topics | Notes |
|----------|--------|-------------|-------|
| Sociolinguistics | EXTEND `linguistics` or `advanced-linguistics` | 8-12 | Linguistics has `sociolinguistics-intro`, `social-variables-in-variation`, `language-attitudes-and-ideology`, `dialect-and-regional-variation`. Advanced linguistics has some too. Missing: variationist sociolinguistics (formal), language policy, language endangerment, code-switching theory. Smaller gap than initially assessed. |
| Psycholinguistics | EXTEND `advanced-linguistics` | 8-10 | Advanced linguistics has `lexical-access-word-recognition`, `prediction-in-language-processing`, `working-memory-sentence-comprehension`, `sentence-parsing-garden-paths`. Missing: bilingual processing, language production models, eye-tracking methods, computational psycholinguistics. Partially covered. |
| Corpus linguistics | EXTEND `advanced-linguistics` | 8-10 | Missing: corpus design, concordance analysis, collocation statistics, corpus annotation, learner corpus research, corpus-based grammar. |
| Historical linguistics | EXTEND `linguistics` | 6-8 | Linguistics has `historical-linguistics`, `comparative-method-linguistics`, `sound-change-and-reconstruction`. Advanced linguistics has `sound-change-mechanisms-diachronic`, `grammaticalization`. Mostly covered. Add: internal reconstruction, areal linguistics, language family classification. Small gap. |
| Discourse analysis | EXTEND `advanced-linguistics` | 6-8 | Linguistics has `discourse-analysis`. Advanced linguistics has `discourse-coherence-relations`, `discourse-representation-theory`. Missing: critical discourse analysis, multimodal discourse, institutional discourse. Small gap. |

---

## Summary

### New Courses Proposed

| Domain | Course | Stage | Est. Topics | Priority |
|--------|--------|-------|-------------|----------|
| Mathematics | `algebraic-topology` | expert | 30-35 | P0 |
| Mathematics | `partial-differential-equations` | advanced/expert | 30-35 | P0 |
| Mathematics | `differential-geometry` | advanced/expert | 30-35 | P0 |
| Mathematics | `commutative-algebra` | expert | 25-30 | P1 |
| Mathematics | `stochastic-processes` | expert | 20-25 | P1 |
| Mathematics | `representation-theory` | expert | 25-30 | P1 |
| Computer Science | `machine-learning-theory` | expert | 25-30 | P0 |
| Computer Science | `cryptography` | advanced/expert | 30-35 | P0 |
| Computer Science | `quantum-computing` | advanced/expert | 25-30 | P0 |
| Computer Science | `information-theory` | advanced/expert | 25-30 | P1 |
| Computer Science | `advanced-algorithms` | expert | 20-25 | P1 |
| Computer Science | `formal-methods` | expert | 20-25 | P1 |
| Physics | `quantum-field-theory` | expert | 30-35 | P0 |
| Physics | `general-relativity` | expert | 25-30 | P0 |
| Physics | `condensed-matter-physics` | expert | 30-35 | P0 |
| Physics | `nonlinear-dynamics` | advanced/expert | 20-25 | P1 |
| Physics | `particle-physics` | expert | 25-30 | P1 |
| Physics | `plasma-physics` | expert | 20-25 | P2 |
| Physics | `atomic-molecular-optical` | expert | 20-25 | P2 |
| Chemistry | `inorganic-chemistry` | formal-systems/advanced | 30-35 | P0 |
| Chemistry | `materials-chemistry` | advanced/expert | 20-25 | P1 |
| Chemistry | `environmental-chemistry` | advanced | 15-20 | P2 |
| Biology | `genomics-and-bioinformatics` | advanced/expert | 25-30 | P0 |
| Biology | `systems-biology` | expert | 20-25 | P1 |
| Biology | `developmental-biology` | advanced/expert | 25-30 | P1 |
| Biology | `structural-biology` | expert | 20-25 | P1 |
| Earth & Space | `remote-sensing-and-gis` | advanced | 25-30 | P1 |
| Earth & Space | `geochemistry` | expert | 25-30 | P1 |
| Health | `biostatistics` | advanced/expert | 25-30 | P1 |
| Health | `health-economics` | advanced | 20-25 | P1 |
| Psychology | `industrial-organizational-psychology` | advanced | 20-25 | P1 |
| Economics | `behavioral-economics` | advanced | 20-25 | P1 |
| Economics | `labor-economics` | advanced | 20-25 | P1 |
| Economics | `environmental-economics` | advanced | 15-20 | P2 |
| Social Sciences | `demography` | advanced | 20-25 | P1 |
| Philosophy | `continental-philosophy` | advanced/expert | 25-30 | P1 |
| Literature | `creative-writing` | advanced | 20-25 | P2 |
| Arts & Aesthetics | `film-studies` | advanced | 20-25 | P2 |
| Music | `ethnomusicology` | advanced | 20-25 | P2 |

### Existing Course Extensions Proposed

| Domain | Target Course | Est. Topics | Priority |
|--------|---------------|-------------|----------|
| Mathematics | graph-theory-and-combinatorics | 15-20 | P2 |
| Mathematics | numerical-analysis | 15-20 | P2 |
| Formal Sciences | category-theory | 10-15 | P2 |
| Formal Sciences | set-theory | 15-20 | P1 |
| Computer Science | databases | 10-15 | P2 |
| Computer Science | compilers | 10-15 | P2 |
| Computer Science | computer-architecture | 10-15 | P2 |
| Computer Science | operating-systems + distributed-systems | 10-15 | P2 |
| Physics | classical-mechanics | 15-20 | P1 |
| Physics | modern-physics | 10-15 | P2 |
| Physics | astronomy (earth-and-space) | 15-20 | P2 |
| Chemistry | organic-chemistry | 15-20 | P1 |
| Chemistry | analytical-chemistry / physical-chemistry (spectroscopy) | 10-15 | P2 |
| Chemistry | physical-chemistry (computational) | 10-15 | P2 |
| Chemistry | physical-chemistry (electrochemistry) | 10-15 | P2 |
| Chemistry | physical-chemistry (thermo) | 10-12 | P2 |
| Chemistry | physical-chemistry (surface) | 8-12 | P2 |
| Biology | biochemistry (bio domain, proteomics) | 10-15 | P2 |
| Biology | biochemistry (bio domain, chem additions) | 10-15 | P1 |
| Biology | genetics-and-molecular-biology (epigenetics) | 10-15 | P1 |
| Biology | genetics-and-molecular-biology (synthetic bio) | 15-20 | P2 |
| Biology | cell-biology (stem cells) | 8-12 | P2 |
| Biology | microbiology (virology expert) | 5-10 | P2 |
| Biology | ecology-and-evolution + evolutionary-biology (pop gen) | 5-10 | P1 |
| Earth & Space | geology (volcanology) | 10-15 | P1 |
| Earth & Space | geology (sedimentology) | 10-15 | P2 |
| Earth & Space | climate-science (atmospheric chem) | 10-15 | P2 |
| Earth & Space | geophysics (space weather) | 8-12 | P2 |
| Earth & Space | planetary-science (astrobiology) | 8-10 | P2 |
| Earth & Space | geology (glaciology) | 8-12 | P2 |
| Health | epidemiology (pharmacoepi) | 8-10 | P2 |
| Health | epidemiology (genetic epi) | 8-10 | P2 |
| Health | public-health (various) | 24-32 | P2 |
| Health | pathophysiology (aging) | 8-10 | P2 |
| Psychology | biological-psychology (behavioral genetics) | 10-15 | P1 |
| Psychology | clinical-psychology (neuropsych + psychotherapy) | 16-22 | P2 |
| Psychology | psychometrics/research-methods (quant methods) | 10-15 | P2 |
| Economics | advanced-microeconomics (public econ) | 12-15 | P1 |
| Social Sciences | political-science (comparative) | 12-15 | P1 |
| Social Sciences | sociology (urban) | 8-12 | P2 |
| Social Sciences | sociological-theory (STS) | 8-10 | P2 |
| Social Sciences | research-methods (ethnographic) | 8-10 | P2 |
| Literature | critical-theory (narrative/rhetoric) | 10-12 | P2 |
| Literature | comparative-literature (digital hum + book + translation) | 22-28 | P2 |
| History | existing period courses (area studies) | 15-20 | P2 |
| History | historiography (digital + public + enviro + cliometrics) | 26-34 | P2 |
| Philosophy | ethics (bioethics expanded) | 8-10 | P2 |
| Philosophy | metaphysics/epistemology (phil of religion) | 10-12 | P2 |
| Philosophy | formal-sciences (advanced logic) | 10-15 | P1 |
| Arts & Aesthetics | drawing-and-painting (studio) | 8-12 | P2 |
| Arts & Aesthetics | design-principles/aesthetic-theory (architecture) | 10-12 | P2 |
| Arts & Aesthetics | art-history/aesthetic-theory (curatorial + photo) | 12-16 | P2 |
| Music | advanced-music-theory (cognition) | 8-10 | P2 |
| Music | composition (technology) | 12-15 | P2 |
| Music | music-theory-fundamentals (pedagogy) | 6-8 | P2 |
| Music | music-history (popular) | 8-10 | P2 |
| Language | linguistics/advanced-linguistics (socio + psycho + corpus + hist + discourse) | 36-48 | P2 |

### Topic Count Estimates by Priority

| Priority | New Course Topics | Extension Topics | Total |
|----------|-------------------|------------------|-------|
| P0 | ~310-365 (10 courses) | 0 | **310-365** |
| P1 | ~380-445 (14 courses) | ~155-205 | **535-650** |
| P2 | ~155-195 (6 courses) | ~395-520 | **550-715** |
| **TOTAL** | **~845-1,005 (30 courses)** | **~550-725** | **~1,395-1,730** |

### Recommended Phasing

**Phase 1 (P0 -- ~310-365 topics, 10 new courses):**
Focus on the 10 entirely missing core subdisciplines. These represent the largest gaps
in the graph's claim to comprehensive expert coverage.
- Math: algebraic-topology, partial-differential-equations, differential-geometry
- CS: machine-learning-theory, cryptography, quantum-computing
- Physics: quantum-field-theory, general-relativity, condensed-matter-physics
- Chemistry: inorganic-chemistry

**Phase 2 (P1 -- ~535-650 topics, 14 new courses + extensions):**
Important gaps that significantly limit domain usefulness at the expert level.
Priority within P1: information-theory, advanced-algorithms, continental-philosophy,
genomics-and-bioinformatics, nonlinear-dynamics, commutative-algebra.

**Phase 3 (P2 -- ~550-715 topics, 6 new courses + extensions):**
Completeness and polish. Many of these are small extensions (6-15 topics) to
already-substantial courses.
