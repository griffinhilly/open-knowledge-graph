---
id: inner-models-relative-consistency
title: Inner Models and Relative Consistency Proofs
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: constructible-universe
  type: hard
- id: reflection-principles-zfc
  type: soft
builds-toward:
- zfc-independence-from-other-axioms
tags:
- inner-models
- consistency
- l
- godel
stage: advanced
status: validated
---

# Inner Models and Relative Consistency Proofs

## Core Idea
An inner model M is a transitive class satisfying ZFC, contained in V. Gödel's L (constructible sets) is the canonical inner model; it satisfies GCH, the axiom of choice, and V=L. Other inner models (HOD, L[0#], etc.) capture different set-theoretic properties. Relative consistency is proved by embedding statements into inner models: if M ⊨ φ for a statement φ and M ⊆ V, then Con(ZFC) implies Con(ZFC + φ).

## How It's Best Learned
Define L recursively: L₀ = ∅, L_{α+1} = Def(L_α), and L_λ = ⋃_{α < λ} L_α, where Def denotes definable subsets. Prove L ⊨ ZFC. Show Con(ZFC) → Con(ZFC + CH) via the canonical inner model. Explore other inner models and their properties.

## Common Misconceptions
- Assuming inner models are 'true' (they are one model among many; V may not equal L).
- Confusing relative consistency with resolution (GCH is consistent with and independent of ZFC, so neither is 'correct').

## Questions

```yaml
- question: "Gödel showed that L ⊨ GCH. A student concludes: 'Therefore GCH must be true, because L is a subclass of the real universe V and inherits its truth.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "It is correct — if GCH holds in L and L ⊆ V, then GCH holds in V"
    - "It confuses relative consistency with truth: GCH holds in L, but L is not V, and V may satisfy ¬GCH"
    - "It is wrong because L does not actually satisfy GCH"
    - "It is wrong because GCH is provable from ZFC, so no model argument is needed"
  answer: 1
  explanation: "Relative consistency is a conditional result, not an absolute one. L ⊆ V means L is a definable class inside V, but L and V are different structures with different truths. Showing L ⊨ GCH proves Con(ZFC) → Con(ZFC + GCH) — GCH cannot be *disproved* from ZFC — but it says nothing about whether GCH holds in V itself. Cohen's forcing later showed V can also satisfy ¬GCH, establishing full independence."

- question: "Why must an inner model M be transitive in order to function as a genuine model of ZFC?"
  type: multiple-choice
  options:
    - "Transitivity ensures M contains all ordinals of V, giving it sufficient 'height'"
    - "Transitivity ensures the ∈-relation inside M agrees with the actual ∈-relation in V, so M's sets are genuine sets rather than artificial simulations"
    - "Transitivity ensures M is closed under power sets and unions"
    - "Transitivity is a convention, not a logical requirement — non-transitive inner models also work"
  answer: 1
  explanation: "Transitivity means: if a ∈ M and b ∈ a, then b ∈ M. This closure condition ensures that when M 'sees' a membership relation a ∈ b, it is the real ∈ of V — not some artificially restricted version. Without transitivity, M might have sets whose elements fall outside M, making M's ∈-relation a distortion of the true one. Transitive models are honest: their membership relation is the real thing."

- question: "Showing that L ⊨ GCH proves that ZFC + GCH is consistent relative to ZFC."
  type: true-false
  answer: true
  explanation: "This is exactly what the inner model technique establishes. If ZFC has a model (i.e., if ZFC is consistent), then L — constructed inside any model of ZFC — is a model of ZFC + GCH. So a proof of inconsistency of ZFC + GCH would translate into a proof of inconsistency of ZFC. The result is conditional: Con(ZFC) → Con(ZFC + GCH)."

- question: "A relative consistency proof for a statement φ, using an inner model M where φ holds, establishes that φ is true in the actual set-theoretic universe V."
  type: true-false
  answer: false
  explanation: "A relative consistency proof establishes only that φ cannot be *disproved* from ZFC — not that φ is true. The inner model M is one possible set-theoretic universe satisfying ZFC, but V may be a different universe where φ fails. GCH holds in L (an inner model), but Cohen's forcing constructed models of ZFC where GCH fails, showing GCH is independent of ZFC — neither provable nor disprovable."

- question: "Why does a relative consistency proof not settle whether a statement like GCH is 'actually true,' and what additional investigation would be required to fully resolve GCH's status?"
  type: short-answer
  answer: "A relative consistency proof shows only that assuming φ leads to no new contradictions — Con(ZFC) → Con(ZFC + φ). It says nothing about truth in V itself, because V might not equal the inner model M used in the proof. To fully resolve GCH's status requires showing both Con(ZFC + GCH) and Con(ZFC + ¬GCH). Gödel's L gives the first; Cohen's forcing gives the second. Together they establish independence: GCH is neither provable nor disprovable from ZFC, so its truth value depends on which additional axioms (if any) one adopts."
  explanation: "Relative consistency answers 'can this coexist with ZFC?' not 'is this true?' Independence is the strongest possible result from this program: it shows ZFC is genuinely underdetermined about GCH. Resolving which value is 'correct' (if the question has an answer) requires stepping outside ZFC to examine large cardinal axioms, inner model theory at the level of L[U], and other foundational commitments — an active research program in set theory today."
```

## Explainer

From your study of the constructible universe L, you know that Gödel built a specific model inside ZFC — a class where every set is "definable from earlier sets" in a precise transfinite construction. An **inner model** generalizes this idea: it is any transitive class M satisfying all ZFC axioms and contained within the set-theoretic universe V. **Transitivity** is the key closure condition: if a ∈ M and b ∈ a, then b ∈ M. This means the model "doesn't import aliens" — every element of every element of M is already in M. Transitivity ensures that the ∈-relation inside M agrees with the actual ∈-relation in V, making M a "genuine" universe of sets, not an artificial simulation.

The key technique inner models provide is **relative consistency**: showing that if ZFC is consistent, then ZFC + φ is also consistent for some additional statement φ. The method is to exhibit an inner model M where φ holds. Gödel showed L ⊨ V=L (every set is constructible), L ⊨ AC (the axiom of choice holds), and L ⊨ GCH (the generalized continuum hypothesis). Since L is a definable class inside any model of ZFC, if ZFC is consistent then L gives a model of ZFC + GCH. This proves Con(ZFC) → Con(ZFC + GCH): you cannot derive a contradiction from ZFC + GCH without first deriving one from ZFC. In other words, GCH cannot be *disproved* from ZFC alone.

Notice what the technique does *not* prove: it does not show GCH is *true*, or that V = L. It shows only that assuming GCH leads to no new contradictions. This is the nature of relative consistency — a conditional, not an absolute, result. The complementary result, that GCH cannot be *proved* from ZFC, came later from Cohen's forcing method, which constructs models where GCH fails. Together, the inner model technique and forcing establish the **independence** of GCH from ZFC: neither the hypothesis nor its negation follows from the axioms. The inner model Gödel constructed answers "can GCH be false?"; forcing answers "can GCH be true by necessity?" — and both answers are no.

Beyond L, the inner model landscape is rich. **HOD** (hereditarily ordinal-definable sets) is the class of all sets whose entire membership tree is definable from ordinals — strictly larger than L, but still an inner model satisfying AC. The **core model** program (due to Jensen and others) generalizes L to accommodate **large cardinal** axioms: if large cardinals exist in V, L is too small to capture them, but a larger inner model built from "mice" (small structured sets with embeddings) can. The existence of the inner model L[0#] — L extended by a "sharp" encoding structural information about L — is equivalent to 0# existing, which in turn follows from certain large cardinal assumptions. Each inner model is a lens for studying which set-theoretic truths are already "built in" to ZFC versus which require additional axioms. Inner models are not alternative realities to be chosen between — they are tools for probing the structure of V itself.
