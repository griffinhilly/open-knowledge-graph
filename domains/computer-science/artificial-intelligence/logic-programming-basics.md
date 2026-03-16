---
id: logic-programming-basics
title: Logic Programming Basics (Prolog)
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: first-order-logic-ai
  type: hard
- id: recursion-basics
  type: hard
tags:
- logic-programming
- prolog
- backward-chaining
- unification
stage: advanced
status: draft
---

# Logic Programming Basics (Prolog)

## Core Idea
Logic programming (Prolog) uses first-order logic clauses and backward chaining to solve problems through unification and goal reduction. Prolog naturally expresses relational and constraint problems, though performance requires careful formulation to avoid inefficient search and the lack of type checking can lead to subtle errors.

## How It's Best Learned
Write Prolog programs for relational problems (family relations, graph traversal) and understand how backtracking explores the proof space.

## Explainer

Logic programming flips the way you think about writing programs. In conventional programming, you write step-by-step instructions telling the computer *how* to compute something. In logic programming, you declare *what* is true — facts and rules expressed in first-order logic — and let the system figure out how to derive answers. You already know how first-order logic represents knowledge with predicates, quantifiers, and logical connectives. Prolog takes that formalism and turns it into a programming language: you state logical clauses, and the interpreter uses them as a program.

A Prolog program consists of **facts** and **rules**. A fact like `parent(alice, bob).` asserts that Alice is a parent of Bob. A rule like `grandparent(X, Z) :- parent(X, Y), parent(Y, Z).` says X is a grandparent of Z if there exists some Y where X is a parent of Y and Y is a parent of Z. When you pose a query — `?- grandparent(alice, W).` — Prolog tries to prove it by searching through the facts and rules using **backward chaining**: it starts from the goal and works backward, trying to find facts that satisfy each sub-goal. This is where your understanding of recursion becomes essential, because rules can refer to themselves, and Prolog naturally handles recursive definitions by repeatedly applying rules until it reaches base-case facts.

The engine that makes this work is **unification**. When Prolog tries to match a goal against a rule head, it finds a substitution of variables that makes them identical. For `grandparent(alice, W)`, it unifies with the rule head `grandparent(X, Z)` by binding X to alice and Z to W, then attempts to prove `parent(alice, Y)` and `parent(Y, W)`. If the first sub-goal succeeds with Y = bob, it then tries `parent(bob, W)`. If that succeeds with W = charlie, the query returns `W = charlie`. If at any point a sub-goal fails, Prolog **backtracks** — it undoes the most recent variable binding and tries alternative matches. This systematic exploration of the proof space is what gives Prolog its power for search and constraint problems.

The elegance of logic programming comes with practical tradeoffs. Because Prolog searches depth-first by default, the order of clauses matters: a poorly ordered recursive rule can send the interpreter into an infinite loop. There is no type system catching errors at compile time, so a misspelled predicate name simply fails silently rather than raising an error. And while Prolog excels at relational reasoning, graph traversal, and symbolic AI tasks like natural language parsing, it struggles with numerical computation and problems that require fine-grained control over execution order. Understanding these strengths and limitations helps you recognize when logic programming is the right tool — typically when your problem is naturally expressed as relationships and constraints rather than sequential transformations.
