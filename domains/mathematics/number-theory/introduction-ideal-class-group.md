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
status: validated
---

# Introduction to the Ideal Class Group

## Core Idea
The ideal class group measures how far a number ring departs from unique factorization. In rings of algebraic integers where elements may not factor uniquely, ideals always factor uniquely into prime ideals. Two ideals are equivalent if they differ by multiplication by a principal ideal. The class group is the quotient of fractional ideals by principal ideals, and its order—the class number h(K)—equals 1 precisely when the ring is a principal ideal domain with unique factorization. Computing class numbers reveals the arithmetic complexity of number fields and connects to deep results in algebraic number theory.

## How It's Best Learned
Work through ℤ[√−5], where 6 = 2 · 3 = (1+√−5)(1−√−5) shows factorization failure. Then verify that ideal factorization restores uniqueness and compute that h = 2, making the class group ℤ/2ℤ.

## Common Misconceptions
The class group is not about individual elements failing to factor—it is about the global structure of ideals. Students sometimes think unique factorization fails "everywhere" when h > 1, but many elements still factor uniquely; it is the exceptions that the class group quantifies.

## Explainer

From your study of the failure of unique factorization, you know that some rings of algebraic integers do not behave like ℤ. In ℤ[√−5], the equation 6 = 2 · 3 = (1 + √−5)(1 − √−5) gives two genuinely distinct factorizations into irreducibles — the ring is not a unique factorization domain. The **ideal class group** is the algebraic object that measures exactly how badly unique factorization fails. It does not just say "factorization is broken" — it quantifies the structural obstruction and organizes it into a group.

The key insight from your study of ideals is that while elements may not factor uniquely, **ideals always do** in a Dedekind domain (which every ring of algebraic integers is). In ℤ[√−5], the ideals (2), (3), (1 + √−5), and (1 − √−5) are not prime ideals, but each can be factored uniquely into products of prime ideals. For instance, (2) = 𝔭₁² where 𝔭₁ = (2, 1 + √−5) is a prime ideal. The passage from elements to ideals restores unique factorization — the problem is not that factorization is impossible, but that it happens at the level of ideals rather than elements.

Two fractional ideals I and J are declared **equivalent** if I = αJ for some nonzero element α of the field — that is, they differ by multiplication by a principal ideal. The equivalence classes form a group under ideal multiplication, called the **ideal class group** Cl(K). The identity element is the class of principal ideals (those of the form (α) for some element α). The **class number** h(K) = |Cl(K)| counts how many equivalence classes there are. The critical fact is: h(K) = 1 if and only if every ideal is principal, which happens if and only if the ring is a PID, which for Dedekind domains is equivalent to being a UFD. So h(K) = 1 is the precise algebraic condition for unique factorization to hold.

For ℤ[√−5], the class group is ℤ/2ℤ, so h = 2. There are exactly two ideal classes: the principal ideals and one non-trivial class represented by 𝔭₁ = (2, 1 + √−5). The non-unique factorization of 6 is a direct consequence: the prime ideal factorization of (6) passes through non-principal ideals, so the factorization at the ideal level cannot be "lifted" to a unique factorization at the element level. Computing class numbers for specific number fields — using Minkowski's bound to reduce the computation to finitely many ideals — is one of the central practical tasks of algebraic number theory and connects to deep results including the analytic class number formula involving L-functions.

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

- question: "In a ring of algebraic integers with h(K) > 1, most element fails to factor uniquely into irreducibles."
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

