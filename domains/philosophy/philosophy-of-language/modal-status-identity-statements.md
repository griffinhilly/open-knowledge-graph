---
id: modal-status-identity-statements
title: The Modal Status of Identity Statements
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: kripke-causal-theory-naming
  type: hard
- id: necessity-and-contingency
  type: hard
- id: possible-worlds-semantics
  type: soft
builds-toward:
- two-dimensional-semantics
tags:
- necessity
- identity
- modality
- a-posteriori
stage: formal-systems
status: draft
---

# The Modal Status of Identity Statements

## Core Idea
Why is "H2O = water" necessarily true while "water is transparent" is contingent? Kripke argued that identity statements between rigid designators are necessarily true if true at all, even when known a posteriori. This explains how empirical discoveries can establish necessities, revolutionizing philosophy's relationship to science and modal logic.

## How It's Best Learned
Begin with Kripke's distinction between epistemic and metaphysical necessity. "Water = H2O" is metaphysically necessary (true in all possible worlds) but epistemically contingent (we had to discover it empirically). Show why descriptivism makes this impossible: if "water" means "the clear liquid from lakes," then it could be false that water is clear. Work through Kripke's arguments that names are rigid designators and identity statements between rigid designators are always necessary.

## Common Misconceptions
- Thinking Kripke's view makes all necessary truths a posteriori; he only claims *some* a posteriori truths are necessary.
- Assuming rigid designation implies names have no descriptive content; reference-fixing can be descriptive while reference itself is direct.
- Confusing psychological necessity (what we believe must be true) with metaphysical necessity.

## Questions

```yaml
- question: "Before astronomers discovered that Hesperus and Phosphorus were the same planet, it seemed possible they were distinct. According to Kripke, in what sense was this 'possible'?"
  type: multiple-choice
  options:
    - "It was both epistemically and metaphysically possible — the identity was contingent before discovery"
    - "It was epistemically possible (compatible with what was known) but never metaphysically possible (there was always only one object)"
    - "It was metaphysically possible because Venus could have been in a different orbit"
    - "It was neither epistemically nor metaphysically possible — the identity was analytically true from the meaning of the names"
  answer: 1
  explanation: "Kripke's key move is distinguishing epistemic from metaphysical possibility. Epistemic possibility is about what is compatible with our knowledge: before the discovery, we couldn't rule out that they were distinct, so it was epistemically open. But metaphysical possibility is about what could have been the case in reality: 'Hesperus' rigidly designates Venus, 'Phosphorus' rigidly designates Venus, so in every possible world they refer to the same object. There is no metaphysically possible world where Hesperus ≠ Phosphorus. Option A is the mistake Kripke is correcting."

- question: "Kripke argues that 'Hesperus = Phosphorus' is necessarily true. What is the key reason?"
  type: multiple-choice
  options:
    - "The sentence is true by definition — the two names were introduced to mean the same thing"
    - "Both names are rigid designators picking out the same object (Venus) in every possible world, so the identity cannot fail in any world"
    - "Identity statements are always necessarily true, regardless of what the names designate"
    - "The discovery was made by scientists, and scientific discoveries are necessarily true"
  answer: 1
  explanation: "The argument turns on rigid designation: 'Hesperus' picks out Venus in every possible world (not just the actual one), and so does 'Phosphorus.' Since both names rigidly designate the same object, there is no possible world in which they designate different objects, and so no world in which the identity fails. Option A is wrong because the names were introduced independently with no definitional link. Option C is too strong — 'the morning star = the evening star' uses descriptions, not rigid designators, and is not necessarily true."

- question: "According to Kripke, all necessary truths are knowable a priori — if something is true in all possible worlds, we can know it without empirical investigation."
  type: true-false
  answer: false
  explanation: "False — this is precisely what Kripke refutes. 'Water = H₂O' is necessarily true (water is H₂O in every possible world, since 'water' rigidly designates the substance that actually has that chemical structure) yet it is a posteriori: we had to do chemistry to discover it. Kripke breaks the traditional alignment of necessity with a prioricity, showing that these are independent dimensions: some truths are necessary AND a posteriori, others are contingent AND a priori."

- question: "If 'water = H₂O' is a necessary truth, then there is no possible world in which water is not H₂O."
  type: true-false
  answer: true
  explanation: "True, on Kripke's account. 'Water' rigidly designates the substance that, in the actual world, has the chemical structure H₂O. Since rigid designators pick out the same thing across all worlds, 'water' picks out H₂O-stuff in every possible world. So there is no world where water exists but lacks that chemical structure. A world with a clear drinkable liquid that isn't H₂O would have a different substance — call it 'XYZ' — but it wouldn't be water. This is counterintuitive precisely because it feels like water could have turned out to be something else, but that's an epistemic intuition, not a metaphysical one."

- question: "Explain in your own words why 'water = H₂O' is both a posteriori and necessarily true, and what this shows about the relationship between necessity and a prioricity."
  type: short-answer
  answer: "It is a posteriori because we had to do empirical chemistry to discover it — there was no way to figure out that water is H₂O by analyzing the concept of water alone. It is necessarily true because 'water' is a rigid designator that picks out H₂O in the actual world, and therefore picks it out in all possible worlds. What this shows is that necessity and a prioricity are independent dimensions: something can be necessary (true in all possible worlds) while also being discoverable only through experience. The old assumption that necessary = a priori and contingent = a posteriori is wrong."
  explanation: "The deeper point is the epistemic/metaphysical distinction. Before chemistry, it was epistemically possible that water wasn't H₂O — our concepts didn't rule it out. But the metaphysical structure was fixed: there was always one substance with that chemical makeup. 'Possible' in the epistemic sense and 'possible' in the metaphysical sense come apart, and Kripke's account of rigid designation explains why."
```

## Explainer

You already know from Kripke's causal theory of naming that names are **rigid designators**: they pick out the same individual in every possible world. "Aristotle" refers to the same person whether we consider the actual world or a counterfactual world where he never taught Alexander. And you know from necessity and contingency that some truths hold across all possible worlds (necessary) while others hold only in some (contingent). This topic shows how these two ideas combine to produce a philosophically surprising result.

Consider the identity statement "Hesperus is Phosphorus"—the claim that the evening star and the morning star are the same object, namely Venus. This was an empirical discovery; ancient astronomers initially believed they were different celestial bodies. So there is a clear epistemic sense in which the statement is not a priori: we had to look at the sky over many nights to establish it. Yet once true, Kripke argues, it is **necessarily** true—true in every possible world. Why? Because "Hesperus" rigidly designates Venus, and "Phosphorus" rigidly designates Venus. In any possible world, these names pick out the same object, so the identity cannot fail. There is no possible world where Hesperus ≠ Phosphorus because there is no possible world where Hesperus fails to be Venus.

This severs a connection that philosophers had long assumed: that necessity and a prioricity go together. Kant treated them as nearly coextensive. Kripke showed they come apart in both directions. "Water is H₂O" is **a posteriori necessary**: we discovered it empirically, yet it is true in every world, because "water" rigidly designates the substance that is actually H₂O. Conversely, "I am in this room now" is **a priori contingent**: you can know it without investigation, yet it is false in many possible worlds. The old picture—necessary = a priori, contingent = a posteriori—is broken.

The deeper point returns to the contrast between **epistemic** and **metaphysical** modality. Epistemic possibility is about what is compatible with what we know; metaphysical possibility is about what could have been the case in reality. Before the discovery that Venus is both Hesperus and Phosphorus, it was *epistemically possible* that they differed—for all we knew, they might have been distinct. But it was never *metaphysically possible* for them to differ: in reality, there was always only one object. Once you distinguish these two senses of "possible," the puzzle dissolves. "Water = H₂O" feels contingent because it was epistemically open before the discovery; it is in fact necessary because in every possible world, the substance called water has whatever structure it actually has. This framework proves essential for analyzing theoretical identities in philosophy of mind—especially the identity theory's claim that pain = C-fiber firing, which faces exactly these modal pressures.
