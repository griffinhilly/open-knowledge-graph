---
id: material-constitution-problem
title: Material Constitution and the Lump-Statue Problem
domain: philosophy
course: metaphysics
prerequisites:
- id: constitution-distinct-from-identity
  type: hard
- id: composition-principles-mereology
  type: hard
- id: identity-of-indiscernibles
  type: soft
builds-toward:
- sortal-identity-conditions
tags:
- constitution
- identity
- composition
- material
- metaphysics
stage: formal-systems
status: validated
---

# Material Constitution and the Lump-Statue Problem

## Core Idea
A bronze lump exactly constitutes a statue at a time with all the same parts and location, yet they differ in identity conditions—the statue ceases to exist if melted down but the lump continues. This pressures theories of identity and composition, forcing choice between denying that constitution and identity differ, or explaining why they come apart.

## Questions

```yaml
- question: "A sculptor melts down a statue of Hermes. The bronze lump continues to exist; the statue ceases to exist. What does this show about the lump and the statue before the melting?"
  type: multiple-choice
  options:
    - "Nothing special — all objects cease to exist when sufficiently transformed"
    - "The lump and the statue were never made of the same matter"
    - "They were not strictly identical objects, since they have different persistence conditions — objects with different properties cannot be the same object (by Leibniz's law)"
    - "The statue was a part of the lump, not a distinct object coincident with it"
  answer: 2
  explanation: "If the lump and the statue were strictly identical, they would share all properties — including their persistence conditions. But they don't: the statue has the property 'would cease to exist if melted down' while the lump lacks it. By the indiscernibility of identicals (Leibniz's law in reverse), if they differ in any property, they are not identical. The melting scenario makes this vivid: their fates come apart, proving they were two distinct objects even when they shared all their matter and spatial location."

- question: "Leibniz's Law is relevant to the material constitution problem because:"
  type: multiple-choice
  options:
    - "It proves that two objects in the same location must be identical"
    - "It states that if two objects share all properties, they are identical — so if the lump and statue differ in any property (like persistence conditions), they cannot be the same object"
    - "It establishes that statues and lumps belong to different ontological categories and cannot be compared"
    - "It shows that modal properties like 'would survive melting' are not genuine properties and don't affect identity"
  answer: 1
  explanation: "Leibniz's Law (the indiscernibility of identicals) states: if A = B, then A and B share all properties. Contraposing: if A and B differ in any property, then A ≠ B. The statue has the modal property 'would cease to exist if melted down'; the lump lacks this property (it would survive). This property difference, if genuine, entails they are not identical. Defenders of strict identity must argue that modal and sortal properties like these are not genuine first-class properties — which requires a substantive metaphysical commitment."

- question: "The material constitution problem applies only to artifacts like statues; organisms and persons do not face analogous puzzles about the relationship between an entity and the matter constituting it."
  type: true-false
  answer: false
  explanation: "The puzzle generalizes far beyond artifacts. Organisms and the masses of cells composing them, rivers and the water molecules constituting them, persons and the bodies constituting them — all face analogous questions. A person might survive the loss of a limb (their body changes but they persist), while the original mass of matter no longer exists as a unified whole. The statue case is philosophically vivid because persistence conditions can be stipulated clearly, but the underlying issue — the relationship between material composition and object identity — appears throughout philosophy of mind, personal identity, and natural kinds."

- question: "If a bronze lump and a bronze statue occupy exactly the same spatial region at the same time and share all their physical parts, they must be numerically identical objects."
  type: true-false
  answer: false
  explanation: "This is precisely what the material constitution problem challenges. The intuition that two material objects cannot fully occupy the same location (the 'impenetrability' intuition) supports the conclusion that coincident objects must be identical. But the lump and statue can have different persistence conditions even while sharing all physical parts and spatial location — which means they cannot be strictly identical. The problem forces a choice: deny that persistence conditions are genuine distinguishing properties, accept coincident distinct objects, or adopt an alternative metaphysical framework (temporal parts, sortal-relative identity, or eliminativism)."

- question: "What is the 'problem of coincident objects,' and why does it arise from the lump-statue case?"
  type: short-answer
  answer: "The problem of coincident objects is that the lump and the statue appear to be two numerically distinct objects (because they have different persistence conditions) that nonetheless fully occupy the same spatial region at the same time and share all their matter. This violates the widespread intuition that space does not allow two material objects to coincide completely — that location is sufficient to individuate material objects. The lump-statue case generates this problem because it shows two objects that are materially indistinguishable at a moment yet differ in their modal properties (what they can survive)."
  explanation: "The problem has bite because both horns are uncomfortable. Accepting coincident objects means revising our intuition about spatial individuation. Denying them means either claiming the lump and statue are identical (hard to square with their different fates) or eliminating one of them from the ontology (either denying statues exist as genuine objects, or treating the lump-talk as fiction). Each major response — temporal parts, sortal-relative identity, eliminativism — involves a substantive philosophical cost. This is what makes material constitution one of the most actively debated problems in contemporary metaphysics."
```

## Explainer

Your prerequisites have given you two key tools. From the study of constitution versus identity, you know that two things can be constitutionally related — made of exactly the same matter, occupying the same space — without being identical. From mereology and composition principles, you know the questions around what makes parts compose a whole, and under what conditions two collections of parts constitute one object versus two. The **material constitution problem** is where these threads collide most dramatically.

Imagine a sculptor who shapes a lump of bronze into a statue of Hermes. At time T, the bronze lump and the statue share all their matter, every particle, and occupy exactly the same region of space. And yet — here is the puzzle — they appear to be two distinct objects with different **persistence conditions**. Melt the statue down, and the statue ceases to exist; the bronze lump continues. Chip a fragment off the statue, and the statue may survive but the original lump is gone — replaced by a smaller lump. Their fates can come apart even when they share all the same matter, which means they cannot be strictly identical. If the lump and the statue were the same object, they would have to share all their properties — including their persistence conditions — and they do not.

This creates what philosophers call the **problem of coincident objects**: two numerically distinct objects occupying the same region at the same time. This violates a widespread intuition — that space does not allow two material objects to fully occupy the same location simultaneously. We need to choose between abandoning that intuition or finding some way to explain why the lump and the statue do not really coincide. The major responses divide into three families. **Temporal parts theories** hold that objects are four-dimensional entities extended through time; the lump and the statue share spatial parts but differ in their temporal parts, so they do not fully coincide. **Sortal-relative identity theories** hold that identity is always identity relative to a sortal concept (statue, lump, organism), so asking whether the lump is the statue simpliciter is a category error. **Eliminativist views** deny that there is a statue over and above the lump — ordinary object talk about statues is a useful fiction grounded in lump-facts.

The identity-of-indiscernibles principle you encountered in prerequisites is directly relevant here. Leibniz's principle states that if A and B share all their properties, then A = B. If the lump and statue share all properties, they must be identical. But they seem to differ — at minimum, the statue has the property "would cease to exist if melted down" while the lump lacks it. If these are genuine properties, the indiscernibility of identicals (the reverse of Leibniz's law) entails they are not identical. Defenders of strict identity must argue that modal and sortal properties like "would survive melting" are not genuine first-class properties that individuate objects — which requires a substantive and contested metaphysical commitment.

The puzzle generalizes far beyond bronze statues. Organisms and the masses of cells that compose them, rivers and the water molecules that constitute them, persons and the bodies that constitute them — all face analogous questions. The statue case is philosophically vivid because we can stipulate exactly when the statue comes into existence and goes out of existence, making the identity conditions maximally concrete. But the underlying issue — the relationship between material composition and object identity — is one of the deepest and most unresolved problems in contemporary metaphysics.
