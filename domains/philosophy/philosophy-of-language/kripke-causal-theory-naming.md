---
id: kripke-causal-theory-naming
title: Kripke's Causal Theory of Reference for Proper Names
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: russell-definite-descriptions
  type: hard
- id: frege-sense-and-reference
  type: hard
builds-toward:
- rigid-designators-modal-reference
- proper-names-and-reference
tags:
- Kripke
- names
- reference
- causation
stage: formal-systems
status: draft
---

# Kripke's Causal Theory of Reference for Proper Names

## Core Idea
Kripke argued that proper names do not function like Russell's descriptions or Frege's senses. A name like 'Richard Nixon' is not synonymous with any description because we can coherently imagine Nixon not satisfying that description. Instead, names are directly referential: they refer via a causal-historical chain connecting the name to its bearer through an initial baptism (ostensive or descriptive). A name refers to whoever originated that causal chain, regardless of what descriptive information speakers associate with the name.

## How It's Best Learned
Trace the causal history of a name from its origin through a community. Contrast with descriptive theories by constructing counterfactuals: suppose Nixon had lost the election; what does 'Nixon' refer to? The answer reveals what determines reference.

## Common Misconceptions
Kripke said speakers need not know what they're referring to—they don't need the correct description or history, but the name must be grounded in community practice. Causal history is metaphysically mysterious—Kripke was proposing an empirical hypothesis about naming conventions.

## Questions

```yaml
- question: "A speaker mistakenly believes 'Einstein' refers to whoever invented the lightbulb. When they say 'Einstein was a genius,' who are they referring to?"
  type: multiple-choice
  options:
    - "Thomas Edison, since that's who satisfies the description 'inventor of the lightbulb'"
    - "No one, because the description associated with the name is false"
    - "Albert Einstein, because their use is connected through a community causal chain to the correct individual"
    - "The meaning shifts depending on which description the speaker holds most firmly"
  answer: 2
  explanation: "On Kripke's causal-historical view, what fixes reference is not the descriptions a speaker associates with a name, but the causal chain connecting their use back to the original baptism. Even with a false belief about the person, the speaker still refers to Einstein because their use is anchored through community practice to the historical individual. This is what Kripke calls the 'linguistic division of labor' — ordinary speakers can refer successfully without holding correct descriptions."

- question: "The sentence 'Aristotle might never have taught Alexander' is:"
  type: multiple-choice
  options:
    - "A contradiction — if 'Aristotle' means 'the teacher of Alexander,' then this says the teacher of Alexander was not the teacher of Alexander"
    - "Coherent and possibly true — 'Aristotle' is a rigid designator picking out the same person even in worlds where he had a different career"
    - "False — historical facts about what Aristotle actually did are necessarily true across all possible worlds"
    - "Meaningless — we cannot coherently reason about counterfactual historical scenarios"
  answer: 1
  explanation: "This is Kripke's central modal argument against description theories. If 'Aristotle' were synonymous with 'the teacher of Alexander,' the sentence would be a contradiction. But it is not — we can coherently imagine Aristotle becoming a fisherman instead. This shows that 'Aristotle' must refer to the person, not to whoever satisfies a description. Names are rigid designators: they pick out the same individual in every possible world where that individual exists, regardless of which properties they happen to have."

- question: "According to Kripke, the reference of a proper name is fixed at an initial baptism and transmitted through a community chain, regardless of what descriptions speakers associate with the name."
  type: true-false
  answer: true
  explanation: "This is the core claim of the causal-historical theory. Reference is grounded in an initial baptismal event — either by ostension ('This person is Aristotle') or description ('Let's name the baby Aristotle'). The name then propagates through a community of speakers, each intending to refer to whoever the previous speaker was referring to. What matters for reference is the chain, not the descriptive content any individual speaker associates with the name."

- question: "On Kripke's view, a name refers to the object that uniquely satisfies the descriptions most speakers in a community associate with it."
  type: true-false
  answer: false
  explanation: "This is the descriptivist view that Kripke directly attacks. He argues that names do not function as abbreviated descriptions. His modal argument shows that we can coherently imagine the name's bearer not satisfying any given description, which means the descriptions cannot be what fix reference. Instead, reference is fixed by the causal-historical chain back to the initial baptism — and speakers can refer correctly even when their associated descriptions are false or incomplete."

- question: "What is a rigid designator, and why does Kripke argue that proper names are rigid designators while definite descriptions are not?"
  type: short-answer
  answer: "A rigid designator is an expression that picks out the same individual in every possible world where that individual exists, regardless of what properties they have in that world. Kripke argues names are rigid because 'Aristotle might not have been a philosopher' refers to that very person possibly having a different career — the name tracks the individual across counterfactual scenarios. A definite description like 'the teacher of Alexander' is not rigid because it picks out whoever satisfies that description in each possible world, which could be a different person. Names latch onto individuals through causal history; descriptions latch onto roles that may be filled by different individuals in different circumstances."
  explanation: "The rigidity of names has important metaphysical consequences. If 'Hesperus' and 'Phosphorus' are both rigid designators for the planet Venus, then 'Hesperus is Phosphorus' is necessarily true if true at all — not contingently true as a description theory would suggest. This connection between naming, rigidity, and modal necessity is Kripke's broader contribution to metaphysics."
```

## Explainer

From Frege, you know that names have both **sense** (the descriptive content or "mode of presentation") and **reference** (the object picked out). From Russell, you know about **definite descriptions** — expressions like "the first person to walk on the moon" that refer via uniquely satisfying a description. Russell argued that ordinary names, on analysis, function as abbreviated definite descriptions: "Aristotle" means something like "the teacher of Alexander who studied under Plato." On this view, what a name refers to is determined by the descriptions speakers associate with it.

Kripke's attack on the description theory begins with **modal intuitions**. Consider: could Aristotle have not been the teacher of Alexander? Intuitively, yes — history could have gone differently, and Aristotle might have become a farmer or died young. But if "Aristotle" just means "the teacher of Alexander," then "Aristotle was not the teacher of Alexander" would mean "the teacher of Alexander was not the teacher of Alexander" — a contradiction. Since it is not a contradiction (we can coherently imagine it), "Aristotle" cannot be synonymous with that description. This motivates the concept of a **rigid designator**: a term that picks out the same individual in every possible world where that individual exists, regardless of what properties they happen to have in that world. Names are rigid designators; descriptions are not — "the teacher of Alexander" picks out whoever satisfies that description in each world, which could vary.

If names don't refer via descriptions, what does fix their reference? Kripke's answer is the **causal-historical chain**. Reference is grounded in an initial **baptism** — a founding event in which the name is attached to its bearer, either by direct ostension ("This person is 'Aristotle'") or by descriptive identification ("Let's name the baby born today 'Aristotle'"). From that point, the name propagates through a community of speakers, each using it with the intention to refer to whoever the previous speaker was referring to. When you use "Aristotle" today, you are linked — through a long chain of transmission — to that original baptismal event, and thereby to Aristotle himself, regardless of what descriptions you personally associate with the name.

The practical upshot is striking: reference can come apart from the descriptions a speaker associates with a name. Suppose you believe "Einstein was the man who invented the lightbulb" — that belief is false, but you are still referring to Einstein when you use his name, because your use is connected through a community chain to the correct historical individual. This reflects a **linguistic division of labor**: ordinary speakers can successfully refer to things they have limited or incorrect beliefs about, as long as their use is properly anchored through the social and historical chain. The implications extend into metaphysics: because names are rigid designators, identity statements involving names ("Hesperus is Phosphorus") are necessarily true if true at all — they are not contingent descriptions of what things happen to be identical. This connection between naming, rigidity, and necessity is the gateway into Kripke's broader work on necessity and the metaphysics of essence.
