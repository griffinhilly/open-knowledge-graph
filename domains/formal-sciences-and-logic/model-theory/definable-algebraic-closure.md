---
id: definable-algebraic-closure
title: Definable Closure and Algebraic Closure
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: definability-and-algebraic-applications
  type: hard
- id: structures-and-formal-languages
  type: soft
builds-toward:
- transcendence-and-independence
- strongly-minimal-and-geometry
tags:
- definable-closure
- algebraic-closure
- closure-operators
stage: expert
status: draft
---

# Definable Closure and Algebraic Closure

## Core Idea
The definable closure dcl(A) consists of elements definable from A with parameters. The algebraic closure acl(A) consists of elements satisfying a formula over A with finitely many solutions. In stable theories, dcl(A) ⊆ acl(A), and when dcl(A) is also algebraically closed it forms a submodel. These closures provide structure theory for models of stable theories.

## Questions

```yaml
- question: "In the real field (ℝ, +, ×, 0, 1) with parameter set A = ℚ, consider the element √2. The formula φ(x) = 'x² = 2' has exactly two solutions: √2 and −√2. Is √2 in dcl(ℚ), in acl(ℚ), or neither?"
  type: multiple-choice
  options:
    - "In dcl(ℚ), because √2 satisfies a polynomial formula over ℚ"
    - "In acl(ℚ) but NOT in dcl(ℚ), because x² = 2 has finitely many solutions but does not uniquely define √2"
    - "In neither, because √2 is irrational and therefore not definable from rational parameters"
    - "In both dcl(ℚ) and acl(ℚ), since algebraic elements over ℚ always satisfy both closure conditions"
  answer: 1
  explanation: "For an element b to be in dcl(A), there must exist a formula φ(x, ā) over A such that b is the UNIQUE solution. The formula x² = 2 has two solutions (√2 and −√2), so it does not uniquely pin down √2 — and no other formula over ℚ uniquely identifies √2 without also using √2 as a parameter. Therefore √2 ∉ dcl(ℚ). However, for acl(A), we only need a formula over A with FINITELY many solutions, and x² = 2 qualifies (two solutions). So √2 ∈ acl(ℚ). This example shows the strict inclusion dcl(A) ⊊ acl(A): algebraically dependent elements that come in pairs or finite groups land in acl but not dcl."

- question: "Which statement correctly distinguishes definable closure from algebraic closure?"
  type: multiple-choice
  options:
    - "dcl(A) contains elements satisfying some formula over A with finitely many solutions; acl(A) requires the formula to have exactly one solution"
    - "dcl(A) requires a formula over A with exactly one solution (unique definability); acl(A) requires a formula over A with finitely many solutions"
    - "dcl(A) and acl(A) are identical in all first-order theories"
    - "acl(A) contains only elements that appear in no formula with parameters from A"
  answer: 1
  explanation: "The definitions are: b ∈ dcl(A) iff there exists a formula φ(x, ā) with ā ∈ A such that φ uniquely defines b (the formula has exactly one solution, namely b). b ∈ acl(A) iff there exists a formula φ(x, ā) with ā ∈ A such that b satisfies φ and φ has only finitely many solutions (but not necessarily one). The inclusion dcl(A) ⊆ acl(A) follows immediately: unique definability is a special case of finite definability. Option A has the definitions reversed. Option C is false — in many theories (including real closed fields), there are elements in acl but not dcl, as the √2 example illustrates."

- question: "The inclusion dcl(A) ⊆ acl(A) holds in every first-order theory, because unique definability is a special case of finite definability."
  type: true-false
  answer: true
  explanation: "If b ∈ dcl(A), there is a formula φ(x, ā) over A with exactly one solution, namely b. But then φ trivially has finitely many solutions (just one), so b ∈ acl(A) by definition. This is not a non-trivial theorem — it follows directly from comparing the two definitions. The content of model theory is in understanding when acl(A) is strictly larger than dcl(A) (as in real closed fields, where algebraic conjugates like √2 and −√2 both belong to acl but neither belongs to dcl over ℚ) and in the structural role these operators play in stability theory and independence."

- question: "If acl(A) = A — meaning A is algebraically closed in the model-theoretic sense — then it also follows that dcl(A) = A."
  type: true-false
  answer: false
  explanation: "acl(A) = A means every element with a finite orbit over A is already in A — no new elements can be added by taking finite definable sets. But this says nothing about dcl(A): it is possible for acl(A) = A while dcl(A) is a proper subset of A. An element b ∈ A might not be uniquely definable from A\\{b} even though it belongs to A. The condition dcl(A) = A (every element of A is uniquely definable from other elements) is independent of acl(A) = A. In stable theories, having both dcl(A) = A and acl(A) = A is what makes A a 'sufficiently closed' set for independence theory, but the two conditions are not equivalent to each other."

- question: "Explain the difference between an element b being in dcl(A) versus acl(A), using the analogy between these model-theoretic closures and classical algebraic dependence in field theory."
  type: short-answer
  answer: "b ∈ dcl(A) means b is uniquely determined by A — there is a formula over A with b as its only solution, analogous to an element being definable by a formula with a unique root. b ∈ acl(A) means b lives in a finite 'orbit' over A — it satisfies a formula over A that has only finitely many solutions (b may be one of several conjugates), analogous to being a root of a polynomial over a base field. In classical field theory, √2 is algebraic over ℚ (satisfies x²−2=0, which has two roots) but is not uniquely defined by ℚ because its conjugate −√2 is equally valid. Model-theoretic acl(ℚ) captures this: √2 ∈ acl(ℚ) because it has a finite orbit {√2, −√2}, but √2 ∉ dcl(ℚ) because no ℚ-formula uniquely identifies it."
  explanation: "This analogy makes the model-theoretic definitions intuitive for students with algebraic background. The key shift is that model theory generalizes these notions to any first-order structure, not just fields. In a general structure, 'being algebraic over A' means living in a finite set definable from A, which captures the essential feature of algebraic elements (bounded degree over the base) without requiring a field structure."
```

## Explainer

From your work on definability, you know that a set S ⊆ M^n is **definable** over a parameter set A if there is a formula φ(x̄, ā) with ā ∈ A such that S = {x̄ : M ⊨ φ(x̄, ā)}. Now consider what elements are "pinned down" by parameters in A. The **definable closure** dcl(A) consists of all elements b such that the singleton {b} is A-definable — that is, φ(x, ā) has exactly one solution, namely b. Think of it as the set of elements you can uniquely name using formulas with parameters from A.

The **algebraic closure** acl(A) relaxes unique definability: b ∈ acl(A) if there exists some formula φ(x, ā) with ā ∈ A such that b satisfies φ and φ has only *finitely many* solutions. The element isn't necessarily uniquely pinned down, but it lives in a finite "orbit" over A. Notice the analogy with field theory: in the field ℝ considered as a structure, √2 is algebraic over ℚ because it satisfies x² − 2 = 0, which has exactly two solutions. Indeed, in algebraically closed fields, model-theoretic acl agrees with the classical algebraic closure from field theory.

The inclusion dcl(A) ⊆ acl(A) is immediate from the definitions: if b is the unique element satisfying φ(x, ā), then φ has finitely many (specifically, one) solution, so b ∈ acl(A). Both operations are **closure operators**: A ⊆ dcl(A), dcl(dcl(A)) = dcl(A), and similarly for acl. In stable theories, these closures behave especially well — acl(A) is always a model-theoretically small structure carrying the "algebraic content" of A, and independence (non-forking) is intimately tied to the acl operator.

The structural importance of these closures comes into focus when building models. A set A is **algebraically closed** (in the model-theoretic sense) if acl(A) = A — every element finitely definable from A is already in A. Algebraically closed sets serve as the "good" parameter sets for independence theory, analogous to how algebraically closed fields are the "good" fields in algebraic geometry. When A = dcl(A), A forms a closed substructure that reflects the ambient theory; combining both conditions gives the structural building blocks for understanding models of stable theories.
