---
id: presentism-formalized
title: Presentism (Formalized)
domain: philosophy
course: metaphysics
prerequisites:
- id: temporal-becoming
  type: hard
- id: philosophy-of-time
  type: hard
- id: temporal-logic
  type: hard
tags:
- time
- presentism
- existence
- temporal-metaphysics
stage: formal-systems
status: validated
---

# Presentism (Formalized)

## Core Idea
Presentism is the metaphysical theory that only the present moment exists. Past events no longer exist and future events do not yet exist; only present entities are real. This view must explain how we can refer to and reason about past and future events if they don't exist.

## Questions

```yaml
- question: "A presentist asserts that 'Caesar was stabbed in 44 BC' is true. What philosophical problem does this create for presentism?"
  type: multiple-choice
  options:
    - "No problem — the statement is obviously true and presentism has no difficulty explaining it"
    - "The statement must be false under presentism, since its subject no longer exists"
    - "If only the present exists, then the entity the statement is about (Caesar, the stabbing) no longer exists, raising the truthmaker problem: what in the present world makes this past-tensed statement true?"
    - "The problem is epistemic: we cannot verify claims about the past without present evidence"
  answer: 2
  explanation: "This is the truthmaker problem for presentism. A true statement needs a truthmaker — something that makes it true. If only present entities exist, then Caesar, the event of the stabbing, and the Rome of 44 BC are all non-existent. Yet 'Caesar was stabbed in 44 BC' appears to be about those things. Presentists have proposed solutions — presently existing tensed facts, causal traces, or abstract propositions — but none is universally accepted. The point is that the naive intuition that only the present exists immediately generates a deep question about the ontological basis of truths about the past."

- question: "Special Relativity poses a serious challenge to presentism. Which statement best explains the challenge?"
  type: multiple-choice
  options:
    - "Special relativity shows that time travel is possible, making it unclear what 'the present' refers to"
    - "Special relativity abolishes absolute simultaneity: what counts as 'now' is frame-dependent, so there is no single objective present — and therefore no unique set of presently existing entities that presentism requires"
    - "The challenge is that special relativity is a physical theory and metaphysics must be derived from physics, not from intuition"
    - "Special relativity proves that the past and future are equally real, which directly settles the debate in favor of eternalism"
  answer: 1
  explanation: "Under special relativity, simultaneity is not absolute — two events that are simultaneous in one reference frame are not simultaneous in another moving frame. If 'the present' is defined as the set of all events simultaneous with now, then different observers have different presents. There is no frame-independent set of simultaneously existing things. This threatens presentism, which requires a unique, objective present whose contents are the only existents. Presentists must either reject this interpretation of relativity, posit a metaphysically privileged frame that physics doesn't detect, or reconstruct presentism within relativistic spacetime — each option carries significant costs."

- question: "Presentism is committed to the A-series conception of time, on which past, present, and future are real dynamic properties — not merely the B-series ordering of events by earlier-than and later-than."
  type: true-false
  answer: true
  explanation: "True. Presentism is the most radical A-theory: it holds that the present is not just a privileged temporal position but the exclusively real one. The A-series treats pastness, presentness, and futurity as genuine flowing properties of events. The B-series, by contrast, treats all times as equally real and ordered only by the fixed relation earlier-than/later-than. Eternalism — the rival of presentism — is a B-theory. Presentism's commitment to the A-series is what motivates both its intuitive appeal (we experience the present as special) and its philosophical difficulties (explaining how the A-series flow is possible and what makes past truths true)."

- question: "Presentism's appeal to currently existing abstract objects (tensed facts or propositions) as truthmakers for past-tensed statements fully resolves the truthmaker problem, making the debate with eternalism largely settled."
  type: true-false
  answer: false
  explanation: "False. The appeal to presently existing abstract objects is a proposed response to the truthmaker problem, not a resolution of it. Critics argue that positing abstract tensed facts — 'it is now a fact that Caesar was stabbed in 44 BC' — simply relocates the mystery: what makes a present abstract fact be about a past concrete event that no longer exists? Trace theories (grounding past truths in present physical effects) face the problem that many past truths leave no surviving traces. The debate between presentism and eternalism remains technically sophisticated and unresolved precisely because neither side's responses to these objections are universally accepted."

- question: "Explain the truthmaker problem for presentism in your own words: what is the problem, and what resources does the presentist have to respond?"
  type: short-answer
  answer: "The truthmaker problem asks: if only present entities exist, what makes past-tensed statements like 'Caesar was stabbed in 44 BC' true? A true claim seems to require something — a truthmaker — that makes it true. But if Caesar no longer exists, neither does the stabbing event, so there is no obvious present entity that the statement is about. Presentists have proposed two main responses: (1) presently existing abstract objects such as tensed facts or propositions that hold now but are about the past; (2) causal traces — present physical records, memories, and effects — that ground truths about what caused them. Neither is without objection: abstract objects raise questions about how they relate to concrete past events; traces cannot cover cases where all physical evidence has been destroyed."
  explanation: "The problem reveals that presentism is far more demanding than its initial intuitive appeal suggests. Accepting that only the present exists forces a systematic account of how modal and temporal discourse can remain meaningful — an account that must compete with the simpler eternalist position that past events exist in their own region of four-dimensional spacetime."
```

## Explainer

You already know from philosophy of time and temporal becoming that there is a deep question about what kind of thing time is. One central divide is between the **A-series** (past, present, future as real, flowing properties) and the **B-series** (all times equally real, ordered only by earlier-than/later-than). Presentism is the most radical A-theory: it holds that the present is not just privileged but *exclusively real*. Dinosaurs are not somewhere in spacetime waiting to be visited; the Roman Empire is not a distant region of four-dimensional reality. They simply do not exist. Only what is present exists.

This is intuitive at first glance—we are never directly acquainted with the past or future, only with the now. But formalization reveals how demanding the view is. You already know from temporal logic that we can reason about past and future using operators like "It was the case that P" (P) and "It will be the case that P" (FP). These operators quantify over past and future times or events. But if only the present exists, what do these operators *range over*? When you truly assert "Caesar was stabbed in 44 BC," you seem to be talking about something. If that something does not exist, how can your statement be true?

This is the **truthmaker problem for presentism**. The most developed responses appeal to **presently existing abstract objects**: propositions, facts, or tensed properties that hold now about what was or will be. On one version, there is a present fact that "Caesar was stabbed in 44 BC"—a tensed fact that exists now but is *about* the past. On another view, the past leaves **traces**: present causal residues (memories, records, physical effects) that ground truths about what was. Neither solution is universally accepted, which is why presentism generates extensive formal machinery.

The other major challenge is **Special Relativity**. Relativistic physics appears to abolish absolute simultaneity—what counts as "the present" is frame-dependent, not a single objective slice of the universe. If there is no frame-independent present, there is no unique set of present existents, and presentism seems either incoherent or committed to a preferred reference frame that physics does not provide. Defenders of presentism have pursued three responses: reject the philosophical interpretation of relativity that threatens presentism, posit a metaphysically privileged frame that physics does not detect, or develop a version of presentism compatible with relativistic spacetime. Each option has costs, which is why the debate between presentism and its rival **eternalism** (all times equally real) remains live and technically sophisticated.
