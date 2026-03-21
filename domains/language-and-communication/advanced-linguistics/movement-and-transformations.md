---
id: movement-and-transformations
title: Movement and Transformations
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: constituency-and-phrases
  type: hard
- id: argument-structure-thematic-roles
  type: hard
builds-toward:
- c-command-and-binding
- minimalist-program-core-concepts
tags:
- syntax
- transformations
- displacement
stage: advanced
status: draft
---

# Movement and Transformations

## Core Idea
Movement (transformations) relocates phrases from one structural position to another, explaining question formation ('What did you see?'), topicalization, and passive voice. Movement leaves a trace or copy linking the moved element to its original position, preserving thematic role assignment and explaining why 'What did you think [trace] Mary saw?' is ungrammatical (extraction from embedded clause).

## Questions

```yaml
- question: "In the question 'What did Mary eat?', where did 'what' receive its thematic role as Theme of the verb 'eat'?"
  type: multiple-choice
  options:
    - "In object position after 'eat', before it moved to the front of the sentence"
    - "In Spec,CP (the front of the clause), where it currently appears on the surface"
    - "In subject position, since Themes in English are assigned there"
    - "Thematic roles are assigned at the surface level, so 'what' received its role in its current position"
  answer: 0
  explanation: "Thematic roles are assigned in the structural positions where verbs' selectional requirements are satisfied — for 'eat', the Theme is assigned to its object position. 'What' moved from object position to Spec,CP to form the question, but it retains the Theme role because a trace or copy in the original object position preserves the thematic connection. Surface position and thematic role assignment are distinct levels of representation — this is the core claim of movement theory."

- question: "Consider: 'What do you think Mary bought?' (grammatical) vs. '*What did you see the man who bought?' (ungrammatical). What explains the contrast?"
  type: multiple-choice
  options:
    - "'What' would have to extract from inside a relative clause — a syntactic island from which movement is blocked"
    - "Objects of perception verbs like 'see' cannot be questioned in English"
    - "Movement can only cross one clause boundary, and both examples cross the same number of boundaries"
    - "The relative pronoun 'who' blocks any further movement within the same sentence"
  answer: 0
  explanation: "The first sentence extracts 'what' from an embedded tensed clause — crossing a CP boundary — which is permitted. The second extracts 'what' from inside a relative clause, which is a syntactic island: movement out of it is blocked. Island constraints follow from movement theory as structural predictions — a trace inside an island cannot be properly licensed, so the movement is ruled out. This ungrammaticality is not an arbitrary fact to memorize but a consequence of the theory's architecture."

- question: "In the passive sentence 'The window was broken by the vandal,' the window receives the Agent thematic role because it occupies the grammatical subject position."
  type: true-false
  answer: false
  explanation: "The window has the Theme role (it is what got broken), not Agent, despite being the grammatical subject. Movement theory explains this as: 'the window' started in object position (where 'break' assigns its Theme role), then moved to subject position via passivization. The vandal retains the Agent role, realized in the by-phrase adjunct. This demonstrates that grammatical subject position does not always correspond to Agent — thematic role and grammatical position can come apart when movement has occurred."

- question: "Movement operations in syntax can apply to any arbitrary sequence of words as long as the resulting sentence is semantically interpretable."
  type: true-false
  answer: false
  explanation: "Movement can only apply to constituents — syntactic units identified as phrases by constituency tests. You cannot move a partial noun phrase, a verb plus one but not all its arguments, or any other non-constituent string. This is not a stipulation but a prediction: movement operates over the same hierarchical structures that define constituency. This is why constituency and movement are mutually dependent topics — violations of constituency in movement produce ungrammaticality in exactly the cases the theory predicts."

- question: "What theoretical work does the trace or copy left behind by movement accomplish? Why does the theory need it, rather than simply describing a phrase as appearing in a new position?"
  type: short-answer
  answer: "The trace or copy preserves the thematic connection between the moved phrase and the position where it received its role. Without a trace, 'What did Mary eat?' would have 'what' in Spec,CP with no structural explanation for why it has the Theme role of 'eat'. The trace in object position maintains the thematic relationship. The trace also makes island constraints predictable: if a trace must be properly licensed in its base position, then base positions inside syntactic islands cannot be traced to, producing the observed ungrammaticality."
  explanation: "The trace is the mechanism that allows movement theory to maintain a single level at which thematic roles are uniformly assigned (the position where the verb selects its arguments), while explaining why surface word order can differ from thematic structure. Without it, the theory would need separate mechanisms for thematic interpretation and island effects, losing explanatory unity. With it, both follow from the same architectural commitment: constituents move, leaving licensed copies that preserve their interpretive properties."
```

## Explainer

From constituency and phrases, you know that sentences aren't linear strings of words but hierarchically structured objects — DPs, VPs, and CPs nested inside each other in principled ways. From argument structure and thematic roles, you know that verbs assign roles (Agent, Theme, Goal) to their arguments in specific structural positions. Movement theory builds on both: it proposes that the *surface* order of words in a sentence is often different from the *underlying* order in which thematic roles were assigned, and that this displacement follows predictable rules.

Consider a simple question: *What did Mary see?* Compare it to the corresponding statement: *Mary saw what*. In the statement, the Theme (*what*) appears in the object position after the verb, which is where the verb *see* assigns its Theme role. In the question, *what* appears at the front of the sentence — in the **specifier of CP** (Spec,CP), a position used for questions and topics — but it still has the Theme role of *see*. How can it have that role when it's not where the verb assigned it? The answer that movement theory gives is: it *was* in the object position originally, then **moved** to Spec,CP, leaving behind a **trace** or copy that preserves the thematic connection. The sentence's surface form and its thematic structure are different levels of representation.

This isn't just a theoretical convenience — it makes specific, testable predictions about **island constraints**: the observation that movement is blocked from certain syntactic environments. You can ask *What do you think Mary saw?* (moving *what* from the embedded clause's object position over a CP boundary), but you cannot ask *\*What did you see the man who bought?* (moving *what* from inside a relative clause). The relative clause is a **syntactic island** — movement out of it is blocked. The trace/copy theory predicts this: if a trace must be in a structurally licensed position, then positions inside islands can't support traces in a way that satisfies all constraints simultaneously. The ungrammaticality isn't arbitrary — it follows from the theory's architecture.

**Passive voice** provides another clear case. *The window was broken by the vandal* has the same thematic interpretation as *The vandal broke the window* — the vandal is still the Agent, the window still the Theme — but the grammatical subject is the window, not the vandal. Movement theory explains this as: the window started as the object (where *break* assigns its Theme role), then moved to subject position, leaving a trace. The *by*-phrase is where the Agent role is now realized, in an adjunct position rather than in the normal structural subject position. Passivization is thus not a separate pattern to memorize but an instance of the general movement mechanism applied under specific morphological conditions.

The minimal unit that moves is always a **constituent** — never a partial phrase, never a random string. This is where your constituency knowledge becomes load-bearing: you can only move things that constituency tests identify as phrases. This is not coincidence — it is the theory's prediction. Movement operates over the same hierarchical structures that define constituency, which is why the two topics are prerequisites for each other. Together, they give you the basic architecture of generative syntax: hierarchical phrase structure, thematic role assignment, and displacement operations governed by structural constraints.
