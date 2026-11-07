---
id: relational-calculus
title: Relational Calculus (Tuple and Domain)
domain: computer-science
course: databases
prerequisites:
- id: relational-algebra
  type: hard
- id: relational-data-model
  type: hard
- id: predicates-quantifiers-discrete
  type: hard
builds-toward: []
tags:
- relational-calculus
- tuple-relational-calculus
- domain-relational-calculus
- query-languages
- declarative
- codd
stage: formal-systems
status: validated
---
# Relational Calculus (Tuple and Domain)

## Core Idea
Relational calculus is a formal query language that describes the result a query should return, using logic, without saying how to compute it. In the tuple relational calculus, a query has the form {t | P(t)}: the set of all tuples t for which the formula P is true. The domain relational calculus uses variables that range over attribute values instead of whole tuples. E. F. Codd showed that relational algebra and the safe relational calculus can express exactly the same queries, which gives a precise meaning to calling a query language relationally complete.

## How It's Best Learned
Translate a handful of English queries over one small schema three ways: into relational algebra, into tuple relational calculus, and into SQL, and compare the shapes. Use "find instructors who teach in every department building" style queries to show where the universal quantifier is natural. Show an unsafe expression such as {t | not (t in instructor)} and ask what its result would be, which motivates the safety restriction.

## Common Misconceptions
- Relational calculus is a procedure the database executes step by step. (It is declarative: it states the condition the result tuples must satisfy, and an implementation is free to choose any evaluation order.)
- Relational calculus can express more queries than relational algebra. (Codd's theorem shows the safe calculus and the algebra have the same expressive power.)
- Any well-formed formula is an acceptable query. (Formulas such as {t | not (t in r)} describe infinite sets; only safe expressions, whose results come from values in the database or the query, are allowed.)

## Questions

```yaml
- question: "Given the relation instructor(ID, name, dept_name, salary), which tuple relational calculus expression returns the IDs of instructors whose salary is greater than 80000?"
  type: multiple-choice
  options:
    - "{t | t in instructor and t[salary] > 80000}"
    - "{t | exists s in instructor (t[ID] = s[ID] and s[salary] > 80000)}"
    - "{t | for all s in instructor (s[salary] > 80000)}"
    - "{t | not (t in instructor) and t[salary] > 80000}"
  answer: 1
  explanation: "Option B builds result tuples t that have only an ID attribute, copied from some instructor tuple s with salary over 80000. Option A returns whole instructor tuples, not just IDs. Option C requires every instructor to qualify. Option D is unsafe and not what is asked."

- question: "What does Codd's theorem state about relational algebra and relational calculus?"
  type: multiple-choice
  options:
    - "Relational algebra can express strictly more queries than relational calculus"
    - "Relational calculus can express strictly more queries than relational algebra"
    - "Relational algebra and safe relational calculus have the same expressive power"
    - "Neither language can express joins"
  answer: 2
  explanation: "Codd showed that every relational algebra expression has an equivalent safe calculus expression and the reverse. A query language that can express all of these queries is called relationally complete."

- question: "The tuple relational calculus expression {t | not (t in instructor)} is a safe query."
  type: true-false
  answer: false
  explanation: "It asks for every possible tuple that is not in instructor, which is an infinite set built from values that need not appear anywhere in the database. Safe expressions restrict results to values drawn from the database and the query itself, so they always produce finite answers."

- question: "Explain in one or two sentences how the tuple relational calculus and the domain relational calculus differ."
  type: short-answer
  answer: "In the tuple relational calculus, variables range over whole tuples, as in {t | t in instructor and t[salary] > 80000}. In the domain relational calculus, variables range over individual attribute values, as in {<i, n, d, s> | <i, n, d, s> in instructor and s > 80000}."
  explanation: "Both are first-order logic over relations and have the same expressive power when restricted to safe expressions. Query-by-Example (QBE) was based on the domain calculus, while SQL draws on ideas from the tuple calculus."
```

## Explainer

Relational algebra describes a query as a sequence of operations: select these rows, project these columns, join with that table. That is a procedure. Relational calculus takes the other approach. It describes the answer by a logical property, and leaves the procedure to the system. If you know predicates and quantifiers from logic, you already have most of the tools.

In the **tuple relational calculus** (TRC), a query looks like {t | P(t)}, read "the set of all tuples t such that P(t) is true." Using the schema instructor(ID, name, dept_name, salary), the instructors earning more than 80000 are:

{t | t ∈ instructor ∧ t[salary] > 80000}

Here t ranges over tuples, and t[salary] picks out one attribute. To return only IDs, introduce a second variable with the existential quantifier:

{t | ∃ s ∈ instructor (t[ID] = s[ID] ∧ s[salary] > 80000)}

This says that t is a one-attribute tuple whose ID matches some well-paid instructor. Joins appear the same way, as several quantified variables tied together by equalities. The universal quantifier ∀ expresses "for every" conditions directly, such as students who have taken every course offered by a department. In relational algebra those queries need the more awkward division operator or a double set difference.

The **domain relational calculus** (DRC) uses variables for individual attribute values instead of whole tuples:

{<i, n, d, s> | <i, n, d, s> ∈ instructor ∧ s > 80000}

The visual language Query-by-Example (QBE), developed at IBM in the 1970s, was based on this form.

Logic is more permissive than databases can tolerate. The expression {t | ¬(t ∈ instructor)} is a legal formula, but it describes every possible tuple not in the table, an infinite set. Such queries are called **unsafe**. A **safe** expression guarantees that every value in the result comes from the database or from constants in the query, so the answer is finite and computable.

E. F. Codd, who proposed the relational model, also proved the central result about these languages. Relational algebra and the safe relational calculus can express exactly the same set of queries. This is known as **Codd's theorem**. It gave the field a yardstick: a query language is **relationally complete** if it can express every query of relational algebra. SQL meets that standard and goes beyond it with aggregation and other features. Its declarative style, stating what is wanted rather than how to get it, comes from the calculus.
