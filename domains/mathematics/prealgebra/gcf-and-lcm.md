---
id: gcf-and-lcm
title: Greatest Common Factor and Least Common Multiple
domain: mathematics
course: prealgebra
prerequisites:
  - id: factors-and-multiples
    type: hard
  - id: prime-and-composite-numbers
    type: hard
  - id: multiples-of-a-number
    type: soft
builds-toward:
  - factoring-gcf
  - adding-fractions-unlike-denominators
tags: [number-theory, factors, multiples, gcf, lcm, arithmetic]
stage: abstract-reasoning
status: validated
---

# Greatest Common Factor and Least Common Multiple

## Core Idea
The greatest common factor (GCF) of two whole numbers is the largest number that divides both of them. The least common multiple (LCM) is the smallest positive number that both of them divide. For 12 and 18 the GCF is 6 and the LCM is 36. The GCF is used to simplify fractions and to factor expressions; the LCM gives the least common denominator and solves "when do two cycles line up again" problems.

## How It's Best Learned
Begin with lists: write the factors of each number and circle the shared ones, then write multiples of each until one repeats. Move to prime factorization, where the GCF takes the shared primes with the smaller exponent and the LCM takes every prime with the larger exponent. Use word problems that force a choice between the two (splitting items into equal groups versus finding when events coincide).

## Common Misconceptions
- The LCM of two numbers is always their product. (That is true only when the numbers share no factor other than 1; the LCM of 4 and 6 is 12, not 24.)
- The GCF must be smaller than both numbers. (The GCF can equal one of the numbers, as with GCF(5, 15) = 5.)
- GCF and LCM problems can be told apart by the size of the answer alone. (Read the situation: sharing or grouping points to the GCF, repeating schedules point to the LCM.)
- Two numbers with no common prime factor have no GCF. (Their GCF is 1, and such numbers are called relatively prime.)

## Questions

```yaml
- question: "What is the least common multiple of 4 and 6?"
  type: multiple-choice
  options: ["2", "10", "12", "24"]
  answer: 2
  explanation: "Multiples of 4 are 4, 8, 12, 16, ... and multiples of 6 are 6, 12, 18, ... The first shared multiple is 12. The product 24 is a common multiple but not the least one, because 4 and 6 share the factor 2."

- question: "The LCM of two whole numbers is always equal to their product."
  type: true-false
  answer: false
  explanation: "The product is a common multiple, but it is the least one only when the numbers share no factor other than 1. For 4 and 6 the product is 24 while the LCM is 12."

- question: "Using prime factorizations 12 = 2² × 3 and 18 = 2 × 3², find the GCF and the LCM of 12 and 18."
  type: short-answer
  answer: "GCF = 2 × 3 = 6; LCM = 2² × 3² = 36"
  explanation: "The GCF takes each shared prime to the smaller power (2¹ and 3¹). The LCM takes each prime that appears to the larger power (2² and 3²). As a check, GCF × LCM = 6 × 36 = 216 = 12 × 18."

- question: "A teacher has 24 pencils and 36 erasers and wants identical kits with nothing left over. What is the greatest number of kits she can make?"
  type: multiple-choice
  options: ["6", "12", "72", "60"]
  answer: 1
  explanation: "Each kit count must divide both 24 and 36, so the largest number of kits is GCF(24, 36) = 12. Each kit then holds 2 pencils and 3 erasers. 72 is the LCM, which answers a different kind of question."
```

## Explainer

Every whole number greater than 1 has factors (numbers that divide it exactly) and multiples (numbers it divides exactly). When two numbers are involved, it is natural to ask which factors they share and which multiples they share. The greatest common factor and the least common multiple are the extreme answers to those two questions.

Start with listing. The factors of 12 are 1, 2, 3, 4, 6 and 12. The factors of 18 are 1, 2, 3, 6, 9 and 18. The shared factors are 1, 2, 3 and 6, so GCF(12, 18) = 6. For multiples, list 12, 24, 36, 48 and 18, 36, 54. The first shared multiple is 36, so LCM(12, 18) = 36.

Listing works for small numbers, but prime factorization is faster and shows why the answers come out as they do. Write 12 = 2² × 3 and 18 = 2 × 3². A common factor can only use primes that both numbers contain, and no more copies than either one has. So the GCF uses 2¹ and 3¹, giving 6. A common multiple must contain everything in each number, so the LCM uses 2² and 3², giving 36.

Notice that 6 × 36 = 216 and 12 × 18 = 216. For any two positive whole numbers, the GCF times the LCM equals the product of the numbers. This explains why the LCM equals the product only when the GCF is 1. Numbers like 8 and 15, whose GCF is 1, are called relatively prime.

The two ideas answer different kinds of questions. If you are splitting things into identical groups with nothing left over, you want a number that divides every amount, so you want the GCF. If you are asking when two repeating events happen together again, such as a bus every 12 minutes and a train every 18 minutes, you want a number that every cycle divides, so you want the LCM: they meet again after 36 minutes.

Both ideas come back often. The GCF reduces 12/18 to 2/3 in one step, and in algebra it becomes the first move in factoring, as in 12x + 18 = 6(2x + 3). The LCM of the denominators is the least common denominator used to add fractions such as 1/12 + 1/18 = 3/36 + 2/36 = 5/36.
