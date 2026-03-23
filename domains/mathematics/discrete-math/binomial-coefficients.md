---
id: binomial-coefficients
title: Binomial Coefficients and Pascal's Triangle
domain: mathematics
course: discrete-math
prerequisites:
- id: combinations-and-selections
  type: hard
builds-toward:
- binomial-theorem
- multinomial-theorem
tags:
- combinatorics
- binomial
stage: formal-systems
status: validated
---

# Binomial Coefficients and Pascal's Triangle

## Core Idea
Binomial coefficients C(n,k) = n!/(k!(n-k)!) count the ways to choose k items from n items. These coefficients appear as entries in Pascal's triangle and satisfy the recursive property C(n,k) = C(n-1,k-1) + C(n-1,k). They also form the coefficients in the expansion of (a+b)^n.

## Questions

```yaml
- question: "Pascal's identity states that C(5,2) = C(4,1) + C(4,2). Which explanation best captures why this is true?"
  type: multiple-choice
  options:
    - "It is a coincidence that holds for small values but breaks down for large n"
    - "Every 2-element selection from 5 items either includes a designated special item (needing C(4,1) additional choices) or excludes it (needing C(4,2) choices from the rest)"
    - "Pascal's triangle is defined by adding adjacent entries as an arithmetic rule, with no deeper meaning"
    - "The factorial formula simplifies algebraically to the sum of the two smaller values"
  answer: 1
  explanation: "This is the combinatorial proof of Pascal's identity. Designate any one item as 'special.' Every 2-item selection either includes or excludes it. If it includes the special item, you choose 1 more from 4: C(4,1) ways. If it excludes it, you choose 2 from 4: C(4,2) ways. These cases are mutually exclusive and exhaustive, so they sum to C(5,2). Option D is true but misses the point — the algebraic fact follows from combinatorial logic, not the other way around."

- question: "A student expanding (a+b)⁴ needs the coefficient of a²b². They identify it as C(4,2) = 6. What is the best explanation for why C(4,2) is correct?"
  type: multiple-choice
  options:
    - "It is the entry in row 4, position 2 of Pascal's triangle — which is true by definition of the triangle"
    - "Expanding (a+b)⁴ means choosing a or b from each of 4 factors; the term a²b² requires choosing b from exactly 2 of the 4 factors, and there are C(4,2) ways to make that choice"
    - "The coefficients must be symmetric and peak in the middle, so the middle terms of a degree-4 expansion are automatically largest"
    - "The formula 4!/(2!2!) = 6 holds by algebraic necessity, with no combinatorial interpretation"
  answer: 1
  explanation: "The binomial theorem connects combination-counting to polynomial expansion. Expanding (a+b)⁴ = (a+b)(a+b)(a+b)(a+b) means choosing a or b from each factor independently. To produce a²b², you need to choose b from exactly 2 of the 4 factors. The number of ways to pick which 2 factors contribute b is — by definition — C(4,2) = 6. This is the same counting argument that defines C(n,k) in the first place."

- question: "The sum of all entries in row n of Pascal's triangle equals 2^n, because it counts all subsets of an n-element set."
  type: true-false
  answer: true
  explanation: "The entries in row n are C(n,0) + C(n,1) + ... + C(n,n). Each C(n,k) counts the k-element subsets. Summing over all k gives the total number of subsets of an n-element set, which is 2^n — each element is either included or excluded, giving 2 independent binary choices for n items. The explainer notes this explicitly as one of Pascal's triangle's deeper patterns, each of which reflects a combinatorial identity."

- question: "Pascal's identity C(n,k) = C(n-1,k-1) + C(n-1,k) can only be verified by algebraic manipulation of the factorial formula — it has no intuitive combinatorial explanation."
  type: true-false
  answer: false
  explanation: "Pascal's identity has a direct combinatorial proof: designate any one object as 'special.' Any k-element selection either includes the special object — leaving C(n-1,k-1) ways to complete it — or excludes it, leaving C(n-1,k) ways to choose all k from the remaining n-1. These cases are mutually exclusive and exhaustive, so they sum to C(n,k). The arithmetic addition rule in Pascal's triangle encodes this logical split. Algebraic verification follows from the combinatorial reality, not the reverse."

- question: "Why do binomial coefficients appear both as entries in Pascal's triangle and as the coefficients in the expansion of (a+b)^n?"
  type: short-answer
  answer: "Because both contexts are counting the same thing: the number of ways to choose k items from n. In Pascal's triangle, C(n,k) is defined as the number of k-element selections from n objects. In the binomial expansion, C(n,k) appears as the coefficient of a^(n-k)b^k because the term a^(n-k)b^k arises when b is chosen from exactly k of the n factors of (a+b)^n — and the number of ways to choose which k factors contribute b is, by definition, C(n,k)."
  explanation: "The triangle and the expansion are not two separate facts that happen to share the same numbers — they reflect the same combinatorial structure. Recognizing binomial coefficients in new settings (probability, polynomial algebra, combinatorial identities) is a core skill in discrete mathematics precisely because the underlying counting argument is the same in all of them."
```

## Explainer

You already know from combinations and selections that C(n,k) = n!/(k!(n-k)!) counts the number of ways to choose k items from n without regard to order. **Binomial coefficients** are exactly these counting numbers — the same formula, now given a geometric home in **Pascal's triangle**. Pascal's triangle arranges these values in a triangular grid: row n contains C(n,0), C(n,1), ..., C(n,n). The outermost entries are always 1 — there's exactly one way to choose nothing, and one way to choose everything — and every interior entry equals the sum of the two entries directly above it.

That addition rule has a beautiful combinatorial explanation, known as **Pascal's identity**: C(n,k) = C(n-1,k-1) + C(n-1,k). Imagine you have n objects and want to choose k. Pick one special object — call it "the red ball." Every size-k selection either includes the red ball or it does not. If it includes the red ball, you're choosing the remaining k-1 from the other n-1 objects: C(n-1,k-1) ways. If it excludes the red ball, you're choosing all k from the other n-1 objects: C(n-1,k) ways. These two cases are mutually exclusive and exhaustive, so their sum equals C(n,k). The triangle's rule is not just arithmetic — it encodes this logical split.

The most important application of binomial coefficients is the **binomial theorem**: (a+b)^n = Σ C(n,k) a^(n-k) b^k. To see why, expand (a+b)^n as the product of n copies of (a+b). Each term in the full expansion comes from picking either a or b from each factor. The coefficient of a^(n-k) b^k is exactly the number of ways to choose which k factors contribute b — which is C(n,k). The triangle's rows literally encode the expansion coefficients: row 2 gives 1, 2, 1 for (a+b)², row 3 gives 1, 3, 3, 1 for (a+b)³, and so on.

Pascal's triangle also harbors deeper patterns. The entries in each row sum to 2^n (the number of all subsets of an n-element set). The **hockey stick identity** — that summing a diagonal gives the entry one row below — corresponds to a counting argument about choosing from sets of growing size. These patterns are not coincidences; they each reflect a combinatorial identity provable by the same logic used for Pascal's identity. Binomial coefficients are the connective tissue between combinatorics, algebra, and probability, and recognizing them in new settings is a core skill in discrete mathematics.
