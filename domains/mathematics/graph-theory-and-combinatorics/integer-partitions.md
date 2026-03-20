---
id: integer-partitions
title: Integer Partitions and Partition Functions
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: generating-functions-intro
  type: soft
builds-toward:
- polya-enumeration-theorem
tags:
- combinatorics
- partitions
stage: formal-systems
status: draft
---

# Integer Partitions and Partition Functions

## Core Idea
An integer partition of n is a non-increasing sequence of positive integers summing to n; p(n) counts these. The generating function is ∏(1/(1-x^k)), revealing structure: partitions by largest part relate to conjugates via Ferrers diagrams, and p(n) has modular properties including Ramanujan congruences. Partitions connect combinatorics, number theory, and representation theory.

## Explainer

An **integer partition** of n is a way of writing n as a sum of positive integers where order does not matter. The partitions of 4, for example, are: 4, 3+1, 2+2, 2+1+1, 1+1+1+1 — five ways in total, so p(4) = 5. The convention of writing parts in non-increasing order (largest first) makes each partition unique. The **partition function** p(n) counts the number of such decompositions; it grows rapidly — p(10) = 42, p(50) = 204226, p(100) = 190569292 — and understanding its structure is a major theme in combinatorics and number theory.

The **Ferrers diagram** is the key visual tool. Represent a partition as a grid of dots: the first row has as many dots as the largest part, the second row as many as the second part, and so on. The partition 4+3+1 of 8 becomes three rows of lengths 4, 3, 1. Now rotate the diagram 90 degrees — read off the column lengths instead of the row lengths. This gives a new partition called the **conjugate**: the conjugate of 4+3+1 is 3+2+2+1 (column heights left to right). The Ferrers diagram makes this transformation concrete and bijective, proving immediately that the number of partitions of n with largest part k equals the number of partitions of n with exactly k parts.

Your prerequisite on **generating functions** unlocks the most powerful tool. Each factor 1/(1-xᵏ) = 1 + xᵏ + x²ᵏ + x³ᵏ + … encodes the choice of how many times part k appears. Multiplying infinitely many such factors together — one for each k = 1, 2, 3, … — the coefficient of xⁿ in the product ∏ₖ 1/(1-xᵏ) is exactly p(n). This is one of the most beautiful generating function identities: it converts a counting problem about additive decompositions into a product formula. Truncating the product gives a practical computation tool, and analyzing it algebraically reveals partition identities — the most famous being Euler's theorem that the number of partitions into odd parts equals the number of partitions into distinct parts.

The **Ramanujan congruences** are one of the most surprising results in all of mathematics: p(5k+4) ≡ 0 (mod 5), p(7k+5) ≡ 0 (mod 7), and p(11k+6) ≡ 0 (mod 11) for all k ≥ 0. That the partition function — a purely combinatorial quantity — should have such clean divisibility behavior by primes 5, 7, and 11 is completely non-obvious and was not proved in full generality until decades after Ramanujan conjectured it. Partitions connect directly to representation theory (partitions label irreducible representations of symmetric groups), to physics (partitions appear in the entropy of black holes and string theory), and forward to topics like Pólya enumeration, where counting under symmetry generalizes the ideas here.
