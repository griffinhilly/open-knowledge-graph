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

## Explainer

You already understand logical connectives like "and," "or," "not," and "if…then." Proof structure is what you get when you organize those connectives into a complete argument. A **proof** is a finite sequence of statements where each statement either is a hypothesis, an axiom, or follows from earlier statements by a recognized inference rule. The final statement in the sequence is the **conclusion** — the claim you set out to establish.

The vocabulary of proofs divides results by their role in a mathematical text. A **theorem** is a significant, standalone result worth proving in its own right. A **lemma** is a helper result — a smaller claim whose main purpose is to make a later theorem's proof cleaner. A **corollary** is a result that follows almost immediately from a theorem just proved, requiring little additional work. A **conjecture** is a claim believed to be true but not yet proven. These labels are informal conventions about importance and status, not formal logical distinctions: a lemma in one text may be called a theorem in another.

Every proof has the same skeleton: **hypotheses**, a body of **logical steps**, and a **conclusion**. The hypotheses are the assumptions you are allowed to make — they are the "given" of the problem. The conclusion is what the theorem claims follows from those hypotheses. The steps in between are justified by definitions, previously proved results, axioms, or basic logical rules. Reading a proof means checking each step and asking: "why is this true, given what came before?" Writing a proof means supplying those justifications explicitly enough that a skeptical reader can follow them.

One subtlety worth internalizing from the start: the word **hypothesis** (or **premise**) refers to an assumption inside a logical argument — the "P" in "if P, then Q." It is not the same as a conjecture. When you prove "if n is even, then n² is even," the hypothesis is "n is even" — you assume it for the sake of the argument, regardless of whether you believe it's usually true. This assumption-bound-to-a-conclusion structure is the core form of almost every theorem in mathematics, and recognizing it — identifying what is given versus what is to be shown — is the first skill every proof-writing course teaches.
