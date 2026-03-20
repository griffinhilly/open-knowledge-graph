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

## Questions

```yaml
- question: "A programmer writes `if (score = 100)` instead of `if (score == 100)`. What does this code actually do in most languages?"
  type: multiple-choice
  options:
    - "It checks whether score equals 100 and runs the if-block only if true"
    - "It assigns 100 to score and then evaluates the result of that assignment as the condition, often always running the if-block"
    - "It causes a syntax error that prevents the program from running"
    - "It compares score to 100 using the most recent assignment's value"
  answer: 1
  explanation: "The single equals sign `=` is assignment, not comparison. `score = 100` sets score to 100 and typically evaluates to the assigned value (100 in this case). Since 100 is non-zero, the condition is treated as true, and the if-block runs regardless of what score was before. This is one of the most dangerous bugs in programming because it is syntactically valid in many languages, produces no error, and causes subtle incorrect behavior. The double equals `==` is the comparison operator."

- question: "In Java, two String objects are created: `String a = new String(\"hello\")` and `String b = new String(\"hello\")`. The expression `a == b` evaluates to false even though both contain 'hello'. Why?"
  type: multiple-choice
  options:
    - "Strings are compared alphabetically in Java, and identical strings always return false"
    - "`==` checks identity — whether two variables refer to the same object in memory — not equality of their contents"
    - "Java does not allow `==` to be used with String objects"
    - "The comparison fails because `new String()` creates immutable objects that cannot be compared"
  answer: 1
  explanation: "This illustrates the identity vs. equality distinction. Each `new String(\"hello\")` creates a separate object in memory, so `a` and `b` point to different locations even though their contents are identical. `==` in Java checks whether two references point to the same object (identity), not whether the objects have the same value (equality). To compare String contents, you use `.equals()`. This distinction becomes critical with any non-primitive type, and forgetting it produces bugs that are hard to trace because the values look the same when printed."

- question: "The expression `7 != 7` evaluates to true because the `!=` operator checks if two values are not equal."
  type: true-false
  answer: false
  explanation: "`7 != 7` evaluates to false. The statement correctly defines what `!=` means, but misapplies it: since 7 does equal 7, the 'not equal' check returns false. The confusion here is between knowing the definition of an operator and correctly applying it. `!=` returns true only when the values differ (e.g., `7 != 8` is true). The question is designed to test whether a student can apply the operator rather than just recite its definition."

- question: "Comparison operators like `<`, `>`, and `==` always produce a boolean result — true or false — regardless of the types being compared."
  type: true-false
  answer: true
  explanation: "This is the defining property of comparison operators: their output type is always boolean. `5 > 3` returns true. `\"apple\" < \"banana\"` returns true (lexicographic comparison). `4.0 == 4` returns true (numeric equality after type coercion in most languages). This is why comparisons connect directly to conditional statements and loops — every branching decision in a program ultimately depends on a boolean value, and comparison operators are the primary way to produce those booleans at runtime."

- question: "Explain the difference between `=` and `==` in programming. Why is confusing them a particularly dangerous mistake?"
  type: short-answer
  answer: "`=` is assignment: it stores a value in a variable, changing program state. `==` is comparison: it tests whether two values are equal and produces a boolean without changing anything. Confusing them is dangerous because in many languages, writing `=` inside a condition is syntactically legal — the program runs without error but behaves incorrectly. The variable gets assigned a new value, the condition evaluates the assigned value (often truthy), and the bug can be hard to find because the code 'looks right' at a glance."
  explanation: "This bug is so common it has a name in some communities: 'the accidental assignment.' Languages like Python make it a syntax error in conditions specifically to prevent it. C and C++ don't, which is why the convention `if (100 == score)` (Yoda conditions) developed — putting the constant first makes the error `if (100 = score)` a compile-time error. Understanding *why* a mistake is dangerous, not just that it's wrong, is what allows you to guard against it and understand the error when you finally see it."
```

## Explainer

You already know that variables hold values of different types — integers, floats, booleans. Comparison operators let you ask questions about those values: is this number bigger than that one? Are these two strings the same? The answer is always a **boolean** — `true` or `false`. This is what connects comparison operators to the boolean type you studied earlier: comparisons are the primary way your program produces boolean values at runtime, and those booleans drive every decision your program makes.

The six **relational operators** are `<` (less than), `>` (greater than), `<=` (less than or equal), `>=` (greater than or equal), `==` (equal to), and `!=` (not equal to). For numbers, these work exactly as you would expect from mathematics: `5 > 3` is `true`, `2 == 2` is `true`, `4 != 4` is `false`. You can also compare characters and strings, where the ordering is typically alphabetical (more precisely, lexicographic based on character encoding). So `"apple" < "banana"` is `true` because "a" comes before "b".

The single most important distinction to internalize is between `=` and `==`. The single equals sign (`=`) is **assignment** — it stores a value in a variable. The double equals sign (`==`) is **comparison** — it tests whether two values are the same. Writing `if (x = 5)` when you mean `if (x == 5)` is one of the most common bugs in programming: instead of checking whether x equals 5, it assigns 5 to x and then treats that assignment's result as a condition. Some languages catch this as an error; others silently do the wrong thing. Train yourself to read `==` as "is equal to?" and `=` as "gets the value of."

As you encounter more complex types — lists, objects, custom data structures — the meaning of `==` becomes less obvious. Does comparing two lists check whether they are the same list in memory, or whether they contain the same elements? This is the distinction between **identity** (are these the same object?) and **equality** (do these objects have the same value?). Different languages handle this differently: Python's `==` checks equality while `is` checks identity; Java's `==` checks identity for objects while `.equals()` checks equality. For now, with simple numeric and boolean types, `==` behaves intuitively. But knowing that this complexity exists will prepare you for when you encounter it.
