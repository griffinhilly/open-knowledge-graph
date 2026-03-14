---
id: floating-point-representation
title: Floating Point Representation
domain: mathematics
course: numerical-analysis
prerequisites: []
builds-toward:
- machine-epsilon
- rounding-errors
tags:
- floating-point
- representation
- computer-arithmetic
stage: abstract-reasoning
status: draft
---

# Floating Point Representation

## Core Idea
Floating point numbers are represented in computers using a fixed number of bits: a sign bit, an exponent, and a mantissa (fractional part). The IEEE 754 standard defines how these are encoded and how arithmetic operations are performed. This limited precision representation allows computers to store a wide range of values but introduces systematic errors in computation.
