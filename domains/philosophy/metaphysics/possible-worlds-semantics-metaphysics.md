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

## Questions

```yaml
- question: "A philosopher claims: 'It is necessarily true that water is H₂O.' How does possible worlds semantics represent this claim?"
  type: multiple-choice
  options:
    - "The claim is true in our world but stipulated to be false in some hypothetical worlds"
    - "The claim is true in all possible worlds — there is no accessible world where water is not H₂O"
    - "The claim is verified by the fact that we can conceive of a world without H₂O"
    - "The claim means only that H₂O is the empirically correct description in the actual world"
  answer: 1
  explanation: "In possible worlds semantics, 'necessarily P' means P is true in all accessible worlds. For metaphysical necessity (where the accessibility relation is universal), 'necessarily water is H₂O' means there is no possible world where water is something other than H₂O. This is distinct from conceivability — one can conceive of XYZ oceans, but conceivability doesn't settle metaphysical possibility. Kripke argued that true identity statements like this are necessarily true."

- question: "Which of the following best captures the difference between modal realism and ersatzism about possible worlds?"
  type: multiple-choice
  options:
    - "Modal realists think possible worlds are useful fictions; ersatzists think they are real"
    - "Modal realists (Lewis) hold that other possible worlds are concrete entities like the actual world; ersatzists hold they are abstract representations"
    - "Modal realists define necessity in terms of what we can imagine; ersatzists use formal logic"
    - "Modal realism is a view about physics; ersatzism is a view about mathematics"
  answer: 1
  explanation: "David Lewis's modal realism holds that possible worlds are concrete, spatiotemporally isolated universes — as real as our world, just causally inaccessible to us. Ersatzism (held by most philosophers) treats possible worlds as abstract objects — sets of propositions, maximal consistent descriptions — that represent ways things could be without being concrete realities. The debate concerns ontological status, not the utility of possible worlds as a formal tool."

- question: "Accepting possible worlds semantics as a formal framework commits a philosopher to modal realism — the view that other possible worlds are concrete entities."
  type: true-false
  answer: false
  explanation: "This is the central misconception to avoid. Possible worlds semantics assigns truth conditions to modal statements — 'possibly P' is true iff P is true in some accessible world — and this works equally well whether worlds are Lewisian concrete universes or abstract ersatz representations. Many philosophers use possible worlds semantics while remaining committed ersatzists. The metaphysical question of what worlds ARE is separate from the semantic question of how modal claims are evaluated."

- question: "In possible worlds semantics, 'possibly P' is true if and only if P is conceivable — that is, we can coherently imagine a world where P holds."
  type: true-false
  answer: false
  explanation: "Conceivability and metaphysical possibility come apart. Conceivability is an epistemic notion — what a mind can entertain without apparent contradiction. But something can be conceivable yet metaphysically impossible: one can conceive of water that is not H₂O (before knowing chemistry), but Kripke argues such a world is not genuinely possible if water's identity with H₂O is necessary. Possible worlds semantics tracks metaphysical possibility, not the limits of human imagination."

- question: "Explain how the possible worlds framework can function as a useful tool for analyzing modal claims without requiring any commitment to a particular view of what possible worlds really are."
  type: short-answer
  answer: "Possible worlds semantics provides truth conditions: 'necessarily P' is true iff P holds in all accessible worlds; 'possibly P' is true iff P holds in some accessible world. These conditions allow evaluating modal arguments, checking validity in Kripke models, and analyzing counterfactuals — regardless of whether 'worlds' are concrete Lewisian universes or abstract ersatz representations. The framework specifies the role possible worlds must play without specifying their intrinsic nature. The metaphysics matters only when seeking a fully reductive account of modality."
  explanation: "An analogy: a mathematician can use the real number line to solve equations without settling what numbers ultimately are (Platonic objects? Structuralist positions? Fictionalist tools?). Similarly, philosophers use possible worlds to evaluate modal reasoning without settling foundational questions about their ontology. The semantic tool works for its purpose regardless of the metaphysical background theory."
```

## Explainer

From modal logic, you know that necessity (□) and possibility (◇) are operators on propositions, and that the Kripke semantics interprets them via accessibility relations between worlds. "Necessarily P" means P is true in all accessible worlds; "possibly P" means P is true in at least one accessible world. What you're now entering is the metaphysical question: what *are* possible worlds? What is the ontological status of these things we're quantifying over?

The framework itself is neutral. Kripke semantics tells us that possible worlds are whatever plays the right theoretical role—complete, consistent ways things could be. Think of them as maximal scenarios: a possible world specifies, for every proposition, whether it is true or false. Our world is one such specification; another world is one where Napoleon won at Waterloo; another is one where water is made of something other than H₂O. The **accessibility relation** between worlds models different modal concepts: for metaphysical necessity, every world is accessible from every other; for epistemic possibility, a world w' is accessible from w if w' is compatible with what is known in w. Different logical systems (S4, S5) correspond to different formal constraints on this relation.

Now comes the metaphysics. **Modal realism**, associated with David Lewis, takes possible worlds to be concrete entities—as real as the actual world, differing only in that we happen to be in this one and not them. Other worlds are not abstract representations; they are spatiotemporally isolated universes containing real people and events. Lewis argues this gives the cleanest, most powerful account of modal truth: "it is possible that P" is literally true because there is a concrete world where P is the case, full stop. The payoff is enormous: counterfactuals, laws of nature, properties, and propositions all get reductive analyses in terms of possible worlds.

The alternative is **ersatzism**: possible worlds are abstract objects—sets of propositions, maximal consistent descriptions, or structural representations—that *represent* ways things could be without being concrete realities. Most philosophers find this less extravagant ontologically. The cost is that you need to explain representation (what makes an abstract object represent a particular possibility?) without using modal primitives, or you end up helping yourself to the very modality you were supposed to be analyzing. The central lesson for applying possible worlds semantics: the framework works as a formal tool regardless of which metaphysical view you hold. You can evaluate modal arguments, analyze counterfactuals, and test for validity in Kripke frames without settling whether possible worlds are Lewisian concreta or abstract ersatz representations. The metaphysics becomes pressing only when you want a fully reductive account of modality itself.
