---
id: programming-fundamentals-arithmetic-operators
title: Arithmetic Operators
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-variables-assignment
  type: hard
builds-toward:
- programming-fundamentals-operator-precedence
- programming-fundamentals-comparison-operators
tags:
- operators
- arithmetic
- math
stage: abstract-reasoning
status: draft
---

# Arithmetic Operators

## Core Idea
Arithmetic operators (+, -, *, /, %) perform mathematical operations on numbers. Addition and subtraction add/remove values; multiplication and division scale values; modulo (%) returns the remainder after division.

## Questions

```yaml
- question: "In a language that performs integer division when both operands are integers, what does the expression 9 / 4 evaluate to?"
  type: multiple-choice
  options:
    - "2.25, because division always produces a decimal result"
    - "3, because computers round to the nearest integer"
    - "2, because integer division truncates toward zero, discarding the decimal part"
    - "2.0, because the result is stored as a floating-point number"
  answer: 2
  explanation: "Integer division truncates — it chops off the decimal part without rounding. 9 ÷ 4 = 2.25, but truncating gives 2, not 3. The result is also an integer (2), not a float (2.0). To get 2.25, at least one operand must be a float: 9.0 / 4 or float(9) / 4. This is one of the most common sources of silent logic errors for beginners: code that produces wrong answers with no error message because an expected decimal is silently discarded."

- question: "What does 17 % 5 evaluate to?"
  type: multiple-choice
  options:
    - "3, because 5 goes into 17 three times"
    - "3.4, because 17 divided by 5 is 3.4"
    - "2, because 5 × 3 = 15 and 17 − 15 = 2"
    - "0, because 17 is not divisible by 5"
  answer: 2
  explanation: "The modulo operator (%) returns the remainder after integer division. 5 goes into 17 three times (5 × 3 = 15), leaving a remainder of 2. So 17 % 5 = 2. Option A (3) is the quotient, not the remainder — the most common confusion. Option B (3.4) is the actual decimal division result. A useful check: dividend = (divisor × quotient) + remainder, so 17 = (5 × 3) + 2 = 15 + 2 ✓."

- question: "In most programming languages, dividing two integer values always produces a decimal (floating-point) result."
  type: true-false
  answer: false
  explanation: "In many common languages — C, C++, Java, Go, and Python 2 — dividing two integers performs integer division, which truncates the decimal portion. For example, 7 / 2 = 3, not 3.5. Python 3 is a notable exception where / always produces a float and // is the explicit integer division operator. This type-dependent behavior — the types of the operands determine the type of division performed — is a critical detail that causes silent bugs when programmers forget to account for it."

- question: "The expression count += 1 is exactly equivalent to count = count + 1 — it reads the current value, adds 1, and stores the result back in the same variable."
  type: true-false
  answer: true
  explanation: "Compound assignment operators (+=, -=, *=, /=, %=) are purely syntactic shorthand. count += 1 performs exactly the same computation as count = count + 1: retrieve count's current value, add 1, assign the result back to count. There is no difference in behavior, only in notation. They exist because updating a variable based on its current value is so common — incrementing counters, accumulating totals, scaling values — that the shorter form improves readability without changing meaning."

- question: "What is integer division, and what type of programming bug can it silently cause? Give a concrete example."
  type: short-answer
  answer: "Integer division is the behavior where dividing two integers produces an integer result by truncating (not rounding) the decimal part. For example, in a language using integer division, 7 / 2 = 3, not 3.5. This causes silent logic errors: a program computing an average with total_score / num_students would truncate any decimal average to an integer — producing a wrong answer with no error message or crash. The fix is to ensure at least one operand is a float: float(total_score) / num_students."
  explanation: "Integer division bugs are particularly insidious because they only manifest when the division is not exact. If all your test cases happen to divide evenly, the bug hides until a non-even case is encountered. Testing with inputs that produce non-integer results is essential whenever division is involved."
```

## Explainer

Now that you understand variables and assignment, arithmetic operators are how you make those stored values do useful work. You already know that a variable holds a value and that you can assign new values to it. Arithmetic operators let you compute new values from existing ones: `total = price * quantity` takes two variables you've already stored and produces a third. The result of any arithmetic expression is itself a value that can be assigned, printed, or passed along — it slots right into the variable system you already know.

The five core operators map directly to the math you already know, with one newcomer. **Addition** (`+`) and **subtraction** (`-`) work exactly as expected. **Multiplication** (`*`) and **division** (`/`) scale values up or down. The one that trips people up is **modulo** (`%`), which returns the remainder after integer division. Think of it this way: `17 % 5` asks "if I divide 17 into groups of 5, what's left over?" The answer is 2, because 5 goes into 17 three times (15) with 2 remaining. Modulo is surprisingly useful — it can tell you whether a number is even (`n % 2 == 0`), cycle through a fixed range, or extract digits from a number.

One critical detail: division behaves differently depending on the types involved. In many languages, dividing two integers performs **integer division**, which truncates the decimal part — so `7 / 2` gives `3`, not `3.5`. This is not a bug; it is a deliberate design choice rooted in how computers represent numbers. If you want the decimal result, at least one operand must be a floating-point number (e.g., `7.0 / 2`). Getting surprised by integer division is one of the most common sources of logic errors for beginners.

Finally, arithmetic operators combine with assignment in a natural way. Instead of writing `count = count + 1`, most languages offer shorthand like `count += 1`. These **compound assignment operators** (`+=`, `-=`, `*=`, `/=`, `%=`) are just syntactic sugar — they do exactly the same thing as writing the long form. They exist because updating a variable based on its current value is so common that a shorter notation pays for itself in readability. Once you're comfortable with these five operators and how they interact with variable assignment, you have the basic machinery to express any computation.
