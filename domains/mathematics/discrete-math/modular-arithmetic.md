---
id: modular-arithmetic
title: Modular Arithmetic and Congruences
domain: mathematics
course: discrete-math
prerequisites:
- id: divisibility-and-gcd
  type: hard
- id: euclidean-algorithm
  type: soft
- id: equivalence-relations
  type: soft
builds-toward:
- chinese-remainder-theorem
tags:
- modular-arithmetic
- congruence
- residue-classes
- clock-arithmetic
- modular-inverse
stage: formal-systems
status: validated
---

# Modular Arithmetic and Congruences

## Core Idea
Two integers a and b are congruent modulo n (written a ≡ b (mod n)) if n divides their difference a − b. Congruence is an equivalence relation that partitions the integers into n residue classes forming the ring ℤₙ. Addition, subtraction, and multiplication all respect congruence. A multiplicative inverse of a mod n exists if and only if gcd(a,n) = 1, and can be computed via the extended Euclidean algorithm. Fast exponentiation (repeated squaring) computes aᵏ mod n efficiently, underpinning RSA encryption.

## How It's Best Learned
Use clock arithmetic (mod 12) as an entry point — familiar from daily life. Practice reducing large expressions mod n, then computing modular inverses and powers. Carefully work through cases where inverses do not exist to understand the role of the gcd condition.

## Common Misconceptions
- Dividing both sides of a congruence by d without verifying gcd(d,n) = 1 first — this is a common error that gives wrong results.
- Assuming every nonzero element has a multiplicative inverse mod n — only elements coprime to n do.
- Confusing the expression a mod n = r with the congruence statement a ≡ r (mod n).
