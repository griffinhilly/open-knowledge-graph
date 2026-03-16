---
id: reward-motivation-circuits
title: Reward and Motivation Circuits
domain: biology
course: neuroscience
prerequisites:
- id: dopamine-system
  type: hard
- id: basal-ganglia-motor-selection
  type: soft
builds-toward:
- reinforcement-learning
- addiction-mechanisms
tags:
- reward
- motivation
- value
stage: advanced
status: draft
---

# Reward and Motivation Circuits

## Core Idea
The reward circuit involves ventral tegmental area (VTA) dopamine neurons projecting to nucleus accumbens and prefrontal cortex. Phasic dopamine firing increases to rewarding stimuli and omission of expected rewards (prediction error). This learning signal reinforces actions that obtain rewards. Dorsolateral striatum encodes habits; ventromedial striatum encodes value.

## How It's Best Learned
Record VTA dopamine neurons during reward tasks. Trace circuit connectivity using optogenetics.

## Common Misconceptions
Dopamine signals pleasure—it signals prediction error and value. Reward is encoded in one area—it's distributed across striatum, vmPFC, and OFC.

## Explainer

From your study of the dopamine system, you know that dopaminergic neurons in the midbrain project widely to the striatum and cortex, and that dopamine plays a key role in movement, motivation, and learning. The reward and motivation circuitry builds on this foundation by explaining *how* the brain uses dopamine to learn which actions lead to good outcomes and to motivate the pursuit of those outcomes. The central insight is that dopamine does not simply signal pleasure — it signals **reward prediction error**, the difference between expected and received reward.

The core of the circuit is the **ventral tegmental area** (VTA), a midbrain nucleus whose dopamine neurons project along two major pathways. The **mesolimbic pathway** targets the **nucleus accumbens** (NAc) in the ventral striatum, which is the key structure for evaluating reward value and invigorating motivated behavior. The **mesocortical pathway** targets the **prefrontal cortex** (PFC), particularly the orbitofrontal cortex (OFC) and ventromedial PFC (vmPFC), which represent the subjective value of options and guide decision-making. When a VTA dopamine neuron fires a **phasic burst**, it signals a positive prediction error — "this outcome was better than expected." When an expected reward is omitted, dopamine firing drops below baseline — a negative prediction error signaling "this was worse than expected." When reward matches expectation exactly, there is no change in firing. This three-part signal is mathematically equivalent to the teaching signal in computational reinforcement learning models, a connection that earned Wolfram Schultz and colleagues wide recognition.

What makes this circuit a learning system rather than just a pleasure meter is how prediction errors reshape behavior over time. Initially, dopamine neurons fire when the reward itself arrives (you take a bite of unexpected cake). But as learning progresses, the dopamine response shifts backward in time to the earliest reliable predictor of reward (the sight of the bakery sign). The reward itself no longer triggers a dopamine burst because it is now fully predicted. This temporal shift means that dopamine is teaching the brain's value system — gradually training the NAc, OFC, and vmPFC to assign accurate value estimates to cues, contexts, and actions that predict future rewards. The dorsolateral striatum enters the picture as well-learned action sequences become **habits**: stimulus-response associations that run automatically, no longer dependent on current outcome expectations.

The distributed nature of reward processing explains why motivation is not a simple on-off switch. The NAc integrates dopamine signals with glutamatergic input from the hippocampus (contextual information), amygdala (emotional significance), and PFC (goals and plans) to determine whether and how vigorously to pursue a reward. The OFC tracks the current value of specific outcomes (devaluing food after satiety, for example), while the vmPFC integrates across outcome types to support choice. Disruptions at different points in this circuit produce different pathologies: VTA-to-NAc dysfunction underlies the anhedonia and amotivation seen in depression, while hypersensitized dopamine signaling in this pathway contributes to the compulsive reward-seeking of addiction — where the prediction error signal becomes exaggerated for drug-associated cues even as the actual pleasure from the drug diminishes with tolerance.
