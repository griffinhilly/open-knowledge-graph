---
id: set-equality-and-extensionality
title: Set Equality and Extensionality
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: set-membership-and-notation
  type: hard
- id: extensionality-axiom
  type: soft
builds-toward:
- subset-proper-subset-relations
tags:
- equality
- extensionality
- foundation
stage: formal-systems
status: validated
---

# Set Equality and Extensionality

## Core Idea
Two sets are equal if and only if they contain exactly the same elements—the principle of extensionality. This means {1,2,3} = {3,2,1} and {x | x² = 4, x ∈ ℤ} = {-2,2}. Sets are completely determined by their membership, independent of how they are described.

## Explainer

You already know what set membership means: the statement x ∈ A says that x belongs to A. The **principle of extensionality** takes that single relationship and makes it the whole story. Two sets are equal — not just equivalent or interchangeable, but literally the same object — if and only if they have exactly the same members. Nothing else counts: not the name of the set, not the order elements were listed, not the description used to define it. The set *is* its extension.

This collapses many apparently different descriptions to the same set. Consider {1, 2, 3} and {3, 1, 2}. These look distinct in notation, but membership is the only test: is 1 in both? Yes. Is 2 in both? Yes. Is 3 in both? Yes. Is anything in either set that's not in the other? No. By extensionality, they are identical. Similarly, {x ∈ ℤ : x² = 4} and {-2, 2} are the same set — not because we *decided* to equate them, but because they have identical membership rosters. The **intension** (how we described it) is irrelevant; the **extension** (what's actually in it) is everything.

This principle also gives set equality a rigorous logical form. To prove A = B, you prove two biconditionals: for every x, x ∈ A if and only if x ∈ B. In practice this usually breaks into two directions — show A ⊆ B, then show B ⊆ A — a proof structure you will use constantly once you reach subset relations. Extensionality is what makes that strategy valid: if every member of A is in B and every member of B is in A, there is nothing left to distinguish them.

One subtle but important implication: the **empty set** is unique. There is only one set with no elements, because any two empty sets have the same (vacuous) membership roster. Extensionality makes ∅ a definite object, not a vague concept. This is one of the foundational reasons set theory, once axiomatized, can be precise enough to serve as a foundation for mathematics: equality between sets is fully determined by membership facts, and nothing else.

## Questions

```yaml
- question: "Which of the following sets is equal to {x ∈ ℤ : x² < 5}?"
  type: multiple-choice
  options:
    - "{0, 1, 2} — only positive integers whose squares are less than 5"
    - "{1, 4} — the squares that are less than 5"
    - "{-2, -1, 0, 1, 2} — all integers whose square is less than 5"
    - "{x : x < √5} — real numbers less than the square root of 5"
  answer: 2
  explanation: "Extensionality says sets are equal iff they have the same members. The integers x with x² < 5 are exactly -2, -1, 0, 1, 2 (since (-2)² = 4 < 5, but (-3)² = 9 ≥ 5). Option A misses the negative integers. Option B lists the values of x² rather than the values of x. Option D is a different set of real numbers. The description 'x ∈ ℤ such that x² < 5' and the enumeration {-2,-1,0,1,2} are different intensions but identical extensions."

- question: "A student argues that {x | x is a positive even number less than 10} and {2, 4, 6, 8} are different sets because one is defined by a rule and the other by explicit listing. The student's reasoning is:"
  type: multiple-choice
  options:
    - "Correct — the method of definition is part of a set's identity in formal set theory"
    - "Correct — the rule-defined set includes all even numbers less than 10, while the list is finite"
    - "Incorrect — by extensionality, sets with identical members are the same set regardless of description"
    - "Incorrect — but only because both are finite sets; infinite sets defined by rules can differ from enumerated sets"
  answer: 2
  explanation: "The principle of extensionality states that a set is completely determined by its members, not by the description used to define it. {x | x is a positive even number less than 10} and {2, 4, 6, 8} have exactly the same elements, so they are the same set — not just 'equivalent' or 'interchangeable' but literally identical as mathematical objects. The method of construction (rule vs. list) is an intensional property; extensionality is an axiom that discards it."

- question: "Two sets can have exactly the same elements but still be different sets if they were constructed using different methods or described differently."
  type: true-false
  answer: false
  explanation: "This is precisely what the axiom of extensionality denies. Sets have no 'identity' beyond their membership roster. {1, 2, 3}, {3, 1, 2}, {x ∈ ℕ : x ≤ 3}, and 'the set of positive integers not greater than 3' all refer to the same object in set theory. The construction method, the notation, and the name are all irrelevant — only the members determine the set. This is what makes set theory a clean foundation for mathematics."

- question: "The uniqueness of the empty set follows from extensionality: any two sets with no elements must be identical because they have the same (vacuous) membership roster."
  type: true-false
  answer: true
  explanation: "Suppose A and B are both empty sets. For any x: x ∈ A is vacuously false, and x ∈ B is vacuously false. So x ∈ A iff x ∈ B holds trivially for every x. By extensionality, A = B. This means we can speak of 'the' empty set (∅) rather than 'an' empty set — it is a unique, definite mathematical object. The axiom of extensionality is what licenses this definite article."

- question: "According to the principle of extensionality, what is the only criterion that determines whether two sets are equal, and why does this mean {1, 2, 3} = {3, 1, 2}?"
  type: short-answer
  answer: "Extensionality says two sets are equal if and only if they have exactly the same members — nothing else determines set identity. Order of listing is not a property of a set; sets are unordered collections. To check whether {1,2,3} = {3,1,2}: verify that every element of the first is in the second (1 ∈ {3,1,2}, 2 ∈ {3,1,2}, 3 ∈ {3,1,2} — yes) and every element of the second is in the first (same check, yes). Since membership is identical, they are the same set."
  explanation: "This is often surprising to students accustomed to thinking about ordered sequences. In set theory, {1,2,3} is not a sequence — it is a collection, and collections have no intrinsic ordering. Two notations 'listing' the same elements in different orders are two ways of writing the same thing, just as '2+1' and '1+2' are two ways of writing the number 3. Extensionality formalizes this intuition precisely."
```

## How It's Best Learned
Work through examples where the same set is specified multiple ways — a list, a rule, a complement — and practice verifying equality by checking membership in both directions. The discipline of writing "show A ⊆ B and B ⊆ A" builds the habit extensionality requires.
