---
id: solving-proportions
title: Solving Proportions
domain: mathematics
course: prealgebra
prerequisites:
- id: proportions
  type: hard
- id: one-step-equations
  type: soft
builds-toward:
- percent-of-a-number
- similar-triangles-aa
- direct-and-inverse-variation
tags:
- proportions
- cross-multiplication
- solving
stage: abstract-reasoning
status: validated
---
# Solving Proportions

## Core Idea
Solving a proportion means finding an unknown value in an equation of two equal ratios, such as 3/5 = x/20. The standard method is cross-multiplication: multiply the numerator of each fraction by the denominator of the other, producing an equation (3 × 20 = 5 × x, so 60 = 5x, thus x = 12). Alternatively, students can use the scale factor between known corresponding parts. This skill is used heavily in geometry (similar figures, scale drawings), science (unit conversions, dilutions), and real-world problem solving (recipes, maps, models).

## How It's Best Learned
Start with simple proportions where the scale factor is obvious (2/3 = 4/6), then move to problems requiring cross-multiplication. Show both the scale-factor method and cross-multiplication so students have two strategies. Use word problems that require setting up the proportion before solving — the setup is often harder than the algebra.

## Common Misconceptions
- Setting up the proportion incorrectly by mixing up which quantities correspond.
- Cross-multiplying incorrectly (multiplying numerator by numerator instead of across).
- Forgetting to divide after cross-multiplying — stopping at 60 = 5x without solving for x.

## Questions

```yaml
- question: "A car travels 240 miles on 8 gallons of gas. A student sets up the proportion 240/8 = x/360 to find how many gallons are needed for 360 miles. What is wrong with this setup?"
  type: multiple-choice
  options:
    - "Nothing — this proportion is correct and will give the right answer"
    - "The types are inconsistent: the left side is miles/gallons, but the right side places the unknown over miles — the same type of quantity must appear in the same position on both sides"
    - "Cross-multiplication is the wrong method for distance-fuel problems"
    - "The unknown x should always appear in the numerator on the right side of a proportion"
  answer: 1
  explanation: "A valid proportion requires the same type of ratio on both sides. 240/8 is miles per gallon; x/360 places x (gallons) over miles — an inverted and inconsistent relationship. Cross-multiplying gives 240 × 360 = 8x → x = 10,800, which is wildly wrong. The correct setup is 240/8 = 360/x (miles/gallons on both sides), giving 240x = 2,880 → x = 12 gallons."

- question: "After correctly cross-multiplying the proportion 3/4 = 9/x, a student writes '3x = 36' but then gives the final answer as x = 33. Which error did they make?"
  type: multiple-choice
  options:
    - "They used the wrong cross-multiplication pairs"
    - "They subtracted 3 from both sides instead of dividing both sides by 3"
    - "Cross-multiplying a proportion with a variable in the denominator requires a different technique"
    - "They should have used the scale-factor method instead of cross-multiplication"
  answer: 1
  explanation: "After cross-multiplying, 3x = 36 is a one-step equation: divide both sides by 3 to get x = 12. Subtracting 3 gives 33 — treating it as 3 + x = 36 instead of 3 × x = 36. This is a common error among students who haven't internalized that cross-multiplication produces a multiplication equation, not an addition one."

- question: "Cross-multiplication works because it transforms a proportion (two equal fractions) into a simple linear equation that can be solved with one-step equation techniques."
  type: true-false
  answer: true
  explanation: "Exactly right. Cross-multiplying a/b = c/d by both denominators (b and d) gives a × d = b × c — an ordinary multiplication equation. This connects proportion-solving to the equation-solving skills you already have, rather than being a separate procedure to memorize."

- question: "Setting up the proportion correctly is usually the easy part of solving proportion problems; most errors occur during the cross-multiplication step."
  type: true-false
  answer: false
  explanation: "This common assumption is backwards. Cross-multiplication is mechanical and easy to check. Setup — correctly identifying which quantities correspond and placing them consistently — is where most errors originate. A correct setup with a small arithmetic error is easily caught; an incorrect setup produces a wrong answer that looks perfectly reasonable and goes undetected."

- question: "Why is it important to keep the same type of quantity in the same position (numerator or denominator) on both sides of a proportion?"
  type: short-answer
  answer: "A proportion asserts that two ratios are equal. If the types are inconsistent — miles on top on one side, hours on top on the other — the fractions represent different relationships, and setting them equal is meaningless. Flipping one fraction inverts the ratio, causing x to come out as its reciprocal. For example, 1/50 = x/3 (inches over miles vs. x over inches) gives x = 3/50 miles instead of the correct 150 miles."
  explanation: "The rule 'same type in same position' is the setup equivalent of the calculation rule 'cross-multiply correctly.' Both are necessary. A proportion is only valid when both fractions represent the same relationship — e.g., both are inches per mile, or both are miles per gallon. Violating this produces an equation that's algebraically solvable but meaninglessly wrong."
```

## Explainer

A **proportion** is a statement that two ratios are equal: a/b = c/d. You already know what a ratio means — 3 cups of flour for every 2 cups of sugar, for example. A proportion simply extends that relationship: if the ratio stays the same as you scale up, the two ratios are equal. Solving a proportion means one of those four numbers is missing, and you need to find it.

The most reliable method is **cross-multiplication**. When two fractions are equal — a/b = c/d — you can multiply both sides of the equation by both denominators (b and d), which gives a × d = b × c. This is the cross-multiplication rule: the product of the numerator of one fraction and the denominator of the other equals the product of the other pair. For example, 3/5 = x/20 gives 3 × 20 = 5 × x, so 60 = 5x, and dividing both sides by 5 gives x = 12. Notice this is just the one-step equation skill you already have — cross-multiplication converts a proportion into an ordinary equation.

The other method is the **scale factor**. If you can see that one denominator is a multiple of the other, you can scale the numerator by the same factor. In 3/5 = x/20, notice that 20 = 5 × 4, so x = 3 × 4 = 12. This method is faster when the scale factor is obvious, but cross-multiplication always works even when it isn't. Use whichever approach helps you see the structure of the problem more clearly.

Setting up the proportion correctly is actually the harder skill. The rule is: keep the same *type* of quantity in the same position (numerator or denominator) on both sides. If the left side is "miles per hour," the right side must also be "miles per hour," not "hours per mile." For a map where 1 inch = 50 miles and you measure 3.5 inches, write 1/50 = 3.5/x — inches on top, miles on bottom, consistently. Flipping one fraction but not the other is the most common setup error, and cross-multiplying a mis-set proportion gives a wrong answer that looks perfectly reasonable.
