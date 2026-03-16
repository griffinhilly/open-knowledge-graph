---
id: anterior-cingulate-cortex-conflict-monitoring
title: Anterior Cingulate Cortex and Conflict Monitoring
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: attention-networks-brain
  type: hard
- id: executive-control-networks
  type: hard
builds-toward:
- error-related-negativity-neural-basis
- cognitive-control-acc-dlpfc-coupling
tags:
- ACC
- conflict
- error-monitoring
- cognitive-control
- adjustment
stage: advanced
status: draft
---

# Anterior Cingulate Cortex and Conflict Monitoring

## Core Idea
The anterior cingulate cortex (ACC) detects response conflict and error signals, triggering adjustments in cognitive control and attention. ACC shows increased activity when competing responses are activated, when errors occur, and when task difficulty increases, suggesting a conflict-monitoring and adjustment function. This region communicates with dorsolateral prefrontal cortex to implement increased control following conflict.

## Explainer

You've already studied the broader architecture of attention networks and executive control. Now zoom in on a specific functional component: the mechanism by which the brain detects that its own processing has gone wrong — and does something about it. The **anterior cingulate cortex (ACC)**, particularly its dorsal portion (dACC), is the key region here.

The conflict-monitoring framework, developed primarily by Matthew Botvinick and colleagues, proposes that the ACC acts as a detector of **response conflict** — situations where two or more competing responses are simultaneously activated at high levels. In the classic Stroop task, when you see the word "RED" printed in blue ink, your well-practiced word-reading system generates one response ("red") while the color-naming task generates another ("blue"). Both responses are activated, and their co-activation produces conflict. The ACC, monitoring the outputs of processing, detects this simultaneous activation of incompatible responses and signals the need for increased control. This is a computational role: the ACC is not implementing control directly but is evaluating the current state of processing to determine whether control adjustments are needed.

What does "conflict signal" look like in the brain? The **error-related negativity (ERN)** is an event-related potential (ERP) component — a negative-going voltage deflection peaking roughly 50–100ms after an error — that is generated in or near the ACC. When you make a mistake, even before you're consciously aware of it, this signal fires. Importantly, similar signals appear not just for errors but for *correct responses on high-conflict trials* — when you nearly made an error, the same region activates, even though you got it right. This supports the conflict-monitoring interpretation: it's not outcome evaluation (error vs. correct) but conflict detection (competing activations) that drives ACC activity.

The connection to **dorsolateral prefrontal cortex (dlPFC)** is critical to understanding what the ACC actually accomplishes. The ACC is a detector, not an implementer. When it registers high conflict or error, it communicates with the dlPFC — your executive control hub from the prerequisite. The dlPFC then implements increased top-down control on the next trial: greater attention to the relevant dimension, stronger suppression of the irrelevant one. The behavioral signature of this loop is **conflict adaptation**: performance improves on the trial following a high-conflict trial, as if the system "learned" to allocate more control. This post-conflict adjustment is diminished in people with conditions involving ACC dysfunction, including schizophrenia and some anxiety disorders, providing a clear link between the neural mechanism and clinical impairment.
