# New topics report: computer-science

Status: DONE. 25 new topic files written; 11 proposed edges into existing topics. No existing files edited.

## 1. Syllabi compared against, per course

| Course | Syllabus / textbook compared against |
|---|---|
| programming-fundamentals | AP Computer Science A (College Board CED, Units 1-10); AP Computer Science Principles (Big Ideas 1-5); ACM/IEEE CS2023 SDF, FPL (OOP, event-driven), SE, SEP |
| data-structures-and-algorithms | AP CSA Unit 7 (searching, sorting); CLRS (Cormen et al., 4th ed.) Parts I-VI; CS2023 AL |
| computer-architecture | Patterson & Hennessy, *Computer Organization and Design* (RISC-V ed.), Ch. 1-6; CS2023 AR |
| operating-systems | Arpaci-Dusseau, *OSTEP* (virtualization, concurrency, persistence); Silberschatz et al., *Operating System Concepts* 10th ed.; CS2023 OS |
| databases | Silberschatz, Korth & Sudarshan, *Database System Concepts* 7th ed.; Ramakrishnan & Gehrke, *Database Management Systems* 3rd ed.; CS2023 DM |
| computer-networking | Kurose & Ross, *Computer Networking: A Top-Down Approach* 8th ed.; CS2023 NC |
| theory-of-computation | Sipser, *Introduction to the Theory of Computation* 3rd ed. (also checked against formal-sciences-and-logic/computability-and-complexity) |
| artificial-intelligence | Russell & Norvig, *Artificial Intelligence: A Modern Approach* 4th ed.; CS2023 AI |
| compilers | Aho, Lam, Sethi & Ullman, *Compilers* 2nd ed.; Bryant & O'Hallaron, *CS:APP* 3rd ed. Ch. 7 (Linking); CS2023 FPL |
| distributed-systems | van Steen & Tanenbaum, *Distributed Systems*; Kleppmann, *Designing Data-Intensive Applications*; CS2023 PDC |
| machine-learning-theory | Shalev-Shwartz & Ben-David, *Understanding Machine Learning* |
| cryptography | Katz & Lindell, *Introduction to Modern Cryptography* 3rd ed.; Boneh & Shoup, *A Graduate Course in Applied Cryptography* |
| quantum-computing | Nielsen & Chuang, *Quantum Computation and Quantum Information* |
| information-theory | Cover & Thomas, *Elements of Information Theory* 2nd ed. |
| advanced-algorithms | CLRS Part VII (incl. Ch. 33 computational geometry); Kleinberg & Tardos; Motwani & Raghavan; Williamson & Shmoys |
| formal-methods | Huth & Ryan, *Logic in Computer Science*; Baier & Katoen, *Principles of Model Checking* |

Coverage note: the domain is dense (about 1,200 topics). Theory of computation, quantum computing, machine-learning theory, information theory and formal methods had no gap clear enough to fill within the 25-topic budget; their candidate gaps are listed under "deferred" below.

## 2. New topics

| new id | course | why it is a gap (syllabus unit) | prerequisites |
|---|---|---|---|
| inheritance-and-subclasses | programming-fundamentals | AP CSA Unit 9 (Inheritance); CS2023 FPL OOP. No CS topic covers superclass/subclass. | intro-to-classes (hard), methods-and-attributes (hard), objects-and-instances (soft) |
| method-overriding-and-dynamic-dispatch | programming-fundamentals | AP CSA Unit 9 (overriding, polymorphism); CS2023 FPL OOP. Only compiler-level type-system polymorphism topics exist. | inheritance-and-subclasses (hard), functions-defining-calling (soft) |
| abstract-classes-and-interfaces | programming-fundamentals | CS2023 FPL OOP; standard CS1/CS2 Java textbooks (abstract classes and interfaces chapter) | inheritance-and-subclasses (hard), method-overriding-and-dynamic-dispatch (hard), function-design-and-contracts (soft) |
| two-dimensional-arrays | programming-fundamentals | AP CSA Unit 8 (2D Array) | arrays-and-lists (hard), array-indexing (hard), nested-loops (hard), parameter-passing-value-vs-reference (soft) |
| random-numbers-and-simulation | programming-fundamentals | AP CSP topics 3.15 (Random Values) and 3.16 (Simulations) | for-loops (hard), numeric-types (hard), conditional-statements (hard), simple-probability (soft) |
| event-driven-programming | programming-fundamentals | CS2023 FPL event-driven and reactive programming; AP CSP Big Idea 1 (events as program input). Only OS-level async I/O event loops existed. | functions-defining-calling (hard), parameters-and-arguments (hard), while-loops (soft), program-structure (soft) |
| version-control-with-git | programming-fundamentals | CS2023 SE (tools, version control). No topic anywhere on version control. | program-structure (soft), file-io-basics (soft), testing-and-validation-basics (soft) |
| software-licensing-and-intellectual-property | programming-fundamentals | AP CSP topic 5.5 (Legal and Ethical Concerns: IP, Creative Commons, open source); CS2023 SEP. No title anywhere in domains/ on software copyright or licensing. | hello-world (soft), technology-ethics (soft) |
| linear-search | data-structures-and-algorithms | AP CSA topic 7.5 (Searching); mentioned only in passing in binary-search-algorithm | arrays-and-lists (hard), for-loops (hard), comparison-operators (hard), big-o-complexity-analysis (soft) |
| virtual-machines-and-hypervisors | operating-systems | Silberschatz Ch. 18 (Virtual Machines); OSTEP virtual machine monitors appendix; CS2023 OS | system-calls (hard), process-concept (hard), virtual-memory-management (soft), exception-handling-architecture (soft) |
| file-system-journaling-crash-consistency | operating-systems | OSTEP Ch. 42 (Crash Consistency: FSCK and Journaling) | file-system-implementation (hard), file-system-concepts (hard), write-ahead-logging (soft) |
| raid-disk-arrays | operating-systems | OSTEP Ch. 38 (RAID); Silberschatz RAID structure section; P&H Ch. 5 | io-management (hard), logical-operators (soft), disk-scheduling (soft), error-detection-and-correction (soft) |
| multicore-processors-and-hardware-multithreading | computer-architecture | P&H Ch. 6 (multicore, Flynn's taxonomy, hardware multithreading) | pipelining-fundamentals (hard), cache-memory-design (hard), performance-and-benchmarking (soft), cache-coherence-protocols (soft) |
| gpu-architecture-and-simt | computer-architecture | P&H Ch. 6 (Introduction to GPUs); Hennessy & Patterson *Computer Architecture* Ch. 4 (data-level parallelism) | multicore-processors-and-hardware-multithreading (hard), memory-hierarchy-overview (hard), vectorization-and-simd (soft) |
| join-algorithms | databases | Silberschatz Ch. 15 (Query Processing, join operation); Ramakrishnan Ch. 14. Join methods only mentioned inside optimizer topics. | sql-joins (hard), relational-algebra (hard), physical-storage-pages-records (hard), hash-indexes (soft), merge-sort (soft) |
| relational-calculus | databases | Ramakrishnan Ch. 4 (Relational Algebra and Calculus); Silberschatz formal relational query languages. Zero mentions in domains/. | relational-algebra (hard), relational-data-model (hard), predicates-quantifiers-discrete (hard) |
| multiple-access-protocols | computer-networking | Kurose & Ross 6.3 (Multiple Access Links and Protocols); no ALOHA anywhere | network-fundamentals (hard), error-detection-and-correction (soft), simple-probability (soft) |
| linking-and-loading | compilers | CS:APP Ch. 7 (Linking); P&H 2.12 (Translating and Starting a Program). Zero linker/relocation topics. | assembly-language-basics (hard), symbol-tables-and-scope (soft), memory-management-basics (soft), process-creation-fork-exec (soft) |
| intelligent-agents-and-environments | artificial-intelligence | Russell & Norvig Ch. 2 (Intelligent Agents: rationality, PEAS, environment types, agent architectures) | algorithm-design-basics (soft), conditional-statements (soft), simple-probability (soft) |
| uninformed-search-strategies | artificial-intelligence | Russell & Norvig Ch. 3 (problem formulation; uniform-cost, depth-limited, iterative deepening). BFS/DFS exist only as graph algorithms. | breadth-first-search (hard), depth-first-search (hard), heaps-and-priority-queues (soft), intelligent-agents-and-environments (soft), asymptotic-notation-big-o-omega-theta (soft) |
| classical-planning-strips | artificial-intelligence | Russell & Norvig Ch. 11 (Automated Planning: STRIPS/PDDL, forward/backward search, relaxed heuristics) | uninformed-search-strategies (hard), first-order-logic-ai (soft), heuristic-search-functions (soft) |
| remote-procedure-calls | distributed-systems | van Steen & Tanenbaum Ch. 4 (Communication: RPC); CS2023 PDC. RPC appears only as a word in observability topics. | socket-programming-basics (hard), functions-defining-calling (hard), parameter-passing-value-vs-reference (soft) |
| mapreduce-programming-model | distributed-systems | Kleppmann Ch. 10 (Batch Processing); Dean & Ghemawat 2004. Zero mentions in domains/. | distributed-systems-introduction (hard), hash-tables (hard), functional-programming-paradigm (soft), data-sharding-partitioning (soft), failure-detection-heartbeats (soft) |
| cpa-cca-security-definitions | cryptography | Katz & Lindell Ch. 3 and 5 (indistinguishability, CPA security, CCA security); terms appear only in passing | perfect-secrecy-and-one-time-pad (hard), symmetric-encryption-block-ciphers (hard), pseudorandom-functions (soft) |
| convex-hull-algorithms | advanced-algorithms | CLRS Ch. 33.3 (Finding the convex hull). No computational-geometry topic anywhere. | stacks-data-structure (hard), asymptotic-notation-big-o-omega-theta (hard), merge-sort (soft), sorting-lower-bounds (soft), cross-product (soft) |

All prerequisite and builds-toward ids were checked with Glob. All 25 new ids were checked to be unused across domains/. Stages were set no lower than the stage of each topic's hard prerequisites.

## Proposed edges into existing topics

Each line means the existing topic (column 3) should list the new topic (column 2) as a prerequisite. Each one matches a `builds-toward` entry in the new file, and each was checked so that it does not close a cycle with the new topic's own prerequisites.

```
ADD	two-dimensional-arrays	graph-adjacency-list-matrix-representations	soft	an adjacency matrix is a 2D array; row/column indexing and nested traversal are assumed
ADD	linear-search	binary-search-algorithm	soft	binary search is motivated and analyzed by contrast with linear search
ADD	join-algorithms	query-optimization	soft	the optimizer chooses among nested-loop, sort-merge and hash joins by estimated cost
ADD	multiple-access-protocols	ethernet-protocol	soft	classic Ethernet uses CSMA/CD with binary exponential backoff
ADD	multiple-access-protocols	wireless-networking-802-11	soft	802.11 uses CSMA/CA, taught as a variant of CSMA
ADD	uninformed-search-strategies	heuristic-search-functions	soft	heuristics are introduced as an improvement on blind search over the same problem formulation
ADD	uninformed-search-strategies	astar-search-algorithm	soft	A* extends uniform-cost search by adding h(n) to g(n)
ADD	remote-procedure-calls	at-least-once-semantics	soft	at-least-once delivery is first met as an RPC call semantics under retries
ADD	remote-procedure-calls	idempotent-operations	soft	idempotence is motivated by safe retrying of remote calls
ADD	cpa-cca-security-definitions	modes-of-operation	soft	modes such as CBC and CTR are judged by whether they meet CPA security; CTR's malleability shows CCA failure
ADD	cpa-cca-security-definitions	authenticated-encryption	soft	authenticated encryption is the standard route to CCA security
```

Not proposed, to avoid a cycle: `multicore-processors-and-hardware-multithreading -> cache-coherence-protocols`, because the new multicore topic already lists cache-coherence-protocols as a soft prerequisite. If reviewers prefer the other direction (coherence draws on multicore), drop that soft prerequisite from the new file first.

## 4. Gaps considered and rejected

Already covered (rejected):
- Dictionaries / key-value maps at CS1 level: covered by hash-tables (DSA).
- Higher-order functions, lambdas, map/filter: covered by functional-programming-paradigm and list-comprehensions.
- Encapsulation, constructors, getters/setters: covered by intro-to-classes and methods-and-attributes.
- Unit testing, test-driven development: covered by testing-and-validation-basics.
- Binary, hexadecimal, base conversion (AP CSP 2.1): binary-number-system, hexadecimal-number-system, number-base-conversion-operations.
- Data compression, lossless/lossy, Lempel-Ziv (AP CSP 2.2): data-compression-basics, huffman-coding.
- IEEE 754 floating point: floating-point-representation.
- Safe computing: phishing, malware, passwords (AP CSP 5.6): practical-life-skills/digital-literacy (phishing-and-scams, common-malware-types-and-defense, password-security).
- Privacy, computing bias, digital ethics (AP CSP 5.1-5.3): digital-privacy-fundamentals, privacy-ethics-surveillance, algorithmic-fairness-ethics, ai-ethics-fairness-bias, technology-ethics.
- SQL injection, buffer overflow: database-security, os-security-basics.
- Amdahl's law: performance-and-benchmarking.
- Cache coherence (MESI): cache-coherence-protocols.
- Dining philosophers: deadlock-conditions, deadlock-conditions-and-graphs.
- Event loops for I/O: asynchronous-io-and-aio (the new event-driven-programming topic covers the programming paradigm, which that topic does not).
- Hamming codes: error-detection-and-correction.
- Go-Back-N, Selective Repeat, stop-and-wait: automatic-repeat-request, sliding-window-protocol.
- Data processing inequality: mutual-information. Kraft inequality: discussed in source-coding-theorem and huffman-coding.
- Recursion theorem: kleene-recursion-theorem (formal-sciences-and-logic). Circuit complexity: circuit-complexity, circuit-complexity-and-bounds (formal-sciences-and-logic).
- Kolmogorov complexity: kolmogorov-complexity-algorithmic. Interactive proofs: interactive-proof-systems.
- Propositional and first-order resolution: resolution-propositional, resolution-fol (formal-sciences-and-logic).
- Value and policy iteration: markov-decision-processes. Hill climbing: local-search-optimization.
- Two-phase commit: two-phase-commit-protocol. Bisimulation: process-calculi.
- Density matrices, mixed states: physics/quantum-mechanics density-matrices, pure-and-mixed-states.
- Bipartite matching: mathematics matchings-bipartite-graphs. Euclid's algorithm: mathematics euclidean-algorithm. Miller-Rabin: rp-corp-classes, las-vegas-vs-monte-carlo.
- Three-address code: intermediate-code-representation.
- Peer-to-peer lookup: partly covered by distributed-hash-tables.

Real gaps found but deferred (not written, to keep within the 10-25 budget; recommended for a later pass):
- containers-and-os-level-virtualization (operating-systems; Silberschatz Ch. 18): only mentioned inside the new VM topic and in network-function-virtualization-nfv.
- software-design-patterns (programming-fundamentals or a future software-engineering course; CS2023 SE): zero topics.
- distributed-mutual-exclusion (distributed-systems; van Steen & Tanenbaum, Ricart-Agrawala): zero mentions.
- method-of-types-and-sanov-theorem (information-theory; Cover & Thomas Ch. 11): zero mentions.
- algorithmic-stability-and-generalization (machine-learning-theory; Shalev-Shwartz & Ben-David Ch. 13): no dedicated topic.
- mistake-bound-model-and-littlestone-dimension (machine-learning-theory; Shalev-Shwartz & Ben-David Ch. 21): no dedicated topic.
- petri-nets (formal-methods): zero mentions in domains/.
- formal specification languages such as TLA+ or Alloy (formal-methods; CS2023 SE formal methods): zero mentions.

Out of scope (no matching course in `_domain.yml`; creating a course would require editing `_domain.yml`): CS2023 Graphics and Interactive Techniques (rasterization, rendering pipeline) and Human-Computer Interaction (usability evaluation). Design-side usability and accessibility exist under arts-and-aesthetics/design-principles.

Process note: one Edit-tool call was used on a newly created file (method-overriding-and-dynamic-dispatch.md, to remove an extra `aliases` key). It touched no pre-existing file. All other writes used Write.
