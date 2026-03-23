---
id: sheaves-and-sheafification
title: Sheaves and Sheafification
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: presheaves
  type: hard
- id: limits-and-colimits
  type: soft
- id: adjoint-functors
  type: soft
builds-toward:
- topos-theory-intro
tags:
- sheaf
- sheafification
- gluing condition
- Grothendieck topology
- descent
- local-to-global
stage: expert
status: validated
---
# Sheaves and Sheafification

## Core Idea
A sheaf on a topological space X is a presheaf F: Open(X)^op → Set satisfying the gluing condition: whenever an open set U is covered by opens {U_i}, compatible local sections (elements of F(U_i) that agree on overlaps) glue uniquely to a global section in F(U). This local-to-global principle is what distinguishes sheaves from mere presheaves. The sheafification functor L: PSh(X) → Sh(X) is left adjoint to the inclusion Sh(X) → PSh(X), universally enforcing the gluing condition. The concept generalizes to Grothendieck topologies on arbitrary categories, providing the foundation for algebraic geometry and topos theory.

## How It's Best Learned
Start with a concrete topological space like the real line. Compare the presheaf of bounded functions (not a sheaf, since a globally unbounded function can be locally bounded on each compact subset) with the sheaf of continuous functions (gluing works). Verify the sheaf axiom explicitly for an open cover. Then apply sheafification to the bounded-functions presheaf and understand what it produces.

## Common Misconceptions
- The gluing condition has two parts: existence (compatible sections glue) and uniqueness (the glued section is unique); a presheaf satisfying only existence is called a separated presheaf.
- Sheafification does not change the sheaf on its stalks in a drastic way; it is the closest sheaf to the original presheaf in a precise adjoint sense.
- Sheaves on a topological space are a special case of sheaves on a site (category with Grothendieck topology); the topological intuition does not always transfer directly to the general setting.

## Questions

```yaml
- question: "The presheaf of bounded continuous functions on ℝ fails to be a sheaf. What specifically causes this failure?"
  type: multiple-choice
  options:
    - "Bounded functions don't have well-defined restriction maps to open subsets"
    - "Compatible local sections (locally bounded functions that agree on overlaps) fail to glue to a global section, because the globally assembled function may be unbounded"
    - "The stalks of the bounded-functions presheaf are trivial, making any gluing impossible"
    - "The restriction maps fail to compose correctly, violating the presheaf axioms"
  answer: 1
  explanation: "The restriction maps are perfectly well-defined (A is wrong). The gluing failure is more subtle: cover ℝ by intervals U_n = (−n−1, n+1). On each U_n, the function f(x) = x is bounded (bounded by n+1), so it's a valid section. These local sections are compatible — they agree on overlaps since they're all the same function. But f(x) = x is globally unbounded and therefore NOT a section of the bounded-functions presheaf on all of ℝ. The compatible local sections exist but cannot be assembled into a global section — the existence part of the gluing condition fails."

- question: "Sheafification takes a presheaf F and produces a sheaf LF. Which statement best characterizes what sheafification changes and preserves?"
  type: multiple-choice
  options:
    - "Sheafification changes the stalks of F, adding new local data to repair gluing failures"
    - "Sheafification preserves the stalks of F but enforces the gluing condition, so LF has the same local data but assembles correctly globally"
    - "Sheafification is only defined for presheaves on topological spaces, not for abstract Grothendieck sites"
    - "Sheafification eliminates all local sections that fail to extend to global sections"
  answer: 1
  explanation: "A key property of sheafification is stalk-preservation: the stalk (LF)_x equals F_x for every point x. Sheafification does not change local data — it only fixes how local data assembles into global sections. The two-step construction (separate to enforce uniqueness, then glue to enforce existence) adds the globally correct sections required by the gluing axiom. Option A is wrong (stalks are preserved). Option C is wrong (sheafification generalizes to Grothendieck sites). Option D is not the mechanism — sheafification adds missing global sections, it doesn't subtract local ones."

- question: "The gluing condition for a sheaf requires two things: compatible local sections must glue to a global section (existence), and that global section must be unique (uniqueness). A presheaf satisfying only the existence part is called a separated presheaf."
  type: true-false
  answer: false
  explanation: "The definition is reversed. A separated presheaf satisfies the uniqueness part — if a global section exists and restricts to the same local data, it is unique — but does not guarantee existence of a global section. Separated presheaves have the property that sections are determined by their stalks locally, but compatible local data may fail to assemble. A full sheaf satisfies both uniqueness and existence. 'Satisfying only existence' is not the standard name for an intermediate notion between presheaf and sheaf."

- question: "The sheafification functor L: PSh(X) → Sh(X) is the left adjoint to the inclusion Sh(X) → PSh(X), meaning maps from a presheaf F to any sheaf G correspond bijectively to maps from LF to G."
  type: true-false
  answer: true
  explanation: "This is the precise categorical formulation of what sheafification does. The adjunction Hom(LF, G) ≅ Hom(F, iG) (where i is the forgetful inclusion) means sheafification is the universal way to map out of a presheaf into any sheaf. Instead of mapping directly from F, you can always factor through LF. This universal property defines LF up to isomorphism: it is the initial sheaf receiving a map from F. Recognizing this adjunction connects sheafification to other universal constructions in algebra — free objects, completions, and left adjoints generally."

- question: "Explain the gluing condition in your own words, and why both the existence AND uniqueness parts are necessary for sheaves to capture the idea of 'local data assembling consistently to global data.'"
  type: short-answer
  answer: "The gluing condition says: given compatible local sections (sections on each open in a cover that agree on all pairwise overlaps), there exists a unique global section that restricts to each local one. Existence ensures that locally consistent data can always be assembled — you are never stuck with compatible pieces that refuse to combine. Uniqueness ensures the assembly is unambiguous — there is only one global section compatible with the local data, so global sections are completely determined by their local behavior."
  explanation: "Both parts do real logical work. Without existence, you could have locally consistent data with no global interpretation — the sheaf would fail to capture global structure from local data. Without uniqueness, two different global sections could have identical local restrictions, meaning global sections carry extra 'hidden' information not detectable locally — the local-to-global principle breaks down. Separated presheaves have uniqueness without existence; they can track local consistency but cannot always assemble it. Full sheaves require both, making sections completely determined by and assembleable from their local data."
```

## Explainer

From your study of presheaves, you know that a presheaf on a topological space X assigns data (a set, group, ring, etc.) to each open set, and provides restriction maps that make the data on larger open sets compatible with the data on smaller ones. A presheaf is purely local in its construction — it says nothing about how local data can be assembled. A **sheaf** adds exactly one additional requirement: the assembly must work correctly. The **gluing condition** is precise: if you have an open cover {U_i} of U, and you have compatible sections s_i ∈ F(U_i) (meaning s_i and s_j agree on U_i ∩ U_j for every pair), then there exists a *unique* global section s ∈ F(U) that restricts to each s_i. Uniqueness here is as essential as existence — without it, the "assembly" would be ambiguous.

A concrete example clarifies why some presheaves fail this condition. The presheaf of **bounded continuous functions** on ℝ assigns to each open set U the set of continuous functions f: U → ℝ with |f| ≤ M for some M depending on U. This is not a sheaf: cover ℝ by the open sets U_n = (−n−1, n+1). The function f(x) = x is continuous and bounded on each U_n (bounded by n+1 on U_n), so it restricts to a section on each piece. These sections are compatible — they all agree on overlaps, since they are all the same function. But f(x) = x is globally unbounded and therefore not a section of the bounded-functions presheaf on all of ℝ. The local sections do not glue to a global one: the gluing condition fails. By contrast, the sheaf of all continuous functions (without a boundedness restriction) satisfies gluing trivially — local continuous functions glue to a global continuous function.

**Sheafification** takes any presheaf F and produces the "closest" sheaf LF, together with a natural transformation F → LF that is universal among maps from F to sheaves. The construction proceeds in two stages: first separate F (enforce uniqueness of gluing by forcing sections to be determined by their stalks), then glue (enforce existence). The stalk of LF at a point x is the same as the stalk of F at x — sheafification does not change local data, only the global assembly. From your study of adjoints, you can recognize the structure: the sheafification functor L: PSh(X) → Sh(X) is left adjoint to the forgetful inclusion Sh(X) → PSh(X). This means L solves a universal problem: maps from F (a presheaf) to G (a sheaf) correspond bijectively to maps from LF to G. Sheafification is the universal way to force the gluing condition.

The concept generalizes far beyond topological spaces. A **Grothendieck topology** on an arbitrary category C specifies which families of morphisms count as "covers," replacing the open-cover idea from topology. A sheaf on this **site** (C with its Grothendieck topology) satisfies a gluing condition phrased in terms of these abstract covers. This is the framework underlying modern algebraic geometry: schemes are built from rings, and the category of rings with a suitable Grothendieck topology (the étale topology, the flat topology, etc.) produces sheaf categories (toposes) rich enough to support cohomological tools. The topos theory you will encounter next is built almost entirely on the sheaf concept generalized to sites.
