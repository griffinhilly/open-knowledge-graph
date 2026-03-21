---
id: universals-nominalism-realism
title: 'Universals: Nominalism and Realism'
domain: philosophy
course: metaphysics
prerequisites:
- id: universals-and-particulars
  type: hard
- id: trope-theory
  type: soft
- id: abstract-entities-platonism
  type: soft
builds-toward:
- categorical-dispositions-distinction
- fundamental-properties-sparse-abundant
tags:
- universals
- nominalism
- realism
- properties
- ontology
stage: formal-systems
status: draft
---

# Universals: Nominalism and Realism

## Core Idea
The problem of universals asks what accounts for objective similarities among particulars. Realism holds that universals (abstract properties shared by many particulars) are real entities that exist in each instance. Nominalism denies universals, explaining similarity through resemblance classes or class membership. This problem remains central because the answer shapes ontology and the theory of properties.

## Questions

```yaml
- question: "Two fire trucks and an apple are all red. A realist and a resemblance nominalist are asked what makes these three things share the property of redness. Which pair of answers best captures their positions?"
  type: multiple-choice
  options:
    - "Realist: 'They all cause the same experience in normal perceivers.' Nominalist: 'They all reflect the same wavelengths of light.'"
    - "Realist: 'There is a single entity, redness, wholly present in each of them.' Nominalist: 'They sufficiently resemble each other and the paradigm cases of red things.'"
    - "Realist: 'They belong to the same natural kind.' Nominalist: 'They are classified together by our linguistic conventions.'"
    - "Realist: 'Redness is a concept in our minds that we apply to them.' Nominalist: 'They each have their own individual redness that is distinct from the others.'"
  answer: 1
  explanation: "Realism holds that universals are real entities wholly present in each instance — the single property redness literally exists in each red thing. Resemblance nominalism denies this, instead explaining similarity through resemblance: two things are red because they sufficiently resemble each other and paradigm red objects, without any shared universal. Option D partially describes trope theory (individual property instances) and a form of conceptualism (redness as a mental concept), neither of which captures the standard realist-nominalist divide."

- question: "Resemblance nominalism faces a circularity objection. Which formulation best captures the problem?"
  type: multiple-choice
  options:
    - "It cannot explain how we learn color terms as children"
    - "To say two things resemble each other is to say they share a property — which smuggles a universal back in through the back door"
    - "It requires an infinite regress of resemblance relations"
    - "Resemblance is itself a universal that must be explained, causing the nominalist's position to be self-refuting"
  answer: 1
  explanation: "The Explainer states this directly: 'What grounds the resemblance relation? If we say two red things resemble each other, are we smuggling in a shared property through the back door?' When you say two things 'sufficiently resemble each other with respect to color,' you seem to already be invoking a shared color property — the very universal the nominalist was trying to eliminate. Option D (the resemblance-universal regress) is related and sometimes cited, but the core objection is the one in option B: explaining similarity through resemblance seems to presuppose similarity."

- question: "Aristotelian realism holds that universals like redness exist even if nothing in the world is currently red."
  type: true-false
  answer: false
  explanation: "This describes Platonic realism, not Aristotelian realism. The Explainer distinguishes them explicitly: 'Platonic realism places universals in a realm of abstract objects that exist independently of any particular instance; redness exists whether or not anything is currently red. A more moderate Aristotelian realism holds that universals are real but only ever exist instantiated in particulars — redness exists only insofar as there are red things.' The contrast between these two forms of realism is itself an important internal divide within the realist camp."

- question: "Trope theory avoids both Platonic abstract universals and the circularity objections facing resemblance nominalism."
  type: true-false
  answer: true
  explanation: "Tropes are particular instances of properties: the redness of this apple is a distinct entity from the redness of that fire truck, even if they resemble each other. This avoids Platonic universals (there is no single abstract redness existing apart from instances) while also giving properties genuine ontological status — unlike class nominalism, which identifies properties with sets. Resemblance nominalism still needs to explain what grounds the resemblance between tropes, but trope theory at least avoids positing a shared universal while still individuating properties."

- question: "What is the core problem that the debate between realism and nominalism is trying to solve, and why does it matter beyond abstract metaphysics?"
  type: short-answer
  answer: "The core problem is explaining what grounds objective similarity among particulars — what makes two red things both genuinely red, rather than merely called red by convention. This matters beyond abstract metaphysics because the answer shapes the theory of natural laws (do laws hold because universals necessitate causal relations?), the status of mathematical objects (are numbers universals?), and the metaphysics of science (what makes something a natural kind rather than an arbitrary grouping?). Choosing between nominalism and realism is one of the first and most consequential decisions in constructing an ontology."
  explanation: "The problem of universals is not just a puzzle about language or classification — it has downstream consequences for whether we think the world has objective structure independent of our categories. A realist can say that natural kinds like 'water' or 'electron' carve nature at its joints because the relevant universals are really there; a nominalist must find another way to distinguish natural kinds from arbitrary groupings. This is why the debate, despite seeming abstract, remains central to philosophy of science and metaphysics."
```

## Explainer

From your study of universals and particulars, you understand the basic distinction: a **particular** is a concrete individual thing (this red apple, that red fire truck), while a **universal** would be the redness they share. The problem of universals asks: what exactly is being shared? Is there a real entity — redness itself — that is literally present in every red thing, or is the similarity among red things explained some other way?

**Realism** holds that universals are genuine entities. When two objects are both red, there is a single property, redness, that is wholly present in each. This explains similarity by positing a common constituent. The most radical version — **Platonic realism** — places universals in a realm of abstract objects that exist independently of any particular instance; redness exists whether or not anything is currently red. A more moderate **Aristotelian realism** holds that universals are real but only ever exist instantiated in particulars — redness exists only insofar as there are red things. Both versions face the challenge of explaining how an abstract or multiply-located entity can causally interact with the physical world, and how we come to have knowledge of it.

**Nominalism** denies that universals exist and tries to explain the appearance of shared properties without them. **Class nominalism** identifies properties with sets: being red just means being a member of the class of red things. **Resemblance nominalism** says that what makes two things red is that they sufficiently resemble each other and the paradigm cases of red things. The challenge for all nominalisms is to explain objective similarity without invoking the very universals they're trying to eliminate. What grounds the resemblance relation? If we say two red things resemble each other, are we smuggling in a shared property through the back door?

Your study of **trope theory** offers a third path: tropes are particular instances of properties — the redness of *this apple* is a distinct entity from the redness of *that truck*, even though they resemble each other. Trope theory avoids Platonic abstract universals while still giving properties ontological status. The debate between these positions isn't merely terminological. It shapes questions about natural laws (do laws hold because properties are universals that necessitate causal relations?), mathematics (are numbers universals?), and the metaphysics of science (what are natural kinds?). Choosing between nominalism and realism is one of the first and most consequential decisions in constructing an ontology.
