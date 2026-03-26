---
id: identity-of-indiscernibles
title: Identity of Indiscernibles
domain: philosophy
course: metaphysics
prerequisites:
- id: substance-and-property
  type: hard
- id: universals-and-particulars
  type: hard
- id: first-order-logic-syntax
  type: soft
tags:
- identity
- indiscernibles
- Leibniz
- Black
- individuation
stage: formal-systems
status: validated
---

# Identity of Indiscernibles

## Core Idea
The Identity of Indiscernibles, attributed to Leibniz, states that no two distinct objects can share all their properties — if x and y have exactly the same properties, then x is y. The strong form includes only intrinsic, non-relational properties; the weak form includes relational and extrinsic properties as well. Max Black's famous thought experiment challenges the principle: imagine a universe containing nothing but two qualitatively identical iron spheres, the same in every intrinsic and relational respect. If such a universe is possible, two distinct objects share all properties, and the Identity of Indiscernibles is false. Defenders respond by denying the coherence of the scenario, invoking haecceities (primitive thisness), or arguing that the spheres differ in impure relational properties. The debate bears on whether individuation is grounded in qualities or in something beyond qualities.

## How It's Best Learned
Read Leibniz's Discourse on Metaphysics section 9, then Black's 'The Identity of Indiscernibles' dialogue. Decide whether Black's two-sphere universe is genuinely possible or subtly incoherent, and trace what your answer commits you to about the nature of individuality.

## Common Misconceptions
- The Identity of Indiscernibles is not the same as the Indiscernibility of Identicals (Leibniz's Law), which says identical things share all properties — this latter principle is uncontroversial.
- Rejecting the Identity of Indiscernibles does not require positing mysterious 'bare particulars'; one can hold that distinctness is primitive without invoking a propertyless substratum.

## Questions

```yaml
- question: "A philosopher argues: 'Hesperus and Phosphorus are the same object — the planet Venus. Therefore, whatever properties Hesperus has, Phosphorus has too.' Which Leibnizian principle is being used?"
  type: multiple-choice
  options:
    - "The Identity of Indiscernibles — if they share all properties, they must be identical"
    - "The Indiscernibility of Identicals — if they are numerically identical, they share all properties"
    - "Haecceitism — each object has a primitive thisness that distinguishes it from all others"
    - "The Principle of Sufficient Reason — every fact has an explanation"
  answer: 1
  explanation: "The Indiscernibility of Identicals runs from identity to shared properties: if x = y (they are the same thing), then x and y have all the same properties. This is uncontroversial — how could one thing fail to have its own properties? The Identity of Indiscernibles runs in the opposite direction: if x and y share all properties, then x = y. That is the contentious claim. The Hesperus/Phosphorus case is moving from sameness of object to sameness of properties — that is the Indiscernibility of Identicals, not the Identity of Indiscernibles."

- question: "Max Black imagines a universe containing only two qualitatively identical iron spheres — same size, mass, composition, and even symmetric relational properties. The primary philosophical purpose of this thought experiment is to:"
  type: multiple-choice
  options:
    - "Show that matter can be duplicated exactly without any observable difference between copies"
    - "Challenge the Identity of Indiscernibles by presenting a possible scenario where two numerically distinct objects share all their properties"
    - "Prove that spatial position is a relational property and therefore cannot ground individuation"
    - "Establish that haecceities (primitive thisnesses) are necessary to individuate any object"
  answer: 1
  explanation: "Black's thought experiment is a counterexample to the Identity of Indiscernibles. If the two-sphere universe is genuinely possible, then two numerically distinct objects (the two spheres) share every property — intrinsic and, by the symmetry of the universe, even relational ones. That would falsify the principle. Option D gets cause and effect backwards: haecceitism is a *response* to Black's challenge, one way of defending the Identity of Indiscernibles against it. The thought experiment motivates haecceitism; it does not establish it."

- question: "The Identity of Indiscernibles and the Indiscernibility of Identicals are two names for the same principle — both say that identical objects share most their properties."
  type: true-false
  answer: false
  explanation: "These are two distinct principles that run in opposite directions. The Indiscernibility of Identicals says: if x and y are identical (the same object), then they share all properties. This is uncontroversial. The Identity of Indiscernibles says: if x and y share all properties, then they are identical (numerically one thing). This is the contentious claim that Black's two-sphere argument attacks. Confusing them is the most common error in this topic — the principles have the same logical form but different premises and conclusions."

- question: "One can reject the Identity of Indiscernibles — accepting that two numerically distinct objects could share all their qualitative properties — without thereby committing to the existence of 'bare particulars' (propertyless substrata)."
  type: true-false
  answer: true
  explanation: "Rejecting the Identity of Indiscernibles means holding that numerical distinctness is not fully grounded in qualitative differences. One way to do this is to posit bare particulars — substrata that are distinct but have no properties of their own. But another way is to treat numerical distinctness as simply a primitive, brute fact about the world's structure: the two spheres are two, full stop, and this distinctness is not reducible to any further property. This position is coherent and does not require bare particulars."

- question: "What is the key difference between the 'weak' and 'strong' forms of the Identity of Indiscernibles, and why does that distinction matter for evaluating Black's two-sphere thought experiment?"
  type: short-answer
  answer: "The weak form includes relational and positional properties — under it, two objects can always be distinguished by their different spatial positions. The strong form restricts to intrinsic, non-relational properties only. Black's argument targets the strong form: in his symmetric two-sphere universe, every relational property of each sphere is matched by the other (each is two meters from a sphere of the same kind), so spatial position cannot distinguish them. The weak form can survive Black's challenge; the strong form cannot, unless one accepts haecceities or denies the scenario's possibility."
  explanation: "The distinction matters because the Identity of Indiscernibles has very different standing depending on which version you're considering. The weak form is arguably trivially true — two objects that occupy different spatial positions can always be distinguished by their position. The philosophically interesting and contested claim is the strong form, which says that qualitative intrinsic properties alone must individuate objects. Black constructs a case where no intrinsic property differs between the two spheres, which is why the strong form is vulnerable and the weak form is not."
```

## Explainer

You already understand the distinction between **universals** (properties and relations that can be shared by many particulars) and **particulars** (individual things). You also understand the substance/property structure: a substance is an individual that instantiates properties, but is not itself a property. This background sets up the Identity of Indiscernibles perfectly — it is a thesis about what makes *individuals* numerically distinct from one another.

There are two Leibnizian principles that are constantly confused. **Leibniz's Law** (the *Indiscernibility of Identicals*) says: if x and y are *identical* (numerically one thing), then they share all their properties. This is uncontroversial — how could one thing fail to have the very properties it has? The **Identity of Indiscernibles** runs in the opposite direction: if x and y share *all* their properties, then they are identical. This is the contentious claim. It says that qualitative sameness entails numerical sameness — that two distinct things must differ in at least one property. Formally, there can be no two distinct objects that are qualitatively perfect duplicates of each other.

The strength of the principle depends on which properties you include. The **weak form** counts relational and positional properties: two objects can be distinguished by their different spatial positions ("the sphere at coordinates A" vs. "the sphere at coordinates B"). The **strong form** restricts to intrinsic, non-relational properties only — and this is the version Max Black attacks. His thought experiment: imagine a symmetric universe containing only two qualitatively identical iron spheres, separated by some distance. Everything true of one sphere is true of the other: same radius, same mass, same composition. Even their relational properties seem symmetric — each is two meters from a sphere of the same kind. If this universe is coherent, two numerically distinct objects share every property, and the Identity of Indiscernibles (in the strong form) is false.

**Haecceitism** is one line of response: each object has a *primitive thisness* (haecceity) — a property of being *this very thing* — that is not reducible to any qualitative property. Sphere A has the property "being A" that Sphere B lacks. This preserves the Identity of Indiscernibles but at a cost: you must accept non-qualitative, purely identifying properties into your ontology. Critics find this unintelligible or viciously circular. An alternative response is to deny that Black's universe is genuinely conceivable — perhaps the description is subtly inconsistent. Another is to simply accept the conclusion: numerical distinctness is primitive and irreducible to any property, qualitative or otherwise. This position rejects the Identity of Indiscernibles without requiring bare particulars, treating individuality as a brute fact about the world's structure.
