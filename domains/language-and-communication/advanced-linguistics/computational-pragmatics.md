---
id: computational-pragmatics
title: Computational Pragmatics
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: pragmatic-implicature-context
  type: hard
builds-toward:
- language-and-artificial-intelligence
tags:
- pragmatics
- computational-linguistics
- NLP
- implicature
- context
stage: expert
status: validated
---
# Computational Pragmatics

## Core Idea
Computational pragmatics applies computational methods to pragmatic phenomena: modeling how context determines meaning, how implicatures are computed, how speakers vary utterances relative to audience and context, and how irony, metaphor, and indirect speech acts are processed. This bridges formal pragmatics, cognitive modeling, and NLP. Systems must model shared knowledge, discourse structure, and common ground — challenging problems in AI because they require representing complex, dynamic context.

## How It's Best Learned
Study computational models of implicature computation (e.g., Rational Speech Acts framework). Examine NLP systems for indirect request recognition, sarcasm detection, and pragmatic inference. Learn how language models capture pragmatic intuitions. Understand limitations of current systems in context-dependent tasks. Explore questions: How are alternatives modeled? How do systems represent common ground? What pragmatic phenomena are computational tractable vs. intractable?

## Common Misconceptions
- Thinking pragmatics is too context-dependent for formal modeling; computational frameworks show surprising tractability.
- Assuming language models automatically capture pragmatics; most successful pragmatic phenomena modeling requires explicit context mechanisms.

## Questions

```yaml
- question: "The challenge of modeling scalar implicatures computationally is that:"
  type: multiple-choice
  options:
    - "Implicatures are purely subjective and cannot be formalized"
    - "Computing implicatures requires representing and reasoning about alternatives, speaker rationality, and listener expectations — all context-dependent and computationally complex"
    - "Implicatures appear only in speech, not written language"
    - "Implicatures are not meaningful phenomena"
  answer: 1
  explanation: "Scalar implicatures (e.g., 'some' implicating 'not all') require reasoning about alternatives and rational speaker behavior. Computational models must represent all logically stronger alternatives, compute listener beliefs about speaker rationality, and infer what the speaker intended to communicate. This is formally tractable but computationally complex, especially with multi-level reasoning."

- question: "Why is modeling common ground (shared knowledge between speaker and listener) critical for computational pragmatics?"
  type: multiple-choice
  options:
    - "Because pragmatics is about grammar, not context"
    - "Because implicatures, reference resolution, and contextual interpretation all depend on what speaker and listener know and believe is known in common"
    - "Because common ground is unchanging and predetermined"
    - "Because pragmatics is irrelevant to understanding meaning"
  answer: 1
  explanation: "Common ground (or context) affects interpretation profoundly. 'It's raining' is a casual observation if the listener sees the rain; it's a warning if the listener doesn't. Pronouns, demonstratives, indirect speech acts, and implicatures all depend on common ground. Systems must track and update common ground dynamically."

- question: "Language models like GPT demonstrate human-level pragmatic competence because they match human judgments on pragmatic inference tasks."
  type: true-false
  answer: false
  explanation: "Language models show impressive performance on some pragmatic tasks (sarcasm detection, indirect request recognition) but often lack deep pragmatic understanding. They capture surface patterns from training data but may not truly compute pragmatic inferences. When context is novel or reasoning is multi-step, models often fail. They're useful tools but not full solutions."

- question: "Modeling sarcasm computationally is fundamentally impossible because sarcasm is fundamentally subjective and context-dependent."
  type: true-false
  answer: false
  explanation: "While sarcasm is context-dependent, computational models have made progress. Sarcasm often involves a contrast between literal and expected meaning; models can learn these patterns. Detection accuracy is lower than literal speech, but not chance. Computational approaches to sarcasm are imperfect but meaningful and improving."

- question: "Explain why the Rational Speech Acts framework is useful for computational pragmatics and what it models."
  type: short-answer
  answer: "The RSA framework models pragmatic meaning through recursive reasoning: the speaker chooses utterances that are informative and relevant given rational listener inference; the listener infers the speaker's intent given rational speaker behavior. Computationally, this involves computing alternatives, reasoning about listener beliefs, and iteratively refining both. It provides a formal, tractable framework for implicature and context effects."
  explanation: "RSA bridges pragmatic theory and computation. It makes formal assumptions explicit and tractable, enabling modeling of empirical phenomena. Iterations of reasoning (speaker reasoning about listener expectations, listener reasoning about speaker rationality) capture how pragmatic meaning emerges."
```

## Explainer

**Pragmatics** studies how context determines meaning — how the same utterance "It's cold" means different things depending on whether you're in a freezing car or a cool room, whether you're asking for a sweater or complaining about the air conditioning. Traditional linguistics has often sidelined pragmatics as too context-dependent for formal study, but **computational pragmatics** shows that context effects are partially formalizable and computationally tractable.

Several core problems in computational pragmatics:

**Implicature computation**: When a speaker says "Some students passed," listeners infer "Not all students passed" (scalar implicature). Computationally, this requires enumerating alternatives ("Some," "All," "None"), reasoning about why the speaker chose the weaker alternative, and inferring the stronger meaning. This requires models of rationality and information structure — not trivial computationally.

**Reference resolution and common ground**: Pronouns and definite descriptions refer based on context. "It's raining; you should bring an umbrella" — the "it" refers to weather because context makes that salient. Computationally, systems must track discourse entities, their salience, and mutual knowledge. Systems that don't model common ground fail at reference.

**Indirect speech acts and context-dependent interpretation**: "Can you pass the salt?" is not a question about ability but a polite request. Interpretation depends on social context (formality, relationship), physical context (is the salt nearby?), and pragmatic reasoning (why would the speaker ask this?). Computational models must represent these contexts.

**Irony and sarcasm**: "Great job," said when someone makes a mistake, is sarcastic — it means the opposite. Detection requires recognizing that literal meaning contradicts expected context. Models can learn patterns (certain words + negative context → likely sarcasm) but real pragmatic understanding is deeper.

**The Rational Speech Acts (RSA) framework** provides one formalizable approach. The basic idea:
- The **speaker** chooses utterances that informatively communicate the intended meaning, given what they believe the listener will infer
- The **listener** interprets utterances by reasoning about what rational speaker would say given their beliefs
- This creates a loop of reasoning that resolves implicatures and contextual effects

Computationally, RSA requires:
1. Enumerate alternatives to the utterance
2. For each alternative, compute the probability a rational speaker would choose it
3. For each interpretation, compute how likely it is given speaker rationality
4. Iterate reasoning (listener reasons about speaker's reasoning about listener's reasoning...)

Modern **language models** (like GPT) learn pragmatic patterns from massive text, and they often perform well on pragmatic tasks. But there are limits: multi-step reasoning, novel contexts, and deep pragmatic understanding remain challenging. Models capture surface patterns but may not compute pragmatic meaning the way humans do.

The future of computational pragmatics involves:
- Better models of common ground and context
- Integration of pragmatic reasoning with formal semantics
- Handling of under-specified, ambiguous utterances
- Modeling of dialectal and register variation in pragmatic norms

Computational pragmatics shows that while pragmatics is context-dependent, it's not entirely intractable. Systematic models can formalize important aspects and make progress on real language understanding.
