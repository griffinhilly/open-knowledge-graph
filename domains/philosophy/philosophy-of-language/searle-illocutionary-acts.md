---
id: searle-illocutionary-acts
title: Searle's Illocutionary Force and Speech Acts
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: austin-speech-acts
  type: hard
builds-toward:
- speaker-meaning
- pragmatics-semantics-boundary
- grice-cooperative-principle-maxims
tags:
- Searle
- illocutionary-acts
- speech-acts
- force-and-content
stage: abstract-reasoning
status: validated
---

# Searle's Illocutionary Force and Speech Acts

## Core Idea
Searle refined and systematized Austin's speech act theory, introducing the concept of illocutionary force—the kind of act performed by an utterance (asserting, questioning, commanding, promising). He distinguished between the propositional content (what) and the illocutionary force (what kind of act). Searle argued that speech acts have structural rules and conditions of satisfaction, and that understanding utterances requires grasping their illocutionary force, not just their semantic content.

## How It's Best Learned
Study a single sentence with different illocutionary forces ('Close the door!' vs. 'Will you close the door?' vs. 'You will close the door.') to see that propositional content and illocutionary force are independent. Classify speech acts by their conditions of satisfaction.

## Common Misconceptions
Illocutionary force is always marked grammatically—many languages perform the same illocution with identical syntax and rely on context. Speech acts are only for performance contexts—all assertion, reference, and predication are speech acts.

## Questions

```yaml
- question: "The utterances 'You will close the door,' 'Close the door!' and 'Will you close the door?' all involve the same state of affairs. According to Searle, how do they differ?"
  type: multiple-choice
  options:
    - "They have different propositional contents — each describes a different action or event"
    - "They have the same propositional content but different illocutionary forces: prediction, command, and question/request respectively"
    - "They have different perlocutionary acts but identical illocutionary acts"
    - "They differ only in politeness level, not in any philosophically significant way"
  answer: 1
  explanation: "This is Searle's central example illustrating the F(p) structure. All three utterances have the same propositional content p — they are all about the same state of affairs (someone closing the door). What differs is F, the illocutionary force: the first asserts/predicts, the second commands, the third requests. The content and the kind of act are independent — the same 'what' can be wrapped in different 'what kind of act' packages."

- question: "A linguist argues that 'Close the door!' and 'Will you close the door?' perform completely different speech acts because they have different grammatical forms. Searle's framework shows this conclusion is:"
  type: multiple-choice
  options:
    - "Correct — Searle holds that illocutionary force is always determined by grammatical form (indicative, imperative, interrogative)"
    - "Correct for these examples, but wrong in general — grammar determines force in English but not in all languages"
    - "Misleading — both utterances can function as directives (attempts to get the hearer to close the door); illocutionary force is not always readable from syntax alone"
    - "Correct — imperatives are always commands and interrogatives are always questions, so these are categorically different acts"
  answer: 2
  explanation: "Searle explicitly identifies as a misconception the idea that illocutionary force is always grammatically marked. 'Will you close the door?' is interrogative in form but typically functions as a directive (a request), not a genuine question about the hearer's future behavior. Context, not syntax, is often the primary force indicator. The linguist's grammatical reading misses the actual speech act being performed."

- question: "According to Searle, making a sincere assertion creates a normative commitment: the speaker is accountable for the truth of what they asserted."
  type: true-false
  answer: true
  explanation: "Searle argues that illocutionary acts generate normative commitments tied to their conditions of satisfaction. An assertive is satisfied if the proposition is true — and to sincerely assert something is to commit yourself to its truth. This is why lying is a violation: it involves asserting while knowing the conditions of satisfaction are not met. Speech acts are not merely descriptions; they create obligations and expectations between speakers."

- question: "Illocutionary force is typically overtly marked by the grammatical mood of the sentence — you can usually identify the force from the syntax."
  type: true-false
  answer: false
  explanation: "This is one of the misconceptions Searle's framework addresses. Many illocutionary acts are performed with syntax that does not directly signal the force. 'It's cold in here' can be an assertion, a complaint, or an indirect request to close the window — same syntax, different forces depending on context. Illocutionary force indicators are often implicit, and recovering the intended force requires pragmatic reasoning about speaker, hearer, and situation."

- question: "Using Searle's F(p) structure, explain why two sentences with the same propositional content can perform entirely different speech acts. Give an example."
  type: short-answer
  answer: "In Searle's framework, an illocutionary act has the structure F(p): F is the illocutionary force (the kind of social act being performed) and p is the propositional content (what the act is about). Because F and p are independent, the same p can appear under different forces. For example, 'You'll submit the report by Friday' can be an assertion/prediction (F = assertive, speaker predicts the hearer's behavior), a directive (F = directive, speaker commands submission), or a threat (F = commissive, with consequences implied) — all with the same propositional content about a report being submitted by Friday. What differs is the normative relationship created and the conditions of satisfaction required."
  explanation: "The F(p) separation is Searle's key theoretical contribution over simply cataloguing speech acts. It reveals the systematic structure underneath the apparent diversity of what we do with words: a finite set of forces can be applied to any propositional content, generating a combinatorial space of possible speech acts. Understanding this structure allows analysis of any utterance by asking: what is the force, what is the content, and what conditions would satisfy this act?"
```

## Explainer

From Austin's speech act theory, you know that utterances do things: they assert, promise, warn, declare, apologize. Austin distinguished the **locutionary act** (saying something with a meaning), the **illocutionary act** (performing a social action in saying it), and the **perlocutionary act** (producing an effect on the listener). Searle took this framework and gave it systematic structure — moving from Austin's taxonomy of examples to a theory of what illocutionary acts fundamentally are and how they work.

Searle's central move was to separate **propositional content** from **illocutionary force**. Consider three utterances: "You will close the door," "Close the door!" and "Will you close the door?" All three have the same propositional content — they are all about the same state of affairs, namely you closing the door. What differs is the illocutionary force: the first is a prediction or assertion, the second a command, the third a question or request. This separation is not cosmetic — it reveals that the same content can be packaged in radically different kinds of social acts. Searle introduced the **force indicator** (F) and **propositional content indicator** (p) to formalize this: an illocutionary act has the structure F(p), where F specifies the kind of act and p specifies what it is about.

Searle also argued that illocutionary acts have **conditions of satisfaction** — conditions that must hold for the act to succeed or be fulfilled. An assertion is satisfied if the proposition asserted is true. A promise is satisfied if the speaker performs the promised action. A question is satisfied if the hearer provides the requested information. This framework explains why illocutionary acts generate normative commitments: to assert sincerely is to commit yourself to the truth of what you asserted; to promise is to incur an obligation. Language is not just a channel for information — it is a mechanism for creating normative relationships between speakers.

Searle classified illocutionary acts into five broad categories: **assertives** (committing the speaker to the truth of a proposition), **directives** (attempting to get the hearer to do something), **commissives** (committing the speaker to a future action), **expressives** (expressing a psychological state), and **declarations** (changing the world by saying something, like "I hereby declare you married"). This taxonomy is powerful because it shows that illocutionary diversity is not chaos — underlying the variety of things we do with words is a small number of fundamental relationships between speaker, hearer, and world. Understanding Searle's framework equips you to analyze any utterance: what is the propositional content? What kind of act is being performed? What conditions would satisfy it? And what normative commitments does the speaker thereby incur?
