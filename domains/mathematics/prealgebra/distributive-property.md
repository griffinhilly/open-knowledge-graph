---
id: distributive-property
title: The Distributive Property
domain: mathematics
course: prealgebra
prerequisites:
- id: variable-expressions
  type: hard
- id: multiplying-integers
  type: hard
- id: properties-of-operations
  type: soft
builds-toward:
- two-step-equations
- multiplying-polynomials
- factoring-gcf
tags:
- distributive-property
- expressions
- multiplication
- algebra
stage: abstract-reasoning
status: validated
---
# The Distributive Property

## Core Idea
The distributive property states that a(b + c) = ab + ac. It connects multiplication and addition, allowing you to "distribute" a factor across terms inside parentheses. For example, 3(x + 4) = 3x + 12. The property works in reverse too — pulling out a common factor is called factoring: 6x + 15 = 3(2x + 5). The distributive property is one of the most important properties in algebra. It is the basis for expanding expressions, multiplying polynomials (including FOIL), and factoring — three pillars of algebraic manipulation.

## How It's Best Learned
Start with numerical examples where students can verify: 3(10 + 2) = 3(12) = 36, and 3(10) + 3(2) = 30 + 6 = 36. Use area models — a rectangle with width 3 and length (x + 4) has area 3x + 12. Then move to purely algebraic expressions. Practice both distributing and "un-distributing" (factoring out the GCF).

## Common Misconceptions
- Distributing only to the first term: 3(x + 4) = 3x + 4 instead of 3x + 12.
- Forgetting to distribute the sign: −2(x − 3) = −2x − 3 instead of −2x + 6.
- Not recognizing the distributive property in reverse (factoring) as the same concept.

## Questions

```yaml
- question: "Simplify: −3(2x − 5)"
  type: multiple-choice
  options:
    - "−6x − 5"
    - "−6x − 15"
    - "−6x + 15"
    - "6x − 15"
  answer: 2
  explanation: "The factor −3 must be distributed to every term inside the parentheses: −3 · 2x = −6x, and −3 · (−5) = +15. The result is −6x + 15. Option A is the most common error — distributing −3 to the first term but not properly applying the sign to the second. Option B results from treating −3 · (−5) incorrectly as −15. Remember: the sign is part of the factor and distributes like everything else; there is no protective barrier around the second term."

- question: "A student needs to simplify 12x + 18. Which application of the distributive property produces the most fully factored form?"
  type: multiple-choice
  options:
    - "2(6x + 9)"
    - "3(4x + 6)"
    - "6(2x + 3)"
    - "The distributive property only works left to right; it cannot be applied here"
  answer: 2
  explanation: "The distributive property runs in both directions. Applied right to left — ab + ac → a(b + c) — it is called factoring. The greatest common factor of 12x and 18 is 6, giving 6(2x + 3). Options A and B are partially factored but not completely: 6 and 9 share a common factor of 3, and 4 and 6 share a common factor of 2. Option D reflects a critical misconception — factoring is the same operation as distributing, just applied in reverse."

- question: "The area model for the distributive property shows why every term inside the parentheses must be multiplied: each sub-rectangle requires the full width of the factor outside."
  type: true-false
  answer: true
  explanation: "In the area model, a rectangle with width a and length (b + c) is divided into two sub-rectangles: one with area a·b and one with area a·c. The full width 'a' applies to every sub-rectangle — you cannot give part of the width to one and not to the other. This geometric fact is why a(b + c) = ab + ac holds: each term inside the parentheses receives the full factor. It also explains why distributing only to the first term — a(b + c) = ab + c — is geometrically nonsensical."

- question: "The expression 3(x + 4) = 3x + 4 is a correct application of the distributive property."
  type: true-false
  answer: false
  explanation: "This is the most common distributing error: multiplying 3 by the first term (x) but forgetting to multiply it by the second term (4). The correct expansion is 3(x + 4) = 3x + 12. Every term inside the parentheses must be multiplied by the factor outside. A useful check: count the terms inside (two: x and 4) and confirm the same number appear after distributing (two: 3x and 12)."

- question: "Explain why factoring — for example, rewriting 6x + 15 as 3(2x + 5) — is the same operation as the distributive property, not a separate rule."
  type: short-answer
  answer: "The distributive property states a(b + c) = ab + ac. Factoring applies this identity right to left: starting with ab + ac and recognizing it equals a(b + c). The mathematical relationship is identical; only the direction of application differs. Factoring is the distributive property run in reverse."
  explanation: "This conceptual unity is important because students who see factoring as a separate, mysterious operation struggle when they encounter it in advanced contexts like solving quadratic equations or simplifying rational expressions. Once you recognize that 6x + 15 = 3(2x + 5) is the same claim as 3(2x + 5) = 6x + 15 read from right to left, the operation becomes one unified tool rather than two separate ones."
```

## Explainer

You already know that multiplication and addition are separate operations — you've been computing with integers and expressions separately. The distributive property reveals a deep connection *between* them: multiplication distributes over addition. This is not obvious from counting alone; it is a structural fact about how numbers work that turns out to be one of algebra's most powerful tools.

The geometric picture makes it concrete. Imagine a rectangle with width 3 and length (x + 4). Its total area can be computed two ways: as one big rectangle giving 3(x + 4), or as two smaller rectangles side by side giving 3·x + 3·4 = 3x + 12. The distributive property just says these two calculations always agree: 3(x + 4) = 3x + 12. This **area model** explains why the property must hold — splitting one dimension of a rectangle into parts and summing the sub-areas must equal the whole area. It also shows why every term inside the parentheses gets multiplied: each sub-rectangle uses the full width of 3.

The algebraic form a(b + c) = ab + ac extends to any number of terms and to subtraction: a(b − c) = ab − ac, because subtraction is adding a negative. The most common mistake is forgetting to touch every term — writing 3(x + 4) = 3x + 4 multiplies only the first term by 3. A useful check: count the terms inside the parentheses and confirm the same number appear after distributing. Negative signs are the other trap: −2(x − 3) requires distributing the negative through both terms, giving −2x + 6. Treating the parentheses as a protective barrier that the sign can't cross is the error; the sign is part of the factor and distributes like everything else.

The property runs in both directions, and this bidirectionality is essential. Left to right — a(b + c) → ab + ac — is **expanding** or **distributing**. Right to left — ab + ac → a(b + c) — is **factoring**, specifically pulling out the **greatest common factor**. Recognizing that 6x + 15 = 3(2x + 5) is the same operation as 3(2x + 5) = 6x + 15, just reversed. You will use the factoring direction constantly in algebra when solving equations or simplifying expressions. The distributive property is also the foundation for multiplying polynomials: (x + 2)(x + 3) = x(x + 3) + 2(x + 3) = x² + 3x + 2x + 6 = x² + 5x + 6 — every term in the first factor distributes over every term in the second.
