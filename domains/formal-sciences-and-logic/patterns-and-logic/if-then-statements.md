---
id: if-then-statements
title: If-Then Statements
domain: formal-sciences-and-logic
course: patterns-and-logic
prerequisites:
- id: true-and-false-statements
  type: hard
builds-toward:
- logical-puzzles
- cause-and-effect-chains
- propositional-logic-introduction
tags:
- logic
- conditionals
- if-then
- reasoning
stage: concrete-operations
status: validated
---

# If-Then Statements

## Core Idea
An if-then statement connects two ideas: a condition (the "if" part) and a result (the "then" part). "If it rains, then the ground gets wet." The condition does not have to be true right now — the statement claims that whenever the condition IS true, the result follows. If-then statements are the backbone of logical reasoning: rules, scientific laws, and mathematical theorems are all expressed as if-then relationships. Understanding them means understanding how conditions and consequences connect.

## How It's Best Learned
Start with familiar cause-and-effect relationships: "If you touch the stove, then you get burned." "If it snows, then school might close." Have students identify the condition and the result in each statement. Practice rephrasing statements into if-then form: "Wearing a coat keeps you warm" becomes "If you wear a coat, then you stay warm." Include examples where the condition is false and discuss what that means for the statement.

## Common Misconceptions
- Thinking the "if" part must be true for the statement to matter — an if-then statement is about a relationship, not a current fact.
- Reversing the direction: "If it rains, then the ground is wet" does NOT mean "If the ground is wet, then it rained" (someone could have used a hose).
- Confusing if-then with "if and only if" — "if it rains, the ground gets wet" does not mean rain is the ONLY way the ground gets wet.
- Thinking an if-then statement is false whenever the "if" part is false — in logic, an if-then statement is actually considered true whenever the condition is not met.

## Questions

```yaml
- question: "In the statement 'If you eat your vegetables, then you can have dessert,' what is the condition and what is the result?"
  type: multiple-choice
  options:
    - "Condition: you can have dessert. Result: you eat your vegetables."
    - "Condition: you eat your vegetables. Result: you can have dessert."
    - "Both parts are conditions"
    - "Both parts are results"
  answer: 1
  explanation: "The condition (the 'if' part) is 'you eat your vegetables.' The result (the 'then' part) is 'you can have dessert.' The condition comes first and must be met for the result to follow. The order matters — reversing them would create a different statement with a different meaning."

- question: "'If it rains, then the ground gets wet' means the same thing as 'If the ground is wet, then it rained.'"
  type: true-false
  answer: false
  explanation: "These are different statements. The original says rain causes wet ground. The reversed version says wet ground means it rained — but the ground could be wet for other reasons (sprinklers, a spilled bucket). Reversing an if-then statement creates a new statement that may or may not be true. This is one of the most important distinctions in logic: the original statement and its reverse (called the 'converse') are independent claims."

- question: "Which of the following is an if-then statement?"
  type: multiple-choice
  options:
    - "'Dogs are animals' — a simple fact"
    - "'Is it cold outside?' — a question"
    - "'If a shape has three sides, then it is a triangle' — a conditional claim"
    - "'Please close the window' — a request"
  answer: 2
  explanation: "'If a shape has three sides, then it is a triangle' has the if-then structure: a condition (three sides) linked to a result (it is a triangle). The other options are a fact, a question, and a request — none have the conditional structure. Any sentence that links a condition to a consequence using 'if...then' is an if-then statement."

- question: "Why is it wrong to reverse an if-then statement and assume the reverse is also true? Give an example."
  type: short-answer
  answer: "Reversing an if-then statement changes its meaning, and the reverse may be false even when the original is true. Example: 'If an animal is a dog, then it has four legs' is true. But the reverse, 'If an animal has four legs, then it is a dog,' is false — cats, horses, and many other animals also have four legs. The original says being a dog guarantees four legs. The reverse says four legs guarantee being a dog, which is a much stronger (and incorrect) claim."
  explanation: "This error — assuming the reverse of a true statement is also true — is called 'affirming the consequent' and is one of the most common logical fallacies. Teaching students to notice this at the if-then level builds resistance to this error in more complex reasoning."
```

## Explainer

You have learned that a statement is a sentence that is either true or false. Now you are going to learn about a special kind of statement that connects two ideas: the **if-then statement**.

An if-then statement has two parts. The **condition** (the "if" part) describes a situation. The **result** (the "then" part) describes what follows. "If you study hard, then you will do well on the test." The condition is studying hard. The result is doing well. The statement claims that when the condition is met, the result follows.

Notice that an if-then statement does not say the condition is true right now. It says: **whenever** the condition is true, the result will be true. "If it snows, then school closes" does not mean it is snowing right now. It means that in any situation where it snows, school closes. The if-then statement describes a rule — a connection between condition and result — not a current fact.

Here is the most important thing to understand about if-then statements: **they do not work in reverse**. "If it rains, then the ground gets wet" is true. But "If the ground is wet, then it rained" is NOT necessarily true — maybe someone turned on a sprinkler. The original statement says rain leads to wet ground. The reverse says wet ground proves rain. These are different claims. Getting comfortable with this one-directional nature is a major step in logical thinking.

If-then statements are everywhere. Every rule at school is an if-then: "If you run in the hallway, then you get a warning." Every scientific law is an if-then: "If you heat water to 100 degrees Celsius, then it boils." Every math fact can be stated as an if-then: "If a number ends in 0 or 5, then it is divisible by 5." Learning to spot, construct, and reason about if-then statements gives you a tool for understanding rules, causes, and consequences in every area of life.
