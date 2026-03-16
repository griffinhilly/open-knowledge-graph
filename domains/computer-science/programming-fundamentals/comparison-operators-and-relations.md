---
id: comparison-operators-and-relations
title: Comparison Operators and Relational Expressions
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: integer-and-floating-point-types
  type: hard
- id: boolean-type-and-truth-values
  type: hard
builds-toward:
- logical-operators-and-gates
tags:
- operators
- comparison
- relations
stage: abstract-reasoning
status: draft
---

# Comparison Operators and Relational Expressions

## Core Idea
Comparison operators (<, >, <=, >=, ==, !=) compare two values and produce a boolean result. These are fundamental for making decisions; understanding equality vs. identity is crucial for correct comparisons.

## How It's Best Learned
Write comparison expressions and predict their results. Compare different types and see type coercion behavior.

## Common Misconceptions
- == and = mean the same thing (= assigns; == compares).
- All types can be safely compared with == (some comparisons may not be meaningful, e.g., comparing objects by reference vs. value).

## Explainer

You already know that variables hold values of different types — integers, floats, booleans. Comparison operators let you ask questions about those values: is this number bigger than that one? Are these two strings the same? The answer is always a **boolean** — `true` or `false`. This is what connects comparison operators to the boolean type you studied earlier: comparisons are the primary way your program produces boolean values at runtime, and those booleans drive every decision your program makes.

The six **relational operators** are `<` (less than), `>` (greater than), `<=` (less than or equal), `>=` (greater than or equal), `==` (equal to), and `!=` (not equal to). For numbers, these work exactly as you would expect from mathematics: `5 > 3` is `true`, `2 == 2` is `true`, `4 != 4` is `false`. You can also compare characters and strings, where the ordering is typically alphabetical (more precisely, lexicographic based on character encoding). So `"apple" < "banana"` is `true` because "a" comes before "b".

The single most important distinction to internalize is between `=` and `==`. The single equals sign (`=`) is **assignment** — it stores a value in a variable. The double equals sign (`==`) is **comparison** — it tests whether two values are the same. Writing `if (x = 5)` when you mean `if (x == 5)` is one of the most common bugs in programming: instead of checking whether x equals 5, it assigns 5 to x and then treats that assignment's result as a condition. Some languages catch this as an error; others silently do the wrong thing. Train yourself to read `==` as "is equal to?" and `=` as "gets the value of."

As you encounter more complex types — lists, objects, custom data structures — the meaning of `==` becomes less obvious. Does comparing two lists check whether they are the same list in memory, or whether they contain the same elements? This is the distinction between **identity** (are these the same object?) and **equality** (do these objects have the same value?). Different languages handle this differently: Python's `==` checks equality while `is` checks identity; Java's `==` checks identity for objects while `.equals()` checks equality. For now, with simple numeric and boolean types, `==` behaves intuitively. But knowing that this complexity exists will prepare you for when you encounter it.
