---
id: constitution-distinct-from-identity
title: Constitution and the Constitution Relation
domain: philosophy
course: metaphysics
prerequisites:
- id: identity-of-indiscernibles
  type: hard
- id: substance-and-property
  type: hard
- id: composition-and-simples
  type: soft
- id: composition-principles-mereology
  type: soft
builds-toward:
- material-constitution-problem
tags:
- constitution
- identity
- composition
- relations
stage: formal-systems
status: validated
---

# Constitution and the Constitution Relation

## Core Idea
Constitution is the relation between an object and the matter that composes it, which is distinct from identity. A statue and the lump of clay that constitutes it share all the same parts at a time, yet they have different identity conditions: the statue ceases to exist when reshaped, but the lump continues. This relation must be carefully distinguished from identity to handle these cases coherently.

## Questions

```yaml
- question: "A sculptor shapes a lump of bronze into a statue. Later, the statue is melted and recast into a different shape. What does the constitution/identity distinction predict?"
  type: multiple-choice
  options:
    - "Both the statue and the bronze lump are destroyed, since they are materially identical"
    - "The bronze lump is destroyed when reshaped; the statue, having no physical form, persists abstractly"
    - "The statue ceases to exist when reshaped, but the bronze lump continues to exist in the new form"
    - "The statue and lump are identical, so whatever happens to one happens to the other"
  answer: 2
  explanation: "The statue and the lump have different persistence conditions: statues are individuated under the sortal 'statue,' which ties their identity to their form; lumps are individuated under 'lump of bronze,' which persists through reshaping. Melting destroys the statue (the form is gone) but the lump simply takes a new shape. Options A and D commit the error of treating constitution as identity — they assume the statue and lump must have the same fate because they share the same matter."

- question: "The argument that a statue and its constituting lump of clay are not identical appeals to Leibniz's Law. What specific property difference does the argument use?"
  type: multiple-choice
  options:
    - "They have different spatial locations at the moment of creation"
    - "They have different masses because the statue includes the sculptor's work"
    - "They have different modal and temporal properties — the statue would not survive reshaping, but the lump would"
    - "They are made of different materials at the microscopic level"
  answer: 2
  explanation: "Leibniz's Law: if x = y, then x and y share all properties. The statue has the property 'would be destroyed if reshaped'; the lump lacks this property (it would survive). This modal difference — a difference in what would happen under counterfactual conditions — is what drives the non-identity argument. Physical properties like mass, location, and composition are shared by the statue and lump at the moment in question, so those cannot do the distinguishing work."

- question: "If the clay lump constitutes the statue, the lump can survive events that destroy the statue."
  type: true-false
  answer: true
  explanation: "This is exactly the force of the constitution-without-identity view. The lump and statue come apart under modal and temporal conditions: squashing the statue destroys it (the form is gone) but the lump persists in the new shape. The lump also pre-existed the statue before the sculptor began work. These asymmetric persistence facts are what show the two are numerically distinct despite complete material overlap at any given moment."

- question: "The constitution relation is symmetric: if A constitutes B, then B also constitutes A."
  type: true-false
  answer: false
  explanation: "Constitution is asymmetric. The lump constitutes the statue — the lump is the underlying material from which the statue is made. The statue does not constitute the lump. This asymmetry mirrors the metaphysical dependency: the statue's existence depends on the lump (or some similar material base), but the lump's existence does not depend on being shaped into a statue. Confusing constitution with identity is partly why students expect symmetry — identity is symmetric (if a = b then b = a), but constitution is not."

- question: "Explain why the constitution relation is described as 'like identity but not identity.'"
  type: short-answer
  answer: "Constitution resembles identity in that the two objects — say, the statue and the lump — completely overlap materially at any given moment: same parts, same location, same intrinsic physical properties. But unlike identity, constitution is not symmetric (lump constitutes statue, not vice versa), not transitive across all cases, and not permanent (the constitution relation can end while both relata persist). Most importantly, the objects differ in modal and temporal properties, which identity forbids: if they were identical, they would have to share every property, but statues and lumps have different persistence conditions under different sortals."
  explanation: "The tension between material overlap (which looks like identity) and modal/temporal divergence (which requires distinctness) is what makes constitution philosophically important. It forces us to recognize that two numerically distinct objects can occupy exactly the same space at the same time — a conclusion that requires sortal-relative identity conditions."
```

## Explainer

From your study of the **identity of indiscernibles**, you know Leibniz's Law: if two things are identical, they share all the same properties. Now consider a sculptor who shapes a lump of clay into a statue of David. When the statue is complete, there appears to be one spatially coincident object — the lump and the statue occupy the exact same location and are made of exactly the same matter. Are they identical? The **constitution relation** is the metaphysician's answer to why the answer is no.

The argument that the statue and the lump are not identical runs through their **modal and temporal properties** — the kind of properties you studied in substance and property theory. The statue would be destroyed if the clay were squashed into a ball; the lump would survive. The lump existed before the statue was sculpted; the statue did not. If identity is symmetric and transitive, two things with different properties cannot be identical. The statue has the property "would cease to exist if reshaped"; the lump lacks this property. By Leibniz's Law, they are not identical. Yet they share all their intrinsic, non-modal, present-tense physical properties. This is the puzzle.

**Constitution** is the relation that holds between the lump and the statue: the lump constitutes the statue without being identical to it. Constitution is like identity in that it requires complete material overlap at a time — the constituting object and the constituted object are co-located and share all their parts. But unlike identity, constitution is not symmetric: the lump constitutes the statue, but the statue does not constitute the lump. And it is not permanent: if the sculptor melts down the statue, the lump no longer constitutes anything, but the lump persists.

The deeper lesson is that **identity conditions** are object-sortal-relative. What makes something the same statue over time is different from what makes something the same lump of clay over time. Statues are typed under the sortal "statue," which brings with it specific persistence and individuation conditions — statues persist through minor repairs but not through fundamental reshaping. Lumps are typed under "lump of clay," which has different persistence conditions. Because objects can be co-located while falling under different sortals with different identity conditions, we can have two numerically distinct objects sharing a single region of space. The constitution relation is precisely what holds between objects in this situation: full material overlap, different identity conditions, different sortal kinds.
