---
id: geometric-sequences
title: Geometric Sequences
domain: mathematics
course: algebra-1
prerequisites:
- id: arithmetic-sequences
  type: soft
- id: exponent-rules-product-power-quotient
  type: hard
- id: multiplying-integers
  type: hard
builds-toward:
- geometric-series
- exponential-functions-and-graphs
tags:
- sequences
- geometric
- common-ratio
- exponential
stage: abstract-reasoning
status: validated
---
# Geometric Sequences

## Core Idea
A geometric sequence is a list of numbers where each term is found by multiplying the previous term by a constant called the common ratio (r). The sequence 2, 6, 18, 54, ... has a common ratio of 3. The nth term formula is aₙ = a₁ × r^(n−1). While arithmetic sequences grow by adding a constant (linear growth), geometric sequences grow by multiplying by a constant (exponential growth). When |r| > 1, the sequence grows rapidly; when 0 < |r| < 1, the sequence decreases toward zero. Geometric sequences model compound interest, population growth, radioactive decay, and any multiplicative process.

## How It's Best Learned
Compare directly with arithmetic sequences: one adds, the other multiplies. Identify the common ratio by dividing consecutive terms. Use the formula to find distant terms (what is the 10th term?). Plot terms to see the exponential curve (vs. the straight line of arithmetic sequences). Include ratios less than 1 (decay) and negative ratios (oscillating sequences). Connect to exponential functions.

## Common Misconceptions
- Confusing common difference (arithmetic) with common ratio (geometric).
- Using addition instead of multiplication to find the next term.
- Forgetting that r^(n−1) uses n − 1, not n, as the exponent (the first term has r⁰ = 1 as its multiplier).
- Not recognizing that a negative common ratio causes terms to alternate in sign.

## Questions

```yaml
- question: "The first term of a geometric sequence is 5 and the common ratio is 2. Which expression correctly gives the 4th term?"
  type: multiple-choice
  options:
    - "5 + (4 × 2) = 13"
    - "5 × 2⁴ = 80"
    - "5 × 2³ = 40"
    - "5 × 4 = 20"
  answer: 2
  explanation: "The nth term formula is aₙ = a₁ × r^(n−1). For the 4th term: a₄ = 5 × 2^(4−1) = 5 × 2³ = 5 × 8 = 40. The exponent is n−1 (not n) because the first term requires zero multiplications by r — it already is a₁. Option B (5 × 2⁴) is the most tempting wrong answer; students who forget the −1 choose it. Option A is the arithmetic mistake: adding r × n instead of multiplying by r^(n−1)."

- question: "A sequence reads: 100, 50, 25, 12.5. A student says this is arithmetic because 'the terms get smaller by a consistent pattern.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is right — the terms do decrease consistently, making it arithmetic"
    - "The differences between consecutive terms are not constant (−50, −25, −12.5), so it cannot be arithmetic; it is geometric with r = 0.5"
    - "It is neither arithmetic nor geometric because the terms eventually reach zero"
    - "The student is right, but should call it a 'decreasing' arithmetic sequence"
  answer: 1
  explanation: "In an arithmetic sequence, you subtract the same constant each time. Here the differences are −50, −25, −12.5 — they keep halving, so the differences are not constant. Instead, divide consecutive terms: 50/100 = 25/50 = 12.5/25 = 0.5. The ratio is constant, making this a geometric sequence with r = 0.5. This models exponential decay: each term is half the previous one. The misconception is equating 'consistent decrease' with 'arithmetic' — what matters is whether you're adding or multiplying."

- question: "In the formula aₙ = a₁ × r^(n−1), the exponent is n rather than n−1."
  type: true-false
  answer: false
  explanation: "The exponent must be n−1, not n. The first term (n = 1) requires zero multiplications by r — it is simply a₁ × r⁰ = a₁ × 1 = a₁. The second term requires one multiplication (r¹), the third requires two (r²), and so on. Using r^n instead would give a₁ × r for the first term, which is actually the second term. This off-by-one error is one of the most common mistakes when applying the formula."

- question: "A geometric sequence with a negative common ratio will always decrease toward zero."
  type: true-false
  answer: false
  explanation: "A negative common ratio causes the sequence to alternate in sign, but does not determine whether it grows or shrinks. If |r| > 1 (e.g., r = −3), the terms grow in absolute value while flipping sign: 2, −6, 18, −54, ... If |r| < 1 (e.g., r = −0.5), the terms do shrink toward zero while alternating. The behavior depends entirely on whether |r| is greater than, equal to, or less than 1 — the sign of r only controls the alternating pattern."

- question: "Why does the formula for the nth term of a geometric sequence use r^(n−1) rather than r^n?"
  type: short-answer
  answer: "Because the first term requires zero multiplications by the common ratio. Starting from a₁, you multiply by r once to reach the second term, twice to reach the third, and so on. By the nth term, you have multiplied by r exactly n−1 times. Using r^n would overcount by one multiplication, shifting every term up by one position."
  explanation: "This connects directly to exponent rules: r^0 = 1, so the first term is a₁ × 1 = a₁ (unchanged). Each subsequent term adds one power of r. The formula aₙ = a₁ × r^(n−1) captures this by starting the exponent at zero and incrementing it by one for each subsequent term. Students who understand this reasoning — rather than memorizing 'subtract 1 from n' — are far less likely to make the off-by-one error."
```

## Explainer

You already know **arithmetic sequences**, where each term is found by *adding* a fixed number (the common difference) to the previous term. Geometric sequences work the same way structurally, but replace addition with multiplication. The **common ratio** r is the constant you multiply by each time: to find the next term, multiply the current term by r. So in the sequence 3, 6, 12, 24, 48, ..., the common ratio is 2. You can confirm this by dividing any term by the one before it: 6/3 = 12/6 = 24/12 = 2.

The nth term formula **aₙ = a₁ × r^(n−1)** captures this compactly. The exponent is n−1 because the first term requires *zero* multiplications by r (r⁰ = 1), the second term requires one multiplication, the third requires two, and so on. This is the same logic as your exponent rules: r^0 = 1 means the starting value is untouched. To find the 7th term of the sequence starting at 5 with ratio 3: a₇ = 5 × 3^(7−1) = 5 × 3⁶ = 5 × 729 = 3645.

The key intuition distinguishing geometric from arithmetic sequences is the *type of growth*. Arithmetic sequences grow linearly — if you graph the terms versus their position, you get a straight line. Geometric sequences grow *exponentially* — the graph curves upward (when r > 1) or decays toward zero (when 0 < r < 1). This connects directly to your prerequisite knowledge of exponent rules: geometric sequences *are* exponential functions evaluated at integer inputs. That's why they build toward exponential functions — the formula aₙ = a₁ × r^(n−1) is just an exponential function f(n) = a₁ · r^(n−1) restricted to positive integer values of n.

Two special cases expand the picture. When 0 < r < 1, each term is a fraction of the previous one, and the sequence shrinks toward 0 — this models **decay** (like radioactive half-life or the balance shrinking each period after a withdrawal). When r is negative, the terms alternate in sign: 2, −6, 18, −54, ... (ratio = −3). The terms still grow in absolute value (|r| > 1), but they flip sign every step. Recognizing which case you're in — growth, decay, or oscillating — tells you the qualitative behavior before you compute a single term.
