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

## Explainer

You already know modal logic: formulas are evaluated at **worlds** in a **Kripke structure**, and the modal operators □ (box, "necessarily") and ◇ (diamond, "possibly") quantify over worlds accessible from the current one. Temporal logic is modal logic where the accessibility relation represents *time*: worlds become **states** (snapshots of a system), and the accessibility relation connects a state to its successors in the next time step. The modal operators are renamed and specialized for temporal meaning, and the result is a family of logics purpose-built for reasoning about how systems evolve.

**Linear Temporal Logic (LTL)** assumes time is a single infinite sequence of states — like a program's execution trace. The four temporal operators are: **G** (globally, i.e., □: holds at all future states including now), **F** (finally, i.e., ◇: holds at some future state), **X** (next: holds at the immediately next state), and **U** (until: φ U ψ means φ holds continuously until ψ becomes true). LTL is evaluated on paths — infinite sequences of states — not on states in a structure. A formula like G(request → F response) says "on every suffix of the trace, whenever a request occurs, a response eventually follows." This is a **liveness property**: something good eventually happens.

**Computation Tree Logic (CTL)** takes a different view of time: from any state, execution can branch into multiple possible futures (like a nondeterministic program or a concurrent system). Time is a tree, not a line. CTL adds **path quantifiers** A ("on all paths from this state") and E ("on some path from this state"), which must be combined with temporal operators: AG φ (globally on all paths), EF φ (eventually on some path), etc. The branching structure lets CTL express properties that LTL cannot: for instance, EF(safe) says "there exists a path where we eventually reach a safe state" — a reachability property that quantifies over the tree structure rather than a single trace. Conversely, some LTL properties (like "on the actual trace, P holds infinitely often") cannot be expressed in CTL, which is why LTL and CTL are incomparable in expressiveness.

**Model checking** is the automated process of verifying whether a finite-state system M satisfies a temporal logic formula φ. The model checker exhaustively explores the state space of M (typically a Kripke structure representing all possible program states) and checks whether φ holds. For LTL, the standard algorithm converts ¬φ to a **Büchi automaton** (a finite automaton over infinite words) and checks whether the product automaton M ⊗ A_¬φ has an accepting run — if not, M satisfies φ. For CTL, a direct **labeling algorithm** marks each state with the subformulas it satisfies, working bottom-up. Both algorithms run in polynomial time in the size of M and exponential time in the size of φ — the state space explosion (M growing exponentially in the number of variables) is the main engineering challenge, addressed by symbolic model checking using BDDs. Temporal logic is the specification language of choice for hardware verification, protocol analysis, and reactive system design precisely because it is expressive, rigorous, and mechanically checkable.

