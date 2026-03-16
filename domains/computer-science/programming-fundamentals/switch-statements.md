---
id: switch-statements
title: Switch Statements and Case Selection
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: else-if-chains
  type: hard
tags:
- control-flow
- conditionals
- switch
stage: abstract-reasoning
status: draft
---

# Switch Statements and Case Selection

## Core Idea
A switch statement compares a value against multiple cases and jumps to the matching case. Fall-through behavior (without break) allows multiple cases to share code. Switch is cleaner than else-if for discrete value matching.

## How It's Best Learned
Convert an else-if chain to a switch. Test fall-through with and without break statements.

## Common Misconceptions
- Switch only works with numbers (many languages support strings and other types).
- Cases without break are always errors (fall-through can be intentional and useful).

## Explainer

You already know how else-if chains work: test one condition, then another, then another, until one matches. A **switch statement** solves the same problem — choosing among multiple alternatives — but with a different structure optimized for a specific pattern: comparing a single value against a list of known possibilities. Instead of writing `if (day == "Monday") ... else if (day == "Tuesday") ... else if (day == "Wednesday") ...`, you write `switch (day)` and list each case. The switch evaluates the expression once, then jumps directly to the matching case label.

The most important behavioral difference from else-if is **fall-through**. In most languages, when a case matches and its code executes, execution continues into the *next* case unless you explicitly insert a `break` statement. This catches many beginners off guard — they match one case, but all subsequent cases run too. The `break` statement exits the switch block entirely, and you almost always want one at the end of each case. But fall-through is not a bug in the language; it is a deliberate feature. When multiple cases should execute the same code, you can stack their labels without any code between them: `case "Saturday": case "Sunday": print("weekend"); break;` handles both weekend days with a single block.

Switch statements work best when you are matching against **discrete, known values** — days of the week, menu options, error codes, enumeration members. They are less suitable when your conditions involve ranges (`score >= 90`), complex boolean expressions, or comparisons between two different variables. In those situations, else-if chains remain the better tool. Some languages restrict switch to integers or enums; others (like JavaScript and Python's match statement) support strings, patterns, or even structural matching. Always check what your language allows.

The `default` case in a switch is the equivalent of the final `else` in an else-if chain — it catches any value that did not match a listed case. Including a default case is good practice even when you believe you have covered all possibilities, because it handles unexpected inputs gracefully and makes your assumptions explicit. If a value truly should never reach the default case, you can use it to signal an error rather than silently doing nothing.
