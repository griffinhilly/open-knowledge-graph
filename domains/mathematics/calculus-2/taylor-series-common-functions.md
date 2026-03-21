---
id: taylor-series-common-functions
title: Taylor Series for Common Functions
domain: mathematics
course: calculus-2
prerequisites:
  - id: maclaurin-series
    type: hard
builds-toward: []
tags: [series, Taylor, reference, common-functions]
stage: formal-systems
status: validated
---

# Taylor Series for Common Functions

## Core Idea
The essential Taylor/Maclaurin series to know are: e^x = sum x^n/n! (all x), sin(x) = sum (-1)^n x^(2n+1)/(2n+1)! (all x), cos(x) = sum (-1)^n x^(2n)/(2n)! (all x), 1/(1-x) = sum x^n (|x| < 1), ln(1+x) = sum (-1)^(n+1) x^n/n (|x| <= 1, x not equal to -1), arctan(x) = sum (-1)^n x^(2n+1)/(2n+1) (|x| <= 1), and (1+x)^k = sum C(k,n) x^n (binomial series, |x| < 1). These serve as building blocks for constructing series of more complex functions.

## How It's Best Learned
Memorize these series and their intervals of convergence. Practice generating new series by substitution (e.g., e^(-x^2)), multiplication, differentiation (e.g., 1/(1-x)^2 from 1/(1-x)), and integration (e.g., ln(1+x) from 1/(1+x)). Use these to evaluate limits, compute integrals without closed forms, and approximate values.

## Common Misconceptions
- Mixing up which series have alternating signs and which do not.
- Forgetting whether a series uses all powers of x or only odd/even powers.
- Not adjusting the radius of convergence after substitution.

## Questions

```yaml
- question: "The geometric series 1/(1−x) = Σxⁿ converges for |x| < 1. What is the interval of convergence for the series of 1/(1−3x) obtained by substituting 3x for x?"
  type: multiple-choice
  options:
    - "|x| < 1, because substitution does not change the radius of convergence"
    - "|x| < 1/3, because the condition |3x| < 1 becomes |x| < 1/3"
    - "|x| < 3, because the substitution stretches the interval by a factor of 3"
    - "All real x, because rational functions are defined everywhere"
  answer: 1
  explanation: "The convergence condition for the geometric series is |substituted variable| < 1. After substituting 3x, the condition becomes |3x| < 1, which simplifies to |x| < 1/3. Option A is the classic error: it copies the original radius without rederiving it after substitution. The radius always scales inversely with any constant multiplier on x — multiplying x by 3 shrinks the interval of convergence by a factor of 3."

- question: "Why does the Maclaurin series for sin(x) contain only odd-power terms (x, x³, x⁵, ...) with no even-power terms?"
  type: multiple-choice
  options:
    - "By coincidence in the pattern of derivatives at x = 0"
    - "Because sin(x) is an odd function, and odd functions have only odd-power Maclaurin series"
    - "Because even-power terms would cause the series to diverge"
    - "Because the denominators n! grow too fast for even powers to contribute"
  answer: 1
  explanation: "An odd function satisfies f(−x) = −f(x). For a Maclaurin series f(x) = Σaₙxⁿ, this forces aₙ = 0 for all even n — otherwise the even terms would not cancel under x → −x. Since sin(−x) = −sin(x), all even coefficients must vanish. The even-power terms are absent by structural necessity, not coincidence. Similarly, cos(x) is even (cos(−x) = cos(x)), so its series has only even powers. This structural insight lets you reconstruct the form of these series quickly even if you forget the exact coefficients."

- question: "Substituting x² into the series for e^x gives a new series valid only for |x| < 1, since e^x itself converges only on a bounded interval."
  type: true-false
  answer: false
  explanation: "The series for e^x converges for all real x (its radius of convergence is infinite). Substituting x² gives e^(x²) = Σ(x²)ⁿ/n! = Σx^(2n)/n!, which also converges for all real x, since x² is finite for any finite x. The misconception arises from confusing e^x with the geometric series 1/(1−x), which does have a finite radius. After substitution into e^x, the only question is whether x² is finite — which it always is."

- question: "Differentiating the geometric series 1/(1−x) = Σxⁿ term by term yields the series for 1/(1−x)²."
  type: true-false
  answer: true
  explanation: "Differentiating both sides: the left side gives 1/(1−x)². The right side differentiates term by term to Σnx^(n−1). This is valid within the radius of convergence |x| < 1, where power series can be differentiated term by term. This technique — differentiating a known series to obtain a new one — is one of the three core manipulation strategies (with substitution and integration) for building new series without starting from scratch."

- question: "Why must you rederive the interval of convergence after substituting into a known Taylor series? Give a specific example."
  type: short-answer
  answer: "The convergence condition depends on the magnitude of the variable in the series. After substitution, the variable changes, so the condition must be re-expressed in terms of the new variable. Example: 1/(1−x) = Σxⁿ converges for |x| < 1. Substituting x² gives 1/(1−x²) = Σx^(2n), convergent when |x²| < 1, i.e., |x| < 1 — same interval here. But substituting 2x gives 1/(1−2x) = Σ(2x)ⁿ, convergent when |2x| < 1, i.e., |x| < 1/2. The substitution changed the interval."
  explanation: "This is a direct application of the chain: 'convergence condition for the original series' → 'apply the substitution' → 'solve for x.' Skipping this step is the most common source of errors when deriving new series. The interval can expand (if you substitute something smaller than x) or contract (if you substitute something larger), so the original radius of convergence is never automatically inherited."
```

## Explainer

You have learned how to construct a Maclaurin series by repeatedly differentiating a function and evaluating at zero. The standard series in this topic are the outputs of that process applied to the most important functions. Think of this list not as facts to memorize in isolation, but as a toolkit: once you have e^x, sin(x), cos(x), and 1/(1−x) committed to memory, you can derive dozens of other series without recomputing from scratch. The power comes from three manipulation techniques — **substitution**, **differentiation**, and **integration** — applied to series you already know.

Substitution is the fastest technique. To find the series for e^{−x²}, replace x with −x² in the series for e^x: e^{−x²} = Σ(−x²)^n/n! = Σ(−1)^n x^{2n}/n!. To find the series for cos(x²), substitute x² into the cosine series. The critical caution: the radius of convergence changes under substitution. The geometric series 1/(1−x) = Σx^n converges for |x| < 1. Substituting x² gives 1/(1−x²) = Σx^{2n}, valid for |x²| < 1, i.e., |x| < 1 — same condition here, but if you had substituted 2x you would get convergence for |2x| < 1, meaning |x| < 1/2. Always re-derive the convergence condition after substitution.

Differentiation and integration extend the toolkit further. Differentiating 1/(1−x) = Σx^n term by term gives 1/(1−x)² = Σnx^{n−1}. Integrating 1/(1−x) gives −ln(1−x) = Σx^{n+1}/(n+1), which rearranges to the series for ln(1+x) after substituting −x. The series for arctan(x) comes from integrating 1/(1+x²) = Σ(−1)^n x^{2n} term by term: arctan(x) = Σ(−1)^n x^{2n+1}/(2n+1). Notice that the known series for 1/(1−x) is the seed from which several other standard series grow.

The series also have a structural logic worth noticing. The series for e^x uses all non-negative powers with no sign changes and denominators n!. The sine series uses only odd powers with alternating signs; the cosine series uses only even powers with alternating signs. This reflects the fact that sin is odd and cos is even — odd functions have only odd-power terms, even functions have only even-power terms. The alternating signs come from the pattern of derivatives: sin, cos, −sin, −cos, sin, ... so every four steps the sign pattern repeats. Seeing the structural reason for each feature helps you reconstruct series quickly if you forget a detail, rather than relying purely on memorization.
