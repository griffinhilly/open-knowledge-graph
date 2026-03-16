---
id: cerebellum
title: 'Cerebellum: Motor Coordination and Learning'
domain: biology
course: neuroscience
prerequisites:
- id: long-term-depression
  type: hard
- id: motor-cortex
  type: soft
tags:
- motor-systems
- learning
stage: advanced
status: draft
---

# Cerebellum: Motor Coordination and Learning

## Core Idea
Learns to cancel prediction errors through LTD at parallel fiber-Purkinje synapse. Climbing fibers carry error; LTD updates cerebellar output to match predicted outcomes.

## Explainer

From your study of long-term depression and the motor cortex, you know that synaptic connections can be weakened through sustained activity patterns and that the motor cortex generates the commands that initiate voluntary movement. The **cerebellum** sits downstream of this process — it does not initiate movement but rather refines it, acting as a real-time error-correction system that learns to predict and cancel the discrepancy between what you intended to do and what actually happened.

The cerebellum's computational architecture is strikingly uniform and well understood. The principal output neurons are **Purkinje cells** — enormous neurons with elaborate dendritic trees that receive two fundamentally different types of input. **Parallel fibers**, the axons of granule cells, carry a massive convergence of sensory and motor context information — each Purkinje cell receives input from roughly 200,000 parallel fibers. **Climbing fibers**, which originate from the inferior olive in the brainstem, carry error signals — they fire when there is a mismatch between the predicted and actual outcome of a movement. Each Purkinje cell receives input from just one climbing fiber, and when it fires, it produces a powerful, unmistakable "complex spike" that temporarily overwhelms the cell.

The learning rule is elegant: when a climbing fiber fires (signaling an error) at the same time that particular parallel fibers are active, the synapses between those parallel fibers and the Purkinje cell undergo **long-term depression (LTD)** — they become weaker. Over repeated trials, this weakening adjusts the Purkinje cell's output so that its firing pattern better compensates for the error. Since Purkinje cells are inhibitory (they release GABA onto deep cerebellar nuclei), weakening their input changes the pattern of inhibition on downstream motor circuits, ultimately refining the motor command. Think of it like tuning a musical instrument: each error signal tells the system which "strings" are out of tune, and LTD adjusts them until the output matches the target.

This error-correction framework explains a wide range of clinical observations. Cerebellar damage does not cause paralysis — the motor cortex still generates commands — but it produces **ataxia**: movements become clumsy, poorly timed, and inaccurate. Patients overshoot when reaching for objects (dysmetria), their speech becomes slurred (dysarthria), and they cannot smoothly track moving targets with their eyes. The cerebellum's role also extends beyond motor control. Recent research shows it contributes to cognitive timing, language processing, and emotional regulation, likely using the same prediction-error architecture applied to non-motor domains. The uniform circuitry of the cerebellum suggests it performs a single fundamental computation — prediction error cancellation — that the brain repurposes across many functional contexts.
