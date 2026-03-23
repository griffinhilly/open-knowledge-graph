---
id: code-comments-and-style
title: Code Comments and Style
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: hello-world
  type: soft
builds-toward:
- function-design-and-contracts
tags:
- documentation
- readability
- best-practices
stage: formal-systems
status: validated
---
# Code Comments and Style

## Core Idea
Comments explain why code exists, not what it does (the code itself shows what). Consistent style—indentation, naming, spacing—makes code readable for yourself later and for others. Good comments and style are markers of professional programming.

## How It's Best Learned
Read others' code and notice which comments help you understand intent; practice re-reading your own code after a week and revising unclear sections.

## Common Misconceptions
That every line needs a comment; actually, clear code with well-named variables needs fewer comments. Comments should explain intent, not restate the code.

## Questions

```yaml
- question: "A developer writes: `total = price * quantity  # multiply price by quantity`. A reviewer flags this comment. Why?"
  type: multiple-choice
  options:
    - "The comment is in the wrong location — it should be above the line, not inline"
    - "The comment restates what the code already shows and adds no useful information"
    - "Multiplication should not be commented because it is a built-in operation"
    - "The variable names are unclear and should be fixed before any comment is added"
  answer: 1
  explanation: "The comment 'multiply price by quantity' exactly restates what `price * quantity` already communicates to any reader who knows the language. Good comments explain WHY the code does what it does — the intent, the constraint, the non-obvious choice — not WHAT the code does, which the code itself shows. This comment adds visual noise without adding knowledge. A useful comment here might explain why this specific formula is used (e.g., '# before tax; tax applied separately in checkout module')."

- question: "A programmer has a complex 20-line block that computes a priority score. They are about to write a long comment explaining the formula. What should they consider first?"
  type: multiple-choice
  options:
    - "Whether the comment should be in the function header instead of inline"
    - "Whether refactoring the code into a well-named function would eliminate the need for the comment"
    - "Whether the programming language supports multi-line comment syntax"
    - "Whether the formula has already been documented in external specifications"
  answer: 1
  explanation: "When a comment needs to be long to explain complex logic, that is often a signal that the code can be refactored to be more self-explanatory. A function named `calculate_priority_score(urgency, recency, user_tier)` communicates intent without any comment. The block inside may still benefit from a brief comment explaining the business rule it encodes, but the primary question should always be: 'Can I make the code clearer so less explanation is needed?' Refactoring to reduce comment burden produces more maintainable code than extensive commenting of hard-to-follow code."

- question: "Using consistent indentation and naming conventions matters more for long-term maintainability than which specific convention is chosen."
  type: true-false
  answer: true
  explanation: "The specific convention — 2 vs 4 spaces, camelCase vs snake_case — matters far less than applying any convention consistently throughout a codebase. Mixed conventions force readers to spend mental energy parsing formatting instead of logic. Most languages have community standards (Python's PEP 8, JavaScript's various style guides) that reduce decision fatigue, but the fundamental principle is consistency within a project. A team that uses a non-standard but consistent style will outperform a team that uses the 'correct' style inconsistently."

- question: "Code that is well-named and clearly structured still requires comments on most lines to be considered professional quality."
  type: true-false
  answer: false
  explanation: "This inverts the principle. Well-named, clearly structured code requires *fewer* comments, not more. The goal is self-documenting code: variable and function names that express intent, logical structure that reveals flow, and comments only where the code cannot speak for itself — edge cases, non-obvious choices, constraints from external systems. Adding comments to every line of readable code makes the code harder to scan by increasing visual noise. Professional-quality code uses comments surgically, not pervasively."

- question: "Why should comments explain 'why' rather than 'what,' and what kinds of 'why' are most valuable to document?"
  type: short-answer
  answer: "The 'what' is already visible in the code — any reader who knows the language can see what operations are performed. The 'why' is what the code cannot show: the business rule being enforced, the bug being worked around, the alternative approach considered and rejected, the external constraint that forced an unusual choice. The most valuable 'why' comments include: explaining a non-obvious algorithm choice ('using binary search here because this list is always pre-sorted'), documenting a workaround ('off-by-one added to compensate for the API's 1-indexed responses'), and warning about fragile dependencies ('this order matters — module X must be initialized before Y')."
  explanation: "Comments that restate what the code does become liabilities: they can go stale when the code changes but the comment is not updated, creating misleading documentation. Comments that explain why rarely go stale — the business rule or constraint usually persists even when the implementation changes. Separating 'what' (code's job) from 'why' (comment's job) produces documentation that remains accurate and useful over time."
```

## Explainer

Now that you have written your first programs, you have likely noticed that code you wrote last week can look confusing when you return to it. Comments and consistent style are the tools that prevent this — they make code readable not just to the computer, but to the human who will maintain it, which is most often your future self.

A **comment** is text that the language ignores during execution. In Python, anything after a `#` on a line is a comment; in JavaScript and C-family languages, `//` marks a single-line comment and `/* ... */` wraps multi-line comments. The most important rule about comments is that they should explain **why**, not **what**. A comment like `x = x + 1  # increment x` is worse than useless — it restates the obvious and adds visual noise. A comment like `x = x + 1  # compensate for zero-based index when displaying to user` tells the reader something the code alone cannot. Good comments capture intent, document edge cases, warn about non-obvious behavior, and explain *why* a particular approach was chosen over an alternative.

**Style** encompasses everything about how code is formatted: indentation width, where braces go, how variables and functions are named, how blank lines separate logical sections. None of these choices affect what the program does, but they profoundly affect how quickly someone can read and understand it. Most languages have community conventions — Python's PEP 8 recommends 4-space indentation and snake_case for variable names; JavaScript communities often use camelCase and 2-space indentation. The specific convention matters less than **consistency**: mixing tabs and spaces, or alternating between `myVariable` and `my_variable` in the same file, forces the reader to spend mental energy on formatting instead of logic.

A practical guideline is to make your code as self-documenting as possible through clear naming, then add comments only where the code cannot speak for itself. A function named `calculate_shipping_cost` with parameters `weight` and `destination` needs far fewer comments than one named `calc` with parameters `w` and `d`. When you find yourself writing a long comment to explain a complex block, consider whether refactoring the code — extracting a well-named function, renaming a variable, or simplifying the logic — would eliminate the need for the comment entirely. The best code reads like well-structured prose; comments fill in the gaps where the prose alone is insufficient.
