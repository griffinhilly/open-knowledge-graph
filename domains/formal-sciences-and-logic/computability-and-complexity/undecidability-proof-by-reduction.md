---
id: undecidability-proof-by-reduction
title: Proving Undecidability via Reduction
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: halting-problem-formal
  type: hard
- id: reducibility-many-one-formal
  type: hard
builds-toward:
- rices-theorem-applications
- post-correspondence-problem
tags:
- undecidability
- proofs
- reduction
stage: formal-systems
status: draft
---

# Proving Undecidability via Reduction

## Core Idea
To show a language L is undecidable, reduce the halting problem (or another known undecidable language) to L: if HALT ≤_m L and HALT is undecidable, then L is undecidable. This technique avoids directly reasoning about diagonal arguments and makes undecidability results intuitive: L inherits the computational hardness of HALT.

## How It's Best Learned
Practice reductions from HALT to at least three non-trivial languages (e.g., emptiness of a Turing machine's language, equivalence of machines, totality of a function).

## Common Misconceptions
- Confusing the direction of reduction (reducing HALT to L proves L is hard, not the other way around).
- Assuming a reduction must preserve decidability; it preserves undecidability.

## Questions

```yaml
- question: "A student constructs a computable function f such that for any (M, w), f(M, w) = ⟨M'⟩ where M' accepts all inputs iff M halts on w. She claims this proves L_total = {⟨M⟩ : M halts on every input} is undecidable. Why does her construction succeed?"
  type: multiple-choice
  options:
    - "Because f is computable, any problem reducible from it must be decidable"
    - "Because if L_total were decidable, composing a decider for L_total with f would decide HALT, contradicting HALT's undecidability"
    - "Because f reduces L_total to HALT, showing L_total is no harder than HALT"
    - "Because M' accepts all inputs, proving totality is a trivial property"
  answer: 1
  explanation: "This is the reduction proof by contrapositive. f defines HALT ≤_m L_total. Suppose L_total were decidable by machine D. Given any (M, w), compute f(M, w) = ⟨M'⟩, then run D on ⟨M'⟩. D accepts iff M' ∈ L_total iff M' halts on every input iff M halts on w — so D∘f decides HALT. Since HALT is undecidable, this contradiction shows L_total must be undecidable too. Option C confuses the direction: f reduces *from* HALT *to* L_total, establishing that L_total is at least as hard as HALT, not the other way."

- question: "A researcher shows that language A ≤_m language B, and B is known to be decidable. What can be concluded about A?"
  type: multiple-choice
  options:
    - "A is undecidable — the reduction shows A is at least as hard as B"
    - "A is decidable — the reduction function combined with a decider for B decides A"
    - "Nothing — many-one reductions do not preserve decidability"
    - "A is decidable only if the reduction function is injective"
  answer: 1
  explanation: "When A ≤_m B via computable f and B has a decider D_B, we decide A as follows: on input x, compute f(x) and run D_B on f(x); accept iff D_B accepts, since x ∈ A iff f(x) ∈ B. Reductions carry decidability downward (from B to A). The contrapositive — used in undecidability proofs — is: if A is undecidable and A ≤_m B, then B must be undecidable. Option C is wrong; reducibility does preserve both decidability and undecidability in the appropriate directions."

- question: "To prove L is undecidable via reduction from HALT, the reduction function f must satisfy: (M, w) ∈ HALT if and only if f(M, w) ∈ L."
  type: true-false
  answer: true
  explanation: "This biconditional is the exact requirement for a many-one reduction HALT ≤_m L. Both directions are necessary: the ⟹ direction (if M halts on w, then f(M, w) ∈ L) and the ⟸ direction (if f(M, w) ∈ L, then M halts on w). Together they guarantee that a hypothetical decider for L, composed with f, would correctly decide HALT. A one-directional implication is insufficient — it would allow L-instances to behave differently from HALT-instances in the missing direction, breaking the simulation."

- question: "Showing that HALT ≤_m L (HALT reduces to L) proves that HALT is undecidable, since L's undecidability transfers back to HALT."
  type: true-false
  answer: false
  explanation: "This reverses both the direction and the logic. HALT ≤_m L means L is at least as hard as HALT — L's undecidability flows *from* HALT's, not toward it. HALT's undecidability is the *premise* (established independently by the diagonal argument), not the conclusion. The proof shows: if L were decidable, HALT would be decidable — contradiction — so L is undecidable. You cannot use a reduction to prove HALT undecidable; reductions propagate hardness *to* the target language, not back to the source."

- question: "Why does the direction of a many-one reduction matter when proving undecidability? What goes wrong if the reduction runs in the wrong direction?"
  type: short-answer
  answer: "To prove L undecidable, you need HALT ≤_m L — a computable f transforming HALT instances into L instances. This shows that solving L would solve HALT (impossible), so L has no decider. If you construct L ≤_m HALT instead, you've only shown that HALT is at least as hard as L — already known, since HALT is undecidable. The wrong direction tells you nothing about L's decidability: L might still be decidable by some means that doesn't go through HALT. The reduction must flow from the known-hard problem to the target to propagate hardness to the target."
  explanation: "Intuition: 'A ≤_m B' means 'B is at least as hard as A — a B-solver can simulate an A-solver.' For undecidability, you want to show your target (L) is hard enough to simulate HALT. That requires HALT ≤_m L. The reverse (L ≤_m HALT) only shows HALT is hard enough to simulate L — but HALT's hardness was already established. The direction of the reduction is the direction of hardness inheritance."
```

## Explainer

You know the halting problem is undecidable: no Turing machine can determine, for all pairs (M, w), whether machine M halts on input w. **Reduction-based undecidability proofs** turn this established fact into a general technique. To show a new language L is undecidable, demonstrate that being able to decide L would let you decide the halting problem. Since the halting problem is already known to be undecidable, L must be undecidable too.

The formal tool is **many-one reducibility**: HALT ≤ₘ L means there exists a computable, total function f such that (M, w) ∈ HALT ⟺ f(M, w) ∈ L. The function f transforms halting-problem instances into L-instances, and it does so completely and computably — you can always compute the transformation, even though you cannot solve either problem. The undecidability proof is by contrapositive: if you had a decider for L, composing it with f would yield a decider for HALT. Since no HALT-decider exists, no L-decider can exist either.

Getting the **direction of the reduction** right is the most common pitfall. The reduction goes *from* the known-hard problem *to* the problem you want to prove hard. "HALT ≤ₘ L" says "L is at least as hard as HALT." If you accidentally reduce in the wrong direction (L ≤ₘ HALT), you are only showing that HALT is at least as hard as L — which is uninformative since HALT was already known to be hard. The intuition: if you can transform any HALT instance into an L instance, then a hypothetical L-solver is strong enough to solve HALT.

A worked example cements the technique. Consider L_empty = {⟨M⟩ : L(M) = ∅}, the set of machine encodings whose language is empty. Given any pair (M, w), construct a new machine M' that, on any input x, first simulates M on w and then accepts. M' accepts at least one string if and only if M halts on w — so (M, w) ∈ HALT ⟺ ⟨M'⟩ ∉ L_empty. The map (M, w) ↦ ⟨M'⟩ is computable, making this a valid many-one reduction. Since HALT is undecidable, L_empty must be too. This pattern generalizes: any non-trivial property of Turing machine languages is undecidable, which is precisely Rice's theorem.
