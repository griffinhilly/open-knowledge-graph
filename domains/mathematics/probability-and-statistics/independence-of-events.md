---
id: independence-of-events
title: Independence of Events
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability-fundamentals
  type: hard
builds-toward:
- sampling-distributions
- central-limit-theorem
tags:
- independence
- probability
stage: formal-systems
status: draft
---

# Independence of Events

## Core Idea
Events A and B are independent if P(A|B)=P(A), equivalently P(A∩B)=P(A)P(B). Independence means information about one event provides no information about the other. Multiple independent events satisfy P(A₁∩...∩Aₙ)=P(A₁)⋯P(Aₙ).

## Explainer

From conditional probability, you know that P(A|B) — the probability of A given that B occurred — generally differs from P(A). Learning that B happened updates your assessment of A's likelihood. **Independence** is the special case where it doesn't: P(A|B) = P(A). Knowing B gives you zero information about A. Using the multiplication rule P(A|B) = P(A∩B)/P(B), this becomes P(A∩B)/P(B) = P(A), which rearranges to P(A∩B) = P(A)·P(B). This **product rule** is the standard working definition of independence because it avoids division by P(B) and applies even when P(B) = 0.

Concrete examples sharpen the intuition. Two fair coin flips are independent: P(H on flip 2 | H on flip 1) = 1/2 = P(H on flip 2). The outcome of the first flip tells you nothing about the second. In contrast, drawing two cards from a deck without replacement makes the draws dependent: P(2nd card is an ace | 1st card was an ace) = 3/51, not 4/52 = P(2nd card is an ace). The product rule fails, confirming dependence.

For more than two events, **mutual independence** requires that *every subset* satisfies the product rule: P(A_{i₁} ∩ ... ∩ A_{iₖ}) = P(A_{i₁})···P(A_{iₖ}) for every subset {i₁, ..., iₖ}. This is strictly stronger than **pairwise independence**, where only pairs satisfy the rule. A classic counterexample: let a fair coin be flipped twice. Define A₁ = {heads on flip 1}, A₂ = {heads on flip 2}, A₃ = {exactly one head total}. Every pair is independent (you can verify P(Aᵢ∩Aⱼ) = P(Aᵢ)P(Aⱼ) for each pair), but P(A₁∩A₂∩A₃) = 0 ≠ P(A₁)P(A₂)P(A₃) = 1/8 — mutual independence fails. Never assume mutual independence just because you have checked all pairs.

Independence is the assumption that makes probability tractable for complex models. If X₁, ..., Xₙ are independent, their joint distribution is the product of the marginals — enormously simplifying calculations for sums, products, and inference. The central limit theorem, the law of large numbers, and virtually every foundational result in statistics assume independent observations. When you move into sampling distributions and limit theorems, checking whether your observations are genuinely independent will be one of the first modeling questions to address.
