---
id: motor-learning-cerebellar
title: Motor Learning and Cerebellar Adaptation
domain: biology
course: neuroscience
prerequisites:
- id: cerebellum-motor-coordination
  type: hard
- id: long-term-depression
  type: hard
builds-toward:
- cerebellar-circuits
- error-correction
tags:
- motor-learning
- adaptation
- cerebellum
stage: advanced
status: draft
---

# Motor Learning and Cerebellar Adaptation

## Core Idea
The cerebellum learns motor tasks through supervised learning: Purkinje cells receive parallel fiber inputs (sensory prediction) and climbing fiber inputs (error signals). Coincident parallel fiber-climbing fiber activation causes LTD at Purkinje synapses, weakening incorrect predictions. This generates internal models enabling smooth, coordinated movement.

## How It's Best Learned
Simulate cerebellar learning for smooth pursuit. Record Purkinje cells during learning.

## Common Misconceptions
The cerebellum drives movement—it learns predictive models. All cerebellar learning is depression—LTP also occurs.

## Explainer

From your study of cerebellar anatomy, you know that the cerebellum coordinates movement through a highly regular circuit involving granule cells, Purkinje cells, and deep cerebellar nuclei. You also understand that long-term depression weakens synaptic connections. **Motor learning** in the cerebellum is where these two concepts converge: the cerebellum uses LTD at specific synapses to learn from movement errors, gradually building internal models that allow you to perform skilled actions smoothly and automatically.

The circuit implements a form of **supervised learning** — a concept borrowed from machine learning, but one that the cerebellum invented hundreds of millions of years before computers. The "teacher" signal arrives via **climbing fibers** from the inferior olive, each of which wraps around a single Purkinje cell with extraordinary intimacy, making hundreds of synaptic contacts. A climbing fiber fires when a movement error occurs — when the actual sensory outcome of a movement does not match the predicted outcome. Meanwhile, **parallel fibers** (the axons of granule cells) carry contextual information about the current state of the body and the intended movement, converging on the same Purkinje cell from a vast number of granule cells. When a parallel fiber input and a climbing fiber error signal arrive at a Purkinje cell at the same time, the parallel fiber synapse undergoes **LTD** — it is weakened. The logic is elegant: the parallel fiber pattern that was active during an erroneous movement becomes less effective at driving that Purkinje cell, effectively removing the incorrect motor command from the repertoire.

Consider learning to throw darts. Your first throws scatter widely. Each errant throw generates a climbing fiber error signal that weakens the specific pattern of parallel fiber inputs that contributed to the bad throw. Over dozens of trials, the surviving parallel fiber patterns — those that were not paired with error signals — come to dominate Purkinje cell output. The result is a refined **internal model**: a learned mapping from intended action to the motor commands that actually produce the desired outcome. This is why cerebellar learning feels like movements becoming automatic rather than consciously computed. Your cerebral cortex initiates the intention to throw; the cerebellum provides the calibrated predictions that make the throw accurate.

Critically, the cerebellum does not only learn through depression. **Long-term potentiation** at parallel fiber–Purkinje cell synapses also occurs, particularly during periods of parallel fiber activity without climbing fiber coincidence. This bidirectional plasticity allows the system to both weaken incorrect predictions and strengthen correct ones. Furthermore, plasticity is not confined to the cerebellar cortex — synapses in the **deep cerebellar nuclei** also undergo learning-related changes, providing a second site of memory storage that may consolidate motor memories over longer timescales. Patients with cerebellar damage do not lose the ability to move (the motor cortex handles that), but they lose the ability to learn new motor skills, adapt existing movements to changing conditions, and maintain the calibration of movements they previously performed effortlessly — revealing the cerebellum's true role as the brain's motor learning engine.
