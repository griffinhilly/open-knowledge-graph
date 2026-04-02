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
status: validated
---

# Logic Programming Basics (Prolog)

## Core Idea
Logic programming (Prolog) uses first-order logic clauses and backward chaining to solve problems through unification and goal reduction. Prolog naturally expresses relational and constraint problems, though performance requires careful formulation to avoid inefficient search and the lack of type checking can lead to subtle errors.

## How It's Best Learned
Write Prolog programs for relational problems (family relations, graph traversal) and understand how backtracking explores the proof space.

## Questions

```yaml
- question: "A Prolog programmer writes the rule: ancestor(X, Z) :- ancestor(X, Y), parent(Y, Z). When queried, the program immediately enters an infinite loop. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The rule is logically incorrect — ancestor cannot be defined in terms of itself"
    - "Prolog searches depth-first and always tries to resolve the recursive subgoal first, looping before reaching base cases"
    - "Unification fails because X and Z are the same variable"
    - "Prolog requires all facts to be listed before rules, and the parent facts must be missing"
  answer: 1
  explanation: "This is the classic Prolog infinite loop from left recursion. When Prolog tries to prove ancestor(X, Z), it first tries the only rule, generating subgoal ancestor(X, Y) — which immediately recurses again before any base-case fact is ever checked. Prolog's depth-first search dives into recursive calls without limit. The fix is to reorder the rule: ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z). — by placing the base-case fact (parent) first, Prolog grounds variables before recursing. This demonstrates why clause ordering is not semantically neutral in Prolog."

- question: "What happens in Prolog when you query a predicate that has been misspelled (e.g., grandparent vs grandparnet)?"
  type: multiple-choice
  options:
    - "A compile-time error is raised identifying the unknown predicate"
    - "A runtime type error is thrown when the predicate is first evaluated"
    - "The query silently fails — Prolog returns 'false' with no error message"
    - "Prolog prompts the user to define the missing predicate interactively"
  answer: 2
  explanation: "Prolog has no type system and no compile-time predicate checking. A misspelled predicate name simply has no matching clauses in the database, so unification fails and the query returns false (or 'no'). There is no error message unless you have explicitly enabled the 'unknown' flag. This silent failure is a notorious source of debugging difficulty in Prolog: a typo masquerades as a genuine negative answer. This is one of the practical limitations that makes Prolog error-prone for large programs."

- question: "In Prolog, when a sub-goal fails during query resolution, the interpreter backtracks by undoing the most recent variable binding and attempting alternative clause matches."
  type: true-false
  answer: true
  explanation: "Backtracking is the core control mechanism in Prolog. When a sub-goal cannot be proved with the current variable bindings, Prolog backtracks to the most recent choice point — the last point where multiple clause matches were possible — undoes all bindings made since then, and tries the next alternative. This systematic search through the proof space is what allows Prolog to find all solutions to a query, not just the first one, and is fundamental to understanding Prolog's execution model."

- question: "The order in which clauses appear in a Prolog program does not affect whether a query will succeed or fail — mainly the logical content of the clauses matters."
  type: true-false
  answer: false
  explanation: "Clause order is semantically significant in Prolog because the search is depth-first and ordered. Prolog tries clauses in the order they are written. A logically correct but poorly ordered program can loop infinitely (as in left-recursive rules) or return results in a different order. Unlike pure logic, where any order of rules leads to the same conclusions, Prolog's procedural search means the programmer must reason about both the logical content and the execution order of clauses."

- question: "Explain the difference between how an imperative program and a Prolog program approach computing the grandparent relationship, and what this reveals about the logic programming paradigm."
  type: short-answer
  answer: "An imperative program specifies the procedure: iterate over known parents, find each person's parent, check if they match the query. Prolog instead declares what is true: grandparent(X,Z) :- parent(X,Y), parent(Y,Z). The interpreter handles the search automatically via backward chaining and unification. This reveals that logic programming separates the knowledge (what relationships exist) from the control (how to search for them) — the programmer states facts and rules, not algorithms."
  explanation: "This distinction — declarative vs procedural — is the fundamental insight of logic programming. In Prolog, you are writing a knowledge base, not a procedure. The interpreter's resolution strategy (backward chaining, depth-first search, backtracking) is the generic 'how'; your clauses supply the domain-specific 'what.' The power is that the same set of facts and rules can answer many different queries without modification. The limitation is that you cannot fully control execution order, which is why performance and termination require understanding the interpreter's search strategy."
```

## Explainer

Logic programming flips the way you think about writing programs. In conventional programming, you write step-by-step instructions telling the computer *how* to compute something. In logic programming, you declare *what* is true — facts and rules expressed in first-order logic — and let the system figure out how to derive answers. You already know how first-order logic represents knowledge with predicates, quantifiers, and logical connectives. Prolog takes that formalism and turns it into a programming language: you state logical clauses, and the interpreter uses them as a program.

A Prolog program consists of **facts** and **rules**. A fact like `parent(alice, bob).` asserts that Alice is a parent of Bob. A rule like `grandparent(X, Z) :- parent(X, Y), parent(Y, Z).` says X is a grandparent of Z if there exists some Y where X is a parent of Y and Y is a parent of Z. When you pose a query — `?- grandparent(alice, W).` — Prolog tries to prove it by searching through the facts and rules using **backward chaining**: it starts from the goal and works backward, trying to find facts that satisfy each sub-goal. This is where your understanding of recursion becomes essential, because rules can refer to themselves, and Prolog naturally handles recursive definitions by repeatedly applying rules until it reaches base-case facts.

The engine that makes this work is **unification**. When Prolog tries to match a goal against a rule head, it finds a substitution of variables that makes them identical. For `grandparent(alice, W)`, it unifies with the rule head `grandparent(X, Z)` by binding X to alice and Z to W, then attempts to prove `parent(alice, Y)` and `parent(Y, W)`. If the first sub-goal succeeds with Y = bob, it then tries `parent(bob, W)`. If that succeeds with W = charlie, the query returns `W = charlie`. If at any point a sub-goal fails, Prolog **backtracks** — it undoes the most recent variable binding and tries alternative matches. This systematic exploration of the proof space is what gives Prolog its power for search and constraint problems.

The elegance of logic programming comes with practical tradeoffs. Because Prolog searches depth-first by default, the order of clauses matters: a poorly ordered recursive rule can send the interpreter into an infinite loop. There is no type system catching errors at compile time, so a misspelled predicate name simply fails silently rather than raising an error. And while Prolog excels at relational reasoning, graph traversal, and symbolic AI tasks like natural language parsing, it struggles with numerical computation and problems that require fine-grained control over execution order. Understanding these strengths and limitations helps you recognize when logic programming is the right tool — typically when your problem is naturally expressed as relationships and constraints rather than sequential transformations.
