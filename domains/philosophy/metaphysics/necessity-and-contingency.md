---
id: necessity-and-contingency
title: Necessity and Contingency
domain: philosophy
course: metaphysics
prerequisites:
- id: possible-worlds-semantics
  type: hard
- id: modal-realism
  type: soft
- id: modal-logic-intro
  type: soft
tags:
- necessity
- contingency
- Kripke
- a posteriori necessity
- modality
stage: expert
status: validated
---

# Necessity and Contingency

## Core Idea
A proposition is metaphysically necessary if it could not have been false — it holds in every possible world — and contingent if it is true but could have been otherwise. The distinction seems straightforward until Kripke showed that necessity and a priority come apart: 'water is H2O' is necessary (true in all possible worlds) yet knowable only a posteriori (through empirical investigation). This shattered the traditional assumption that necessary truths are always known from the armchair. Kripke also argued for the necessity of origin (this table, if it exists, must have come from this very block of wood) and the necessity of identity (if Hesperus is Phosphorus, it is necessarily so). These results transformed metaphysics by showing that the structure of reality constrains what is possible in ways that outstrip what we can know a priori.

## How It's Best Learned
Read Kripke's Naming and Necessity lectures I and III. Work through the Hesperus/Phosphorus case carefully: why is the identity necessary despite being an empirical discovery? Then compare with Fine's critique in 'Essence and Modality,' which argues that necessity should be grounded in essence, not the other way around.

## Common Misconceptions
- Metaphysical necessity is not the same as logical necessity — some philosophers hold that there are metaphysically necessary truths (like natural kind identities) that are not truths of logic.
- Contingency does not mean randomness; a contingent truth is one that could have been otherwise, not one that happened by chance.

## Questions

```yaml
- question: "Kripke argues that 'water is H₂O' is necessarily true. Which of the following best explains why this identity is necessary rather than contingent?"
  type: multiple-choice
  options:
    - "Scientists confirmed through repeated experiment that water reliably has the composition H₂O, making it a well-established law of nature"
    - "'Water' is a rigid designator — it refers to the same substance (H₂O) in every possible world, so any world containing water contains H₂O, and anything with a different structure simply would not be water"
    - "The molecular structure of water cannot change because chemical bonds are governed by immutable physical laws"
    - "Mathematical truths about molecular bonding make it logically impossible for H₂O to have a different structure"
  answer: 1
  explanation: "Kripke's argument turns on rigid designation. Natural kind terms like 'water' pick out the same substance in every possible world — whatever has the actual molecular structure H₂O. A world with a liquid that looks, tastes, and flows like water but has a different molecular structure would not be a world containing water; it would be a world containing a water-like impostor. Therefore, in every possible world where water exists, it is H₂O. The necessity is metaphysical, not logical or empirical. Crucially, this necessity was discovered empirically (option A describes how it was found, not why it is necessary), which is Kripke's key point: necessary a posteriori."

- question: "Before Kripke, philosophers typically assumed that necessary truths are always knowable a priori. Which pair of examples correctly represents Kripke's challenge to this assumption?"
  type: multiple-choice
  options:
    - "Necessary a priori: 'All bachelors are unmarried.' Necessary a posteriori: 'Water is H₂O.'"
    - "Necessary a priori: 'Water is H₂O.' Contingent a posteriori: 'Hesperus is Phosphorus.'"
    - "Necessary a priori: 'Hesperus is Phosphorus.' Contingent a posteriori: 'All bachelors are unmarried.'"
    - "Necessary a priori: 'Napoleon was exiled to Saint Helena.' Contingent a posteriori: '2 + 2 = 4.'"
  answer: 0
  explanation: "'All bachelors are unmarried' is the paradigm case of necessary a priori: true in all possible worlds and knowable by analysis of the concept alone, without empirical investigation. 'Water is H₂O' is Kripke's paradigm of necessary a posteriori: true in all possible worlds (because 'water' rigidly designates H₂O), but discoverable only through empirical chemistry. The other options scramble these categories. Option B wrongly makes 'water is H₂O' a priori and 'Hesperus is Phosphorus' contingent — both are necessary a posteriori on Kripke's view."

- question: "According to Kripke, the fact that 'Hesperus is Phosphorus' was an empirical astronomical discovery shows that this identity statement is merely contingent — true in the actual world, but false in some possible world."
  type: true-false
  answer: false
  explanation: "False, and this is exactly the confusion Kripke's account of rigid designation resolves. 'Hesperus' and 'Phosphorus' are both proper names that rigidly designate Venus — the very same planet in every possible world where it exists. Once we discover (empirically) that both names pick out the same object, the identity 'Hesperus = Phosphorus' holds necessarily: there is no possible world where Venus is both Hesperus and not Phosphorus. The discovery was empirical (a posteriori), but what was discovered is a necessary truth. Epistemic status (how we came to know it) and modal status (whether it could have been otherwise) are independent dimensions."

- question: "A proposition is contingent if it is true in the actual world but false in at least one other possible world."
  type: true-false
  answer: true
  explanation: "True — this is the standard definition within possible worlds semantics. 'Napoleon was exiled to Saint Helena' is true in the actual world but false in worlds where the Battle of Waterloo ends differently or where Napoleon dies earlier. 'Water is H₂O' is not contingent on Kripke's view, because it is true in every possible world where water exists. The possible-worlds framework makes precise what it means to say something 'could have been otherwise': there exists an accessible world where it is not the case."

- question: "What does it mean for a truth to be 'necessary a posteriori,' and why is this concept philosophically significant? Use 'water is H₂O' as your example."
  type: short-answer
  answer: "A necessary a posteriori truth is one that holds in every possible world (necessary) but can only be known through empirical investigation rather than pure reason (a posteriori). 'Water is H₂O' is necessary because 'water' rigidly designates the substance with that molecular structure — any possible world containing water thereby contains H₂O. But we could not know this from the armchair; it required empirical chemistry to discover. Before the discovery, someone could coherently imagine water turning out to be XYZ rather than H₂O. After the discovery, we know that was impossible. The philosophical significance is that Kripke broke the traditional alignment between necessity and a priority, showing that the structure of reality constrains what is possible in ways that go beyond what we can know by pure reason."
  explanation: "Before Kripke, the dominant view was that the necessary/contingent distinction mapped neatly onto the a priori/a posteriori distinction — necessary truths are known by reason, contingent truths by experience. Kripke showed these are independent dimensions: the modal question (true in all possible worlds?) and the epistemic question (knowable without experience?) come apart. This transformed metaphysics by revealing that empirical science can discover not just what is actually the case, but what must be the case — a much stronger claim than was previously recognized."
```

## Explainer

From your study of possible worlds semantics, you have a precise formal definition to work with: a proposition is **necessarily true** if it is true in every possible world, and **contingently true** if it is true in the actual world but false in at least one other possible world. The proposition "2 + 2 = 4" is true in every world — it could not have been false. The proposition "Napoleon was exiled to Saint Helena" is true in the actual world but false in worlds where the battle of Waterloo goes differently. These seem like clear cases. The interesting philosophy begins when you ask whether the formal distinction maps neatly onto the epistemic distinction between what we can know from the armchair and what we must investigate.

Before Kripke, the dominant view was that the necessary/contingent distinction coincided with the **a priori/a posteriori** distinction. What is necessary, the thought went, is knowable by pure reason; what is contingent must be learned from experience. Kripke's lectures *Naming and Necessity* dismantled this alignment with a series of brilliant examples. The identity "water is H₂O" can only be known through empirical chemistry — it is firmly **a posteriori**. Yet once we know it, we see that it could not have been otherwise. Water just *is* H₂O; a substance with a different molecular structure would not be water, regardless of how much it looked and tasted like the stuff in our rivers. This is a case of **necessary a posteriori** truth — necessary in the modal dimension (true in all possible worlds), yet not knowable from the armchair.

Kripke developed two further examples of necessity that resist a priori access. The **necessity of identity** holds that if two names designate the same thing, the identity is necessary: "Hesperus is Phosphorus" is necessarily true once we discover it is true, because both names rigidly designate Venus — the same object in every world. The **necessity of origin** holds that an object could not have originated from a substantially different origin: this table, if it exists at all, could not have been made from a completely different piece of wood. These claims are metaphysical rather than merely linguistic; they tell us that the structure of reality — not just our concepts — constrains what is possible.

Kit Fine's later work introduces a challenge to this picture. Fine argues that necessity should be grounded in **essence** rather than the other way around. On Kripke's view, Socrates is necessarily not a number because a world where Socrates is a number is too different from the actual world to count as one where Socrates exists. But Fine points out that the number 2 is necessarily not identical to Socrates — yet this seems to have nothing to do with Socrates's essence. Socrates's nature, Fine argues, is what grounds what must be true *of Socrates*, and essence is not reducible to necessity. This refinement does not undermine Kripke's insight that necessity and a priority come apart; it pushes more deeply into what explains modal facts in the first place.

