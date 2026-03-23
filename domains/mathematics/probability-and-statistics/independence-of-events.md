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
status: validated
---

# Independence of Events

## Core Idea
Events A and B are independent if P(A|B)=P(A), equivalently P(A∩B)=P(A)P(B). Independence means information about one event provides no information about the other. Multiple independent events satisfy P(A₁∩...∩Aₙ)=P(A₁)⋯P(Aₙ).

## Questions

```yaml
- question: "Events A and B are mutually exclusive, each with P(A) = P(B) = 0.3. Are A and B independent?"
  type: multiple-choice
  options:
    - "Yes — mutually exclusive events cannot influence each other since they share no outcomes"
    - "No — if B occurred, then A definitely did not occur, so P(A|B) = 0 ≠ 0.3 = P(A)"
    - "Yes — independence and mutual exclusivity are equivalent for events with equal probabilities"
    - "It depends on whether A and B are from the same experiment"
  answer: 1
  explanation: "Mutually exclusive events (A ∩ B = ∅) with positive probability are dependent, not independent. If B occurred, A is impossible — P(A|B) = 0, which differs from P(A) = 0.3. Independence requires that knowing B occurred gives no information about A. Mutual exclusivity gives maximum negative information: knowing B makes A impossible. This is the opposite of independence. The confusion arises because 'they can't happen together' sounds like 'they don't affect each other,' but probabilistically it's a strong dependency."

- question: "Which of the following is the correct working definition of independence for events A and B?"
  type: multiple-choice
  options:
    - "A and B come from physically separate experiments"
    - "A and B cannot occur at the same time"
    - "P(A ∩ B) = P(A) · P(B)"
    - "P(A | B) is defined and equals P(B | A)"
  answer: 2
  explanation: "Independence is formally defined as P(A ∩ B) = P(A) · P(B). This product rule is the working definition because it avoids dividing by P(B) (which could be 0) and generalizes naturally to more than two events. Option A describes a common intuition that is often but not always correct — physical separateness suggests independence but is not the definition. Option B is mutual exclusivity, which implies dependence for events with positive probability."

- question: "If P(A) = 0.4 and P(B) = 0.5 and A and B are independent, then P(A ∩ B) = 0.2."
  type: true-false
  answer: true
  explanation: "By the product rule for independent events: P(A ∩ B) = P(A) · P(B) = 0.4 × 0.5 = 0.2. This is direct application of the definition. Note that this product rule is not valid for dependent events — if A and B were dependent, you would need P(A ∩ B) = P(A) · P(B | A), and P(B | A) ≠ P(B)."

- question: "If three events are pairwise independent — every pair satisfies the product rule — then the three events are mutually independent."
  type: true-false
  answer: false
  explanation: "Pairwise independence does not imply mutual independence. Classic counterexample: flip a fair coin twice. Let A₁ = heads on flip 1, A₂ = heads on flip 2, A₃ = exactly one head total. Every pair is independent (P(Aᵢ ∩ Aⱼ) = P(Aᵢ)P(Aⱼ) for each pair). But P(A₁ ∩ A₂ ∩ A₃) = 0 (you can't have two heads AND exactly one head), while P(A₁)P(A₂)P(A₃) = 1/8 ≠ 0. Mutual independence requires all subsets — not just pairs — to satisfy the product rule."

- question: "Explain why mutually exclusive events with positive probability are dependent, not independent. Use the formal definition of independence in your answer."
  type: short-answer
  answer: "Two events are independent if P(A ∩ B) = P(A) · P(B). For mutually exclusive events, P(A ∩ B) = 0 (they cannot both occur). But if P(A) > 0 and P(B) > 0, then P(A) · P(B) > 0. So P(A ∩ B) = 0 ≠ P(A) · P(B), violating the product rule — the events are dependent. Intuitively: if A and B are mutually exclusive and you learn B occurred, you immediately know A did not occur (P(A|B) = 0), which differs from P(A). Learning B tells you something definitive about A — the opposite of independence."
  explanation: "This is one of the most important and counterintuitive facts in probability. Students often confuse 'independent' with 'unrelated' or 'separate,' and 'mutually exclusive' sounds like the events are completely separate. But probability independence is a quantitative condition about information, and mutually exclusive events are as far from independent as possible."
```

## Explainer

From conditional probability, you know that P(A|B) — the probability of A given that B occurred — generally differs from P(A). Learning that B happened updates your assessment of A's likelihood. **Independence** is the special case where it doesn't: P(A|B) = P(A). Knowing B gives you zero information about A. Using the multiplication rule P(A|B) = P(A∩B)/P(B), this becomes P(A∩B)/P(B) = P(A), which rearranges to P(A∩B) = P(A)·P(B). This **product rule** is the standard working definition of independence because it avoids division by P(B) and applies even when P(B) = 0.

Concrete examples sharpen the intuition. Two fair coin flips are independent: P(H on flip 2 | H on flip 1) = 1/2 = P(H on flip 2). The outcome of the first flip tells you nothing about the second. In contrast, drawing two cards from a deck without replacement makes the draws dependent: P(2nd card is an ace | 1st card was an ace) = 3/51, not 4/52 = P(2nd card is an ace). The product rule fails, confirming dependence.

For more than two events, **mutual independence** requires that *every subset* satisfies the product rule: P(A_{i₁} ∩ ... ∩ A_{iₖ}) = P(A_{i₁})···P(A_{iₖ}) for every subset {i₁, ..., iₖ}. This is strictly stronger than **pairwise independence**, where only pairs satisfy the rule. A classic counterexample: let a fair coin be flipped twice. Define A₁ = {heads on flip 1}, A₂ = {heads on flip 2}, A₃ = {exactly one head total}. Every pair is independent (you can verify P(Aᵢ∩Aⱼ) = P(Aᵢ)P(Aⱼ) for each pair), but P(A₁∩A₂∩A₃) = 0 ≠ P(A₁)P(A₂)P(A₃) = 1/8 — mutual independence fails. Never assume mutual independence just because you have checked all pairs.

Independence is the assumption that makes probability tractable for complex models. If X₁, ..., Xₙ are independent, their joint distribution is the product of the marginals — enormously simplifying calculations for sums, products, and inference. The central limit theorem, the law of large numbers, and virtually every foundational result in statistics assume independent observations. When you move into sampling distributions and limit theorems, checking whether your observations are genuinely independent will be one of the first modeling questions to address.
