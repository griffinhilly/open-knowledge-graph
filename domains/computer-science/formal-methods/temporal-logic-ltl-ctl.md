---
id: temporal-logic-ltl-ctl
title: "Temporal Logic: LTL and CTL"
domain: computer-science
course: formal-methods
prerequisites:
- id: model-checking-intro
  type: hard
- id: propositional-logic-introduction
  type: hard
- id: kripke-structures
  type: soft
builds-toward:
- bdd-based-verification
tags:
- linear-temporal-logic
- computation-tree-logic
- ltl
- ctl
- liveness
- safety
stage: expert
status: validated
---
# Temporal Logic: LTL and CTL

## Core Idea
Temporal logics extend propositional logic with operators that express properties over time, enabling specification of system behaviors like "every request is eventually granted" (liveness) or "the system never enters an error state" (safety). Linear Temporal Logic (LTL) reasons about individual execution paths using operators like G (globally/always), F (finally/eventually), X (next), and U (until). Computation Tree Logic (CTL) reasons about the branching tree of all possible futures, combining path quantifiers (A = all paths, E = some path) with temporal operators. LTL and CTL have incomparable expressive power: each can express properties the other cannot.

## Questions

```yaml
- question: "The LTL formula G(request -> F grant) expresses which property?"
  type: multiple-choice
  options:
    - "If a request occurs, a grant must occur in the very next state"
    - "On every execution path, whenever a request occurs, a grant eventually follows at some future point"
    - "There exists some path where every request is followed by a grant"
    - "Grants always precede requests"
  answer: 1
  explanation: "G means 'globally' (at every point in time) and F means 'finally' (at some future point). So G(request -> F grant) says: at every moment, if request holds, then there exists some future moment where grant holds. LTL formulas are implicitly universally quantified over all paths, so this must hold on every possible execution. This is a classic liveness property — something good eventually happens."

- question: "LTL and CTL have the same expressive power — any property expressible in one can be expressed in the other."
  type: true-false
  answer: false
  explanation: "LTL and CTL are incomparable in expressiveness. The CTL formula AG(EF restart) ('from every reachable state, there exists a path to restart') cannot be expressed in LTL because LTL cannot mix path quantifiers with temporal operators at arbitrary nesting depths. Conversely, the LTL formula F(G p) ('eventually p holds forever') cannot be expressed in CTL. The logic CTL* subsumes both, combining branching-time quantifiers with arbitrary linear-time operators."

- question: "Explain the difference between the safety property G(not error) and the liveness property G(request -> F grant), and why this distinction matters for verification."
  type: short-answer
  answer: "G(not error) is a safety property: it says something bad (error) NEVER happens. Any violation is witnessed by a finite prefix of execution reaching the bad state. G(request -> F grant) is a liveness property: it says something good (grant) EVENTUALLY happens after a request. Violations require infinite traces where the grant never arrives. Safety properties can be checked on finite executions, while liveness properties require reasoning about infinite behavior, making them fundamentally harder to verify."
  explanation: "This distinction affects model checking algorithms. Safety violations produce finite counterexamples (a path to the bad state). Liveness violations require finding infinite counterexamples, typically lasso-shaped: a finite prefix followed by a cycle that repeats forever without satisfying the liveness condition. The algorithmic machinery for detecting such cycles (nested DFS, accepting conditions of Buchi automata) is more complex than simple reachability analysis for safety."

- question: "In CTL, what is the difference between AG p and EG p?"
  type: short-answer
  answer: "AG p means 'on ALL paths, p holds Globally (at every state)' — p is true in every reachable state of the system. EG p means 'there EXISTS a path where p holds Globally' — there is at least one infinite execution where p is always true, though other paths may violate p. AG is a universal guarantee about all behaviors; EG is an existential claim about one possible behavior."
  explanation: "The path quantifiers A (for all paths) and E (exists a path) are what distinguish CTL from LTL. LTL formulas are implicitly universally quantified over paths (like AG), but CTL allows mixing A and E at every level of nesting. AG(EF p) — 'from every reachable state, there exists some path eventually reaching p' — is a natural CTL property with no LTL equivalent."
```

## Explainer

Temporal logic provides the **specification language** for model checking. While propositional logic can describe what is true at a single moment, temporal logic adds operators that talk about the evolution of truth over time — what was true, what will become true, what remains true forever. Two families dominate formal methods: **Linear Temporal Logic (LTL)** and **Computation Tree Logic (CTL)**.

**LTL** views time as a single infinite sequence of states — one execution path. Its temporal operators modify propositions relative to positions along this path. **G p** (globally p) means p holds at every future position. **F p** (finally p) means p holds at some future position. **X p** (next p) means p holds at the immediately next position. **p U q** (p until q) means p holds continuously until q becomes true (and q must eventually become true). Complex properties compose these: G(request -> F grant) says "always, a request is followed by an eventual grant." LTL formulas are implicitly universally quantified over all execution paths — the property must hold on every possible run of the system.

**CTL** views time as a branching tree: at each state, the system may transition to multiple possible successor states (representing nondeterminism or concurrency). CTL combines **path quantifiers** (A = "for all paths from this state," E = "there exists a path from this state") with **state-level temporal operators** (G, F, X, U). These always appear in pairs: AG p, EF p, AX p, EU(p,q), etc. The formula AG(not deadlock) means "on all paths, globally, no deadlock occurs." The formula AG(EF restart) means "from every reachable state, on all paths, there exists a path reaching a restart state" — the system can always potentially recover.

The two logics are **incomparable** in expressiveness. LTL can express fairness properties like F(G p) ("eventually p holds forever") that CTL cannot. CTL can express branching properties like AG(EF p) ("p is always reachable") that LTL cannot. The unifying logic **CTL*** subsumes both, allowing arbitrary nesting of path quantifiers and temporal operators, but its model checking algorithms are more expensive. In practice, the choice between LTL and CTL depends on the property: use LTL for path-centric properties (fairness, response patterns) and CTL for branching properties (reachability, recoverability).

The distinction between **safety** and **liveness** properties cuts across both logics. Safety properties (G not bad) say "nothing bad ever happens" — they are violated by finite prefixes. Liveness properties (G(request -> F response)) say "something good eventually happens" — they can only be violated by infinite traces where the good thing never occurs. This distinction profoundly affects model checking algorithms: safety violations produce finite counterexample traces, while liveness violations produce "lasso" counterexamples (a finite stem followed by an infinitely repeating cycle). Understanding which temporal operators express safety vs. liveness is essential for writing effective specifications.
