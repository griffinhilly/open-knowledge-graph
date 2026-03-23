---
id: natural-kinds-and-essence
title: Natural Kind Terms and Essential Properties
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: putnam-semantic-externalism
  type: hard
- id: kripke-causal-theory-naming
  type: hard
- id: first-order-logic-syntax
  type: soft
builds-toward:
- empty-names-fictional
tags:
- natural-kinds
- essence
- reference
stage: formal-systems
status: validated
---

# Natural Kind Terms and Essential Properties

## Core Idea
Natural kind terms like 'water,' 'gold,' and 'tiger' refer to categories defined by underlying properties rather than apparent properties. The meaning and reference of natural kind terms depends on scientific discoveries about the kinds' essences, not on stereotype or appearance.

## Questions

```yaml
- question: "Before the discovery of chemistry, people used 'water' to refer to the clear, drinkable liquid in rivers and rain. According to Kripke and Putnam, did they mean the same thing by 'water' as we do today?"
  type: multiple-choice
  options:
    - "No — they associated 'water' with the description 'clear drinkable liquid,' so their word picked out a different concept"
    - "Yes — 'water' referred to H₂O even then, because reference is fixed by the underlying nature of the kind, not by speakers' descriptions"
    - "Partially — they meant the behavioral and phenomenal properties, while we additionally know the chemical composition"
    - "Yes — but only because water and H₂O happen to be co-extensive in our world"
  answer: 1
  explanation: "Reference is fixed at the initial dubbing by whatever natural kind is instantiated, not by the description in speakers' heads. Pre-chemistry speakers pointed at H₂O when they said 'water,' so their term referred to H₂O even though they didn't know its chemical structure. This is Putnam's insight that meaning 'ain't in the head' — what counts is the actual nature of the thing referred to, not the internal mental state of the user. Option A describes the description theory that Kripke and Putnam are rejecting."

- question: "On Twin Earth, XYZ fills lakes and taps — chemically different from H₂O but macroscopically indistinguishable. Twin Earthers use 'water' just as we do. According to Putnam, what is the relationship between their word and ours?"
  type: multiple-choice
  options:
    - "They mean the same as us, since they have identical perceptual experiences with the substance"
    - "Their 'water' and our 'water' have the same sense but different reference — the words are synonymous"
    - "Their 'water' refers to XYZ; our 'water' refers to H₂O — the terms pick out different natural kinds despite identical surface usage"
    - "They mean the same as us, since meaning is determined by functional role and behavior, not chemical composition"
  answer: 2
  explanation: "This is the Twin Earth thought experiment's conclusion: reference tracks the underlying nature, not the internal mental life or functional role. Although Twin Earthers' use of 'water' is behaviorally indistinguishable from ours, their term refers to XYZ and ours refers to H₂O — two different natural kinds. Options A and D represent exactly the internalist/functionalist picture that Putnam's externalism is designed to refute."

- question: "'Water is H₂O' is a necessary truth — true in every possible world — even though it was discovered through empirical investigation rather than conceptual analysis."
  type: true-false
  answer: true
  explanation: "This is the central example of an a posteriori necessity. 'Water' rigidly designates the natural kind whose essence is H₂O — in any possible world, water is H₂O. But we could only know this through chemistry. Kripke's key contribution is separating necessity (a metaphysical category: true in all possible worlds) from a priority (an epistemic category: knowable without experience). These can come apart, and natural kind terms are the primary source of a posteriori necessities."

- question: "Natural kind terms like 'water' refer to what ordinary speakers stereotypically describe — the typical color, taste, and behavior — since these observable properties are what fix the reference of the term."
  type: true-false
  answer: false
  explanation: "This is the description theory, which Kripke and Putnam explicitly reject. Reference is fixed by the actual underlying nature of the kind, discovered through an initial dubbing and scientific investigation. Speakers can use 'water' correctly without knowing it is H₂O — and being told 'water is H₂O' is genuinely informative rather than a mere definition. If stereotypical properties fixed reference, 'water is H₂O' would be a contingent discovery rather than a necessary truth."

- question: "What is an 'a posteriori necessity,' and why does the natural kinds framework generate them?"
  type: short-answer
  answer: "An a posteriori necessity is a statement that is true in all possible worlds (necessary) but can only be known through empirical investigation (a posteriori). Natural kind terms generate them because they rigidly designate kinds by their underlying essence. 'Water' picks out H₂O in every possible world, so 'water is H₂O' is metaphysically necessary — but only chemistry could reveal this, making it epistemically a posteriori."
  explanation: "The classical assumption — that necessity and a priority coincide — breaks down for natural kind terms. The statement 'all bachelors are unmarried' is both necessary and a priori (knowable by definition). 'Water is H₂O' is necessary (water couldn't be anything else in any possible world) but a posteriori (we needed science to find out). This distinction reshapes both philosophy of language and metaphysics by showing that essences are discovered, not stipulated."
```

## Explainer

From your study of Putnam's semantic externalism you know that meaning "ain't in the head" — what our words refer to is determined partly by facts about the world and our environment, not purely by our internal mental states or descriptions. From your study of Kripke's causal theory of naming you know that proper names are **rigid designators**: they pick out the same individual across all possible worlds, with reference fixed by an initial dubbing and transmitted through a causal-historical chain. **Natural kind terms** extend this apparatus from individuals to kinds. When your ancestors first pointed at water and said "water," they fixed the reference of that term not to a description (the clear, drinkable liquid) but to whatever natural kind instantiated the stuff in front of them — which turned out to be H₂O.

The key consequence is that **essential properties** of natural kinds are discovered, not stipulated. Before chemistry, no one knew that water was H₂O. But H₂O is not merely how we recognize water — it is what water fundamentally is. In every possible world where something is water, it is H₂O. A possible world with XYZ (another substance, structurally different) filling the lakes and running from taps would have something that looks and behaves like water but is not water. This is Putnam's Twin Earth thought experiment: the inhabitants of Twin Earth who use "water" to refer to XYZ are talking about a different substance, even though their inner lives — perceptions, beliefs, descriptions — are indistinguishable from ours. Reference tracks the underlying nature; the rest is stereotype.

This means natural kind terms support a distinctive kind of modal claim: **a posteriori necessities**. "Water is H₂O" is necessary — true in every possible world — but it was only discovered through empirical investigation, not through conceptual analysis. Similarly, "Gold has atomic number 79" is not a definition that exhausts what we mean by "gold"; it is a scientific discovery that reveals gold's essence. Once discovered, the identity holds necessarily. Compare this with a description theory of meaning, on which "water" means "the clear, drinkable liquid" — then "Water is H₂O" would be contingent (there could have been worlds with clear, drinkable XYZ), and the term would shift reference in different possible worlds. Kripke and Putnam argue the description theory gets this wrong.

The scope extends beyond chemistry. **Biological kinds** like "tiger" and "human" are natural kinds whose essential properties are determined by biology — genetic structure, evolutionary lineage, developmental biology — not by the appearance or behavioral stereotype we use to identify them. A **natural kind** in this sense is any category that "carves nature at its joints": a real division in the world that supports inductive inference, causal explanation, and scientific law. Not every grammatically natural predicate picks out a natural kind — "jade," as noted, picks out two different minerals with similar appearances; "is an electron" plausibly does pick out a natural kind. Distinguishing natural kinds from mere categories or artificial kinds, and understanding what makes a property essential to a kind rather than merely typical of it, sits at the intersection of philosophy of language, metaphysics, and philosophy of science.
