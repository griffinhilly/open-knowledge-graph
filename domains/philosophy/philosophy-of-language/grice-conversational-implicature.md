---
id: grice-conversational-implicature
title: Grice's Theory of Conversational Implicature
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: meaning-and-reference-basics
  type: hard
builds-toward:
- grice-cooperative-principle-maxims
- speaker-meaning
- pragmatics-semantics-boundary
tags:
- Grice
- implicature
- pragmatics
- meaning
stage: abstract-reasoning
status: validated
---

# Grice's Theory of Conversational Implicature

## Core Idea
Grice distinguished between what an utterance literally says (semantic meaning) and what a speaker implicates or suggests by saying it (pragmatic meaning). 'Can you pass the salt?' literally asks about ability but implicates a request. Implicatures arise from the assumption that speakers are cooperative and follow rational principles. They are cancelable ('I'm asking literally') and detachable (other formulations can carry the same implicature), distinguishing them from literal meaning.

## How It's Best Learned
Study classic examples: 'A is a good dancer' (implicating A is not good at other things), 'X went to the bathroom' in response to 'What happened to X?' (implicating X is unavailable). See how implicatures depend on shared assumptions and can be canceled without contradiction.

## Common Misconceptions
Implicatures are vague suggestions—they are precisely calculable from semantic content and conversational principles. All implicatures are the same—Grice distinguished conventional implicatures (non-cancelable) from conversational implicatures.

## Questions

```yaml
- question: "Someone asks 'How is Sarah doing in her new teaching job?' and the reply is 'She has excellent classroom management.' According to Grice's framework, what is the most likely implicature?"
  type: multiple-choice
  options:
    - "Sarah is an outstanding teacher in every respect"
    - "Sarah struggles with teaching beyond keeping order in the classroom"
    - "The speaker does not know anything else about Sarah's performance"
    - "Classroom management is the most important skill for a teacher"
  answer: 1
  explanation: "The maxim of Quantity requires a speaker to say enough. By offering only 'excellent classroom management' when asked about overall performance, the speaker implicates that this is all that can be said in Sarah's favor — that she is not performing well in other dimensions of teaching. This is the key mechanism: the hearer reasons that a cooperative speaker who had better news to give would have given it, so the limited praise implies a limitation. This is not stated — it is calculated from the gap between what was said and what the question required."

- question: "A speaker says 'He has excellent handwriting — and actually, he's also the top performer on our team; I just mentioned the handwriting as one specific strength.' Which property of conversational implicature does this demonstrate?"
  type: multiple-choice
  options:
    - "Calculability — the implicature was logically derived from the context"
    - "Cancelability — the implicature is blocked without any contradiction"
    - "Conventionality — the word 'handwriting' conventionally implies limited praise"
    - "Relevance — the speaker's addition satisfies the maxim of Relation"
  answer: 1
  explanation: "Cancelability is the defining diagnostic for conversational implicature: you can add a clause that blocks the inferred meaning without contradicting anything previously said. The original sentence implied 'this is all good to say about him,' but the added clause removes that inference without creating a logical contradiction. This distinguishes implicature from entailment — you cannot cancel an entailment. 'John is a bachelor' entails 'John is unmarried'; no added clause can block that without contradiction."

- question: "Conversational implicatures are cancelable without contradiction, which distinguishes them from logical entailments."
  type: true-false
  answer: true
  explanation: "Cancelability is Grice's key diagnostic for identifying conversational implicatures. An implicature can be blocked by adding a clause that removes the inferred meaning without any contradiction: 'He has neat handwriting — and he's actually quite skilled overall, I just mentioned the handwriting as one example.' Entailments cannot be canceled this way: you cannot say 'John is a bachelor, but he is married' without contradiction. This asymmetry is what shows implicatures are pragmatic inferences, not logical consequences of the literal content."

- question: "When a speaker's utterance appears to violate the maxim of Quantity by saying too little, the hearer's natural inference is that the speaker has failed at communication."
  type: true-false
  answer: false
  explanation: "This reverses the Gricean mechanism. When apparent maxim violation occurs, the hearer does not conclude the speaker has failed — they infer the speaker is exploiting the maxim to communicate something beyond the literal content. The assumption of cooperation is preserved: the hearer reasons that a cooperative speaker who appeared to say too little must be conveying that the extra content is unavailable or unfavorable. The apparent violation is the signal that extra meaning is being communicated, not evidence of communicative breakdown."

- question: "A colleague asks how a candidate performed in a programming interview, and you say 'She arrived on time and was very professional.' Explain how Grice's framework allows a listener to derive an implicature from this, and explain why the derived meaning is cancelable."
  type: short-answer
  answer: "The maxim of Quantity requires saying enough to satisfy the conversational purpose. Evaluating a programming candidate requires addressing coding skill, problem-solving, and technical knowledge — the response says nothing about any of these. A cooperative speaker with positive technical feedback would have provided it, so the hearer infers the speaker is implying the candidate's technical performance was not good. The implicature is cancelable because one could add 'and her technical skills were also exceptional — I just wanted to note the professionalism first' without any contradiction arising."
  explanation: "The calculation runs: 'The speaker is cooperative; what they said is far less than what the question requires; to maintain the assumption of cooperation, the speaker must be conveying that nothing better can be said about technical ability; therefore the candidate likely performed poorly technically.' Cancelability holds because this conclusion is a pragmatic inference, not a logical entailment of the words used."
```

## Explainer

You already know the basics of meaning and reference: words have semantic content, sentences express propositions, and those propositions have truth conditions. But the gap between what sentences literally say and what speakers actually communicate is enormous. Grice's theory of **conversational implicature** is the main philosophical account of how that gap is bridged — how we routinely communicate far more than we literally say, and how this extra content is nevertheless rationally recoverable.

The foundation is the **Cooperative Principle**: we assume that speakers are making their contribution "such as is required, at the stage at which it occurs, by the accepted purpose or direction of the talk exchange." From this general principle, Grice derives four **maxims**: Quantity (say enough, don't say too much), Quality (don't say what you believe to be false or for which you lack evidence), Relation (be relevant), and Manner (be clear, brief, orderly). These maxims are not arbitrary conventions — they reflect rational norms that make communication efficient and trustworthy. When a speaker appears to violate a maxim, the hearer doesn't simply conclude the speaker has failed; they infer that the speaker is *exploiting* the maxim to communicate something beyond the literal content.

Here is the mechanism of implicature calculation. Someone asks, "How is John doing at his new job?" and the response is, "He has excellent handwriting." The literal content is entirely true and relevant-ish — but obviously insufficient as an answer to the question. The hearer reasons: the speaker is being cooperative; the speaker's literal statement says nothing useful about how John is doing at his job; to maintain cooperation, the speaker must be conveying that this is all that can be said in John's favor. The **implicature** is that John is not doing well. This conclusion is not entailed by the literal words — it is calculated from the assumption of cooperation plus the evident gap between what was said and what was needed.

The two key diagnostic properties of conversational implicatures are **cancelability** and **calculability**. An implicature is **cancelable**: you can add a clause that blocks it without contradiction. "He has excellent handwriting — and actually he's doing very well overall, I just mentioned the handwriting as one specific strength." Nothing has been contradicted; the implicature was defeasible. This is what distinguishes implicature from entailment: "John is a bachelor" entails "John is unmarried" — you can't coherently add "but he is married." By contrast, **calculability** means implicatures are not vague hunches but reasoned inferences derivable from the maxims plus context. You can reconstruct the chain of reasoning that gets you from the literal utterance to the communicated content.

Grice also distinguished **conventional implicature** — meaning attached to specific words by convention rather than conversational reasoning. "But" in "she is rich but generous" conventionally implicates a contrast between wealth and generosity, even though this contrast is not part of what is strictly asserted. Unlike conversational implicatures, conventional implicatures are not cancelable — they are part of the word's meaning. This distinction matters enormously for philosophy of language: it shows that word meaning is not just truth-conditional content but also includes what the word *implies* in a conventional, non-truth-conditional way. Grice's framework opened up the systematic study of pragmatics — the way context, intention, and rational assumption shape what is communicated — and it remains the starting point for any serious investigation of how language functions in use.
