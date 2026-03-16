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
stage: formal-systems
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

## Explainer

You already know from Gödel's incompleteness theorems that any sufficiently powerful consistent axiomatic system must leave some statements unprovable. You also know about the Continuum Hypothesis (CH) — the question of whether 2^ℵ₀ = ℵ₁. Independence results in set theory make the incompleteness phenomenon concrete and pervasive: natural, specific mathematical questions about infinite sets turn out to be undecidable from ZFC alone.

**Gödel's constructible universe** L was the first half of the proof. Gödel showed (1938) how to build a specific model of ZFC — the smallest possible model, in a precise sense — by iterating a process of taking "definable subsets" through all ordinal stages. In L, every set is explicitly constructable from simpler sets by first-order formulas. Within L, both the Axiom of Choice (AC) and the Continuum Hypothesis hold by a counting argument: the construction process is so constrained that there is no room for extra subsets of ℵ₀. Since L satisfies ZFC + CH, it follows that ZFC cannot refute CH: if ZFC were to prove CH false, L would witness a contradiction.

**Cohen's forcing** (1963) was the second half and is the deeper and more powerful technique. The key idea is to *extend* a model of ZFC by adding a new "generic" set G that was not already present. You specify G not by listing its elements explicitly, but by a **forcing poset** — a partial order of finite approximations (called forcing conditions) to the behavior of G. Each condition says a finite amount about what G will look like. A **generic filter** over this poset is a coherent collection of compatible conditions that decides everything about G. Cohen showed that starting from a countable transitive model M of ZFC, one can always find a generic filter G outside M, and the extended model M[G] also satisfies ZFC. By choosing the forcing poset carefully, he arranged for M[G] to contain ℵ₂ many subsets of ℵ₀, making CH fail. Since ZFC cannot prevent this extension, ZFC cannot prove CH.

The **forcing method** turned out to be extraordinarily general. Set theorists use it to build models where every natural number has a normal measure (measurability), where Martin's axiom holds but CH fails, where certain definable sets of reals are not Lebesgue measurable, and much more. The technique works by choosing forcing conditions tailored to the property you want to add. The meta-theorem is: if you want to show ZFC cannot prove some statement φ about sets, construct a forcing poset such that adding its generic object produces a model where φ fails.

The philosophical consequence is significant. ZFC is not a complete theory of sets — it cannot pin down the structure of infinite sets to a unique universe. Different forcing extensions of the same ground model give different "parallel" universes with different cardinal arithmetic. Some set theorists respond by seeking new axioms (large cardinal axioms, forcing axioms like PFA or MM) that resolve these independent questions and narrow the class of "acceptable" models. Others argue that independence results reveal genuine pluralism: there are many legitimate set-theoretic universes, not a unique one, and asking "which is the real one?" may be asking the wrong question.
