---
id: speech-act-content-and-force
title: Speech Act Content and Illocutionary Force
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: austin-speech-acts
  type: hard
- id: searle-illocutionary-acts
  type: hard
builds-toward:
- performative-utterances
- literal-meaning-speaker-meaning
tags:
- speech-acts
- illocution
- force
stage: advanced
status: draft
---

# Speech Act Content and Illocutionary Force

## Core Idea
Speech acts have both locutionary content (what is literally said) and illocutionary force (what the speaker is doing: asserting, commanding, questioning). The same content can be expressed with different forces, determined partly by syntactic mood and partly by context and intention.

## Questions

```yaml
- question: "During a faculty meeting, the department chair says to a junior professor, 'It would really be wonderful if everyone could submit their assessment reports by Friday.' What is the primary illocutionary act being performed?"
  type: multiple-choice
  options:
    - "An assertion about the chair's aesthetic preferences"
    - "A prediction about what will happen by Friday"
    - "An indirect directive — the chair is requesting or requiring the submission, using a polite declarative surface form"
    - "A performative declaration creating an official deadline"
  answer: 2
  explanation: "The sentence is grammatically a declarative expressing a hypothetical preference, but in the institutional context (department chair addressing junior faculty), the illocutionary force is clearly a directive — a request bordering on a requirement. The hearer recognizes that the literal force cannot be the primary force given who is speaking to whom about what, and infers the intended force via Gricean cooperation. This is Searle's indirect speech act: the surface form is a declarative; the real illocutionary act is a directive. Identifying only the surface form misses what is actually being communicated."

- question: "Consider 'Close the door,' 'Could you close the door?,' and 'The door is open.' In what sense can all three share a common illocutionary point while differing in propositional content and syntactic form?"
  type: multiple-choice
  options:
    - "They cannot share an illocutionary point — each sentence performs a different speech act by definition"
    - "In appropriate contexts, all three can function as requests (directives) — same force, different content and form"
    - "They share propositional content about the door but not illocutionary force"
    - "Only the imperative 'Close the door' can function as a request; the others cannot"
  answer: 1
  explanation: "The force/content distinction runs in both directions: the same content can carry different forces, but also different contents can carry the same force. In context, 'Close the door' (imperative, direct), 'Could you close the door?' (interrogative, indirect), and 'The door is open' (declarative, hint) can all function as requests to close the door. The propositional contents differ — closing commanded, ability questioned, door state described — but the illocutionary point (get the hearer to close the door) is shared."

- question: "The same propositional content — say, a proposition about a door being closed — can be expressed in speech acts with different illocutionary forces (command, request, question, assertion, wish)."
  type: true-false
  answer: true
  explanation: "This is the core of the force/content distinction. 'Close the door' (command), 'Will you close the door?' (request), 'Is the door closed?' (question), 'I assert that the door is closed' (assertion), and 'If only the door were closed!' (wish) all involve propositional content about door-closing but perform entirely different speech acts. The same proposition appears in radically different illocutionary acts. Force — what the speaker is doing — is a separate dimension from content — what the speech act is about."

- question: "Syntactic mood is a reliable indicator of illocutionary force: a declarative sentence always performs an assertion, an interrogative always asks a question, and an imperative always issues a command."
  type: true-false
  answer: false
  explanation: "Syntactic mood is a defeasible signal of force, not a guarantee. The most common counterexamples are indirect speech acts: 'Can you pass the salt?' is syntactically interrogative but functions as a request, not a question about ability. 'You will report to the office immediately' is syntactically declarative but functions as a command. 'I'd love it if you left' is declarative but functions as a request to leave. The relationship between linguistic form and communicative act is mediated by context, institutional roles, and shared knowledge — not simply read off from grammatical structure."

- question: "Explain how 'Can you pass the salt?' functions as a request rather than a question about the hearer's physical ability. What does this reveal about the relationship between syntactic form and illocutionary force?"
  type: short-answer
  answer: "The literal reading as a question about physical ability is almost always irrelevant at a dinner table. Searle's account: the hearer recognizes (1) the literal force is a yes/no question about ability, (2) a genuine question about ability would be odd given the context — the cooperative principle suggests the speaker must have a different purpose, (3) the most plausible purpose, given context (meal, proximity to salt, politeness norms), is a request to pass the salt. The hearer infers the intended illocutionary force (directive) by recognizing that the literal force fails to explain why the speaker would say this now. This reveals that syntactic mood is a default signal of force — defaults can be overridden by context, and real force is often inferred pragmatically."
  explanation: "Indirect speech acts are possible because communication operates at multiple levels simultaneously. The speaker 'says' one thing (asks about ability) and 'does' another (requests an action), and hearers navigate this via shared context and Gricean maxims. The force/content distinction is what makes this analysis possible — it separates what the sentence is about (the proposition) from what the speaker is doing (the act), and shows these can come apart."
```

## Explainer

From Austin and Searle, you know that utterances are not just truth-apt propositions—they are *acts*. When you say "I promise to return," you're not describing a promise; you're making one. The **illocutionary act** is what you are doing with language: asserting, promising, requesting, warning, commanding, congratulating. Every speech act has both a **propositional content**—what it is about—and an **illocutionary force**—what act is being performed with that content. These two dimensions are largely independent, and that independence is the central insight of this topic.

The same content can carry different forces. "You will close the door" can be an assertion (I'm telling you what will happen), a prediction (same content, slightly different epistemic stance), a command (I'm telling you to do it), or a performative declaration (in the right institutional context, I hereby mandate it). What changes is not the proposition about door-closing but the speech act being performed. Conversely, different contents can carry the same force: "Get out," "Would you please leave," "I'd appreciate your leaving," and "It's getting late" can all function as requests or indirect commands, with different propositional contents but the same illocutionary point.

**Syntactic mood** is the primary grammatical signal of force: declaratives default to assertions, interrogatives to questions, imperatives to commands. But mood is only a defeasible signal, not a guarantee. "Can you pass the salt?" is grammatically a question about your ability, but it functions as a request—an **indirect speech act**. Searle's account of indirect speech acts explains this via a two-step process: the hearer recognizes the literal force (a question), recognizes that it can't be the primary force given the context, and infers the intended illocutionary force (a request) by Gricean cooperation. Context—shared knowledge, institutional roles, tone, prior discourse—determines which inference to draw.

The force/content distinction matters practically because misreading it causes real communicative failures. A judge who hears "Would you like to approach the bench?" as a genuine question about preferences has misread the force. A student who hears "That's an interesting interpretation" as sincere praise rather than polite skepticism has misread the force. What makes speech act theory powerful is that it provides systematic tools—felicity conditions, force indicators, background institutional context—for diagnosing which act is being performed, even when the surface form is misleading. This is why the distinction between what is *said* (locutionary content) and what is *done* (illocutionary force) is foundational for any serious analysis of how language functions in real communicative contexts.
