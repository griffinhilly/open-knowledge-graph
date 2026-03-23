---
id: rigid-designators-modal-reference
title: Rigid Designators and Necessary Reference
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: kripke-causal-theory-naming
  type: hard
- id: modal-logic-intro
  type: soft
builds-toward:
- proper-names-and-reference
tags:
- rigid-designators
- Kripke
- names
- possible-worlds
- modal
stage: formal-systems
status: validated
---

# Rigid Designators and Necessary Reference

## Core Idea
Kripke introduced the concept of rigid designators—terms that refer to the same object in all possible worlds in which that object exists. Proper names are typically rigid; they pick out an individual essentially. Definite descriptions are usually non-rigid: 'the tallest person' designates different individuals in different possible worlds. This distinction has profound implications: statements like 'Hesperus could have not existed' become necessary truths, not contingent discoveries.

## How It's Best Learned
Study the Hesperus/Phosphorus example: both are names of Venus, so the identity 'Hesperus = Phosphorus' is necessary (true in all possible worlds), not contingent. Compare with non-rigid descriptions.

## Common Misconceptions
Rigid designators must pick out the same thing in all worlds—they only need to pick out the same thing in worlds where they pick out anything. Necessity must be knowable a priori—Kripke's distinction between metaphysical necessity and epistemic necessity allows necessary truths to be discovered empirically.

## Questions

```yaml
- question: "Ancient astronomers discovered that 'Hesperus' (the evening star) and 'Phosphorus' (the morning star) both refer to Venus. Given that both names are rigid designators, what is the modal status of the statement 'Hesperus is Phosphorus'?"
  type: multiple-choice
  options:
    - "Contingently true — it could have turned out otherwise under different astronomical conditions"
    - "Necessarily true — since both names rigidly pick out Venus in every possible world, there is no possible world where Hesperus exists and Phosphorus exists but they are distinct"
    - "Necessarily false — a priori reasoning shows that evening and morning appearances are different objects"
    - "Neither necessary nor contingent — modal logic does not apply to empirical identity statements"
  answer: 1
  explanation: "Because 'Hesperus' and 'Phosphorus' are rigid designators — each picks out Venus in every world where Venus exists — the identity statement 'Hesperus is Phosphorus' is necessarily true if true at all. There is no possible world where both names refer to different objects. This is Kripke's key result: the identity is metaphysically necessary even though it was an empirical discovery requiring astronomical observation. The tempting wrong answer (contingently true) conflates metaphysical necessity with epistemic a priority."

- question: "In possible world W, the person who actually invented bifocals (Benjamin Franklin) became a farmer and never invented anything. What does the definite description 'the inventor of bifocals' refer to in world W?"
  type: multiple-choice
  options:
    - "Benjamin Franklin — because he is the inventor of bifocals in the actual world"
    - "No one — if Franklin never invented bifocals, there may be no inventor of bifocals in W"
    - "Whoever invented bifocals in world W, which may be a different person or no one"
    - "The description is rigid, so it still refers to Franklin in W"
  answer: 2
  explanation: "Definite descriptions are non-rigid: 'the inventor of bifocals' picks out whoever satisfies that description in each world, not Franklin across all worlds. In a world where Franklin never invented bifocals, 'the inventor of bifocals' may refer to someone else or to no one. This contrasts with the name 'Benjamin Franklin,' which rigidly picks out that same individual in every world where he exists, regardless of what he did or didn't do."

- question: "Since 'water is H₂O' is a necessary truth on Kripke's account, a sufficiently skilled chemist could have known it through a priori reasoning alone, without any empirical investigation."
  type: true-false
  answer: false
  explanation: "This is the confusion Kripke explicitly dismantles. 'Water is H₂O' is metaphysically necessary — there is no possible world where water is not H₂O — but it is not knowable a priori. It required empirical chemistry to discover that the substance we call 'water' has the molecular structure H₂O. Kripke's central contribution is separating metaphysical necessity from epistemic a priority: necessary truths can be empirical discoveries, and a priori truths can be contingent. The two categories do not coincide."

- question: "A definite description like 'the tallest person alive in 2025' is a non-rigid designator because it could pick out different individuals in different possible worlds."
  type: true-false
  answer: true
  explanation: "Definite descriptions are paradigm non-rigid designators: they pick out whoever or whatever satisfies their descriptive content in a given world, not a fixed individual across worlds. In the actual world, 'the tallest person alive in 2025' refers to whoever is tallest; in a possible world with a different population and growth patterns, it refers to a different person. This contrasts with a proper name like 'Elon Musk,' which picks out that specific individual in every world where he exists, regardless of whether he is tallest."

- question: "Why does the rigidity of proper names imply that true identity statements between two names are necessarily true, rather than merely contingently true?"
  type: short-answer
  answer: "If both 'A' and 'B' are rigid designators and 'A is B' is true, then both names pick out the same object in the actual world. Since they are rigid, each name picks out that same object in every possible world where it exists. Therefore there is no possible world in which A exists and B exists but they are distinct things — the identity holds across all worlds. Necessity follows directly from rigidity: rigid co-reference means the identity cannot fail in any possible world."
  explanation: "The contrast with descriptions makes this clear. 'The morning star is the evening star' could have been false — those descriptions could have picked out different objects. But 'Hesperus is Phosphorus' cannot be false in any world where both referents exist, because both names track Venus rigidly. The metaphysical necessity is a consequence of the names' semantic behavior, not of any contingent astronomical facts."
```

## Explainer

From your study of Kripke's causal theory of naming, you know that proper names get their reference not through associated descriptions (as Frege and Russell thought) but through a causal-historical chain connecting the name back to an initial baptism event. "Aristotle" refers to a particular person not because competent speakers associate the name with "the teacher of Alexander" or "the author of the Nicomachean Ethics," but because their use of the name connects back, through a chain of transmission, to the original introduction of that name to that person. This causal account tells you *how* names refer. Rigid designation tells you *what* that reference consists in across possible worlds.

A **rigid designator** is a term that picks out the same object in every possible world in which that object exists. Proper names, on Kripke's view, are the paradigm case. "Aristotle" refers to Aristotle in the actual world; it also refers to Aristotle in the possible world where he became a farmer instead of a philosopher, and in the world where he died in infancy. In every world where Aristotle exists at all, the name "Aristotle" tracks *him*. **Non-rigid designators** contrast sharply. The definite description "the teacher of Alexander" picks out whoever happens to fill that role in a given world — in the actual world, Aristotle; in a world where Aristotle was never hired, perhaps someone else entirely. Same words, different referents in different possible worlds.

This distinction has a striking consequence for modal statements. If both "Hesperus" and "Phosphorus" are rigid names — both referring to Venus in every world — then "Hesperus is Phosphorus" expresses a **necessary identity**. The names co-refer in every possible world. There is no world where Hesperus exists and Phosphorus exists but they are different things. The identity is necessary even though it was an empirical astronomical discovery. This is Kripke's key result: **necessity and a priority come apart**. The statement "Hesperus is Phosphorus" is metaphysically necessary but not knowable a priori — it required telescope and observation to establish. The pre-Kripkean assumption that all necessary truths are knowable from the armchair was false.

The same logic extends to **natural kind terms** — words like "water," "gold," and "tiger." These terms, Kripke argued (along with Hilary Putnam), refer rigidly to their underlying essential nature: "water" refers to H₂O in every possible world. A substance that appeared exactly like water but had a different molecular structure would not be water — it would be something else, regardless of how it looked and tasted. This is why "water is H₂O" is necessarily true once discovered, not merely contingently true as a definition. Together, rigid designation and natural kind reference transform how we understand the relationship between language, modal reality, and scientific discovery: names and kind terms hook directly onto the world, and the necessities they reveal are in the world, not just in our concepts.

