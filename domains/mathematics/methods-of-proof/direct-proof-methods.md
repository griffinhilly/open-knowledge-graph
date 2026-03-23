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
status: validated
---

# Direct Proof

## Core Idea
In a direct proof, we assume the hypothesis and logically derive the conclusion through valid inference steps. We follow a chain of implications from the hypothesis toward the goal, each step justified by definitions, axioms, or previously proven results. Direct proof is the most straightforward technique and should be attempted first whenever possible.

## Questions

```yaml
- question: "You want to prove: 'If n is odd, then n² is odd.' What is the correct first step in a direct proof?"
  type: multiple-choice
  options:
    - "Write n² = (n−1)(n+1) + 1 and argue it must be odd"
    - "Write n = 2k + 1 for some integer k, applying the definition of odd to the hypothesis"
    - "Assume n² is even and derive a contradiction"
    - "Note that squaring preserves parity, so the result follows immediately"
  answer: 1
  explanation: "The first move in a direct proof is always to unpack the hypothesis using its formal definition. 'n is odd' means there exists an integer k such that n = 2k + 1. Without this translation, you have nothing algebraic to work with. Options C and D are errors in proof strategy: option C describes proof by contradiction (not direct proof), and option D is precisely the kind of vague assertion a valid proof must replace with a justified derivation."

- question: "A student proves 'the sum of two even integers is even' by writing: 'Let m and n be even. Since both are even, clearly m + n is even. QED.' What is wrong with this proof?"
  type: multiple-choice
  options:
    - "Nothing — if the statement is true and both integers are even, the conclusion follows"
    - "The word 'clearly' hides the logical work; the proof must show that m + n has the algebraic form 2·(integer) by unpacking the definitions"
    - "The student should have used mathematical induction instead of a direct proof"
    - "The proof is circular because it assumes what it is trying to prove"
  answer: 1
  explanation: "Writing 'clearly m + n is even' is not a proof — it is a claim without justification. A valid direct proof writes m = 2j and n = 2k (unpacking 'even'), computes m + n = 2j + 2k = 2(j + k), and concludes that since j + k is an integer, m + n is twice an integer and therefore even. Each step must be checkable. 'Clearly' and 'obviously' are warning signs that the logical work is being hidden."

- question: "In a direct proof, the standard first move after stating the hypothesis is to translate it into its formal definition — for example, replacing 'n is even' with 'n = 2k for some integer k.'"
  type: true-false
  answer: true
  explanation: "Definition-unpacking is the key first step because it converts an abstract predicate ('is even') into an algebraic form (n = 2k) that can be manipulated. This translation is what makes the subsequent chain of reasoning possible. Without it, you have only the words of the hypothesis, not the formal machinery needed to derive the conclusion."

- question: "A direct proof works by assuming the conclusion is true and deriving the hypothesis from it."
  type: true-false
  answer: false
  explanation: "A direct proof works in the natural direction: assume the hypothesis P is true, then derive the conclusion Q through valid steps. Assuming Q and deriving P is not a valid proof of P → Q; it would prove the converse (Q → P) instead. Confusing these directions is a fundamental error — the proof must flow from hypothesis to conclusion, not the other way around."

- question: "Why is 'unpacking definitions' the critical first step in most direct proofs, and what goes wrong if you skip it?"
  type: short-answer
  answer: "Definitions translate abstract claims into algebraic or logical forms that can be manipulated step by step. 'n is even' is a predicate about n; 'n = 2k for some integer k' is an equation you can substitute, add, and factor. Without this translation, you have no formal foothold — any subsequent steps are either intuitive leaps or circular assertions. Skipping definitions forces you to argue in natural language, where it is easy to smuggle in assumptions and impossible to verify correctness rigorously."
  explanation: "This is what makes direct proof a discipline rather than just 'writing down the obvious.' The algebraic manipulation that follows definition-unpacking is usually straightforward — once m = 2j and n = 2k are in place, m + n = 2(j + k) writes itself. The entire work of the proof is in the first translation step."
```

## Explainer

From your study of proof structure, you know that most mathematical theorems take the form "If P, then Q" — a hypothesis P and a conclusion Q. A **direct proof** works in the most natural direction: you assume P is true and then derive Q through a chain of logically valid steps. Each step in the chain must be justified — either by the definitions of the objects involved, by axioms of the system, or by previously proven results. The chain ends when you arrive at exactly Q.

The key discipline in a direct proof is unpacking definitions. When you assume "n is even," you immediately translate that into the definition: there exists an integer k such that n = 2k. This symbolic rewriting is usually the first move in any direct proof, and it's what makes the algebraic manipulation possible. Suppose you want to prove: "If m and n are both even, then m + n is even." You write m = 2j and n = 2k for integers j and k (the hypothesis, unpacked). Then m + n = 2j + 2k = 2(j + k). Since j + k is an integer, m + n is twice an integer — which is the definition of even. The proof is complete.

Notice how every step in that example was forced by what you knew. Once you unpacked the definitions, the algebra essentially wrote itself. This "follow the definitions" strategy is what makes direct proof the first technique to try. When the conclusion is a direct algebraic or logical consequence of the hypothesis, definitions give you a clear path. You should look for that path before reaching for more indirect techniques like proof by contradiction or contrapositive.

The structure of the proof matters as much as its content. A written direct proof should explicitly state what is being assumed (the hypothesis), present each logical step in order, and make clear which definition or result justifies each step. Vague prose like "obviously" or "clearly" hides the logical work and makes it impossible to check correctness. Good proof-writing is essentially annotated reasoning: every claim earns its place with a justification, and the reader should be able to verify each step independently. This discipline is what distinguishes a proof from a plausible argument.
