---
id: integer-partitions
title: Integer Partitions and Partition Functions
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: generating-functions-intro
  type: soft
- id: exponential-generating-functions
  type: soft
builds-toward:
- polya-enumeration-theorem
tags:
- combinatorics
- partitions
stage: formal-systems
status: validated
---
# Integer Partitions and Partition Functions

## Core Idea
An integer partition of n is a non-increasing sequence of positive integers summing to n; p(n) counts these. The generating function is ∏(1/(1-x^k)), revealing structure: partitions by largest part relate to conjugates via Ferrers diagrams, and p(n) has modular properties including Ramanujan congruences. Partitions connect combinatorics, number theory, and representation theory.

## Questions

```yaml
- question: "How many partitions does the integer 5 have?"
  type: multiple-choice
  options:
    - "5"
    - "6"
    - "7"
    - "8"
  answer: 2
  explanation: "The partitions of 5 are: 5; 4+1; 3+2; 3+1+1; 2+2+1; 2+1+1+1; 1+1+1+1+1 — seven in total, so p(5) = 7. A common error is to count only the 'most obvious' decompositions (into two parts, etc.) and miss the cases with many small parts or the partition consisting of the number itself. Listing systematically by largest part avoids omissions."

- question: "The Ferrers diagram of the partition 4+2+1 of 7 is conjugated (reflected along its main diagonal). Which partition results?"
  type: multiple-choice
  options:
    - "1+2+4 — the parts of the original, reversed in order"
    - "3+2+1+1 — reading column heights left to right from the original diagram"
    - "7 — all parts collapsed into a single row"
    - "4+2+1 — this partition is self-conjugate"
  answer: 1
  explanation: "The Ferrers diagram of 4+2+1 has rows of length 4, 2, and 1. Reading the column heights left-to-right: column 1 has 3 dots (three rows have at least 1), column 2 has 2 dots (two rows have at least 2), column 3 has 1 dot (one row has at least 3), column 4 has 1 dot (one row has at least 4). This gives 3+2+1+1. Option A is a common confusion between reversing parts and taking the conjugate; the conjugate reads columns, not rows in reverse."

- question: "The coefficient of x^n in the infinite product ∏(1/(1−x^k)) for k = 1, 2, 3, … equals p(n), the number of partitions of n."
  type: true-false
  answer: true
  explanation: "Each factor 1/(1−x^k) = 1 + x^k + x^(2k) + … encodes how many times part k appears (0, 1, 2, … times). Multiplying over all k = 1, 2, 3, … collects every combination of parts summing to n in the coefficient of x^n. This generating function identity converts the partition-counting problem into a product formula, one of the most powerful tools for studying p(n)."

- question: "The Ramanujan congruences state that p(n) is divisible by 5 for nearly every positive integer n."
  type: true-false
  answer: false
  explanation: "The Ramanujan congruence for the prime 5 states p(5k+4) ≡ 0 (mod 5) — divisibility holds only when n ≡ 4 (mod 5). For example, p(4) = 5, p(9) = 30, p(14) = 135, each divisible by 5; but p(1) = 1 and p(2) = 2 are not. The surprise is that such a clean modular pattern exists at all for a combinatorial quantity — not that every value is divisible."

- question: "What is the conjugate of a partition, and what theorem does the Ferrers diagram immediately prove about conjugates?"
  type: short-answer
  answer: "The conjugate of a partition is obtained by transposing its Ferrers diagram — reading the column lengths instead of the row lengths. This gives a new partition of the same integer. The Ferrers diagram immediately proves that the number of partitions of n with largest part equal to k equals the number of partitions of n with exactly k parts, because taking the conjugate is a bijection that swaps 'largest part' with 'number of parts.'"
  explanation: "The bijective proof via conjugation is a prototype of the combinatorial proof technique: instead of computing two quantities separately and showing they're equal, you exhibit a one-to-one correspondence between the two sets. The Ferrers diagram makes this correspondence visual and concrete — rotating the grid 90° is the bijection."
```

## Explainer

An **integer partition** of n is a way of writing n as a sum of positive integers where order does not matter. The partitions of 4, for example, are: 4, 3+1, 2+2, 2+1+1, 1+1+1+1 — five ways in total, so p(4) = 5. The convention of writing parts in non-increasing order (largest first) makes each partition unique. The **partition function** p(n) counts the number of such decompositions; it grows rapidly — p(10) = 42, p(50) = 204226, p(100) = 190569292 — and understanding its structure is a major theme in combinatorics and number theory.

The **Ferrers diagram** is the key visual tool. Represent a partition as a grid of dots: the first row has as many dots as the largest part, the second row as many as the second part, and so on. The partition 4+3+1 of 8 becomes three rows of lengths 4, 3, 1. Now rotate the diagram 90 degrees — read off the column lengths instead of the row lengths. This gives a new partition called the **conjugate**: the conjugate of 4+3+1 is 3+2+2+1 (column heights left to right). The Ferrers diagram makes this transformation concrete and bijective, proving immediately that the number of partitions of n with largest part k equals the number of partitions of n with exactly k parts.

Your prerequisite on **generating functions** unlocks the most powerful tool. Each factor 1/(1-xᵏ) = 1 + xᵏ + x²ᵏ + x³ᵏ + … encodes the choice of how many times part k appears. Multiplying infinitely many such factors together — one for each k = 1, 2, 3, … — the coefficient of xⁿ in the product ∏ₖ 1/(1-xᵏ) is exactly p(n). This is one of the most beautiful generating function identities: it converts a counting problem about additive decompositions into a product formula. Truncating the product gives a practical computation tool, and analyzing it algebraically reveals partition identities — the most famous being Euler's theorem that the number of partitions into odd parts equals the number of partitions into distinct parts.

The **Ramanujan congruences** are one of the most surprising results in all of mathematics: p(5k+4) ≡ 0 (mod 5), p(7k+5) ≡ 0 (mod 7), and p(11k+6) ≡ 0 (mod 11) for all k ≥ 0. That the partition function — a purely combinatorial quantity — should have such clean divisibility behavior by primes 5, 7, and 11 is completely non-obvious and was not proved in full generality until decades after Ramanujan conjectured it. Partitions connect directly to representation theory (partitions label irreducible representations of symmetric groups), to physics (partitions appear in the entropy of black holes and string theory), and forward to topics like Pólya enumeration, where counting under symmetry generalizes the ideas here.
