---
id: programming-fundamentals-exceptions-intro
title: Exceptions and Error Handling Introduction
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-function-definition
  type: soft
builds-toward:
- programming-fundamentals-try-catch-finally
tags:
- errors
- exceptions
- handling
stage: abstract-reasoning
status: draft
---

# Exceptions and Error Handling Introduction

## Core Idea
Exceptions are errors that occur during program execution. Instead of crashing, programs can catch exceptions and handle them gracefully. Common exceptions include division by zero, file not found, and index out of bounds.

## Explainer

When you write a function — as you learned in your prerequisite on function definitions — you expect it to receive certain inputs and produce certain outputs. But what happens when something goes wrong at runtime? A user passes a string where a number was expected, a file you need to read has been deleted, or a calculation tries to divide by zero. These are not syntax errors the compiler catches before your program runs; they are **exceptions**, problems that arise only during execution when conditions are not what your code assumed.

Without exception handling, a runtime error immediately terminates your program. Imagine a calculator app that crashes every time someone accidentally divides by zero — that is a terrible user experience. Exceptions give your program a structured way to detect the problem, respond to it, and keep running. Instead of the program halting at the error, execution jumps to a special block of code you have written specifically to deal with that kind of failure. This is the core idea: separating the "normal path" of your code from the "error path."

Most languages organize exceptions into types that describe what went wrong. A **ValueError** means the data was the wrong kind, an **IndexError** means you tried to access a position that does not exist in a list, a **FileNotFoundError** means the file you requested is missing. Each type gives you specific information about the failure, so you can respond appropriately — maybe you prompt the user for a different filename, use a default value, or log the problem and move on. The key insight is that exceptions are not random chaos; they are predictable categories of failure with names and meanings.

Think of exception handling like a safety net beneath a trapeze artist. The artist (your code) performs their routine (the normal logic), and most of the time the net is irrelevant. But when something goes wrong — a missed catch, an unexpected slip — the net is there to prevent a catastrophic fall. Your exception-handling code is that net: it does not change what the normal path does, but it guarantees that when the unexpected happens, your program lands safely instead of crashing to the ground. In the topics ahead, you will learn the specific syntax — try, catch, and finally blocks — that let you build these safety nets precisely where you need them.
