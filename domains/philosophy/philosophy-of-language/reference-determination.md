---
id: reference-determination
title: 'Reference Determination: How Words Hook onto the World'
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: meaning-and-reference-basics
  type: hard
builds-toward:
- kripke-causal-theory-naming
- putnam-semantic-externalism
- davidson-truth-conditional-semantics
tags:
- reference
- semantics
- grounding
stage: abstract-reasoning
status: validated
---

# Reference Determination: How Words Hook onto the World

## Core Idea
Reference-determination addresses the fundamental question: what makes a word or expression pick out a particular object or set of objects in the world? Theories include descriptive content, causal history, use conventions, and speaker intentions. No single mechanism explains all cases—some terms may be referentially fixed by description, others by causal chains, others by social convention.

## Questions

```yaml
- question: "According to the causal-historical theory of reference, if it turns out that a man named Schmidt actually proved the incompleteness theorems and Gödel merely stole the proof, then our uses of 'Gödel' refer to:"
  type: multiple-choice
  options:
    - "Schmidt, because 'Gödel' picks out whoever actually proved the incompleteness theorems"
    - "No one, because the name's descriptive content fails to fit any real person"
    - "Gödel, because reference tracks the causal chain back to the original naming, not descriptive fit"
    - "Both men equally, since the reference is ambiguous"
  answer: 2
  explanation: "On the causal-historical theory (Kripke), reference is fixed by a causal chain tracing back to the original dubbing event, not by whatever descriptions speakers associate with the name. Most people associate 'Gödel' with 'proved the incompleteness theorems' — but if that description fits Schmidt, not Gödel, the causal theory says we're still talking about Gödel. The name hooks onto the man who was originally called 'Gödel,' regardless of whether our beliefs about him are correct. This is exactly the kind of case that shows why the description theory fails: it would wrongly predict we're talking about Schmidt."

- question: "Putnam's semantic externalism argues that what 'water' refers to is determined by:"
  type: multiple-choice
  options:
    - "The descriptions and beliefs speakers associate with the word 'water'"
    - "Social conventions established by linguistic communities over time"
    - "The real nature of the stuff in the environment, even when speakers don't know its chemical structure"
    - "The intentions of the original speaker who introduced the term"
  answer: 2
  explanation: "Putnam's externalism holds that 'water' refers to H₂O even among speakers who had no idea water was H₂O. Reference is partly determined by the environment — by what is actually there — not solely by internal mental content. Before chemistry, people used 'water' to refer to H₂O without knowing it. The reference was already fixed by the nature of the substance in the world. This is why Putnam says 'meanings ain't in the head': what a word picks out can depend on facts outside the speaker's mind."

- question: "On the description theory of reference, if everyone who uses the name 'Aristotle' associates it only with 'the teacher of Alexander,' then it is necessarily true that Aristotle taught Alexander."
  type: true-false
  answer: true
  explanation: "True — and this is precisely Kripke's devastating objection to the description theory. If 'Aristotle' just *means* 'the teacher of Alexander,' then by definition, Aristotle taught Alexander — it's analytically true, hence necessarily true. But intuitively, Aristotle *might* never have met Alexander; it's a contingent historical fact. The description theory generates a false necessity by conflating the reference-fixing description with the meaning of the name. This shows that names cannot simply mean their associated descriptions."

- question: "Semantic externalism implies that two speakers with identical internal mental states could mean different things by the same word."
  type: true-false
  answer: true
  explanation: "True, and this is Putnam's 'Twin Earth' thought experiment. Imagine a planet exactly like Earth where the substance that fills rivers, falls as rain, and is called 'water' has a different chemical structure (XYZ instead of H₂O). A person on Twin Earth and their mental duplicate on Earth have identical internal states, but their uses of 'water' refer to different substances — H₂O vs. XYZ. This shows that reference is determined at least partly by the environment, not solely by what is in the speaker's head. Meaning is not purely internal."

- question: "Why does the causal-historical theory say reference is stable even when speakers hold false beliefs about the referent?"
  type: short-answer
  answer: "Because on the causal-historical theory, what determines reference is the chain of communication tracing back to an original naming event, not the accuracy of speakers' subsequent descriptions. Each speaker inherits their use from prior speakers, who inherited it from others, all the way back to whoever first introduced the name for the object. Even if beliefs associated with the name are wrong, the referential chain remains anchored to the original object."
  explanation: "This is the deepest advantage of the causal-historical view over description theories. Reference doesn't require descriptive knowledge of the referent — it requires only participation in a communicative tradition that links back to an original grounding. This explains how ordinary people can refer to 'gold' or 'Aristotle' even if their beliefs about gold's chemistry or Aristotle's biography are largely mistaken. The chain does the referential work; speakers need not know the exact nature of what they're talking about."
```

## Explainer

From your prerequisite work on meaning and reference basics, you know the Fregean starting point: there's a difference between **sense** (the mode of presentation, *how* you think about something) and **reference** (the object itself, *what* is picked out). The morning star and the evening star have different senses but the same reference — Venus. But this raises a deeper question: what makes it the case that any expression refers to anything at all? What's the mechanism by which the word "gold" hooks onto actual gold in the world, rather than something else?

The classical answer, the **description theory**, says a name or term refers to whatever uniquely satisfies the descriptions associated with it. "Aristotle" refers to the person who was the teacher of Alexander, the student of Plato, the author of the *Nicomachean Ethics*, and so on. The reference is fixed by the descriptive content speakers associate with the name. This view has intuitive appeal — it explains how we can think about absent and non-existent objects using descriptive content. But it runs into severe problems. Kripke's modal argument: if "Aristotle" meant "the teacher of Alexander," then it would be *necessarily* true that Aristotle taught Alexander, since that's what "Aristotle" picks out. But it seems clearly *contingent* — Aristotle might never have met Alexander. The description theory conflates the reference-fixing description with the meaning, generating false necessities.

Kripke's alternative is the **causal-historical theory**: names refer because of a causal chain linking present use back to an original dubbing or naming event. "Aristotle" refers to Aristotle because someone introduced that name while pointing to (or talking directly about) the man, and subsequent uses of the name inherited their reference through a chain of communication back to that original event. This explains why reference is stable even when speakers associate wrong descriptions with a name. Most people associate "Gödel" with "the man who proved the incompleteness theorems" — but if it turned out a man named Schmidt actually proved those theorems and Gödel stole the proof, we'd say our uses of "Gödel" still referred to the man called Gödel, not to Schmidt. Reference tracks causal origin, not descriptive fit.

Natural kind terms like "water" and "gold" introduce a third variation: **semantic externalism**. Putnam argued that "water" refers to H₂O even when speakers didn't know water's chemical structure, because what the term picks out is determined by the real nature of the stuff, not by speakers' internal descriptions. Reference is partly determined by the *environment* — by what is actually there — not just by what's in the speaker's head. Together these theories show that reference-determination is a heterogeneous phenomenon: different mechanisms may operate for proper names, natural kind terms, and ordinary descriptions, which is why this course builds toward Kripke, Putnam, and Davidson as three distinct frameworks, not one unified theory.
