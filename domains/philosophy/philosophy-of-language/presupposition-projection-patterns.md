---
id: presupposition-projection-patterns
title: Presupposition Projection and Triggering
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: grice-cooperative-principle-maxims
  type: hard
- id: possible-worlds-semantics
  type: soft
builds-toward:
- presupposition-and-assertion
- discourse-coherence-linguistic
tags:
- presupposition
- projection
- context-sensitivity
stage: formal-systems
status: draft
---

# Presupposition Projection and Triggering

## Core Idea
Presuppositions are content speakers assume and expect hearers to accept without assertion. They project upward through logical operators, though presuppositions can be filtered or accommodated depending on structural position and discourse context.

## How It's Best Learned
Study presupposition triggers like definite descriptions and factives in simple sentences, negations, conditionals, and questions to map projection patterns and filtering effects.

## Questions

```yaml
- question: "The sentence 'Alex stopped cheating on their taxes' is negated: 'Alex has not stopped cheating on their taxes.' What happens to the presupposition that Alex was previously cheating?"
  type: multiple-choice
  options:
    - "It is cancelled — the negation eliminates the presupposition along with the assertion"
    - "It is reversed — the negation implies Alex was not previously cheating"
    - "It projects — both the positive and negative sentences carry the presupposition that Alex was cheating"
    - "It becomes a Gricean implicature rather than a presupposition"
  answer: 2
  explanation: "Projection through negation is the defining characteristic of presupposition. Both 'Alex stopped cheating' and 'Alex has not stopped cheating' presuppose Alex was previously cheating — the negation reverses the assertion (whether stopping has occurred) but leaves the background assumption intact. This contrasts with entailments, which are cancelled under negation: 'Alex stopped cheating' entails Alex is no longer cheating, but the negated version cancels that entailment entirely."

- question: "A politician says: 'Even my critics know that my economic policy will create jobs.' How is this best analyzed in terms of presupposition?"
  type: multiple-choice
  options:
    - "It is a direct assertion that the policy will create jobs, open to direct rebuttal"
    - "It is a Gricean implicature — mentioning critics implies the claim is widely accepted"
    - "The factive verb 'know' presupposes its complement is true, planting 'the policy will create jobs' as common ground without asserting it"
    - "It is an entailment that critics hold a positive view of the policy"
  answer: 2
  explanation: "Factive verbs like 'know' presuppose their complement clause. By attributing knowledge to critics, the politician builds in the presupposition that the policy will create jobs — as background content taken for granted rather than argued for. This is more powerful than assertion because presuppositions aren't directly at issue; to object, a hearer must explicitly challenge the presupposition rather than the assertion, which is conversationally marked and awkward."

- question: "In the sentence 'If France has a king, the king of France is bald,' the existence presupposition of the consequent does not project to the whole conditional."
  type: true-false
  answer: true
  explanation: "This is the classic example of presupposition filtering. The presupposition of 'the king of France is bald' (that France has a king) is satisfied by the antecedent 'If France has a king...', so it is absorbed and does not project to the whole sentence. The full conditional does not presuppose France has a king — it is conditional on it. Filtering occurs when the embedding context provides or entails the presupposed content, absorbing rather than passing it upward."

- question: "Presuppositions and entailments behave the same way under negation — both are cancelled when a sentence is negated."
  type: true-false
  answer: false
  explanation: "This is the key diagnostic difference. Entailments are cancelled under negation: 'The cat is on the mat' entails there is a cat, but 'The cat is not on the mat' does not. Presuppositions survive negation: 'The king of France is bald' and 'The king of France is not bald' both presuppose there is a king of France. This projection behavior under negation is what makes presuppositions distinctive — they are not simply weak or defeasible entailments."

- question: "What is presupposition accommodation, and why might strategic use of presupposition triggers be more rhetorically effective than making the same content an explicit assertion?"
  type: short-answer
  answer: "Accommodation occurs when a hearer silently accepts a speaker's presupposition even though it was not already in the common ground, rather than objecting. If someone says 'My car broke down' to a hearer unaware they own a car, the hearer typically accommodates the car's existence rather than interrupting. Strategically, presupposing content is more powerful than asserting it because assertions are directly at issue and invite rebuttal, while presuppositions slide into common ground as background. To challenge a presupposition, the hearer must step outside the normal conversational flow and meta-linguistically object — which is socially marked and conversationally costly."
  explanation: "This is why presupposition triggers are tools of persuasion. 'When did you stop beating your spouse?' presupposes beating occurred, placing the respondent in a position where any direct answer accepts the presupposition. Political discourse routinely embeds contested claims as presuppositions ('the failed policy,' 'the job-killing regulation') because once they enter common ground through accommodation, they are harder to dislodge than openly asserted claims."
```

## Explainer

From your study of Grice's cooperative principle, you know that communication involves more than what is literally said — implicatures arise from the assumption that speakers are being cooperative, informative, and relevant. **Presuppositions** are a different kind of implicit content: not inferences the hearer draws, but background assumptions the speaker *takes for granted* and *builds into* the utterance as common ground. The sentence "The king of France is bald" presupposes that there is a king of France; the sentence "Maria regrets that she left early" presupposes that Maria did leave early. These presuppositions are not asserted — they are the context the assertion rests on.

**Presupposition triggers** are linguistic constructions that reliably introduce presuppositions. Definite descriptions ("the X") trigger existence presuppositions. **Factive verbs** ("know," "realize," "regret") presuppose their complement is true — "John knows it's raining" presupposes it is raining. Change-of-state verbs ("stop," "begin," "continue") carry presuppositions about prior states. Iteratives ("again," "still," "return") presuppose a prior occurrence or state. Each trigger type has a characteristic presupposition that is introduced whenever the construction is used.

The **projection problem** asks what happens to presuppositions when these triggers appear inside complex sentences — in negations, conditionals, questions, and modal constructions. The surprising fact is that presuppositions often **project** out of their embedding context, surviving operators that would normally affect assertoric content. "It's not the case that the king of France is bald" still carries the presupposition that France has a king — even though the negation reverses the assertion. "Does Maria regret leaving early?" still presupposes she left early — even though the question doesn't assert it. Your knowledge of possible worlds semantics is relevant here: presuppositions can be understood as constraints on the contexts of utterance — they require the presupposed content to be true in all worlds in the common ground.

But projection is not absolute. **Filtering** occurs when the embedding context provides information that absorbs or cancels the presupposition. In "If France has a king, the king of France is bald," the presupposition of the consequent ("France has a king") is satisfied by the antecedent and does not project to the whole. **Accommodation** occurs when a presupposition is not already in the common ground but hearers silently add it rather than reject the utterance — if someone says "My car broke down" to a hearer who didn't know they had a car, the hearer typically accommodates the existence presupposition rather than objecting. Understanding when presuppositions project, get filtered, or get accommodated is crucial for analyzing how information is managed and contested across a discourse: speakers can use presupposition triggers strategically to smuggle contested content into common ground without asserting it openly.
