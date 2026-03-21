---
id: introduction-ideal-class-group
title: Introduction to the Ideal Class Group
domain: mathematics
course: number-theory
prerequisites:
- id: failure-unique-factorization
  type: hard
- id: subrings-and-ideals
  type: hard
tags:
- ideal-class-group
- algebraic-number-theory
stage: advanced
status: draft
---

# Introduction to the Ideal Class Group

## Core Idea
The ideal class group measures how far a number ring departs from unique factorization. In rings of algebraic integers where elements may not factor uniquely, ideals always factor uniquely into prime ideals. Two ideals are equivalent if they differ by multiplication by a principal ideal. The class group is the quotient of fractional ideals by principal ideals, and its order—the class number h(K)—equals 1 precisely when the ring is a principal ideal domain with unique factorization. Computing class numbers reveals the arithmetic complexity of number fields and connects to deep results in algebraic number theory.

## How It's Best Learned
Work through ℤ[√−5], where 6 = 2 · 3 = (1+√−5)(1−√−5) shows factorization failure. Then verify that ideal factorization restores uniqueness and compute that h = 2, making the class group ℤ/2ℤ.

## Common Misconceptions
The class group is not about individual elements failing to factor—it is about the global structure of ideals. Students sometimes think unique factorization fails "everywhere" when h > 1, but many elements still factor uniquely; it is the exceptions that the class group quantifies.

## Questions

```yaml
- question: "In ℤ[√−5], we have 6 = 2·3 = (1+√−5)(1−√−5). What does this tell us about the ideal class group of ℤ[√−5]?"
  type: multiple-choice
  options:
    - "The class group is trivial (h = 1), because 6 has a factorization"
    - "The class group is nontrivial (h > 1), because element factorization is not unique"
    - "The class group is nontrivial (h > 1), because ideal factorization also fails in this ring"
    - "Nothing — the class group is defined for fields, not rings"
  answer: 1
  explanation: "The non-unique factorization of 6 as an element signals that ℤ[√−5] is not a unique factorization domain, hence not a principal ideal domain, hence h > 1. The class group for ℤ[√−5] is ℤ/2ℤ, so h = 2. Note that option C is wrong: ideal factorization into prime ideals is always unique — that is precisely what ideals restore. The class group measures the failure at the element level via the structure of ideals, not a failure of ideal factorization."

- question: "A number ring has class number h(K) = 1. Which conclusion follows?"
  type: multiple-choice
  options:
    - "Every nonzero element factors uniquely into irreducibles"
    - "The ring has no prime ideals"
    - "Every ideal is principal, so the ring is a PID with unique factorization"
    - "The ring contains no zero divisors"
  answer: 2
  explanation: "h(K) = 1 means every fractional ideal is principal — the class group is trivial. For rings of algebraic integers, being a PID is equivalent to being a UFD, so h = 1 is the precise condition for unique factorization to hold. Option A sounds correct but is the consequence, not the definition: the PID property is the direct interpretation of h = 1, and unique factorization follows from it."

- question: "In a ring of algebraic integers with h(K) > 1, every element fails to factor uniquely into irreducibles."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about the ideal class group. When h > 1, the ring is not a UFD, meaning unique factorization fails for *some* elements — but many elements still factor uniquely. The class group quantifies the global obstruction to unique factorization; it is not a statement that every element is problematic. In ℤ[√−5] with h = 2, for example, the element 5 = (√−5)² factors uniquely, while 6 = 2·3 = (1+√−5)(1−√−5) does not."

- question: "If two ideals I and J satisfy I = (α)J for some element α, then I and J represent the same element of the ideal class group."
  type: true-false
  answer: true
  explanation: "The ideal class group is defined by declaring two fractional ideals equivalent when they differ by multiplication by a principal ideal (α). This equivalence relation defines the classes: I ~ J iff I = (α)J for some nonzero α. The group operation is ideal multiplication, and the identity element is the class of principal ideals. The fact that principal ideals form the trivial class is exactly why h = 1 means 'everything is principal.'"

- question: "Why do ideals restore unique factorization in rings where elements do not factor uniquely, and what does the class group measure about this restoration?"
  type: short-answer
  answer: "In a Dedekind domain (which rings of algebraic integers are), every nonzero ideal factors uniquely into prime ideals — even when elements do not factor uniquely. The obstruction to element-level unique factorization is that some ideals are not principal: a 'missing' element factorization corresponds to a factorization of ideals that cannot be expressed as products of principal ideals. The class group — fractional ideals modulo principal ideals — measures exactly how many 'non-principal' equivalence classes exist. h(K) = 1 means every ideal is principal, collapsing ideal factorization and element factorization into the same thing."
  explanation: "The key insight is the two-level structure: ideals always factor uniquely (Dedekind domain property), but elements factor uniquely only when every ideal is principal. The class group is the gap between these two levels. A class number of 2 means there is one non-trivial equivalence class of ideals that lacks a principal representative — and this is what causes element factorization to fail in specific cases like 6 in ℤ[√−5]."
```

