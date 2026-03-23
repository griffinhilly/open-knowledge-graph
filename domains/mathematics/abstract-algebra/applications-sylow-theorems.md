---
id: applications-sylow-theorems
title: Applications of Sylow Theorems
domain: mathematics
course: abstract-algebra
prerequisites:
- id: sylow-theorems
  type: hard
tags:
- sylow
- structure
- simple-groups
stage: advanced
status: validated
---

# Applications of Sylow Theorems

## Core Idea
Sylow theorems are used to prove groups of specific orders have particular structures or are simple. For example, no simple group of order 12 exists, and every group of order p² is abelian.

## Questions

```yaml
- question: "G is a group of order 30 = 2 × 3 × 5. The number of Sylow 5-subgroups n₅ must satisfy n₅ ≡ 1 (mod 5) and n₅ | 6. What are the possible values of n₅, and what structural consequence follows if n₅ = 6?"
  type: multiple-choice
  options:
    - "n₅ ∈ {1, 6}; if n₅ = 6, each Sylow 5-subgroup contributes 4 non-identity elements, accounting for 24 elements of order 5"
    - "n₅ ∈ {1, 5}; if n₅ = 5, the group must be cyclic"
    - "n₅ ∈ {1, 6}; if n₅ = 6, the Sylow 5-subgroups must all be normal"
    - "n₅ ∈ {1, 2, 3, 6}; all values satisfying divisibility are possible"
  answer: 0
  explanation: "The constraints are: n₅ ≡ 1 (mod 5) gives n₅ ∈ {1, 6, 11, …}, and n₅ | 6 gives n₅ ∈ {1, 2, 3, 6}. The intersection is n₅ ∈ {1, 6}. If n₅ = 6, there are six Sylow 5-subgroups, each of order 5. Since any two such subgroups of prime order intersect trivially, they contribute 6 × 4 = 24 distinct non-identity elements of order 5 — severely constraining what elements remain for other Sylow subgroups. Option C is wrong: multiple Sylow subgroups are conjugate, not normal; only a unique (n_p = 1) Sylow subgroup is normal."

- question: "When applying Sylow theorems to show a group G of order 12 is not simple, what is the key structural observation?"
  type: multiple-choice
  options:
    - "Order 12 groups must be cyclic, and cyclic groups are always simple"
    - "In any case — whether n₃ = 1 or n₂ = 1 — G has a normal Sylow subgroup, so it cannot be simple"
    - "The Sylow 2-subgroup of G is always normal because 2 is the smallest prime dividing 12"
    - "Showing that G has elements of order 3 and order 4 proves it is not simple"
  answer: 1
  explanation: "The argument proceeds by case analysis: n₃ ∈ {1, 4} and n₂ ∈ {1, 3}. If n₃ = 4, the four Sylow 3-subgroups contribute 4 × 2 = 8 non-identity elements of order 3, leaving only 4 elements for Sylow 2-subgroups — forcing n₂ = 1. If n₃ = 1, the Sylow 3-subgroup is itself normal. In both cases, G has at least one normal Sylow subgroup, which is a proper nontrivial normal subgroup — so G cannot be simple. The two cases are exhaustive and both yield normality."

- question: "If n_p = 1 for some prime p dividing |G|, then the unique Sylow p-subgroup is automatically a normal subgroup of G."
  type: true-false
  answer: true
  explanation: "This follows directly from the second Sylow theorem: all Sylow p-subgroups are conjugate. If there is only one Sylow p-subgroup P, then P is conjugate only to itself — meaning gPg⁻¹ = P for all g ∈ G, which is precisely the definition of a normal subgroup. The strategy of proving n_p = 1 in applications of Sylow's theorem is therefore equivalent to finding a normal Sylow subgroup — the object needed to prove non-simplicity."

- question: "The key step when applying Sylow's theorem to prove a group of given order is not simple is verifying that Sylow subgroups of each prime order exist."
  type: true-false
  answer: false
  explanation: "Existence of Sylow subgroups is guaranteed by the first Sylow theorem for any finite group — verifying it proves nothing about simplicity. The substantive step is constraining the *number* n_p of Sylow p-subgroups using the congruence and divisibility conditions, and then showing via element-counting that at least one n_p must equal 1. It is uniqueness (n_p = 1), not mere existence, that forces normality and hence non-simplicity. A common error is to stop after identifying the possible Sylow subgroups rather than proceeding to constrain their count."

- question: "Describe the general strategy for using Sylow theorems to prove that a group of a specific order cannot be simple. What are the key steps?"
  type: short-answer
  answer: "The strategy has four steps: (1) Factor the order |G| = p₁^a₁ · p₂^a₂ · … and identify the Sylow p-subgroups for each prime. (2) For each prime p, apply the Sylow constraints — n_p ≡ 1 (mod p) and n_p | (|G|/p^a) — to enumerate the possible values of n_p. (3) Use element-counting to show that having multiple Sylow subgroups for all primes simultaneously is incompatible with |G|: if each prime had more than one Sylow subgroup, the non-identity elements they contribute would collectively exceed |G|. (4) Conclude that some n_p = 1, giving G a proper nontrivial normal Sylow subgroup and proving G cannot be simple. The meta-skill is targeting the prime with the tightest constraints first and recognizing when case analysis is needed."
  explanation: "The power of the method lies in turning a combinatorial constraint (n_p divides the cofactor and is 1 mod p) into a structural conclusion (normal subgroup) via element counting. Many 'show G is not simple' proofs follow this exact skeleton."
```

## Explainer

The Sylow theorems — which you have already studied — give you three tools: existence of Sylow p-subgroups, their conjugacy, and a congruence constraint on their count n_p. **Applications** means weaponizing these tools to force structural conclusions about groups whose orders factor in particular ways. The general strategy is: compute what n_p *must* be, use the constraints to show it must equal 1, and conclude that the unique Sylow subgroup is normal — giving you a normal subgroup to work with.

Consider a group G of order 12 = 2² × 3. The number of Sylow 3-subgroups satisfies n_3 ≡ 1 (mod 3) and n_3 | 4, so n_3 ∈ {1, 4}. The number of Sylow 2-subgroups satisfies n_2 ≡ 1 (mod 2) and n_2 | 3, so n_2 ∈ {1, 3}. If n_3 = 4, those four subgroups each have order 3 and pairwise trivial intersection, contributing 4 × 2 = 8 non-identity elements of order 3. That forces n_2 = 1 (only 4 elements remain). So in either case — n_3 = 1 or n_2 = 1 — there is a normal Sylow subgroup. No group of order 12 can be **simple** (have no nontrivial normal subgroups), because we always find one.

For groups of order p², the argument is different. Every group of order p² is abelian. The proof uses the fact that the center Z(G) is nontrivial (a standard result from the class equation), so |Z(G)| is p or p². If |Z(G)| = p², then G = Z(G) is abelian. If |Z(G)| = p, then G/Z(G) has order p and is therefore cyclic, but a group G is abelian whenever G/Z(G) is cyclic — a contradiction that forces |Z(G)| = p² after all.

The meta-skill to internalize is **counting with Sylow constraints to force normality**. Many "show this group is not simple" or "classify groups of order n" proofs follow the same skeleton: (1) identify the possible Sylow subgroups by applying the divisibility and congruence constraints, (2) count elements to show the options are incompatible unless one n_p = 1, (3) conclude the group has a proper normal subgroup and therefore cannot be simple, or (4) use the normal subgroup's structure to classify the full group as a direct or semidirect product. Mastery is recognizing which prime p to target first for the tightest constraint.
