---
id: operator-precedence-and-evaluation
title: Operator Precedence and Order of Evaluation
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: arithmetic-operators-intro
  type: hard
- id: comparison-operators-and-relations
  type: hard
- id: logical-operators-and-gates
  type: hard
builds-toward:
- conditional-statements
tags:
- operators
- precedence
- evaluation
stage: abstract-reasoning
status: draft
---

# Operator Precedence and Order of Evaluation

## Core Idea
Operator precedence determines the order in which operators are applied in complex expressions. Parentheses override precedence. Understanding evaluation order is essential for writing correct expressions and debugging subtle bugs.

## How It's Best Learned
Evaluate complex expressions with mixed operators. Use parentheses to override precedence and compare results.

## Common Misconceptions
- Operators are always evaluated left to right (precedence and associativity matter; some languages have special rules).
- Parentheses are always necessary for clarity (they're helpful but the precedence rules still apply).

## Questions

```yaml
- question: "What does the Python expression `not False or True and False` evaluate to?"
  type: multiple-choice
  options:
    - "False — evaluated strictly left to right: (not False or True) = True, then True and False = False"
    - "True — 'not' is highest precedence, then 'and', then 'or': not False = True, True and False = False, True or False = True"
    - "False — 'or' is highest precedence, so the whole thing reduces to False"
    - "True — because any expression containing True evaluates to True"
  answer: 1
  explanation: "Applying correct precedence: 'not' (unary) is applied first → 'not False' = True. Then 'and' binds more tightly than 'or': 'True and False' = False. Then 'or': 'True or False' = True. Option A shows the classic left-to-right misconception: if you evaluate left-to-right ignoring precedence, you get '(not False or True) and False' = '(True or True) and False' = 'True and False' = False. This demonstrates precisely why operator precedence matters — the same expression evaluated in two different orders produces different results."

- question: "Which of the following best illustrates why operator associativity matters independently of operator precedence?"
  type: multiple-choice
  options:
    - "The expression `a > b and c > d` produces a boolean result"
    - "`2 ** 3 ** 2` evaluates to 512 (right-associative) rather than 64 (left-associative), a difference of nearly 8x"
    - "The expression `a + b * c` requires knowing the precedence of + vs *"
    - "`a and b or c` requires knowing the precedence of 'and' vs 'or'"
  answer: 1
  explanation: "Associativity determines evaluation order when two operators have equal precedence. Exponentiation in Python is right-associative: `2 ** 3 ** 2` is parsed as `2 ** (3 ** 2)` = `2 ** 9` = 512. If it were left-associative, it would be `(2 ** 3) ** 2` = `8 ** 2` = 64. This is not about which operator is 'stronger' (both are **) but about which direction evaluation proceeds. The other options involve operators of different precedence levels, making them examples of precedence, not associativity."

- question: "The expression `x + 3 > 10` is evaluated as `(x + 3) > 10` because arithmetic operators have higher precedence than comparison operators."
  type: true-false
  answer: true
  explanation: "Arithmetic operators (+, -, *, /) sit higher in the precedence hierarchy than comparison operators (>, <, ==, !=). So in `x + 3 > 10`, the addition is applied first, producing a number, which is then compared to 10. This is the intuitive and expected behavior — you almost certainly want 'is (x plus 3) greater than 10?' rather than 'is x greater than (3 greater than 10)?'. The fact that precedence matches our intuition here is why many programmers don't notice when it doesn't."

- question: "All binary operators in programming languages are evaluated left to right when they appear in sequence."
  type: true-false
  answer: false
  explanation: "Most binary operators are left-associative (evaluated left to right), but important exceptions exist. Exponentiation (**) in Python is right-associative, as is assignment (=) in most languages: `a = b = 5` assigns 5 to b first, then assigns the result to a (right to left). Assuming universal left-to-right evaluation is a reliable source of bugs, especially when working with exponentiation or chained assignment. The safe habit is to use parentheses whenever the evaluation order matters and isn't immediately obvious."

- question: "A programmer writes `if x > 0 and y > 0 or z > 0` intending it to mean 'both x and y are positive, or z is positive.' Explain what the expression actually evaluates to, and how to fix it."
  type: short-answer
  answer: "Because 'and' has higher precedence than 'or', the expression is evaluated as `(x > 0 and y > 0) or z > 0` — which happens to match the programmer's intent. However, if the programmer had written `x > 0 or y > 0 and z > 0` meaning 'either x is positive, or both y and z are positive', that would also evaluate as written. The safe fix in any ambiguous case is to add explicit parentheses: `(x > 0 and y > 0) or z > 0` to make the intent unambiguous to both the compiler and to future readers."
  explanation: "In this particular case the programmer got lucky — 'and' before 'or' matches their intent. But relying on precedence rules to carry intent without parentheses is a readability and maintenance hazard. When reviewing code, a reader who doesn't immediately remember the and/or precedence ordering will have to look it up. Parentheses make intent explicit at zero runtime cost. The general principle: use parentheses for anything involving mixed logical operators."
```

## Explainer

From arithmetic operators, comparison operators, and logical operators, you know three families of operators that each produce results — numbers, booleans from comparisons, and booleans from logical combinations. When these operators appear together in a single expression like `x + 3 > 10 and y * 2 < 20`, the computer needs a set of rules to determine which operations happen first. **Operator precedence** is that set of rules — it defines a hierarchy that determines the order in which operators are applied, exactly as the mathematical convention "multiplication before addition" determines that `2 + 3 × 4` equals 14, not 20.

The general precedence hierarchy across most languages, from highest (evaluated first) to lowest, is: **parentheses** → **unary operators** (NOT, negation) → **arithmetic** (first multiplication/division/modulus, then addition/subtraction) → **comparison** (>, <, ==, !=) → **logical AND** → **logical OR**. So the expression `x + 3 > 10 and y * 2 < 20` is evaluated as `((x + 3) > 10) and ((y * 2) < 20)` — arithmetic first, then comparisons, then the logical AND combines the two boolean results. You never need to memorize the entire precedence table; knowing the broad categories (arithmetic beats comparison beats logic) and using parentheses for anything non-obvious is the practical approach.

When two operators have the **same precedence**, **associativity** determines the order. Most binary operators are **left-associative**: `a - b - c` is evaluated as `(a - b) - c`, left to right. The notable exception is exponentiation in languages that have it (`**` in Python): `2 ** 3 ** 2` evaluates as `2 ** (3 ** 2)` = `2 ** 9` = 512, not `(2 ** 3) ** 2` = 64, because exponentiation is **right-associative**. Assignment is another right-associative operator: `a = b = 5` assigns 5 to b first, then assigns the result to a.

**Parentheses always override precedence**, and this is the most important practical rule. If you are unsure whether `a + b * c` means what you intend, add parentheses: `a + (b * c)` or `(a + b) * c`. Parentheses make your intent explicit to both the compiler and to anyone reading your code. The common mistake is not that programmers fail to memorize precedence tables — it is that they *assume* left-to-right evaluation when precedence or associativity dictates otherwise. When debugging an expression that produces an unexpected result, add parentheses to match what you *think* the evaluation order is, then compare with what the language actually does. The discrepancy, when it exists, is almost always a precedence or associativity issue.
