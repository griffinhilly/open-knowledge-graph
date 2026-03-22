---
id: normal-spaces
title: Normal Spaces (T4 Spaces)
domain: mathematics
course: topology
prerequisites:
- id: separation-axioms
  type: hard
builds-toward:
- urysohns-lemma
- tietze-extension-theorem
tags:
- normal
- t4
stage: formal-systems
status: draft
---

# Normal Spaces (T4 Spaces)

## Core Idea
A space is normal if disjoint closed sets F, G have disjoint open neighborhoods. Every compact Hausdorff space and every metric space is normal.

## Questions

```yaml
- question: "A topological space X is T₃ (regular) but you want to verify whether it is also T₄ (normal). Which of the following would be sufficient to show X is NOT normal?"
  type: multiple-choice
  options:
    - "Finding a point p and a closed set C not containing p that cannot be separated by disjoint open sets"
    - "Finding two disjoint closed sets F and G in X that cannot be separated by disjoint open sets"
    - "Finding two distinct points in X that cannot be separated by disjoint open sets"
    - "Finding a closed set in X that is not also open"
  answer: 1
  explanation: "Normality requires that every pair of disjoint closed sets can be separated by disjoint open neighborhoods. To show a space fails to be normal, you need to exhibit two disjoint closed sets with no such separating neighborhoods. Option A describes failure of T₃ (regularity), which separates a point from a closed set — that condition is already assumed to hold. Option C describes failure of T₂ (Hausdorff). Understanding the hierarchy is essential: each axiom makes a stronger demand than the previous one."

- question: "Which of the following spaces is guaranteed to be normal (T₄)?"
  type: multiple-choice
  options:
    - "Every Hausdorff (T₂) space, by the separation axiom hierarchy"
    - "Every regular (T₃) space, since normality is just a slight strengthening of regularity"
    - "Every metric space and every compact Hausdorff space, but not necessarily every regular space"
    - "Every second-countable space, since countability conditions imply normality"
  answer: 2
  explanation: "The two major classes guaranteed to be normal are metric spaces and compact Hausdorff spaces. For metric spaces, the proof is constructive using the distance function. For compact Hausdorff spaces, compactness and Hausdorff-ness together force normality. Regular spaces are NOT automatically normal — there exist T₃ spaces that fail T₄, such as certain infinite products. The hierarchy T₁ ⊂ T₂ ⊂ T₃ does not automatically continue to T₄ without additional hypotheses."

- question: "Every Hausdorff (T₂) topological space is automatically normal (T₄)."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about the separation axiom hierarchy. The T₁ ⊂ T₂ ⊂ T₃ ⊂ T₄ containments do NOT hold in general without extra conditions. There exist Hausdorff spaces that are not regular, and regular spaces that are not normal. A famous example of a non-normal Hausdorff space is the Niemytzki (Moore) plane. Normality requires substantially more structure than Hausdorff-ness — the condition that arbitrary disjoint closed sets (not just points) can be separated is genuinely harder to satisfy."

- question: "Urysohn's Lemma requires normality because it needs to construct a continuous function that separates two disjoint closed sets by mapping one to 0 and the other to 1."
  type: true-false
  answer: true
  explanation: "Urysohn's Lemma states: in a normal space, any two disjoint closed sets F and G admit a continuous function f: X → [0,1] with f(F) = 0 and f(G) = 1. Normality is exactly the right hypothesis — the proof constructs a dense family of intermediate open sets using iterated applications of the normality condition. In a space that fails normality (some disjoint closed sets have no separating open neighborhoods), this construction breaks down and no such continuous function can be guaranteed to exist. Normality is both necessary and sufficient for Urysohn's Lemma."

- question: "Why is normality the 'right' condition for Urysohn's Lemma — what does normality provide that regularity (T₃) alone does not?"
  type: short-answer
  answer: "Regularity only separates a single point from a closed set by open sets. Normality separates any two disjoint closed sets — including large, complicated ones — by open neighborhoods. Urysohn's Lemma's proof works by iterating the normality condition: given F and G, you first find an open set U_{1/2} with F ⊂ U_{1/2} ⊂ Ū_{1/2} ⊂ X∖G, then apply normality again to find U_{1/4} and U_{3/4}, and so on for all dyadic rationals. This requires separating closed sets at every step, not just separating a point. With only T₃, you cannot run this construction for arbitrary closed sets F."
  explanation: "This connection — normality → Urysohn's Lemma → Tietze Extension — is the reason normal spaces are a central object in topology. The upgrade from 'separated by open sets' to 'separated by a continuous function' is enormous: it means the topological space is rich enough to support real analysis on it. This is why metric spaces and compact Hausdorff spaces, being normal, admit continuous function theory, while more exotic spaces may not."
```

## Explainer

You've studied the **separation axioms** — a hierarchy of conditions that capture how well a topological space can separate points and sets using open sets. Recall the key levels: T₁ (points are closed), T₂ or Hausdorff (disjoint points have disjoint open neighborhoods), and T₃ or regular (a point and a disjoint closed set have disjoint open neighborhoods). **Normal spaces** (T₄) push this one step further: *two disjoint closed sets* can always be separated by disjoint open neighborhoods.

To feel why this is a meaningful strengthening, compare T₃ and T₄. In a regular space, you can separate a *point* from a closed set it doesn't belong to. But a single point is a very special kind of closed set. Normality demands the same separation for *arbitrary* disjoint closed sets — even large, complicated ones. In some pathological spaces (certain infinite products, the long line), disjoint closed sets cannot always be separated this way, showing that normality is a genuine restriction.

The two major classes of normal spaces are metric spaces and compact Hausdorff spaces. For metric spaces, the proof is constructive: given disjoint closed sets F and G in a metric space, let U = {x : d(x,F) < d(x,G)} and V = {x : d(x,G) < d(x,F)}. These are open (they're defined by strict inequalities of continuous functions), disjoint, and contain F and G respectively. The metric provides enough structure to build the separating neighborhoods explicitly. For compact Hausdorff spaces, the argument is topological: compactness lets you build finite open covers, and Hausdorff-ness provides local separability that can be pieced together globally.

Why does normality matter? It is the exact condition needed for **Urysohn's Lemma**, which you'll study next: in a normal space, any two disjoint closed sets can be separated not just by open sets, but by a *continuous real-valued function* — one that equals 0 on one closed set and 1 on the other. This is a striking upgrade from separation by open sets alone, and it's the key to constructing continuous functions in topology. Urysohn's Lemma is then the engine behind the **Tietze Extension Theorem**, which says that every continuous real-valued function defined on a closed subset of a normal space extends to the whole space. Together, these results make normality the foundation of the theory of continuous functions on topological spaces.
