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
stage: expert
status: draft
---

# Reward Learning and Dopamine Circuits

## Core Idea
Dopamine neurons in ventral tegmental area signal reward prediction errors—the discrepancy between expected and actual reward—that update value estimates. These error signals train downstream regions (striatum, prefrontal cortex) to predict and pursue rewarding outcomes. Dopamine's role extends beyond reward to motivation, attention, and learning, explaining dopamine dysfunction in addiction (sensitized reward system), depression (reduced motivation), and schizophrenia (aberrant predictions).

## Questions

```yaml
- question: "An animal has been thoroughly conditioned: a tone reliably predicts food. On a test trial, the tone sounds but no food is delivered. What happens to VTA dopamine neuron activity at the moment the food would have arrived?"
  type: multiple-choice
  options:
    - "Dopamine activity surges, because the animal is highly motivated by hunger at that moment"
    - "Dopamine activity is unchanged from baseline, because no food arrived and no prediction was made"
    - "Dopamine activity dips below baseline — a negative prediction error signal"
    - "Dopamine activity increases at the tone and then returns to baseline when food is omitted"
  answer: 2
  explanation: "After conditioning, the brain predicts food at a specific time. When food fails to arrive, dopamine neurons generate a negative prediction error: activity falls *below* baseline at the moment reward was expected but absent. This is the neural signal for 'worse than expected.' It is not merely silence — the dip is an active downward signal that weakens the value assigned to preceding events. This asymmetry (burst for better-than-expected, dip for worse-than-expected) is the key signature of prediction error coding."

- question: "After extensive training with a tone-food pairing, when does the dopamine burst primarily occur during a successful trial (tone sounds, food delivered on schedule)?"
  type: multiple-choice
  options:
    - "At the moment of food delivery, because dopamine codes the presence of reward"
    - "At the tone onset, because it is now the earliest reliable predictor of reward"
    - "Equally at both the tone and food delivery, because both events are associated with reward"
    - "Only when the food is eaten, reflecting the pleasurable taste experience"
  answer: 1
  explanation: "This temporal shift is the hallmark of learned prediction error signaling. Early in training, dopamine fires at the unexpected food reward. As the tone reliably predicts food, the dopamine burst migrates backward to the tone — the earliest predictor. The dopamine response at food delivery itself returns to baseline (no surprise = no prediction error). The system has learned what predicts reward and signals that learning by moving the burst to the predictive cue. If the tone itself were predictable by an earlier cue, the burst would migrate back further still."

- question: "Dopamine neurons fire most strongly in response to rewards themselves, and their firing rate at the time of reward delivery stays elevated even after extensive conditioning."
  type: true-false
  answer: false
  explanation: "This is the central misconception about dopamine and reward. What dopamine actually encodes is prediction error — the discrepancy between what was expected and what occurred. After conditioning, the animal fully predicts the reward following the cue, so there is no positive prediction error at delivery, and dopamine activity at that moment returns to baseline. The burst now occurs at the conditioned cue. Dopamine responding to rewards themselves describes only early, unexpected encounters with reward — it is a learning signal, not a 'pleasure signal' that fires whenever something good happens."

- question: "In addiction, drugs of abuse can sensitize the dopamine prediction error system to assign enormous value to drug-related cues, even as natural rewards like food and social connection lose their ability to activate the system effectively."
  type: true-false
  answer: true
  explanation: "Drugs of abuse produce dopamine surges far larger than natural rewards — often 5–10× the normal signal. This massive 'prediction error' trains the system to assign enormous value to drug-related cues (paraphernalia, environments, people associated with drug use). Meanwhile, the system's baseline recalibrates such that natural rewards, which produce much smaller dopamine signals, appear to generate insufficient prediction errors to sustain motivation — the neural substrate of anhedonia and the compulsive focus on drug-seeking over natural pleasures."

- question: "Why does dopamine fire at a conditioned stimulus rather than at the reward itself after learning is complete, and what would happen to dopamine activity if the expected reward were suddenly and permanently omitted?"
  type: short-answer
  answer: "Dopamine encodes prediction error (actual − expected reward), not reward itself. Once a cue reliably predicts reward, the animal fully expects the reward at delivery — so there is no positive prediction error, and dopamine at reward delivery returns to baseline. The dopamine burst migrates to the cue because the cue is where the first 'better-than-expected' signal now occurs (the cue was unexpected before it became a predictor). If the expected reward is permanently omitted, dopamine initially dips below baseline at the expected reward time (negative prediction error). Over repeated omissions, the cue itself stops predicting reward, the conditioned response extinguishes, and the dopamine burst at the cue disappears — the system unlearns the association through repeated negative prediction errors."
  explanation: "This migration of the dopamine signal is not a quirk — it is exactly what a rational learning system should do. Resources and attention should be directed to the earliest reliable signal of a coming reward, not to the reward itself when it's already certain. The extinguishing of the cue response when reward is permanently omitted shows the same mechanism in reverse: negative prediction errors at omission, then at the cue, systematically downgrade the value estimate until the cue is no longer worth responding to."
```

## Explainer

You already know from your study of the dopamine reward system that dopamine is released in the nucleus accumbens and other striatal regions in response to rewards. The key conceptual advance in this topic is understanding *when* and *why* dopamine neurons fire — and the answer is stranger and more powerful than "when something rewarding happens." Dopamine neurons don't simply respond to reward. They respond to **prediction error**: the difference between what was expected and what actually occurred.

Think through a learning sequence. The first time an unexpected food reward arrives, dopamine neurons in the **ventral tegmental area (VTA)** fire a burst at the moment of the reward itself. But after repeated pairings of a tone with that food, something shifts: dopamine neurons start firing at the tone — the predictive cue — rather than the reward. If the reward then arrives on schedule, dopamine activity at reward delivery returns to baseline (no surprise, no error). If the reward is omitted, dopamine activity *dips below baseline* — a negative prediction error signaling "expected but didn't get." This temporal shift is the neural signature of learning. The reward signal has migrated to the earliest reliable predictor of reward, which is exactly what an efficient learning system should do.

The downstream consequence of these prediction error signals is that the **striatum** and **prefrontal cortex** learn to assign value to stimuli and actions. When dopamine is released at a cue (positive prediction error), the synaptic weights connecting that cue's representation to the action that produced reward are strengthened. This is the neurobiological implementation of the reinforcement learning principle: actions followed by unexpected good outcomes are selected more often; actions followed by unexpected bad outcomes are selected less often. The prefrontal cortex uses dopamine signals to maintain and update value estimates, informing planning and goal-directed behavior.

Dopamine dysfunction across clinical conditions reflects failures in this prediction error machinery. In **addiction**, drugs of abuse produce dopamine surges that dwarf natural rewards, training the system to assign enormous value to drug-related cues while natural rewards lose their signaling power — explaining why addicted individuals find normal pleasures flat. In **depression**, reduced tonic dopamine activity impairs motivation and the sense that actions lead to rewards (anhedonia) — the system underestimates the value of engaging with the world. In **schizophrenia**, aberrant dopamine activity generates false positive prediction errors, causing neutral stimuli to acquire spurious salience — a plausible mechanism for delusion formation, where the person experiences ordinary things as deeply meaningful. The same machinery that makes learning possible, when miscalibrated, produces dramatically different behavioral pathologies.
