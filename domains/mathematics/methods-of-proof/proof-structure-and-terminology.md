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

## Questions

```yaml
- question: "A student tries to prove 'If n is even, then n² is even.' They write: 'Assume n is even. Since even numbers squared are even, n² is even. Therefore if n is even, n² is even.' What is wrong with this proof?"
  type: multiple-choice
  options:
    - "The student stated the hypothesis incorrectly — they should have assumed n² is even"
    - "The student used the conclusion ('even numbers squared are even') as a step inside the proof, which assumes what was supposed to be demonstrated"
    - "The student needed to prove a lemma first before this argument could work"
    - "The student forgot to specify that n must be a positive integer"
  answer: 1
  explanation: "This is a circular argument — the most common beginner proof error. The claim 'even numbers squared are even' is exactly the statement the student is supposed to prove. Using it as a step inside the proof assumes the conclusion, making the argument logically empty. A valid proof must derive the conclusion from the hypothesis using only things already established: assume n is even, write n = 2k, compute n² = 4k² = 2(2k²), conclude n² is even by definition."

- question: "After proving a major theorem about the convergence of infinite series, a mathematician immediately observes that a simpler special case follows almost automatically as a consequence. This simpler result is called:"
  type: multiple-choice
  options:
    - "A lemma — a helper result proved specifically to support the main theorem"
    - "An axiom — a foundational assumption the theorem rests on"
    - "A corollary — a result that follows easily as a consequence of a just-proved theorem"
    - "A hypothesis — the conditional assumption from which the theorem was derived"
  answer: 2
  explanation: "A corollary is a result that follows readily from a theorem that has just been proved — it extends the theorem's reach almost for free. A lemma, by contrast, is proved before the main theorem to support it. An axiom is assumed without proof as a foundational rule. A hypothesis is the 'if' part of a conditional statement. These distinctions reflect the architecture of mathematical knowledge: theorems rest on lemmas, and corollaries extend their reach."

- question: "A lemma differs from an axiom in that a lemma must be proved, even though both serve as stepping stones in a larger argument."
  type: true-false
  answer: true
  explanation: "An axiom is assumed to be true without proof — it is a starting point, a foundational rule of the game. A lemma is a proved result: it is a full theorem, just one proved specifically because it is needed to establish something larger. Both play supporting roles in mathematical arguments, but only axioms are accepted without demonstration."

- question: "In a direct proof of 'If P, then Q,' the mathematician begins by assuming Q is true and then derives P — this is the standard structure of a direct proof."
  type: true-false
  answer: false
  explanation: "In a direct proof, you assume the hypothesis P and derive the conclusion Q. Assuming Q and deriving P is the structure of a proof by contrapositive (where you prove ¬P → ¬Q instead) or part of proof by contradiction. Reversing hypothesis and conclusion is a common beginner error — often confused with contrapositive reasoning. In a direct proof, the flow is always: start with P, apply logical steps, arrive at Q."

- question: "Why is writing a mathematical proof described as a 'communication to a reader' rather than just a chain of private reasoning, and what does this mean for how proofs should be structured?"
  type: short-answer
  answer: "A proof's purpose is not only to convince yourself but to allow any qualified reader to independently verify every step. This means logical transitions must be made explicit using precise language ('therefore,' 'it follows that,' 'assume,' 'we have shown'), the hypothesis and conclusion must be clearly separated so the reader knows what is being established, and each step must be justified by prior results, definitions, or axioms. Private reasoning can take shortcuts; a written proof cannot, because it must be independently checkable."
  explanation: "This is what distinguishes mathematics from other fields of argument. In mathematics, a claim is not accepted because the arguer is authoritative or the reasoning sounds plausible — it is accepted only when the logical structure is transparent enough that any qualified reader can trace every step. This standard is demanding precisely because it is what makes mathematical truth reliable: the proof stands or falls on its logic alone, independent of who wrote it."
```

## Explainer

From your study of logical equivalences, you know how to manipulate statements symbolically — recognizing when "P → Q" is equivalent to "¬Q → ¬P," or when a conjunction is equivalent to a disjunction. A **proof** is what connects abstract logical structure to actual mathematical content: it is a logically valid argument that establishes the truth of a mathematical statement, starting from things we already know. Understanding the vocabulary of proof is the first step to reading and writing mathematics fluently.

The **vocabulary of proof types** organizes mathematical results by their role. A **theorem** is a statement that has been proved true — it's the main result you're trying to establish. An **axiom** (or postulate) is assumed true without proof; it's a foundational rule of the game, like "two distinct points determine a unique line" in geometry. A **lemma** is a helper result — a theorem proved specifically because it's needed to prove something larger. A **corollary** is a result that follows easily from a theorem just proved, almost as a free consequence. These distinctions reflect the architecture of mathematical knowledge: big theorems rest on lemmas, which rest on axioms, and corollaries extend the reach of theorems.

The **structure of a theorem** is almost always "if P, then Q," where P is the **hypothesis** (what we assume) and Q is the **conclusion** (what we want to prove). Reading a theorem carefully means separating these two parts before doing anything else. When you prove a theorem, your job is to start with P and arrive at Q by logically valid steps. A common beginner error is to assume what you're trying to prove — a circular argument — or to prove something slightly different from Q. Keeping hypothesis and conclusion clearly distinguished prevents both mistakes.

A written proof is not just a private chain of reasoning — it's a **communication** to a reader. The goal is to make the logical structure transparent: the reader should be able to check every step independently. This is why proof-writing requires precision in language. "It follows that" and "therefore" signal logical consequences; "assume" and "suppose" signal the beginning of a hypothesis; "we have shown" signals the conclusion has been reached. Learning this vocabulary lets you parse complex proofs written by others and structure your own proofs so they can be verified — which is ultimately what distinguishes mathematics from every other kind of argument.
