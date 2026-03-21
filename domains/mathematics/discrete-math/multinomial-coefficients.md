---
id: multinomial-coefficients
title: Multinomial Coefficients
domain: mathematics
course: discrete-math
prerequisites:
- id: combinations
  type: hard
- id: binomial-theorem
  type: hard
- id: permutations
  type: soft
builds-toward:
- generating-functions-intro
tags:
- multinomial
- coefficients
- counting
- combinatorics
- polynomial-expansion
stage: formal-systems
status: validated
---

# Multinomial Coefficients

## Core Idea
The multinomial coefficient n!/(k₁! k₂! ⋯ kₘ!) counts the number of ways to divide n distinct objects into m ordered groups of sizes k₁, k₂, …, kₘ where k₁ + k₂ + ⋯ + kₘ = n. The multinomial theorem generalizes the binomial theorem: (x₁ + x₂ + ⋯ + xₘ)ⁿ equals the sum over all valid (k₁,…,kₘ) of the multinomial coefficient times x₁^k₁ ⋯ xₘ^kₘ. Multinomial coefficients arise naturally when counting arrangements of strings with repeated letters.

## How It's Best Learned
Connect to the binomial theorem first as the m=2 special case. Count arrangements of words with repeated letters (e.g., MISSISSIPPI has 11!/(4!4!2!1!) arrangements) to make the formula concrete before moving to polynomial expansion.

## Common Misconceptions
- Treating the multinomial coefficient as a product of binomial coefficients — this only works in specific decomposition sequences, not in general.
- Forgetting that all group sizes must sum to n.

## Questions

```yaml
- question: "The word PEPPER has 6 letters: three P's, two E's, and one R. How many distinct arrangements of these letters are there?"
  type: multiple-choice
  options:
    - "720 (= 6!)"
    - "60 (= 6! / (3! · 2! · 1!))"
    - "120 (= 5!)"
    - "360 (= 6! / 2!)"
  answer: 1
  explanation: "The multinomial coefficient corrects for repeated letters by dividing out all permutations among identical elements. With 3 P's, 2 E's, and 1 R, the formula is 6!/(3!·2!·1!) = 720/12 = 60. Option A (720) ignores the repeats entirely and overcounts — it assumes all 6 letters are distinct. Options C and D only account for one type of repetition instead of all."

- question: "In the expansion of (a + b + c)⁴, what is the coefficient of the term a²bc?"
  type: multiple-choice
  options:
    - "4"
    - "6"
    - "12"
    - "24"
  answer: 2
  explanation: "The coefficient of a^k₁ b^k₂ c^k₃ in (a+b+c)ⁿ is the multinomial coefficient n!/(k₁!k₂!k₃!). Here n=4, k₁=2, k₂=1, k₃=1, so the coefficient is 4!/(2!·1!·1!) = 24/2 = 12. A common error is to use C(4,2) = 6 (option B), which only accounts for choosing the positions for a but ignores the subsequent distribution of b and c. The multinomial coefficient counts all the ways to assign the four 'slots' to a (2 slots), b (1 slot), and c (1 slot)."

- question: "The binomial theorem is a special case of the multinomial theorem that applies only when all exponents in the expansion are equal."
  type: true-false
  answer: false
  explanation: "The binomial theorem is the m=2 special case of the multinomial theorem — it applies when there are exactly two terms being summed, regardless of the exponents. The multinomial theorem covers (x₁ + x₂ + ⋯ + xₘ)ⁿ for any number of terms m; setting m=2 gives exactly the binomial theorem with the familiar binomial coefficients C(n,k) = n!/(k!(n−k)!). Exponent equality is irrelevant."

- question: "The number of distinct arrangements of a string of n letters, where letter i appears kᵢ times (with k₁ + k₂ + ⋯ + kₘ = n), is exactly the multinomial coefficient n!/(k₁!k₂!⋯kₘ!)."
  type: true-false
  answer: true
  explanation: "Correct. If all n letters were distinct, there would be n! arrangements. But among the arrangements, any permutation of the kᵢ identical copies of letter i produces the same word — so we are overcounting by kᵢ! for each group. Dividing by k₁!k₂!⋯kₘ! corrects all overcounting simultaneously, giving n!/(k₁!⋯kₘ!). This is the core combinatorial meaning of the multinomial coefficient."

- question: "Why does the multinomial coefficient formula divide by each kᵢ! separately rather than, say, by (k₁ + k₂ + ⋯ + kₘ)! or by the product k₁ · k₂ · ⋯ · kₘ? What does each factorial represent?"
  type: short-answer
  answer: "Each kᵢ! accounts for the kᵢ! ways of permuting the identical copies of item i among themselves — permutations that produce the same arrangement and must not be counted separately. Since the groups are independent, the total overcounting is the product of all the individual kᵢ! values, so we divide by each factorial independently. Dividing by the sum (k₁+⋯+kₘ)! = n! would over-correct, and dividing by the product of the raw values kᵢ wouldn't fully remove all redundant permutations."
  explanation: "The factorial kᵢ! appears because the kᵢ identical copies of item i can be rearranged among themselves in kᵢ! ways, all yielding the same outcome. Since these groups of identical objects are independent of each other, the overcounting factors multiply: total overcounting = k₁! × k₂! × ⋯ × kₘ!. Dividing n! by this product gives the exact count of truly distinct arrangements."
```

## Explainer

You already know the **binomial coefficient** C(n, r) = n!/(r!(n−r)!) and the **binomial theorem**: (x + y)ⁿ expands into a sum of terms C(n, k) xᵏ yⁿ⁻ᵏ. The multinomial coefficient generalizes both to situations with more than two categories. Suppose you have n distinct objects and want to sort them into m labeled boxes of sizes k₁, k₂, …, kₘ (where the sizes sum to n). The **multinomial coefficient** n!/(k₁! k₂! ⋯ kₘ!) counts the ways to do this. When m = 2, it reduces exactly to C(n, k₁) = n!/(k₁! k₂!) — the familiar binomial coefficient.

The most concrete way to build intuition is through **arrangements of strings with repeated letters**. How many ways can you arrange the letters in MISSISSIPPI? You have 11 letters: 1 M, 4 I's, 4 S's, and 2 P's. If all 11 were distinct, there'd be 11! arrangements. But the 4 I's are identical — any permutation among them gives the same word — so divide by 4!. Same for the S's (divide by 4!) and P's (divide by 2!). Result: 11!/(1!⋅4!⋅4!⋅2!) = 34,650. The formula is not an arbitrary definition; it's exactly the correction factor for repeated elements.

The **multinomial theorem** extends this to polynomial expansion: (x₁ + x₂ + ⋯ + xₘ)ⁿ = Σ n!/(k₁!⋯kₘ!) · x₁^k₁ ⋯ xₘ^kₘ, where the sum runs over all tuples (k₁,…,kₘ) of non-negative integers summing to n. To see why: expanding the product means choosing, from each of the n factors, one variable xᵢ to "take." For a given monomial x₁^k₁⋯xₘ^kₘ to appear, you must pick x₁ exactly k₁ times, x₂ exactly k₂ times, etc. — and the number of ways to make those selections is precisely the multinomial coefficient. The binomial theorem is just the m = 2 special case.

Where multinomial coefficients diverge from iterated binomial coefficients is subtle. You *can* compute a multinomial coefficient as a product of binomials: n!/(k₁!k₂!k₃!) = C(n, k₁) · C(n−k₁, k₂) · C(n−k₁−k₂, k₃). This "sequential selection" decomposition is valid and sometimes useful, but the end result — the multinomial coefficient — is a single number, not a sequence-dependent product. The value is independent of which decomposition order you choose, because the formula n!/(k₁!⋯kₘ!) is symmetric in interpretation.
