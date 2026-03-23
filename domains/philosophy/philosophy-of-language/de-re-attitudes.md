---
id: de-re-attitudes
title: De Re and De Dicto Attitudes
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: intentionality-aboutness
  type: hard
- id: philosophical-zombies
  type: soft
- id: first-order-logic-syntax
  type: soft
builds-toward:
- semantic-content-externalism
tags:
- attitudes
- reference
- intentionality
- quantification
stage: formal-systems
status: validated
---

# De Re and De Dicto Attitudes

## Core Idea
The de re/de dicto distinction matters for propositions involving objects and their properties. "John wants to marry a millionaire" (de dicto: he wants someone with money) differs from "John wants to marry that millionaire" (de re: about a particular individual). Understanding how attitudes relate to referential content is crucial for philosophy of mind and language, especially given externalism about content.

## How It's Best Learned
Use Quine's famous example: Ralph believes de dicto that a spy is a patriot, but de re (of the actual spy he sees), Ralph believes him to be a patriot. Practice translating English sentences into logical form, noting how quantifier scope and operator scope interact. Study Kaplan's semantics for de re attributions and how they depend on direct reference to objects.

## Common Misconceptions
- Thinking one reading is always correct; the same sentence often genuinely admits both readings.
- Confusing de re belief with having metalinguistic knowledge about someone's name.
- Assuming de re attitudes require only causal contact; they require the right kind of cognitive relation to the object.

## Questions

```yaml
- question: "Mary believes that whoever is tallest on the team will win the award. She has no particular person in mind — just whoever happens to satisfy that description. What kind of belief is this?"
  type: multiple-choice
  options:
    - "De re, because tallness is a real physical property of a specific individual"
    - "De dicto, because the belief is about whoever satisfies the description 'tallest player,' not about any particular individual"
    - "Neither, because beliefs about teams are always collective rather than individual"
    - "De re, because there is in fact a specific tallest player even if Mary doesn't know who it is"
  answer: 1
  explanation: "A de dicto attitude is directed at a description or proposition — here, 'whoever is tallest.' Mary's belief would be satisfied by any person who turns out to be the tallest; she is not thinking about a particular individual. The tempting wrong answer is D: even though a specific person happens to satisfy the description, Mary's belief is not anchored to that individual as an individual — it would transfer to a different person if the team roster changed. De re beliefs, by contrast, are anchored to a specific object regardless of how it is described."

- question: "Ralph has seen a man on the beach and believes him to be a pillar of the community. Unknown to Ralph, this man is a spy named Ortcutt. Which statement best describes Ralph's doxastic situation?"
  type: multiple-choice
  options:
    - "Ralph has de dicto beliefs about Ortcutt because he doesn't know Ortcutt's name"
    - "Ralph has de re beliefs about Ortcutt — his belief is about that particular individual, regardless of Ralph's ignorance of his name or identity"
    - "Ralph has no genuine beliefs about Ortcutt since they have never been formally introduced"
    - "Ralph's belief is neither de re nor de dicto because it is based on incomplete information"
  answer: 1
  explanation: "This is Quine's famous Ortcutt example. A de re belief is anchored to a specific individual — the res — rather than to how that individual is described. Ralph has perceived Ortcutt directly and formed a belief about him; the belief is about that particular person even though Ralph would not describe him as 'the spy Ortcutt.' Knowing someone's name is not required for de re belief — what matters is the right kind of direct cognitive relation to the individual. The tempting wrong answer is A: lack of metalinguistic knowledge (not knowing a name) does not reduce a de re belief to a de dicto one."

- question: "The de re/de dicto distinction can be formalized in first-order logic by the relative scope of the existential quantifier and the attitude operator: de dicto places the quantifier inside the operator's scope, while de re places it outside."
  type: true-false
  answer: true
  explanation: "This is the standard logical representation of the distinction. De dicto: John believes [∃x: x is a millionaire ∧ he marries x] — the quantifier is inside the scope of 'believes,' so the belief is about whatever description is satisfied. De re: ∃x: x is a millionaire ∧ John believes [he marries x] — the quantifier scopes outside 'believes,' so the belief is about a particular individual that exists in the domain. The scope difference captures the philosophical distinction precisely."

- question: "A de re attitude requires the believer to know the name or a correct identifying description of the object the belief is about."
  type: true-false
  answer: false
  explanation: "This is a common misconception. De re attitudes require the right kind of direct cognitive relation to the object — perception, acquaintance, tracking — not metalinguistic knowledge of names or descriptions. You can have a de re belief about someone you saw on the street without knowing their name. What matters, as Kaplan and others have argued, is that the belief is genuinely anchored to the individual as an individual, not to whatever satisfies some description. Knowing a name is neither necessary nor sufficient for de re belief."

- question: "Explain why the same English sentence can be genuinely ambiguous between a de re and a de dicto reading, and give an example illustrating the difference."
  type: short-answer
  answer: "Natural language attitude reports don't mark quantifier scope syntactically in a way that resolves the de re/de dicto distinction. A sentence like 'John wants to marry a millionaire' can mean (de dicto) that John wants it to be the case that whoever he marries is a millionaire, or (de re) that there is a particular millionaire John wants to marry. Both are grammatically available readings of the same sentence."
  explanation: "The ambiguity is not merely semantic slipperiness — it reflects a genuine philosophical distinction about how the attitude is directed. In the de dicto case, John's desire would be satisfied by any millionaire; if the woman he marries turns out not to be a millionaire, the desire is frustrated even if she's wonderful. In the de re case, John's desire is about Sarah specifically; whether she's a millionaire is incidental to the direction of the desire. The difference has implications for substitutivity, transparency, and content externalism."
```

## Explainer

From your study of intentionality and aboutness, you know that mental states and linguistic expressions can be **about** things — they have content that points toward objects or states of affairs in the world. The de re / de dicto distinction is a refinement of this: it asks *how* an attitude or statement is about its object, and specifically whether the object is picked out as a definite individual or merely as whatever satisfies a description.

Start with a concrete example. Suppose John wants to marry a millionaire, but he has no particular person in mind — he just wants whoever happens to have that much money. This is a **de dicto** attitude: John's desire is about the description "a millionaire," *dictum* being Latin for "what is said." Now suppose John is secretly in love with his neighbor Sarah, who (unknown to him) is a millionaire. John wants to marry *Sarah*. This is a **de re** attitude: his desire is about a specific *res* — a particular thing in the world — regardless of how he or anyone else describes it. De re attitudes are object-directed in a direct, referential way; de dicto attitudes are description-directed. The same English sentence — "John wants to marry a millionaire" — is often genuinely ambiguous between these two readings.

Your study of first-order logic syntax helps here. The de dicto reading of "John wants a millionaire wife" places the existential quantifier *inside* the scope of the attitude operator: John wants [there to exist an x such that x is a millionaire and he is married to x]. The de re reading places the quantifier *outside*: there exists an x such that x is a millionaire and John wants [to be married to x]. The difference in **quantifier scope** is the formal marker of the distinction. Quine's famous spy example illustrates the stakes: Ralph believes de dicto that someone is a spy (there is a spy somewhere). He believes de re of Ortcutt — a particular person he has seen — that Ortcutt is not a spy. But Ortcutt is in fact the spy. Does Ralph believe of the spy that he is not a spy? The de re reading says yes, because the belief is about Ortcutt the individual, not about Ortcutt under any description.

Why does this matter for philosophy of mind and language? Because **content externalism** — the view that the content of your thoughts is partly determined by what is in your environment, not just what is in your head — applies differently to de re and de dicto attitudes. A de re belief about water is a belief about H₂O whether or not the believer knows the chemical formula. A de dicto belief "I believe that water is wet" might have a different content in a **Twin Earth** scenario where the watery stuff has a different chemical composition. De re attitudes seem especially vulnerable to Putnam-style externalist arguments, because their content is anchored to the actual object of the belief, not the believer's internal description of it.

The deeper issue is what kind of cognitive relation is required for a genuinely de re attitude. It is tempting to say: all you need is causal contact with the object. But the right kind of cognitive grip seems to matter. You are causally connected to distant stars, but most philosophers would say you cannot have de re beliefs about a particular star unless you have some epistemic or referential access to it — through perception, testimony, proper names, or tracking. This is why Kaplan's semantics for de re attributions appeal to notions like **acquaintance**: a de re belief requires that the believer stand in the right kind of direct cognitive relation to the object, not merely that the object causally influenced them at some point. Working out precisely what that relation is connects this topic directly to your upcoming study of semantic content externalism.

