---
id: combinations-selections-discrete
title: Combinations and Selections
domain: mathematics
course: discrete-math
prerequisites:
- id: permutations-arrangements-discrete
  type: hard
- id: combinations
  type: hard
builds-toward:
- binomial-theorem-discrete
- inclusion-exclusion-advanced
tags:
- combinations
- selections
- C(n,r)
- unordered
stage: formal-systems
status: draft
---

# Combinations and Selections

## Core Idea
A combination is an unordered selection of objects. The number of r-combinations of n objects is C(n, r) = n!/(r!(n−r)!). When order doesn't matter—choosing committee members or lottery numbers—combinations apply.

## How It's Best Learned
Derive C(n, r) = P(n, r)/r! by recognizing that r! orderings of the same r objects must be divided out. Use the identity C(n, r) = C(n, n−r) to simplify.

## Common Misconceptions
Combinations count unordered sets; {A, B} and {B, A} are the same. Confusing combinations with permutations is the most common error in counting problems.

## Explainer

You already know how to count **permutations** — ordered arrangements. The key insight connecting permutations to combinations is that every unordered selection corresponds to many ordered arrangements. If you pick 3 people from a group of 10 to form a committee, you don't care who was chosen "first" — what matters is the set of names on the list. But when you counted P(10, 3), you treated every ordering of those 3 people as distinct. The fix is simple: divide out the overcounting. Any selection of 3 people can be arranged in 3! = 6 ways, so C(10, 3) = P(10, 3) / 3! = 720 / 6 = 120.

This derivation, C(n, r) = P(n, r) / r! = n! / (r!(n−r)!), is the formula made meaningful. The denominator r! accounts for the fact that order doesn't matter among the chosen items, and (n−r)! accounts for the items not chosen (which were excluded from the permutation count already). You can also think of it as two successive choices: choose which r items are "in" (r! ways to arrange them, divided out) and which n−r are "out" (already handled). This symmetry gives the elegant identity C(n, r) = C(n, n−r) — the number of ways to choose a committee of 3 from 10 equals the number of ways to choose who is *not* on the committee.

The practical test for whether to use combinations or permutations is a question of identity: are {A, B, C} and {C, B, A} the same outcome, or different outcomes? A committee, a hand of cards, a subset of medicines — these are unordered, so combinations apply. A race podium, a password, a seating arrangement — these are ordered, so permutations apply. Most real counting problems require this judgment call first. Combinations appear constantly in probability (where "sample space" events are usually sets), in the binomial theorem, and in Pascal's triangle, where C(n, r) gives every entry.
