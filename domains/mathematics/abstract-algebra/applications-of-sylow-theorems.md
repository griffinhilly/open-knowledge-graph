---
id: applications-of-sylow-theorems
title: Applications of Sylow Theorems
domain: mathematics
course: abstract-algebra
prerequisites:
- id: sylow-theorems
  type: hard
tags:
- sylow
- group-structure
- classification
stage: advanced
status: draft
---

# Applications of Sylow Theorems

## Core Idea
Sylow theorems classify groups of certain orders. Every group of order p² is abelian; groups of order pq are determined by their Sylow structure. These applications show how Sylow theorems reveal group structure for specific orders.

## Explainer

The Sylow theorems — existence, conjugacy, and the congruence constraint on the number of Sylow p-subgroups — are powerful tools for reverse-engineering the structure of a finite group from its order alone. You have already proved the theorems; now the goal is to use them. The core technique in applications is a counting argument: you compute the allowable numbers of Sylow subgroups, then show that some of them must be normal, which forces the group to have a recognizable structure.

The standard recipe is: let |G| = n, write n = p^a · m with gcd(p, m) = 1, and let n_p denote the number of Sylow p-subgroups. The third Sylow theorem gives you that n_p ≡ 1 (mod p) and n_p divides m. These two constraints together often leave very few options. If the only value satisfying both constraints is 1, you have proved that the Sylow p-subgroup is **normal** in G (since all Sylow p-subgroups are conjugate, and a single subgroup is its own conjugate class). A normal Sylow subgroup is a significant structural finding.

Consider groups of order pq where p < q are distinct primes. The number of Sylow q-subgroups satisfies n_q ≡ 1 (mod q) and n_q | p. Since p < q, the only divisor of p that is ≡ 1 (mod q) is 1 itself — so the Sylow q-subgroup is always normal. Meanwhile, n_p | q and n_p ≡ 1 (mod p), giving n_p ∈ {1, q}. If q ≢ 1 (mod p), then n_p = 1 and the Sylow p-subgroup is also normal. In that case, G is the **direct product** of its two Sylow subgroups and is therefore cyclic (isomorphic to Z_pq). If q ≡ 1 (mod p), a non-abelian group of order pq exists, and the Sylow counting tells you exactly how many Sylow p-subgroups it contains.

For groups of order p², both Sylow p-subgroups must account for the entire group (since the group's order is a prime power). Every group of order p² is **abelian** — it is isomorphic to either Z_{p²} or Z_p × Z_p. This follows from the fact that the center of a p-group is non-trivial, and a group G with G/Z(G) cyclic must be abelian. The Sylow approach here blends the structure theorem for p-groups with the explicit constraint on subgroup counts. These two cases — pq and p² — illustrate the template for all Sylow applications: use n_p constraints to force normality, then use normality and direct-product recognition to identify the isomorphism type.
