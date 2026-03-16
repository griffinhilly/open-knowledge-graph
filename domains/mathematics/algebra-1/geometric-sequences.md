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

## Explainer

You already know **arithmetic sequences**, where each term is found by *adding* a fixed number (the common difference) to the previous term. Geometric sequences work the same way structurally, but replace addition with multiplication. The **common ratio** r is the constant you multiply by each time: to find the next term, multiply the current term by r. So in the sequence 3, 6, 12, 24, 48, ..., the common ratio is 2. You can confirm this by dividing any term by the one before it: 6/3 = 12/6 = 24/12 = 2.

The nth term formula **aₙ = a₁ × r^(n−1)** captures this compactly. The exponent is n−1 because the first term requires *zero* multiplications by r (r⁰ = 1), the second term requires one multiplication, the third requires two, and so on. This is the same logic as your exponent rules: r^0 = 1 means the starting value is untouched. To find the 7th term of the sequence starting at 5 with ratio 3: a₇ = 5 × 3^(7−1) = 5 × 3⁶ = 5 × 729 = 3645.

The key intuition distinguishing geometric from arithmetic sequences is the *type of growth*. Arithmetic sequences grow linearly — if you graph the terms versus their position, you get a straight line. Geometric sequences grow *exponentially* — the graph curves upward (when r > 1) or decays toward zero (when 0 < r < 1). This connects directly to your prerequisite knowledge of exponent rules: geometric sequences *are* exponential functions evaluated at integer inputs. That's why they build toward exponential functions — the formula aₙ = a₁ × r^(n−1) is just an exponential function f(n) = a₁ · r^(n−1) restricted to positive integer values of n.

Two special cases expand the picture. When 0 < r < 1, each term is a fraction of the previous one, and the sequence shrinks toward 0 — this models **decay** (like radioactive half-life or the balance shrinking each period after a withdrawal). When r is negative, the terms alternate in sign: 2, −6, 18, −54, ... (ratio = −3). The terms still grow in absolute value (|r| > 1), but they flip sign every step. Recognizing which case you're in — growth, decay, or oscillating — tells you the qualitative behavior before you compute a single term.
