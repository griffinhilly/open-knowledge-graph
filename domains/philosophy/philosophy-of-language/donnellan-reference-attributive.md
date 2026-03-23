---
id: donnellan-reference-attributive
title: Donnellan's Referential-Attributive Distinction
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: russell-definite-descriptions
  type: hard
- id: kripke-causal-theory-naming
  type: soft
builds-toward:
- context-dependence-utterance
tags:
- reference
- use
- descriptions
- context
stage: formal-systems
status: validated
---

# Donnellan's Referential-Attributive Distinction

## Core Idea
Donnellan distinguished how definite descriptions can be used either referentially (to talk about a specific individual regardless of their actual properties) or attributively (to talk about whoever has certain properties). This distinction shows that the same sentence can have different truth conditions depending on speaker intent, suggesting that semantic content depends partly on context of utterance in ways classical theories miss.

## How It's Best Learned
Use Donnellan's cases: someone points at an innocent person and says "The murderer is tall" intending to refer to the person they see (who isn't the actual murderer). Attributively, the sentence would be false; referentially, it's true. Practice identifying which use is at play in examples, then examine how Russell's theory and intentionalism each handle the distinction.

## Common Misconceptions
- Thinking the referential use shows descriptions don't have their logical form; Russell can accommodate it via pragmatics.
- Confusing speaker-reference with semantic reference; Donnellan's point is about actual use, not necessarily what semantics delivers.
- Assuming attributive use is the 'real' logical meaning; both uses are legitimate speech acts.

## Questions

```yaml
- question: "Smith points at Jones at a party and says 'The man drinking champagne is a philosopher,' but Jones is actually drinking tonic water. Using Donnellan's distinction, what is the most accurate analysis?"
  type: multiple-choice
  options:
    - "Smith's statement is false because Jones is not drinking champagne, so the description fails"
    - "Smith used the description referentially — successfully referring to Jones despite the inaccurate description — and the statement is true if Jones is a philosopher"
    - "Smith used the description attributively, meaning whoever is actually drinking champagne at the party is a philosopher"
    - "The statement lacks a truth value because the description fails to apply to anyone"
  answer: 1
  explanation: "In the referential use, the description serves as a conversational vehicle for identifying a specific individual the speaker has in mind. Smith intends to talk about Jones; the description 'man drinking champagne' is just the means of pointing him out. If Jones is a philosopher, the statement is communicatively successful — Smith said something true about Jones even though the description was inaccurate. In the attributive use (option C), the description must correctly apply for reference to occur."

- question: "A philosophy student argues: 'Donnellan's distinction proves Russell's theory of descriptions is simply wrong.' A more careful response would be:"
  type: multiple-choice
  options:
    - "Donnellan's distinction proves that both Russell and Frege were correct about descriptions"
    - "Russell could accommodate the referential use via pragmatics: semantic content (what the sentence means) can diverge from speaker meaning (what the speaker intends), and the referential use is a pragmatic phenomenon, not a counterexample to the semantics"
    - "Donnellan's distinction only applies to fictional contexts, not everyday speech"
    - "Russell's theory was never meant to account for cases where descriptions happen to be inaccurate"
  answer: 1
  explanation: "The Gricean/Kripkean response is that the referential use exploits a semantic description for pragmatic purposes. The Russellian semantic analysis still applies to what the sentence *means*; what varies is speaker meaning — what the speaker *intends* to communicate. The distinction between semantic reference and speaker reference preserves Russell's semantics while acknowledging that use outstrips semantic content. Donnellan showed language use is richer than logical form, not that the logical form is wrong."

- question: "In an attributive use of a definite description, if no one actually satisfies the description, the speaker's statement refers to no one and has no subject."
  type: true-false
  answer: true
  explanation: "In the attributive use, the description's role is to pick out whoever has the relevant properties — the reference is description-governed. If the detective says 'The murderer is insane' and the death was accidental (no murderer exists), the statement has no subject: it applies to whoever is the murderer, and there is no such person. This contrasts with the referential use, where the speaker has a specific person in mind and successfully refers to them even if the description is inaccurate."

- question: "Donnellan's referential-attributive distinction shows that the meaning of a sentence is fully determined by the speaker's intent at the moment of utterance."
  type: true-false
  answer: false
  explanation: "Donnellan's distinction actually highlights the *gap* between semantic content (the sentence's meaning, determined by linguistic convention) and speaker meaning (what the speaker intends to communicate). The same sentence has the same semantic content whether used referentially or attributively — what changes is the speaker's purpose and the context. The point is not that intent determines meaning, but that intent creates a dimension of communicative use that semantic content alone cannot capture."

- question: "Explain the difference between the attributive and referential use of a definite description, using an example."
  type: short-answer
  answer: "In the attributive use, 'the F' means whoever actually has property F — the description does its full descriptive work. Example: a detective who says 'The murderer is insane' without a suspect in mind means whoever turns out to have committed the crime. In the referential use, the speaker uses 'the F' to pick out a specific individual they have in mind, and successful reference doesn't depend on that person actually being F. Example: someone pointing at an innocent person says 'The murderer must be clever' — they mean that person, not whoever actually committed the crime."
  explanation: "Attributive uses are description-governed: truth conditions depend on who actually satisfies the description, and if no one does, reference fails. Referential uses are person-governed: truth conditions depend on the individual the speaker intends to pick out, and successful reference doesn't require the description to apply accurately. The same sentence can have different truth conditions depending on which use is at play — which is the key evidence that semantic content alone underdetermines what a speaker is talking about."
```

## Explainer

Russell's theory of definite descriptions gives a powerful analysis of expressions like "the murderer." On Russell's account, "The murderer is insane" means roughly: there is exactly one person who committed the murder, and that person is insane. The description does not *refer* to anyone directly — it makes a quantified claim. You know this analysis well. Keith Donnellan's 1966 paper "Reference and Definite Descriptions" challenged this picture not by refuting Russell's logic but by showing that language use outruns logical form in an important way.

Donnellan distinguished two uses of a definite description. In the **attributive** use, the speaker intends to talk about *whoever* satisfies the description — the description's role is to pick out the object that fits. If a detective sees a bloody corpse and says "The murderer is insane" without knowing who committed the crime, she is using the description attributively: she means whoever turns out to be the murderer. If it emerges that no one committed a murder (the death was accidental), her statement doesn't apply to anyone. In the **referential** use, the description is used to refer to a *specific individual* the speaker has in mind, and the description serves merely as a means of identifying that person in the conversational context. If Smith points at Jones at a party and says "The man drinking a martini is a philosopher," Smith refers to Jones — even if Jones is actually drinking tonic water. The success of reference doesn't depend on Jones actually satisfying the description.

The referential/attributive distinction reveals a gap between **semantic content** (what the sentence means as a matter of linguistic convention) and **speaker meaning** (what the speaker intends to communicate). In the referential case, the speaker successfully refers to Jones even though the Russellian analysis delivers the "wrong" answer about who the sentence concerns. This is where the puzzle bites. Does this show Russell's theory is incorrect? Or just incomplete as an account of use? Russell himself might respond (and Grice later articulated this in detail) that what the speaker means can diverge from what the sentence *means* — the referential use is a case of pragmatic deviation from semantic content, not a counterexample to the semantics. Kripke's own response follows this line: the referential use exploits a semantic description for pragmatic purposes, but the underlying semantic mechanism is still Russellian.

The deeper lesson is that context of utterance partly determines what a speaker is talking about in ways that semantic content alone cannot capture. This connects forward to broader debates about context-dependence in language: indexicals ("I", "here", "now"), demonstratives ("this", "that"), and referential uses of descriptions all suggest that meaning cannot be read off the sentence in isolation from the situation in which it is uttered. Donnellan's distinction is often cited as one of the key moments that pushed philosophy of language toward a more thoroughly pragmatic and context-sensitive picture of how language works.
