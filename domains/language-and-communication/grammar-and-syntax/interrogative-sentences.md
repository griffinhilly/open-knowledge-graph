---
id: interrogative-sentences
title: Interrogative Sentences and Question Formation
domain: language-and-communication
course: grammar-and-syntax
prerequisites:
- id: subject-and-predicate
  type: hard
- id: auxiliary-verbs-and-modality
  type: soft
builds-toward:
- subject-auxiliary-inversion
tags:
- sentence-types
- questions
- interrogative
stage: abstract-reasoning
status: validated
---

# Interrogative Sentences and Question Formation

## Core Idea
Interrogative sentences ask questions and have two main types: yes/no questions answered with yes or no ("Do you like pizza?") and wh-questions seeking information ("What did you eat?"). Questions typically involve special word order, question words, and intonation patterns that distinguish them from statements.

## How It's Best Learned
Practice converting statements to yes/no questions by identifying and moving the auxiliary verb. For wh-questions, start with the question word, then add the auxiliary if needed, then follow with subject and main verb.

## Common Misconceptions
- Confusing question word order with statement word order (questions need special inversion patterns).
- Not recognizing that yes/no questions require auxiliaries ("Do you like it?" not "Like you it?").

## Questions

```yaml
- question: "A student wants to form a yes/no question from the statement 'Maria works at the hospital.' Which version is grammatically correct?"
  type: multiple-choice
  options:
    - "Works Maria at the hospital?"
    - "Does Maria work at the hospital?"
    - "Do Maria works at the hospital?"
    - "Maria does works at the hospital?"
  answer: 1
  explanation: "English cannot invert a bare main verb, so the dummy auxiliary 'does' is inserted to carry tense. Once 'does' carries the tense, the main verb reverts to its base form ('work,' not 'works'). Option A (*Works Maria?) is ungrammatical — main verbs cannot invert in English. Option C has the right auxiliary but fails to drop the tense inflection from the main verb."

- question: "A student writes: 'Who did call you last night?' A classmate says it should be 'Who called you last night?' Which is correct, and why?"
  type: multiple-choice
  options:
    - "'Who did call you last night?' — wh-questions always require the auxiliary 'did'"
    - "'Who called you last night?' — when the question word is the subject, no inversion or dummy auxiliary is needed"
    - "'Who called you last night?' — but only because 'called' is in the past tense"
    - "Both are correct; 'did' is optional for added emphasis"
  answer: 1
  explanation: "When the wh-word functions as the grammatical subject ('who' is the one who called), subject-auxiliary inversion does not apply. 'Who called you?' follows normal subject-verb order with no inserted auxiliary. By contrast, 'Who did you call?' requires 'did' because 'who' is the object and 'you' is the subject. The rule: inversion applies only when the wh-word is NOT the subject."

- question: "In the question 'What did you eat for dinner?', the word 'what' is the grammatical subject of the sentence."
  type: true-false
  answer: false
  explanation: "'What' is the grammatical object — it names the thing eaten. 'You' is the subject. Because 'what' is in the object position, subject-auxiliary inversion applies and 'did' is inserted. If 'what' were the subject (as in 'What fell off the shelf?'), no inversion and no dummy auxiliary would be needed."

- question: "A yes/no question in English always requires an auxiliary verb, even if the corresponding statement contains no auxiliary."
  type: true-false
  answer: true
  explanation: "English question formation requires moving an auxiliary before the subject. When a statement has no auxiliary (e.g., 'She sings'), the main verb cannot invert directly (*'Sings she?'). The dummy auxiliary 'do' must be inserted to carry tense: 'Does she sing?' This insertion is obligatory — there is no grammatical alternative when no real auxiliary exists."

- question: "Why does English insert 'do' to form some questions (as in 'Do you like it?') but not others (as in 'Are you ready?')? What determines when 'do' is needed?"
  type: short-answer
  answer: "'Do' is inserted only when the declarative sentence has no auxiliary verb. English questions are formed by moving an auxiliary before the subject — if none exists, 'do' is supplied as a dummy auxiliary to carry tense. When an auxiliary already exists (is, are, will, can, etc.), it inverts directly without 'do.'"
  explanation: "The underlying principle: English questions move an auxiliary, never a main verb. 'Are you ready?' already has 'are.' 'You like it' has no auxiliary, so 'do' is supplied: 'Do you like it?' The form of 'do' carries the tense (do/does for present, did for past), while the main verb drops its tense inflection."
```

## Explainer

You already know that every sentence has a **subject** (who or what the sentence is about) and a **predicate** (what the subject does or is). In declarative sentences, the subject comes first: "She *is* happy." Interrogative sentences — questions — disrupt this default order. The most important structural operation in English question formation is **subject-auxiliary inversion**: the auxiliary verb moves to a position before the subject, signaling to the listener that a question is being asked rather than a statement being made.

For **yes/no questions**, the process is straightforward once you spot the auxiliary. Take "She is happy." The auxiliary *is* inverts with the subject: "Is she happy?" Take "They will arrive soon." Inversion gives "Will they arrive soon?" The challenge arises when the declarative sentence has no auxiliary — "She likes tea." English does not allow bare inversion of a main verb (*"Likes she tea?" is ungrammatical), so it inserts the dummy auxiliary **do** to carry the tense: "Does she like tea?" This is why your prerequisite knowledge of auxiliary verbs is essential here: you must recognize which element in the sentence is the auxiliary, because that is the element that moves.

**Wh-questions** add a second layer. They begin with a question word — *who, what, where, when, why, how* — that names the type of information sought. The question word occupies the front position, and subject-auxiliary inversion still applies to the rest of the sentence: "What did she eat?" = [what] + [did ← inverted auxiliary] + [she ← subject] + [eat ← main verb]. When the question word *is* the subject, inversion disappears entirely — "Who called you?" not "Who did call you?" — because moving the auxiliary would require it to follow its own subject, which is already at the front.

Intonation completes the picture. In speech, yes/no questions typically end with rising pitch, signaling incompleteness and inviting a response. Many wh-questions use falling pitch, since the question word already signals that information is expected. In writing, the question mark does the same work. Together, word order, auxiliary selection, and intonation form an interconnected system: change one component without the others and the result sounds strange or ambiguous. Mastering question formation means understanding these three components not as separate rules but as a coordinated grammatical package.
