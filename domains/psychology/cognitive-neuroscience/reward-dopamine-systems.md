---
id: reward-dopamine-systems
title: Reward Learning and Dopamine Circuits
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: dopamine-reward-system
  type: hard
- id: reward-motivation-circuits
  type: hard
builds-toward:
- neuroeconomics-value-computation
tags:
- reward
- dopamine
- learning
stage: advanced
status: draft
---

# Reward Learning and Dopamine Circuits

## Core Idea
Dopamine neurons in ventral tegmental area signal reward prediction errors—the discrepancy between expected and actual reward—that update value estimates. These error signals train downstream regions (striatum, prefrontal cortex) to predict and pursue rewarding outcomes. Dopamine's role extends beyond reward to motivation, attention, and learning, explaining dopamine dysfunction in addiction (sensitized reward system), depression (reduced motivation), and schizophrenia (aberrant predictions).

## Explainer

You already know from your study of the dopamine reward system that dopamine is released in the nucleus accumbens and other striatal regions in response to rewards. The key conceptual advance in this topic is understanding *when* and *why* dopamine neurons fire — and the answer is stranger and more powerful than "when something rewarding happens." Dopamine neurons don't simply respond to reward. They respond to **prediction error**: the difference between what was expected and what actually occurred.

Think through a learning sequence. The first time an unexpected food reward arrives, dopamine neurons in the **ventral tegmental area (VTA)** fire a burst at the moment of the reward itself. But after repeated pairings of a tone with that food, something shifts: dopamine neurons start firing at the tone — the predictive cue — rather than the reward. If the reward then arrives on schedule, dopamine activity at reward delivery returns to baseline (no surprise, no error). If the reward is omitted, dopamine activity *dips below baseline* — a negative prediction error signaling "expected but didn't get." This temporal shift is the neural signature of learning. The reward signal has migrated to the earliest reliable predictor of reward, which is exactly what an efficient learning system should do.

The downstream consequence of these prediction error signals is that the **striatum** and **prefrontal cortex** learn to assign value to stimuli and actions. When dopamine is released at a cue (positive prediction error), the synaptic weights connecting that cue's representation to the action that produced reward are strengthened. This is the neurobiological implementation of the reinforcement learning principle: actions followed by unexpected good outcomes are selected more often; actions followed by unexpected bad outcomes are selected less often. The prefrontal cortex uses dopamine signals to maintain and update value estimates, informing planning and goal-directed behavior.

Dopamine dysfunction across clinical conditions reflects failures in this prediction error machinery. In **addiction**, drugs of abuse produce dopamine surges that dwarf natural rewards, training the system to assign enormous value to drug-related cues while natural rewards lose their signaling power — explaining why addicted individuals find normal pleasures flat. In **depression**, reduced tonic dopamine activity impairs motivation and the sense that actions lead to rewards (anhedonia) — the system underestimates the value of engaging with the world. In **schizophrenia**, aberrant dopamine activity generates false positive prediction errors, causing neutral stimuli to acquire spurious salience — a plausible mechanism for delusion formation, where the person experiences ordinary things as deeply meaningful. The same machinery that makes learning possible, when miscalibrated, produces dramatically different behavioral pathologies.
