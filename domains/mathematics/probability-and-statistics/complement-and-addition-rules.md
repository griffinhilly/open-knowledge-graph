---
id: complement-and-addition-rules
title: Complement Rule and Addition Rule
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-axioms
  type: hard
builds-toward:
- conditional-probability
- bayes-theorem
tags:
- complement-rule
- addition-rule
- mutually-exclusive
- probability-rules
stage: formal-systems
status: validated
---

# Complement Rule and Addition Rule

## Core Idea
The complement rule states P(Aᶜ) = 1 − P(A), useful when the complement is easier to compute than the event itself. The general addition rule is P(A ∪ B) = P(A) + P(B) − P(A ∩ B), which corrects for double-counting the intersection. When A and B are mutually exclusive (P(A ∩ B) = 0), this simplifies to P(A ∪ B) = P(A) + P(B).

## How It's Best Learned
Use Venn diagrams to make the double-counting in the addition rule visual. The complement rule is especially powerful for 'at least one' problems — computing P(none) is often simpler than summing multiple cases.

## Common Misconceptions
- Applying the simplified addition rule (without subtracting intersection) when events are not mutually exclusive.
- Confusing 'mutually exclusive' with 'complementary' — complementary events must together exhaust S and are a special case of mutually exclusive.

## Explainer

From the probability axioms, you know that P(S) = 1 and that probabilities of disjoint events add up. The complement and addition rules are direct consequences of these axioms, packaged into reusable formulas. Understanding them is less about memorizing formulas and more about internalizing when it's easier to count what *doesn't* happen than what does.

The **complement rule** P(Aᶜ) = 1 − P(A) follows immediately from the axioms: A and Aᶜ are disjoint and together make up the entire sample space S, so P(A) + P(Aᶜ) = P(S) = 1. Rearranging gives the rule. Its power appears in "at least one" problems. Suppose you flip a fair coin 5 times and ask: what is the probability of getting at least one head? Directly, you'd need to sum the probabilities of exactly 1, 2, 3, 4, or 5 heads — five terms. Using the complement, P(at least one head) = 1 − P(no heads) = 1 − (1/2)⁵ = 31/32. One calculation instead of five. Whenever "at least one" appears, the complement rule is usually the right tool.

The **addition rule** P(A ∪ B) = P(A) + P(B) − P(A ∩ B) corrects for double-counting. Imagine a Venn diagram: the left circle is A, the right circle is B, and the overlapping region is A ∩ B. When you add P(A) and P(B), you've counted the overlap twice — once in each circle. Subtracting P(A ∩ B) removes the extra count. This is the inclusion-exclusion principle for two sets. When A and B are **mutually exclusive** — their circles don't overlap, P(A ∩ B) = 0 — the subtraction term vanishes, giving the simpler P(A ∪ B) = P(A) + P(B).

The critical distinction is between **mutually exclusive** and **complementary**. Mutually exclusive just means the events can't both occur: P(A ∩ B) = 0. Complementary is stricter: A and Aᶜ are mutually exclusive *and* they cover all possibilities, so P(A) + P(Aᶜ) = 1. Every complementary pair is mutually exclusive, but most mutually exclusive pairs are not complementary. For example, rolling a 1 and rolling a 2 on a die are mutually exclusive (can't both happen on one roll) but not complementary (neither covers all non-outcomes of the other). Keeping this distinction sharp prevents the most common error: applying the complement rule P(A ∪ B) = 1 − P(A ∩ B), which would only be valid for very special cases.
