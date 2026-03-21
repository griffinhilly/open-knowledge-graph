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

## Questions

```yaml
- question: "A teacher wants to select 4 students from a class of 20 to represent the school at a conference. How many ways can this selection be made, and which counting method applies?"
  type: multiple-choice
  options:
    - "P(20, 4) = 116,280 — because we are choosing 4 students in sequence"
    - "C(20, 4) = 4,845 — because the group of 4 is what matters, not who was chosen first"
    - "20⁴ = 160,000 — because each of the 4 spots can be filled by any of 20 students"
    - "C(20, 4) × 4! = 116,280 — because we must arrange the representatives alphabetically"
  answer: 1
  explanation: "The key question is: does order matter? A committee or representative group is an unordered set — {Alice, Bob, Carol, Dan} and {Dan, Carol, Bob, Alice} are the same group. So combinations apply: C(20, 4) = 20!/(4! × 16!) = 4,845. Option A is the permutation count, which would be correct if we were assigning roles (president, vice president, etc.) to the 4 students. Option D makes the mistake of combining both methods — if you use C(20, 4), you have already divided out all orderings among the chosen 4."

- question: "A student claims: 'C(12, 5) must be different from C(12, 7) because you are choosing a different number of items.' Are they correct?"
  type: multiple-choice
  options:
    - "Yes — C(12, 5) = 792 and C(12, 7) = 792 happen to be equal only by coincidence"
    - "No — C(n, r) = C(n, n−r) always, because choosing 5 items is equivalent to choosing which 7 to leave out"
    - "Yes — the formula gives different values whenever r ≠ n−r"
    - "No — all combinations with the same n are equal regardless of r"
  answer: 1
  explanation: "The student is wrong. C(n, r) = C(n, n−r) is a fundamental identity, not a coincidence. Choosing 5 items from 12 is the same as choosing which 7 items to exclude — every selection of 5 uniquely determines a rejection of 7, and vice versa. So C(12, 5) = C(12, 7) = 792 exactly. This symmetry also provides a computational shortcut: when r > n/2, compute C(n, n−r) instead, which involves smaller factorials."

- question: "The identity C(n, r) = C(n, n−r) holds for all valid values of n and r."
  type: true-false
  answer: true
  explanation: "This identity follows directly from the formula: C(n, r) = n!/(r!(n−r)!) and C(n, n−r) = n!/((n−r)!r!). The denominators are the same product in different order, so the values are always equal. The combinatorial interpretation is equally clean: choosing r items to include is the same operation as choosing n−r items to exclude, since specifying one completely determines the other."

- question: "In a race with 8 runners, the number of ways to determine the top 3 finishers (first, second, third place) is C(8, 3) = 56."
  type: true-false
  answer: false
  explanation: "Order matters in a race — first, second, and third are distinct positions. {Alice 1st, Bob 2nd, Carol 3rd} is a different outcome than {Bob 1st, Alice 2nd, Carol 3rd}. So permutations apply: P(8, 3) = 8 × 7 × 6 = 336, not C(8, 3) = 56. The combination count 56 would be correct if we just wanted to know which 3 runners made the podium, without caring about their order — for example, selecting 3 runners to receive a generic medal. This is the essential judgment call: ordered → permutations, unordered → combinations."

- question: "Explain why C(n, r) = P(n, r) / r!. What does dividing by r! correct for, and how does this derivation show that combinations count unordered selections?"
  type: short-answer
  answer: "P(n, r) counts all ordered arrangements of r items chosen from n. But if we only care about which r items are chosen — not the order — then every distinct unordered set of r items has been counted r! times in P(n, r), once for each way to arrange those same r items. Dividing by r! cancels this overcounting, leaving exactly the number of distinct unordered selections. This is why C(n, r) = P(n, r) / r!: permutations overcount combinations by a factor of r!, the number of orderings of the selected items."
  explanation: "The derivation makes the formula meaningful rather than arbitrary. The key insight is that overcounting is systematic — every unordered selection is overcounted by exactly the same factor r! — so dividing by r! corrects all cases simultaneously. This also explains why combinations are always smaller than or equal to permutations: combinations disregard ordering information that permutations treat as significant."
```

## Explainer

You already know how to count **permutations** — ordered arrangements. The key insight connecting permutations to combinations is that every unordered selection corresponds to many ordered arrangements. If you pick 3 people from a group of 10 to form a committee, you don't care who was chosen "first" — what matters is the set of names on the list. But when you counted P(10, 3), you treated every ordering of those 3 people as distinct. The fix is simple: divide out the overcounting. Any selection of 3 people can be arranged in 3! = 6 ways, so C(10, 3) = P(10, 3) / 3! = 720 / 6 = 120.

This derivation, C(n, r) = P(n, r) / r! = n! / (r!(n−r)!), is the formula made meaningful. The denominator r! accounts for the fact that order doesn't matter among the chosen items, and (n−r)! accounts for the items not chosen (which were excluded from the permutation count already). You can also think of it as two successive choices: choose which r items are "in" (r! ways to arrange them, divided out) and which n−r are "out" (already handled). This symmetry gives the elegant identity C(n, r) = C(n, n−r) — the number of ways to choose a committee of 3 from 10 equals the number of ways to choose who is *not* on the committee.

The practical test for whether to use combinations or permutations is a question of identity: are {A, B, C} and {C, B, A} the same outcome, or different outcomes? A committee, a hand of cards, a subset of medicines — these are unordered, so combinations apply. A race podium, a password, a seating arrangement — these are ordered, so permutations apply. Most real counting problems require this judgment call first. Combinations appear constantly in probability (where "sample space" events are usually sets), in the binomial theorem, and in Pascal's triangle, where C(n, r) gives every entry.
