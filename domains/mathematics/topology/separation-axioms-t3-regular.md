---
id: separation-axioms-t3-regular
title: Regularity (T₃) and Normal Spaces (T₄)
domain: mathematics
course: topology
prerequisites:
- id: hausdorff-spaces
  type: hard
builds-toward:
- urysohn-lemma
- tietze-extension-theorem
tags:
- regularity
- t3
- normal
- t4
- separation
stage: advanced
status: validated
---

# Regularity (T₃) and Normal Spaces (T₄)

## Core Idea
Regular spaces (T₃) allow separation of points from disjoint closed sets by open neighborhoods, while normal spaces (T₄) extend this to separating disjoint closed sets. These axioms enable the existence of continuous functions with prescribed values on closed sets (Tietze extension) and provide flexibility in constructing continuous real-valued functions (Urysohn's lemma).

## Questions

```yaml
- question: "What is the key structural difference between a T₂ (Hausdorff) space and a T₃ (regular) space?"
  type: multiple-choice
  options:
    - "T₂ requires separating any two disjoint closed sets; T₃ requires separating any two points"
    - "T₂ separates two distinct points by disjoint open sets; T₃ separates a point from a disjoint closed set by disjoint open sets"
    - "T₃ is weaker than T₂ — it imposes fewer separation requirements"
    - "T₂ and T₃ are equivalent; the different labels are historical artifacts"
  answer: 1
  explanation: "In T₂ (Hausdorff), you separate two points: given x ≠ y, find disjoint open U ∋ x and V ∋ y. In T₃ (regular, plus T₁), you separate a point from a closed set: given a point x and a closed set C not containing x, find disjoint open U ∋ x and V ⊇ C. T₃ strictly implies T₂ — separating a point from a (possibly large) closed set is harder than separating two individual points. Option C has the implication direction backward. Option D is false — there exist T₂ spaces that are not T₃."

- question: "Urysohn's lemma states that in a normal (T₄) space, given disjoint closed sets A and B, there exists a continuous function f: X → [0,1] with f(A) = 0 and f(B) = 1. What is most remarkable about this construction?"
  type: multiple-choice
  options:
    - "It uses the metric to measure distances between A and B, making it specific to metric spaces"
    - "It constructs a continuous function from purely topological data — normality alone, with no metric or explicit formula"
    - "It proves that A and B are homeomorphic when they are disjoint closed sets"
    - "It shows that every normal space is compact"
  answer: 1
  explanation: "Urysohn's lemma is remarkable because it produces a continuous function purely from topological hypotheses — no metric, no formula, no coordinates. The proof iteratively finds open sets U_r for each dyadic rational r ∈ [0,1] using normality at every inductive step. The function f(x) = inf{r : x ∈ U_r} turns out to be continuous as a consequence of the nesting relationships. This shows that T₄ is the exact threshold where separation axioms become strong enough to guarantee continuous real-valued functions — a purely topological analogue of metric-space constructions."

- question: "Every metric space is normal (T₄)."
  type: true-false
  answer: true
  explanation: "Given disjoint closed sets A and B in a metric space, define U = {x : d(x,A) < d(x,B)} and V = {x : d(x,B) < d(x,A)}. These sets are open, disjoint, and contain A and B respectively. So every metric space is normal. This is why T₄ feels like the natural baseline for classical analysis — all spaces that arise in analysis and geometry are metric spaces and hence automatically normal."

- question: "A regular (T₃) space is also normal (T₄), since both axioms concern separation of closed sets by open sets."
  type: true-false
  answer: false
  explanation: "Regularity and normality are genuinely distinct: T₃ does not imply T₄. A classical example is the Sorgenfrey plane (ℝ with the lower limit topology, squared), which is regular but not normal. The difference is significant: T₃ separates a single point from a closed set; T₄ must separate two arbitrary disjoint closed sets. Separating two large closed sets from each other is a strictly harder requirement. The hierarchy T₁ ⊂ T₂ ⊂ T₃ ⊂ T₄ is strict at every step."

- question: "Why is normality (T₄) the threshold that enables continuous functions to be constructed from purely topological data, as Urysohn's lemma demonstrates?"
  type: short-answer
  answer: "Urysohn's proof constructs a function by induction: at each step, given two disjoint closed sets (the 'level sets' of the function-to-be), normality guarantees the existence of an open set separating them. Without normality, this inductive step fails — there is no guarantee that two disjoint closed sets can be separated by open sets at all. The function f(x) = inf{r : x ∈ U_r} is built from a nested family of open sets U_r; continuity follows from nesting relationships that normality makes possible at each step. T₃ is not sufficient because it only separates points from closed sets, not two closed sets from each other."
  explanation: "The hierarchy of separation axioms marks exactly which topological constructions become available at each level. T₄ is the precise threshold because both Urysohn's lemma and Tietze extension use the separation of two disjoint closed sets at the core of their proofs."
```

## Explainer

From your study of Hausdorff spaces (T₂), you know that a space satisfies the T₂ axiom if any two distinct points can be separated by disjoint open sets: given x ≠ y, find open U ∋ x and V ∋ y with U ∩ V = ∅. **Regularity** (T₃) strengthens this: instead of separating two points, you separate a point from a closed set. A space is **regular** if for every point x and every closed set C not containing x, there exist disjoint open sets U and V with x ∈ U and C ⊆ V. A **T₃ space** is both regular and T₁ (singletons are closed). The hierarchy so far: T₃ implies T₂ implies T₁. Regularity is strictly stronger because you are now matching an entire closed set with a single open set V, which demands more of the topology than separating two individual points.

**Normality** (T₄) pushes one step further: X is normal if any two disjoint closed sets A and B can be separated by disjoint open sets. A **T₄ space** is both normal and T₁. Every metric space is normal: given disjoint closed sets A and B, the open sets U = {x : d(x,A) < d(x,B)} and V = {x : d(x,B) < d(x,A)} are disjoint and cover A and B respectively (the triangle inequality ensures they work). So all the spaces of classical analysis are normal, which is why T₄ feels like the natural baseline for many theorems.

The payoff for T₄ is the pair of theorems it enables. **Urysohn's lemma** states: in a normal space, given disjoint closed sets A and B, there exists a continuous function f: X → [0,1] with f(A) = 0 and f(B) = 1. This is remarkable — it constructs a continuous function from purely topological data, with no metric or formula. The proof builds f by inductively finding open sets U_r for every dyadic rational r ∈ [0,1], arranged so that A ⊆ U_0 and X \ B ⊇ U_1 and U_r ⊆ closure(U_s) whenever r < s. Normality is invoked at every inductive step to find each new separating open set. The function f(x) = inf{r : x ∈ U_r} then turns out to be continuous.

The **Tietze extension theorem** follows from Urysohn and completes the picture: in a normal space, every continuous real-valued function defined on a closed subspace extends to a continuous function on the whole space. Together, Urysohn and Tietze show that T₄ is the threshold where topology becomes rich enough to guarantee the existence of continuous functions with prescribed behavior on closed sets. This matters practically: when you work in abstract settings like manifolds or function spaces, verifying normality (or the related condition of complete regularity, T₃.₅) is often the first step that legitimizes the use of partition-of-unity arguments, bump functions, and other tools that make analysis flexible.
