---
id: bounded-model-checking
title: Bounded Model Checking
domain: computer-science
course: formal-methods
prerequisites:
- id: model-checking-intro
  type: hard
- id: temporal-logic-ltl-ctl
  type: hard
- id: boolean-satisfiability-and-reductions
  type: hard
- id: symbolic-execution
  type: soft
tags:
- bounded-model-checking
- sat-based-verification
- smt-solving
- counterexample
- bmc
- unrolling
stage: expert
status: validated
---

# Bounded Model Checking

## Core Idea
Bounded model checking (BMC) verifies temporal properties by unrolling the transition relation of a system up to a fixed depth k and encoding the resulting verification problem as a Boolean satisfiability (SAT) or satisfiability modulo theories (SMT) formula. If the formula is satisfiable, a counterexample of length at most k exists; if unsatisfiable, the property holds for all executions of that length. BMC leverages the extraordinary power of modern SAT/SMT solvers, which can handle formulas with millions of variables, to find deep bugs that BDD-based symbolic model checking cannot reach due to state space explosion. While BMC is inherently incomplete (bounded depth), techniques like k-induction and interpolation-based abstraction extend it toward completeness.

## Questions

```yaml
- question: "Bounded model checking encodes the question 'does a property violation exist within k steps?' as a SAT formula. What are the main components of this encoding?"
  type: multiple-choice
  options:
    - "Only the initial state and the property to be checked"
    - "The initial state constraint I(s_0), the transition relation T(s_i, s_{i+1}) unrolled k times, and the negation of the property at each step (disjunction of bad states across steps 0 through k)"
    - "A BDD representing all reachable states and a CTL formula"
    - "The program source code translated directly to CNF"
  answer: 1
  explanation: "The BMC encoding creates Boolean variables for the state at each time step s_0, s_1, ..., s_k. The formula is: I(s_0) AND T(s_0,s_1) AND T(s_1,s_2) AND ... AND T(s_{k-1},s_k) AND (NOT P(s_0) OR NOT P(s_1) OR ... OR NOT P(s_k)), where I is the initial state predicate, T is the transition relation, and P is the safety property. A satisfying assignment gives concrete state values at each step -- a counterexample trace. If UNSAT, no violation exists in k steps. The formula size grows linearly with k, making deep unrolling feasible with modern SAT solvers."

- question: "BDD-based symbolic model checking computes the exact set of reachable states, while bounded model checking does not. Why is BMC often more effective at finding bugs in practice?"
  type: short-answer
  answer: "BDD-based model checking builds a BDD representing ALL reachable states, which can blow up exponentially in the number of state variables (the BDD size is highly sensitive to variable ordering and system structure). BMC avoids constructing the full reachable state set -- it only asks whether a counterexample of bounded length exists. Modern SAT solvers handle formulas with millions of variables through conflict-driven clause learning (CDCL), which exploits the structure of the specific instance. For bug finding, BMC is superior because bugs typically manifest as short counterexamples, and SAT solvers are remarkably efficient at finding satisfying assignments (or proving unsatisfiability) for structured industrial formulas."
  explanation: "The empirical dominance of SAT-based BMC over BDD-based methods for bug finding was demonstrated convincingly by Biere, Cimatti, Clarke, and Zhu (1999). Key insight: for verification (proving absence of bugs), BDD methods may still be necessary since BMC at depth k only proves safety up to k steps. However, k-induction and Craig interpolation extend BMC toward complete verification."

- question: "K-induction strengthens bounded model checking to achieve complete verification (not just bounded bug-finding). The induction step checks whether any state satisfying the property for k consecutive steps must also satisfy it at step k+1."
  type: true-false
  answer: true
  explanation: "K-induction has two parts: (1) the base case checks that the property holds for all states reachable in 0 to k steps from the initial states (standard BMC with UNSAT result), and (2) the induction step checks: for ANY sequence of k+1 states satisfying the transition relation, if the property holds at steps 0 through k-1, does it hold at step k? If the induction step is also UNSAT (no counterexample to the inductive hypothesis), the property holds for all reachable states at any depth. The parameter k controls the strength of the induction: k=1 is standard induction, larger k handles properties that require stronger inductive invariants. K-induction is complete for finite-state systems (some k suffices) but finding the right k may require auxiliary invariants."

- question: "Craig interpolation is used in BMC-based verification to derive an overapproximation of the reachable states from an unsatisfiability proof. Why is this useful for proving unbounded safety properties?"
  type: short-answer
  answer: "When a BMC formula at depth k is UNSAT, the SAT solver produces a proof of unsatisfiability. Craig's interpolation theorem guarantees that from a proof that A AND B is unsatisfiable, one can extract a formula (the interpolant) that is implied by A, inconsistent with B, and uses only variables common to A and B. In BMC, A encodes the first i transition steps and B encodes the remaining steps plus the property violation. The interpolant overapproximates the states reachable in i steps. Iteratively computing interpolants for increasing depths builds an overapproximation of the full reachable state set. If this overapproximation stabilizes (reaches a fixed point) and excludes all bad states, unbounded safety is proven -- without ever computing the exact reachable state set."
  explanation: "McMillan (2003) introduced interpolation-based model checking, which combines the bug-finding power of SAT-based BMC with the completeness of image computation. The key advantage over BDD-based approaches is that interpolants are computed from SAT proofs (leveraging CDCL efficiency) rather than BDD operations (which suffer from variable ordering sensitivity). This approach has been highly successful in hardware verification, where systems have enormous state spaces but structured transition relations."
```

## Explainer

Classical model checking, as introduced by Clarke and Emerson, computes the set of all reachable states and checks whether a temporal property holds throughout. The standard implementation uses BDDs (Binary Decision Diagrams) to represent state sets symbolically, avoiding explicit enumeration. While BDD-based methods are complete -- they give a definitive yes/no answer -- they often fail on large systems because BDD size can explode exponentially, with performance highly sensitive to variable ordering. **Bounded model checking** (BMC), introduced by Biere, Cimatti, Clarke, and Zhu in 1999, takes a fundamentally different approach: instead of computing all reachable states, it asks a bounded question -- does a counterexample of length at most k exist?

The BMC encoding is elegant. Create Boolean variables representing the system state at each time step 0 through k. Assert that step 0 satisfies the initial condition, each consecutive pair of steps satisfies the transition relation, and at least one step violates the property. The conjunction of these constraints is a propositional formula: if SAT, the satisfying assignment is a concrete counterexample trace; if UNSAT, no violation exists within k steps. The formula size grows linearly in k and in the size of the transition relation, making it feasible to unroll systems for hundreds or thousands of steps. Modern **CDCL SAT solvers** (MiniSat, CaDiCaL, Kissat) exploit the structure of these formulas through unit propagation, conflict-driven learning, and restarts, routinely handling millions of variables.

For **software verification**, BMC extends naturally to **SMT** (Satisfiability Modulo Theories). Instead of encoding everything as bare Boolean variables, the formula uses richer theories: linear integer arithmetic for loop counters, bitvector arithmetic for machine integers, arrays for memory, and uninterpreted functions for abstractions. SMT solvers like Z3, CVC5, and MathSAT integrate theory-specific solvers with the CDCL framework, handling the richer formulas that arise from software models. Tools like CBMC (C Bounded Model Checker) translate C programs directly into BMC formulas, unrolling loops up to a bound and encoding each statement's semantics as SMT constraints.

The main limitation of BMC is **incompleteness**: an UNSAT result at depth k only proves safety up to k steps, not for all executions. Two techniques address this. **K-induction** adds an induction step: if no counterexample exists in k steps from any state (not just initial states) and the property held for the previous k-1 steps, then the property holds universally. When k-induction succeeds, it provides a complete proof of unbounded safety. **Craig interpolation** extracts an overapproximation of the reachable states from BMC unsatisfiability proofs. The interpolant is implied by the first few transitions, inconsistent with property violations, and uses only state variables (not time-step indices). Iteratively computing interpolants and checking for a fixed point yields complete verification: if the overapproximation stabilizes without including any bad states, the property holds for all reachable states. McMillan's interpolation-based model checking (2003) combines the scalability of SAT solving with the completeness of reachability analysis, representing one of the most significant advances in practical verification.

BMC has had enormous practical impact. In **hardware verification**, it is the standard first-pass technique at Intel, AMD, and other semiconductor companies, finding bugs in processor designs that BDD-based methods miss due to state explosion. In **software verification**, CBMC and similar tools find buffer overflows, integer overflows, and assertion violations in C/C++ code. The **HWMCC** (Hardware Model Checking Competition) and **SV-COMP** (Software Verification Competition) benchmarks consistently show SAT/SMT-based techniques outperforming BDD-based methods on industrial instances. The success of BMC exemplifies a broader trend in formal methods: leveraging the remarkable empirical performance of SAT/SMT solvers to solve verification problems that are theoretically intractable (SAT is NP-complete) but structured enough to be tractable in practice.
