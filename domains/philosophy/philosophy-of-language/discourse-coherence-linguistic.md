---
id: discourse-coherence-linguistic
title: Discourse Coherence and Rhetorical Relations
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: anaphora-and-discourse-dynamics
  type: hard
- id: pragmatics-semantics-boundary
  type: soft
builds-toward:
- meaning-convention-vs-intention
tags:
- discourse
- coherence
- pragmatics
stage: formal-systems
status: validated
---

# Discourse Coherence and Rhetorical Relations

## Core Idea
Discourse coherence concerns how sequences of utterances are meaningfully connected through coherence relations (narration, explanation, contrast). These relations constrain interpretation of pronouns, temporal expressions, and other context-dependent elements.

## Questions

```yaml
- question: "Consider two texts: (A) 'John fell. Mary pushed him.' and (B) 'John fell. Mary caught him.' In A we understand Mary as the cause of the fall; in B she is helping him. Neither text explicitly states a causal relationship. What produces these different interpretations?"
  type: multiple-choice
  options:
    - "The different verbs ('pushed' vs. 'caught') directly encode causation in their semantic entries"
    - "Coherence relations inferred between the clauses — causal in A, result/sequence in B — determine the causal structure the reader constructs"
    - "Anaphoric binding of 'him' differs between the two texts, producing different event interpretations"
    - "Past tense encodes temporal ordering differently in the two sentences"
  answer: 1
  explanation: "Neither text explicitly states that Mary caused John's fall or helped him. The reader infers the causal structure by identifying the most plausible coherence relation linking the clauses. In (A), the most plausible relation is causal (Mary's action explains the fall); in (B), it is narrative sequence with result (she responded to the fall). These relations are inferred — not encoded — but they have concrete semantic consequences for the event structure the reader constructs."

- question: "In a pure narration sequence — 'Max walked in. He sat down. He ordered coffee' — pronoun 'he' consistently refers to Max. In a contrast sequence — 'Max ordered coffee. Bill had tea. He paid and left' — the final 'he' is ambiguous. What explains the difference?"
  type: multiple-choice
  options:
    - "Narration uses first-person pronouns while contrast uses third-person, creating structural ambiguity"
    - "The narration relation keeps the main event participant (Max) salient across clauses, while the contrast relation introduces a new contrastive topic (Bill), dividing focus and making the subsequent pronoun ambiguous"
    - "Verb tense in narration sequences uniquely resolves pronoun reference in ways contrast sequences cannot"
    - "Pronouns in contrast sequences always refer to the most recently mentioned noun"
  answer: 1
  explanation: "Coherence relations directly influence focus structure, and focus structure determines which entities are accessible for pronominal reference. Narration keeps the main event participant as the center of attention across clauses, making pronouns unambiguous. Contrast introduces a new contrastive topic, splitting attention between two entities and making subsequent pronouns ambiguous. The coherence relation acts as a constraint on anaphora resolution — get the relation wrong and pronoun reference becomes misassigned."

- question: "Coherence relations such as narration, explanation, and contrast are inferred by listeners through world knowledge and plausibility reasoning, rather than being directly encoded in the sentences themselves."
  type: true-false
  answer: true
  explanation: "This is a central claim of discourse coherence theory. Unlike grammatical relations that are syntactically encoded, coherence relations are pragmatically inferred. Readers use world knowledge, genre conventions, and plausibility to identify which relation connects two propositions. This is why 'John fell. Mary pushed him' and 'John fell. Mary caught him' receive such different causal interpretations — the sentences themselves don't encode the causal structure; it is inferred by finding the most plausible connecting relation."

- question: "In a narration sequence, pronoun reference is more ambiguous than in a contrast sequence, because multiple narrative events compete for salience."
  type: true-false
  answer: false
  explanation: "The opposite is true. Narration sequences keep the main event participant salient across clauses, making pronoun reference relatively unambiguous — 'he' consistently refers to the narrative subject. In contrast sequences, a new entity is introduced as a contrastive topic, splitting focus and making subsequent pronoun reference ambiguous. Coherence relations concentrate or distribute salience: narration concentrates it on one participant, contrast distributes it across two."

- question: "Explain how coherence relations constrain the interpretation of temporal expressions like the past perfect ('had spilled'), using an example."
  type: short-answer
  answer: "Coherence relations set the temporal frame within which tense and aspect are interpreted. In 'John entered the room. He had spilled something on his tie,' the past perfect signals that the spilling is prior to the entering — but more specifically, the reader infers an elaboration relation: the second clause provides background about John's state as he entered, rather than advancing the narrative sequence. Without this inferred relation, you might misparse the timeline. The coherence relation determines the function each clause plays in discourse structure, which shapes how tense and aspect are understood."
  explanation: "Temporal expressions and coherence relations are mutually constraining: each provides clues for interpreting the other. The past perfect 'had spilled' signals backgrounding, which is consistent with the elaboration relation; conversely, recognizing an elaboration relation supports the past-perfect reading as background state rather than narrative advance. This interplay shows that discourse interpretation is not simply the sum of individual sentence meanings."
```

## Explainer

From your study of anaphora and discourse dynamics, you know that interpreting a pronoun or definite description requires tracking what is salient in the discourse context — the center of attention, recent referents, entities introduced into the discourse model. **Discourse coherence** extends this picture: it is not just individual referents that form a context, but the *relations between propositions* that give a discourse its structure. A sequence of sentences hangs together as a discourse only if the listener can identify how successive utterances are connected — and those connections constrain interpretation as powerfully as anything in the sentence itself.

The building blocks of discourse structure are **rhetorical relations** (also called coherence relations), which include among others: **narration** (a sequence of events in temporal order), **explanation** (the second clause gives the cause of the first), **elaboration** (the second clause says more about the same topic), **contrast** (the clauses highlight a difference), and **result** (the second clause is the consequence of the first). Consider the difference between "John fell. Mary pushed him" and "John fell. Mary caught him." The identical first clause receives radically different interpretations depending on which relation links it to the second. In the first, John's fall is presumably caused by Mary's push; in the second, he fell but was then helped. The relation determines the causal structure the reader infers.

This matters for your understanding of anaphora because coherence relations constrain which entities are accessible for pronominal reference. In a narration sequence — "Max walked in. He sat down. He ordered coffee" — each pronoun resolves to the narrative subject, Max, because the narration relation keeps the main event participant salient. But in a contrast sequence — "Max ordered coffee. Bill had tea" — the new entity (Bill) is introduced as a contrastive topic, and the subsequent pronoun "He paid and left" is ambiguous in a way it wouldn't be in pure narration. The coherence relation partly determines the **focus structure** of the discourse, and focus structure determines pronoun accessibility.

**Temporal expressions** are equally sensitive to coherence structure. "John entered the room. He had spilled something on his tie" — the past perfect ("had spilled") signals that the spilling is background information, not a narrative advance. This temporal interpretation is not determined by the sentence alone; it depends on recognizing that the second clause is elaborating on background state rather than advancing the narrative sequence. Coherence relations set the temporal frame within which tense and aspect are interpreted. Get the relation wrong and you misparse the timeline.

The deeper implication, relevant to your upcoming work on meaning and convention, is that discourse interpretation involves inferential work well beyond decoding individual sentences. Listeners default to specific coherence relations based on plausibility, world knowledge, and genre conventions. Reading a recipe, you assume each step is a narration; reading a scientific paper's discussion section, you expect explanation and result relations. The pragmatics-semantics boundary you've already studied now extends to discourse level: the coherence relations holding a text together are inferred, not encoded — yet they have concrete semantic consequences for how every constituent part is understood.
