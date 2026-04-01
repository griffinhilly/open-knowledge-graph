---
id: sat-solving-cdcl
title: SAT Solving and Conflict-Driven Clause Learning
domain: computer-science
course: formal-methods
prerequisites:
- id: boolean-satisfiability-and-reductions
  type: hard
- id: propositional-logic-introduction
  type: hard
builds-toward: []
tags:
- sat
- cdcl
- dpll
- unit-propagation
- backjumping
- watched-literals
- clause-learning
stage: expert
status: validated
---

# SAT Solving and Conflict-Driven Clause Learning

## Core Idea
Modern SAT solvers determine whether a propositional formula in conjunctive normal form (CNF) has a satisfying assignment. The DPLL algorithm (Davis-Putnam-Logemann-Loveland) searches by choosing variable assignments, propagating forced implications (unit propagation), and backtracking on contradictions. Conflict-Driven Clause Learning (CDCL) dramatically improves on DPLL by analyzing each conflict to learn a new clause that prevents the same mistake, then backjumping non-chronologically past irrelevant decisions. With additional techniques like watched literals for efficient propagation, restart strategies, and variable-state-independent decaying sum (VSIDS) heuristics, CDCL solvers routinely handle industrial instances with millions of variables -- despite SAT being NP-complete.

## Questions

```yaml
- question: "What distinguishes CDCL backjumping from the chronological backtracking used in basic DPLL?"
  type: multiple-choice
  options:
    - "CDCL always backtracks to decision level 0 and starts over"
    - "CDCL analyzes the conflict to identify the most recent decision actually responsible, then backtracks directly to that level, skipping irrelevant intermediate decisions"
    - "CDCL backtracks one level at a time but faster because it uses parallel computation"
    - "CDCL never backtracks -- it restarts from scratch whenever a conflict occurs"
  answer: 1
  explanation: "When CDCL detects a conflict, it performs conflict analysis by tracing the implication graph backward to find the set of decisions that caused the conflict. It derives a learned clause from this analysis. The backjump level is determined by the second-highest decision level in the learned clause -- the solver jumps directly there, undoing all intermediate decisions that played no role in the conflict. This non-chronological backjumping can skip many decision levels at once, dramatically pruning the search space compared to chronological backtracking which can only undo one level at a time."

- question: "Unit propagation determines the value of a variable when a clause has exactly one unassigned literal and all other literals are false."
  type: true-false
  answer: true
  explanation: "A unit clause (or a clause that has become unit under the current partial assignment) has exactly one unassigned literal with all others evaluating to false. The remaining literal must be set to true to satisfy that clause -- this is a forced assignment, not a decision. Unit propagation applies this rule repeatedly: each forced assignment may make additional clauses unit, triggering a cascade of implications. This cascade is recorded in the implication graph, which CDCL later uses for conflict analysis. Efficient unit propagation (via watched literals) is the single most performance-critical component of a CDCL solver."

- question: "Explain how the watched-literals data structure achieves efficient unit propagation without scanning all clauses after every assignment."
  type: short-answer
  answer: "Each clause watches exactly two of its unassigned literals. When a variable is assigned, only clauses watching that literal need examination -- not all clauses containing it. A watched literal is replaced only when it becomes false: the solver scans the clause for another non-false literal to watch. A clause requires attention (becomes unit or conflicting) only when both watched literals are false and no replacement can be found. This means most assignments trigger no clause scanning for most clauses, giving amortized near-constant-time propagation."
  explanation: "Watched literals, introduced in the Chaff solver (Moskewicz et al., 2001), were a breakthrough in SAT solver engineering. Unlike earlier schemes that maintained full occurrence lists or head/tail pointers requiring updates on backtracking, watched literals require no bookkeeping during backtracking at all -- the watches remain valid because they only track 'at least two non-false literals exist.' This lazy approach dramatically reduces the overhead of the propagation-backtrack cycle that dominates solver runtime."

- question: "Why do modern CDCL solvers periodically restart the search despite losing the current partial assignment?"
  type: short-answer
  answer: "Restarts allow the solver to escape from unproductive parts of the search tree where early variable decisions have channeled it into a region containing no solutions. Crucially, learned clauses survive restarts, so the knowledge gained from conflicts is preserved. The combination of restarts with VSIDS heuristics means the solver effectively re-prioritizes its variable ordering based on recently active conflicts, focusing on the variables that matter most. Luby and geometric restart strategies have been shown empirically to improve performance on structured industrial instances by orders of magnitude."
  explanation: "The theoretical justification comes from heavy-tailed runtime distributions observed in combinatorial search: some runs get lucky with early decisions and solve quickly, while others get stuck exponentially long. Restarts with increasing frequency exploit this by repeatedly sampling fresh starting points while retaining learned knowledge. The Luby sequence (1, 1, 2, 1, 1, 2, 4, 1, ...) provides an optimal universal restart strategy for Las Vegas algorithms."
```

## Explainer

The Boolean satisfiability problem (SAT) asks whether there exists an assignment of truth values to variables that makes a propositional formula true. The formula is typically given in **conjunctive normal form** (CNF): a conjunction of clauses, where each clause is a disjunction of literals (variables or their negations). Despite being the canonical NP-complete problem, SAT has become practically solvable for enormous structured instances thanks to the CDCL algorithm, which powers every competitive modern SAT solver (MiniSat, CaDiCaL, Kissat, Glucose).

The foundation is the **DPLL algorithm** (1962), which searches for a satisfying assignment through three operations: **decide** (choose an unassigned variable and tentatively assign it true or false), **propagate** (apply unit propagation -- if a clause has exactly one unassigned literal and all others are false, that literal must be true), and **backtrack** (when a conflict is reached -- some clause has all literals false -- undo the most recent decision and try the opposite). DPLL organizes the search as a binary decision tree, with unit propagation pruning branches where implications are forced. On its own, DPLL with chronological backtracking is complete but can explore exponentially large subtrees that could have been avoided.

**Conflict-Driven Clause Learning** (CDCL), developed through the GRASP (1996), Chaff (2001), and subsequent solvers, transforms DPLL with three key innovations. First, **conflict analysis**: when propagation leads to a conflict, the solver traces backward through the **implication graph** (a DAG recording which decisions and propagations led to each assignment) to identify the true cause of the conflict. It derives a **learned clause** -- a new clause that is logically implied by the original formula but which the solver did not originally have. This clause prevents the same combination of decisions from recurring. Second, **non-chronological backjumping**: instead of undoing just the most recent decision, the solver jumps back to the decision level identified by conflict analysis as the source of the problem, potentially skipping many irrelevant decision levels at once. Third, **efficient data structures**: the **watched-literals** scheme ensures that unit propagation examines only the clauses directly affected by each assignment, achieving near-constant amortized cost per propagation step.

Modern CDCL solvers add several additional techniques that contribute to their remarkable empirical performance. The **VSIDS** (Variable State Independent Decaying Sum) decision heuristic prioritizes variables that appeared in recent conflicts, focusing the search on the "active" part of the formula. **Restarts** periodically abandon the current search tree and begin again from scratch, but crucially, all learned clauses are retained -- the solver restarts with strictly more knowledge than it began with. **Clause database management** periodically deletes low-activity learned clauses to control memory usage while retaining the most useful conflict information. **Phase saving** remembers the last assigned polarity of each variable and reuses it after restarts, preserving locality in the search. Together, these techniques enable CDCL solvers to exploit the structure present in real-world industrial formulas, which is why they succeed on instances with millions of variables even though random SAT instances of a few hundred variables can be impractical.

SAT solving is the engine underneath much of formal methods. Bounded model checking encodes verification problems as SAT formulas. Symbolic execution uses SAT/SMT to determine path feasibility. Invariant generation techniques use SAT oracles for counterexample-guided refinement. Understanding how the solver works -- not just that it returns SAT or UNSAT -- is essential for formulating verification problems in solver-friendly ways and for diagnosing why a verification tool succeeds or fails on a given instance.
