---
id: reference-determination-theory
title: Reference Determination and Semantic Reference
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: kripke-causal-theory-naming
  type: hard
- id: putnam-semantic-externalism
  type: hard
- id: direct-reference-theory
  type: soft
- id: intensionality-and-opacity
  type: soft
- id: proper-names-and-reference
  type: soft
- id: proposition-and-semantic-content
  type: soft
- id: naturalism-semantic-facts
  type: soft
builds-toward:
- natural-kinds-and-essence
- empty-names-fictional
tags:
- reference
- naming
- semantics
stage: formal-systems
status: validated
---
# Reference Determination and Semantic Reference

## Core Idea
How do names and descriptions refer? Causal-historical theories hold reference is fixed by initial baptism and historical chain; descriptive theories hold reference is determined by properties. Modern approaches combine elements: reference is anchored historically but constrained by descriptive content.

## Questions

```yaml
- question: "A speaker uses the name 'Aristotle' but believes only false things about him — that he was a Macedonian king, never wrote philosophy, and lived in the 1st century BCE. On Kripke's causal-historical account, does this speaker successfully refer to Aristotle?"
  type: multiple-choice
  options:
    - "No — the speaker cannot refer to Aristotle because their beliefs don't match his actual properties"
    - "Yes — reference is determined by the causal-historical chain connecting the speaker's use to the original baptism of 'Aristotle,' not by the speaker's descriptions"
    - "Only partly — the speaker refers to a 'Aristotle-like' individual satisfying most of their descriptions"
    - "No — reference requires at least one true belief about the referent to anchor the causal chain"
  answer: 1
  explanation: "On Kripke's account, individual speakers 'borrow' reference from the community they learned the name from, ultimately tracing back to the historical introduction of the name. The speaker need not have accurate beliefs — reference is a social and historical phenomenon, not a matter of individual mental content. This is the radical anti-descriptivist conclusion: even a speaker who believes almost nothing true about Aristotle successfully refers to him, because their use is connected to the right historical chain. Option A is the descriptivist position Kripke argues against."

- question: "What is the 'qua problem' and why does it show that pure causal theories of reference are incomplete?"
  type: multiple-choice
  options:
    - "The qua problem is that causal chains degrade over time, so historical reference becomes uncertain"
    - "When a name is introduced by pointing at an object, the causal chain alone doesn't fix what kind of thing is named — this gold ring, this ring, this piece of gold, this material object — so some descriptive content is needed to determine the extension"
    - "The qua problem shows that causal theories cannot account for reference to abstract objects like numbers"
    - "Causal chains require physical contact, which rules out reference to past individuals"
  answer: 1
  explanation: "The qua problem: when you introduce 'Goldie' by pointing, the pointing gesture is compatible with naming this individual ring, this instance of gold, this ring-shape, this material object, and so on. The causal chain runs from this object, but which aspect of the object? Without some descriptive constraint specifying 'we're naming this as a piece of gold' or 'as an individual ring,' the extension is indeterminate. Mixed theories respond by holding that reference needs both a causal anchor (the pointing) and a minimal description of kind membership ('as a K') to fully determine what is referred to."

- question: "According to Kripke's descriptivist opponents (Frege and Russell), a name like 'Aristotle' refers to whatever individual uniquely satisfies the descriptions associated with it — such as being the teacher of Alexander and the student of Plato."
  type: true-false
  answer: true
  explanation: "This correctly characterizes the descriptivist position that Kripke argues against. For descriptivists, names function as abbreviated descriptions: 'Aristotle' means something like 'the individual who taught Alexander, studied under Plato, and wrote the Nicomachean Ethics.' Reference is determined by description-satisfaction. Kripke's modal argument against this — we can coherently imagine Aristotle existing without satisfying any of these descriptions — is meant to show that names are rigid designators that track individuals across counterfactual situations rather than description-satisfiers."

- question: "On Putnam's semantic externalism, two people with identical internal mental states could be using the word 'water' to refer to different substances."
  type: true-false
  answer: true
  explanation: "This is Putnam's Twin Earth thought experiment. On a duplicate Earth where 'water' picks out a superficially identical but chemically different substance (XYZ instead of H₂O), a person and their molecule-for-molecule duplicate would use 'water' in the same mental state but refer to different things. Since what their word 'water' refers to is determined by what substance in their actual environment they and their community are causally connected to, identical internal states can yield different reference. Meaning, in Putnam's slogan, 'ain't in the head.'"

- question: "What does it mean for a name to be a 'rigid designator,' and why does this property create a problem for description theories of reference?"
  type: short-answer
  answer: "A rigid designator refers to the same individual in every possible world where that individual exists. 'Aristotle' is a rigid designator: it refers to Aristotle in every counterfactual scenario — even worlds where he never taught philosophy, never wrote anything, and died as an infant. A description like 'the teacher of Alexander' is not a rigid designator: in a world where Plato taught Alexander instead, 'the teacher of Alexander' refers to Plato. So if 'Aristotle' meant 'the teacher of Alexander,' then 'Aristotle is the teacher of Alexander' would be necessarily true — but it isn't; it could easily have been false. This modal argument shows names cannot be disguised descriptions."
  explanation: "Rigidity is Kripke's central technical concept in the modal argument against descriptivism. The key observation is that names behave differently from descriptions when we reason about counterfactual situations. 'Aristotle could have been a farmer' is true; 'the teacher of Alexander could have been a farmer' is also true but could be talking about a different person. Rigid designators fix their referent and then range over possible worlds asking questions about that individual; non-rigid designators (definite descriptions) pick out whoever happens to satisfy them in the world under discussion, which may vary. This difference reveals that names and descriptions have fundamentally different semantic behavior."
```

## Explainer

From Kripke's causal theory of naming, you know that proper names are **rigid designators** — they refer to the same individual in every possible world — and that reference is fixed not by descriptions associated with the name but by an initial *baptism* followed by a historical chain of use that preserves reference across speakers and generations. From Putnam's semantic externalism, you know that meaning "ain't in the head": what our natural kind terms refer to is determined partly by facts about the external environment, not solely by internal mental states. Reference determination theory asks: given these insights, what is the general account of how expressions latch onto the world?

The crucial negative insight from both Kripke and Putnam is that reference is not description-satisfaction. The traditional view (associated with Frege and Russell) held that a name refers to whatever uniquely satisfies the descriptions associated with it: "Aristotle" refers to whoever was the teacher of Alexander, the student of Plato, the author of the *Nicomachean Ethics*. Kripke showed this cannot be right: we can coherently imagine a world where Aristotle existed but none of those descriptions apply to him — perhaps he died young — and we would still be talking about Aristotle. The name tracks the individual, not the cluster of descriptions. But this generates a puzzle: *how* does the name track the individual across counterfactual situations and across generations of speakers who never encountered the referent?

The **causal-historical chain** is Kripke's answer: reference is introduced in an initial baptism (ostensive or descriptive) and transmitted through a chain of social practice. Each subsequent speaker borrows reference from those they learned the name from, ultimately tracing back to the original introduction. Individual speakers need not have accurate beliefs about the referent — you can use "Aristotle" correctly while believing almost nothing true about him — because reference is determined by community practice, not individual mental content. Putnam extends this to **natural kind terms** like "water," "gold," and "tiger": these refer to whatever shares the underlying nature (microstructure, essential properties) of the paradigm cases used in the original introduction, regardless of what any speaker believes about that nature. Experts and the world together fix what the term refers to; the ordinary speaker defers to them.

Modern accounts combine these insights while addressing their limits. Pure causal accounts face the **qua problem**: when you introduce the name "Goldie" by pointing at a particular object, what exactly have you named — this ring? this gold? this material object? The causal chain alone doesn't fix the extension; some descriptive content is needed to determine what kind of thing is being referred to. **Mixed theories** hold that reference is anchored by causal contact with a paradigm and constrained by a minimal description of kind membership. This is why reference determination builds naturally toward natural kinds and essence: fixing the reference of a natural kind term requires a theory of what makes something a member of that kind, which is itself a substantive metaphysical question about the deep structure of reality.
