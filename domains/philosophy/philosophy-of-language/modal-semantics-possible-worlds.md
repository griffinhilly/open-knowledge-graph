---
id: modal-semantics-possible-worlds
title: Modal Semantics and Possible Worlds
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: possible-worlds-semantics
  type: hard
- id: modal-logic-intro
  type: hard
builds-toward:
- temporal-semantics-and-tense
- counterfactual-conditionals
tags:
- modality
- possible-worlds
- necessity
- semantics
stage: advanced
status: draft
---

# Modal Semantics and Possible Worlds

## Core Idea
Modal sentences involving necessity and possibility are analyzed using possible worlds: a sentence is necessarily true iff true at all possible worlds; possibly true iff true at some accessible world. This extends truth-conditional semantics to modal discourse by adding a dimension of possible alternatives.

## How It's Best Learned
Understand accessibility relations and how different modal logics (K, S4, S5) correspond to different properties of accessibility. Work through simple modal sentences and their truth conditions across worlds.

## Questions

```yaml
- question: "Consider the sentence: 'Necessarily, the number of planets is greater than seven.' Is this true or false in standard possible worlds semantics (S5), and why?"
  type: multiple-choice
  options:
    - "True, because 'the number of planets' picks out the number 8, which necessarily exceeds 7"
    - "False, because 'the number of planets' is a non-rigid description — in some possible worlds there are fewer than eight planets"
    - "True, because the sentence is about actual astronomy, which doesn't change across worlds"
    - "False, because mathematical claims cannot be expressed in natural language modal semantics"
  answer: 1
  explanation: "This is a de dicto reading: necessity attaches to the proposition 'the number of planets is greater than seven.' 'The number of planets' is a non-rigid description — it picks out whatever number happens to be the count of planets in each world. In worlds with six planets, this description picks out 6, and 6 > 7 is false. So the sentence is false: there exist accessible worlds where it fails. Compare: 'Necessarily, 8 is greater than 7' is true, because '8' is a rigid numeral that picks out 8 in every world. The distinction between rigid (names, numerals) and non-rigid (descriptions) is precisely what Kripke's insight resolves."

- question: "Two modal logics differ only in their accessibility relations: Logic A has a reflexive, transitive relation; Logic B has an equivalence relation (reflexive, symmetric, transitive). What is the key difference in what they count as necessary?"
  type: multiple-choice
  options:
    - "Logic A allows more sentences to be necessary because reflexivity adds more worlds"
    - "In Logic B (S5), if something is possible, it is necessarily possible — the accessibility relation links all worlds to all worlds, making necessity absolute"
    - "Logic A is stronger because transitive accessibility means necessity propagates further"
    - "There is no meaningful difference between these logics for natural language"
  answer: 1
  explanation: "Logic B corresponds to S5 (reflexive + symmetric + transitive = equivalence relation). In S5, accessibility is universal: every world can access every other. This makes necessity 'absolute' — if p is necessarily true at any world, it's necessary at all worlds. The S5 axiom '◇p → □◇p' (if possibly p, then necessarily possibly p) holds. Logic A (reflexive + transitive, corresponding to S4) lacks symmetry: some worlds may not access back to the actual world, so necessity in distant worlds doesn't necessarily propagate back. S5 is typically used for metaphysical modality; S4 is used for epistemic contexts where knowledge doesn't propagate symmetrically."

- question: "In possible worlds semantics, a sentence is necessarily true if and only if it is true in the actual world."
  type: true-false
  answer: false
  explanation: "This conflates truth with necessary truth. A sentence is true if it holds at the actual world; it is *necessarily* true if it holds at every accessible possible world. Many sentences are true at the actual world without being necessarily true — 'Barack Obama was the 44th U.S. president' is actually true but not necessary, since there are possible worlds where someone else held that office. Necessary truth is a far stronger claim than actual truth. The whole point of modal semantics is to capture this distinction formally, using possible worlds to define the 'at every world' quantifier."

- question: "According to Kripke's possible worlds semantics, a proper name like 'Aristotle' rigidly designates the same individual across all possible worlds, whereas a definite description like 'the teacher of Alexander' may pick out different individuals in different worlds."
  type: true-false
  answer: true
  explanation: "This is Kripke's doctrine of rigid designation. Names are rigid: 'Aristotle' refers to that specific person — Aristotle of Stagira — in every world where he exists, even worlds where he never taught Alexander. Descriptions are typically non-rigid: 'the teacher of Alexander' picks out whoever taught Alexander in each world, which could be a different person in different worlds. This explains why 'Aristotle was necessarily Aristotle' is true (a rigid designator refers to the same object in all worlds) but 'Aristotle was necessarily the teacher of Alexander' is false (in some worlds, Aristotle might have pursued a different career)."

- question: "Why does the accessibility relation matter in possible worlds semantics, and how do different properties of this relation correspond to different modal logics?"
  type: short-answer
  answer: "The accessibility relation determines which worlds count when evaluating modal claims. 'Necessarily p' means p is true at all worlds accessible from the current world — so whether a sentence is necessary depends entirely on which worlds are considered accessible. Different properties of accessibility correspond to different modal axioms: reflexivity (every world accesses itself) corresponds to the T axiom (what's necessary is true); transitivity corresponds to the S4 axiom (what's necessarily necessary is necessary); symmetry combined with transitivity and reflexivity gives S5, where accessibility is universal and necessity is absolute."
  explanation: "This is why modal logic is not one logic but a family: K, T, S4, S5 each impose different constraints on accessibility and thus make different sentences come out as valid. For metaphysical modality, S5 is usually assumed — metaphysical necessity holds in all worlds without restriction. For epistemic modality (what is known), symmetry fails because knowledge is not symmetric between agents. The power of possible worlds semantics is that it gives a uniform semantic framework that models all these different notions of modality by varying one parameter: the accessibility relation."
```

## Explainer

Modal language — "necessarily," "possibly," "could have been," "must" — is pervasive but semantically opaque without a framework. What does it even mean to say something is necessary? From your study of possible worlds semantics and modal logic, you know the fundamental setup: a **possible world** is a complete way reality could be or could have been. The actual world is one possible world — the way things are. Other worlds are the ways things might have been. Modal semantics cashes out necessity and possibility as quantification over these worlds.

The core semantic clauses are elegant. A sentence is **necessarily true** if and only if it is true at every possible world accessible from the world of evaluation. It is **possibly true** if and only if it is true at some accessible world. The notion of an **accessibility relation** is what differentiates modal logics. If every world accesses every other, we get S5 — the logic typically used for metaphysical modality, where what's necessarily true is so in all worlds without restriction. If accessibility is reflexive but not symmetric (every world accesses itself, but not necessarily every other), we get different systems. Your modal logic background lets you see that formal axioms correspond to properties of accessibility: the T axiom ("if necessarily p, then p") corresponds to reflexivity — every world accesses itself, so what's necessary in this world is true here.

The philosophical significance goes beyond formal elegance. Possible worlds semantics gives a uniform account of **de dicto** and **de re** modality — the difference between necessity attributed to a proposition versus necessity attributed to an object's property. "Necessarily, the number of planets is greater than seven" (de dicto) is false: in some worlds, there are fewer planets. "Eight necessarily has the property of being greater than seven" (de re) is true: in every world, eight exceeds seven. The analysis uses **rigid designators** — terms like numerals and proper names that pick out the same object in every world — versus non-rigid descriptions like "the number of planets." Kripke's insight was that names are rigid while descriptions often are not, which explains why "Aristotle was necessarily Aristotle" is true but "Aristotle was necessarily the teacher of Alexander" is not.

The framework extends naturally to **counterfactual conditionals**: "if it had rained, the match would have been canceled" is true at a world w if and only if the closest worlds to w where it rained are worlds where the match was canceled. "Closest" is measured by a similarity ordering — Lewis's account uses exactly this structure. Possible worlds semantics thus serves triple duty: it formalizes modal logic, provides truth conditions for modal language in natural language, and underpins the semantics of counterfactuals. Understanding the unifying role of this framework — how a single ontological apparatus addresses questions from logic, language, and metaphysics simultaneously — is what makes it central to contemporary analytic philosophy.

