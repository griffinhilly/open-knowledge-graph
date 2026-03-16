---
id: program-structure-and-flow
title: Program Structure and Control Flow
domain: computer-science
course: programming-fundamentals
prerequisites: []
builds-toward:
- conditional-statements
- loop-fundamentals
tags:
- fundamentals
- control-flow
- structure
stage: abstract-reasoning
status: draft
---

# Program Structure and Control Flow

## Core Idea
A computer program is a sequence of statements that execute in order, with control flow determining which statements run and when. Understanding sequence, branching, and repetition is fundamental to programming.

## How It's Best Learned
Trace through simple programs by hand, noting which statements execute and in what order. Use visualization tools to see control flow branches.

## Common Misconceptions
- Thinking all code executes simultaneously rather than sequentially.
- Confusing the order statements are written with the order they execute.

## Explainer

Every program you will ever write is built from just three kinds of control flow: **sequence**, **selection**, and **iteration**. Sequence is the default — the computer reads your instructions from top to bottom, executing each one before moving to the next, like following a recipe step by step. If you write three statements in a row, they run in exactly that order, one at a time. There is no parallelism, no skipping ahead. The computer is relentlessly literal: it does what you wrote, in the order you wrote it.

**Selection** (branching) is what lets a program make decisions. Instead of always running the same steps, the program can check a condition and choose one path or another. "If the user typed 'yes,' do this; otherwise, do that." This is where programs stop being simple scripts and start responding to the world. Without branching, every run of the program would produce identical output — useful for calculators, useless for almost everything else.

**Iteration** (looping) is what lets a program repeat work. Rather than writing the same instruction a thousand times, you write it once inside a loop and let the computer handle the repetition. A loop combines sequence (do these steps) with selection (should I keep going or stop?) into a single powerful structure. Together, these three constructs — do things in order, choose between alternatives, repeat until done — are sufficient to express any computation. Every complex program, from web browsers to video games, is ultimately a composition of sequences, branches, and loops.

One subtlety worth internalizing early: the order statements are *written* in your source file is not always the order they *execute*. A branch might skip an entire block. A loop might re-execute the same block dozens of times. When you are confused about what a program does, the single most effective debugging technique is to **trace** the execution by hand — point to each line as the computer would encounter it, track what values change, and follow the actual path through the code rather than reading it like prose.
