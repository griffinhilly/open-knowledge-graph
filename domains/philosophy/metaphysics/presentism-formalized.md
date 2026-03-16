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
status: draft
---

# Presentism (Formalized)

## Core Idea
Presentism is the metaphysical theory that only the present moment exists. Past events no longer exist and future events do not yet exist; only present entities are real. This view must explain how we can refer to and reason about past and future events if they don't exist.

## Explainer

You already know from philosophy of time and temporal becoming that there is a deep question about what kind of thing time is. One central divide is between the **A-series** (past, present, future as real, flowing properties) and the **B-series** (all times equally real, ordered only by earlier-than/later-than). Presentism is the most radical A-theory: it holds that the present is not just privileged but *exclusively real*. Dinosaurs are not somewhere in spacetime waiting to be visited; the Roman Empire is not a distant region of four-dimensional reality. They simply do not exist. Only what is present exists.

This is intuitive at first glance—we are never directly acquainted with the past or future, only with the now. But formalization reveals how demanding the view is. You already know from temporal logic that we can reason about past and future using operators like "It was the case that P" (P) and "It will be the case that P" (FP). These operators quantify over past and future times or events. But if only the present exists, what do these operators *range over*? When you truly assert "Caesar was stabbed in 44 BC," you seem to be talking about something. If that something does not exist, how can your statement be true?

This is the **truthmaker problem for presentism**. The most developed responses appeal to **presently existing abstract objects**: propositions, facts, or tensed properties that hold now about what was or will be. On one version, there is a present fact that "Caesar was stabbed in 44 BC"—a tensed fact that exists now but is *about* the past. On another view, the past leaves **traces**: present causal residues (memories, records, physical effects) that ground truths about what was. Neither solution is universally accepted, which is why presentism generates extensive formal machinery.

The other major challenge is **Special Relativity**. Relativistic physics appears to abolish absolute simultaneity—what counts as "the present" is frame-dependent, not a single objective slice of the universe. If there is no frame-independent present, there is no unique set of present existents, and presentism seems either incoherent or committed to a preferred reference frame that physics does not provide. Defenders of presentism have pursued three responses: reject the philosophical interpretation of relativity that threatens presentism, posit a metaphysically privileged frame that physics does not detect, or develop a version of presentism compatible with relativistic spacetime. Each option has costs, which is why the debate between presentism and its rival **eternalism** (all times equally real) remains live and technically sophisticated.
