---
id: first-order-logic-ai
title: First-Order Logic for AI
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: soft
builds-toward:
- logic-programming-basics
- knowledge-graphs
- semantic-networks
tags:
- logic
- knowledge-representation
- reasoning
- formal-systems
stage: advanced
status: draft
---

# First-Order Logic for AI

## Core Idea
First-order logic (FOL) extends propositional logic with predicates, quantifiers, and variables to represent complex domains formally and expressively. FOL serves as a foundation for logical inference, planning, and knowledge representation; however, automated reasoning in FOL is computationally expensive (semi-decidable) and even for restricted fragments can be intractable.

## How It's Best Learned
Practice translating English statements into FOL formulas, then use a theorem prover (e.g., Prolog or DPLL-based solvers) to prove simple theorems.

## Explainer

If you have worked with propositional logic (Boolean variables, AND, OR, NOT, implications), you know its power and its limitation. You can express statements like "if it rains, the ground is wet" as R → W, and chain such rules together for inference. But propositional logic cannot express "every student who studies passes the exam" because it has no way to talk about objects, their properties, or quantification over collections. **First-order logic** (FOL) extends propositional logic with exactly these capabilities.

FOL introduces three key elements. **Predicates** are functions that return true or false for specific objects: Student(alice), Passes(bob, math). **Variables** stand in for unspecified objects: Student(x). **Quantifiers** bind variables to make general claims: ∀x (Student(x) ∧ Studies(x) → Passes(x)) says "for all x, if x is a student and x studies, then x passes." The existential quantifier ∃x says "there exists at least one x such that..." — for example, ∃x (Student(x) ∧ Passes(x, philosophy)) means "some student passes philosophy." With predicates, variables, quantifiers, and the logical connectives you already know (∧, ∨, ¬, →), FOL can represent a vast range of real-world knowledge in a form that supports automated reasoning.

In AI, FOL serves as the foundation for **knowledge representation and reasoning**. A knowledge base is a set of FOL sentences describing what is known about a domain. An inference engine applies rules of deduction — **modus ponens** (from P and P → Q, conclude Q), **universal instantiation** (from ∀x P(x), conclude P(alice) for any specific alice), and **resolution** (a general-purpose rule that combines clauses to derive new conclusions) — to answer queries. For example, given the knowledge base {∀x (Bird(x) ∧ ¬Penguin(x) → Flies(x)), Bird(tweety), ¬Penguin(tweety)}, the inference engine can derive Flies(tweety). This is the basis for logic programming languages like Prolog, expert systems, and semantic web technologies.

The computational cost of FOL reasoning is the central practical challenge. While propositional logic is decidable (you can always determine if a formula is satisfiable, though it may take exponential time), FOL is only **semi-decidable**: if a conclusion follows from the premises, an algorithm will eventually find the proof, but if it does not follow, the algorithm may run forever without halting. This is not a theoretical curiosity — it is a fundamental limit proved by Church and Turing. In practice, this means FOL theorem provers can handle moderately sized knowledge bases but struggle with the scale of real-world knowledge. Restricted fragments of FOL — such as **Horn clauses** (the basis of Prolog) or **description logics** (the basis of OWL and the semantic web) — trade expressiveness for decidability, giving guaranteed termination at the cost of being unable to represent certain kinds of knowledge.

Despite competition from statistical and neural approaches, FOL remains essential in AI for domains requiring provably correct reasoning: formal verification of software, planning systems that must guarantee safety properties, legal and regulatory reasoning, and knowledge graph construction. Its value lies not in processing noisy, uncertain data (where machine learning excels) but in maintaining logical consistency and supporting explanations — if the system concludes something, it can show you the chain of deductive steps that led there.
