---
id: continuum-hypothesis-and-independence
title: Continuum Hypothesis and Independence from ZFC
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: uncountable-sets-and-cantor-diagonalization
  type: hard
- id: cardinal-arithmetic-operations-and-exponentiation
  type: hard
- id: continuum-hypothesis
  type: soft
- id: forcing-intro
  type: soft
tags:
- continuum-hypothesis
- independence
- godel-cohen
- forcing
stage: advanced
status: draft
---

# Continuum Hypothesis and Independence from ZFC

## Core Idea
The Continuum Hypothesis (CH) asserts 2^ℵ₀ = ℵ₁—that there is no cardinal strictly between ℵ₀ and the continuum. Gödel proved CH is consistent with ZFC; Cohen proved its negation is also consistent. Thus CH is independent of ZFC: undecidable from the standard axioms alone.

## Questions

```yaml
- question: "Someone claims: 'Cohen's proof showed that ZFC can prove the Continuum Hypothesis.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Cohen showed ZFC can disprove CH, not prove it"
    - "Cohen showed ¬CH is consistent with ZFC, meaning ZFC cannot prove CH"
    - "Cohen showed CH is true in every model of ZFC"
    - "Cohen proved CH using large cardinal axioms, not forcing"
  answer: 1
  explanation: "Cohen's forcing construction built a model of ZFC in which CH *fails* — showing ¬CH is consistent with ZFC. This means ZFC cannot prove CH (if it could, CH would hold in all models). Combined with Gödel's result (ZFC cannot disprove CH), the two results together establish *independence*: ZFC neither proves nor disproves CH."

- question: "What did Gödel's constructible universe L establish about the Continuum Hypothesis?"
  type: multiple-choice
  options:
    - "CH is true in all possible set-theoretic universes"
    - "CH is equivalent to the Axiom of Choice"
    - "ZFC can prove CH, establishing it as a theorem"
    - "ZFC cannot disprove CH — CH is consistent with ZFC"
  answer: 3
  explanation: "Gödel showed that L is a model of ZFC in which CH is true. This means you cannot derive a contradiction from ZFC + CH: if ZFC is consistent, so is ZFC + CH. Crucially, this establishes only that CH cannot be *disproved* from ZFC — not that it is provable. Cohen's later result (¬CH is also consistent) completed the independence proof."

- question: "The independence of CH from ZFC means that both ZFC + CH and ZFC + ¬CH are consistent (assuming ZFC itself is consistent)."
  type: true-false
  answer: true
  explanation: "This is exactly what independence means: Gödel showed ZFC + CH is consistent (so ¬CH is not provable from ZFC), and Cohen showed ZFC + ¬CH is consistent (so CH is not provable from ZFC). Together, these results place CH beyond the reach of ZFC in either direction."

- question: "The independence of CH from ZFC settles that the Continuum Hypothesis has no definite truth value."
  type: true-false
  answer: false
  explanation: "Independence is a statement about *provability from axioms*, not about truth. A Platonist would say CH is either true or false in the actual universe of sets — we simply cannot determine which from ZFC. A pluralist might say there are many valid set-theoretic universes, some satisfying CH and some not. Independence leaves the philosophical question open but does not resolve it by declaring CH truth-valueless."

- question: "Why does establishing that CH is independent of ZFC not settle the question of whether CH is 'really' true?"
  type: short-answer
  answer: "Independence shows that ZFC is silent on CH — the axioms neither entail CH nor entail ¬CH. But 'true' depends on what we take as the intended universe of sets. ZFC is not the only possible axiomatic standard: adding large cardinal axioms, Martin's Axiom, or other principles can decide CH one way or another. Some set theorists believe there is a unique correct set-theoretic universe in which CH is determinately true or false; others accept a plurality of universes. Independence rules out a ZFC-proof, but leaves room for richer frameworks that do settle the question."
  explanation: "The key distinction is provability versus truth. Gödel's incompleteness theorems already showed that no consistent system strong enough to express arithmetic can prove all truths about its own subject matter. CH is another instance: the question of its truth lives beyond the reach of ZFC, but not necessarily beyond all mathematical investigation."
```

## Explainer

You already know from Cantor's diagonalization that the set of real numbers is strictly larger than the set of natural numbers — |ℝ| = 2^{ℵ₀} > ℵ₀. And from cardinal arithmetic you know that power sets jump to strictly larger cardinalities. The natural question is: exactly how much larger is 2^{ℵ₀}? The **Continuum Hypothesis** is the claim that 2^{ℵ₀} = ℵ₁ — the reals are precisely the *next* infinite cardinality after the naturals, with no cardinal in between. It is one of the most famous open questions in the history of mathematics, and its resolution revealed something unexpected: neither CH nor its negation is provable from the standard axioms.

Gödel established the first half in 1940 by constructing the **constructible universe L** — a minimal model of ZFC built by systematically defining only sets that are explicitly definable from earlier sets. In L, the axiom of choice holds, the generalized continuum hypothesis holds, and CH in particular holds. This means you cannot disprove CH from ZFC: if ZFC is consistent, then ZFC + CH is consistent, because L is a model of ZFC in which CH is true. Gödel's method is sometimes called an **inner model** argument — you build a carefully constrained universe inside any model of ZFC where the desired statement happens to be true.

Paul Cohen established the second half in 1963 using a radically new technique called **forcing**. Starting from a model of ZFC + CH, forcing constructs a carefully designed extension of the model — adding new "generic" sets — in which CH fails. The extended model satisfies all the ZFC axioms but contains enough real numbers to make 2^{ℵ₀} > ℵ₁. Cohen's construction showed you can add arbitrarily many reals to a model without contradiction. CH is therefore undecidable: neither CH nor ¬CH can be derived from ZFC alone. Together, Gödel and Cohen showed that CH is **independent** of ZFC — it is a statement that ZFC is simply silent about.

What does independence mean philosophically? It does not mean CH is meaningless or random. It means ZFC does not determine the answer. Set theorists have since explored both CH and its negation as possible axioms, and explored stronger axioms (large cardinal axioms, Martin's Axiom, Woodin's Ultimate L program) that do decide CH one way or another. Some mathematicians hold a Platonist view — there is a real mathematical universe and CH is either truly true or truly false, even if ZFC cannot tell us which. Others take a pluralist view — there are many consistent universes of set theory, and CH is true in some and false in others. The independence of CH was a watershed moment that permanently changed mathematicians' understanding of what axioms do and do not determine.
