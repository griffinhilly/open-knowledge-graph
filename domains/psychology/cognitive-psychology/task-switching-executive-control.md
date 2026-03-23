---
id: task-switching-executive-control
title: Task Switching and Executive Control Costs
domain: psychology
course: cognitive-psychology
prerequisites:
- id: stroop-interference-semantic-control
  type: hard
- id: attention-capacity-and-bottlenecks
  type: soft
tags:
- executive-control
- task-switching
- attention
- costs
stage: formal-systems
status: draft
---

# Task Switching and Executive Control Costs

## Core Idea
Switching between tasks produces switch costs: slowed responses and higher error rates following task switches versus repetitions. Switch costs reflect time to reconfigure task-set and suppress interference from prior task demands. Costs increase with task dissimilarity and complexity, demonstrating executive control demands of mental flexibility.

## Questions

```yaml
- question: "Participants are given a generous preparation interval and told exactly which task is coming next before each switch trial. Responses on switch trials are still slower than on repeat trials. What does this residual switch cost demonstrate?"
  type: multiple-choice
  options:
    - "The participants failed to use the preparation interval effectively"
    - "Switching involves a cognitive cost that advance preparation cannot fully pre-resolve"
    - "Long preparation intervals paradoxically increase switch costs through over-preparation"
    - "Switch costs are entirely due to surprise, and the design failed to eliminate surprise"
  answer: 1
  explanation: "The residual switch cost — the cost that persists even after full advance preparation — is the central theoretical finding of task-switching research. It shows that switching is not merely about being caught off guard or having insufficient time to prepare. There is a proactive interference component: the prior task-set persists and must be overcome at the moment of the switch itself. Preparation can accomplish partial reconfiguration but cannot dissolve the carryover from the previous task, revealing a genuine architectural cost of cognitive flexibility."

- question: "What distinguishes a 'switch cost' from a 'mixing cost' in task-switching paradigms?"
  type: multiple-choice
  options:
    - "Switch costs occur on error trials; mixing costs occur on correct trials"
    - "Switch costs are the penalty on task-switch trials relative to repeat trials; mixing costs are the slowing on all trials in a mixed block relative to a pure single-task block"
    - "Switch costs reflect response competition; mixing costs reflect perceptual interference"
    - "Mixing costs apply only when tasks share stimulus modalities; switch costs apply otherwise"
  answer: 1
  explanation: "Switch costs capture the specific penalty of the task-transition — slower responses and higher errors on switch trials versus repeat trials within the same block. Mixing costs capture the broader overhead of holding two task-sets simultaneously: even on repeat trials in a mixed block, responses are slower than in a pure single-task block. Mixing costs reflect the standing executive demand of maintaining two tasks in readiness, independent of whether a switch just occurred. Together they reveal two distinct sources of cognitive cost from task flexibility."

- question: "If a person knows exactly which task is coming next and is given a long preparation interval, switch costs will be eliminated."
  type: true-false
  answer: false
  explanation: "This is one of the most replicated findings in executive control research. Longer preparation intervals reduce switch costs — reconfiguration can be partially completed in advance — but residual costs reliably remain. The residual reflects task-set carryover: the prior task-set persists and must be overcome at the moment of switching, a process that cannot be fully accomplished before the switch occurs. If switch costs were entirely due to insufficient preparation, long forewarning would eliminate them entirely — the fact that it doesn't reveals a genuine irreducible cost."

- question: "Switching between two tasks that compete for the same cognitive resources — same stimulus dimension, same response channel — typically produces larger switch costs than switching between tasks using entirely different inputs and outputs."
  type: true-false
  answer: true
  explanation: "Switch costs scale with the degree of competition between task-sets. When tasks share representations or response channels, the prior task-set more powerfully interferes with the incoming one — the carryover is stronger and harder to overcome. Tasks using different modalities, different effectors, or different decision rules compete less, producing smaller proactive interference and therefore smaller switch costs. This relationship is informative about the mechanism: it is not the act of switching per se that is costly, but the interference from a prior task-set that occupies shared cognitive resources."

- question: "Why does the residual switch cost — the cost remaining even after full advance preparation — matter for understanding the cognitive architecture of executive control?"
  type: short-answer
  answer: "The residual switch cost shows that cognitive flexibility has an irreducible cost not attributable to surprise or inadequate preparation. If reconfiguration could be fully pre-completed, long forewarning would eliminate switch costs; it doesn't. This means the prior task-set persists as proactive interference that must be resolved at the moment of transition — the cognitive system cannot simply 'delete' the previous task context. This reveals something fundamental about executive control: flexibility is not free, and the cost of changing cognitive context is partly inescapable, providing a window into the architecture of how the executive system manages competing task demands."
  explanation: "This finding led researchers to distinguish two separable mechanisms: task-set reconfiguration (proactive preparation, reducible by forewarning) and task-set carryover or proactive interference (residual from the prior task, not fully reducible). The two can be experimentally dissociated, and the residual component localizes to the moment of switching itself — the prior task must be actively inhibited or overwritten, a process that can begin but not complete before the new trial begins."
```

## Explainer

From your study of the Stroop task, you know that well-practiced automatic processes — like reading a written word — exert influence on cognition even when they are task-irrelevant. The Stroop interference effect demonstrates that you cannot simply turn off an automatic process just by intending to. Task switching extends this insight from within-task conflict to between-task transitions: how does the cognitive system shift from doing one thing to doing something entirely different, and what costs does this incur? The answer reveals something fundamental about the executive control system and the nature of cognitive flexibility.

The core phenomenon is the **switch cost**: when participants alternate between two tasks — say, on one trial judge whether a digit is odd or even, on the next judge whether it is greater or less than 5 — responses are slower and more error-prone on switch trials than on task-repeat trials. This is expected. What is theoretically important is the **residual switch cost**: even when participants are given a long preparation interval and know exactly which task is coming next, some cost remains. Full advance preparation does not eliminate switching difficulty. This residual cost shows that switching involves something beyond mere surprise or insufficient preparation — there is a cost to changing cognitive context that preparation cannot fully pre-resolve.

Two mechanisms contribute to switch costs and can be experimentally dissociated. **Task-set reconfiguration** is the proactive process of preparing for the new task: retrieving the relevant rules from memory, orienting attention toward the relevant stimulus dimension, and priming the appropriate response mappings. Longer preparation intervals reduce (but don't eliminate) switch costs — the reconfiguration can be partially accomplished in advance. **Task-set carryover**, or **proactive interference**, is the residual that remains even after full preparation: the prior task-set persists and interferes with the new one. Connecting back to your study of attention capacity and bottlenecks: this can be understood as the prior task occupying working memory resources or biasing attentional orienting that needs to be redirected. The previous task is not simply "turned off" — it leaves a residue that the system must overcome.

The magnitude of switch costs scales with the degree to which the two tasks compete for the same cognitive resources. Switching between tasks that use different input modalities, different response hands, or different decision rules produces smaller costs than switching between tasks that share representations and response channels. A related phenomenon is the **mixing cost**: the mere presence of two tasks in a block slows responses on both, even on repeat trials, compared to blocks requiring only a single task. Mixing costs reflect the standing overhead of maintaining two task-sets simultaneously — the executive system must hold both tasks active and ready, consuming resources that would otherwise be fully available for the current task. Together, switch costs and mixing costs reveal that mental flexibility is not free: the executive system pays a real computational price for maintaining and switching between competing task demands, and that price provides a window into the architecture of cognitive control.
