---
id: boolean-logic
title: Boolean Type and Truth Values
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: memory-and-data-storage
  type: hard
- id: boolean-algebra
  type: soft
- id: truth-tables
  type: soft
builds-toward:
- comparison-operators
- logical-operators
- conditional-statements
- while-loops
- loop-control-statements
tags:
- types
- boolean
- logic
stage: formal-systems
status: validated
---
# Boolean Type and Truth Values

## Core Idea
The boolean type represents two values: true and false. Booleans are produced by comparisons and logical operations, and are used to make decisions in programs through conditionals and loops.

## How It's Best Learned
Write expressions that evaluate to true or false. Explore how different comparisons produce booleans.

## Common Misconceptions
- Booleans are just flags (they are first-class values that can be stored and reasoned about).
- True and false are numbers (they are distinct values; some languages may convert them, but they're conceptually different).

## Questions

```yaml
- question: "A programmer writes: is_raining = temperature < 32. When temperature holds the value 45, what is stored in is_raining?"
  type: multiple-choice
  options:
    - "45"
    - "32"
    - "true"
    - "false"
  answer: 3
  explanation: "The expression temperature < 32 asks: 'Is 45 less than 32?' The answer is no, so the comparison evaluates to false. That boolean value false is then stored in is_raining. The key insight is that the result of a comparison is itself a value — not the numbers involved in the comparison."

- question: "Which statement best describes what the expression x > 10 produces when evaluated in a program?"
  type: multiple-choice
  options:
    - "The number 1 if x is greater than 10, or 0 otherwise"
    - "A boolean value — either true or false — depending on x's current value"
    - "Nothing — it tests a condition but does not produce a storable value"
    - "The difference between x and 10"
  answer: 1
  explanation: "A comparison expression evaluates to a boolean value. x > 10 produces true when x is greater than 10, and false otherwise. This is a first-class value, just like a number or text string — it can be stored, passed to a function, or used in a conditional. Option A confuses the conceptual result with how some languages internally represent it."

- question: "The result of a comparison like age >= 18 can be stored in a variable, just like a number or text value."
  type: true-false
  answer: true
  explanation: "Booleans are first-class values in programming. Writing is_adult = age >= 18 is perfectly valid — the comparison evaluates to either true or false, and that value is stored in is_adult. You can then use is_adult anywhere a boolean is expected, rather than repeating the comparison."

- question: "Because booleans represent simple yes/no answers, each comparison must stand on its own — boolean values cannot be combined with other operations."
  type: true-false
  answer: false
  explanation: "Booleans can absolutely be combined using logical operators: AND, OR, and NOT. For example, is_adult AND is_registered produces a single boolean that is true only when both conditions hold. This ability to compose boolean values is precisely what makes them powerful — it allows complex decision logic to be built from simple comparisons."

- question: "A classmate argues that booleans are just 0 and 1 and there's no reason to treat them differently from numbers. Why is this view incomplete?"
  type: short-answer
  answer: "While many languages internally represent true as 1 and false as 0, booleans carry logical meaning that numbers do not. A variable named is_logged_in communicates intent clearly; a variable named login_status holding 1 does not. Booleans also connect naturally to logical reasoning (AND, OR, NOT), which operates on propositions rather than quantities. Treating them as mere numbers leads to code that is harder to read and reason about."
  explanation: "The distinction matters most for clarity and intent. The variable name is_logged_in tells anyone reading the code exactly what it represents — a yes/no state. It also signals that the right operations to apply are logical (combine with AND, negate with NOT), not arithmetic (add, subtract). Using 0/1 invites errors like accidentally doing arithmetic on a 'flag' value, while also obscuring the code's meaning."
```

## Explainer

You already understand that computers store data in memory and that variables hold values. The **boolean type** is the simplest data type possible: it has exactly two values, **true** and **false**. Named after mathematician George Boole, booleans represent the answers to yes-or-no questions. Is 5 greater than 3? True. Is "hello" equal to "goodbye"? False. Every comparison you write in a program produces a boolean result.

Booleans are created most often through **comparison operators**. When you write `x > 10`, the computer evaluates this expression and produces either true or false depending on the current value of x. The expression `temperature == 100` checks equality and produces true or false. These comparisons — greater than, less than, equal to, not equal to — are the basic building blocks that generate boolean values. The key insight is that the result of a comparison is itself a value, just like the number 42 or the text "hello". You can store it in a variable: `is_adult = age >= 18` puts either true or false into `is_adult`.

What makes booleans powerful is that they are the language of **decisions** in programs. Every time a program chooses between two paths — should I show an error message or continue? should I keep looping or stop? — it evaluates a boolean expression. The `if` statement you'll encounter next takes a boolean and executes one block of code when it's true and optionally another when it's false. Loops repeat as long as a boolean condition remains true. Without booleans, programs would execute the same instructions every time with no ability to respond to different situations.

A common source of confusion is the relationship between booleans and numbers. In many languages, true behaves like 1 and false like 0 when used in arithmetic, and non-zero numbers are treated as "truthy" in boolean contexts. But treating booleans as mere numbers misses their purpose. A boolean carries **meaning** — it represents a logical proposition, not a quantity. The variable `is_logged_in` communicates intent in a way that the number 1 never could. As you move into logical operators and conditionals, thinking of booleans as answers to questions rather than as numbers will make your code clearer and your reasoning more precise.
