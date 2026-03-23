---
id: murphyjitsu
title: "Murphyjitsu"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: premortem-analysis
    type: hard
  - id: the-planning-fallacy
    type: soft
tags: ["CFAR", "planning", "technique", "robustness", "mental-simulation"]
stage: advanced
status: validated
---

## Core Idea

Murphyjitsu (from CFAR) is a mental simulation technique for stress-testing plans. For each step of your plan, ask: "Does this feel like the sort of plan that will work, or the sort of plan that will fail?" If your gut says it feels like it will fail, identify the most likely failure mode, modify the plan to address it, and repeat until the plan passes the gut check. The technique combines the premortem's failure-imagination with iterative plan repair. It leverages System 1's pattern-matching ability — your intuition often detects problems that your explicit reasoning has not surfaced. The name is a portmanteau of Murphy's Law and jujitsu: using the force of Murphy's Law ("what can go wrong will go wrong") to strengthen your plan rather than being defeated by it.

## How It's Best Learned

Before your next important meeting, trip, or project deadline, walk through your plan step by step. At each step, ask "does this feel like it will work?" If not, identify the failure mode and fix it. Repeat until each step passes. Compare the revised plan to your original — the differences reveal your blind spots.

## Common Misconceptions

- Murphyjitsu is not about being paranoid — it is about systematically finding and fixing plan weaknesses before they manifest.
- The technique does not require that you fix every possible failure mode — only the ones your gut flags as realistic.

## Explainer

From premortem analysis, you know that imagining a project has already failed -- and then explaining why -- surfaces risks that optimism bias and social pressure would otherwise hide. Murphyjitsu, developed by CFAR (the Center for Applied Rationality), takes this insight and adds an iterative repair loop that transforms risk identification into actual plan improvement.

The technique works like this. You walk through your plan step by step, and at each step you ask a simple gut-check question: "Does this feel like the sort of step that will work, or the sort of step that will fail?" If your gut says it feels like it will fail, you stop and identify the most likely failure mode. Then -- and this is what distinguishes Murphyjitsu from a standard premortem -- you modify the plan to address that failure mode. After the modification, you ask the gut-check question again. You repeat this cycle -- identify failure, fix, re-check -- until every step passes the gut check. The name is a portmanteau of Murphy's Law ("what can go wrong will go wrong") and jujitsu (using your opponent's force to your advantage): instead of being defeated by Murphy's Law, you use it to strengthen your plan.

The technique's power comes from deliberately leveraging **System 1 pattern-matching**. Your intuition, shaped by years of experience, often detects problems that your explicit reasoning has not surfaced. A plan might look coherent on paper -- every step follows logically from the last -- yet still "feel off." That gut reaction is System 1 recognizing a pattern it has seen before: a plan that resembles other plans that failed. Murphyjitsu treats this feeling as a signal worth interrogating rather than dismissing. By asking "why does this feel like it will fail?", you translate an inarticulate intuition into a specific, addressable failure mode.

The practical result is a plan that has been stress-tested against your best intuitions about what typically goes wrong. Consider preparing for a conference talk. Your original plan might be: finish slides by Wednesday, do a practice run Thursday, present Friday. Murphyjitsu might surface that "finish slides by Wednesday" feels unrealistic given your other commitments (fix: block Tuesday afternoon for slides), that your practice run has no audience (fix: ask a colleague to listen), and that you have not tested the projector setup (fix: arrive 30 minutes early). Each fix is small, but the cumulative effect is a plan that accounts for the failure modes you would otherwise discover only when they materialized. The stopping criterion -- "every step passes the gut check" -- keeps the technique bounded and practical rather than spiraling into infinite risk cataloging.

## Questions

```yaml
- question: "A project manager finishes a Murphyjitsu session for a product launch. She has gone through the plan step by step, identified three failure modes, and modified the plan to address each. The plan now 'feels like it will work' at every step. What should she do next?"
  type: multiple-choice
  options:
    - "She should run at least five more iterations regardless, because gut checks are unreliable"
    - "The session is complete — the plan has passed the gut check and is ready to proceed"
    - "She should create a formal risk register to document all identified failure modes for stakeholders"
    - "The gut check is only valid for short-term plans; long-term plans require external review"
  answer: 1
  explanation: "Murphyjitsu concludes when the plan passes the gut check — when each step feels like the kind of step that will work. The gut check is the stopping criterion, not an arbitrary number of iterations or a formal documentation requirement. The key insight is that the gut check reflects System 1's pattern-matching judgment that identified failure modes have been adequately addressed."

- question: "Which of the following best describes how Murphyjitsu differs from a standard premortem?"
  type: multiple-choice
  options:
    - "A premortem uses imagined future failure; Murphyjitsu uses historical data about past failures"
    - "Murphyjitsu adds an iterative repair loop — after identifying a failure mode, you fix it and repeat the gut check until the plan passes"
    - "Murphyjitsu is only used for short-term personal plans, while premortems are for organizational projects"
    - "A premortem assigns probabilities to failure modes; Murphyjitsu treats all failure modes as equally likely"
  answer: 1
  explanation: "Both techniques involve imagining failure before it occurs. What distinguishes Murphyjitsu is the iterative repair loop: you identify a failure mode, modify the plan to address it, then ask the gut-check question again. You repeat — identify, fix, check — until each step passes. A premortem typically lists failure modes for awareness, but does not structure the process as iterative plan improvement until a robustness threshold is met."

- question: "Murphyjitsu recommends systematically identifying and addressing every conceivable failure mode in a plan before proceeding."
  type: true-false
  answer: false
  explanation: "Murphyjitsu is specifically scoped to failure modes that your gut flags as realistic — those System 1 identifies as the kind of thing that would likely go wrong. It is not a comprehensive risk audit. The technique explicitly does not require fixing every possible failure mode, only the ones that feel realistic enough to trigger a failed gut check. This scope keeps the technique practical and prevents paralysis while still catching the most likely failure points."

- question: "Murphyjitsu leverages System 1 (intuitive pattern-matching) to detect plan weaknesses that explicit reasoning may have overlooked."
  type: true-false
  answer: true
  explanation: "This is a core feature of the technique. Explicit System 2 reasoning may construct a plan that looks coherent on paper but still 'feels off' because intuition, shaped by experience, has pattern-matched it to previous failures. Murphyjitsu uses this gut reaction as a signal: if a step feels like it will fail, that feeling is worth interrogating even if you cannot immediately articulate why. The goal is to surface implicit concerns and convert them into explicit fixes."

- question: "What does Murphyjitsu add beyond a simple premortem, and why does that addition matter for the quality of plans?"
  type: short-answer
  answer: "A premortem generates a list of failure modes; Murphyjitsu adds an iterative repair loop. After identifying a failure mode, you modify the plan to address it, then run the gut check again. This continues until every step passes. The addition matters because awareness of a failure mode without plan modification does little to prevent it — Murphyjitsu produces an actually improved plan, not just a list of risks."
  explanation: "The name captures this: jujitsu uses the opponent's force to strengthen yourself rather than merely bracing for impact. Murphyjitsu takes Murphy's Law — whatever can go wrong will — and instead of treating it as a warning, uses it as a tool to iteratively strengthen plans. The iteration stops at the gut-check threshold, making the technique bounded and practical rather than an infinite risk-cataloging exercise."
```
