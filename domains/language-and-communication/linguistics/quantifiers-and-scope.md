---
id: quantifiers-and-scope
title: Quantifiers and Scope
domain: language-and-communication
course: linguistics
prerequisites:
- id: compositional-semantics
  type: hard
tags:
- quantifiers
- scope ambiguity
- universal quantifier
- existential quantifier
- binding
- logical form
stage: formal-systems
status: draft
---

# Quantifiers and Scope

## Core Idea
Quantifiers are expressions like "every," "some," "no," "most," and "few" that specify how many individuals in a domain satisfy a predicate. Natural language quantifiers interact with each other and with other operators (negation, modals) to produce scope ambiguities: "Every student read a book" can mean every student read the same book (a > every) or each read a different one (every > a), depending on which quantifier takes wide scope. Formal semantic analysis represents these readings using logical forms where quantifier order determines interpretation. Binding theory governs when a quantifier can bind a pronoun — "Every student thinks she will pass" allows a bound-variable reading (each student thinks of herself) alongside a referential reading (each thinks some specific person will pass).

## How It's Best Learned
Practice generating both scope readings for ambiguous sentences and drawing the logical forms that distinguish them. Translate English quantified sentences into predicate logic notation to make the scope relations explicit. Test your intuitions by constructing contexts that force one reading over the other — "Every student submitted a paper" is ambiguous in isolation but disambiguated in context.

## Common Misconceptions
- Scope ambiguity is not vagueness — an ambiguous sentence has two (or more) distinct, precise interpretations, while a vague sentence has one underspecified meaning.
- "Some" in logic (existential quantifier) means "at least one," which conflicts with the conversational implicature that "some" means "not all" — this is a pragmatic enrichment, not part of the semantic meaning.
- Not all surface word orders correspond to scope order; quantifier raising and other covert movement operations can produce scope readings that do not match linear position.

## Explainer

From your work in compositional semantics, you know that the meaning of a sentence is built from the meanings of its parts according to syntactic structure. Quantifiers are the elements that make compositional semantics genuinely interesting — and genuinely difficult — because they don't just contribute a fixed meaning to a slot in the structure; they operate on entire **predicates**, binding variables that can appear elsewhere in the sentence.

Start with the basics. An **existential quantifier** (some, a, there exists...) says that at least one thing in some domain satisfies a predicate. "A student left early" = there exists at least one student x such that x left early. A **universal quantifier** (every, all, each) says that everything in a domain satisfies the predicate. "Every student left early" = for every student x, x left early. These are precise logical claims with distinct truth conditions. The semantic analysis represents them using formulas from predicate logic, where the quantifier's **scope** — the stretch of formula it governs — determines what it ranges over.

Scope becomes interesting when a sentence contains more than one quantifier. "Every student read a book" has two quantifiers: *every student* and *a book*. Which one takes **wide scope** — governs the other? If *every* takes wide scope, the meaning is: for every student, there exists some book (possibly a different one) that the student read. If *a* takes wide scope, the meaning is: there exists one specific book such that every student read it. These are genuinely different truth conditions. The first is satisfied by a classroom where each student read a different book; the second requires a single shared text. Natural languages are systematically **ambiguous** in cases like this — the same surface string admits both logical forms — and the job of a semantic analysis is to generate both readings and identify the conditions that favor one over the other.

**Binding theory** extends scope into the domain of pronouns. In "Every student thinks she will pass," the pronoun *she* can either refer to a specific individual in context (referential reading) or be bound by *every student* as a variable (bound-variable reading, meaning: each student thinks that she herself will pass). When *every student* binds *she*, the quantifier's scope extends over the embedded clause, creating a bound-variable interpretation. The rule governing this is that a quantifier can bind a pronoun only if the quantifier takes scope over the position of the pronoun. Sentences like "She thinks every student will pass" cannot have a bound reading where *every student* binds *she*, because the quantifier occurs after and inside the matrix clause — it cannot take scope over the subject position of the main clause. Constructing sentences that force or block bound readings is one of the most effective exercises for making scope relations concrete and testable.
