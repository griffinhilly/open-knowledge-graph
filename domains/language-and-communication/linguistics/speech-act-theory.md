---
id: speech-act-theory
title: Speech Act Theory
domain: language-and-communication
course: linguistics
prerequisites:
- id: linguistic-pragmatics
  type: hard
builds-toward:
- conversational-implicature
- discourse-analysis
tags:
- speech acts
- Austin
- Searle
- illocution
- performatives
- indirect speech acts
stage: formal-systems
status: validated
---

# Speech Act Theory

## Core Idea
Speech act theory, developed by Austin and Searle, recognizes that utterances do not merely describe the world but perform actions. Austin distinguished locutionary acts (what is literally said), illocutionary acts (what is done in saying it — promising, warning, asserting), and perlocutionary acts (the effect produced in the hearer). Searle classified illocutionary acts into five types: assertives, directives, commissives, expressives, and declarations. Indirect speech acts occur when the literal and intended illocutionary force diverge (e.g., 'Can you pass the salt?' as a request, not a question about ability).

## How It's Best Learned
Collect examples of each illocutionary type and analyze the felicity conditions required for each to succeed. Work through indirect speech acts by asking what contextual reasoning licenses the non-literal interpretation.

## Common Misconceptions
- Performative utterances ('I hereby declare...') do not describe actions — they constitute them at the moment of utterance.
- Not all questions are requests for information; not all declaratives are assertions — illocutionary force underdetermines sentence form.
- Indirect speech acts are not dishonest or unclear; they are a normal, efficient, and face-saving feature of human communication.

## Questions

```yaml
- question: "A judge says 'I hereby sentence you to five years in prison.' Which of Searle's five illocutionary categories does this utterance belong to?"
  type: multiple-choice
  options: ["Assertive", "Commissive", "Directive", "Declaration"]
  answer: 3
  explanation: "Declarations are illocutionary acts that bring about the state of affairs they name — the sentencing is accomplished by the utterance itself, provided the judge has the institutional authority to perform it. Assertives describe an existing state; commissives commit the speaker to a future action; directives attempt to get the hearer to act."

- question: "When someone says 'Can you pass the salt?', the illocutionary force is a question about the hearer's physical ability to reach the salt."
  type: true-false
  answer: false
  explanation: "This is an indirect speech act: the literal locutionary content is an interrogative about ability, but the illocutionary force — what is actually done in saying it — is a directive, specifically a polite request. Speakers and hearers use contextual reasoning (Gricean principles, situational knowledge) to recover the intended illocutionary force from the literal form."

- question: "What is the difference between an illocutionary act and a perlocutionary act? Give an example that illustrates the distinction."
  type: short-answer
  answer: "An illocutionary act is what the speaker does in uttering words — the intended social action (warning, promising, asserting). A perlocutionary act is the effect produced in the hearer as a result. For example, saying 'The bridge is out' is an illocutionary act of warning; the hearer turning back is the perlocutionary effect. The illocutionary act is defined by the speaker's intention and felicity conditions; the perlocutionary effect depends on the hearer's response and may not occur."
  explanation: "Austin's three-way distinction matters because illocutionary acts are conventionally regulated (a promise counts as a promise if felicity conditions are met regardless of whether it changes behavior), whereas perlocutionary effects are contingent on the hearer's psychology and circumstances. Conflating them leads to confusing whether a communicative act succeeded with whether it had its intended impact."
```

## Explainer

You already know from pragmatics that meaning in context goes beyond what sentences literally say. Speech act theory sharpens this insight into a formal account of the different things language does. When Austin observed that some utterances — "I promise," "I now pronounce you married," "I hereby sentence you" — are not descriptions of actions but the performance of actions, he identified a puzzle: the standard truth-conditional view of meaning cannot capture what these utterances do, because asking whether "I promise to call you" is true or false misses the point entirely. The utterance is a promise, not a claim.

Austin's solution was to distinguish three layers in every utterance. The **locutionary act** is the act of saying something with literal sense and reference — the phonological and semantic content. The **illocutionary act** is what is done *in* saying it: promising, warning, asserting, asking, apologizing. The **perlocutionary act** is the effect produced *by* saying it in the hearer: being persuaded, being frightened, being informed. These three levels are analytically distinct. A single utterance ("There's a loose wire behind you") may be a locutionary act with a propositional content, an illocutionary act of warning, and a perlocutionary act of alarming the hearer — but whether the alarm is felt depends on the hearer, not the speaker.

Searle systematized illocutionary acts into five categories based on their direction of fit and sincerity conditions. **Assertives** commit the speaker to the truth of a proposition (claiming, concluding). **Directives** attempt to get the hearer to act (requesting, commanding, asking). **Commissives** commit the speaker to a future course of action (promising, offering). **Expressives** express the speaker's psychological state (thanking, apologizing, congratulating). **Declarations** bring about the state of affairs they name, contingent on the speaker's institutional authority (sentencing, firing, marrying). This last category captures Austin's original insight about performatives: declarations work not because they describe a pre-existing reality but because the institutional context gives the utterance the power to create one.

Indirect speech acts arise when the illocutionary force of an utterance diverges from its literal form. "Can you pass the salt?" has the syntactic form of a yes/no question (a directive for information), but virtually no one hears it as a sincere inquiry into motor ability. Contextual reasoning — including Gricean maxims you studied in pragmatics — licenses the move from the literal question to the intended request. Indirect speech acts are not evasive or confusing; they are pervasive and efficient, allowing speakers to make requests politely, reduce face threat, and leave the hearer room to decline gracefully.

A key practical concept is **felicity conditions** — the requirements that must be met for an illocutionary act to succeed. A promise requires that the speaker sincerely intends to do the thing, that the thing is possible, that the hearer would prefer it to be done, and that it is not already going to happen regardless. If any condition is violated, the speech act is infelicitous — not false, but defective. Understanding felicity conditions is what lets you see why "I promise I'll be rude to you" sounds odd (it violates the preference condition) and why authority matters so much for declarations.
