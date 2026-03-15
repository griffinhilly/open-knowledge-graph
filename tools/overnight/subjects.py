"""Subject queue for overnight knowledge graph generation.

MATH_COURSES: individual math courses to populate.
DOMAIN_SPECS: new domains, each expanded into per-course subjects at runtime.
build_queue(): returns the full flat execution queue.
"""

# =========================================================================
# MATH COURSES — each generates topics for one existing math course
# =========================================================================

MATH_COURSES = [
    {
        "id": "math-kindergarten",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "kindergarten",
        "course_title": "Kindergarten Math",
        "stage": "pre-formal",
        "target_topics": 25,
        "prereq_domains": [],
        "guidance": (
            "Counting and cardinality (1-20), number recognition and writing, "
            "one-to-one correspondence, comparing quantities (more/less/same), "
            "basic 2D shapes (circle, square, triangle, rectangle), sorting and "
            "classifying by attributes, simple repeating patterns (AB, ABC), "
            "combining and separating small groups (pre-addition/subtraction), "
            "positional words (above/below/beside), measurement comparison "
            "(longer/shorter, heavier/lighter). These are ROOT topics — most "
            "will have empty prerequisites []."
        ),
    },
    {
        "id": "math-1st-grade",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "1st-grade",
        "course_title": "1st Grade Math",
        "stage": "pre-formal",
        "target_topics": 28,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Addition and subtraction within 20, place value (tens and ones), "
            "comparing two-digit numbers, measuring length with non-standard units, "
            "telling time to the hour and half-hour, intro to data (tally charts, "
            "picture graphs), 2D vs 3D shapes, composing and decomposing shapes, "
            "skip counting by 2s/5s/10s, number line introduction, word problems "
            "with addition/subtraction, half and quarter of shapes. Prerequisites "
            "should reference kindergarten topics where appropriate."
        ),
    },
    {
        "id": "math-2nd-grade",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "2nd-grade",
        "course_title": "2nd Grade Math",
        "stage": "concrete-operations",
        "target_topics": 30,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Addition and subtraction within 100 (with regrouping), place value "
            "to 1000, measuring length in inches/cm/feet/meters, money (counting "
            "coins and bills, making change), introduction to multiplication as "
            "equal groups and arrays, time to nearest 5 minutes, bar graphs and "
            "picture graphs, odd and even numbers, mental math strategies, "
            "three-digit number comparison, estimation."
        ),
    },
    {
        "id": "math-3rd-grade",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "3rd-grade",
        "course_title": "3rd Grade Math",
        "stage": "concrete-operations",
        "target_topics": 32,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Multiplication and division facts to 100, properties of multiplication "
            "(commutative, associative, distributive), introduction to fractions "
            "(halves, thirds, fourths, sixths, eighths), fractions on a number line, "
            "area as covering with unit squares, perimeter of polygons, rounding to "
            "nearest 10 and 100, elapsed time, scaled bar graphs and pictographs, "
            "multi-step word problems, patterns in arithmetic. This course bridges "
            "into the existing 4th-grade topics."
        ),
    },
    {
        "id": "math-linear-algebra",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "linear-algebra",
        "course_title": "Linear Algebra",
        "stage": "formal-systems",
        "target_topics": 35,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Vectors in R^n (operations, dot product, cross product), matrix "
            "operations (addition, multiplication, transpose), systems of linear "
            "equations (row reduction, Gaussian elimination, RREF), linear "
            "transformations and their matrices, determinants (computation and "
            "properties), vector spaces and subspaces, linear independence, "
            "basis and dimension, rank and nullity, eigenvalues and eigenvectors, "
            "diagonalization, inner product spaces, orthogonality and Gram-Schmidt, "
            "least squares approximation. Prerequisites should reference algebra-2 "
            "and precalculus topics (systems of equations, matrices intro)."
        ),
    },
    {
        "id": "math-multivariable-calculus",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "multivariable-calculus",
        "course_title": "Multivariable Calculus",
        "stage": "formal-systems",
        "target_topics": 35,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Vectors in 3D space, vector-valued functions and space curves, "
            "partial derivatives, gradient and directional derivatives, tangent "
            "planes and linear approximation, optimization with Lagrange multipliers, "
            "double integrals (Cartesian and polar), triple integrals (Cartesian, "
            "cylindrical, spherical), change of variables and Jacobians, line "
            "integrals, conservative vector fields, Green's theorem, surface "
            "integrals, Stokes' theorem, divergence theorem. Prerequisites should "
            "reference calculus-2 and linear-algebra topics."
        ),
    },
    {
        "id": "math-methods-of-proof",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "methods-of-proof",
        "course_title": "Methods of Proof",
        "stage": "formal-systems",
        "target_topics": 25,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Propositional logic (statements, connectives, truth tables), logical "
            "equivalences, predicates and quantifiers, direct proof, proof by "
            "contrapositive, proof by contradiction, mathematical induction, "
            "strong induction, proof by cases/exhaustion, existence and uniqueness "
            "proofs, sets (union, intersection, complement, Cartesian product), "
            "relations (equivalence relations, partial orders), functions "
            "(injective, surjective, bijective), cardinality and countability. "
            "Prerequisites should reference algebra-1 and algebra-2 topics."
        ),
    },
    {
        "id": "math-probability-and-statistics",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "probability-and-statistics",
        "course_title": "Probability & Statistics",
        "stage": "formal-systems",
        "target_topics": 35,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Descriptive statistics (mean, median, mode, standard deviation), "
            "data visualization (histograms, boxplots, scatterplots), probability "
            "axioms and rules, conditional probability and Bayes' theorem, "
            "discrete random variables and distributions (binomial, Poisson, "
            "geometric), continuous distributions (uniform, normal, exponential), "
            "expected value and variance, sampling distributions, central limit "
            "theorem, confidence intervals, hypothesis testing (z-test, t-test, "
            "chi-square), linear regression and correlation, ANOVA introduction. "
            "Prerequisites should reference algebra-2 and calculus-1 topics."
        ),
    },
    {
        "id": "math-discrete-math",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "discrete-math",
        "course_title": "Discrete Math",
        "stage": "formal-systems",
        "target_topics": 30,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Combinatorics (counting principles, permutations, combinations, "
            "binomial coefficients), pigeonhole principle, inclusion-exclusion, "
            "graph theory (graphs, paths, cycles, trees, Euler/Hamilton circuits, "
            "planar graphs, graph coloring), recurrence relations and solving them, "
            "generating functions introduction, modular arithmetic and congruences, "
            "Boolean algebra, algorithmic thinking (Big-O, algorithm analysis), "
            "number theory basics (divisibility, primes, GCD, Euclidean algorithm). "
            "Prerequisites should reference algebra-2, methods-of-proof topics."
        ),
    },
]

# =========================================================================
# DOMAIN SPECS — each expanded into per-course subjects by build_queue()
# =========================================================================

DOMAIN_SPECS = [
    # --- TIER 1: Heavy math overlap ---
    {
        "domain": "physics",
        "domain_title": "Physics",
        "domain_description": (
            "The study of matter, energy, and the fundamental forces governing "
            "the natural world, from subatomic particles to the structure of the "
            "universe. Heavily mathematical — every physics concept builds on "
            "mathematical prerequisites."
        ),
        "target_topics_per_course": 30,
        "prereq_domains": ["mathematics"],
        "courses": [
            {"id": "classical-mechanics", "title": "Classical Mechanics", "stage": "formal-systems"},
            {"id": "electricity-and-magnetism", "title": "Electricity & Magnetism", "stage": "formal-systems"},
            {"id": "thermodynamics", "title": "Thermodynamics", "stage": "formal-systems"},
            {"id": "waves-and-optics", "title": "Waves & Optics", "stage": "formal-systems"},
            {"id": "modern-physics", "title": "Modern Physics", "stage": "advanced"},
        ],
        "course_guidance": {
            "classical-mechanics": (
                "Kinematics (1D and 2D), Newton's laws, free-body diagrams, friction, "
                "work and energy, conservation of energy, momentum and impulse, "
                "collisions, circular motion, rotational kinematics and dynamics, "
                "torque, angular momentum, oscillations (SHM, springs, pendulums), "
                "gravitation (Newton's law, orbits, Kepler's laws)."
            ),
            "electricity-and-magnetism": (
                "Electric charge and Coulomb's law, electric field, Gauss's law, "
                "electric potential, capacitors and dielectrics, DC circuits (Ohm's law, "
                "Kirchhoff's rules, RC circuits), magnetic fields and forces, "
                "Biot-Savart law, Ampere's law, Faraday's law and induction, "
                "inductors, AC circuits, Maxwell's equations introduction."
            ),
            "thermodynamics": (
                "Temperature and thermal equilibrium, heat and heat transfer, "
                "ideal gas law, kinetic theory, first law of thermodynamics, "
                "work in thermodynamic processes, heat engines and efficiency, "
                "second law and entropy, Carnot cycle, phase transitions."
            ),
            "waves-and-optics": (
                "Wave properties (wavelength, frequency, speed), superposition, "
                "standing waves, sound waves, Doppler effect, interference, "
                "diffraction, reflection and refraction, Snell's law, thin lenses, "
                "mirrors, optical instruments, polarization."
            ),
            "modern-physics": (
                "Special relativity (postulates, time dilation, length contraction, "
                "mass-energy equivalence), blackbody radiation, photoelectric effect, "
                "Bohr model, wave-particle duality, de Broglie wavelength, "
                "uncertainty principle, Schrödinger equation introduction, "
                "quantum numbers, nuclear structure, radioactive decay."
            ),
        },
    },
    {
        "domain": "computer-science",
        "domain_title": "Computer Science & Information",
        "domain_description": (
            "The study of computation, algorithms, data structures, and information "
            "processing. Spans from practical programming to theoretical foundations "
            "of what can and cannot be computed."
        ),
        "target_topics_per_course": 28,
        "prereq_domains": ["mathematics"],
        "courses": [
            {"id": "programming-fundamentals", "title": "Programming Fundamentals", "stage": "abstract-reasoning"},
            {"id": "data-structures-and-algorithms", "title": "Data Structures & Algorithms", "stage": "formal-systems"},
            {"id": "computer-architecture", "title": "Computer Architecture", "stage": "formal-systems"},
            {"id": "operating-systems", "title": "Operating Systems", "stage": "formal-systems"},
            {"id": "databases", "title": "Databases", "stage": "formal-systems"},
            {"id": "theory-of-computation", "title": "Theory of Computation", "stage": "advanced"},
        ],
        "course_guidance": {
            "programming-fundamentals": (
                "Variables and types, operators, control flow (if/else, loops), "
                "functions, parameters and return values, scope, recursion, "
                "arrays/lists, strings, basic I/O, debugging, intro to classes "
                "and objects, error handling, file I/O."
            ),
            "data-structures-and-algorithms": (
                "Complexity analysis (Big-O), linked lists, stacks, queues, "
                "trees (binary, BST, AVL), heaps and priority queues, hash tables, "
                "graphs (representation, BFS, DFS), sorting algorithms (merge, quick, "
                "heap), searching, dynamic programming, greedy algorithms, "
                "divide and conquer, shortest path algorithms."
            ),
            "computer-architecture": (
                "Binary and hexadecimal, logic gates (AND, OR, NOT, XOR), "
                "combinational circuits, sequential circuits (flip-flops, registers), "
                "CPU architecture (ALU, control unit, datapath), instruction sets, "
                "memory hierarchy (cache, RAM, disk), pipelining, I/O systems."
            ),
            "operating-systems": (
                "Processes and threads, process scheduling, inter-process communication, "
                "synchronization (mutexes, semaphores), deadlocks, memory management "
                "(paging, segmentation), virtual memory, file systems, "
                "I/O management, security basics."
            ),
            "databases": (
                "Relational model, SQL (SELECT, JOIN, GROUP BY, subqueries), "
                "ER diagrams, normalization (1NF through BCNF), indexing (B-trees, "
                "hash indexes), transactions and ACID, concurrency control, "
                "query optimization, NoSQL concepts, CAP theorem."
            ),
            "theory-of-computation": (
                "Finite automata (DFA, NFA), regular expressions, regular languages, "
                "context-free grammars, pushdown automata, pumping lemma, "
                "Turing machines, decidability, halting problem, reducibility, "
                "complexity classes (P, NP, NP-complete), Cook-Levin theorem."
            ),
        },
    },
    {
        "domain": "formal-sciences-and-logic",
        "domain_title": "Formal Sciences & Logic",
        "domain_description": (
            "The study of formal systems, abstract structures, and deductive reasoning. "
            "Extends beyond mathematics into philosophical logic, metalogic, and the "
            "foundations of formal reasoning itself."
        ),
        "target_topics_per_course": 20,
        "prereq_domains": ["mathematics"],
        "courses": [
            {"id": "propositional-and-predicate-logic", "title": "Propositional & Predicate Logic", "stage": "formal-systems"},
            {"id": "set-theory", "title": "Set Theory", "stage": "formal-systems"},
            {"id": "computability-and-complexity", "title": "Computability & Complexity", "stage": "advanced"},
            {"id": "category-theory", "title": "Category Theory", "stage": "advanced"},
        ],
        "course_guidance": {
            "propositional-and-predicate-logic": (
                "Syntax vs semantics, proof systems (natural deduction, sequent calculus), "
                "soundness and completeness theorems, compactness, model theory basics, "
                "Gödel's incompleteness theorems overview, non-classical logics "
                "(intuitionistic, modal) introduction."
            ),
            "set-theory": (
                "Naive vs axiomatic set theory, ZFC axioms, ordinal and cardinal "
                "numbers, transfinite induction, axiom of choice and equivalents, "
                "continuum hypothesis, well-ordering theorem."
            ),
            "computability-and-complexity": (
                "Lambda calculus, recursive functions, Church-Turing thesis, "
                "halting problem, Rice's theorem, Kolmogorov complexity intro, "
                "time and space complexity, NP-completeness, reductions, "
                "probabilistic computation basics."
            ),
            "category-theory": (
                "Categories (objects and morphisms), functors, natural transformations, "
                "universal properties, products and coproducts, limits and colimits, "
                "adjunctions, Yoneda lemma, monads introduction."
            ),
        },
    },

    # --- TIER 2: Well-structured sciences ---
    {
        "domain": "chemistry",
        "domain_title": "Chemistry",
        "domain_description": (
            "The study of matter, its properties, composition, structure, and the "
            "changes it undergoes during chemical reactions. Bridges physics and "
            "biology through understanding of atomic and molecular behavior."
        ),
        "target_topics_per_course": 28,
        "prereq_domains": ["mathematics", "physics"],
        "courses": [
            {"id": "general-chemistry", "title": "General Chemistry", "stage": "formal-systems"},
            {"id": "organic-chemistry", "title": "Organic Chemistry", "stage": "formal-systems"},
            {"id": "physical-chemistry", "title": "Physical Chemistry", "stage": "advanced"},
            {"id": "analytical-chemistry", "title": "Analytical Chemistry", "stage": "advanced"},
        ],
        "course_guidance": {
            "general-chemistry": (
                "Atomic structure, electron configuration, periodic trends, "
                "chemical bonding (ionic, covalent, metallic), Lewis structures, "
                "VSEPR, stoichiometry, gas laws, solutions, acids and bases, "
                "chemical equilibrium, thermochemistry, electrochemistry, kinetics."
            ),
            "organic-chemistry": (
                "Nomenclature, functional groups, stereochemistry (chirality, "
                "enantiomers, diastereomers), reaction mechanisms (SN1, SN2, E1, E2), "
                "alkanes/alkenes/alkynes, aromatic compounds, alcohols/ethers, "
                "carbonyls, carboxylic acid derivatives, amines, spectroscopy basics."
            ),
            "physical-chemistry": (
                "Quantum chemistry basics, molecular orbital theory, spectroscopy "
                "theory, statistical thermodynamics, chemical kinetics (advanced), "
                "surface chemistry, transport properties."
            ),
            "analytical-chemistry": (
                "Gravimetric and volumetric analysis, spectroscopic methods "
                "(UV-Vis, IR, NMR, mass spectrometry), chromatography (GC, HPLC), "
                "electroanalytical methods, quality assurance, method validation."
            ),
        },
    },
    {
        "domain": "biology",
        "domain_title": "Biology",
        "domain_description": (
            "The study of living organisms, their structure, function, growth, "
            "evolution, and interactions. From molecular machinery inside cells "
            "to ecosystems spanning continents."
        ),
        "target_topics_per_course": 28,
        "prereq_domains": ["mathematics", "chemistry"],
        "courses": [
            {"id": "cell-biology", "title": "Cell Biology", "stage": "abstract-reasoning"},
            {"id": "genetics-and-molecular-biology", "title": "Genetics & Molecular Biology", "stage": "formal-systems"},
            {"id": "physiology", "title": "Physiology", "stage": "formal-systems"},
            {"id": "ecology-and-evolution", "title": "Ecology & Evolution", "stage": "formal-systems"},
            {"id": "microbiology", "title": "Microbiology", "stage": "formal-systems"},
        ],
        "course_guidance": {
            "cell-biology": (
                "Cell theory, prokaryotic vs eukaryotic cells, organelles and their "
                "functions, cell membrane and transport, enzymes, cellular respiration "
                "(glycolysis, Krebs, ETC), photosynthesis, cell cycle and mitosis, meiosis."
            ),
            "genetics-and-molecular-biology": (
                "DNA structure and replication, transcription, translation, "
                "gene regulation, Mendelian genetics, non-Mendelian inheritance, "
                "genetic mapping, PCR, gel electrophoresis, genomics overview, "
                "CRISPR and gene editing."
            ),
            "physiology": (
                "Nervous system, endocrine system, cardiovascular system, "
                "respiratory system, digestive system, musculoskeletal system, "
                "immune system, homeostasis and feedback loops."
            ),
            "ecology-and-evolution": (
                "Population ecology, community ecology, ecosystems and energy flow, "
                "biogeochemical cycles, natural selection, speciation, phylogenetics, "
                "biodiversity and conservation."
            ),
            "microbiology": (
                "Bacterial structure and metabolism, viruses, fungi, "
                "host-pathogen interactions, immunology basics, antimicrobials "
                "and resistance, microbial ecology, biotechnology applications."
            ),
        },
    },
    {
        "domain": "earth-and-space-sciences",
        "domain_title": "Earth & Space Sciences",
        "domain_description": (
            "The study of Earth's systems and the broader universe. From minerals "
            "and plate tectonics to stellar evolution and cosmology."
        ),
        "target_topics_per_course": 22,
        "prereq_domains": ["mathematics", "physics", "chemistry"],
        "courses": [
            {"id": "geology", "title": "Geology", "stage": "abstract-reasoning"},
            {"id": "meteorology-and-climate", "title": "Meteorology & Climate", "stage": "abstract-reasoning"},
            {"id": "oceanography", "title": "Oceanography", "stage": "abstract-reasoning"},
            {"id": "astronomy", "title": "Astronomy & Astrophysics", "stage": "formal-systems"},
        ],
        "course_guidance": {
            "geology": (
                "Minerals and rocks (igneous, sedimentary, metamorphic), plate "
                "tectonics, earthquakes and seismology, volcanoes, weathering "
                "and erosion, geological time scale, fossils, hydrogeology."
            ),
            "meteorology-and-climate": (
                "Atmosphere composition and structure, weather systems and fronts, "
                "pressure systems, precipitation, climate zones, climate change "
                "science, greenhouse effect, Coriolis effect, severe weather."
            ),
            "oceanography": (
                "Ocean circulation (thermohaline, wind-driven), waves and tides, "
                "marine ecosystems, ocean chemistry, seafloor features and spreading, "
                "El Niño/La Niña, coral reefs."
            ),
            "astronomy": (
                "Celestial mechanics, solar system (planets, moons, asteroids), "
                "stellar classification and HR diagram, stellar evolution, "
                "galaxies and galaxy clusters, cosmology (Big Bang, expansion, "
                "dark matter/energy), telescopes and observation methods."
            ),
        },
    },
    {
        "domain": "economics",
        "domain_title": "Economics & Political Economy",
        "domain_description": (
            "The study of how societies allocate scarce resources, from individual "
            "decision-making to national and global economic systems."
        ),
        "target_topics_per_course": 28,
        "prereq_domains": ["mathematics"],
        "courses": [
            {"id": "microeconomics", "title": "Microeconomics", "stage": "abstract-reasoning"},
            {"id": "macroeconomics", "title": "Macroeconomics", "stage": "abstract-reasoning"},
            {"id": "econometrics", "title": "Econometrics", "stage": "formal-systems"},
            {"id": "financial-economics", "title": "Financial Economics", "stage": "formal-systems"},
        ],
        "course_guidance": {
            "microeconomics": (
                "Supply and demand, elasticity, consumer theory (utility, "
                "indifference curves, budget constraints), producer theory (costs, "
                "profit maximization), market structures (perfect competition, "
                "monopoly, oligopoly), game theory basics, externalities, public goods."
            ),
            "macroeconomics": (
                "GDP and measurement, inflation, unemployment, aggregate supply "
                "and demand, fiscal policy, monetary policy, banking and money supply, "
                "IS-LM model, international trade and exchange rates, economic growth."
            ),
            "econometrics": (
                "Simple and multiple regression, hypothesis testing in regression, "
                "panel data, time series basics, instrumental variables, "
                "causal inference, difference-in-differences, regression discontinuity."
            ),
            "financial-economics": (
                "Present value and discounting, bond pricing, stock valuation, "
                "portfolio theory, CAPM, efficient market hypothesis, options "
                "pricing basics, risk and return, behavioral finance intro."
            ),
        },
    },

    # --- TIER 3: Structured but more branching ---
    {
        "domain": "psychology",
        "domain_title": "Psychology & Cognitive Science",
        "domain_description": (
            "The scientific study of mind and behavior, from neural mechanisms "
            "to social dynamics. Bridges biology, philosophy, and social science."
        ),
        "target_topics_per_course": 22,
        "prereq_domains": ["mathematics", "biology"],
        "courses": [
            {"id": "research-methods-psychology", "title": "Research Methods in Psychology", "stage": "abstract-reasoning"},
            {"id": "biological-psychology", "title": "Biological Psychology", "stage": "formal-systems"},
            {"id": "cognitive-psychology", "title": "Cognitive Psychology", "stage": "formal-systems"},
            {"id": "developmental-psychology", "title": "Developmental Psychology", "stage": "abstract-reasoning"},
            {"id": "social-psychology", "title": "Social Psychology", "stage": "abstract-reasoning"},
        ],
        "course_guidance": {
            "research-methods-psychology": (
                "Scientific method in psychology, experimental design, variables "
                "(IV, DV, confounds), sampling and populations, ethical guidelines, "
                "descriptive/correlational/experimental research, reliability "
                "and validity, basic statistical analysis for psychology."
            ),
            "biological-psychology": (
                "Neurons and neurotransmission, brain structure and function, "
                "nervous system organization, sensation and perception, "
                "consciousness and altered states, sleep, psychopharmacology."
            ),
            "cognitive-psychology": (
                "Attention, memory (encoding, storage, retrieval, types), "
                "language processing, problem solving and reasoning, decision "
                "making and cognitive biases, mental representations, expertise."
            ),
            "developmental-psychology": (
                "Prenatal development, Piaget's stages, attachment theory, "
                "language acquisition, moral development (Kohlberg, Gilligan), "
                "adolescent development, adult development and aging, "
                "nature vs nurture."
            ),
            "social-psychology": (
                "Social cognition, attitudes and persuasion, conformity "
                "(Asch), obedience (Milgram), group dynamics and groupthink, "
                "prejudice and discrimination, aggression, prosocial behavior, "
                "attribution theory."
            ),
        },
    },
    {
        "domain": "engineering",
        "domain_title": "Engineering & Technology",
        "domain_description": (
            "The application of scientific and mathematical principles to design, "
            "build, and optimize systems and structures."
        ),
        "target_topics_per_course": 22,
        "prereq_domains": ["mathematics", "physics", "chemistry"],
        "courses": [
            {"id": "statics-and-dynamics", "title": "Statics & Dynamics", "stage": "formal-systems"},
            {"id": "materials-science", "title": "Materials Science", "stage": "formal-systems"},
            {"id": "fluid-mechanics", "title": "Fluid Mechanics", "stage": "formal-systems"},
            {"id": "circuits-and-electronics", "title": "Circuits & Electronics", "stage": "formal-systems"},
            {"id": "control-systems", "title": "Control Systems", "stage": "advanced"},
        ],
        "course_guidance": {
            "statics-and-dynamics": (
                "Forces and moments, equilibrium of particles and rigid bodies, "
                "trusses and frames, friction, centroids and moments of inertia, "
                "kinematics of particles, Newton's laws applications, work-energy "
                "for systems, impulse-momentum."
            ),
            "materials-science": (
                "Crystal structure, defects, mechanical properties and testing, "
                "stress-strain behavior, failure modes (fracture, fatigue, creep), "
                "phase diagrams, heat treatment, polymers, ceramics, composites."
            ),
            "fluid-mechanics": (
                "Fluid statics and pressure, Bernoulli's equation, viscous flow, "
                "pipe flow (laminar and turbulent), boundary layers, drag and lift, "
                "dimensional analysis, open channel flow basics."
            ),
            "circuits-and-electronics": (
                "Circuit elements (R, L, C), Kirchhoff's laws, Thevenin/Norton "
                "equivalents, AC circuit analysis, impedance, filters, diodes, "
                "BJT and MOSFET transistors, operational amplifiers."
            ),
            "control-systems": (
                "Transfer functions, block diagrams, stability analysis (Routh), "
                "root locus, Bode plots, Nyquist criterion, PID control, "
                "state-space representation, controllability and observability."
            ),
        },
    },
    {
        "domain": "health-and-human-development",
        "domain_title": "Health & Human Development",
        "domain_description": (
            "The study of human health, wellness, and development across the "
            "lifespan. From anatomy to public health, nutrition to child development."
        ),
        "target_topics_per_course": 20,
        "prereq_domains": ["biology", "chemistry"],
        "courses": [
            {"id": "anatomy-and-physiology", "title": "Anatomy & Physiology", "stage": "abstract-reasoning"},
            {"id": "nutrition-science", "title": "Nutrition Science", "stage": "abstract-reasoning"},
            {"id": "public-health", "title": "Public Health", "stage": "abstract-reasoning"},
            {"id": "child-development", "title": "Child Development", "stage": "abstract-reasoning"},
        ],
        "course_guidance": {
            "anatomy-and-physiology": (
                "Body organization and terminology, skeletal system, muscular system, "
                "cardiovascular system, respiratory system, digestive system, "
                "nervous system, endocrine system, urinary system, reproductive "
                "system, integumentary system, lymphatic/immune system."
            ),
            "nutrition-science": (
                "Macronutrients (carbs, proteins, fats), micronutrients (vitamins, "
                "minerals), metabolism basics, dietary guidelines, nutritional "
                "assessment, food safety, sports nutrition, nutritional disorders."
            ),
            "public-health": (
                "Epidemiology basics, disease prevention levels, health promotion, "
                "environmental health, global health challenges, health policy "
                "and systems, biostatistics in public health, infectious disease "
                "surveillance."
            ),
            "child-development": (
                "Prenatal through adolescence, physical milestones, cognitive "
                "milestones, social-emotional development, attachment, play and "
                "learning, language development, parenting styles, developmental "
                "disorders and early intervention."
            ),
        },
    },

    # --- TIER 4: Humanities ---
    {
        "domain": "history",
        "domain_title": "History & Civilization",
        "domain_description": (
            "The study of human societies across time, from earliest civilizations "
            "to the modern world. Chronological structure provides natural ordering."
        ),
        "target_topics_per_course": 25,
        "prereq_domains": [],
        "courses": [
            {"id": "historical-methods", "title": "Historical Methods", "stage": "abstract-reasoning"},
            {"id": "ancient-civilizations", "title": "Ancient Civilizations", "stage": "abstract-reasoning"},
            {"id": "medieval-world", "title": "Medieval World", "stage": "abstract-reasoning"},
            {"id": "early-modern-period", "title": "Early Modern Period", "stage": "abstract-reasoning"},
            {"id": "modern-history", "title": "Modern History", "stage": "abstract-reasoning"},
        ],
        "course_guidance": {
            "historical-methods": (
                "Primary vs secondary sources, historiography, bias and perspective, "
                "periodization, causation in history, oral history, archaeological "
                "evidence, digital history tools."
            ),
            "ancient-civilizations": (
                "Mesopotamia, Egypt, Indus Valley, ancient China, ancient Greece "
                "(democracy, philosophy), Roman Republic and Empire, major religions "
                "origins, trade networks, key turning points."
            ),
            "medieval-world": (
                "Fall of Rome, Byzantine Empire, rise of Islam and Islamic Golden Age, "
                "feudalism, Crusades, Mongol Empire, medieval Africa (Mali, "
                "Great Zimbabwe), medieval Asia (Tang/Song China, Japan)."
            ),
            "early-modern-period": (
                "Renaissance, Reformation, Age of Exploration, Scientific Revolution, "
                "Enlightenment, Atlantic slave trade, colonialism, American Revolution, "
                "French Revolution."
            ),
            "modern-history": (
                "Industrial Revolution, nationalism and nation-states, World War I, "
                "Russian Revolution, World War II, Holocaust, Cold War, decolonization, "
                "civil rights movements, globalization, digital revolution."
            ),
        },
    },
    {
        "domain": "philosophy",
        "domain_title": "Philosophy & Ethics",
        "domain_description": (
            "The systematic study of fundamental questions about existence, knowledge, "
            "values, reason, mind, and language."
        ),
        "target_topics_per_course": 20,
        "prereq_domains": ["formal-sciences-and-logic"],
        "courses": [
            {"id": "logic-and-critical-thinking", "title": "Logic & Critical Thinking", "stage": "abstract-reasoning"},
            {"id": "epistemology", "title": "Epistemology", "stage": "formal-systems"},
            {"id": "metaphysics", "title": "Metaphysics", "stage": "formal-systems"},
            {"id": "ethics", "title": "Ethics", "stage": "abstract-reasoning"},
            {"id": "political-philosophy", "title": "Political Philosophy", "stage": "abstract-reasoning"},
            {"id": "philosophy-of-mind", "title": "Philosophy of Mind", "stage": "formal-systems"},
        ],
        "course_guidance": {
            "logic-and-critical-thinking": (
                "Arguments (premises and conclusions), validity and soundness, "
                "informal fallacies, deductive vs inductive reasoning, analogical "
                "reasoning, Socratic method, thought experiments, charity principle."
            ),
            "epistemology": (
                "Knowledge (JTB and Gettier problems), skepticism (Cartesian, external "
                "world), rationalism vs empiricism, foundationalism vs coherentism, "
                "reliabilism, testimony, epistemology of disagreement."
            ),
            "metaphysics": (
                "Substance and properties, causation, free will vs determinism, "
                "personal identity, philosophy of time, possible worlds, universals "
                "vs particulars, mereology basics."
            ),
            "ethics": (
                "Metaethics (moral realism, relativism, expressivism), utilitarianism, "
                "deontology (Kant), virtue ethics (Aristotle), applied ethics "
                "(bioethics, environmental ethics), moral psychology, agency."
            ),
            "political-philosophy": (
                "Justice (Rawls), rights and liberty, social contract (Hobbes, Locke, "
                "Rousseau), democracy, distributive justice, political obligation, "
                "civil disobedience."
            ),
            "philosophy-of-mind": (
                "Mind-body problem, dualism, physicalism, functionalism, "
                "intentionality, consciousness (hard problem, qualia), "
                "mental causation, AI and minds, Chinese Room argument."
            ),
        },
    },
    {
        "domain": "social-sciences",
        "domain_title": "Social Sciences",
        "domain_description": (
            "The study of human societies, social relationships, and institutions."
        ),
        "target_topics_per_course": 20,
        "prereq_domains": ["mathematics"],
        "courses": [
            {"id": "sociology", "title": "Sociology", "stage": "abstract-reasoning"},
            {"id": "anthropology", "title": "Anthropology", "stage": "abstract-reasoning"},
            {"id": "political-science", "title": "Political Science", "stage": "abstract-reasoning"},
            {"id": "human-geography", "title": "Human Geography", "stage": "abstract-reasoning"},
        ],
        "course_guidance": {
            "sociology": (
                "Sociological imagination, social stratification, race and ethnicity, "
                "gender and sexuality, institutions (family, education, religion), "
                "deviance and social control, social movements, urbanization, "
                "research methods in sociology."
            ),
            "anthropology": (
                "Cultural anthropology (culture concept, kinship, ritual, language), "
                "biological anthropology basics, archaeology basics, ethnography, "
                "cross-cultural comparison, globalization and culture change."
            ),
            "political-science": (
                "Political systems and regimes, democracy and authoritarianism, "
                "constitutions, branches of government, political parties and "
                "elections, international relations theories, political ideologies."
            ),
            "human-geography": (
                "Population geography, migration, cultural landscapes, urbanization, "
                "economic geography, political geography (borders, states), "
                "environmental geography, spatial analysis."
            ),
        },
    },

    # --- TIER 5: Arts & expression ---
    {
        "domain": "language-and-communication",
        "domain_title": "Language & Communication",
        "domain_description": (
            "The study of human language — its structure, use, and power."
        ),
        "target_topics_per_course": 20,
        "prereq_domains": [],
        "courses": [
            {"id": "grammar-and-syntax", "title": "Grammar & Syntax", "stage": "concrete-operations"},
            {"id": "rhetoric-and-composition", "title": "Rhetoric & Composition", "stage": "abstract-reasoning"},
            {"id": "linguistics", "title": "Linguistics", "stage": "formal-systems"},
            {"id": "public-speaking", "title": "Public Speaking", "stage": "abstract-reasoning"},
        ],
        "course_guidance": {
            "grammar-and-syntax": (
                "Parts of speech, sentence structure, clauses and phrases, "
                "subject-verb agreement, pronoun reference, punctuation rules, "
                "common grammatical errors, sentence combining, paragraph structure."
            ),
            "rhetoric-and-composition": (
                "Thesis development, evidence and reasoning, rhetorical appeals "
                "(ethos, pathos, logos), argument structure, research writing, "
                "revision strategies, writing modes (narrative, expository, "
                "persuasive, descriptive)."
            ),
            "linguistics": (
                "Phonetics and phonology, morphology, syntax (phrase structure), "
                "semantics, pragmatics, sociolinguistics, language acquisition, "
                "historical linguistics, writing systems."
            ),
            "public-speaking": (
                "Speech organization, delivery techniques, audience analysis, "
                "visual aids, persuasive speaking, informative speaking, debate, "
                "managing speech anxiety."
            ),
        },
    },
    {
        "domain": "literature",
        "domain_title": "Literature",
        "domain_description": (
            "The study of written works as art forms that illuminate the human condition."
        ),
        "target_topics_per_course": 20,
        "prereq_domains": ["language-and-communication"],
        "courses": [
            {"id": "literary-analysis", "title": "Literary Analysis", "stage": "abstract-reasoning"},
            {"id": "fiction", "title": "Fiction: Genres & Forms", "stage": "abstract-reasoning"},
            {"id": "poetry", "title": "Poetry", "stage": "abstract-reasoning"},
            {"id": "drama", "title": "Drama", "stage": "abstract-reasoning"},
            {"id": "critical-theory", "title": "Critical Theory", "stage": "formal-systems"},
        ],
        "course_guidance": {
            "literary-analysis": (
                "Plot structure, character analysis, setting, theme, point of view, "
                "symbolism, irony, figurative language, tone and mood, close "
                "reading techniques."
            ),
            "fiction": (
                "Short story vs novel, narrative structure, genre conventions "
                "(realism, fantasy, sci-fi, mystery, historical fiction), "
                "unreliable narrator, stream of consciousness, world-building."
            ),
            "poetry": (
                "Meter and rhythm, rhyme schemes, free verse, poetic forms "
                "(sonnet, haiku, ode, elegy, villanelle), imagery, sound devices "
                "(alliteration, assonance), enjambment."
            ),
            "drama": (
                "Dramatic structure, tragedy and comedy, theatrical conventions, "
                "dramatic irony, soliloquy and monologue, stagecraft, absurdism, "
                "Greek drama to modern."
            ),
            "critical-theory": (
                "Formalism, structuralism, post-structuralism, feminist criticism, "
                "postcolonial criticism, Marxist criticism, reader-response theory, "
                "New Historicism, psychoanalytic criticism."
            ),
        },
    },
    {
        "domain": "music",
        "domain_title": "Music",
        "domain_description": (
            "The study of organized sound — theory, history, performance, and "
            "creation. More sequential than most arts."
        ),
        "target_topics_per_course": 20,
        "prereq_domains": ["mathematics"],
        "courses": [
            {"id": "music-theory-fundamentals", "title": "Music Theory Fundamentals", "stage": "concrete-operations"},
            {"id": "harmony-and-voice-leading", "title": "Harmony & Voice Leading", "stage": "abstract-reasoning"},
            {"id": "music-history", "title": "Music History", "stage": "abstract-reasoning"},
            {"id": "ear-training", "title": "Ear Training & Aural Skills", "stage": "concrete-operations"},
            {"id": "composition", "title": "Composition", "stage": "formal-systems"},
        ],
        "course_guidance": {
            "music-theory-fundamentals": (
                "Pitch and notation, scales (major, minor, modes), intervals, "
                "rhythm and meter, key signatures, triads and 7th chords, "
                "basic chord progressions, song form."
            ),
            "harmony-and-voice-leading": (
                "Four-part writing rules, harmonic analysis (Roman numerals), "
                "secondary dominants, modulation, chromatic harmony, counterpoint "
                "basics, extended chords, jazz harmony introduction."
            ),
            "music-history": (
                "Medieval and Renaissance, Baroque, Classical, Romantic, "
                "20th Century art music, jazz history, popular music genres, "
                "world music traditions."
            ),
            "ear-training": (
                "Interval recognition, chord quality identification, rhythmic "
                "dictation, melodic dictation, sight-singing, harmonic dictation, "
                "solfège systems."
            ),
            "composition": (
                "Melody writing, harmonization, arranging, form and structure, "
                "text setting, orchestration basics, electronic music production, "
                "improvisation."
            ),
        },
    },
    {
        "domain": "arts-and-aesthetics",
        "domain_title": "Arts & Aesthetics",
        "domain_description": (
            "The visual arts, design principles, and aesthetic theory."
        ),
        "target_topics_per_course": 18,
        "prereq_domains": [],
        "courses": [
            {"id": "visual-elements-and-principles", "title": "Visual Elements & Principles", "stage": "concrete-operations"},
            {"id": "drawing-and-painting", "title": "Drawing & Painting", "stage": "concrete-operations"},
            {"id": "art-history", "title": "Art History", "stage": "abstract-reasoning"},
            {"id": "design-principles", "title": "Design Principles", "stage": "abstract-reasoning"},
        ],
        "course_guidance": {
            "visual-elements-and-principles": (
                "Line, shape, form, color theory (color wheel, mixing, temperature), "
                "value, texture, space; principles of balance, contrast, emphasis, "
                "movement, pattern, rhythm, unity."
            ),
            "drawing-and-painting": (
                "Observational drawing, perspective (1-point, 2-point, atmospheric), "
                "figure drawing basics, composition, media techniques (pencil, "
                "charcoal, watercolor, acrylic, oil), still life, portraiture."
            ),
            "art-history": (
                "Prehistoric art, ancient civilizations art, medieval art, "
                "Renaissance, Baroque, Neoclassicism, Romanticism, Impressionism, "
                "modern art movements, contemporary art, non-Western traditions."
            ),
            "design-principles": (
                "Typography, layout and grid systems, visual hierarchy, "
                "user interface basics, branding, color in design, accessibility, "
                "responsive design."
            ),
        },
    },
    {
        "domain": "practical-life-skills",
        "domain_title": "Practical Life Skills",
        "domain_description": (
            "Essential knowledge for functioning effectively in daily life."
        ),
        "target_topics_per_course": 16,
        "prereq_domains": ["mathematics"],
        "courses": [
            {"id": "financial-literacy", "title": "Financial Literacy", "stage": "abstract-reasoning"},
            {"id": "cooking-and-nutrition", "title": "Cooking & Nutrition", "stage": "concrete-operations"},
            {"id": "home-maintenance", "title": "Home Maintenance", "stage": "concrete-operations"},
            {"id": "digital-literacy", "title": "Digital Literacy", "stage": "concrete-operations"},
        ],
        "course_guidance": {
            "financial-literacy": (
                "Budgeting, saving, compound interest, credit and debt, taxes "
                "basics, insurance types, investing fundamentals (stocks, bonds, "
                "index funds), retirement accounts, mortgages, avoiding scams."
            ),
            "cooking-and-nutrition": (
                "Kitchen safety and hygiene, basic techniques (boiling, sautéing, "
                "baking, roasting), meal planning, reading recipes, knife skills, "
                "food storage, basic nutrition."
            ),
            "home-maintenance": (
                "Basic tools and their uses, electrical safety, plumbing basics, "
                "painting, cleaning, lawn and garden care, pest control, when to "
                "DIY vs hire professional, seasonal maintenance."
            ),
            "digital-literacy": (
                "File management, internet safety, email etiquette, effective "
                "searching, basic troubleshooting, privacy and security, social "
                "media literacy, productivity tools."
            ),
        },
    },
]


# =========================================================================
# ADVANCED MATH COURSES — graduate-level expansion (all stage: advanced)
# =========================================================================

ADVANCED_MATH_COURSES = [
    {
        "id": "math-differential-equations",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "differential-equations",
        "course_title": "Differential Equations",
        "stage": "advanced",
        "target_topics": 42,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "First-Order Linear ODEs, Integrating Factor Method, Exact Equations, "
            "Existence and Uniqueness Theorems for ODEs, Autonomous Equations and "
            "Phase Lines, Bifurcation in ODEs, Euler's Method for ODEs, Second-Order "
            "Linear Homogeneous ODEs, Characteristic Equation Method, Complex Roots "
            "and Oscillatory Solutions, Repeated Roots and Reduction of Order, "
            "Wronskian and Linear Independence, Undetermined Coefficients, Variation "
            "of Parameters, Higher-Order Linear ODEs, Spring-Mass Systems and "
            "Mechanical Vibrations, RLC Circuit Applications, Laplace Transform "
            "Definition and Properties, Common Laplace Transforms, Inverse Laplace "
            "Transform, Laplace Transform of Derivatives, Solving IVPs with Laplace "
            "Transforms, Step Functions and Laplace Transforms, Convolution Theorem, "
            "Dirac Delta Function, Systems of First-Order Linear ODEs, Matrix "
            "Exponential Method, Phase Portraits for Linear Systems, Stability "
            "Classification, Linearization of Nonlinear Systems, Power Series "
            "Solutions, Ordinary and Singular Points, Frobenius Method, Bessel "
            "Functions, Legendre Equations and Polynomials, Fourier Series Definition "
            "and Coefficients, Convergence of Fourier Series, Even/Odd Extensions, "
            "The Heat Equation, Separation of Variables for PDEs, The Wave Equation, "
            "Laplace's Equation and Boundary Value Problems. Prerequisites: "
            "calculus-2 (integration-by-parts, taylor-series, power-series), "
            "linear-algebra (eigenvalues-and-eigenvectors, matrix-operations), "
            "multivariable-calculus (partial-derivatives)."
        ),
    },
    {
        "id": "math-real-analysis",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "real-analysis",
        "course_title": "Real Analysis",
        "stage": "advanced",
        "target_topics": 40,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Ordered Field Axioms of the Real Numbers, The Completeness Axiom (Least "
            "Upper Bound Property), Supremum and Infimum, The Archimedean Property, "
            "Density of the Rationals, Sequences: Epsilon-N Convergence, Monotone "
            "Convergence Theorem, Subsequences and Bolzano-Weierstrass, Cauchy "
            "Sequences and Completeness, Limit Superior and Inferior, Open and Closed "
            "Sets on the Real Line, Compact Sets and Heine-Borel Theorem, Connected "
            "Sets, Epsilon-Delta Continuity, Sequential Characterization of "
            "Continuity, Extreme Value Theorem (Proof via Compactness), Intermediate "
            "Value Theorem (Rigorous), Uniform Continuity, Uniform Continuity on "
            "Compact Sets, Rigorous Definition of the Derivative, Mean Value Theorem "
            "(Rigorous), Taylor's Theorem with Remainder, L'Hopital's Rule (Rigorous), "
            "Rigorous Series Convergence, Absolute Convergence and Rearrangement, "
            "Riemann Integral via Darboux Sums, Criteria for Riemann Integrability, "
            "Properties of the Riemann Integral, Fundamental Theorem of Calculus "
            "(Rigorous), Improper Integrals (Rigorous), Pointwise Convergence of "
            "Function Sequences, Uniform Convergence, Uniform Convergence Preserves "
            "Continuity, Interchange of Limit and Integral, Interchange of Limit and "
            "Derivative, Uniform Convergence of Power Series, Weierstrass M-Test, "
            "Weierstrass Approximation Theorem, Introduction to Lebesgue Measure, "
            "Introduction to the Lebesgue Integral. Prerequisites: calculus-1 "
            "(continuity-definition, limit-laws, mean-value-theorem), calculus-2 "
            "(sequences-intro, series-convergence-tests), methods-of-proof "
            "(direct-proof, proof-by-contradiction, mathematical-induction)."
        ),
    },
    {
        "id": "math-abstract-algebra",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "abstract-algebra",
        "course_title": "Abstract Algebra",
        "stage": "advanced",
        "target_topics": 45,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Binary Operations and Algebraic Structures, Group Definition and "
            "Examples, Basic Properties of Groups, Subgroups and Subgroup Test, "
            "Cyclic Groups, Order of a Group Element, Permutation Groups, Cycle "
            "Notation and Decomposition, Sign of a Permutation, Dihedral Groups, "
            "Group Homomorphisms, Group Isomorphisms, Cosets and Lagrange's Theorem, "
            "Normal Subgroups, Quotient Groups, First Isomorphism Theorem for Groups, "
            "Second and Third Isomorphism Theorems, Direct Products, Classification "
            "of Finite Abelian Groups, Group Actions, Orbit-Stabilizer Theorem, The "
            "Class Equation, Sylow Theorems, Applications of Sylow Theorems, Ring "
            "Definition and Examples, Ring Homomorphisms, Subrings and Ideals, "
            "Quotient Rings, First Isomorphism Theorem for Rings, Integral Domains, "
            "Principal Ideal Domains, Unique Factorization Domains, Polynomial Rings, "
            "Irreducibility Criteria, Maximal and Prime Ideals, Field Definition and "
            "Examples, Field Extensions, Algebraic and Transcendental Elements, "
            "Splitting Fields, Finite Fields, Galois Groups, Fundamental Theorem of "
            "Galois Theory, Insolvability of the Quintic, Ruler and Compass "
            "Constructions (Algebraic Proof), Cayley's Theorem. Prerequisites: "
            "methods-of-proof (direct-proof, proof-by-contradiction, mathematical-"
            "induction, equivalence-relations), linear-algebra (vector-spaces, "
            "linear-transformations)."
        ),
    },
    {
        "id": "math-topology",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "topology",
        "course_title": "Topology",
        "stage": "advanced",
        "target_topics": 38,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Topological Spaces: Definition and Examples, Open and Closed Sets, "
            "Basis for a Topology, Subspace Topology, Product Topology, Quotient "
            "Topology, Closure/Interior/Boundary, Limit Points and Convergence, "
            "Hausdorff Spaces, Continuity in Topological Spaces, Homeomorphisms, "
            "Topological Invariants, Metric Spaces: Definition and Examples, Metric "
            "Topology, Completeness in Metric Spaces, Contraction Mapping Theorem, "
            "Open Covers and Compactness, Compactness in Hausdorff Spaces, Sequential "
            "Compactness, Compactness in Metric Spaces, Tychonoff's Theorem, "
            "Connectedness, Path Connectedness, Connected Components, Separation "
            "Axioms (T0 through T4), Urysohn's Lemma, Tietze Extension Theorem, "
            "First and Second Countability, Metrization Theorems, Homotopy of Paths, "
            "The Fundamental Group, Fundamental Group of the Circle, Simply Connected "
            "Spaces, Covering Spaces, Van Kampen's Theorem, Classification of Compact "
            "Surfaces, Baire Category Theorem, Introduction to Topological Manifolds. "
            "Prerequisites: methods-of-proof (set-theory-basics, proof-by-contradiction, "
            "equivalence-relations), real-analysis (open-and-closed-sets-real-line, "
            "compact-sets-heine-borel, cauchy-sequences-and-completeness)."
        ),
    },
    {
        "id": "math-complex-analysis",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "complex-analysis",
        "course_title": "Complex Analysis",
        "stage": "advanced",
        "target_topics": 35,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "The Complex Plane and Its Topology, Complex Functions and Mappings, "
            "Limits and Continuity of Complex Functions, Complex Differentiability "
            "(Holomorphic Functions), Cauchy-Riemann Equations, Elementary Complex "
            "Functions (exp, log, trig), Complex Logarithm and Branch Cuts, Complex "
            "Power Functions, Complex Line Integrals, Cauchy's Theorem "
            "(Cauchy-Goursat), Cauchy's Integral Formula, Cauchy's Integral Formula "
            "for Derivatives, Liouville's Theorem, Fundamental Theorem of Algebra "
            "(Complex-Analytic Proof), Maximum Modulus Principle, Taylor Series for "
            "Complex Functions, Laurent Series, Classification of Isolated "
            "Singularities, Residues: Definition and Computation, The Residue Theorem, "
            "Evaluating Real Integrals Using Residues, Trigonometric Integrals via "
            "Unit Circle, Improper Real Integrals via Contour Methods, The Argument "
            "Principle, Rouche's Theorem, Open Mapping Theorem, Schwarz Lemma, "
            "Conformal Mappings, Mobius Transformations, Riemann Mapping Theorem, "
            "Analytic Continuation, Monodromy Theorem, Harmonic Functions, "
            "Weierstrass Factorization Theorem, The Gamma Function. Prerequisites: "
            "calculus-2 (power-series, taylor-series), multivariable-calculus "
            "(partial-derivatives, line-integrals, greens-theorem), real-analysis "
            "(open-and-closed-sets-real-line, uniform-convergence)."
        ),
    },
    {
        "id": "math-number-theory",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "number-theory",
        "course_title": "Number Theory",
        "stage": "advanced",
        "target_topics": 38,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Divisibility Theory (Formal Treatment), Bezout's Identity, Linear "
            "Diophantine Equations, Fundamental Theorem of Arithmetic (Rigorous), "
            "Arithmetic Functions and Multiplicativity, Euler's Totient Function, "
            "Mobius Function and Inversion, Fermat's Little Theorem, Euler's Theorem, "
            "Wilson's Theorem, Primitive Roots and Cyclic Groups Mod p, Discrete "
            "Logarithms, Quadratic Residues and Legendre Symbol, Euler's Criterion, "
            "Law of Quadratic Reciprocity, The Jacobi Symbol, Sum of Two Squares "
            "Theorem, Lagrange's Four-Square Theorem, Pythagorean Triples "
            "(Parametrization), Fermat's Last Theorem (Overview), Pell's Equation, "
            "Continued Fractions, Best Rational Approximations, Distribution of "
            "Primes and Prime Number Theorem, Prime Counting Function and Chebyshev "
            "Bounds, Introduction to the Riemann Zeta Function, Dirichlet Series and "
            "L-Functions, Primes in Arithmetic Progressions (Dirichlet's Theorem), "
            "Algebraic Integers, Gaussian Integers, The Norm in Algebraic Number "
            "Fields, Failure of Unique Factorization, Introduction to Ideal Class "
            "Group, p-adic Valuation, Introduction to p-adic Numbers, Arithmetic "
            "in p-adic Numbers, Hensel's Lemma, Cryptographic Applications (RSA). "
            "Prerequisites: discrete-math (modular-arithmetic, euclidean-algorithm, "
            "fundamental-theorem-of-arithmetic), abstract-algebra (group-definition-"
            "and-examples, ring-definition-and-examples)."
        ),
    },
    {
        "id": "math-probability-and-mathematical-statistics",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "probability-and-mathematical-statistics",
        "course_title": "Probability & Mathematical Statistics",
        "stage": "advanced",
        "target_topics": 40,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Sigma-Algebras and Measurable Sets, Probability Spaces "
            "(Measure-Theoretic Definition), Random Variables as Measurable "
            "Functions, Distribution and Density Functions, Expectation "
            "(Measure-Theoretic), Moment Generating Functions, Characteristic "
            "Functions, Joint Distributions and Marginals (Rigorous), Conditional "
            "Expectation, Independence of Sigma-Algebras, Borel-Cantelli Lemmas, "
            "Convergence in Probability, Almost Sure Convergence, Convergence in "
            "Distribution, Convergence in L^p, Relationships Between Modes of "
            "Convergence, Weak Law of Large Numbers, Strong Law of Large Numbers, "
            "Central Limit Theorem (Rigorous via Characteristic Functions), "
            "Multivariate Normal Distribution, Exponential Family, Sufficient "
            "Statistics, Fisher Information, Cramer-Rao Lower Bound, Maximum "
            "Likelihood Estimation (Theory), Method of Moments, Consistency of "
            "Estimators, Asymptotic Normality of MLE, UMVUE, Rao-Blackwell Theorem, "
            "Neyman-Pearson Lemma, Likelihood Ratio Tests, Uniformly Most Powerful "
            "Tests, Confidence Intervals (Rigorous Theory), Bayesian Inference "
            "Foundations, Conjugate Priors, Bayesian Point Estimation, Markov Chains, "
            "Stationary Distributions, Introduction to Martingales. Prerequisites: "
            "probability-and-statistics (probability-axioms, bayes-theorem, "
            "expected-value, variance), real-analysis (riemann-integral-via-darboux-"
            "sums), measure-theory (sigma-algebras, lebesgue-measure)."
        ),
    },
    {
        "id": "math-numerical-analysis",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "numerical-analysis",
        "course_title": "Numerical Analysis",
        "stage": "advanced",
        "target_topics": 36,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Floating Point Representation, Machine Epsilon and Rounding Errors, "
            "Catastrophic Cancellation, Numerical Stability and Conditioning, "
            "Condition Number of a Problem, Bisection Method, Fixed Point Iteration, "
            "Newton's Method (Convergence Analysis), Secant Method, Order of "
            "Convergence, Lagrange Polynomial Interpolation, Newton's Divided "
            "Differences, Interpolation Error Analysis, Runge's Phenomenon, Chebyshev "
            "Nodes and Optimal Interpolation, Cubic Spline Interpolation, Numerical "
            "Differentiation, Richardson's Extrapolation, Newton-Cotes Quadrature, "
            "Composite Quadrature Rules, Gaussian Quadrature, Romberg Integration, "
            "Gaussian Elimination with Pivoting, LU Decomposition, Condition Number "
            "of a Matrix, Jacobi Iterative Method, Gauss-Seidel Method, SOR, "
            "Convergence of Iterative Methods, Power Method for Eigenvalues, QR "
            "Algorithm, Numerical Least Squares, Euler's Method (Error Analysis), "
            "Runge-Kutta Methods, Multistep Methods (Adams-Bashforth/Moulton), Stiff "
            "Equations and Stability Regions. Prerequisites: calculus-1 "
            "(mean-value-theorem), calculus-2 (taylor-series), linear-algebra "
            "(matrix-operations, eigenvalues-and-eigenvectors)."
        ),
    },
    {
        "id": "math-graph-theory-and-combinatorics",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "graph-theory-and-combinatorics",
        "course_title": "Graph Theory & Combinatorics",
        "stage": "advanced",
        "target_topics": 37,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Graph Theory: Formal Definitions, Degree Sequences and Erdos-Gallai "
            "Theorem, Graph Operations and Products, Matchings in Bipartite Graphs, "
            "Hall's Marriage Theorem, Konig's Theorem, Network Flows and Max-Flow "
            "Min-Cut, Menger's Theorem, Chromatic Number Bounds, Brooks' Theorem, "
            "The Chromatic Polynomial, Edge Coloring and Vizing's Theorem, List "
            "Coloring, Planar Graphs: Kuratowski's and Wagner's Theorems, The Four "
            "Color Theorem, Graph Minors and Robertson-Seymour, Ramsey Theory "
            "Foundations, Ramsey Numbers and Bounds, Infinite Ramsey Theory, Turan's "
            "Theorem, Extremal Graph Theory, The Probabilistic Method, Lovasz Local "
            "Lemma, Algebraic Graph Theory: Adjacency Matrix, Graph Laplacian and "
            "Spectrum, Matrix Tree Theorem, Generating Functions: Advanced Techniques, "
            "Exponential Generating Functions, Catalan Numbers, Stirling Numbers, "
            "Integer Partitions, Polya Enumeration Theorem, Inclusion-Exclusion "
            "Advanced Applications, Latin Squares, Block Designs and Steiner Systems, "
            "Introduction to Matroids, Hamiltonian Cycle Conditions (Dirac/Ore). "
            "Prerequisites: discrete-math (graph-theory-intro, graph-coloring, "
            "permutations-and-combinations), probability-and-statistics "
            "(expected-value), linear-algebra (eigenvalues-and-eigenvectors)."
        ),
    },
    {
        "id": "math-measure-theory-and-functional-analysis",
        "type": "math-course",
        "domain": "mathematics",
        "course_id": "measure-theory-and-functional-analysis",
        "course_title": "Measure Theory & Functional Analysis",
        "stage": "advanced",
        "target_topics": 40,
        "prereq_domains": ["mathematics"],
        "guidance": (
            "Sigma-Algebras (Formal Construction), Measures and Measure Spaces, "
            "Outer Measure and Caratheodory's Theorem, Lebesgue Measure on R^n, "
            "Measurable Functions, Simple Functions and Approximation, Lebesgue "
            "Integral (Full Construction), Monotone Convergence Theorem, Fatou's "
            "Lemma, Dominated Convergence Theorem, Comparison of Riemann and "
            "Lebesgue Integrals, Product Measures and Fubini's Theorem, L^p Spaces, "
            "Holder's and Minkowski's Inequalities, Completeness of L^p (Riesz-"
            "Fischer), Normed Vector Spaces, Banach Spaces, Bounded Linear Operators, "
            "The Operator Norm, Dual Spaces and Bounded Linear Functionals, "
            "Hahn-Banach Theorem, Open Mapping Theorem, Closed Graph Theorem, "
            "Uniform Boundedness Principle, Hilbert Spaces, Orthogonality in Hilbert "
            "Spaces, Orthogonal Projections, Riesz Representation Theorem (Hilbert), "
            "Orthonormal Bases, Bessel's Inequality and Parseval's Identity, Fourier "
            "Series as L^2 Theory, Compact Operators, Spectral Theorem for Compact "
            "Self-Adjoint Operators, Fredholm Alternative, Weak and Weak* Convergence, "
            "Reflexive Spaces, Radon-Nikodym Theorem, Signed Measures and "
            "Hahn-Jordan Decomposition, Riesz Representation Theorem (Measures), "
            "Introduction to Sobolev Spaces. Prerequisites: real-analysis "
            "(open-and-closed-sets-real-line, compact-sets-heine-borel, "
            "uniform-convergence, riemann-integral-via-darboux-sums), linear-algebra "
            "(vector-spaces, inner-products, eigenvalues-and-eigenvectors), "
            "topology (topological-spaces, compactness, hausdorff-spaces)."
        ),
    },
]


def build_queue():
    """Expand all specs into a flat execution queue.

    Returns list of dicts, each with a "type" field:
      - "math-course": generate topics for a math course
      - "domain-setup": create _domain.yml (no agent needed)
      - "domain-course": generate topics for one course in a new domain
      - "cross-domain-review": review and add cross-domain links
    """
    queue = []

    # Phase 1: Math courses (original + advanced)
    queue.extend(MATH_COURSES)
    queue.extend(ADVANCED_MATH_COURSES)

    # Phase 1b: Expansion courses (advanced content across all domains)
    import sys
    from pathlib import Path as _Path
    overnight_dir = str(_Path(__file__).resolve().parent)
    if overnight_dir not in sys.path:
        sys.path.insert(0, overnight_dir)
    try:
        from expansion_courses import EXPANSION_COURSES
        queue.extend(EXPANSION_COURSES)
    except ImportError:
        pass

    # Phase 2: New domain courses
    for spec in DOMAIN_SPECS:
        # Setup entry (creates _domain.yml, no agent call)
        queue.append({
            "id": f"{spec['domain']}--setup",
            "type": "domain-setup",
            "domain": spec["domain"],
            "domain_title": spec["domain_title"],
            "domain_description": spec["domain_description"],
            "courses": spec["courses"],
        })

        # Per-course entries
        for course in spec["courses"]:
            course_guidance = spec.get("course_guidance", {}).get(course["id"], "")
            queue.append({
                "id": f"{spec['domain']}--{course['id']}",
                "type": "domain-course",
                "domain": spec["domain"],
                "domain_title": spec["domain_title"],
                "course_id": course["id"],
                "course_title": course["title"],
                "stage": course["stage"],
                "target_topics": spec["target_topics_per_course"],
                "prereq_domains": spec["prereq_domains"],
                "guidance": course_guidance,
            })

    # Phase 3: Cross-domain connection review (one per domain with prereqs)
    for spec in DOMAIN_SPECS:
        if spec["prereq_domains"]:
            queue.append({
                "id": f"{spec['domain']}--crosslinks",
                "type": "cross-domain-review",
                "domain": spec["domain"],
                "domain_title": spec["domain_title"],
                "prereq_domains": spec["prereq_domains"],
            })

    return queue
