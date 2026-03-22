---
id: independence-results-set-theory
title: Independence Results in Set Theory
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: continuum-hypothesis
  type: hard
- id: cofinality-and-regular-cardinals
  type: soft
- id: godels-incompleteness-theorems
  type: soft
tags:
- independence
- forcing
- constructible universe
- Godel
- Cohen
- models
stage: advanced
status: validated
---

# Independence Results in Set Theory

## Core Idea
A statement is independent of ZFC if neither it nor its negation is provable from ZFC. Gödel (1938) constructed the inner model L (the constructible universe) and showed both CH and AC hold in L, proving ZFC cannot refute them. Cohen (1963) invented forcing — building generic extensions of models by adding new sets satisfying carefully chosen conditions — and showed ZFC cannot prove CH or many other natural statements. Independence results demonstrate that ZFC leaves infinitely many natural questions about infinite sets undecided, including the exact value of 2^ℵ₀, the existence of measurable cardinals, and the projective determinacy of infinite games.

## How It's Best Learned
Study Gödel's L at the sketch level: sets built by definable operations in a transfinite hierarchy, within which CH holds by a counting argument. Then understand Cohen forcing conceptually: forcing conditions are finite partial approximations to a new 'generic' set; combining countably many conditions produces a model in which CH fails. The key takeaway is that different models of ZFC can have wildly different cardinal arithmetic.

## Common Misconceptions
- Independence does not mean a statement is meaningless or lacks a truth value — it means ZFC cannot determine it. Whether it has a 'real' truth value depends on philosophical commitments about mathematical Platonism.
- Forcing does not change 'the' actual universe of sets; it constructs alternative models within a meta-theory, usually ZFC itself or a fragment of it.

## Questions

```yaml
- question: "Gödel (1938) proved that CH is consistent with ZFC by:"
  type: multiple-choice
  options:
    - "Showing that CH can be derived as a theorem from the ZFC axioms alone"
    - "Constructing a model (the constructible universe L) in which all ZFC axioms and CH both hold, proving ZFC cannot refute CH"
    - "Showing that any model of ZFC satisfying ¬CH leads to a contradiction"
    - "Proving that the Continuum Hypothesis is equivalent to the Axiom of Choice within ZFC"
  answer: 1
  explanation: "Gödel proved only *half* of independence — that ZFC cannot refute CH. He did this by constructing L (the constructible universe), a specific model in which both ZFC and CH are satisfied. Since L is a model of ZFC + CH, ZFC is consistent with CH; if ZFC could prove ¬CH, then L would be a model satisfying a contradiction. Crucially, Gödel did NOT show ZFC can prove CH — that would require showing CH holds in every model of ZFC. Cohen's forcing (1963) completed the other half by constructing a model where CH fails."

- question: "A set theorist says: 'The Continuum Hypothesis is independent of ZFC.' What does this mean for the truth value of CH in specific models of ZFC?"
  type: multiple-choice
  options:
    - "CH has no truth value in any model — it is semantically meaningless"
    - "CH is true in some models of ZFC and false in others; ZFC alone cannot determine which"
    - "CH must be added as a new axiom before it can be assigned a truth value in any model"
    - "CH is true in the standard model of ZFC but unprovable from the axioms"
  answer: 1
  explanation: "Independence means ZFC is compatible with both CH and ¬CH — there exist models satisfying each. In Gödel's L, CH holds; in Cohen's forcing extensions, CH fails and 2^ℵ₀ can equal ℵ₂ or larger. So CH has definite truth values in individual models — it is simply not determined by ZFC alone which value it takes. This is very different from meaninglessness. The philosophical question of whether there is a 'real' answer beyond model relativity depends on commitments about mathematical Platonism."

- question: "Because CH is independent of ZFC, it is neither true nor false in any mathematical sense — it is simply an undecidable sentence with no determinate truth value."
  type: true-false
  answer: false
  explanation: "Independence from ZFC does not strip a statement of its truth value in models. CH is true in Gödel's constructible universe L and false in Cohen's forcing extensions — it has determinate truth values relative to specific models of set theory. What independence shows is that ZFC cannot pin down which universe of sets is 'the' real one. Whether CH has a mind-independent truth value is a separate philosophical question about mathematical Platonism, not a consequence of independence itself."

- question: "Cohen's forcing method works by constructing a new model of ZFC by extending an existing model with a 'generic' set that was not already in it."
  type: true-false
  answer: true
  explanation: "Forcing adds a new generic set G to a ground model M by specifying a partial order of finite approximations (forcing conditions) that describe G's behavior. A generic filter coherently collects compatible conditions and determines G completely. The extended model M[G] satisfies ZFC, and by choosing the forcing poset carefully, Cohen arranged for M[G] to contain ℵ₂ many subsets of ℵ₀ — making CH fail. Crucially, forcing constructs a new model; it does not modify ZFC's axioms."

- question: "What are Gödel's and Cohen's respective contributions to proving that CH is independent of ZFC, and why were both needed?"
  type: short-answer
  answer: "Independence requires proving two things: (1) ZFC cannot prove CH, and (2) ZFC cannot refute CH. Gödel proved (2) in 1938 by constructing L, the smallest model of ZFC, in which CH holds — showing ZFC is consistent with CH. Cohen proved (1) in 1963 by inventing forcing: he extended a model of ZFC to a model where 2^ℵ₀ = ℵ₂, making CH false — showing ZFC is consistent with ¬CH. Together, both halves establish that CH is neither provable nor refutable from ZFC; either can be added as an axiom without contradiction."
  explanation: "A common error is attributing the full independence result to Gödel alone. Gödel had only one direction: consistency of CH with ZFC. The other direction — consistency of ¬CH with ZFC — required Cohen's entirely new technique of forcing, which was a major breakthrough. Neither alone establishes independence; you need both models (one satisfying CH, one satisfying ¬CH) to prove the statement is genuinely undecidable from ZFC."
```

## Explainer

You already know from Gödel's incompleteness theorems that any sufficiently powerful consistent axiomatic system must leave some statements unprovable. You also know about the Continuum Hypothesis (CH) — the question of whether 2^ℵ₀ = ℵ₁. Independence results in set theory make the incompleteness phenomenon concrete and pervasive: natural, specific mathematical questions about infinite sets turn out to be undecidable from ZFC alone.

**Gödel's constructible universe** L was the first half of the proof. Gödel showed (1938) how to build a specific model of ZFC — the smallest possible model, in a precise sense — by iterating a process of taking "definable subsets" through all ordinal stages. In L, every set is explicitly constructable from simpler sets by first-order formulas. Within L, both the Axiom of Choice (AC) and the Continuum Hypothesis hold by a counting argument: the construction process is so constrained that there is no room for extra subsets of ℵ₀. Since L satisfies ZFC + CH, it follows that ZFC cannot refute CH: if ZFC were to prove CH false, L would witness a contradiction.

**Cohen's forcing** (1963) was the second half and is the deeper and more powerful technique. The key idea is to *extend* a model of ZFC by adding a new "generic" set G that was not already present. You specify G not by listing its elements explicitly, but by a **forcing poset** — a partial order of finite approximations (called forcing conditions) to the behavior of G. Each condition says a finite amount about what G will look like. A **generic filter** over this poset is a coherent collection of compatible conditions that decides everything about G. Cohen showed that starting from a countable transitive model M of ZFC, one can always find a generic filter G outside M, and the extended model M[G] also satisfies ZFC. By choosing the forcing poset carefully, he arranged for M[G] to contain ℵ₂ many subsets of ℵ₀, making CH fail. Since ZFC cannot prevent this extension, ZFC cannot prove CH.

The **forcing method** turned out to be extraordinarily general. Set theorists use it to build models where every natural number has a normal measure (measurability), where Martin's axiom holds but CH fails, where certain definable sets of reals are not Lebesgue measurable, and much more. The technique works by choosing forcing conditions tailored to the property you want to add. The meta-theorem is: if you want to show ZFC cannot prove some statement φ about sets, construct a forcing poset such that adding its generic object produces a model where φ fails.

The philosophical consequence is significant. ZFC is not a complete theory of sets — it cannot pin down the structure of infinite sets to a unique universe. Different forcing extensions of the same ground model give different "parallel" universes with different cardinal arithmetic. Some set theorists respond by seeking new axioms (large cardinal axioms, forcing axioms like PFA or MM) that resolve these independent questions and narrow the class of "acceptable" models. Others argue that independence results reveal genuine pluralism: there are many legitimate set-theoretic universes, not a unique one, and asking "which is the real one?" may be asking the wrong question.
