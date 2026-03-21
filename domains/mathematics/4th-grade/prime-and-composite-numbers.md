---
id: prime-and-composite-numbers
title: Prime and Composite Numbers
domain: mathematics
course: 4th-grade
prerequisites:
- id: factors-and-multiples
  type: hard
- id: multiples-of-a-number
  type: soft
builds-toward:
- equivalent-fractions
tags:
- number-theory
- primes
- factors
stage: concrete-operations
status: validated
---
# Prime and Composite Numbers

## Core Idea
A prime number has exactly two factors: 1 and itself. A composite number has more than two factors, meaning it can be divided evenly by at least one number other than 1 and itself. The number 1 is neither prime nor composite (it has only one factor). Every composite number can be written as a product of primes (its prime factorization), a fact that becomes important in later work with fractions and algebra. At fourth grade, students learn to classify numbers as prime or composite and begin to appreciate that primes are the "building blocks" of all whole numbers.

## How It's Best Learned
Use the Sieve of Eratosthenes: on a 1-100 chart, cross out multiples of 2, then 3, then 5, then 7 -- the surviving numbers are primes. This makes the concept active and visual. Have students try to form different rectangles with a given number of tiles; prime numbers can only make a 1-by-n rectangle.

## Common Misconceptions
- Thinking 1 is prime (it is not -- it has only one factor, not two).
- Thinking 2 is not prime because it is even (it is the only even prime).
- Confusing "prime" with "odd" -- 9, 15, 21, etc. are odd but composite.

## Questions

```yaml
- question: "A student claims 1 is a prime number because 'it can only be divided evenly by 1 and itself, and those are the same number.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — 1 is a prime number by the standard definition"
    - "A prime must have exactly two DIFFERENT factors; 1 has only one factor (itself)"
    - "1 is actually composite because all whole numbers are either prime or composite"
    - "1 is prime only in certain number systems, not in standard arithmetic"
  answer: 1
  explanation: "The definition of prime requires exactly two factors: 1 and the number itself — and these must be two different numbers. For 7, the factors are 1 and 7 (different numbers). For 1, 'itself' is also 1 — so there is only one distinct factor. One factor satisfies neither the prime definition (needs two) nor the composite definition (needs more than two). The student's reasoning sounds logical but misses that 'itself' must be a different number from 1."

- question: "Which of the following numbers is composite despite being odd?"
  type: multiple-choice
  options:
    - "7"
    - "11"
    - "9"
    - "13"
  answer: 2
  explanation: "9 = 3 × 3, so its factors are 1, 3, and 9 — three factors, making it composite. Many students assume all odd numbers are prime, but this is false. 9, 15, 21, 25, and many other odd numbers are composite because they have factor pairs beyond just 1 and themselves. Being odd is not sufficient to be prime — a number is prime only if it has NO divisors other than 1 and itself."

- question: "Every even number greater than 2 is composite."
  type: true-false
  answer: true
  explanation: "Any even number greater than 2 is divisible by 2, giving it at least three factors: 1, 2, and itself. Having three or more factors means it is composite by definition. The only even prime is 2 itself — it has exactly two factors (1 and 2) and is not divisible by any other whole number."

- question: "All odd numbers are prime numbers."
  type: true-false
  answer: false
  explanation: "Many odd numbers are composite. Examples: 9 = 3 × 3, 15 = 3 × 5, 21 = 3 × 7, 25 = 5 × 5. Being odd means the number is not divisible by 2 — but there are many other potential divisors. A number is only prime if it has NO divisors other than 1 and itself. Odd just rules out divisibility by 2; it doesn't rule out divisibility by 3, 5, 7, and so on."

- question: "Why is 1 classified as neither prime nor composite, rather than simply being the smallest prime?"
  type: short-answer
  answer: "Prime is defined as having exactly two factors: 1 and itself, where those are two different numbers. The number 1 has only one factor — itself — so it fails the prime definition. It also fails the composite definition, which requires more than two factors. Additionally, including 1 as prime would destroy the uniqueness of prime factorization: 12 could then be written as 2×2×3, or 1×2×2×3, or 1×1×2×2×3 — infinitely many ways."
  explanation: "The Fundamental Theorem of Arithmetic states that every whole number greater than 1 has exactly one prime factorization. This uniqueness is what makes primes so powerful in mathematics. Excluding 1 from 'prime' preserves this guarantee and is not an arbitrary decision — it's mathematically necessary."
```

## Explainer

You've already worked with factors and multiples, so you know that factors of a number are the whole numbers that divide into it evenly. **Prime** and **composite** are simply two categories based on how many factors a number has.

A **prime number** has exactly two factors: 1 and itself. Take 7: its only factors are 1 and 7. You cannot divide 7 evenly by 2, 3, 4, 5, or 6 — there's nothing in between. A prime number is, in a sense, indivisible (other than by 1 and itself). A **composite number** has three or more factors, meaning there's at least one other divisor. Take 12: its factors are 1, 2, 3, 4, 6, and 12 — six factors total. Equivalently, you can arrange 12 tiles into a 2 × 6 rectangle or a 3 × 4 rectangle, not just a 1 × 12 strip. Composite numbers can always be "broken apart" into smaller factor pairs.

The Sieve of Eratosthenes gives you a systematic way to find all primes up to 100. Start by crossing out 1 (not prime — only one factor). Circle 2 (prime), then cross out all multiples of 2. Circle 3, cross out all multiples of 3. Continue with 5 and 7. Everything left uncrossed is prime. The sieve reveals an important pattern: primes become rarer as numbers get larger, but they never stop appearing entirely.

Two special cases demand attention. First, **1 is neither prime nor composite** — it has exactly one factor (itself), which satisfies neither definition. This isn't a technicality to memorize blindly; it matters because the fundamental theorem of arithmetic says every whole number greater than 1 has a unique prime factorization. If 1 were prime, you could write 12 = 2 × 2 × 3 or 1 × 2 × 2 × 3 or 1 × 1 × 2 × 2 × 3, destroying the uniqueness. Second, **2 is the only even prime**. Every other even number is divisible by 2, giving it at least three factors. So 2 gets to be both even and prime — it's the one exception. Every prime after 2 is odd, but being odd does not make a number prime (9 = 3 × 3; 15 = 3 × 5).
