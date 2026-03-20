---
id: solving-radical-equations
title: Solving Radical Equations
domain: mathematics
course: algebra-2
prerequisites:
  - id: radical-functions-and-graphs
    type: hard
  - id: rational-exponents
    type: hard
builds-toward:
  - solving-rational-equations
tags: [radicals, equations, extraneous-solutions]
stage: formal-systems
status: validated
---

# Solving Radical Equations

## Core Idea
To solve a radical equation, isolate the radical on one side and raise both sides to the appropriate power to eliminate it. For square roots, square both sides; for cube roots, cube both sides. Squaring can introduce extraneous solutions, so checking all solutions in the original equation is mandatory. Equations with two radicals may require squaring twice.

## How It's Best Learned
Start with simple one-radical equations. Emphasize the isolation step before squaring. Demonstrate extraneous solutions with examples where checking eliminates invalid answers. Progress to equations with two radicals, showing the double-squaring technique. Reinforce checking every solution.

## Common Misconceptions
- Forgetting to isolate the radical before squaring (squaring both sides of sqrt(x) + 3 = 5 is not (sqrt(x))^2 + 9 = 25).
- Not checking for extraneous solutions (the most critical error in this topic).
- Thinking that cubing both sides also produces extraneous solutions (it does not; only even powers can introduce them).

## Explainer

From your work with **radical functions**, you know that √x is only defined for x ≥ 0 and always produces a non-negative output. From **rational exponents**, you know that √x = x^(1/2) and that raising to a power is the inverse of taking a root. These two facts together explain both the technique and the danger of solving radical equations: raising both sides to a power eliminates the radical, but the process is not perfectly reversible, which can generate answers that don't actually work.

The fundamental technique is **isolation then elimination**. Consider √(2x + 3) = 5. First, the radical is already isolated. Then square both sides: (√(2x+3))² = 5², giving 2x + 3 = 25, so x = 11. Check: √(2·11 + 3) = √25 = 5. ✓ Now consider a slightly different equation: √x + 3 = 0. Isolating gives √x = −3. You already know from radical functions that √x ≥ 0 always, so √x can never equal −3. No solution exists. But if you forget to think and just square: x = 9. Check: √9 + 3 = 3 + 3 = 6 ≠ 0. The check catches it — x = 9 is **extraneous**, a solution introduced by the squaring step that doesn't satisfy the original equation.

Why does squaring create extraneous solutions? Because squaring is not a one-to-one operation: both 3 and −3 square to 9. When you square both sides of an equation, you're saying "these two expressions have the same square" — but that's true both when they're equal *and* when they're negatives of each other. So squaring can turn a false equation into a true one. Cube roots don't have this problem because the cube function *is* one-to-one: only 3 cubes to 27, and −3 cubes to −27. This is why only even-index roots create extraneous solutions.

For equations with two radicals — like √(x+5) + √(x−1) = 4 — the strategy is to isolate one radical, square, simplify, and then isolate the remaining radical and square again. This double-squaring is necessary but doubles the risk of extraneous solutions. After two squaring steps, you may end up with a quadratic that has two solutions, one or both of which might be extraneous. The mandatory final check is not just a formality — it is the correct conclusion of the solving process, restoring the constraint that the original radical expressions must be non-negative.
