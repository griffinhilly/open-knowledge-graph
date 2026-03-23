---
id: los-theorem-and-preservation
title: Łoś's Theorem and Preservation in Ultraproducts
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: ultraproducts-of-structures
  type: hard
builds-toward:
- categorical-theories-and-uniqueness
tags:
- Łoś's theorem
- preservation
- first-order preservation
- fundamental theorem
stage: expert
status: validated
---

# Łoś's Theorem and Preservation in Ultraproducts

## Core Idea
Łoś's Theorem states: a formula φ is satisfied in the ultraproduct ∏ᵤ Mᵢ iff it is satisfied in the component structures on a U-large set. This profound statement implies first-order logic is preserved 'generically' under ultraproducts. Łoś's Theorem is the key tool justifying ultraproduct utility and underlies many deep results in model theory.

## Questions

```yaml
- question: "Łoś's theorem states that a first-order sentence φ holds in the ultraproduct ∏_U Mᵢ if and only if {i : Mᵢ ⊨ φ} ∈ U. Why is this a profound result?"
  type: multiple-choice
  options:
    - "It shows that first-order truth in the ultraproduct is completely determined by the first-order truths of the components: the ultraproduct is precisely the structure where what holds 'almost everywhere' (in the ultrafilter sense) is true"
    - "It proves that any two structures satisfying the same first-order theory must be isomorphic to each other"
    - "It shows that ultraproducts always satisfy strictly more first-order sentences than any single component structure"
    - "It establishes that every consistent first-order theory has a model, giving a purely semantic completeness theorem"
  answer: 0
  explanation: "Łoś's theorem makes the notion of 'almost everywhere' in the ultrafilter sense perfectly compatible with first-order logic. The ultrafilter captures what 'generically' holds in the family of structures, and Łoś's theorem shows this aligns exactly with first-order satisfaction in the ultraproduct. This is what makes ultraproducts a tool for transferring first-order properties: if you want the ultraproduct to satisfy a sentence, ensure it holds in a U-large set of components. The theorem does not say the ultraproduct has more sentences than components (option C) — it could have fewer if some sentence holds in only finitely many components."

- question: "A logician takes an ultrapower ∏_U ℝ by forming a product of countably many copies of ℝ modulo a non-principal ultrafilter U. What does Łoś's theorem guarantee about this structure?"
  type: multiple-choice
  options:
    - "Every first-order sentence true in ℝ is also true in ∏_U ℝ, because each such sentence holds in all (hence in a U-large set of) component copies"
    - "The ultrapower ∏_U ℝ is isomorphic to ℝ itself, since all component structures are identical"
    - "The ultrapower satisfies only universal first-order sentences from ℝ, but not existential ones"
    - "Łoś's theorem applies only to ultraproducts of distinct structures, not ultrapowers where all components are the same"
  answer: 0
  explanation: "In an ultrapower, every component Mᵢ = ℝ, so for any first-order sentence φ, the set {i : Mᵢ ⊨ φ} is either all of ℕ (if φ is true in ℝ) or empty (if false). Since any ultrafilter contains the full index set, every sentence true in ℝ holds in a U-large set of components, and by Łoś's theorem it holds in the ultrapower. The ultrapower is therefore elementarily equivalent to ℝ — it satisfies exactly the same first-order sentences. But it is not isomorphic to ℝ: it contains additional elements (infinitesimals and infinite numbers) not present in ℝ, demonstrating that elementary equivalence is weaker than isomorphism."

- question: "Łoś's theorem applies to all first-order formulas including those with quantifiers, because the ultrafilter's properties — closure under supersets and finite intersections — mesh exactly with the Boolean and quantifier connectives."
  type: true-false
  answer: true
  explanation: "The proof of Łoś's theorem goes by induction on formula complexity. The atomic and Boolean cases are straightforward from the definition of the ultraproduct. The critical quantifier case: ∃x ψ holds in ∏_U Mᵢ iff there is an element (aᵢ) such that ψ(aᵢ) holds in Mᵢ for U-many i — iff U-many Mᵢ satisfy ∃x ψ. The ultrafilter's closure under intersections handles conjunctions (∧), closure under supersets handles disjunctions (∨), and the complement property handles negations (¬). These algebraic properties of the ultrafilter are precisely what is needed for the quantifier and Boolean cases to go through, making the theorem both elegant and structurally inevitable."

- question: "By Łoś's theorem, if a first-order sentence φ holds in the ultraproduct ∏_U Mᵢ, then φ must hold in every component structure Mᵢ."
  type: true-false
  answer: false
  explanation: "Łoś's theorem requires only that φ holds in a U-large set of indices — a set belonging to the ultrafilter U — not in every index. An ultrafilter on an infinite index set can contain sets that exclude finitely many (or even infinitely many) indices. For example, if Mᵢ ⊨ φ for all i ≥ 5 and M₁, M₂, M₃, M₄ ⊭ φ, and U is a non-principal ultrafilter containing all co-finite sets, then {i : Mᵢ ⊨ φ} ∈ U (it is co-finite), so φ holds in ∏_U Mᵢ despite failing in four component structures. This is the whole power of the ultrafilter: it 'ignores' what happens on small sets."

- question: "Explain how Łoś's theorem enables a semantic proof of the compactness theorem for first-order logic. What role does the ultrafilter play?"
  type: short-answer
  answer: "Compactness states: if every finite subset of a theory T has a model, then T has a model. To prove this using Łoś's theorem: index the finite subsets of T by I = {finite S ⊆ T}. For each finite S, let Mₛ be a model of S (which exists by hypothesis). Take an ultrafilter U on I containing all sets of the form {S : φ ∈ S} for each φ ∈ T — these sets are closed under finite intersection (since {S : φ ∈ S} ∩ {S : ψ ∈ S} = {S : φ,ψ ∈ S}), so they generate a filter that can be extended to an ultrafilter. For each φ ∈ T, Mₛ ⊨ φ whenever φ ∈ S, and {S : φ ∈ S} ∈ U by construction, so by Łoś's theorem ∏_U Mₛ ⊨ φ. Since this holds for every φ ∈ T, the ultraproduct is a model of all of T."
  explanation: "The ultrafilter plays two roles: it defines which sets count as 'large' (generating the notion of 'almost all'), and it witnesses that each sentence holds in sufficiently many components to transfer to the ultraproduct. The compactness proof via ultraproducts is often considered more illuminating than the syntactic Henkin construction, because it shows concretely what the model looks like — it is built from the individual finite models, stitched together by the ultrafilter."
```

## Explainer

Recall that an **ultraproduct** ∏_U Mᵢ is built from a family of structures {Mᵢ : i ∈ I} and an ultrafilter U on the index set I. Its elements are equivalence classes of sequences (aᵢ), where two sequences are identified if they agree on a U-large set of indices (a set in the ultrafilter). The ultrafilter captures the notion of "almost all" indices: a property holds almost everywhere if the set of indices where it holds is in U. Łoś's theorem makes this precise for first-order logic.

**Łoś's Theorem** states that a first-order sentence φ is true in ∏_U Mᵢ if and only if {i ∈ I : Mᵢ ⊨ φ} ∈ U — that is, φ holds in the ultraproduct iff it holds in almost all component structures. The proof is by induction on the complexity of φ. The atomic and Boolean cases follow from how the ultraproduct is defined. The crucial step is the quantifier case: ∃x ψ holds in the ultraproduct iff there is an element (aᵢ) such that ψ holds of it almost everywhere, which holds iff almost all Mᵢ satisfy ∃x ψ. The ultrafilter's closure under supersets and intersections ensures that the logic of "almost all" meshes perfectly with the logic of ∧ and ∨.

The most immediate consequence is the **compactness theorem** of first-order logic via ultraproducts. Suppose every finite subset of a theory T has a model. Build a family of models Mᵢ for each finite subset Tᵢ, index by the finite subsets of T, and take an ultrafilter containing all co-finite sets (which exists by the ultrafilter lemma). Łoś's theorem then shows the ultraproduct satisfies every sentence in T, because each sentence φ belongs to almost all Tᵢ. This is a beautiful semantic proof of compactness that avoids the syntactic machinery of Henkin constructions.

Łoś's theorem also governs which properties are *preserved* under ultraproducts. Since ultraproducts preserve all first-order sentences (by the theorem), they are a tool for transferring properties between structures when you know the property is first-order. **Non-standard analysis** exploits this directly: take an ultrapower ∏_U ℝ of the real numbers; by Łoś's theorem, every first-order statement true of ℝ is true of ∗ℝ (the hyperreals), including all of real analysis. The extra elements in ∗ℝ (infinitesimals and infinite numbers) don't violate any first-order property of ℝ — they only differ in higher-order or set-theoretic respects. Łoś's theorem is thus the engine that makes non-standard analysis logically sound.
