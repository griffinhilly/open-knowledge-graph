---
id: opposites-and-additive-inverses
title: Opposites and Additive Inverses
domain: mathematics
course: prealgebra
prerequisites:
  - id: integers-and-number-line
    type: hard
builds-toward:
  - subtracting-integers
  - absolute-value
  - one-step-equations
tags: [opposites, additive-inverse, integers, number-line]
stage: abstract-reasoning
status: validated
---

# Opposites and Additive Inverses

## Core Idea
The opposite (or additive inverse) of a number is the number that, when added to it, gives zero. The opposite of 5 is −5 because 5 + (−5) = 0. The opposite of −3 is 3. On the number line, opposites are the same distance from zero but on opposite sides. This concept is critical because subtraction is defined as adding the opposite, and solving equations relies on additive inverses to cancel terms. Understanding opposites also reinforces the symmetry of the number line and the special role of zero as the additive identity.

## How It's Best Learned
Use the number line to show mirror-image pairs across zero. Practice finding opposites of positive numbers, negative numbers, and zero (which is its own opposite). Connect to real-world contexts: if depositing $50 is +50, then withdrawing $50 is −50. Show that the opposite of the opposite of a number is the original number: −(−4) = 4.

## Common Misconceptions
- Thinking the opposite of a number is always negative (the opposite of −7 is +7).
- Confusing "opposite" with "reciprocal" (the reciprocal of 5 is 1/5, not −5).
- Not recognizing that 0 is its own opposite.

## Questions

```yaml
- question: "A student wants to cancel out the term +8 in the equation x + 8 = 15. They ask: 'Which number do I add to +8 to make it disappear?' What is the correct answer, and why does it work?"
  type: multiple-choice
  options:
    - "−8, because the additive inverse of 8 is −8, and 8 + (−8) = 0"
    - "−8, because any number minus itself equals zero, which is a separate operation from addition"
    - "1/8, because that is the inverse of 8"
    - "0, because adding zero cancels any number"
  answer: 0
  explanation: "The additive inverse of 8 is −8, because 8 + (−8) = 0. Adding the opposite produces zero — the additive identity — which 'cancels' the term. Option B is a distractor: it gets the right answer but gives the wrong reason (this is addition, not subtraction). Option C confuses additive inverse with multiplicative inverse (reciprocal). Option D is wrong because 8 + 0 = 8, not 0."

- question: "A student says 'the opposite of −12 must be −12 because it already has a negative sign.' What is the correct response?"
  type: multiple-choice
  options:
    - "The student is right — negative numbers are their own opposites"
    - "The opposite of −12 is +12, because opposites are equidistant from zero on opposite sides of the number line"
    - "The opposite of −12 is 0, because zero is the additive identity"
    - "The opposite of −12 is 1/12, because that is its multiplicative inverse"
  answer: 1
  explanation: "Opposites are mirror images across zero on the number line. −12 is 12 units to the left of zero; its opposite is 12 units to the right, which is +12. The confusion arises from thinking 'negative' already means 'opposite,' but the opposite of a negative number is always positive. Check: −12 + 12 = 0 ✓. The common misconception — that the opposite of a negative must also be negative — is exactly what option A represents."

- question: "The double opposite of any number equals the original number — that is, −(−n) = n for all n."
  type: true-false
  answer: true
  explanation: "Each application of 'take the opposite' reflects you across zero on the number line. Starting at n, one flip lands you at −n. A second flip from −n lands you back at n. This is not a trick — it is a direct consequence of what opposites mean geometrically. −(−7) = 7 because the opposite of '7 units left of zero' is '7 units right of zero,' which is just 7."

- question: "The opposite of a number and the reciprocal of a number are the same thing."
  type: true-false
  answer: false
  explanation: "These are inverses for completely different operations. The opposite (additive inverse) of 5 is −5, because 5 + (−5) = 0 — it undoes addition back to the additive identity (zero). The reciprocal (multiplicative inverse) of 5 is 1/5, because 5 × (1/5) = 1 — it undoes multiplication back to the multiplicative identity (one). Confusing the two is one of the most common errors in early algebra."

- question: "Explain why subtraction can be understood as 'adding the opposite,' and give an example. Why is this reframing useful?"
  type: short-answer
  answer: "Subtraction a − b equals a + (−b). For example, 7 − 3 = 7 + (−3) = 4. This reframing is useful because it reduces two operations (addition and subtraction) to a single operation (addition) plus the concept of additive inverse. In equation solving, every step that 'moves a term to the other side' is secretly using an additive inverse: to cancel +5, you add −5 to both sides. This unification makes the logic of algebra consistent and reduces the number of rules a student must memorize."
  explanation: "The reframing also clarifies why subtracting a negative number yields addition: 7 − (−3) = 7 + 3 = 10. Seen as 'add the opposite of −3,' the answer follows directly from the rule that the opposite of −3 is +3. Without the additive inverse concept, this double-negative rule appears arbitrary."
```

## Explainer

You already know about integers and the number line — numbers extend infinitely in both directions, with positive numbers to the right of zero and negative numbers to the left. When you look at the number line, every positive number has a mirror image on the other side of zero: 5 and −5 are both exactly 5 units from zero, just in opposite directions. This mirror relationship defines **opposites**. Two numbers are opposites if they are the same distance from zero but on different sides — they reflect each other across zero.

The algebraic way to capture this mirror relationship is the **additive inverse**: the additive inverse of a number is the number you add to it to get zero. Add any number to its opposite and you always land at zero — 5 + (−5) = 0, −3 + 3 = 0, 100 + (−100) = 0. Zero is the special case: it is its own opposite, because 0 + 0 = 0. No other number has this property, since any nonzero number added to itself gives a nonzero result. The name "additive inverse" emphasizes the algebraic role: it is the inverse under addition, the element that undoes any addition back to zero, the **additive identity**.

This concept unlocks subtraction. Rather than thinking of subtraction as a separate operation, you can reframe it as adding the opposite: 7 − 3 = 7 + (−3). This reframing matters because it means you only need one operation — addition — plus the idea of opposites to handle all subtraction. When you later solve equations, every step that "moves a term to the other side" is secretly using an additive inverse: to cancel +5 from one side, you add −5 to both sides. The same logic works whether the term is a number, a negative number, or an expression like 3x.

One persistent confusion is between **opposite** and **reciprocal**. The opposite of 5 is −5 (its additive inverse: 5 + (−5) = 0). The reciprocal of 5 is 1/5 (its multiplicative inverse: 5 × (1/5) = 1). These are inverses for different operations — addition versus multiplication. Another confusion involves double negatives: −(−7) = 7. This is not a trick; it is just saying that the opposite of "7 units left of zero" is "7 units right of zero." Every application of the opposite operation flips you across zero, so two flips return you to where you started.
