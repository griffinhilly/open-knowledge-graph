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

## Explainer

From constituency and phrases, you know that sentences aren't linear strings of words but hierarchically structured objects — DPs, VPs, and CPs nested inside each other in principled ways. From argument structure and thematic roles, you know that verbs assign roles (Agent, Theme, Goal) to their arguments in specific structural positions. Movement theory builds on both: it proposes that the *surface* order of words in a sentence is often different from the *underlying* order in which thematic roles were assigned, and that this displacement follows predictable rules.

Consider a simple question: *What did Mary see?* Compare it to the corresponding statement: *Mary saw what*. In the statement, the Theme (*what*) appears in the object position after the verb, which is where the verb *see* assigns its Theme role. In the question, *what* appears at the front of the sentence — in the **specifier of CP** (Spec,CP), a position used for questions and topics — but it still has the Theme role of *see*. How can it have that role when it's not where the verb assigned it? The answer that movement theory gives is: it *was* in the object position originally, then **moved** to Spec,CP, leaving behind a **trace** or copy that preserves the thematic connection. The sentence's surface form and its thematic structure are different levels of representation.

This isn't just a theoretical convenience — it makes specific, testable predictions about **island constraints**: the observation that movement is blocked from certain syntactic environments. You can ask *What do you think Mary saw?* (moving *what* from the embedded clause's object position over a CP boundary), but you cannot ask *\*What did you see the man who bought?* (moving *what* from inside a relative clause). The relative clause is a **syntactic island** — movement out of it is blocked. The trace/copy theory predicts this: if a trace must be in a structurally licensed position, then positions inside islands can't support traces in a way that satisfies all constraints simultaneously. The ungrammaticality isn't arbitrary — it follows from the theory's architecture.

**Passive voice** provides another clear case. *The window was broken by the vandal* has the same thematic interpretation as *The vandal broke the window* — the vandal is still the Agent, the window still the Theme — but the grammatical subject is the window, not the vandal. Movement theory explains this as: the window started as the object (where *break* assigns its Theme role), then moved to subject position, leaving a trace. The *by*-phrase is where the Agent role is now realized, in an adjunct position rather than in the normal structural subject position. Passivization is thus not a separate pattern to memorize but an instance of the general movement mechanism applied under specific morphological conditions.

The minimal unit that moves is always a **constituent** — never a partial phrase, never a random string. This is where your constituency knowledge becomes load-bearing: you can only move things that constituency tests identify as phrases. This is not coincidence — it is the theory's prediction. Movement operates over the same hierarchical structures that define constituency, which is why the two topics are prerequisites for each other. Together, they give you the basic architecture of generative syntax: hierarchical phrase structure, thematic role assignment, and displacement operations governed by structural constraints.
