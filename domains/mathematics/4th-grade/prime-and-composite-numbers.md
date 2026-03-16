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

## Explainer

You've already worked with factors and multiples, so you know that factors of a number are the whole numbers that divide into it evenly. **Prime** and **composite** are simply two categories based on how many factors a number has.

A **prime number** has exactly two factors: 1 and itself. Take 7: its only factors are 1 and 7. You cannot divide 7 evenly by 2, 3, 4, 5, or 6 — there's nothing in between. A prime number is, in a sense, indivisible (other than by 1 and itself). A **composite number** has three or more factors, meaning there's at least one other divisor. Take 12: its factors are 1, 2, 3, 4, 6, and 12 — six factors total. Equivalently, you can arrange 12 tiles into a 2 × 6 rectangle or a 3 × 4 rectangle, not just a 1 × 12 strip. Composite numbers can always be "broken apart" into smaller factor pairs.

The Sieve of Eratosthenes gives you a systematic way to find all primes up to 100. Start by crossing out 1 (not prime — only one factor). Circle 2 (prime), then cross out all multiples of 2. Circle 3, cross out all multiples of 3. Continue with 5 and 7. Everything left uncrossed is prime. The sieve reveals an important pattern: primes become rarer as numbers get larger, but they never stop appearing entirely.

Two special cases demand attention. First, **1 is neither prime nor composite** — it has exactly one factor (itself), which satisfies neither definition. This isn't a technicality to memorize blindly; it matters because the fundamental theorem of arithmetic says every whole number greater than 1 has a unique prime factorization. If 1 were prime, you could write 12 = 2 × 2 × 3 or 1 × 2 × 2 × 3 or 1 × 1 × 2 × 2 × 3, destroying the uniqueness. Second, **2 is the only even prime**. Every other even number is divisible by 2, giving it at least three factors. So 2 gets to be both even and prime — it's the one exception. Every prime after 2 is odd, but being odd does not make a number prime (9 = 3 × 3; 15 = 3 × 5).
