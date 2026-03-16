---
id: programming-fundamentals-console-io
title: Console Input and Output
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-variables-assignment
  type: hard
builds-toward:
- programming-fundamentals-file-io
tags:
- io
- input
- output
- console
stage: abstract-reasoning
status: draft
---

# Console Input and Output

## Core Idea
Console I/O allows programs to communicate with the user via text. Output (printing) sends text to the screen; input reads text from the keyboard. Basic I/O is essential for interactive programs.

## Explainer

Up to this point, your programs have worked with variables in silence — assigning values, performing calculations, but never telling anyone the result. **Console output** is how a program speaks: it takes a value from inside the program and displays it as text on the screen. In Python, `print(total)` sends the current value of `total` to the console. In most languages, the output function converts the value to a readable string automatically, so `print(42)` displays the text "42" even though the variable holds a number.

**Console input** works in the opposite direction. When a program calls an input function — like `input("Enter your name: ")` in Python — execution pauses, a prompt appears, and the program waits for the user to type something and press Enter. The typed text is then stored in a variable, just like any other assignment you have already practiced. The critical detail is that input almost always arrives as a string, even if the user types a number. If a user enters "25", the program receives the text "25", not the integer 25. This is why type conversion becomes important once you start building programs that do arithmetic on user-provided values.

The console is a **text stream** — output appears line by line, and input is read line by line. Think of it as a simple conversation: the program prints a question, the user types an answer, the program processes it and prints a response. This back-and-forth pattern is the foundation of every interactive command-line program. Even sophisticated applications with graphical interfaces ultimately rely on the same principle: data flows out to the user and back in from the user, just through different channels.

One practical habit to develop early is using output for **debugging**. When your program produces an unexpected result, inserting print statements to display intermediate variable values lets you trace exactly where the logic diverges from your expectation. This technique — printing a variable's value at key points in your code — remains one of the most effective debugging strategies at every skill level, from first programs to production systems.
