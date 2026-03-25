---
id: possible-worlds-framework
title: Possible Worlds Framework
domain: philosophy
course: metaphysics
prerequisites:
- id: possible-worlds-semantics
  type: hard
- id: modal-semantics-possible-worlds
  type: hard
- id: modal-logic-intro
  type: soft
- id: counterfactual-truth-modality
  type: soft
builds-toward:
- abstract-objects-existence
tags:
- possible-worlds
- modality
- necessity
- semantics
stage: formal-systems
status: validated
---
# Possible Worlds Framework

## Core Idea
Possible worlds provide a formal framework for analyzing modal truths and metaphysical claims. A proposition is necessarily true if it's true in all possible worlds; something is essential if it holds in all worlds where the object exists. This framework has become central to contemporary metaphysics.

## How It's Best Learned
Work with concrete examples (is water necessarily H2O? Is Hesperus necessarily Phosphorus?). Understand how possible worlds semantics connects to modal logic. Compare to counterpart-theory as an alternative.

## Common Misconceptions
That possible worlds are metaphysically remote abstract objects. That anything logically consistent is possible. That the possible worlds framework is purely linguistic or artificial.

## Questions

```yaml
- question: "A property P is essential to object x according to the possible worlds framework. Which analysis is correct?"
  type: multiple-choice
  options:
    - "P is a property x has in the actual world — essential means actually possessed"
    - "P is a property x has in every possible world in which x exists"
    - "P is a necessary truth that applies to all objects, not just x"
    - "P is a property x would have regardless of circumstances, but only in worlds similar to the actual world"
  answer: 1
  explanation: "On the possible worlds framework, a property is essential to an object just in case that object has it in every world where the object exists. Option 0 confuses essential with actual — an object can have many actual properties that are merely accidental (it has them in this world but could have lacked them). An accidental property is one the object has in the actual world but lacks in some possible world. The distinction essential/accidental corresponds precisely to all-worlds vs. some-world."

- question: "Consider the claim 'It is possibly true that 7 is even.' How does the possible worlds framework evaluate this?"
  type: multiple-choice
  options:
    - "True — we can conceive of a world where mathematics works differently"
    - "False — '7 is even' is false in every possible world, making it necessarily false rather than merely actually false"
    - "True if Lewis's modal realism is correct, false if abstractionism is correct"
    - "Undecidable — possible worlds semantics applies to contingent claims, not mathematical ones"
  answer: 1
  explanation: "On the possible worlds framework, possibility means truth in at least one possible world. '7 is even' is a mathematical claim whose negation is a necessary truth — it is false in every possible world. Therefore it is not merely actually false but necessarily false (impossible). Importantly, this is a stronger claim than 'we cannot conceive of it easily.' The framework sharply distinguishes conceivability (an epistemic notion) from genuine metaphysical possibility (truth in some world)."

- question: "On the possible worlds framework, a proposition is necessarily true if it is true in the actual world and true in most, but not all, possible worlds."
  type: true-false
  answer: false
  explanation: "Necessity requires truth in ALL possible worlds without exception — not merely most, or many, or a preponderance. A proposition true in all but one possible world would be contingent (possibly false) rather than necessary. This is one of the framework's most important contributions: making necessary truth into a precise, fully universal quantification over possible worlds rather than a vague claim about robustness."

- question: "The possible worlds framework enables precise, non-circular definitions of what it means for a property to be essential or accidental to an object."
  type: true-false
  answer: true
  explanation: "Before the possible worlds framework, essential properties were often defined using primitive modal notions ('essential' means 'necessarily possessed') — circular and uninformative. The framework replaces 'necessarily' with explicit quantification over possible worlds: essential = holds in all worlds where the object exists; accidental = holds in the actual world but not all worlds where the object exists. This is not circular — it reduces the modal claim to world-quantification."

- question: "What is the fundamental difference between Lewis's modal realism and abstractionist accounts of possible worlds, and what is each account's main tradeoff?"
  type: short-answer
  answer: "Lewis holds that possible worlds are concrete, spatiotemporally isolated universes existing as fully as the actual world — 'actual' is indexical, meaning just our world. This gives a fully reductive account of modality with no primitive modal notions, but it is ontologically extravagant (infinitely many concrete universes exist). Abstractionism (Plantinga, Adams) holds worlds are abstract objects — maximal consistent sets of propositions or states of affairs — that exist necessarily but non-concretely. This is ontologically conservative but must rely on primitive modal notions like 'consistent' rather than reducing them."
  explanation: "The tradeoff is parsimony of ideology (Lewis) vs. parsimony of ontology (abstractionists). Lewis buys clean semantics at the cost of exotic ontology. Abstractionists avoid exotic ontology but retain modal primitives in their machinery, arguably not fully explaining what modality is."
```

## Explainer

You've already encountered possible worlds in their semantic role — as tools for giving truth conditions to modal statements in formal logic. The possible worlds *framework* takes that semantic machinery and asks a deeper question: what are these worlds, metaphysically? What is a possible world, and what work can the framework do beyond interpreting modal logic? This is where the formal tool becomes a philosophical theory in its own right.

The central insight is that **modal truths** — claims about what is necessary, possible, or impossible — can be systematically analyzed in terms of possible worlds. "It is necessarily true that 2+2=4" means: in every possible world, 2+2=4. "It is possibly true that there is intelligent life elsewhere in the universe" means: in at least one possible world, there is intelligent life elsewhere. "It is impossible to be a married bachelor" means: in no possible world is anyone both married and a bachelor. This framework gives modal claims precise truth conditions and lets us reason about necessity and possibility with the same tools we use for ordinary truth.

The metaphysical dispute concerns the *nature* of these worlds. David Lewis's **modal realism** holds that possible worlds are just as concrete and real as the actual world — they are complete spatiotemporally isolated universes, and "the actual world" just means *our* world, the one we inhabit. On this view, when we say something is possible, we are genuinely quantifying over things that exist. Lewis's theory is ontologically extravagant but logically elegant: it gives a fully reductive account of modality with no primitive modal notions. The opposing view, **modal abstractionism** (associated with Plantinga and others), holds that possible worlds are abstract objects — maximal consistent sets of propositions, or ways things could be — that exist necessarily but non-concretely. The actual world is the one that is **instantiated**, while merely possible worlds are abstract structures that could have been instantiated but aren't.

For essentialism, the framework delivers precise tools. A property is **essential** to an object if and only if the object has that property in every possible world in which it exists. A property is **accidental** if the object has it in the actual world but lacks it in some possible world. These definitions transform what could be vague intuitions into precise claims subject to argument and counterexample. The framework also undergirds theories of **counterfactuals** ("If you had studied harder, you would have passed"), **de re modality** (necessity attributed to objects, not just descriptions), and the semantics of natural-kind terms — making possible worlds one of the most productive frameworks in contemporary metaphysics.
