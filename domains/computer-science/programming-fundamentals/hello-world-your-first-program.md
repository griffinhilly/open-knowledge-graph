---
id: hello-world-your-first-program
title: 'Hello World: Your First Program'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: algorithm-design-basics
  type: soft
builds-toward:
- program-structure-and-anatomy
- code-comments-and-style
tags:
- introduction
- getting-started
- basic
stage: formal-systems
status: draft
---
# Hello World: Your First Program

## Core Idea
A 'Hello World' program is the simplest complete program—it demonstrates the basic syntax needed to execute code and produce output. Writing and running your first program teaches you how to write, save, and execute code in your chosen language.

## How It's Best Learned
Type it yourself rather than copying; make small changes (different text, different output) to see immediate results.

## Common Misconceptions
That the program must do something complex or useful; actually, simplicity is the point—to see the minimal structure required.

## Explainer

Every programming journey starts the same way: you write a program that prints "Hello, World!" to the screen and run it. This tradition dates back to the 1970s, when Brian Kernighan used it in a tutorial for the C programming language, and it has been the standard first program in virtually every language since. The reason is not sentimentality — it is practicality. Before you can learn anything else, you need to verify that your entire toolchain works: your text editor, your language installation, your ability to save a file, and your ability to execute it. Hello World tests all of this with the smallest possible program.

In Python, the entire program is one line: `print("Hello, World!")`. In Java, it requires a class definition, a main method, and a System.out.println call — roughly eight lines of boilerplate to produce the same output. In C, you need a #include directive, a main function, and a printf call. These differences are not arbitrary; they reveal each language's philosophy. Python prioritizes simplicity and readability. Java enforces object-oriented structure from the start. C gives you direct control but requires you to specify more. Noticing these differences in your first program gives you a preview of how the language will feel as you learn more.

The act of typing the program yourself — rather than copying and pasting — matters more than it seems. Your fingers need to learn where the parentheses, quotes, and semicolons go. You will likely make a mistake: a missing quotation mark, a misspelled function name, a wrong kind of bracket. The error message you get is itself a lesson. Learning to read error messages — to see that "SyntaxError: EOL while scanning string literal" means you forgot a closing quote — is a skill you will use every day as a programmer. Your first bug is as educational as your first successful run.

Once Hello World runs, experiment with it. Change the text inside the quotes. Add a second print statement. Try removing the parentheses and see what happens. This exploratory instinct — changing one thing, running the program, observing the result — is the fundamental loop of learning to program. You are not just memorizing syntax; you are building a mental model of how the computer interprets your instructions. Every modification tests a small hypothesis about how the language works, and the immediate feedback from running the program confirms or corrects your understanding.
