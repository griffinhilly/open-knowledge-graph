---
id: predicate-logic-introduction
title: Introduction to Predicate Logic (First-Order Logic)
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-logic-introduction
  type: hard
- id: set-fundamentals
  type: hard
- id: functions-and-function-properties
  type: hard
- id: domain-and-range
  type: soft
builds-toward:
- predicates-and-relations-fol
- quantifier-notation-and-basics
- first-order-logic-syntax
tags:
- foundations
- first-order-logic
- introduction
stage: formal-systems
status: draft
---

# Introduction to Predicate Logic (First-Order Logic)

## Core Idea
Predicate logic extends propositional logic by introducing predicates (properties and relations), variables, and quantifiers. Instead of treating 'Socrates is mortal' as atomic, predicate logic breaks it into a predicate applied to an individual. This enables formal reasoning about all objects with a property or about objects' existence.

## How It's Best Learned
Compare propositional and predicate formulations of the same statements. Practice translating English sentences with 'all' and 'some' into formal notation. Examine why propositional logic cannot express 'All humans are mortal; Socrates is human; therefore, Socrates is mortal.'

## Common Misconceptions
Thinking predicate logic is just different notation. Confusing when to use universal vs. existential quantifiers. Assuming quantifiers don't change fundamental decidability properties.

## Questions

```yaml
- question: "In propositional logic, you represent 'Socrates is mortal' as atom P and 'Plato is mortal' as atom Q. Why can you NOT use propositional logic to prove 'Socrates is mortal' from 'All humans are mortal' and 'Socrates is human'?"
  type: multiple-choice
  options:
    - "You can — just define P = 'Socrates is mortal' and derive it from other atoms using modus ponens"
    - "Propositional logic can't represent the universal claim 'All humans are mortal' — it would need a separate atom for every individual human, with no formal connection between them"
    - "Propositional logic is too slow to evaluate syllogisms with more than two premises"
    - "The argument is invalid, so neither logic system can prove it"
  answer: 1
  explanation: "This is the core limitation predicate logic was designed to fix. In propositional logic, 'All humans are mortal' would require an infinite set of independent atoms (P₁ = 'Alice is mortal', P₂ = 'Bob is mortal', ...) with no formal link between them and 'x is human'. There is no way to express quantification over a domain. Predicate logic introduces ∀x Human(x) → Mortal(x), which formally connects the universal claim to any specific individual via instantiation."

- question: "A student argues: 'Predicate logic is just propositional logic with better notation — they're equally powerful, predicate logic is just more convenient.' What is the strongest objection to this claim?"
  type: multiple-choice
  options:
    - "Predicate logic uses more symbols, which makes it harder to read"
    - "Predicate logic is fundamentally more expressive: it can quantify over infinite domains and express relations, neither of which propositional logic can do"
    - "Predicate logic can only be used in mathematics, while propositional logic is general-purpose"
    - "Propositional logic handles temporal reasoning better than predicate logic does"
  answer: 1
  explanation: "The difference is not aesthetic — it's a difference in expressive power that has concrete computational consequences. Propositional logic is decidable (truth tables determine validity for any formula). Predicate logic is undecidable: Church and Turing proved in 1936 that no algorithm can determine whether an arbitrary first-order formula is valid. This is not a limitation of current technology; it's a fundamental theorem. The extra expressiveness (universal and existential quantification over infinite domains) comes with this unavoidable computational cost."

- question: "The statement ∀x Human(x) → Mortal(x) is a valid formula in predicate logic that could not be expressed as a single formula in propositional logic."
  type: true-false
  answer: true
  explanation: "This formula uses a universal quantifier ranging over a domain of objects — a feature predicate logic adds that propositional logic lacks entirely. In propositional logic, you can only have atomic propositions and truth-functional connectives. There is no mechanism to say 'for all objects x in the domain.' Predicate logic's ability to express universal and existential claims about entire domains is precisely what makes it strictly more expressive."

- question: "Because predicate logic is undecidable, it is impossible to prove any theorem in first-order logic — all proofs must be carried out informally."
  type: true-false
  answer: false
  explanation: "Undecidability means there is no algorithm that correctly decides validity for *all* first-order formulas. It does not mean proofs are impossible. For specific formulas, proofs can often be constructed (and verified mechanically). Proof assistants like Coq and Lean verify first-order proofs formally. Undecidability only means you can't write a program that halts on all inputs with a correct yes/no answer — you can still enumerate and check valid proofs, you just can't guarantee finding them for every formula."

- question: "What is the key structural difference between propositional and predicate logic, and why does that difference make predicate logic undecidable when propositional logic is decidable?"
  type: short-answer
  answer: "Propositional logic has finitely many atomic propositions, so a formula with n distinct atoms has exactly 2^n truth assignments to check — truth tables always terminate. Predicate logic introduces quantifiers over potentially infinite domains, meaning there is no finite procedure to check all possible interpretations. A formula like ∃x P(x) could be true in one domain and false in another, and verifying it requires reasoning about all possible domain structures."
  explanation: "The undecidability of predicate logic (the Entscheidungsproblem) is one of the foundational results in mathematical logic and theoretical computer science. Church proved it using lambda calculus; Turing proved it using Turing machines — and these proofs were among the first results that defined the limits of what algorithms can compute. Propositional logic avoids this because the domain of truth values is just {T, F} — finite and fixed."
```

## Explainer

Propositional logic treats statements like "Socrates is mortal" as indivisible atoms — the letter P either stands for the whole claim or it doesn't. This works for reasoning about fixed named facts, but breaks down the moment you want to say something about *all* members of a class or about the *existence* of something. "All humans are mortal" and "There exists a prime number greater than 1000" cannot be expressed in propositional logic, because they involve quantification over a domain of objects. **Predicate logic** — also called first-order logic — extends propositional logic by introducing exactly the machinery needed to express these patterns.

The core additions are three: **predicates**, **variables**, and **quantifiers**. A predicate like Human(x) expresses a *property* that an object x may or may not have. A function like mother(x) maps one object to another. Variables range over a **domain** — the set of objects you're talking about — and quantifiers bind those variables. You already know what a domain and range of a function are; the domain in predicate logic plays the same role: it is the universe of discourse over which variables take values. The universal quantifier ∀x Human(x) → Mortal(x) says: for every object x in the domain, if x is human, then x is mortal. No single atomic proposition in propositional logic can capture this.

The classical syllogism "All humans are mortal; Socrates is human; therefore, Socrates is mortal" exposes exactly why propositional logic is insufficient. In propositional logic you'd need three unrelated atoms P, Q, R and no formal connection between them. In predicate logic you have: (1) ∀x Human(x) → Mortal(x), (2) Human(socrates), and from these you derive (3) Mortal(socrates) by instantiating the universal with x = socrates. The proof is valid *because of the logical structure*, not by coincidence. The connection between your set-theory prerequisite and predicate logic is direct: ∀x P(x) is essentially a claim about every element of the domain set; ∃x P(x) is a claim that the extension of P (the subset of domain elements satisfying P) is nonempty.

A critical insight — noted in your common misconceptions — is that predicate logic is not merely different notation. It is fundamentally more expressive and fundamentally harder. Propositional logic is **decidable**: there is an algorithm (truth tables) that determines, for any formula, whether it is a tautology. Predicate logic is **undecidable**: no algorithm can determine for an arbitrary first-order formula whether it is valid. This is not a shortcoming of current technology — it is a theorem (the negative answer to Hilbert's Entscheidungsproblem, proved by Church and Turing independently in 1936). You can enumerate valid formulas, but you cannot systematically check all formulas for validity. This greater expressive power — the ability to talk about all objects in a domain, about relations between objects, and about existence — comes with this fundamental computational cost.

