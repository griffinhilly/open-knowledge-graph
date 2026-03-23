---
id: design-documentation-and-rationale
title: Design Documentation and Rationale
domain: arts-and-aesthetics
course: design-principles
prerequisites:
- id: design-systems-and-consistency
  type: hard
- id: systems-thinking-in-design
  type: soft
tags:
- documentation
- communication
- knowledge-sharing
- rationale
stage: formal-systems
status: validated
---

# Design Documentation and Rationale

## Core Idea
Design documentation captures not just the final design but the reasoning behind decisions—the problems identified, constraints considered, alternatives rejected, and principles applied. Good documentation preserves institutional knowledge, allows new team members to understand the system, and prevents reinvention. Documentation is especially critical in design systems where consistency depends on shared understanding.

## How It's Best Learned
Document one of your designs with full rationale: problems, constraints, principles, alternatives considered. Later, have someone else implement it from your documentation.

## Common Misconceptions
That documentation is busywork that slows down design. Good documentation actually accelerates teams by reducing questions and rework.

## Questions

```yaml
- question: "A new designer joins a team and wants to change the primary button color from the existing '#2563EB' to a slightly different blue they prefer aesthetically. Which piece of documentation would most effectively prevent this from causing problems?"
  type: multiple-choice
  options:
    - "A screenshot showing the original button in context across multiple screens"
    - "The rationale explaining that this specific blue was chosen to meet WCAG AA contrast requirements, was selected after testing three alternatives with users, and aligns with the brand's trust-signaling palette"
    - "A changelog listing every time the button color was previously changed"
    - "A style guide listing all approved colors in the design system"
  answer: 1
  explanation: "The style guide (option D) tells the new designer what color to use but not why — it cannot explain what they would break by changing it. The rationale (option B) captures the constraints (accessibility compliance), the evidence (user testing), and the alternatives already rejected. With this information, the new designer understands that the color is not aesthetic preference but a functional requirement with documented justification. The 'why' is what transforms a spec into a constraint — and it is exactly what prevents the next designer from unknowingly breaking something that took significant work to get right."

- question: "A designer argues: 'I shouldn't need to write design rationale — the design file is self-documenting because all the specs are visible in Figma.' What is the critical flaw in this view?"
  type: multiple-choice
  options:
    - "The designer is right — modern design tools capture all the relevant decision information"
    - "Design files capture what was decided (the final specs and values), but not why — they show the color but not the accessibility testing, user research, and rejected alternatives that led to it. Without rationale, future designers cannot distinguish intentional constraints from arbitrary choices"
    - "The designer should document rationale only for controversial or contested decisions"
    - "Design files are insufficient only for very large systems with more than 50 components"
  answer: 1
  explanation: "This is the central misconception named in the Core Idea: documentation that only records what was decided is of limited value. The Figma file shows '#2563EB'; it does not show that three alternative blues were tested and rejected, that this specific value was chosen because it passes WCAG AA at 4.6:1 contrast ratio, or that users in testing found it 23% more clickable. Without that rationale, a future designer sees a color and has no way to know whether it is a carefully engineered constraint or an arbitrary leftover. The 'why' is what allows the design system to be maintained intelligently rather than randomly."

- question: "Good design documentation should capture not just the final decision but also the alternatives that were considered and the reasons they were rejected."
  type: true-false
  answer: true
  explanation: "True — documenting rejected alternatives is one of the most valuable things rationale can contain. It prevents future team members from independently rediscovering and relitigating decisions that were already thoroughly explored. If three button styles were evaluated and two rejected for specific reasons, recording those reasons means the next designer who thinks 'what about a pill-shaped button?' can immediately see that it was considered, understand why it was rejected, and apply their energy elsewhere. Without this, teams repeatedly revisit the same decisions — a direct source of wasted effort that the Core Idea describes as 'reinvention.'"

- question: "Design documentation is primarily useful for external stakeholders and can be safely skipped for internal design systems where existing team members already understand the decisions."
  type: true-false
  answer: false
  explanation: "False — internal teams change over time through hiring, departures, role changes, and simple forgetting. The Explainer states this explicitly: 'the moment those people leave, go on vacation, or simply forget why they made a particular decision, the system starts to drift.' Even original decision-makers forget their own reasoning within months. A design system that exists only in team members' heads is fragile and opaque — a problem that compounds over time as decisions accumulate without documentation. The documentation is for the future state of the team, not just its present composition."

- question: "What is the practical test of whether design documentation is sufficient, and why is this a high bar to meet?"
  type: short-answer
  answer: "The practical test is whether a new team member can implement a component correctly, handle edge cases the original designer anticipated, and extend the system in its intended direction — all without asking the original designer a single question. This is a high bar because it requires documentation to capture not just specifications but the complete reasoning: what problem was being solved, what constraints were in play, what alternatives were rejected and why, and which principles guided the final decision. Documentation that only lists specs fails this test entirely — it tells you what to do but not what not to do, why, or how to handle situations the original designer thought about but didn't expose in the final design."
  explanation: "The 'new team member' test is a concrete operationalization of what it means for a design system to be self-sustaining. It separates documentation that feels complete from documentation that actually is — because the test requires the documentation to transfer not just information but judgment. Documentation that passes this test means the system can grow and adapt without requiring access to its creators, which is the whole point of building a scalable design system rather than a personal style guide."
```

## Explainer

From your understanding of design systems, you know that consistency depends on shared rules applied across many contexts by many people. Design documentation is the mechanism that makes this sharing possible. Without it, a design system exists only in the heads of its creators — and the moment those people leave, go on vacation, or simply forget why they made a particular decision, the system starts to drift.

The most important thing documentation captures is not *what* was decided but **why**. Recording that your primary button is blue is trivial — anyone can see that in the design file. Recording that the button is that specific blue because it meets WCAG AA contrast requirements against your background color, aligns with the brand's trust-signaling palette, and was tested against three alternatives with users who found it 23% more clickable — that is documentation worth writing. The "why" is what prevents the next designer from changing the button color on a whim and breaking accessibility compliance, or from relitigating a decision that was already thoroughly explored.

Effective design documentation typically captures four layers: the **problem** being solved (what user need or business goal drove this design), the **constraints** considered (technical limitations, accessibility requirements, brand guidelines), the **alternatives explored** (what other approaches were considered and why they were rejected), and the **principles applied** (which design system rules or heuristics guided the final decision). This structure mirrors how design decisions are actually made and provides enough context for someone encountering the documentation months later to understand not just what to do but what *not* to do and why.

The systems-thinking perspective from your prerequisites is critical here: documentation is not a separate artifact bolted onto the design process — it is part of the system itself. A design system without documentation is like a codebase without comments or commit messages: it works today but becomes increasingly opaque over time. The practical test of good documentation is whether a new team member can implement a component correctly, handle an edge case the original designer anticipated, and extend the system in its intended direction — all without asking the original designer a single question. That standard is high, but it is exactly what separates a living, scalable design system from a static style guide that nobody trusts.
