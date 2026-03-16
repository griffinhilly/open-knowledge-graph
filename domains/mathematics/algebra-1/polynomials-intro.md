---
id: polynomials-intro
title: Introduction to Polynomials
domain: mathematics
course: algebra-1
prerequisites:
- id: variables-and-expressions-review
  type: hard
- id: exponent-rules-product-power-quotient
  type: hard
- id: zero-exponent
  type: soft
builds-toward:
- adding-subtracting-polynomials
- multiplying-polynomials
tags:
- polynomials
- degree
- terms
- classification
stage: abstract-reasoning
status: validated
---
# Introduction to Polynomials

## Core Idea
A polynomial is an expression consisting of variables and coefficients, combined using addition, subtraction, and non-negative integer exponents. Examples: 3x² + 2x − 5 (a trinomial of degree 2), 7x⁴ (a monomial of degree 4), and x³ − 1 (a binomial of degree 3). The degree of a polynomial is the highest exponent on the variable. Polynomials are classified by degree (linear, quadratic, cubic, quartic, ...) and by number of terms (monomial, binomial, trinomial). Polynomials are the building blocks of algebraic manipulation — factoring, solving, and graphing all depend on understanding their structure.

## How It's Best Learned
Start by identifying whether expressions are polynomials (e.g., 1/x is not, because it involves a negative exponent). Practice identifying the degree, leading coefficient, and number of terms. Write polynomials in standard form (descending order of exponents). Classify by degree and number of terms. Connect to evaluation — a polynomial is a function whose value depends on the input.

## Common Misconceptions
- Thinking 1/x or sqrt(x) are polynomials (they are not because the exponents are negative or fractional).
- Confusing the degree of a polynomial with the number of terms.
- Not writing in standard form (terms in descending order of degree).

## Explainer

You already know how to work with variables and algebraic expressions, and you've learned exponent rules for products and powers. A **polynomial** is a specific kind of expression built from those tools: it combines non-negative integer powers of a variable with constants, using only addition, subtraction, and multiplication. Think of a polynomial as a list of **terms**, where each term is a coefficient times a power of the variable.

The requirement of non-negative integer exponents is the defining restriction. The expression 3x² + 2x − 5 qualifies as a polynomial: the exponents are 2, 1, and 0 (the constant −5 is really −5x⁰). But 1/x = x⁻¹ has a negative exponent, so it is not a polynomial. And √x = x^(1/2) has a fractional exponent — also not a polynomial. This constraint is what makes polynomials behave so well under arithmetic: the sum, difference, and product of two polynomials always yield another polynomial, because combining non-negative integers through addition and multiplication always produces non-negative integers.

Two measurements describe any polynomial's structure. The **degree** is the highest exponent that appears: the polynomial 4x³ − 2x + 1 has degree 3, making it a **cubic**. A degree-1 polynomial is **linear**, degree-2 is **quadratic**, and degree-4 is **quartic**. The **leading coefficient** is the number multiplied by the highest-degree term; in 4x³ − 2x + 1 it is 4. Polynomials are also classified by number of terms: one term is a **monomial** (like 7x⁴), two terms a **binomial** (like x² − 4), and three terms a **trinomial** (like x² + 3x + 2).

**Standard form** means writing a polynomial with terms in descending order of degree: 3x² + 2x − 5, not −5 + 2x + 3x². This ordering makes it trivial to read off the degree and leading coefficient — they are always the first term. It also makes adding and subtracting polynomials mechanical: you align like terms (same degree) in columns, the same way you align digits when adding numbers. Standard form is the expected starting point for factoring, solving, and graphing, so developing the habit now will save constant reorganization later. Polynomials are the backbone of algebra: every subsequent topic — operations on polynomials, factoring, solving polynomial equations, and graphing — builds directly on the structural vocabulary you are learning here.
