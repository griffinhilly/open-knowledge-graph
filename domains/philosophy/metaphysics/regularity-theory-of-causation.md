---
id: regularity-theory-of-causation
title: Regularity Theory of Causation
domain: philosophy
course: metaphysics
prerequisites:
- id: causation-and-causal-relations
  type: hard
builds-toward:
- counterfactual-causation
tags:
- Hume
- regularity
- constant conjunction
- causal necessity
- empiricism
stage: formal-systems
status: validated
---

# Regularity Theory of Causation

## Core Idea
The regularity theory, associated with Hume, holds that causation consists in nothing more than constant conjunction under a universal law: C causes E if and only if events of type C are invariably followed by events of type E. There is no hidden 'necessary connection' beyond this regularity. This view fits with empiricist scruples about metaphysical excess, but faces the problem of distinguishing genuine causal laws from accidental regularities (all gold spheres are under a mile in diameter — yet this isn't a causal law). Mill's methods and later INUS condition accounts (Mackie) attempted to refine the regularity approach.

## How It's Best Learned
Read Hume's Treatise 1.3.14 on the idea of necessary connexion, then Mackie's 'Causes and Conditions' for the INUS refinement. Try to construct a counterexample to the basic regularity view before reading the responses.

## Common Misconceptions
- Regularity theory doesn't say causation is merely subjective; the regularities are objective features of the world.
- The INUS account is a significant upgrade over naive constant conjunction — don't equate the two.

## Questions

```yaml
- question: "All gold spheres in existence have been less than one mile in diameter — a universal regularity. Why does the simple regularity theory struggle to treat this as a causal law?"
  type: multiple-choice
  options:
    - "It should count as a causal law — the regularity theory accepts all universal regularities as causal"
    - "There are not enough gold spheres observed to establish a reliable regularity"
    - "The regularity theory cannot distinguish this accidental correlation from genuine causal laws — it lacks the resources to require more than bare constant conjunction"
    - "Gold is not a natural kind, so regularities involving gold are excluded by the theory"
  answer: 2
  explanation: "This is the classic counterexample to naive constant conjunction. Being a gold sphere doesn't cause smallness — the correlation is accidental, not underwritten by any physical necessity. The bare regularity theory, which requires only that C-type events invariably precede E-type events, cannot on its own distinguish genuine causal laws (which support counterfactuals and reflect physical structure) from accidental regularities (which don't). This is the central problem the theory must solve."

- question: "A house fire starts after a short circuit. According to Mackie's INUS account, the short circuit is best described as:"
  type: multiple-choice
  options:
    - "A sufficient cause — by itself it caused the fire"
    - "A necessary cause — without it, no fire could have occurred"
    - "An Insufficient but Necessary part of an Unnecessary but Sufficient condition — required within the actual bundle of conditions, though other bundles could also cause fire"
    - "An accidental antecedent — its presence was correlated with but not causally relevant to the fire"
  answer: 2
  explanation: "INUS: the short circuit alone is insufficient (it needs dry conditions, flammable materials, no sprinklers, etc.). But within the actual bundle of conditions present, removing the short circuit would have prevented that particular sufficient condition from obtaining — so it was necessary within the bundle. However, other bundles (e.g., arson) could have caused fire, so the short circuit is not necessary overall. This multi-part analysis captures why we single out the short circuit as the cause without claiming it was either sufficient alone or necessary in all possible scenarios."

- question: "According to Hume's regularity theory, there is no observable necessary connection between cause and effect — only the constant conjunction of event-types is observed."
  type: true-false
  answer: true
  explanation: "This is Hume's central empiricist insight and the foundation of the regularity theory. We never directly observe causation or necessity — we observe fire reliably followed by heat, repeatedly. The feeling that we 'see' necessity is, Hume argued, a projection of our habituated expectations onto the external world. The regularity theory takes this austerity seriously by grounding causation entirely in objective regularities rather than unobservable metaphysical connections."

- question: "According to the regularity theory, a genuine cause must be a necessary condition for its effect — without the cause, the effect could not have occurred."
  type: true-false
  answer: false
  explanation: "The regularity theory requires that C-type events be invariably followed by E-type events, but does not require that E cannot occur without C. Overdetermination — where two simultaneous, each-sufficient causes both produce the effect — is precisely a case where neither cause is strictly necessary (the other would have produced the effect anyway). This is one of the hard cases that exposes the theory's limits. Confusing causation with necessity is exactly the metaphysical excess Hume wanted to eliminate."

- question: "What is the 'accidental regularity' problem for the regularity theory, and how does Mackie's INUS account attempt to address it?"
  type: short-answer
  answer: "The problem: some universal regularities are not causal (all gold spheres are small, but smallness isn't caused by being a gold sphere). Bare constant conjunction cannot distinguish these from genuine laws. Mackie's INUS account addresses this by requiring that a cause be a necessary part of a sufficient bundle of conditions — singling out factors that play a structural role in producing the effect, not just any correlation."
  explanation: "The INUS account moves beyond mere correlation by requiring that the cause play a specific role within a sufficient set of conditions (necessary within the bundle). This excludes pure accidental regularities, where there is no bundle of conditions of which the 'cause' is a necessary component. However, the account still relies on regularities at some level — the sufficiency of the bundle is itself a regularity claim — which is why the theory remains in the 'regularity' family rather than moving to counterfactual or causal-powers approaches."
```

## Explainer

From your study of causation and causal relations, you know the core philosophical puzzle: causation seems to be more than mere correlation — when one event causes another, there appears to be a necessary connection between them, not just a temporal sequence. Striking a match in oxygen causes ignition; it doesn't merely precede it. The question is what this "necessary connection" actually is. Hume's revolutionary answer was: nothing. You never observe necessity; you observe only that striking is reliably followed by ignition. The regularity theory builds an account of causation on that austerity.

The basic **regularity account** states: event C causes event E if and only if events of type C are invariably followed by events of type E, under a universal law. There is no hidden metaphysical glue beyond this regularity — no causal powers, no productive relations, no necessary connections in nature. When we say fire causes heat, all that is objectively in the world is the constant conjunction: fire-type events are universally followed by heat-type events. The subjective feeling that we "see" the necessity is, Hume argued, a projection of our own habituated expectations onto the external world. We observe regularity; we feel necessity. The necessity is in us, not in the world.

The immediate problem is distinguishing **genuine causal laws from accidental regularities**. Consider: all gold spheres are less than a mile in diameter, and this has been true throughout history — a universal regularity. But being a gold sphere doesn't *cause* smallness; the regularity is merely accidental, not lawlike. Or consider a clock that always runs slightly ahead of another: the earlier reading is always followed by the later reading, but the first clock doesn't cause the second to advance. John Stuart Mill's **methods** — agreement, difference, joint method, concomitant variation — were attempts to operationalize the distinction: a genuine cause is the factor that is present when the effect is present and absent when the effect is absent, across systematic variation of other factors. But Mill's methods identify correlations, not causation; they don't escape the original problem.

John Mackie's **INUS account** is a more sophisticated refinement. A cause is an Insufficient but Necessary part of an Unnecessary but Sufficient condition. That is: the full set of conditions that produces an effect is often far richer than any single factor (it's insufficient on its own), yet the particular cause we identify is a necessary component of that bundle (without it, that particular sufficient condition fails). Multiple different bundles might suffice for the same effect (the condition is unnecessary), but within the bundle that actually obtained, the cause was required. This captures why we say the short circuit caused the fire: the short circuit was a necessary part of the bundle of conditions (dry weather, flammable material, no sprinklers) that was sufficient for ignition — even though other bundles might have caused the fire some other way.

The INUS account is a genuine advance, but the regularity framework as a whole still faces hard cases. **Overdetermination** (two simultaneous, each sufficient causes), **pre-emption** (one cause that beats another to the effect), and **symmetric overdetermination** (two simultaneous, each alone sufficient) all produce cases where regularity analyses give unintuitive verdicts. These difficulties motivate the transition to counterfactual theories of causation — theories that analyze causation in terms of what would have happened if C had not occurred — which you will encounter in the next topic.
