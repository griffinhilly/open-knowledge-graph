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
tags:
- reward
- motivation
- value
stage: advanced
status: validated
---

# Reward and Motivation Circuits

## Core Idea
The reward circuit involves ventral tegmental area (VTA) dopamine neurons projecting to nucleus accumbens and prefrontal cortex. Phasic dopamine firing increases to rewarding stimuli and omission of expected rewards (prediction error). This learning signal reinforces actions that obtain rewards. Dorsolateral striatum encodes habits; ventromedial striatum encodes value.

## How It's Best Learned
Record VTA dopamine neurons during reward tasks. Trace circuit connectivity using optogenetics.

## Common Misconceptions
Dopamine signals pleasure—it signals prediction error and value. Reward is encoded in one area—it's distributed across striatum, vmPFC, and OFC.

## Questions

```yaml
- question: "A rat is trained over many sessions to press a lever after a tone to receive food. Initially, VTA dopamine neurons fire when the rat eats the food. After extensive training, what pattern would you expect?"
  type: multiple-choice
  options:
    - "Dopamine neurons continue to fire strongly when the rat eats — because eating is always pleasurable regardless of experience"
    - "Dopamine neurons now fire at the tone, and the response to eating the food diminishes toward baseline"
    - "Dopamine neurons fire throughout the entire tone-lever-food sequence with equal magnitude"
    - "Dopamine firing ceases entirely — the rat has learned the sequence and no longer needs a teaching signal"
  answer: 1
  explanation: "This temporal shift is the defining hallmark of reward prediction error signaling. Early in training, the food itself is unexpected, generating a large positive prediction error — dopamine fires at delivery. As learning proceeds, the tone reliably predicts the food, so the dopamine response shifts backward to the earliest predictor (the tone). The food itself, now fully expected, no longer generates a prediction error — dopamine firing at food delivery returns to baseline. This demonstrates that dopamine does not encode pleasure; it encodes the *surprise* of reward relative to expectation."

- question: "A well-trained animal expects food after a tone. On a probe trial, the tone plays but no food is delivered. What happens to dopamine neuron activity at the time when the food would have arrived?"
  type: multiple-choice
  options:
    - "Dopamine firing increases — the animal is alerted and motivated to search for the missing reward"
    - "Dopamine firing stays at baseline — no reward, no signal, so the system is silent"
    - "Dopamine firing drops below baseline — a negative prediction error signaling the outcome was worse than expected"
    - "Dopamine firing first increases then rapidly decreases to encode the disappointment sequence"
  answer: 2
  explanation: "The reward prediction error model predicts three states: positive error (reward better than expected → firing above baseline), no error (reward matches expectation → firing at baseline), and negative error (reward worse than expected, or expected reward omitted → firing below baseline). The omission of an expected reward is a negative prediction error — the outcome was worse than what was predicted. This dip below baseline is the 'anti-reward' signal that teaches the system to reduce the value assigned to the cue. It is the mechanism by which extinction learning occurs."

- question: "An addict who reports that heroin no longer produces euphoria may still compulsively seek the drug because dopamine signaling in the reward circuit has sensitized to drug-associated cues."
  type: true-false
  answer: true
  explanation: "This dissociation between 'wanting' and 'liking' is a key feature of addiction. Tolerance reduces the hedonic impact of the drug itself (opioid receptor downregulation reduces 'liking'), but repeated drug use sensitizes the mesolimbic dopamine circuit to drug-associated cues — needles, locations, people, smells. These cues trigger strong dopamine responses (large positive prediction errors) that drive compulsive seeking behavior ('wanting') even as the drug itself delivers diminishing pleasure. Dopamine encodes incentive salience, not pleasure, which explains why craving can intensify even as enjoyment fades."

- question: "Dopamine neurons in the VTA fire most strongly in response to the subjective pleasantness of a reward experience."
  type: true-false
  answer: false
  explanation: "This is the central misconception about dopamine. VTA dopamine neurons encode reward prediction error — the difference between expected and received reward — not the absolute hedonic value of an experience. A reward that is fully predicted produces no increase in dopamine firing, regardless of how pleasant it is. The clearest evidence is the temporal shift in conditioning: after learning, dopamine fires to the predictive cue (which produces no pleasure itself), not to the reward. Pleasure (hedonic value) is thought to be more closely tied to opioid signaling in the nucleus accumbens shell, not dopamine."

- question: "A patient with early Parkinson's disease has lost dopaminergic neurons primarily in the substantia nigra, but their neurologist notes they also show reduced motivation and difficulty learning which new behaviors lead to positive outcomes. How does the prediction error function of dopamine explain these non-motor symptoms?"
  type: short-answer
  answer: "Dopamine prediction error signals are necessary for reinforcement learning — they update the value estimates stored in striatal and prefrontal circuits that guide motivated behavior. Without a reliable prediction error signal, the brain cannot update its model of which actions lead to reward. The patient would have difficulty learning that a new behavior produces a good outcome, because the dopamine 'teaching signal' that would reinforce the behavior is absent or degraded. Reduced motivation follows because the mesolimbic pathway (VTA → nucleus accumbens) encodes incentive salience — the drive to pursue predicted rewards. Depleted dopamine signaling reduces this drive, producing the amotivation and anhedonia characteristic of both Parkinson's disease and depression."
  explanation: "The non-motor symptoms of Parkinson's disease are among the strongest clinical evidence for the prediction error theory of dopamine. They also illustrate that different dopamine pathways serve different functions: the nigrostriatal pathway (substantia nigra → dorsal striatum) controls movement, the mesolimbic pathway (VTA → nucleus accumbens) controls reward motivation, and the mesocortical pathway (VTA → PFC) controls value-based decision making. Early Parkinson's affects the nigrostriatal pathway most severely, but as the disease progresses, VTA neurons also degenerate, producing the motivational and learning deficits described."
```

## Explainer

From your study of the dopamine system, you know that dopaminergic neurons in the midbrain project widely to the striatum and cortex, and that dopamine plays a key role in movement, motivation, and learning. The reward and motivation circuitry builds on this foundation by explaining *how* the brain uses dopamine to learn which actions lead to good outcomes and to motivate the pursuit of those outcomes. The central insight is that dopamine does not simply signal pleasure — it signals **reward prediction error**, the difference between expected and received reward.

The core of the circuit is the **ventral tegmental area** (VTA), a midbrain nucleus whose dopamine neurons project along two major pathways. The **mesolimbic pathway** targets the **nucleus accumbens** (NAc) in the ventral striatum, which is the key structure for evaluating reward value and invigorating motivated behavior. The **mesocortical pathway** targets the **prefrontal cortex** (PFC), particularly the orbitofrontal cortex (OFC) and ventromedial PFC (vmPFC), which represent the subjective value of options and guide decision-making. When a VTA dopamine neuron fires a **phasic burst**, it signals a positive prediction error — "this outcome was better than expected." When an expected reward is omitted, dopamine firing drops below baseline — a negative prediction error signaling "this was worse than expected." When reward matches expectation exactly, there is no change in firing. This three-part signal is mathematically equivalent to the teaching signal in computational reinforcement learning models, a connection that earned Wolfram Schultz and colleagues wide recognition.

What makes this circuit a learning system rather than just a pleasure meter is how prediction errors reshape behavior over time. Initially, dopamine neurons fire when the reward itself arrives (you take a bite of unexpected cake). But as learning progresses, the dopamine response shifts backward in time to the earliest reliable predictor of reward (the sight of the bakery sign). The reward itself no longer triggers a dopamine burst because it is now fully predicted. This temporal shift means that dopamine is teaching the brain's value system — gradually training the NAc, OFC, and vmPFC to assign accurate value estimates to cues, contexts, and actions that predict future rewards. The dorsolateral striatum enters the picture as well-learned action sequences become **habits**: stimulus-response associations that run automatically, no longer dependent on current outcome expectations.

The distributed nature of reward processing explains why motivation is not a simple on-off switch. The NAc integrates dopamine signals with glutamatergic input from the hippocampus (contextual information), amygdala (emotional significance), and PFC (goals and plans) to determine whether and how vigorously to pursue a reward. The OFC tracks the current value of specific outcomes (devaluing food after satiety, for example), while the vmPFC integrates across outcome types to support choice. Disruptions at different points in this circuit produce different pathologies: VTA-to-NAc dysfunction underlies the anhedonia and amotivation seen in depression, while hypersensitized dopamine signaling in this pathway contributes to the compulsive reward-seeking of addiction — where the prediction error signal becomes exaggerated for drug-associated cues even as the actual pleasure from the drug diminishes with tolerance.
