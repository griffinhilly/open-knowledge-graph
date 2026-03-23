---
id: unit-fractions-halves-thirds-fourths
title: 'Unit Fractions: Halves, Thirds, Fourths'
domain: mathematics
course: 3rd-grade
prerequisites:
- id: fractions-halves-fourths-thirds-2nd
  type: hard
- id: partition-shapes-equal-parts
  type: soft
builds-toward:
- fractions-equal-parts
tags:
- fractions
- unit-fractions
- equal-parts
stage: concrete-operations
status: validated
---

# Unit Fractions: Halves, Thirds, Fourths

## Core Idea
A unit fraction has numerator 1 and represents one equal part of a whole: ½ (one of two equal parts), ⅓ (one of three), ¼ (one of four). The denominator indicates how many equal parts partition the whole.

## Questions

```yaml
- question: "A pizza is cut into 8 equal slices and you get one slice (⅛). Your friend's pizza is the same size but is cut into 4 equal slices and she gets one slice (¼). Who has more pizza?"
  type: multiple-choice
  options:
    - "You do — ⅛ is bigger because 8 is bigger than 4"
    - "Your friend does — ¼ is bigger because fewer cuts means larger pieces"
    - "You have the same amount — both got one slice"
    - "It depends on how large the pizza is"
  answer: 1
  explanation: "Your friend has more pizza. When a whole is cut into fewer pieces, each piece is larger. 4 cuts give bigger slices than 8 cuts from the same pizza. So ¼ > ⅛ — even though 4 is smaller than 8. This is the crucial counterintuitive insight: for unit fractions, a larger denominator means a smaller piece, not a larger one. Option A is the most common wrong answer, reflecting the tempting but false idea that bigger numbers mean bigger fractions."

- question: "Which of the following correctly orders these unit fractions from smallest to largest: ½, ¼, ⅓?"
  type: multiple-choice
  options:
    - "½, ⅓, ¼ — ordered by denominator from smallest to largest"
    - "¼, ⅓, ½ — larger denominator means smaller piece, so ¼ is smallest"
    - "¼, ½, ⅓ — fourths are smallest, then halves, then thirds"
    - "They are all equal because each is exactly one part of a whole"
  answer: 1
  explanation: "¼ < ⅓ < ½ — as the denominator increases, each piece gets smaller because the whole is being divided into more parts. Cutting something into 4 equal pieces gives smaller pieces than cutting into 3 or 2. The correct order from smallest to largest is ¼, ⅓, ½. Option D is wrong because the pieces are only equal if the wholes are divided the same way."

- question: "Because 4 is larger than 2, the fraction ¼ is larger than ½."
  type: true-false
  answer: false
  explanation: "This is the central misconception about unit fractions. ¼ is actually smaller than ½. The denominator counts how many equal pieces the whole is divided into — more pieces means smaller pieces. Think of cutting a sandwich: 4 equal cuts produce smaller pieces than 2 equal cuts. The 'bigger number = bigger fraction' intuition from whole numbers works in reverse for unit fractions."

- question: "The denominator of a fraction tells you how many equal parts the whole has been divided into."
  type: true-false
  answer: true
  explanation: "This is the precise meaning of the denominator. In ¾, the denominator 4 tells you the whole is divided into 4 equal parts; the numerator 3 tells you how many of those parts you have. For unit fractions, the numerator is always 1, so all that changes between ½, ⅓, and ¼ is how finely the whole is divided — which the denominator tracks."

- question: "Why does a unit fraction get smaller as the denominator gets larger? Explain using the idea of equal parts."
  type: short-answer
  answer: "When you divide a whole into more equal parts, each individual part must be smaller, because the same total amount is shared among more pieces. For example, dividing a pizza into 8 equal slices gives smaller slices than dividing it into 2 slices. So ⅛ (one of eight pieces) is a smaller amount than ½ (one of two pieces). Larger denominator = more pieces = each piece is smaller."
  explanation: "This insight reverses the usual 'bigger number = bigger amount' intuition from counting, and that reversal is the hardest thing to internalize about fractions. Anchoring the explanation in a physical image — slices of pizza or pieces of ribbon — makes the logic concrete and memorable. Once students truly understand why the reversal happens, they stop relying on the faulty shortcut."
```

## Explainer

You've already worked with shapes divided into equal parts and given them names like halves, thirds, and fourths. Now you're building the formal notation for what you already understand. A **fraction** is a way of writing down what happens when you divide a whole into equal parts and take some of them. A **unit fraction** is the simplest case — you take exactly one of those equal parts.

The fraction ½ means "divide the whole into 2 equal parts, take 1." The fraction ⅓ means "divide the whole into 3 equal parts, take 1." The fraction ¼ means "divide the whole into 4 equal parts, take 1." The number on the bottom — the **denominator** — counts the equal parts the whole is cut into. The number on top — the **numerator** — counts how many of those parts you have. For all unit fractions, the numerator is 1; what changes is how finely the whole is divided.

Here is a crucial insight that surprises many students: as the denominator gets *larger*, the unit fraction gets *smaller*. Why is ¼ smaller than ½? Because when you cut something into 4 equal pieces, each piece is smaller than when you cut it into 2 pieces. Think of a pizza: cut into 2 slices, each slice is large; cut into 4 slices, each slice is half as large; cut into 8 slices, each is tiny. More cuts = smaller pieces. So ¼ < ⅓ < ½. This runs against the instinct that "bigger numbers mean bigger things," and internalizing the reversal is one of the most important conceptual moves in early fractions.

Unit fractions are the **building blocks** of all other fractions. ¾ means "3 copies of ¼" — you've taken 3 of the 4 equal parts. 2/3 means "2 copies of ⅓." Every fraction is just a whole-number count of unit fractions. Understanding unit fractions deeply now means that every later fraction concept — comparing sizes, adding fractions, multiplying — will have a solid, visual foundation to rest on.
