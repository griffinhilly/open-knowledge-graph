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

## Explainer

From your work with primitive data types, you know that integers, floats, strings, and booleans are fundamentally different kinds of values. But programs constantly need to move between these types. When a user types "25" at a console prompt, it arrives as a string — but if you want to add 10 to it, you need the integer 25. **Type conversion** is the mechanism that bridges this gap, transforming a value from one type into another so that operations make sense.

**Implicit conversion** (also called **coercion**) happens automatically when the language decides a conversion is safe and obvious. For example, in many languages, adding an integer to a float automatically promotes the integer to a float: `3 + 2.5` becomes `3.0 + 2.5` yielding `5.5`. The language widens the integer to a float because no information is lost — every integer has an exact floating-point representation. This "safe direction" principle is key: conversions that preserve all information tend to happen implicitly, while conversions that might lose data require you to be explicit about your intent.

**Explicit conversion** (or **casting**) is when you deliberately request a type change using a function or operator. In Python, `int("42")` converts the string to an integer, and `str(42)` converts the integer to a string. The important insight is that not all conversions succeed: `int("hello")` will crash because there is no meaningful way to interpret arbitrary text as a number. And some conversions that succeed still lose information — converting the float `3.9` to an integer gives you `3`, not `4`, because integer conversion truncates the decimal part rather than rounding.

Understanding which conversions are **widening** (safe, no data loss) versus **narrowing** (potentially lossy) helps you predict where bugs will appear. A float-to-integer conversion is narrowing because the decimal part vanishes. An integer-to-boolean conversion is narrowing because all nonzero values collapse to `true`. When you encounter unexpected behavior in your programs — a calculation that seems off by a fraction, or a comparison that yields a surprising result — type conversion is one of the first things to investigate. Making conversions explicit, even when the language would do them implicitly, is a defensive habit that makes your intent clear and your bugs easier to find.
