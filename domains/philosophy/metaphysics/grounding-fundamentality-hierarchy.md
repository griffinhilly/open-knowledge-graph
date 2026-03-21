---
id: grounding-fundamentality-hierarchy
title: Grounding and the Hierarchy of Fundamental Facts
domain: philosophy
course: metaphysics
prerequisites:
- id: grounding-and-fundamentality
  type: hard
- id: facts-and-truthmakers
  type: soft
- id: truthmaker-fundamentalism
  type: soft
builds-toward:
- metaphysical-structure-and-architecture
- fundamental-properties-sparse-abundant
tags:
- grounding
- fundamentality
- hierarchy
- structure
- metaphysics
stage: formal-systems
status: draft
---

# Grounding and the Hierarchy of Fundamental Facts

## Core Idea
Grounding is the 'in-virtue-of' relation: fact B holds in virtue of fact A grounding B. A full metaphysical picture specifies which facts are fundamental (ungrounded) and how all other facts are grounded in these fundamentals, forming a hierarchy that reveals what reality is fundamentally like.

## Questions

```yaml
- question: "A philosopher says: 'The fact that water is H₂O causes the fact that water is wet.' A grounding theorist would object that this misdescribes the relationship. Why?"
  type: multiple-choice
  options:
    - "Water being H₂O does not actually explain water's wetness — the two facts are unrelated"
    - "Causation is a temporal relation between events; grounding is an atemporal in-virtue-of relation between facts — the molecular structure doesn't cause wetness over time, it constitutes its metaphysical basis"
    - "The fundamental level contains only physical facts, so chemical facts cannot ground phenomenal ones"
    - "Wetness is a fundamental fact and is not grounded in anything"
  answer: 1
  explanation: "Causation and grounding are distinct relations. Causation is temporal: event A brings about event B by preceding it. Grounding is atemporal: fact B holds in virtue of fact A right now, constituting its metaphysical basis rather than producing it over time. The molecular structure of water doesn't cause its wetness by preceding it — the structure is what makes wetness obtain. Conflating these relations mischaracterizes the explanatory structure grounding theory is designed to capture."

- question: "What does it mean to say the grounding hierarchy is 'well-founded'?"
  type: multiple-choice
  options:
    - "The hierarchy is based on empirical evidence from physics and chemistry"
    - "There is a bedrock of fundamental, ungrounded facts at which the chain of 'what grounds what' terminates"
    - "Every fact in the hierarchy has exactly one grounding fact beneath it"
    - "The hierarchy is organized by causal priority, with earlier events at the bottom"
  answer: 1
  explanation: "Well-foundedness means the grounding hierarchy does not descend forever — there is a bottom level of fundamental facts that are not themselves grounded in anything further. Without well-foundedness, every fact's grounding appeal would point to yet another grounded fact, producing an infinite regress that leaves everything ultimately unexplained. Most metaphysicians assume well-foundedness because an explanatory chain that never bottoms out seems to explain nothing in the end, even if each individual step is valid."

- question: "Grounding is an asymmetric relation: if A grounds B, then B cannot ground A."
  type: true-false
  answer: true
  explanation: "Asymmetry is a core feature of grounding. The fact that this surface has these reflective properties grounds the fact that it is red — but the redness does not in turn ground the reflective properties. The relation runs in one direction only, from the more fundamental to the less fundamental. Symmetry would collapse the hierarchy into a flat structure with no genuine priority, defeating the point of positing grounding as a metaphysical relation at all. Grounding is designed to capture dependence, and dependence is inherently directional."

- question: "Grounding is the same relation as logical entailment: whenever the facts at level A logically entail the facts at level B, A grounds B."
  type: true-false
  answer: false
  explanation: "Grounding and logical entailment are distinct. Entailment is a logical relation between propositions: some statements guarantee the truth of others by logical necessity. Grounding is a metaphysical relation between facts in reality: B holds in virtue of A, capturing real-world dependence rather than logical inference. Many entailments are not groundings (mathematical truths entail each other without one grounding the other in the relevant metaphysical sense), and grounding theorists argue the relation must be metaphysically primitive, not reducible to logic or necessity."

- question: "Why do most metaphysicians assume that the grounding hierarchy is well-founded (terminates at a bedrock), and what would it mean if it were not?"
  type: short-answer
  answer: "Well-foundedness is assumed because an infinite regress of grounding — where every fact is grounded in another, which is grounded in another, with no terminus — seems to leave everything metaphysically unexplained. If there is no bedrock, the chain of 'what grounds what' always passes the explanatory buck: there is no ultimate account of why anything is the way it is. A non-well-founded hierarchy would mean reality has no fundamental level — every layer of explanation bottoms out in yet another layer requiring explanation."
  explanation: "The assumption is contested: some philosophers argue that a non-well-founded but coherent explanatory structure is possible, with each step genuinely informative even without a terminus. The debate concerns whether the purpose of grounding — revealing what reality is fundamentally like — requires a bedrock or merely requires each step in the chain to be genuinely explanatory. For most working metaphysicians, well-foundedness is load-bearing: it is what makes the question 'what is fundamental?' a coherent inquiry with a determinate answer, rather than an infinitely regressing one."
```

## Explainer

From your study of grounding and fundamentality you already know the basic idea: some facts depend on — hold *in virtue of* — other facts. The fact that the table is red holds in virtue of facts about how its surface reflects light; the fact that a symphony is beautiful holds in virtue of facts about its structure and our responses to it. **Grounding** is the formal name for this dependence relation. It is not the same as causation (which relates events over time) and not the same as logical entailment (which is a relation between propositions, not facts). Grounding is meant to capture the distinctively *metaphysical* sense in which some facts make other facts obtain.

The concept of a **hierarchy** adds structure to this picture. Imagine a vast directed graph where each node is a fact and each arrow points from a grounding fact to a grounded fact. At the bottom of the graph sit the **fundamental facts** — those that are not themselves grounded in anything. These are the bedrock: they explain without being explained (in the metaphysical sense). Everything above them is grounded, directly or indirectly, in the fundamental level. A complete metaphysical theory would describe what sits at the bottom and trace the grounding chains upward through chemistry, biology, psychology, and social facts, showing how each level is grounded in the levels beneath it.

**Fundamentality** is a comparative and absolute concept. Two things can be compared: fundamental particles are more fundamental than molecules; molecules are more fundamental than organisms. But there is also the limiting case: the absolutely fundamental, which is grounded in nothing further. Most metaphysicians assume there is a **bedrock** — that the grounding hierarchy does not go on forever — because an infinite regress of "what grounds what?" would leave everything unexplained. This assumption (that grounding is **well-founded**) is itself contested, but it structures most discussions of what the fundamental level contains.

One useful example is the physical/mental case you may have encountered through truthmakers. The fact that you are in pain seems to hold in virtue of facts about your neural states. The fact that neural states obtain may hold in virtue of facts about molecular chemistry, which hold in virtue of atomic physics, which holds in virtue of quantum field facts. Each level is grounded in the one below. The philosophical question is not just whether this chain exists (most agree it does) but what the relationship at each step looks like — is it full reduction, constitution, realization, or something else? Grounding theory is designed to remain neutral between those options while still capturing the asymmetric, explanatory dependence involved.

The hierarchy picture has significant implications. It tells us that not all facts are equally real or equally basic — there is a genuine structure to reality, and philosophy's job is to map it. It also raises the question of **priority monism** versus **priority pluralism**: does a single ultimate entity (the cosmos as a whole, perhaps) ground everything else? Or are there many fundamental items? And it raises questions about the relationship between grounding and ontology: does everything that is grounded still *exist*, or does being grounded mean being merely derivative — perhaps less than fully real? These questions, which you will pursue further in the metaphysics of structure and architecture, all flow from taking seriously the idea that "in virtue of" relations carve reality at its joints.

