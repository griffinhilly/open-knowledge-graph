---
id: cook-levin-theorem-formal
title: The Cook-Levin Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: polynomial-time-reductions
  type: hard
- id: nondeterministic-turing-machines
  type: hard
- id: boolean-algebra
  type: soft
- id: big-o-notation
  type: soft
- id: algorithm-analysis-big-o
  type: soft
tags:
- NP-complete
- SAT
- satisfiability
- Cook-Levin
stage: formal-systems
status: validated
---

# The Cook-Levin Theorem

## Core Idea
The Cook-Levin theorem proves that Boolean satisfiability (SAT) is NP-complete — the first problem proven NP-complete (Cook 1971, independently Levin 1973). The proof encodes the computation of an arbitrary NTM as a propositional formula: variables represent tape cells, head positions, and states at each time step, while clauses enforce the transition rules. Since every NP problem reduces to SAT, SAT is the 'universal' hard problem in NP and the historical starting point for the entire theory of NP-completeness.

## How It's Best Learned
Work through the tableau construction carefully: understand how an NTM's accepting computation of length t is encoded as a formula of size O(t²). Appreciate that the reduction itself runs in polynomial time even though the formula can be large relative to the original instance.

## Common Misconceptions
- The theorem proves SAT is NP-complete, not that SAT is unsolvable — SAT is in NP, so it can be solved, just not known to be solvable in polynomial time.
- The historical significance is not merely proving SAT hard, but establishing the concept of NP-completeness itself and identifying the first complete problem from which all others reduce.

## Questions

```yaml
- question: "A student reads about the Cook-Levin theorem and concludes: 'This proves SAT cannot be solved in polynomial time — we know it requires exponential time.' What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "SAT actually has a polynomial-time algorithm discovered after Cook's paper"
    - "Cook-Levin proves SAT is NP-complete, but NP-completeness does not prove any problem requires superpolynomial time — whether P=NP remains open"
    - "Cook proved SAT is NP-hard but not that it is in NP, so NP-completeness does not follow from his result"
    - "The theorem only applies to 3-CNF satisfiability, not general SAT, so the conclusion overstates the result"
  answer: 1
  explanation: "This is the central misconception flagged in the topic's Common Misconceptions. NP-completeness means SAT is in NP and every NP problem reduces to SAT in polynomial time. It does NOT prove SAT is hard in an absolute sense. If P=NP (still unresolved after 50+ years), then SAT would have a polynomial-time algorithm and Cook-Levin would still be true. The theorem identifies SAT as the right problem to study to resolve P vs. NP — it does not resolve the question itself."

- question: "What is the key technique by which the Cook-Levin proof shows that every NP problem reduces to SAT?"
  type: multiple-choice
  options:
    - "Encoding the problem's input as a binary string that a SAT solver tests by guessing all possible assignments"
    - "Constructing a tableau formula that encodes an accepting computation history of a polynomial-time NTM, where satisfying assignments correspond exactly to valid accepting computations"
    - "Using a diagonal argument to show SAT can simulate any NTM by parallel nondeterministic branching"
    - "Showing that SAT's search space has the same cardinality as any NP problem's solution space"
  answer: 1
  explanation: "The tableau construction is the heart of the proof. For any NP problem with a poly-time NTM M and input w, the proof constructs a propositional formula φ_{M,w} using three families of variables: cell variables (what symbol is on each tape cell at each time step), head variables (head position), and state variables (machine state). Clauses enforce the initial configuration, valid transitions, and acceptance. The formula has size O(t²) — polynomial. It is satisfiable if and only if M accepts w. This works for ANY NP problem's NTM, so every NP problem reduces to SAT."

- question: "If SAT were shown to have a polynomial-time algorithm, then every problem in NP could be solved in polynomial time."
  type: true-false
  answer: true
  explanation: "This is precisely what NP-completeness means. Every NP problem reduces to SAT in polynomial time (Cook-Levin gives the reduction for an arbitrary NTM; subsequent reductions from SAT to other NP-complete problems complete the chain). A polynomial-time SAT solver, combined with these polynomial-time reductions, would give polynomial-time algorithms for all of NP — resolving P=NP in the affirmative."

- question: "The Cook-Levin theorem proves that SAT cannot be solved in polynomial time."
  type: true-false
  answer: false
  explanation: "Cook-Levin proves SAT is NP-complete: SAT is in NP, and every NP problem reduces to SAT. It says nothing about whether polynomial-time algorithms for SAT (and hence all of NP) exist. Whether P=NP — whether NP problems genuinely require superpolynomial time — is the most famous open problem in computer science. Cook-Levin identifies SAT as the pivotal problem; it does not answer the question."

- question: "Describe the tableau construction in the Cook-Levin proof: what does the formula represent, and why does this construction demonstrate that every NP problem reduces to SAT?"
  type: short-answer
  answer: "The tableau is a t×t grid where rows are time steps (1 through t) and columns are tape positions. Three families of variables describe the machine's configuration at each step: cell variables (symbol on each tape cell), head variables (head position), and state variables (current machine state). Clauses enforce: (1) the initial configuration matches the input w, (2) each transition follows the NTM's rules, (3) an accepting state is reached by step t. The formula is satisfiable iff M accepts w. Since this construction works for any polynomial-time NTM, every NP problem (which by definition has a poly-time NTM witness) reduces to SAT."
  explanation: "The formula size is O(t²) — polynomial — because the tableau has t rows and t columns, and each variable or clause is defined for each cell. The reduction itself runs in polynomial time, which is required for the reduction to be valid. The elegance of the proof is that it doesn't use any special property of SAT — it uses only the fact that SAT can express arbitrary boolean constraints. This is what makes SAT the 'universal' NP problem: computation itself can be encoded as a satisfiability question."
```

## Explainer

You already know that NP is the class of problems solvable by a **nondeterministic Turing machine (NTM)** in polynomial time, and that a polynomial-time reduction from problem A to problem B means "if we could solve B quickly, we could solve A quickly." The Cook-Levin theorem asks a sharper question: is there a single problem in NP so hard that *every* NP problem reduces to it? The answer is yes, and that problem is **Boolean satisfiability (SAT)** — the question of whether a propositional formula over variables x₁, …, xₙ has a truth assignment making it true.

The proof works by encoding computation as logic. Any NP problem has a polynomial-time NTM M that witnesses its solutions. Given an input w of length n, M runs in at most t(n) = nᶜ steps. The trick is to build a propositional formula φ_{M,w} — the **tableau formula** — whose satisfying assignments correspond exactly to accepting computation histories of M on w. The formula uses three families of variables: cell variables encoding what symbol occupies each tape cell at each time step, head variables encoding where the read/write head is, and state variables encoding M's current state. Together, they describe a t × t grid of "snapshots" of the machine's tape. Clauses then enforce: (1) the initial configuration matches w, (2) each transition follows the NTM's rules, and (3) M reaches an accepting state by step t.

The formula φ_{M,w} has size O(t²) — polynomial in n — and can be constructed in polynomial time. Here is the key insight: φ_{M,w} is satisfiable if and only if M accepts w. An accepting computation history is exactly a satisfying assignment. So the polynomial-time reduction from any NP problem to SAT is: "given an instance w, output the formula φ_{M,w}." This works for *any* NTM M, which means *every* NP problem reduces to SAT. Combined with the fact that SAT is itself in NP (guess an assignment, verify in polynomial time), SAT is NP-complete.

The theorem's historical weight goes beyond the single result. Before Cook and Levin, there was no vocabulary for saying "these hard-looking problems are all equally hard." By identifying SAT as a universal NP problem, the theorem gave complexity theory its organizing principle: to classify a new problem as NP-complete, you only need to show it's in NP and reduce a single known NP-complete problem to it. Every subsequent NP-completeness proof stands on this foundation — SAT is the ancestor of all known NP-complete problems.

One subtlety worth internalizing: the theorem does not say SAT is unsolvable, or that it requires exponential time. It says SAT is as hard as any problem in NP. Whether NP contains problems that *genuinely* require superpolynomial time — whether P ≠ NP — remains open. Cook-Levin identifies SAT as the right problem to study if you want to resolve P vs. NP; it does not resolve the question itself.
