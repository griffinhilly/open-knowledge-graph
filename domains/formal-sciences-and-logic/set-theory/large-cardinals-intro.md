---
id: large-cardinals-intro
title: Introduction to Large Cardinals
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: continuum-hypothesis
  type: soft
- id: singular-cardinals
  type: soft
builds-toward: []
tags:
- large cardinals
- inaccessible cardinals
- Mahlo cardinals
- measurable cardinals
- consistency strength
stage: formal-systems
status: validated
---

# Introduction to Large Cardinals

## Core Idea
Large cardinal axioms postulate the existence of cardinals so large that their existence cannot be proved from ZFC alone — each one strengthens the consistency strength of the theory. An inaccessible cardinal κ is uncountable, regular (cf(κ) = κ), and a strong limit (2^λ < κ for all λ < κ); if such a cardinal exists, then V_κ is a model of ZFC, so ZFC cannot prove inaccessibles exist without proving its own consistency. Mahlo cardinals are inaccessible cardinals where the set of inaccessible cardinals below is stationary. Measurable cardinals carry a non-trivial κ-complete ultrafilter and imply the existence of elementary embeddings of the universe. These axioms form a roughly linear hierarchy of increasing consistency strength, providing a yardstick for measuring the logical power of mathematical statements.

## How It's Best Learned
Begin with inaccessible cardinals: verify that if κ is inaccessible then V_κ satisfies each ZFC axiom, so Con(ZFC + 'there exists an inaccessible') implies Con(ZFC). Then see how Mahlo cardinals strengthen inaccessibility by requiring 'many' inaccessibles below. For measurable cardinals, focus on the ultrafilter characterization before encountering elementary embeddings. The key insight is that each large cardinal axiom is a natural strengthening of the previous one, not an ad hoc addition.

## Common Misconceptions
- Large cardinals are not just 'very big numbers' — their defining property is logical strength (what new theorems they allow), not mere size.
- The large cardinal hierarchy is not strictly linear in every detail, but the main levels (inaccessible < Mahlo < measurable < supercompact < ...) are well-ordered by consistency strength.

## Questions

```yaml
- question: "Why can ZFC not prove the existence of an inaccessible cardinal, assuming ZFC is consistent?"
  type: multiple-choice
  options:
    - "Inaccessible cardinals are too large to be defined within ZFC's language"
    - "The axiom of choice forbids inaccessible cardinals from existing"
    - "If an inaccessible cardinal κ exists, then V_κ models ZFC, so ZFC + 'inaccessibles exist' proves Con(ZFC) — which ZFC cannot do by Gödel's second incompleteness theorem"
    - "Inaccessible cardinals require additional axioms about class-sized structures"
  answer: 2
  explanation: "This is the central reason large cardinal axioms transcend ZFC. If κ is inaccessible, the cumulative hierarchy up to stage κ (denoted V_κ) satisfies every ZFC axiom — so κ's existence provides a model of ZFC inside your universe. By Gödel's second incompleteness theorem, if ZFC is consistent it cannot prove its own consistency. But ZFC + 'an inaccessible exists' does prove Con(ZFC). Therefore, plain ZFC cannot prove the inaccessible exists without proving its own consistency — which it cannot do."

- question: "What properties distinguish an inaccessible cardinal κ from a large cardinal like ℵ_ω that ZFC can prove exists?"
  type: multiple-choice
  options:
    - "κ must be the first uncountable cardinal"
    - "κ must be the cardinality of some set whose existence cannot be stated in ZFC"
    - "κ is both regular (not expressible as a union of fewer-than-κ smaller sets) and a strong limit (2^λ < κ for all λ < κ), while ℵ_ω fails regularity"
    - "κ must be larger than every ordinal definable by a formula with parameters"
  answer: 2
  explanation: "ℵ_ω is a countable union ℵ₀ ∪ ℵ₁ ∪ ℵ₂ ∪ ... of sets each smaller than ℵ_ω — so it fails regularity. An inaccessible cardinal κ cannot be reached 'from below' by either of ZFC's main closure operations: taking unions of fewer than κ smaller sets (regularity) or taking power sets of smaller cardinals (strong limit). Together these make V_κ a natural model of ZFC. ℵ_ω's existence follows from ZFC's axiom of replacement; inaccessibles' existence does not."

- question: "Large cardinals are called 'large' primarily because they are very large cardinal numbers — far bigger than ℵ_ω or other infinite cardinals provable from ZFC."
  type: true-false
  answer: false
  explanation: "False — large cardinals are defined by structural and logical properties, not by raw size. What makes a cardinal 'large' in the set-theoretic sense is its consistency strength: its existence implies Con(ZFC), something ZFC alone cannot establish. Many ZFC-provable cardinals are size-wise enormous (ℵ_{ω₁}, ℵ_{ω·ω}, ...) yet are not large cardinals. An inaccessible cardinal is 'large' because its existence gives a model of ZFC inside the universe — a logical richness property, not a size threshold."

- question: "ZFC + 'there exists a measurable cardinal' is strictly stronger in consistency strength than ZFC + 'there exists an inaccessible cardinal.'"
  type: true-false
  answer: true
  explanation: "True — the large cardinal hierarchy is well-ordered by consistency strength: inaccessible < Mahlo < measurable < ... (and further up). A measurable cardinal carries a κ-complete non-principal ultrafilter that allows constructing an elementary embedding j: V → M, which implies the existence of many inaccessible and Mahlo cardinals below it. So ZFC + measurable proves Con(ZFC + inaccessible), but not vice versa. Each level of the hierarchy strictly outpowers all levels below it — this is the precise meaning of 'higher consistency strength.'"

- question: "What does it mean for one large cardinal axiom to have 'greater consistency strength' than another? Why does this concept matter for mathematics beyond set theory?"
  type: short-answer
  answer: "A theory T₁ has greater consistency strength than T₂ if T₁ proves Con(T₂) but T₂ does not prove Con(T₁). For large cardinals: ZFC + measurable proves Con(ZFC + inaccessible) but not vice versa, so measurable is strictly stronger. This matters beyond set theory because when a theorem in analysis, combinatorics, or algebra requires a large cardinal axiom of level X to prove, that tells us the theorem's exact logical price — how much additional assumption is needed beyond ZFC. Large cardinals serve as a calibration scale: they let mathematicians quantify the logical strength of theorems that would otherwise seem to require incomparable axioms."
  explanation: "The large cardinal hierarchy's near-linearity is itself a deep theorem — it is not obvious that consistency strength should be well-ordered, but it turns out that virtually all natural mathematical statements are comparable in this scale. This gives set theory a central role as the 'thermometer' measuring the logical temperature of all of mathematics."
```

## Explainer

From infinite cardinals, you know that ℵ₀ < ℵ₁ < ℵ₂ < ... is just the beginning of a vast hierarchy of infinite sizes. And from the continuum hypothesis, you know that ZFC leaves the size of ℝ undetermined — neither CH nor ¬CH is provable from ZFC alone. Large cardinal axioms push this logic further: they assert the existence of cardinals so structurally rich that ZFC itself cannot prove they exist. The reason is profound — each large cardinal axiom implies Con(ZFC), and by Gödel's second incompleteness theorem, ZFC cannot prove its own consistency. So if κ is an inaccessible cardinal, ZFC + "κ exists" strictly outpowers plain ZFC.

An **inaccessible cardinal** κ satisfies two conditions beyond mere uncountability. First, it is **regular**: κ cannot be expressed as a union of fewer than κ sets each of size less than κ. (Contrast: ℵ_ω = sup{ℵ₀, ℵ₁, ℵ₂, ...} is a union of ω sets each smaller than ℵ_ω, so it's singular.) Second, it is a **strong limit**: for every λ < κ, the power set 2^λ is still less than κ — exponentiation cannot "jump over" κ. Together these conditions make κ a natural ceiling: the cumulative hierarchy V_κ satisfies every ZFC axiom, so κ's existence gives you a model of ZFC inside your universe.

**Mahlo cardinals** strengthen inaccessibility by requiring that inaccessible cardinals are *dense* below κ in a precise sense: the set of inaccessible cardinals less than κ is **stationary** (it intersects every club — closed unbounded — subset of κ). This is a richness condition on the structure of cardinals below κ, not just on κ itself. A Mahlo cardinal is inaccessible, but an inaccessible need not be Mahlo: the first inaccessible is not Mahlo, but Mahlo cardinals, if they exist, sit strictly above the first inaccessible in the consistency strength ordering.

**Measurable cardinals** introduce a genuinely new idea: a measurable cardinal κ carries a **κ-complete non-principal ultrafilter** U on κ. Informally, U is a consistent "voting system" where every large subset of κ wins. The completeness condition says that intersecting fewer than κ winning sets still gives a winning set. This ultrafilter lets you build an ultrapower of the set-theoretic universe, producing an **elementary embedding** j: V → M where M is an inner model and j(κ) > κ. The existence of such an embedding is extremely powerful — it implies, for instance, that every projective set of reals is Lebesgue measurable and has the Baire property, settling questions completely independent of ZFC alone.

These three levels — inaccessible, Mahlo, measurable — are just the beginning of a hierarchy that extends through Woodin cardinals, supercompact cardinals, and beyond. What unifies them is the concept of **consistency strength**: each level implies the consistency of all levels below it, so they form a well-ordered calibration scale. When mathematicians prove a theorem from ZFC + a large cardinal axiom, they are measuring how much logical strength the theorem requires. This gives large cardinals a central role not just in set theory, but as a measuring instrument for the rest of mathematics.

