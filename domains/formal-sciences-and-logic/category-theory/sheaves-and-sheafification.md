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
