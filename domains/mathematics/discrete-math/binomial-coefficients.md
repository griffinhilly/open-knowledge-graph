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
status: draft
---

# Binomial Coefficients and Pascal's Triangle

## Core Idea
Binomial coefficients C(n,k) = n!/(k!(n-k)!) count the ways to choose k items from n items. These coefficients appear as entries in Pascal's triangle and satisfy the recursive property C(n,k) = C(n-1,k-1) + C(n-1,k). They also form the coefficients in the expansion of (a+b)^n.

## Explainer

You already know from combinations and selections that C(n,k) = n!/(k!(n-k)!) counts the number of ways to choose k items from n without regard to order. **Binomial coefficients** are exactly these counting numbers — the same formula, now given a geometric home in **Pascal's triangle**. Pascal's triangle arranges these values in a triangular grid: row n contains C(n,0), C(n,1), ..., C(n,n). The outermost entries are always 1 — there's exactly one way to choose nothing, and one way to choose everything — and every interior entry equals the sum of the two entries directly above it.

That addition rule has a beautiful combinatorial explanation, known as **Pascal's identity**: C(n,k) = C(n-1,k-1) + C(n-1,k). Imagine you have n objects and want to choose k. Pick one special object — call it "the red ball." Every size-k selection either includes the red ball or it does not. If it includes the red ball, you're choosing the remaining k-1 from the other n-1 objects: C(n-1,k-1) ways. If it excludes the red ball, you're choosing all k from the other n-1 objects: C(n-1,k) ways. These two cases are mutually exclusive and exhaustive, so their sum equals C(n,k). The triangle's rule is not just arithmetic — it encodes this logical split.

The most important application of binomial coefficients is the **binomial theorem**: (a+b)^n = Σ C(n,k) a^(n-k) b^k. To see why, expand (a+b)^n as the product of n copies of (a+b). Each term in the full expansion comes from picking either a or b from each factor. The coefficient of a^(n-k) b^k is exactly the number of ways to choose which k factors contribute b — which is C(n,k). The triangle's rows literally encode the expansion coefficients: row 2 gives 1, 2, 1 for (a+b)², row 3 gives 1, 3, 3, 1 for (a+b)³, and so on.

Pascal's triangle also harbors deeper patterns. The entries in each row sum to 2^n (the number of all subsets of an n-element set). The **hockey stick identity** — that summing a diagonal gives the entry one row below — corresponds to a counting argument about choosing from sets of growing size. These patterns are not coincidences; they each reflect a combinatorial identity provable by the same logic used for Pascal's identity. Binomial coefficients are the connective tissue between combinatorics, algebra, and probability, and recognizing them in new settings is a core skill in discrete mathematics.
