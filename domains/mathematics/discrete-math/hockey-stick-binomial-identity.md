---
id: hockey-stick-binomial-identity
title: Hockey Stick Identity
domain: mathematics
course: discrete-math
prerequisites:
- id: binomial-coefficients
  type: hard
- id: double-counting-principle
  type: soft
tags:
- combinatorics
- binomial-coefficients
- identities
stage: formal-systems
status: validated
---

# Hockey Stick Identity

## Core Idea
The hockey stick identity (also called Pascal's identity summed) states Σ C(n+i, i) = C(n+r+1, r) for non-negative integers. It gets its name from the shape traced in Pascal's triangle and is proven using combinatorial arguments or induction.

## Questions

```yaml
- question: "A student verifies the hockey stick identity C(2,2) + C(3,2) + C(4,2) = C(5,3) by computing 1 + 3 + 6 = 10 = C(5,3) and declares the identity proved. What is the limitation of this approach?"
  type: multiple-choice
  options:
    - "The arithmetic is wrong — 1 + 3 + 6 does not equal 10"
    - "Numerical verification confirms a specific instance but does not explain why the identity must hold for all valid n and r"
    - "This method cannot be extended to r = 2 for larger n"
    - "The student should trace the hockey stick shape in Pascal's triangle instead of computing directly"
  answer: 1
  explanation: "Checking one case confirms the identity holds there, but mathematics requires a proof that works for all n and r. The double-counting proof answers 'why' by showing both sides count the same set of objects — a level of explanation numerical verification cannot provide."

- question: "In the double-counting proof of the hockey stick identity, why is conditioning on the largest element chosen the key move?"
  type: multiple-choice
  options:
    - "To reduce the problem to a smaller instance using strong induction on n"
    - "Because the largest element uniquely determines the rest of the subset"
    - "Because fixing which element is the maximum transforms the remaining choice into a specific binomial coefficient, and summing over all possible maxima produces exactly the hockey stick sum"
    - "To ensure all chosen elements form a consecutive sequence in the original set"
  answer: 2
  explanation: "Once you fix that the largest chosen element is r+k+1, the remaining r elements must be drawn from the k+r elements below it, giving C(r+k, r). Summing k from 0 to n−r yields the hockey stick. The elegance is that a combinatorial question about the maximum element decomposes the problem into exactly the terms on the left side of the identity."

- question: "The Hockey Stick Identity is an example of the double-counting technique: the same combinatorial quantity is counted in two different ways, and equating those counts yields the identity."
  type: true-false
  answer: true
  explanation: "This is precisely how the canonical proof works. C(n+1, r+1) counts subsets of size r+1 from {1,...,n+1}. Conditioning on the maximum element and summing gives the hockey stick sum. Since both expressions count the same thing, they are equal — revealing not just that the identity is true but why."

- question: "The 'hockey stick' name refers to the curved shape of the algebraic formula when written in standard sigma notation."
  type: true-false
  answer: false
  explanation: "The name comes from the visual shape traced in Pascal's triangle: the summed binomial coefficients form a straight diagonal shaft, and the result appears just below and to one side of the final term, like the curved blade of a hockey stick. The name is geometric, not algebraic."

- question: "Explain in your own words why conditioning on the largest element in the double-counting proof produces the hockey-stick sum and not some other formula."
  type: short-answer
  answer: "Fixing the maximum element to be value m reduces the choice of remaining r elements to the m−1 elements below it, yielding C(m−1, r). Summing over all possible values of m from r+1 to n+1 generates exactly the terms in the hockey stick sum, and these are exhaustive and mutually exclusive cases that together cover all (r+1)-element subsets."
  explanation: "The partition by maximum element is key: every (r+1)-element subset has a unique maximum, so the cases are disjoint and exhaustive. This is what guarantees the sum counts exactly C(n+1, r+1) without overlap or omission — the identity falls out as a consequence of how the partition is structured."
```

## Explainer

From your work with **binomial coefficients**, you know that C(n, k) counts the number of ways to choose k items from n, and that Pascal's triangle encodes these values with each entry equal to the sum of the two above it. The **Hockey Stick Identity** reveals a different pattern: add up a diagonal of entries in Pascal's triangle, and you get the value just one step below the bottom of that diagonal. Specifically: C(r, r) + C(r+1, r) + C(r+2, r) + ⋯ + C(n, r) = C(n+1, r+1). If you trace these cells in Pascal's triangle, the summed entries form the straight shaft of a hockey stick, and the result is the curved blade at the bottom — hence the name.

The cleanest proof uses the **double-counting principle** from your prerequisites. Ask: how many ways can you choose r+1 items from the set {1, 2, 3, ..., n+1}? The answer is C(n+1, r+1). Now count the same thing a different way: condition on which element is the *largest* chosen. If the largest is r+1, the remaining r items come from {1, ..., r}, giving C(r, r) = 1 way. If the largest is r+2, the remaining r come from {1, ..., r+1}, giving C(r+1, r) ways. If the largest is r+k+1, you get C(r+k, r) ways. Summing over all possible largest elements from r+1 up to n+1 produces exactly the hockey stick sum — and both counts equal C(n+1, r+1). The identity follows.

Let's verify with r = 2: C(2,2) + C(3,2) + C(4,2) + C(5,2) = C(6,3). Computing: 1 + 3 + 6 + 10 = 20, and C(6,3) = 20. ✓ In Pascal's triangle these values — 1, 3, 6, 10 — appear along a diagonal moving down-right from the apex, and the answer 20 appears one step below and one step right of the last term, forming the blade. Marking these cells makes the hockey stick shape unmistakable.

The Hockey Stick Identity is a powerful shortcut whenever you need to sum a diagonal run of binomial coefficients — a computation that arises in probability distributions, combinatorial proofs, and algorithm analysis. More broadly, it exemplifies a central technique in combinatorics: identify the same quantity in two different ways, equate the counts, and the resulting equation is a non-trivial identity. Double counting doesn't just verify formulas — it reveals *why* they are true.
