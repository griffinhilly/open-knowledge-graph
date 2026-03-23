---
id: cardinality-and-countability
title: Cardinality and Countability
domain: mathematics
course: discrete-math
prerequisites:
- id: set-relations-functions-discrete
  type: hard
builds-toward:
- generating-functions-basics
tags:
- cardinality
- countability
- infinite-sets
- bijection
stage: formal-systems
status: validated
---

# Cardinality and Countability

## Core Idea
Cardinality measures set size; finite sets have cardinalities like 3 or 100, while infinite sets can be countably infinite (same cardinality as ℕ) or uncountably infinite (like ℝ). Two sets have equal cardinality if a bijection exists between them.

## How It's Best Learned
Use bijections to show equal cardinality. Recognize that ℤ, ℚ are countable but ℝ is not. Understand Cantor's diagonalization argument.

## Common Misconceptions
Not all infinities are equal; uncountable infinities are 'larger' than countable ones. A set with cardinality equal to ℕ is still infinite but countable.

## Questions

```yaml
- question: "Which of the following sets has the same cardinality as the natural numbers ℕ?"
  type: multiple-choice
  options: ["The real numbers ℝ", "The power set of ℕ", "The rational numbers ℚ", "The set of all infinite subsets of ℕ"]
  answer: 2
  explanation: "ℚ is countably infinite — there is a bijection between ℚ and ℕ (e.g., via a diagonal enumeration of fractions). ℝ and the power set of ℕ are both uncountably infinite, with strictly larger cardinality than ℕ. This surprises students who expect ℚ to be 'larger' because it is dense on the number line."

- question: "The set of even integers {0, 2, 4, 6, ...} has strictly smaller cardinality than the set of all natural numbers ℕ because it is only half as large."
  type: true-false
  answer: false
  explanation: "Cardinality is determined by whether a bijection exists, not by 'how many' elements seem present intuitively. The function f(n) = 2n maps every natural number to a unique even integer and covers all even integers, so the two sets have equal cardinality. This is one of the defining — and counterintuitive — features of infinite sets."

- question: "Describe the key idea behind Cantor's diagonalization argument and what it proves about ℝ."
  type: short-answer
  answer: "Cantor's diagonal argument shows that no list can enumerate all real numbers in [0,1]. Given any proposed list, you construct a new real number by changing the nth digit of the nth entry, guaranteeing it differs from every entry on the list. This proves ℝ is uncountable — its cardinality is strictly greater than that of ℕ."
  explanation: "The argument is a proof by contradiction: assume a bijection exists between ℕ and ℝ, then construct an element of ℝ not in the image of that bijection. The diagonal construction makes the contradiction concrete and irrefutable."
```

## Explainer

When you first learned about sets, size seemed simple: count the elements. But what does 'size' mean for infinite sets? The key insight is to separate the question of size from the question of counting. Two sets are defined to have the same cardinality if a bijection exists between them — a one-to-one correspondence that pairs every element of one set with exactly one element of the other, with nothing left over.

This definition produces a striking result: the set of even integers has the same cardinality as the set of all integers, which has the same cardinality as the rational numbers ℚ. In each case you can exhibit an explicit bijection. For even integers and ℕ, the map n ↦ 2n works perfectly. For ℤ and ℕ, interleave positives and negatives: 0, 1, -1, 2, -2, .... For ℚ, use the diagonal enumeration of fractions p/q — arrange them in a grid and sweep diagonally, skipping duplicates. Any set that can be put into bijection with ℕ is called countably infinite.

Not all infinite sets are countable. Georg Cantor proved that the real numbers ℝ cannot be listed in any sequence. The argument is elegant: suppose you have any purported list of all reals in [0,1]. Construct a new real number by taking the nth decimal digit of the nth entry and changing it. The number you construct differs from every entry on the list at at least one decimal place — so it is a real number your list missed. Since this works for any list, no list can be complete. ℝ is uncountably infinite, and its cardinality (written |ℝ| or 2^ℵ₀) is strictly larger than ℵ₀ (the cardinality of ℕ).

This means there is a genuine hierarchy of infinities. The integers and rationals sit at the bottom, all sharing cardinality ℵ₀. The reals, the complex numbers, and the set of all functions from ℕ to ℕ all sit at a higher level. Cantor went further and proved there is no largest infinity — for any infinite set S, the power set 𝒫(S) always has strictly greater cardinality than S itself.

The practical takeaway for formal mathematics and computer science is this: countably infinite sets are the ones you can in principle enumerate with a program. If a set is countable, you can write a loop that will eventually reach any element. Uncountable sets — like the reals — cannot be enumerated by any algorithm, which has deep consequences for computability theory and the limits of what programs can do.
