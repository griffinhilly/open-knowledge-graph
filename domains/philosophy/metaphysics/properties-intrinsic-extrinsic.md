---
id: properties-intrinsic-extrinsic
title: Intrinsic and Extrinsic Properties
domain: philosophy
course: metaphysics
prerequisites:
- id: substance-and-property
  type: hard
- id: universals-and-particulars
  type: soft
tags:
- properties
- intrinsic
- extrinsic
- relational
- duplication
stage: formal-systems
status: validated
---

# Intrinsic and Extrinsic Properties

## Core Idea
An intrinsic property is one a thing has purely in virtue of how it itself is, independent of its surroundings — mass, shape, and chemical composition are standard examples. An extrinsic property depends on the thing's relations to other things — being two miles from a barn, being someone's sister, or being famous. The distinction matters because metaphysical principles often turn on it: duplicates share all intrinsic properties; causation is often thought to supervene on intrinsic states; and essentialist claims typically concern intrinsic features. Defining the distinction precisely is harder than it appears — Lewis proposed that intrinsic properties are those shared by all possible duplicates, but this appeals to the notion of duplication, which itself seems to presuppose intrinsicality.

## How It's Best Learned
Read Lewis's 'Extrinsic Properties' and Langton and Lewis's 'Defining "Intrinsic".' Test the proposed definitions against edge cases: is being lonely (being the only object in the world) intrinsic or extrinsic? Is shape intrinsic if space is relational?

## Common Misconceptions
- Intrinsic does not mean essential — a thing can have an intrinsic property contingently (a ball's colour is intrinsic but could have been different).
- Relational properties are not always extrinsic in a trivial sense; some philosophers argue that spatiotemporal properties are both relational and intrinsic to the system.

## Questions

```yaml
- question: "A sculpture is currently the most expensive artwork in the gallery. Is 'being the most expensive artwork in the gallery' an intrinsic or extrinsic property of the sculpture, and why?"
  type: multiple-choice
  options:
    - "Intrinsic — it reflects the artwork's inherent aesthetic quality"
    - "Extrinsic — it depends on the sculpture's relations to other artworks and to buyers' valuations"
    - "Intrinsic — monetary value is a fixed feature of the object itself"
    - "Extrinsic — all economic properties are trivially relational and therefore philosophically unimportant"
  answer: 1
  explanation: "Whether a sculpture is the most expensive artwork in a gallery depends entirely on what other artworks are in the gallery and what valuations people assign them. Remove the other artworks, or change buyers' preferences, and the property disappears — the sculpture itself hasn't changed at all. This is the hallmark of an extrinsic property: it holds in virtue of relations to other things, not in virtue of how the object is internally. A perfect duplicate of the sculpture placed in a different gallery might not be the most expensive artwork there."

- question: "A philosopher argues: 'This ball's color is contingent — it could have been painted differently — so its color cannot be an intrinsic property.' Is this reasoning correct?"
  type: multiple-choice
  options:
    - "Yes — intrinsic properties must also be essential properties that the object has in every possible world"
    - "No — a property can be intrinsic (independent of surroundings) without being essential; the ball's color depends on how it itself is, not on its relations, even if it could have been otherwise"
    - "Yes — contingent properties are by definition relational, since they depend on external causes"
    - "No — color is always extrinsic because it is perceived by external observers"
  answer: 1
  explanation: "Intrinsic and essential are distinct concepts that are frequently conflated. An intrinsic property is one a thing has purely in virtue of how it itself is, independent of its surroundings. An essential property is one a thing has in every possible world where it exists. A ball's color is intrinsic — it doesn't depend on what else exists in the universe — but it is not essential, since the ball could have been painted differently. A thing can have an intrinsic property contingently."

- question: "If two objects are perfect duplicates, they must share all their properties — both intrinsic and extrinsic."
  type: true-false
  answer: false
  explanation: "Lewis's duplication criterion says duplicates share all intrinsic properties — that is precisely what makes them duplicates. But extrinsic properties can differ between duplicates. Two perfect physical copies of the same sculpture can be in different cities (different location), owned by different people (different ownership), and be worth different amounts (different market value). Their internal nature is identical; their relational properties are not. This is why the intrinsic/extrinsic distinction matters: duplicates are identical in their internal natures but can occupy entirely different relational situations."

- question: "A thing's mass is an intrinsic property because it does not change depending on what other objects exist in the thing's surroundings."
  type: true-false
  answer: true
  explanation: "Mass is the standard textbook example of an intrinsic property. A ball has its mass whether it exists alone in the universe or surrounded by other objects. A perfect duplicate of the ball — same internal structure in every respect — must have the same mass. This independence from surroundings is exactly what intrinsicality means. Contrast this with 'being the heaviest object in the room,' which changes depending on what else is in the room."

- question: "State Lewis's duplication criterion for intrinsicality and explain why it faces a circularity problem."
  type: short-answer
  answer: "Lewis defines an intrinsic property as one shared by all perfect duplicates: P is intrinsic if and only if no two duplicates differ with respect to P. Two objects are duplicates if they share all their intrinsic properties. The circularity problem is that duplication is defined in terms of intrinsicality, and intrinsicality is defined in terms of duplication — each concept presupposes the other. You cannot use the criterion to determine which properties are intrinsic without already knowing which properties are intrinsic to specify what makes two objects duplicates."
  explanation: "Langton and Lewis attempted to escape the circularity by defining intrinsicality using 'natural properties' and scenarios involving lonely objects (existing alone) versus accompanied objects (existing alongside others). The circularity problem reveals that the intuitive concept of intrinsicality — what a thing is 'in itself' — is harder to make precise than it first appears."
```

## Explainer

From your study of substance and property, you know that objects are distinguished from one another partly by the properties they instantiate. But not all properties do the same metaphysical work. Some properties characterize an object purely in virtue of what it is in itself — independent of anything else in the world. Others are relational, holding only because the object stands in certain relations to other things. This is the distinction between **intrinsic** and **extrinsic** properties, and it turns up repeatedly in metaphysics wherever we ask what determines an object's nature.

The intuitive cases are clear. A ball's **mass** is intrinsic: it has that mass regardless of what surrounds it. Its **shape** is intrinsic: a spherical ball is spherical whether alone in the universe or surrounded by other objects. By contrast, being "two miles from the Eiffel Tower" is **extrinsic**: this property depends entirely on the ball's spatial relation to a specific external object. Being "the most expensive ball in the room" is extrinsic: it depends on what other balls exist in the room. Being "someone's favorite" is extrinsic: it depends on the psychological states of other people.

The philosophically standard criterion for intrinsicality comes from David Lewis: an intrinsic property is one that is shared by all **duplicates**. Two objects are duplicates if they are alike in all intrinsic properties — perfect copies down to their internal structure. On this account, duplicates must share their shape, mass, and chemical composition, but need not share their location, their relational history, or their social roles. The criterion is powerful but faces a circularity worry: defining intrinsicality via duplication, when duplication itself seems to presuppose intrinsicality. Langton and Lewis attempted a more refined definition using **natural properties** and **lonely/accompanied scenarios** to escape the circle.

The distinction carries genuine metaphysical weight. Many philosophical principles are formulated specifically in terms of intrinsic properties. **Supervenience claims** — that mental properties supervene on physical properties — are typically meant as claims about intrinsic physical states. **Causal powers** are usually held to be intrinsic: what an object can do depends on its own nature, not on its environment. **Essentialism** claims that an object's essential properties are (typically) intrinsic — the properties it has in every possible world where it exists. And Lewis's famous theory of **modality** relies on the idea that possible worlds are like this world, containing concrete objects with intrinsic properties.

One genuinely tricky edge case: is **loneliness** (being the only object in the universe) intrinsic or extrinsic? It seems to depend on what else exists, suggesting extrinsicality. But an object's internal nature doesn't change when you add or remove other objects, suggesting something odd is happening. This case (discussed by Langton and Lewis) reveals that the intrinsic/extrinsic line is not always sharp, and that making it precise requires careful choices about what "internal to the object" really means — a question your work on universals and particulars has equipped you to pursue.
