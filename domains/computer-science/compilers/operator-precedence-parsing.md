---
id: operator-precedence-parsing
title: Operator Precedence Parsing
domain: computer-science
course: compilers
prerequisites:
- id: context-free-grammars
  type: hard
- id: parsing-problem-overview
  type: hard
builds-toward:
- grammar-design-for-compilation
tags:
- parsing
- operators
- grammars
stage: advanced
status: validated
---

# Operator Precedence Parsing

## Core Idea
Operator precedence parsing handles expressions by assigning precedence levels to operators and parsing operands recursively at appropriate precedence levels. This eliminates special grammar rules and allows direct parsing of flat operator sequences. Widely used in expression evaluators and scripting languages.

## How It's Best Learned
Implement a simple arithmetic expression parser using precedence climbing, then verify it handles mixed operators (+, *, ^) correctly with proper evaluation order.

## Common Misconceptions
Precedence and associativity are the same thing—they're separate. Right-associativity requires different handling than left-associativity in recursive descent.

## Questions

```yaml
- question: "In a precedence climbing parser, a left-associative operator at precedence level P triggers a recursive call for the right operand with minimum precedence P+1. What would change if P were used instead of P+1 in that recursive call?"
  type: multiple-choice
  options:
    - "The parser would become more efficient, reducing the number of recursive calls needed"
    - "The operator would be treated as right-associative — expressions like a+b+c would parse as a+(b+c) instead of (a+b)+c"
    - "The parser would enter an infinite loop because the recursion would never terminate"
    - "Higher-precedence operators would no longer bind more tightly than lower-precedence ones"
  answer: 1
  explanation: "Using P in the recursive call allows the recursive invocation to immediately consume another operator at the same precedence level, grouping it on the right — which is exactly right-associativity. Using P+1 instead raises the threshold just enough to prevent consuming same-level operators inside the recursion, so they are left for the outer call to handle in left-to-right order. This single +1 difference is the entire mechanism that separates left- from right-associativity in a precedence climbing parser."

- question: "Consider parsing `2 ^ 3 ^ 4` where ^ has precedence 3 and is right-associative. Which parse does a correctly implemented precedence climbing parser produce?"
  type: multiple-choice
  options:
    - "(2 ^ 3) ^ 4, because the leftmost operator is encountered and consumed first"
    - "2 ^ (3 ^ 4), because right-associativity uses the same precedence (not +1) in the recursive call, allowing the second ^ to be consumed inside the recursion"
    - "((2 ^ 3) ^ 4), because precedence climbing always produces left-associative grouping by default"
    - "The expression cannot be parsed without explicit parentheses when the same operator appears twice"
  answer: 1
  explanation: "For right-associative ^, the recursive call for the right operand uses minimum precedence = 3 (same as ^, not 3+1). When parsing the right side after the first ^, the parser reads 3, then sees another ^ at precedence 3 which meets the threshold, so it consumes it inside the recursion, producing 3^4. Back in the outer call, the result is 2^(3^4). If ^ were left-associative, the recursive call would use minimum precedence 4, blocking consumption of the second ^ inside the recursion, and the outer call would handle it, producing (2^3)^4."

- question: "Operator precedence and operator associativity describe the same property — how tightly an operator binds to its operands."
  type: true-false
  answer: false
  explanation: "Precedence and associativity are distinct concepts requiring separate handling. Precedence determines which operator binds more tightly when *different* precedence levels appear together — for example, * binds tighter than + so 2+3*4 = 2+(3*4). Associativity determines how operators at the *same* precedence level group — left-associative means a−b−c = (a−b)−c (group left), right-associative means a^b^c = a^(b^c) (group right). Confusing them is the most common misconception in this topic."

- question: "A grammar-based parser using separate nonterminals for each precedence level can express the same expression languages as a precedence climbing parser."
  type: true-false
  answer: true
  explanation: "Both approaches implement the same underlying context-free grammar for arithmetic expressions with precedence and associativity. Precedence climbing is a parsing *algorithm* that encodes the grammar implicitly through its threshold logic, while the grammar-based approach encodes it explicitly through nonterminal structure (Expr → Expr + Term, Term → Term * Factor, etc.). The two are equivalent in expressive power; precedence climbing is simply more compact and easier to extend when new operators are added."

- question: "Explain how the threshold value passed to recursive calls in a precedence climbing parser enforces both operator precedence and operator associativity."
  type: short-answer
  answer: "The threshold controls which operators the current recursive call is allowed to consume. If the next operator's precedence is below the threshold, the recursive call returns without consuming it, leaving the operator for its caller — this enforces precedence, since low-precedence operators are always handled by outer (earlier) calls and group last. Associativity is controlled by the threshold passed when recursing for the right operand of a binary operator: left-associative operators pass threshold = current precedence + 1, which prevents consuming another same-level operator inside the recursion (forcing left-grouping by returning it to the outer call); right-associative operators pass threshold = current precedence, which allows consuming another same-level operator inside the recursion (forcing right-grouping). The two behaviors differ by exactly one integer."
  explanation: "The elegance of precedence climbing is that both precedence and associativity are encoded in a single integer parameter. There are no special cases or lookup tables — just arithmetic on the threshold value passed to each recursive call."
```

## Explainer

When you learned about context-free grammars, you saw how to encode arithmetic expressions using multiple nonterminals — one for each precedence level. A grammar for `+` and `*` might have `Expr → Expr + Term`, `Term → Term * Factor`, `Factor → number | ( Expr )`. This works, but it is verbose: every new operator means another nonterminal and another level of recursion. **Operator precedence parsing** collapses all of that into a single algorithm driven by a table of precedence levels and associativity rules.

The core insight is that an expression like `3 + 4 * 5 + 2` is really a flat sequence of operands and operators, and all you need to decide is where to place the implicit parentheses. The **precedence climbing** (or Pratt parsing) algorithm handles this elegantly. It parses an operand, then enters a loop: as long as the next operator has precedence at or above a threshold (the "minimum precedence"), it consumes the operator and recursively parses the right-hand operand at a higher minimum precedence. For left-associative operators, the recursive call uses `precedence + 1` as its minimum; for right-associative operators, it uses `precedence` unchanged. This one difference in the recursive call is all that separates `2 ^ 3 ^ 4` being parsed as `2 ^ (3 ^ 4)` versus `(2 ^ 3) ^ 4`.

Consider parsing `3 + 4 * 5`. The algorithm reads `3`, then sees `+` with precedence 1 (meeting the initial threshold of 0). It consumes `+`, then recursively parses the right side at minimum precedence 2. Inside that recursive call, it reads `4`, sees `*` with precedence 2 (meeting the threshold), consumes `*`, and parses `5`. Now it checks again — there are no more operators, so it returns `4 * 5`. Back in the outer call, the result is `3 + (4 * 5)`. The precedence threshold naturally caused `*` to bind tighter than `+` without any grammar rewriting.

This technique is remarkably practical. Most hand-written parsers for real programming languages — including early versions of GCC and many scripting language interpreters — use some form of operator precedence parsing for expressions. Adding a new operator is trivial: assign it a precedence level and associativity, and the algorithm handles it automatically. The trade-off is that this approach only works for binary infix operators (plus unary prefix operators with a small extension). Constructs like ternary operators, array indexing, or function calls require special handling outside the precedence loop. But for the expression subset of a language, precedence parsing is hard to beat in simplicity and extensibility.
