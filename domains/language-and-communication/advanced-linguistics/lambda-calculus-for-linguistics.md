---
id: lambda-calculus-for-linguistics
title: Lambda Calculus for Linguistic Semantics
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: lambda-calculus
  type: hard
- id: compositional-semantics
  type: hard
builds-toward:
- montague-semantics
tags:
- semantics
- formal
- logic
stage: advanced
status: draft
---

# Lambda Calculus for Linguistic Semantics

## Core Idea
Lambda calculus provides a formal system for representing meanings and their composition. Lambda abstraction represents predicates as functions (the verb 'sleep' as λx.sleep(x)), and function application models how arguments combine with predicates. This framework enables precise modeling of quantifiers, modification, and binding, eliminating ambiguity inherent in informal semantic representations.

## Explainer

From your study of compositional semantics, you know the core principle: the meaning of a sentence is built systematically from the meanings of its parts, following syntactic structure. From your study of lambda calculus, you have the formal tools: functions, abstraction, and reduction. The application of lambda calculus to linguistics is what makes compositional semantics *computable* — it gives you a precise notation for representing meanings as functions and combining them step by step.

Start with a simple verb. The verb *sleep* means something like "x sleeps" — it expresses a property that can be true or false of any individual. In lambda notation, this is **λx.sleep(x)**: a function that takes an individual *x* and returns the proposition "x sleeps." When we apply this to an argument — say, the name "Maria," which denotes an individual *m* — we get **(λx.sleep(x))(m)**, which **beta-reduces** to *sleep(m)*: the proposition that Maria sleeps. Beta reduction is just substitution: replace the bound variable *x* with the argument *m* everywhere it appears in the function body. This mirrors the syntactic operation of predication — a verb phrase combining with its subject.

Transitive verbs require two steps of function application. *Loves* has type **λy.λx.love(x,y)**: a function that takes an object *y* and returns a function waiting for a subject *x*. Applying it first to "Maria" yields **λx.love(x,m)** ("x loves Maria"); applying *that* to "John" yields **love(j,m)** ("John loves Maria"). Notice the order: the lambda expression is built so that object applies first, then subject — this corresponds to the syntactic structure where the verb combines with its object before the VP combines with the subject. **Type theory** keeps track of what can combine with what: an expression of type *e* (entity) can combine with an expression of type *(e→t)* (a function from entity to truth value) to produce type *t* (a truth value).

The real power emerges with **quantifiers**. "Every student slept" can't be handled by simply plugging a name into λx.sleep(x), because "every student" doesn't denote an individual. Instead, it denotes a **generalized quantifier**: a function over properties. **∀-every-student** is represented as **(λP.∀x[student(x) → P(x)])** — a function that takes a property P and says "for every x who is a student, x has P." Applying this to the VP *λx.sleep(x)* yields: **∀x[student(x) → sleep(x)]** — "for every x, if x is a student, then x sleeps." This treatment of quantifiers as higher-order functions (functions that take functions as arguments) is what allows compositional semantics to handle the full range of natural language quantification — *some*, *most*, *no*, *exactly three* — within a uniform formal framework, eliminating the ambiguities that plague informal paraphrase.
