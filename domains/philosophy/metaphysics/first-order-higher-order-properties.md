---
id: first-order-higher-order-properties
title: First-Order and Higher-Order Properties
domain: philosophy
course: metaphysics
prerequisites:
- id: property-exemplification
  type: hard
- id: propositional-logic-introduction
  type: soft
builds-toward:
- higher-order-theories
tags:
- properties
- first-order
- higher-order
stage: formal-systems
status: validated
---

# First-Order and Higher-Order Properties

## Core Idea
First-order properties characterize individuals (being red, being massive, being conscious), while higher-order properties characterize properties themselves (being intrinsic, being causal, being sparse). Understanding whether higher-order properties are real and fundamental illuminates debates across metaphysics, logic, and philosophy of mind.

## Questions

```yaml
- question: "Which of the following is a higher-order property?"
  type: multiple-choice
  options:
    - "Being red"
    - "Being massive"
    - "Being intrinsic (having a property independently of relational facts about one's surroundings)"
    - "Being conscious"
  answer: 2
  explanation: "Being red, being massive, and being conscious are first-order properties — they characterize individuals (apples, particles, persons). Being intrinsic is a higher-order property: it characterizes properties themselves, distinguishing properties like mass (which an object has regardless of its relations) from properties like being-the-tallest-in-the-room (which depends on relational context). 'Being intrinsic' is not a feature of individuals but a feature of property types."

- question: "Functionalism in philosophy of mind defines mental states by their causal roles — pain is whatever state plays the pain-role. Why does this make functionalism a higher-order theory of mind?"
  type: multiple-choice
  options:
    - "Because it requires higher cognitive functions like reasoning to explain mental states"
    - "Because 'playing a causal role' is itself a property of property types — a higher-order property that mental state types must satisfy"
    - "Because it appeals to second-order logic to formally define mental predicates"
    - "Because mental properties are more abstract than the physical properties that realize them"
  answer: 1
  explanation: "Functionalism says pain is not defined by what it is physically made of but by the causal role it plays — what it is caused by, what it causes, how it interacts with other states. 'Playing the pain-role' is not a property of an individual but a property of a property type: it characterizes what kind of property pain must be. This is the structure of a higher-order property — a property that one property must have in relation to other properties."

- question: "Second-order logic extends first-order logic by allowing quantification over properties of individuals, not just over individuals themselves."
  type: true-false
  answer: true
  explanation: "First-order logic quantifies over individuals ('there exists an x such that...'). Second-order logic additionally allows quantification over properties of individuals ('there exists a property P such that...'). Third-order logic would allow quantification over properties of properties, and so on. Whether second-order quantification is genuinely irreducible to first-order quantification is a foundational question in logic."

- question: "Higher-order properties are never genuinely real — all talk about properties of properties can ultimately be reduced to first-order claims about individuals."
  type: true-false
  answer: false
  explanation: "Whether higher-order properties can be eliminated is a substantive and unresolved philosophical debate. A thoroughgoing nominalist might attempt this reduction; a Platonist about properties accepts higher-order properties as real at every level. Presenting eliminability as settled fact mistakes one contested philosophical position for an established result. The debate between nominalists and Platonists about properties is ongoing."

- question: "Give one example from metaphysics and one from philosophy of mind showing why the first-order/higher-order distinction matters."
  type: short-answer
  answer: "In metaphysics: 'being fundamental' (or being a sparse/natural property) is a higher-order property — it characterizes which first-order properties are genuine joints of reality. Saying charge is more fundamental than 'being next-to-something-blue' is a higher-order claim about properties, not about individual charged things. In philosophy of mind: functionalism's 'playing the pain-role' is a higher-order property, which is why the same mental state type can be multiply realized in different physical substrates — what matters is not what a state is physically made of (first-order) but what functional role it plays (higher-order)."
  explanation: "In both cases, the higher-order level captures something that first-order facts alone cannot express. Which properties are fundamental cannot be read off from first-order physical facts — it requires a metametaphysical judgment about property structure. And the type identity of mental states cannot be fixed at the first-order physical level if functionalism is right — it requires the higher-order characterization of causal role. The first-order/higher-order distinction thus carves a real explanatory boundary in both domains."
```

## Explainer

You already know from property exemplification that properties are instantiated by objects: the apple instantiates redness, the electron instantiates charge, the argument instantiates validity. These are **first-order properties**—their subjects are ordinary individuals (concrete or abstract things). The key move in this topic is recognizing that properties can themselves be the subjects of further properties. When a property has a property, that second-level property is a **higher-order property**.

Consider a few examples to build the intuition. The property *being red* is a first-order property of apples, fire trucks, and stop signs. But now consider the property *being a color*—this is a property that *being red* itself has, along with *being blue*, *being green*, and so on. Or consider *being intrinsic*: mass is intrinsic (a particle has it independently of its surroundings); being-the-tallest-person-in-the-room is extrinsic (it depends on relational facts). These—*being intrinsic*, *being extrinsic*, *being a color*, *being causal*—are higher-order properties, because they characterize properties, not individuals.

The distinction matters enormously for several debates you will encounter. In **logic and language**, first-order logic quantifies over individuals; second-order logic quantifies over properties of individuals; third-order logic quantifies over properties of properties of individuals. Whether we need genuinely higher-order quantification—or whether it can always be reduced to first-order—is a central question in the foundations of logic. In **metaphysics of properties**, recall that fundamental (sparse) properties are the genuinely natural joints of reality. *Being sparse* or *being fundamental* is itself a higher-order property: a metametaphysical claim about which first-order properties are real. In **philosophy of mind**, functionalism defines mental states by their causal role—pain is whatever state plays the pain-role. "Playing a causal role" is a higher-order property, which is why functionalism is sometimes called a **higher-order theory** of mind.

The deeper question is whether higher-order properties are real in their own right or whether talk about them can always be paraphrased away. A thoroughgoing nominalist might try to eliminate them; a Platonist about properties has no difficulty accepting them at every level. Understanding this hierarchy—and the commitments it entails—is the scaffolding for the more advanced theories of properties and mind that build on this topic.
