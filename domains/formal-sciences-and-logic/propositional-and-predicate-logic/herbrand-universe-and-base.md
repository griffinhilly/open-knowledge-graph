---
id: herbrand-universe-and-base
title: Herbrand Universe and Herbrand Base
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: domain-and-structure-fol
  type: hard
- id: skolemization-and-witnesses
  type: hard
tags:
- first-order-logic
- herbrand
- model-theory
stage: formal-systems
status: draft
---

# Herbrand Universe and Herbrand Base

## Core Idea
Given a first-order language, the Herbrand universe consists of all ground terms (terms with no variables) built from the language's constants and function symbols. The Herbrand base consists of all ground atoms (atomic formulas with no variables). Herbrand models provide a canonical way to interpret formulas in terms of the syntax itself, enabling automated reasoning techniques.

## Explainer

When you studied **domains and structures** in first-order logic, you learned that a model consists of a domain — an arbitrary set — plus interpretations for all the symbols. This is powerful but inconvenient for automated reasoning: the domain could be anything, and you would need to check infinitely many possible domains to determine satisfiability. The **Herbrand construction** solves this by building a canonical domain directly from the syntax of the language itself.

The **Herbrand universe** H is the set of all **ground terms** — terms built from constants and function symbols with no variables. If your language has a constant `a` and a unary function symbol `f`, the Herbrand universe is {a, f(a), f(f(a)), f(f(f(a))), ...} — just the syntactic expressions you can construct. There are no "hidden" elements; the domain is exactly the terms you can write down. If there are no function symbols, H is just the set of constants (or {a} if there are none at all, to ensure the universe is non-empty).

The **Herbrand base** B is the set of all **ground atoms** — atomic formulas formed by applying predicate symbols to elements of the Herbrand universe. A **Herbrand interpretation** assigns a truth value to each element of the Herbrand base; it is equivalent to specifying which ground atoms are true. A **Herbrand model** is a Herbrand interpretation that satisfies the formula. The critical theorem — Herbrand's theorem — states that a set of clauses (universal sentences in CNF) is satisfiable if and only if it has a Herbrand model. This reduces satisfiability over arbitrary domains to satisfiability over the canonical syntactic domain.

Why does this matter? Because it transforms logical satisfiability into a combinatorial problem over syntax. Instead of quantifying over abstract domains, you can substitute all possible ground terms for variables and check whether any finite set of ground instances leads to a contradiction. This is the theoretical foundation of **resolution theorem proving** and logic programming (Prolog). When a Prolog interpreter evaluates a query, it is effectively searching for a satisfying Herbrand model. The Herbrand universe is the set of all possible terms the interpreter might unify; the base is all the facts it might prove. Herbrand's insight that syntax suffices to witness satisfiability is what makes automated first-order reasoning tractable.
