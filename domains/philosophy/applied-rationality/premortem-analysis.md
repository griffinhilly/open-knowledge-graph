---
id: premortem-analysis
title: "Premortem Analysis"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: debiasing-techniques
    type: hard
  - id: the-planning-fallacy
    type: soft
builds-toward:
  - murphyjitsu
tags: ["debiasing", "planning", "risk", "technique"]
stage: advanced
status: draft
---

## Core Idea

A premortem asks: "Imagine this project has failed. Why did it fail?" By assuming failure has already occurred, the technique bypasses optimism bias and social pressure to be supportive, giving team members permission to voice concerns. Gary Klein, who developed the technique, found that premortems increase the ability to identify reasons for potential failure by 30%. The mechanism works because imagining a concrete failure is cognitively easier than imagining abstract risks — it leverages narrative thinking (System 1) to identify problems that analytical risk assessment (System 2) misses. Premortems are most valuable at the start of a project, when there is still time to adjust the plan.

## How It's Best Learned

Run a premortem on your next significant decision or project. Write "It is [future date] and this has failed" at the top of a page, then list every plausible reason for failure you can think of in 5 minutes. Compare the list to a standard risk assessment — the premortem typically surfaces risks the standard approach misses.

## Common Misconceptions

- A premortem is not pessimism — it is a structured technique for surfacing risks that optimism bias would otherwise hide.
- The premortem does not replace risk analysis — it complements it by accessing a different cognitive mode.

## Questions

```yaml
- question: "A project team runs both a standard risk assessment and a premortem on the same proposed launch. The premortem surfaces three critical failure modes the risk assessment missed. What best explains this?"
  type: multiple-choice
  options:
    - "The premortem included more participants, so more total information was gathered"
    - "Assuming failure has already occurred activates narrative thinking that bypasses optimism bias and social pressure, surfacing risks invisible to analytical risk assessment"
    - "Risk assessments are structurally biased toward overestimating success due to flawed methodology"
    - "The premortem takes longer, giving participants more time to think of risks"
  answer: 1
  explanation: "The mechanism is cognitive, not procedural. When asked 'what risks might occur?', optimism bias suppresses concerns and social pressure makes people reluctant to voice pessimism. When told 'the project has already failed — why?', two things change: imagining a concrete failure is cognitively easier than speculating about abstract risks (narrative/System 1 thinking), and explaining a fait accompli removes the social stigma of pessimism. The premortem accesses a different cognitive mode, which is why it surfaces risks that analytical checklists miss — not because it uses more people or more time."

- question: "When is a premortem most valuable?"
  type: multiple-choice
  options:
    - "After a project completes successfully, to document what contributed to its success"
    - "Immediately after a real failure, when the team has fresh information about what went wrong"
    - "At the start of a significant project, while plans can still be adjusted based on identified risks"
    - "During mid-project reviews, when actual problems are beginning to emerge"
  answer: 2
  explanation: "A premortem is a prospective tool: it uses imagined failure to improve the plan before execution makes changing course costly. Gary Klein explicitly notes it is most valuable at the project's start. After a real failure, you have actual data — a post-mortem is appropriate then. During execution, some risks have already materialized. The premortem's distinctive value is identifying failure modes early enough that the plan can be adjusted to address them."

- question: "A premortem is best described as a form of pessimism — a deliberate exercise in imagining failure that undermines team confidence and morale."
  type: true-false
  answer: false
  explanation: "A premortem is a structured debiasing technique, not pessimism. It temporarily adopts the assumption of failure to surface risks that optimism bias would hide, then uses that information to strengthen the plan. Teams that complete premortems don't abandon their projects — they adjust plans to address identified weaknesses, often producing warranted increases in confidence. Conflating the technique with pessimism is the common misconception that prevents organizations from using it."

- question: "Simply asking team members 'what could go wrong?' before a project produces the same risk-identification benefits as a formal premortem, since both invite critical thinking about failure."
  type: true-false
  answer: false
  explanation: "The key difference is cognitive framing. 'What could go wrong?' is prospective and speculative — it runs directly into optimism bias (the team expects success) and social pressure (nobody wants to be the pessimist). 'The project has failed — why?' assumes failure as a given, bypassing both. The mechanism is prospective hindsight: imagining a concrete past failure is cognitively much easier than speculating about future risks. The formal structure of the premortem — framing failure as a fait accompli — is what activates the different cognitive mode."

- question: "Explain the cognitive mechanism by which a premortem produces better failure-mode identification than standard risk analysis. Why does assuming failure has already occurred matter?"
  type: short-answer
  answer: "The premortem works through prospective hindsight: framing failure as an accomplished fact activates the narrative reasoning we use to explain events that have already happened. Explaining a past failure is cognitively easier than imagining a future one — the mind naturally constructs causal stories about concrete events. This engages System 1 (fast, narrative, pattern-based) thinking that analytical risk checklists (System 2) miss. It also removes social pressure: team members are explaining a done thing, not predicting their colleagues' work will fail, making concerns socially acceptable to voice."
  explanation: "Standard risk analysis asks people to speculate against a background assumption of success. Optimism bias suppresses failure-probability estimates. Social dynamics discourage naming specific failure modes tied to specific colleagues' work. The premortem sidesteps all of this by establishing failure as the premise — the exercise becomes 'explain this' rather than 'predict this,' a cognitively and socially different task. Gary Klein's research found this produced roughly 30% more identified failure modes compared to standard prospective risk assessment."
```
