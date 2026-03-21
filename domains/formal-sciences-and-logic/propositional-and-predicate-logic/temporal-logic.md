---
id: temporal-logic
title: Temporal Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: modal-logic-intro
  type: hard
builds-toward: []
tags:
- temporal-logic
- LTL
- CTL
- Kripke-structures
- model-checking
- program-verification
stage: advanced
status: draft
---

# Temporal Logic

## Core Idea
Temporal logic specializes modal logic to reason about time. Linear Temporal Logic (LTL) models time as a single infinite sequence of states, with operators G (always/globally), F (eventually/finally), X (next), and U (until). Computation Tree Logic (CTL) models time as a branching tree, adding path quantifiers A (on all paths) and E (on some path) before temporal operators. Both are interpreted over Kripke structures where the accessibility relation represents temporal succession. Temporal logic is the formal backbone of model checking — the automated verification technique that exhaustively tests whether a system satisfies its specification, used extensively in hardware and software verification.

## How It's Best Learned
Write LTL specifications for simple properties (e.g., "every request is eventually followed by a response" = G(request → F response)) and evaluate them on small transition systems drawn as labeled graphs. Then compare LTL and CTL expressiveness by finding properties expressible in one but not the other.

## Common Misconceptions
- LTL and CTL are not subsets of each other — they are incomparable in expressiveness. Some properties (e.g., fairness) are expressible in LTL but not CTL, and vice versa.
- The "always" operator G does not mean "at every time step from now" in CTL without a path quantifier — AG and EG mean very different things.
- Temporal logic model checking is decidable and efficient for finite-state systems, but undecidable for infinite-state systems in general.

## Questions

```yaml
- question: "The LTL formula GF p means 'p holds infinitely often on every execution trace.' Which statement about this property is correct?"
  type: multiple-choice
  options:
    - "It is expressible in CTL as AGF p, making LTL and CTL equivalent for this property"
    - "It is expressible in CTL as AGAF p, which is distinct from the LTL formula"
    - "It cannot be expressed in CTL because CTL cannot quantify over all positions on a single infinite trace"
    - "It is equivalent to AF p in CTL since CTL handles fairness natively"
  answer: 2
  explanation: "GF p (p holds infinitely often) is a canonical LTL property that has no direct CTL equivalent. CTL path quantifiers (A, E) must immediately precede temporal operators (G, F, X, U) — you cannot nest them freely. The CTL formula AGAF p means 'from every reachable state, on all paths from there, p eventually holds,' which is a stronger property than 'p holds infinitely often on traces.' This incomparability — where LTL can express trace-level properties that CTL cannot — is why neither logic subsumes the other."

- question: "In CTL, what is the difference between AG φ and EG φ at a given state s?"
  type: multiple-choice
  options:
    - "No difference — both say φ holds at every future state reachable from s"
    - "AG φ means φ holds on all paths from s; EG φ means φ holds on some path from s; they can have different truth values at s"
    - "AG φ is the LTL interpretation and EG φ is the CTL interpretation of the same property"
    - "AG φ means φ holds at all states globally in the model; EG φ is restricted to successors of s"
  answer: 1
  explanation: "CTL path quantifiers (A = 'on all paths', E = 'on some path') fundamentally change meaning. AG φ is true at s if φ holds at every state on every computation path from s — a universal claim. EG φ is true at s if there exists at least one computation path from s where φ holds at every state. A branching system can have states where one path maintains φ indefinitely (making EG φ true) while another path eventually violates φ (making AG φ false). This distinction only makes sense in CTL's branching-time view of computation."

- question: "CTL is strictly more expressive than LTL because CTL adds path quantifiers A and E that LTL lacks."
  type: true-false
  answer: false
  explanation: "LTL and CTL are *incomparable* in expressiveness — neither is a subset of the other. Some properties are expressible in LTL but not CTL (e.g., GF p, 'p holds infinitely often'), and some are expressible in CTL but not LTL (e.g., EF safe, 'there exists a path where safe is eventually reached' — a branching reachability property that quantifies over the tree structure). The key insight is that LTL reasons about individual traces while CTL reasons about the branching structure of all possible executions; these are fundamentally different perspectives, not one extending the other."

- question: "Temporal logic model checking for finite-state systems is decidable, meaning there is an algorithm that always terminates with a correct yes/no answer."
  type: true-false
  answer: true
  explanation: "For finite-state systems (Kripke structures with finitely many states), both LTL and CTL model checking are decidable and run in polynomial time in the size of the model. The main practical challenge is state space explosion — the model size grows exponentially in the number of system variables — but this is an engineering challenge, not a decidability barrier. Model checking becomes undecidable for infinite-state systems in general, but the finite-state case, which covers most hardware and many software verification problems, is algorithmically tractable."

- question: "Explain in your own words why LTL and CTL are incomparable in expressiveness, rather than one being a subset of the other."
  type: short-answer
  answer: "LTL treats time as a single infinite sequence (a trace) and cannot distinguish between 'all paths' and 'some path.' CTL treats time as a branching tree and requires path quantifiers before every temporal operator, which prevents it from making statements about a single infinite trace. LTL can say 'p holds infinitely often on this trace' (GF p) — a property about the long-run behavior of one path — while CTL cannot express this directly. Conversely, CTL can say 'there exists some path where q is eventually reached' (EF q) — a branching reachability property — while LTL cannot, because LTL quantifies implicitly over all traces. Each logic captures something the other misses."
  explanation: "The incomparability reflects the fundamental design difference: LTL's linear-time view is better at trace-level properties like fairness and liveness along a single execution, while CTL's branching-time view is better at reachability and safety properties over the full state space. Neither view strictly dominates. CTL* was developed as a unifying logic that subsumes both, but at a computational cost."
```

## Explainer

You already know modal logic: formulas are evaluated at **worlds** in a **Kripke structure**, and the modal operators □ (box, "necessarily") and ◇ (diamond, "possibly") quantify over worlds accessible from the current one. Temporal logic is modal logic where the accessibility relation represents *time*: worlds become **states** (snapshots of a system), and the accessibility relation connects a state to its successors in the next time step. The modal operators are renamed and specialized for temporal meaning, and the result is a family of logics purpose-built for reasoning about how systems evolve.

**Linear Temporal Logic (LTL)** assumes time is a single infinite sequence of states — like a program's execution trace. The four temporal operators are: **G** (globally, i.e., □: holds at all future states including now), **F** (finally, i.e., ◇: holds at some future state), **X** (next: holds at the immediately next state), and **U** (until: φ U ψ means φ holds continuously until ψ becomes true). LTL is evaluated on paths — infinite sequences of states — not on states in a structure. A formula like G(request → F response) says "on every suffix of the trace, whenever a request occurs, a response eventually follows." This is a **liveness property**: something good eventually happens.

**Computation Tree Logic (CTL)** takes a different view of time: from any state, execution can branch into multiple possible futures (like a nondeterministic program or a concurrent system). Time is a tree, not a line. CTL adds **path quantifiers** A ("on all paths from this state") and E ("on some path from this state"), which must be combined with temporal operators: AG φ (globally on all paths), EF φ (eventually on some path), etc. The branching structure lets CTL express properties that LTL cannot: for instance, EF(safe) says "there exists a path where we eventually reach a safe state" — a reachability property that quantifies over the tree structure rather than a single trace. Conversely, some LTL properties (like "on the actual trace, P holds infinitely often") cannot be expressed in CTL, which is why LTL and CTL are incomparable in expressiveness.

**Model checking** is the automated process of verifying whether a finite-state system M satisfies a temporal logic formula φ. The model checker exhaustively explores the state space of M (typically a Kripke structure representing all possible program states) and checks whether φ holds. For LTL, the standard algorithm converts ¬φ to a **Büchi automaton** (a finite automaton over infinite words) and checks whether the product automaton M ⊗ A_¬φ has an accepting run — if not, M satisfies φ. For CTL, a direct **labeling algorithm** marks each state with the subformulas it satisfies, working bottom-up. Both algorithms run in polynomial time in the size of M and exponential time in the size of φ — the state space explosion (M growing exponentially in the number of variables) is the main engineering challenge, addressed by symbolic model checking using BDDs. Temporal logic is the specification language of choice for hardware verification, protocol analysis, and reactive system design precisely because it is expressive, rigorous, and mechanically checkable.

