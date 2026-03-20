---
id: possible-worlds-semantics-metaphysics
title: Possible Worlds
domain: philosophy
course: metaphysics
prerequisites:
- id: modal-logic-intro
  type: hard
- id: what-is-metaphysics
  type: soft
- id: propositional-semantics
  type: soft
- id: possible-worlds-semantics
  type: soft
builds-toward:
- modal-realism
- counterfactual-causation
tags:
- possible worlds
- modality
- necessity
- possibility
- semantics
stage: advanced
status: validated
---
# Possible Worlds

## Core Idea
Possible worlds are complete ways reality could have been — they provide truth conditions for modal claims like 'possibly P' (true in some world) and 'necessarily P' (true in all worlds). Introduced by Leibniz and formalized by Kripke for modal logic, possible worlds semantics is now the standard framework for analyzing modality, counterfactuals, and propositional attitudes. The framework is neutral between realist views (possible worlds are concrete entities) and ersatzist views (they are abstract representations). The semantics works regardless of one's metaphysical commitments about the status of these worlds.

## How It's Best Learned
Master Kripke semantics for propositional modal logic first, then read the opening chapters of Lewis's On the Plurality of Worlds for the realist extension. Practice evaluating modal sentences by tracing which worlds are accessible from which.

## Common Misconceptions
- Possible worlds are not physical universes in another dimension — that's one controversial interpretation (modal realism), not the framework itself.
- 'Possible' does not mean 'conceivable'; conceivability is an epistemic notion and may not track genuine metaphysical possibility.

## Explainer

From modal logic, you know that necessity (□) and possibility (◇) are operators on propositions, and that the Kripke semantics interprets them via accessibility relations between worlds. "Necessarily P" means P is true in all accessible worlds; "possibly P" means P is true in at least one accessible world. What you're now entering is the metaphysical question: what *are* possible worlds? What is the ontological status of these things we're quantifying over?

The framework itself is neutral. Kripke semantics tells us that possible worlds are whatever plays the right theoretical role—complete, consistent ways things could be. Think of them as maximal scenarios: a possible world specifies, for every proposition, whether it is true or false. Our world is one such specification; another world is one where Napoleon won at Waterloo; another is one where water is made of something other than H₂O. The **accessibility relation** between worlds models different modal concepts: for metaphysical necessity, every world is accessible from every other; for epistemic possibility, a world w' is accessible from w if w' is compatible with what is known in w. Different logical systems (S4, S5) correspond to different formal constraints on this relation.

Now comes the metaphysics. **Modal realism**, associated with David Lewis, takes possible worlds to be concrete entities—as real as the actual world, differing only in that we happen to be in this one and not them. Other worlds are not abstract representations; they are spatiotemporally isolated universes containing real people and events. Lewis argues this gives the cleanest, most powerful account of modal truth: "it is possible that P" is literally true because there is a concrete world where P is the case, full stop. The payoff is enormous: counterfactuals, laws of nature, properties, and propositions all get reductive analyses in terms of possible worlds.

The alternative is **ersatzism**: possible worlds are abstract objects—sets of propositions, maximal consistent descriptions, or structural representations—that *represent* ways things could be without being concrete realities. Most philosophers find this less extravagant ontologically. The cost is that you need to explain representation (what makes an abstract object represent a particular possibility?) without using modal primitives, or you end up helping yourself to the very modality you were supposed to be analyzing. The central lesson for applying possible worlds semantics: the framework works as a formal tool regardless of which metaphysical view you hold. You can evaluate modal arguments, analyze counterfactuals, and test for validity in Kripke frames without settling whether possible worlds are Lewisian concreta or abstract ersatz representations. The metaphysics becomes pressing only when you want a fully reductive account of modality itself.
