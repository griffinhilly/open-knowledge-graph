---
id: proof-structure-and-terminology
title: Proof Structure and Terminology
domain: mathematics
course: methods-of-proof
prerequisites:
- id: logical-equivalences
  type: hard
builds-toward:
- direct-proof
- proof-by-contrapositive
tags:
- proof
- structure
- terminology
stage: formal-systems
status: draft
---

# Proof Structure and Terminology

## Core Idea
Proofs are logical arguments establishing truth of statements using axioms and logical rules. Key terms: theorem (proven statement), axiom (assumed true), lemma (helper result), corollary (consequence), hypothesis and conclusion (if-then parts).

## Explainer

From your study of logical equivalences, you know how to manipulate statements symbolically — recognizing when "P → Q" is equivalent to "¬Q → ¬P," or when a conjunction is equivalent to a disjunction. A **proof** is what connects abstract logical structure to actual mathematical content: it is a logically valid argument that establishes the truth of a mathematical statement, starting from things we already know. Understanding the vocabulary of proof is the first step to reading and writing mathematics fluently.

The **vocabulary of proof types** organizes mathematical results by their role. A **theorem** is a statement that has been proved true — it's the main result you're trying to establish. An **axiom** (or postulate) is assumed true without proof; it's a foundational rule of the game, like "two distinct points determine a unique line" in geometry. A **lemma** is a helper result — a theorem proved specifically because it's needed to prove something larger. A **corollary** is a result that follows easily from a theorem just proved, almost as a free consequence. These distinctions reflect the architecture of mathematical knowledge: big theorems rest on lemmas, which rest on axioms, and corollaries extend the reach of theorems.

The **structure of a theorem** is almost always "if P, then Q," where P is the **hypothesis** (what we assume) and Q is the **conclusion** (what we want to prove). Reading a theorem carefully means separating these two parts before doing anything else. When you prove a theorem, your job is to start with P and arrive at Q by logically valid steps. A common beginner error is to assume what you're trying to prove — a circular argument — or to prove something slightly different from Q. Keeping hypothesis and conclusion clearly distinguished prevents both mistakes.

A written proof is not just a private chain of reasoning — it's a **communication** to a reader. The goal is to make the logical structure transparent: the reader should be able to check every step independently. This is why proof-writing requires precision in language. "It follows that" and "therefore" signal logical consequences; "assume" and "suppose" signal the beginning of a hypothesis; "we have shown" signals the conclusion has been reached. Learning this vocabulary lets you parse complex proofs written by others and structure your own proofs so they can be verified — which is ultimately what distinguishes mathematics from every other kind of argument.
