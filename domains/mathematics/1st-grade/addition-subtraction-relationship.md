---
id: addition-subtraction-relationship
title: Addition and Subtraction Relationship
domain: mathematics
course: 1st-grade
prerequisites:
- id: addition-within-10
  type: hard
- id: subtraction-within-10
  type: hard
- id: part-part-whole-model-1st
  type: hard
- id: subtraction-within-20
  type: soft
- id: core-number
  type: hard
- id: discernment-same-different
  type: soft
builds-toward:
- fact-families
tags:
- inverse-operations
- relationships
stage: pre-formal
status: validated
---

# Addition and Subtraction Relationship

## Core Idea
Addition and subtraction are inverse operations: if 5+3=8, then 8-3=5 and 8-5=3. Recognizing this relationship helps students see that fact families belong together and supports flexible thinking.

## Questions

```yaml
- question: "You know that 6 + 7 = 13. Which subtraction facts does this immediately give you, without any new calculation?"
  type: multiple-choice
  options:
    - "13 - 6 = 7 and 13 - 7 = 6"
    - "7 - 6 = 1 and 6 - 7 = -1"
    - "13 - 6 = 7 only, because subtraction is not commutative"
    - "None — addition and subtraction are separate skills"
  answer: 0
  explanation: "Addition and subtraction are inverse operations: every addition fact contains two subtraction facts in the same fact family. Knowing 6 + 7 = 13 immediately tells you that 13 - 7 = 6 and 13 - 6 = 7. The same three numbers (6, 7, 13) are related in all four facts of the family."

- question: "A student is trying to solve 9 - 4. She thinks: 'I don't know that subtraction fact, but I know 4 + 5 = 9, so the answer must be 5.' This approach works because..."
  type: multiple-choice
  options:
    - "Addition always produces bigger numbers than subtraction"
    - "Subtraction undoes addition, so if 4 + 5 = 9, then 9 - 4 = 5"
    - "She got lucky — this strategy only works sometimes"
    - "The numbers 4, 5, and 9 are special; this would not work with other numbers"
  answer: 1
  explanation: "This is exactly the power of understanding inverse operations. Because subtraction undoes addition, you can answer any subtraction question by asking 'what do I add to get that total?' The strategy works for all whole number facts — it reflects the structure of the number system itself, not a coincidence."

- question: "Once you know one addition fact, you automatically know four related facts."
  type: true-false
  answer: true
  explanation: "True. Knowing 3 + 4 = 7 gives you four facts: 3 + 4 = 7, 4 + 3 = 7 (commutative property), 7 - 4 = 3, and 7 - 3 = 4. These four facts form a fact family — they all share the same three numbers and reflect the inverse relationship between addition and subtraction."

- question: "To solve a subtraction fact you don't know, it's better to memorize it directly rather than use addition knowledge."
  type: true-false
  answer: false
  explanation: "False. Using addition knowledge to solve subtraction is a powerful and efficient strategy. Because addition and subtraction are inverse operations, existing addition facts unlock subtraction facts. Thinking 'what plus 4 equals 9?' to answer 9 - 4 is not a workaround — it is how mathematicians think flexibly about number relationships."

- question: "Why can knowing 5 + 8 = 13 help you solve 13 - 5? Explain the connection."
  type: short-answer
  answer: "Because addition and subtraction are inverse operations — they undo each other. The numbers 5, 8, and 13 belong to a fact family. If adding 5 to 8 gives 13, then taking 5 away from 13 must give back 8. You do not need to memorize 13 - 5 separately; your addition knowledge already contains the answer."
  explanation: "The relationship runs in both directions: addition combines two parts into a whole, and subtraction separates a whole back into its parts. Fact families make this explicit — one group of three numbers generates four related facts. Learning addition first does not just feel easier; it directly builds subtraction knowledge."
```

## Explainer

You already know how to add numbers within 10 and subtract numbers within 10. Now we're going to see something surprising: those two skills are secretly the same skill, just running in different directions.

Think about a box of 8 crayons. If you know that 5 red crayons and 3 blue crayons make 8 total, you already know two subtraction facts — even if you haven't done the subtraction yet. If someone takes away the 3 blue crayons, how many are left? 5. If someone takes away the 5 red ones, how many are left? 3. The same three numbers — 5, 3, and 8 — belong to a whole family of facts: **5 + 3 = 8**, **3 + 5 = 8**, **8 − 3 = 5**, **8 − 5 = 3**. That's a **fact family**.

The reason this works is that addition and subtraction are **inverse operations** — they undo each other. Adding 3 to something and then taking 3 away brings you back to where you started. So whenever you see an addition fact, there are two subtraction facts hiding inside it. This is a powerful shortcut: instead of memorizing subtraction facts separately, you can think "what addition fact do I already know that uses these same numbers?"

This connection also helps when a subtraction problem feels hard. If you don't immediately know 8 − 5, you can think: "What plus 5 equals 8?" You're searching your addition knowledge to answer a subtraction question. That flexible thinking — moving back and forth between addition and subtraction — is exactly what mathematicians do. Numbers aren't separate facts to memorize in isolation; they form a web of relationships, and once you see those relationships, each fact you know unlocks several others.
