---
id: direct-proof-methods
title: Direct Proof
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-structure-terminology
  type: hard
- id: predicates-and-quantifiers-intro
  type: soft
builds-toward:
- mathematical-induction-intro
tags:
- proof
- direct
stage: formal-systems
status: draft
---

# Direct Proof

## Core Idea
In a direct proof, we assume the hypothesis and logically derive the conclusion through valid inference steps. We follow a chain of implications from the hypothesis toward the goal, each step justified by definitions, axioms, or previously proven results. Direct proof is the most straightforward technique and should be attempted first whenever possible.

## Explainer

From your study of proof structure, you know that most mathematical theorems take the form "If P, then Q" — a hypothesis P and a conclusion Q. A **direct proof** works in the most natural direction: you assume P is true and then derive Q through a chain of logically valid steps. Each step in the chain must be justified — either by the definitions of the objects involved, by axioms of the system, or by previously proven results. The chain ends when you arrive at exactly Q.

The key discipline in a direct proof is unpacking definitions. When you assume "n is even," you immediately translate that into the definition: there exists an integer k such that n = 2k. This symbolic rewriting is usually the first move in any direct proof, and it's what makes the algebraic manipulation possible. Suppose you want to prove: "If m and n are both even, then m + n is even." You write m = 2j and n = 2k for integers j and k (the hypothesis, unpacked). Then m + n = 2j + 2k = 2(j + k). Since j + k is an integer, m + n is twice an integer — which is the definition of even. The proof is complete.

Notice how every step in that example was forced by what you knew. Once you unpacked the definitions, the algebra essentially wrote itself. This "follow the definitions" strategy is what makes direct proof the first technique to try. When the conclusion is a direct algebraic or logical consequence of the hypothesis, definitions give you a clear path. You should look for that path before reaching for more indirect techniques like proof by contradiction or contrapositive.

The structure of the proof matters as much as its content. A written direct proof should explicitly state what is being assumed (the hypothesis), present each logical step in order, and make clear which definition or result justifies each step. Vague prose like "obviously" or "clearly" hides the logical work and makes it impossible to check correctness. Good proof-writing is essentially annotated reasoning: every claim earns its place with a justification, and the reader should be able to verify each step independently. This discipline is what distinguishes a proof from a plausible argument.
