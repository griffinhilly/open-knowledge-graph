---
id: identity-theory
title: Identity Theory (Type and Token)
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: physicalism-about-mind
  type: hard
- id: universals-and-particulars
  type: soft
builds-toward:
- functionalism-philosophy-of-mind
- multiple-realizability
- eliminative-materialism
tags:
- identity-theory
- type-identity
- token-identity
- Place
- Smart
stage: formal-systems
status: validated
---

# Identity Theory (Type and Token)

## Core Idea
Identity theory, developed by U.T. Place and J.J.C. Smart in the 1950s, claims that mental states are identical to brain states. Type identity theory says that mental state types (e.g., pain-in-general) are identical to neural state types (e.g., C-fiber firing). Token identity theory makes the weaker claim that each individual mental event token is identical to some physical event token, without requiring that all instances of a mental type share a single physical type. Type identity theory faces the multiple realizability objection: the same mental state can be realized by very different physical substrates across species, suggesting mental types cannot be identified with a single neural type.

## How It's Best Learned
Read Place's 'Is Consciousness a Brain Process?' (1956) alongside Putnam's multiple realizability critique. Distinguish the type/token distinction carefully using examples: pain-the-type versus my-pain-right-now-the-token.

## Common Misconceptions
- Identity claims in this context are contingent a posteriori identities (like 'water = H₂O'), not logical necessities discoverable from an armchair.
- Token identity does not imply that mental properties are reducible to or explicable in physical terms.

## Questions

```yaml
- question: "A researcher discovers that octopuses experience pain through a completely different neural mechanism than humans — not involving C-fibers at all. Which version of identity theory does this finding most directly challenge, and why?"
  type: multiple-choice
  options:
    - "Token identity theory, because the finding shows that pain tokens in octopuses lack a physical counterpart"
    - "Type identity theory, because it shows that the mental type 'pain' is realized by different physical types across species, undermining the claim that pain = a single neural type"
    - "Both equally, since both require mental states to have physical correlates"
    - "Neither — identity theory only applies to human minds, so cross-species findings are irrelevant"
  answer: 1
  explanation: "Type identity theory holds that the mental type 'pain' is identical to a specific neural type (like C-fiber firing) across all its instances. If octopuses feel pain via entirely different neural hardware, then 'pain' as a category cannot be identified with any single physical type — undermining type identity directly. Token identity theory survives this challenge because it only claims that each individual pain event (token) is identical to some physical event — it doesn't require all pain tokens to share the same physical type. This is precisely why the multiple realizability objection is a serious problem for type identity but not for token identity."

- question: "According to identity theory, the claim 'pain = C-fiber firing' is most similar in logical structure to which of the following?"
  type: multiple-choice
  options:
    - "'Bachelors are unmarried men' — a conceptual truth knowable from definitions alone"
    - "'Water = H₂O' — a contingent identity discovered through empirical investigation, not armchair reasoning"
    - "'2 + 2 = 4' — a necessary mathematical truth that could not be otherwise"
    - "'The morning star is bright' — a description that is contingently true but not an identity claim"
  answer: 1
  explanation: "Identity theorists explicitly describe mental-physical identities as contingent a posteriori claims — discovered through scientific investigation, not derivable from concepts. Just as 'water = H₂O' was not knowable by thinking about the word 'water' (it required chemistry), 'pain = C-fiber firing' (if true) would be discovered through neuroscience. This matters because it means the identity could in principle turn out to be false — it is an empirical hypothesis, not a logical necessity. Confusing it with analytic truths like 'bachelors are unmarried' is the mistake that leads people to think the mind-brain identity could be established or refuted by conceptual analysis alone."

- question: "According to identity theory, mental states and brain states are not merely correlated or causally linked — they are literally the same thing, described at different levels of abstraction."
  type: true-false
  answer: true
  explanation: "This is the core claim of identity theory, and what distinguishes it from weaker physicalist positions like epiphenomenalism or property dualism. 'Pain' and 'C-fiber firing' name the same state, just as 'heat' and 'mean kinetic energy of molecules' name the same physical phenomenon. The apparent gap between mental vocabulary and physical vocabulary is, on this view, simply a vocabulary gap — not a gap in the world. This strong identity claim is both the theory's power (it is scientifically tractable) and its vulnerability (it is falsifiable by multiple realizability)."

- question: "Token identity theory makes the weaker claim that each individual mental event is identical to some physical event, so it implies that mental properties are fully reducible to and explicable in physical terms."
  type: true-false
  answer: false
  explanation: "This is one of the key misconceptions flagged in the topic. Token identity claims only that each mental event token has some physical event token it is identical to — it says nothing about whether mental properties (the kinds, types, or categories of mental states) are reducible to physical properties. A mental property like 'being in pain' could be multiply realizable across different physical substrates, meaning it resists type-level reduction even if every token pain is physically realized. Token identity is compatible with anti-reductionism about mental properties — which is part of why it is the weaker and more defensible position."

- question: "How does the analogy 'heat is mean kinetic energy of molecules' illuminate what identity theorists mean when they say mental states are identical to brain states, rather than merely correlated with them?"
  type: short-answer
  answer: "The analogy shows that 'heat' and 'mean kinetic energy' are two different descriptions of one underlying physical reality — not two separate things that happen to go together. Before physics, people noticed heat and molecular motion were correlated; physics revealed they are the same thing at different levels of description. Identity theorists make the same move: 'pain' and 'C-fiber firing' aren't two things that reliably co-occur — they are one thing described in mentalistic versus neurological vocabulary. The correlation is not the identity; the identity explains why the correlation is perfect."
  explanation: "This analogy is central to understanding why identity theory is a stronger and more parsimonious claim than mere correlation. Correlation still implies two things; identity implies one thing with two names. The practical difference: if pain merely correlated with C-fiber firing, we might ask what makes them go together, and whether they could come apart. If they are identical, those questions dissolve — there is no further fact to explain. The heat/kinetic energy case also illustrates that the identity was not obvious a priori, which is why identity theorists insist these are a posteriori, empirical identities discovered through science."
```

## Explainer

You already know that physicalism holds that the mind is entirely physical — that there is nothing in the mental world beyond what exists in the physical world. Identity theory is physicalism's most direct version: it says mental states are not merely correlated with brain states or causally produced by them, but are literally *identical* to them. Just as "water" and "H₂O" name the same substance, "pain" and "C-fiber firing" name the same state. This is a **contingent a posteriori identity** — we discovered it through science, not armchair reasoning, exactly as we discovered that water is H₂O.

The crucial distinction the theory draws is between **type identity** and **token identity**. A *type* is a category — pain-in-general, the kind of mental state. A *token* is an individual instance — this particular pain I feel right now. Type identity theory (associated with Place and Smart) makes the bold claim that the mental type *pain* is identical to the physical type *C-fiber firing*. Every instance of pain, across every person and every creature, involves that same neural type. Token identity theory makes the weaker claim: each individual mental event token is identical to some physical event token, but different instances of pain might correspond to different physical types.

Why does the type/token distinction matter? Because of the **multiple realizability** objection, which your next topic addresses directly. Pain is felt by humans, octopuses, and perhaps robots. Human pain may involve C-fibers; octopus pain involves different neural hardware entirely; a silicon-based AI might involve transistors. If the mental type *pain* could be realized by radically different physical types, then there is no single physical type for it to be identical to — which defeats type identity theory. Token identity survives this challenge by not requiring sameness of physical type; each token pain simply needs some physical token to be identical to.

Think of the identity claim like discovering that heat *is* mean kinetic energy of molecules — not that they go together, or that one produces the other, but that they are the same thing described at different levels of abstraction. The apparent gap between mind-talk and brain-talk is, on this view, just a gap between two vocabularies for one underlying reality. Identity theory's power and vulnerability come from the same source: it commits to a strong reductionist claim that makes it falsifiable, but also exposes it to empirical and conceptual challenge.
