---
id: subtraction-fact-families-1st
title: Subtraction Fact Families
domain: mathematics
course: 1st-grade
prerequisites:
- id: addition-fact-families-1st
  type: hard
- id: subtraction-within-20
  type: hard
builds-toward:
- subtraction-fact-families
- addition-subtraction-word-problems
tags:
- relationships
- subtraction
- addition
stage: pre-formal
status: validated
---

# Subtraction Fact Families

## Core Idea
From the fact family 3 + 5 = 8, we also know 5 + 3 = 8, 8 – 3 = 5, and 8 – 5 = 3. Recognizing that subtraction 'undoes' addition helps students see that learning one addition fact gives them three other facts for free.

## Questions

```yaml
- question: "You know that 7 + 9 = 16. Without doing any new calculation, what subtraction fact can you immediately conclude?"
  type: multiple-choice
  options:
    - "9 − 7 = 16"
    - "16 − 9 = 7"
    - "16 + 7 = 9"
    - "7 − 16 = 9"
  answer: 1
  explanation: "Because subtraction undoes addition, every addition fact produces two subtraction facts using the same three numbers. If 7 + 9 = 16, then 16 − 9 = 7 (and also 16 − 7 = 9). The big number (16) always starts the subtraction sentence. No new calculation is needed — the relationship is already encoded in the addition fact you already know."

- question: "A student solves 13 − 8 = ? by asking 'What number goes with 8 to make 13?' and answers 5. This strategy works because..."
  type: multiple-choice
  options:
    - "Addition and subtraction always produce the same numerical answer"
    - "8 is less than 13, so subtraction is not needed"
    - "Subtraction is the inverse of addition, so 13 − 8 = ? is the same question as 8 + ? = 13"
    - "The student is using a different fact family entirely"
  answer: 2
  explanation: "Turning a subtraction problem into a missing-addend question works because subtraction and addition are inverse operations — they undo each other. '13 − 8 = ?' asks how much you have left after removing 8 from 13. '8 + ? = 13' asks what you need to add to 8 to reach 13. These are two ways of describing the same relationship between the three numbers 8, 5, and 13. This is the key shortcut that makes subtraction facts accessible through addition knowledge."

- question: "Subtraction facts must be memorized separately from addition facts because the two operations are unrelated."
  type: true-false
  answer: false
  explanation: "This is exactly backward. Subtraction is the inverse of addition — it undoes it. Every fact family bundles two addition facts and two subtraction facts from the same three numbers. If you know 6 + 7 = 13 and 7 + 6 = 13, you automatically know 13 − 6 = 7 and 13 − 7 = 6. Learning them separately ignores this relationship and doubles the memorization work unnecessarily."

- question: "In the fact family containing 4, 7, and 11, both '4 + 7 = 11' and '11 − 4 = 7' are correct members of the family."
  type: true-false
  answer: true
  explanation: "Yes. A fact family groups all the addition and subtraction equations that use the same three numbers. For 4, 7, and 11: the two addition facts are 4 + 7 = 11 and 7 + 4 = 11, and the two subtraction facts are 11 − 4 = 7 and 11 − 7 = 4. All four belong to the same family because the same three numbers appear in each, just arranged differently."

- question: "Explain why knowing one addition fact like 6 + 8 = 14 immediately gives you two subtraction facts. What is the relationship between addition and subtraction that makes this work?"
  type: short-answer
  answer: "Addition and subtraction are inverse operations — subtraction undoes addition. If putting 6 and 8 together makes 14, then taking 6 away from 14 gives back 8, and taking 8 away from 14 gives back 6. So 6 + 8 = 14 immediately yields 14 − 6 = 8 and 14 − 8 = 6. The three numbers (6, 8, 14) are always 'in the same family' — the big number starts every subtraction, and the two smaller numbers fill the other positions."
  explanation: "Understanding this relationship is far more powerful than memorizing subtraction facts independently. It means your addition knowledge is also subtraction knowledge — you just need to recognize when to use the inverse relationship. The 'door' analogy from the topic helps: addition pushes the door open (6 and 8 combine to make 14), subtraction pulls it back (start with 14, remove one part, return to the other)."
```

## Explainer

You already know addition fact families — the idea that 3 + 5 = 8 and 5 + 3 = 8 are two ways of writing the same relationship. Subtraction fact families extend that thinking one step further: if you know those two addition facts, you also know 8 − 3 = 5 and 8 − 5 = 3, for free. That's four facts from one group of three numbers.

The reason this works is that **subtraction is the inverse of addition** — it undoes it. Think of it like a door with two sides. Addition pushes the door open (3 and 5 go together to make 8). Subtraction pulls the door back (start with 8, take away 3, and you're back to 5). The same three numbers — 3, 5, and 8 — appear in all four facts. Mathematicians call this a **fact family** because those numbers are always "in the same family" together.

Here's how to see all four members of the family at once. Pick any three numbers where the small two add up to the big one, like 4, 6, and 10. Write both addition orders: 4 + 6 = 10 and 6 + 4 = 10. Then write both subtraction versions by starting from the big number: 10 − 4 = 6 and 10 − 6 = 4. Notice that the big number always appears at the beginning of a subtraction sentence — that's the whole thing you started with before you took something away.

This insight makes you a faster mathematician. Instead of memorizing subtraction facts separately from addition facts, you can retrieve them from the same mental "family." When you see 13 − 7 = ?, you can ask yourself: "What goes with 7 to make 13?" — turning the subtraction into a missing-addend problem. Because you already know 7 + 6 = 13 from your addition work, you immediately know the answer is 6. Fact families are your shortcut to knowing subtraction without having to learn it all over again.
