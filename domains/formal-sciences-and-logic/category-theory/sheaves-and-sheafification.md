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
stage: advanced
status: draft
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

## Explainer

From your study of presheaves, you know that a presheaf on a topological space X assigns data (a set, group, ring, etc.) to each open set, and provides restriction maps that make the data on larger open sets compatible with the data on smaller ones. A presheaf is purely local in its construction — it says nothing about how local data can be assembled. A **sheaf** adds exactly one additional requirement: the assembly must work correctly. The **gluing condition** is precise: if you have an open cover {U_i} of U, and you have compatible sections s_i ∈ F(U_i) (meaning s_i and s_j agree on U_i ∩ U_j for every pair), then there exists a *unique* global section s ∈ F(U) that restricts to each s_i. Uniqueness here is as essential as existence — without it, the "assembly" would be ambiguous.

A concrete example clarifies why some presheaves fail this condition. The presheaf of **bounded continuous functions** on ℝ assigns to each open set U the set of continuous functions f: U → ℝ with |f| ≤ M for some M depending on U. This is not a sheaf: cover ℝ by the open sets U_n = (−n−1, n+1). The function f(x) = x is continuous and bounded on each U_n (bounded by n+1 on U_n), so it restricts to a section on each piece. These sections are compatible — they all agree on overlaps, since they are all the same function. But f(x) = x is globally unbounded and therefore not a section of the bounded-functions presheaf on all of ℝ. The local sections do not glue to a global one: the gluing condition fails. By contrast, the sheaf of all continuous functions (without a boundedness restriction) satisfies gluing trivially — local continuous functions glue to a global continuous function.

**Sheafification** takes any presheaf F and produces the "closest" sheaf LF, together with a natural transformation F → LF that is universal among maps from F to sheaves. The construction proceeds in two stages: first separate F (enforce uniqueness of gluing by forcing sections to be determined by their stalks), then glue (enforce existence). The stalk of LF at a point x is the same as the stalk of F at x — sheafification does not change local data, only the global assembly. From your study of adjoints, you can recognize the structure: the sheafification functor L: PSh(X) → Sh(X) is left adjoint to the forgetful inclusion Sh(X) → PSh(X). This means L solves a universal problem: maps from F (a presheaf) to G (a sheaf) correspond bijectively to maps from LF to G. Sheafification is the universal way to force the gluing condition.

The concept generalizes far beyond topological spaces. A **Grothendieck topology** on an arbitrary category C specifies which families of morphisms count as "covers," replacing the open-cover idea from topology. A sheaf on this **site** (C with its Grothendieck topology) satisfies a gluing condition phrased in terms of these abstract covers. This is the framework underlying modern algebraic geometry: schemes are built from rings, and the category of rings with a suitable Grothendieck topology (the étale topology, the flat topology, etc.) produces sheaf categories (toposes) rich enough to support cohomological tools. The topos theory you will encounter next is built almost entirely on the sheaf concept generalized to sites.
