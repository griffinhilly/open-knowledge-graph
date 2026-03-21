---
id: proof-structure-terminology
title: Proof Structure and Mathematical Terminology
domain: mathematics
course: methods-of-proof
prerequisites:
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- direct-proof-methods
- proof-by-contrapositive
- proof-by-contradiction
tags:
- proof
- terminology
- structure
stage: formal-systems
status: draft
---

# Proof Structure and Mathematical Terminology

## Core Idea
A proof is a logical argument establishing a conclusion from accepted premises. Key terms include theorem (important true statement), lemma (auxiliary helper result), corollary (consequence of a theorem), and conjecture (unproven claim). Understanding proof structure—hypothesis, logical steps, and conclusion—is essential for reading and writing mathematical arguments clearly.

## Questions

```yaml
- question: "A professor says: 'Let's prove the following: if n is even, then n² is divisible by 4.' A student asks, 'But how do we know n is even — is that proven?' The best response is:"
  type: multiple-choice
  options:
    - "We don't know — that's why it's a conjecture, not a theorem"
    - "It's given as a hypothesis — we assume it for the sake of the argument without needing to prove it"
    - "We'll prove n is even as the first step of the proof"
    - "We assume it's even because most integers are even"
  answer: 1
  explanation: "In proof structure, the hypothesis (or premise) is an assumption you are allowed to make for the sake of the argument — the 'P' in 'if P, then Q.' You do not prove the hypothesis; you assume it and derive the conclusion from it. The proof shows that *if* n is even *then* n² is divisible by 4. Confusing hypothesis with conjecture (option A) is the central misconception this topic addresses."

- question: "A textbook proves a major result about convergent series, then in the next paragraph states and proves a simple consequence in two lines. The second result would most naturally be called a:"
  type: multiple-choice
  options:
    - "Theorem — because it is independently true and important"
    - "Lemma — because it helps prove more important results later"
    - "Corollary — because it follows almost immediately from the theorem just proved"
    - "Conjecture — because it has only been shown in this specific case"
  answer: 2
  explanation: "A corollary is a result that follows almost immediately from a theorem just proved, requiring little additional work. A lemma (option B) is a helper result that assists in proving *later* theorems — the opposite direction. These labels are informal conventions about role and importance, not formal logical distinctions."

- question: "In mathematics, the hypothesis of a theorem is a guess or unproven claim that motivates the proof."
  type: true-false
  answer: false
  explanation: "This is the central misconception. In proof terminology, 'hypothesis' (or premise) means an assumed premise in a logical argument — the 'P' in 'if P, then Q.' It is not a guess; you assume it for the sake of the argument. The word that means 'unproven claim believed to be true' is *conjecture*. Conflating these two is a common error for students new to proof-writing, since 'hypothesis' in everyday scientific usage often does mean a tentative guess."

- question: "A lemma in one mathematical text might be called a theorem in another, because these labels reflect importance and role rather than formal logical distinctions."
  type: true-false
  answer: true
  explanation: "The labels theorem, lemma, and corollary are informal conventions about importance and status — not formal categories with precise logical definitions. A central result in a short paper might be labeled a lemma in a longer treatise that uses it as a stepping stone. The logical content is the same; only the labeling convention differs."

- question: "What is the difference between the 'hypothesis' of a proof and a 'conjecture,' and why does the distinction matter for reading proofs?"
  type: short-answer
  answer: "A hypothesis (or premise) is an assumption you make for the sake of a logical argument — the 'P' in 'if P, then Q.' You do not prove it; you derive the conclusion from it. A conjecture is a claim believed to be true but not yet proved. The distinction matters because when you read a theorem like 'if n is even, then n² is divisible by 4,' you must recognize that 'n is even' is the given assumption, not a claim being proved — misidentifying it makes you look for a proof where none is needed."
  explanation: "The first skill taught in any proof-writing course is identifying what is given versus what is to be shown. The hypothesis is the given; the conclusion is what must be shown. Conflating hypothesis with conjecture leads students to try to prove the hypothesis (which is already assumed) or to treat the conclusion as an assumption. Getting this structure right is prerequisite to reading any proof correctly."
```

## Explainer

You already understand logical connectives like "and," "or," "not," and "if…then." Proof structure is what you get when you organize those connectives into a complete argument. A **proof** is a finite sequence of statements where each statement either is a hypothesis, an axiom, or follows from earlier statements by a recognized inference rule. The final statement in the sequence is the **conclusion** — the claim you set out to establish.

The vocabulary of proofs divides results by their role in a mathematical text. A **theorem** is a significant, standalone result worth proving in its own right. A **lemma** is a helper result — a smaller claim whose main purpose is to make a later theorem's proof cleaner. A **corollary** is a result that follows almost immediately from a theorem just proved, requiring little additional work. A **conjecture** is a claim believed to be true but not yet proven. These labels are informal conventions about importance and status, not formal logical distinctions: a lemma in one text may be called a theorem in another.

Every proof has the same skeleton: **hypotheses**, a body of **logical steps**, and a **conclusion**. The hypotheses are the assumptions you are allowed to make — they are the "given" of the problem. The conclusion is what the theorem claims follows from those hypotheses. The steps in between are justified by definitions, previously proved results, axioms, or basic logical rules. Reading a proof means checking each step and asking: "why is this true, given what came before?" Writing a proof means supplying those justifications explicitly enough that a skeptical reader can follow them.

One subtlety worth internalizing from the start: the word **hypothesis** (or **premise**) refers to an assumption inside a logical argument — the "P" in "if P, then Q." It is not the same as a conjecture. When you prove "if n is even, then n² is even," the hypothesis is "n is even" — you assume it for the sake of the argument, regardless of whether you believe it's usually true. This assumption-bound-to-a-conclusion structure is the core form of almost every theorem in mathematics, and recognizing it — identifying what is given versus what is to be shown — is the first skill every proof-writing course teaches.
