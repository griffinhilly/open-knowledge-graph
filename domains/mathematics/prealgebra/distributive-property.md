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

## Explainer

You already know that multiplication and addition are separate operations — you've been computing with integers and expressions separately. The distributive property reveals a deep connection *between* them: multiplication distributes over addition. This is not obvious from counting alone; it is a structural fact about how numbers work that turns out to be one of algebra's most powerful tools.

The geometric picture makes it concrete. Imagine a rectangle with width 3 and length (x + 4). Its total area can be computed two ways: as one big rectangle giving 3(x + 4), or as two smaller rectangles side by side giving 3·x + 3·4 = 3x + 12. The distributive property just says these two calculations always agree: 3(x + 4) = 3x + 12. This **area model** explains why the property must hold — splitting one dimension of a rectangle into parts and summing the sub-areas must equal the whole area. It also shows why every term inside the parentheses gets multiplied: each sub-rectangle uses the full width of 3.

The algebraic form a(b + c) = ab + ac extends to any number of terms and to subtraction: a(b − c) = ab − ac, because subtraction is adding a negative. The most common mistake is forgetting to touch every term — writing 3(x + 4) = 3x + 4 multiplies only the first term by 3. A useful check: count the terms inside the parentheses and confirm the same number appear after distributing. Negative signs are the other trap: −2(x − 3) requires distributing the negative through both terms, giving −2x + 6. Treating the parentheses as a protective barrier that the sign can't cross is the error; the sign is part of the factor and distributes like everything else.

The property runs in both directions, and this bidirectionality is essential. Left to right — a(b + c) → ab + ac — is **expanding** or **distributing**. Right to left — ab + ac → a(b + c) — is **factoring**, specifically pulling out the **greatest common factor**. Recognizing that 6x + 15 = 3(2x + 5) is the same operation as 3(2x + 5) = 6x + 15, just reversed. You will use the factoring direction constantly in algebra when solving equations or simplifying expressions. The distributive property is also the foundation for multiplying polynomials: (x + 2)(x + 3) = x(x + 3) + 2(x + 3) = x² + 3x + 2x + 6 = x² + 5x + 6 — every term in the first factor distributes over every term in the second.
