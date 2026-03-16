---
id: independence-and-multiplication-rule
title: Independence and the Multiplication Rule
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability
  type: hard
- id: probability-axioms
  type: hard
builds-toward:
- compound-probability
- binomial-distribution
- random-variables-intro
tags:
- independence
- multiplication-rule
- dependent-events
stage: formal-systems
status: draft
---

# Independence and the Multiplication Rule

## Core Idea
Two events A and B are independent if P(A|B) = P(A), meaning knowledge of B does not change the probability of A. For independent events, P(A ∩ B) = P(A) × P(B). The multiplication rule generalizes to: P(A ∩ B) = P(A) × P(B|A) for any events, which is essential for computing probabilities of sequences of outcomes.

## How It's Best Learned
Contrast independent scenarios (flipping two coins) with dependent ones (drawing cards without replacement). Verify independence by checking if P(A|B) = P(A).

## Common Misconceptions
Assuming events are independent when they are not (e.g., weather today and tomorrow). Confusing 'mutually exclusive' with 'independent'.

## Explainer

You've studied conditional probability: P(A|B) = P(A ∩ B)/P(B) tells you how the probability of A changes when you learn B occurred. **Independence** is the special case where learning B tells you nothing new about A — P(A|B) = P(A). Plugging this into the definition of conditional probability immediately gives P(A ∩ B) = P(A) · P(B). This elegant formula is both the formal definition of independence and its most useful computational tool: to find the probability that two independent events both occur, simply multiply their individual probabilities.

The most persistent confusion is between **independence** and **mutual exclusivity**. Mutually exclusive events cannot both occur: P(A ∩ B) = 0, which means if P(A) and P(B) are both positive, knowing A occurred tells you with certainty that B did not — they are maximally dependent. Truly independent events can absolutely both occur: flipping heads on two successive coin flips are independent events that both happen 25% of the time. If two events are mutually exclusive and have positive probability, they are *not* independent. The two concepts are almost opposites.

For sequences of outcomes, the **general multiplication rule** P(A ∩ B) = P(A) · P(B|A) applies whether or not A and B are independent. When they are independent, P(B|A) = P(B) and the formula simplifies to the product rule. When they are dependent, the conditional probability must be carried explicitly. Drawing cards without replacement is the canonical dependent example: P(first card is an ace) = 4/52; P(second card is an ace | first was an ace) = 3/51, not 4/52. The joint probability is (4/52)(3/51) ≠ (4/52)². Replacing the card between draws restores independence.

Independence extends to multiple events: A₁, A₂, ..., Aₙ are **mutually independent** if every subset satisfies the product formula — not just pairs. Pairwise independence is not enough to guarantee mutual independence (there are mathematical counterexamples). For mutually independent events, P(A₁ ∩ A₂ ∩ ... ∩ Aₙ) = P(A₁) · P(A₂) · ... · P(Aₙ), which you'll use constantly: in the binomial distribution (each trial independent), in computing probabilities of repeated experiments, and across all of statistical modeling where the i.i.d. (independent and identically distributed) assumption is the foundation of inference.
