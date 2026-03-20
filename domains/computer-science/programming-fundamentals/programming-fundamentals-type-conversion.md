---
id: programming-fundamentals-type-conversion
title: Type Conversion and Casting
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-primitive-types
  type: hard
builds-toward:
- programming-fundamentals-comparison-operators
tags:
- types
- conversion
- casting
stage: abstract-reasoning
status: draft
---

# Type Conversion and Casting

## Core Idea
Type conversion transforms a value from one data type to another, such as converting a string "42" to the integer 42. Some conversions happen automatically (implicit); others require explicit casting. Conversions can lose information, such as when truncating decimals.

## Questions

```yaml
- question: "In Python, you run the following code: x = 3.9, then y = int(x). What is the value of y?"
  type: multiple-choice
  options:
    - "4 — Python rounds to the nearest integer"
    - "3 — integer conversion truncates the decimal part"
    - "3.9 — int() preserves the original value with a different type label"
    - "An error is raised because 3.9 is not a valid integer"
  answer: 1
  explanation: "Integer conversion truncates — it cuts off the decimal, it does not round. int(3.9) gives 3, not 4, and int(3.1) also gives 3. This is a narrowing conversion: information (the decimal part) is lost. This is a common source of subtle bugs when developers expect rounding behavior and get truncation instead."

- question: "What happens when you execute int('hello') in Python?"
  type: multiple-choice
  options:
    - "It returns 0 as a default integer value"
    - "It returns the ASCII sum of the characters in 'hello'"
    - "It raises an error because 'hello' has no meaningful integer representation"
    - "It returns the length of the string as an integer"
  answer: 2
  explanation: "Not all type conversions succeed. int() can convert strings that look like numbers — int('42') works — but it cannot handle arbitrary text. When a conversion has no meaningful result, it raises an error rather than silently returning a default. This is why checking the validity of user input before converting it is important: if someone types 'hello' where you expected a number, your program needs to handle that failure case."

- question: "Converting the float value 7.9 to an integer in most programming languages produces the result 7, not 8."
  type: true-false
  answer: true
  explanation: "Integer conversion truncates the decimal part rather than rounding. This is a narrowing conversion — the fractional information is permanently lost. The result of int(7.9) is 7 in Python, Java, C, and most other mainstream languages. Developers who expect rounding behavior will encounter subtle, hard-to-spot bugs in calculations that repeatedly truncate small fractions."

- question: "When a programming language performs an implicit type conversion, the original value can always be recovered from the converted result."
  type: true-false
  answer: false
  explanation: "Implicit conversions are not guaranteed to be reversible. For example, many languages implicitly convert integers to booleans (0 → false, any nonzero → true). The integer 5 becomes true — but you cannot recover 5 from true. Similarly, implicit promotion of an integer to a float is lossless for small integers but can lose precision for very large ones. The principle is that implicit conversions tend to go in the 'safe direction,' but 'safe' is not the same as 'fully reversible.'"

- question: "Why is it a good defensive habit to make type conversions explicit, even when the programming language would perform them implicitly?"
  type: short-answer
  answer: "Explicit conversions make your intent clear in the code — a reader (or your future self) can see that a conversion is happening and what type you expect. Implicit conversions can happen silently and produce unexpected results: a float silently truncated to an integer loses decimal precision; an integer silently coerced to a boolean loses all numerical information. When something goes wrong, explicit conversions make the conversion site visible and debuggable, whereas implicit conversions can hide the moment where type mismatch causes incorrect behavior."
  explanation: "This is about code clarity and bug visibility. Writing int(x) instead of relying on implicit conversion documents your assumption that x should be treated as an integer at this point. If that assumption is wrong, the explicit conversion makes the failure site obvious rather than buried in a chain of implicit coercions."
```

## Explainer

From your work with primitive data types, you know that integers, floats, strings, and booleans are fundamentally different kinds of values. But programs constantly need to move between these types. When a user types "25" at a console prompt, it arrives as a string — but if you want to add 10 to it, you need the integer 25. **Type conversion** is the mechanism that bridges this gap, transforming a value from one type into another so that operations make sense.

**Implicit conversion** (also called **coercion**) happens automatically when the language decides a conversion is safe and obvious. For example, in many languages, adding an integer to a float automatically promotes the integer to a float: `3 + 2.5` becomes `3.0 + 2.5` yielding `5.5`. The language widens the integer to a float because no information is lost — every integer has an exact floating-point representation. This "safe direction" principle is key: conversions that preserve all information tend to happen implicitly, while conversions that might lose data require you to be explicit about your intent.

**Explicit conversion** (or **casting**) is when you deliberately request a type change using a function or operator. In Python, `int("42")` converts the string to an integer, and `str(42)` converts the integer to a string. The important insight is that not all conversions succeed: `int("hello")` will crash because there is no meaningful way to interpret arbitrary text as a number. And some conversions that succeed still lose information — converting the float `3.9` to an integer gives you `3`, not `4`, because integer conversion truncates the decimal part rather than rounding.

Understanding which conversions are **widening** (safe, no data loss) versus **narrowing** (potentially lossy) helps you predict where bugs will appear. A float-to-integer conversion is narrowing because the decimal part vanishes. An integer-to-boolean conversion is narrowing because all nonzero values collapse to `true`. When you encounter unexpected behavior in your programs — a calculation that seems off by a fraction, or a comparison that yields a surprising result — type conversion is one of the first things to investigate. Making conversions explicit, even when the language would do them implicitly, is a defensive habit that makes your intent clear and your bugs easier to find.
