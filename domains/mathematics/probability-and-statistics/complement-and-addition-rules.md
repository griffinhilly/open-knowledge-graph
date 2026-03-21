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

## Questions

```yaml
- question: "Two events A and B satisfy P(A) = 0.4, P(B) = 0.3, and P(A ∩ B) = 0.1. What is P(A ∪ B)?"
  type: multiple-choice
  options:
    - "0.7 — simply add the probabilities since both events can occur"
    - "0.6 — subtract the intersection to correct for double-counting"
    - "0.12 — multiply the probabilities since they are not independent"
    - "0.5 — take the average of the two probabilities"
  answer: 1
  explanation: "P(A ∪ B) = P(A) + P(B) − P(A ∩ B) = 0.4 + 0.3 − 0.1 = 0.6. Option A is the classic error: adding without subtracting the intersection counts the overlap twice. The intersection region appears in both P(A) and P(B), so it must be subtracted once to give each outcome exactly one count."

- question: "You roll a fair 6-sided die 4 times. What is the most efficient approach to find P(at least one 6)?"
  type: multiple-choice
  options:
    - "Add the probabilities of getting exactly 1 six, exactly 2 sixes, exactly 3 sixes, and exactly 4 sixes"
    - "Use the complement: 1 − P(no sixes) = 1 − (5/6)⁴"
    - "Apply the addition rule to four separate roll events"
    - "Multiply the probability of a 6 on one roll by 4"
  answer: 1
  explanation: "The complement rule turns 'at least one' into 'none': P(no 6 in 4 rolls) = (5/6)⁴, so P(at least one 6) = 1 − (5/6)⁴ ≈ 0.518. This is one calculation. The direct approach (option A) requires four separate binomial terms. Whenever 'at least one' appears, ask yourself whether the complement — 'none' — is easier to compute."

- question: "If two events are mutually exclusive, they are also complementary."
  type: true-false
  answer: false
  explanation: "Mutually exclusive means P(A ∩ B) = 0 — the events can't both occur simultaneously. Complementary is stricter: A and Aᶜ must also together cover the entire sample space, so P(A) + P(Aᶜ) = 1. Every complementary pair is mutually exclusive, but most mutually exclusive pairs are not complementary. Rolling a 1 and rolling a 2 on a die are mutually exclusive but not complementary — the other four outcomes belong to neither."

- question: "Using the complement rule is often the most efficient way to compute the probability of 'at least one' occurrence."
  type: true-false
  answer: true
  explanation: "The complement of 'at least one' is 'none at all' — typically a single multiplicative calculation. The direct approach requires summing probabilities over all possible counts (1, 2, 3, ..., n occurrences), which grows rapidly. The complement shortcut is almost always simpler, especially when outcomes are independent."

- question: "Explain why P(A ∪ B) = P(A) + P(B) − P(A ∩ B) and not just P(A) + P(B)."
  type: short-answer
  answer: "When you add P(A) and P(B), any outcome in the intersection A ∩ B is counted twice — once as part of A and once as part of B. Subtracting P(A ∩ B) removes the extra count, giving each outcome exactly one contribution to the total. The simpler formula P(A ∪ B) = P(A) + P(B) is correct only when A and B are mutually exclusive, because then the intersection is empty and there is nothing to remove."
  explanation: "This is the inclusion-exclusion principle for two sets. Visualize a Venn diagram: the left circle is A, the right is B, and the middle lens is A ∩ B. Adding the full left circle and the full right circle counts the lens region twice. Subtracting the lens once gives the correct total area of the union. The same logic extends to three or more events with more alternating addition and subtraction terms."
```

## Explainer

From the probability axioms, you know that P(S) = 1 and that probabilities of disjoint events add up. The complement and addition rules are direct consequences of these axioms, packaged into reusable formulas. Understanding them is less about memorizing formulas and more about internalizing when it's easier to count what *doesn't* happen than what does.

The **complement rule** P(Aᶜ) = 1 − P(A) follows immediately from the axioms: A and Aᶜ are disjoint and together make up the entire sample space S, so P(A) + P(Aᶜ) = P(S) = 1. Rearranging gives the rule. Its power appears in "at least one" problems. Suppose you flip a fair coin 5 times and ask: what is the probability of getting at least one head? Directly, you'd need to sum the probabilities of exactly 1, 2, 3, 4, or 5 heads — five terms. Using the complement, P(at least one head) = 1 − P(no heads) = 1 − (1/2)⁵ = 31/32. One calculation instead of five. Whenever "at least one" appears, the complement rule is usually the right tool.

The **addition rule** P(A ∪ B) = P(A) + P(B) − P(A ∩ B) corrects for double-counting. Imagine a Venn diagram: the left circle is A, the right circle is B, and the overlapping region is A ∩ B. When you add P(A) and P(B), you've counted the overlap twice — once in each circle. Subtracting P(A ∩ B) removes the extra count. This is the inclusion-exclusion principle for two sets. When A and B are **mutually exclusive** — their circles don't overlap, P(A ∩ B) = 0 — the subtraction term vanishes, giving the simpler P(A ∪ B) = P(A) + P(B).

The critical distinction is between **mutually exclusive** and **complementary**. Mutually exclusive just means the events can't both occur: P(A ∩ B) = 0. Complementary is stricter: A and Aᶜ are mutually exclusive *and* they cover all possibilities, so P(A) + P(Aᶜ) = 1. Every complementary pair is mutually exclusive, but most mutually exclusive pairs are not complementary. For example, rolling a 1 and rolling a 2 on a die are mutually exclusive (can't both happen on one roll) but not complementary (neither covers all non-outcomes of the other). Keeping this distinction sharp prevents the most common error: applying the complement rule P(A ∪ B) = 1 − P(A ∩ B), which would only be valid for very special cases.
