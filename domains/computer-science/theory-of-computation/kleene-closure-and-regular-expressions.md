---
id: kleene-closure-and-regular-expressions
title: Kleene Closure, Kleene Star, and Regular Language Operations
domain: computer-science
course: theory-of-computation
prerequisites:
- id: regular-expressions-to-automata
  type: hard
builds-toward:
- regular-languages-fundamentals
- closure-properties-regular-languages
tags:
- regular-languages
- operations
- closure
stage: advanced
status: draft
---

# Kleene Closure, Kleene Star, and Regular Language Operations

## Core Idea
The Kleene star L* of a language L denotes zero or more repetitions of strings from L. Regular languages are closed under union, concatenation, and Kleene star; these operations preserve recognizability by finite automata. Kleene's theorem states that a language is regular if and only if it can be expressed using these operations starting from singleton languages.

## Questions

```yaml
- question: "If L = {ab, c}, which of the following strings is in L*?"
  type: multiple-choice
  options:
    - "ba — because L* allows rearranging characters from strings in L"
    - "abc — because L* includes all strings containing letters from L"
    - "ε — because L* always includes zero repetitions of strings from L"
    - "a — because 'a' is a prefix of a string in L"
  answer: 2
  explanation: "L* includes all strings formed by concatenating zero or more strings chosen from L (with repetition allowed). Zero repetitions gives the empty string ε — so ε ∈ L* regardless of what L contains. One repetition gives 'ab' or 'c'. Two repetitions give 'abab', 'abc', 'cab', 'cc'. And so on. 'ba' is not in L* because L* doesn't allow reordering characters — it concatenates whole strings from L. 'a' is not in L* because 'a' alone is not a string in L and cannot be produced by concatenating strings from L."

- question: "A classmate argues: 'I can construct a finite automaton that recognizes a language no regular expression can describe.' What does Kleene's theorem tell you about this claim?"
  type: multiple-choice
  options:
    - "The claim is plausible for non-deterministic automata, since NFAs are more powerful than DFAs"
    - "The claim is impossible: every language recognized by a finite automaton can be expressed by a regular expression, and vice versa"
    - "The claim is possible for automata with ε-transitions, which are strictly more powerful than regular expressions"
    - "The claim depends on the alphabet size — for large alphabets, automata may exceed regular expression power"
  answer: 1
  explanation: "Kleene's theorem is a biconditional: a language is regular if and only if it can be built from finite character sets using union, concatenation, and Kleene star (i.e., expressed as a regular expression). The 'only if' direction proves that every language a finite automaton recognizes can be expressed as a regular expression. So no finite automaton — DFA, NFA, or NFA with ε-transitions — can recognize a language that exceeds the expressive power of regular expressions. All three models define exactly the same class of languages."

- question: "The Kleene star L* of any non-empty language L always contains the empty string ε, even if every string in L has length greater than zero."
  type: true-false
  answer: true
  explanation: "L* is defined as the union over all n ≥ 0 of Lⁿ, where L⁰ = {ε} by definition (zero concatenations of strings from L). So ε ∈ L* regardless of what strings L contains. This is an important edge case: even if L = {ab, xyz} contains only strings of length 2 and 3, L* still includes ε because 'zero repetitions' is always a valid choice."

- question: "Because regular languages are closed under Kleene star, applying L* to a regular language may sometimes produce a non-regular language."
  type: true-false
  answer: false
  explanation: "Closure under Kleene star means the *opposite*: applying Kleene star to any regular language always produces another regular language — never a non-regular one. The proof is constructive: given an NFA for L, you can build an NFA for L* by adding a new start/accept state with ε-transitions. The result is always a valid NFA, which always recognizes a regular language. Closure properties are exactly what guarantee you cannot escape the class of regular languages by applying these operations."

- question: "State Kleene's theorem and explain what the 'if and only if' means about the relationship between regular expressions and finite automata."
  type: short-answer
  answer: "Kleene's theorem states: a language is regular if and only if it can be expressed using union, concatenation, and Kleene star applied to finite sets of characters. The biconditional means two things: (1) every language expressible by a regular expression is recognizable by a finite automaton, and (2) every language recognizable by a finite automaton is expressible by a regular expression. Together, these establish that regular expressions and finite automata have exactly identical expressive power — they define the same class of languages, approached from two completely different formalisms."
  explanation: "The significance of the biconditional is that neither formalism is more powerful than the other. You might expect that automata — which are computational machines — could recognize languages that no algebraic pattern can describe, or vice versa. Kleene's theorem says no: the two formalisms are perfectly matched. This equivalence is foundational to the theory of computation because it means results proven about regular expressions automatically transfer to automata, and vice versa, giving theorists two different tools to prove the same theorems."
```

## Explainer

From your work on converting regular expressions to automata, you understand that a regular expression is a pattern that describes a set of strings, and that every regular expression can be turned into a finite automaton that recognizes exactly those strings. This topic steps back to examine the three fundamental operations that regular expressions are built from, and why they are exactly the right operations for characterizing regular languages.

The three operations are **union**, **concatenation**, and **Kleene star**. Union (written L₁ ∪ L₂ or `L₁ | L₂` in regex notation) collects all strings that belong to either language. Concatenation (L₁L₂) forms all strings made by gluing a string from L₁ to a string from L₂. Kleene star (L*) is the most powerful of the three: it takes all possible concatenations of zero or more strings from L. If L = {ab, c}, then L* includes ε (zero repetitions), ab, c, abab, abc, cab, cc, ababc, and so on — every possible sequence of pieces drawn from L. The "zero repetitions" part is important: L* always includes the empty string ε, regardless of what L contains.

Closure under these operations means that if you start with regular languages and apply union, concatenation, or Kleene star, the result is always another regular language. The proof is constructive: given NFAs for L₁ and L₂, you can build an NFA for their union (add a new start state with ε-transitions to both), their concatenation (link the accept states of the first to the start state of the second via ε-transitions), or the Kleene star (add a new start/accept state with ε-transitions to the old start, and from old accept states back to the old start). Each construction is simple and mechanical, producing a valid NFA every time. This is why NFAs with ε-transitions are the natural "backend" for regular expressions — the regex-to-NFA conversion mirrors these three constructions exactly.

**Kleene's theorem** ties everything together with a biconditional: a language is regular if and only if it can be built from individual characters using union, concatenation, and Kleene star. The "if" direction says that these three operations, applied to the simplest possible languages (single characters and ε), generate all regular languages — you don't need any other operation. The "only if" direction says that every language recognized by a finite automaton can be expressed this way. The proof of the "only if" direction is more involved, typically using state elimination on a DFA to extract a regular expression. Together, the two directions establish that regular expressions and finite automata define exactly the same class of languages — two very different formalisms with identical expressive power.
