---
id: psychostimulant-cocaine-methamphetamine-mechanisms
title: 'Psychostimulant Mechanisms: Cocaine and Methamphetamine'
domain: psychology
course: biological-psychology
prerequisites:
- id: monoamine-synthesis-and-catabolism
  type: hard
- id: dopamine-receptor-subtypes-and-signaling
  type: hard
builds-toward:
- addiction-and-reward-system-plasticity
- stimulant-use-disorder
tags:
- cocaine
- methamphetamine
- dopamine
- stimulants
- addiction
stage: formal-systems
status: validated
---

# Psychostimulant Mechanisms: Cocaine and Methamphetamine

## Core Idea
Cocaine and methamphetamine both increase dopamine by blocking the dopamine transporter (DAT), but via different mechanisms: cocaine is a competitive antagonist, while methamphetamine also releases dopamine by reversing DAT via amphetamine-type release. Both produce brief intense euphoria through accumbens dopamine surge followed by rapid offset, creating powerful negative reinforcement driving compulsive use. Chronic use produces hypofunctional dopamine systems (reduced D2 receptor availability), anhedonia, and cognitive impairment.

## How It's Best Learned
Use microdialysis or fast-scan cyclic voltammetry to measure real-time dopamine changes during cocaine vs methamphetamine administration. Compare dopamine transporter availability in addicted vs control subjects using PET imaging.

## Common Misconceptions
Both cocaine and methamphetamine increase dopamine, but via distinct mechanisms—cocaine blocks uptake while methamphetamine actively reverses it, explaining different addiction trajectories and neurotoxicity.

## Questions

```yaml
- question: "A researcher blocks all action potentials in dopaminergic neurons (preventing vesicular release) and then administers cocaine to one subject and methamphetamine to another. What would happen to synaptic dopamine levels?"
  type: multiple-choice
  options:
    - "Neither drug increases synaptic dopamine, since both require vesicular release triggered by action potentials"
    - "Cocaine increases synaptic dopamine but methamphetamine does not, since cocaine acts on already-released dopamine while methamphetamine requires normal neuronal firing"
    - "Methamphetamine increases synaptic dopamine but cocaine does not, since methamphetamine reverses DAT to release cytoplasmic dopamine independently of vesicular release"
    - "Both drugs equally increase synaptic dopamine, since both work by blocking the dopamine transporter"
  answer: 2
  explanation: "Cocaine is a competitive reuptake inhibitor — it prevents clearance of dopamine already in the synapse but does not itself cause release. Without vesicular release (action potentials blocked), cocaine has no dopamine to protect and cannot increase synaptic levels. Methamphetamine is fundamentally different: it enters the presynaptic terminal and reverses DAT, actively pumping cytoplasmic dopamine into the synapse independently of vesicular release or action potentials. This mechanistic difference — blocking vs. reversing the transporter — explains methamphetamine's greater acute potency, longer duration, and higher neurotoxicity."

- question: "Why does chronic methamphetamine use cause greater long-term damage to dopaminergic terminals than chronic cocaine use at equivalent doses?"
  type: multiple-choice
  options:
    - "Methamphetamine is more potent, causing more acute receptor stimulation in the short term"
    - "Cocaine is metabolized faster, so total cumulative dopamine exposure is lower with cocaine"
    - "Methamphetamine's reverse DAT transport floods the terminal with cytoplasmic dopamine, and methamphetamine also crosses into mitochondria to inhibit oxidative phosphorylation, generating reactive oxygen species that directly damage terminals"
    - "Methamphetamine blocks both DAT and SERT simultaneously, causing greater combined monoamine disruption"
  answer: 2
  explanation: "The combination of massive dopamine flooding (via reverse DAT transport and disruption of VMAT2 vesicular storage) and direct mitochondrial toxicity (methamphetamine is sufficiently lipid-soluble to enter mitochondria and disrupt oxidative phosphorylation) generates reactive oxygen species. This oxidative stress, combined with the cytoplasmic dopamine flood, causes direct damage to dopaminergic axon terminals — especially in the striatum and prefrontal cortex. Cocaine, which only prevents reuptake without reversing the transporter or entering mitochondria, does not produce equivalent terminal damage."

- question: "Both cocaine and methamphetamine increase synaptic dopamine by the same mechanism: blocking the dopamine transporter (DAT)."
  type: true-false
  answer: false
  explanation: "This is the key distinction. Cocaine is a competitive reuptake inhibitor — it occupies DAT's binding site and prevents the transporter from clearing already-released dopamine. Methamphetamine does something more aggressive: it enters the presynaptic neuron and causes reverse transport — DAT runs backwards, actively pumping dopamine from the cytoplasm into the synapse, independent of vesicular release. Methamphetamine also disrupts VMAT2 (vesicular monoamine transporter) and inhibits MAO. These mechanistic differences produce larger and longer-lasting dopamine surges, greater neurotoxicity, and a distinct addiction trajectory."

- question: "Chronic stimulant use leads to downregulation of D2 dopamine receptors in the nucleus accumbens, contributing to anhedonia and compulsive drug-seeking."
  type: true-false
  answer: true
  explanation: "Persistent overstimulation of postsynaptic D2 receptors by chronically elevated dopamine triggers homeostatic downregulation — cells reduce receptor density to compensate. PET imaging confirms dramatically reduced D2 receptor availability in people with stimulant use disorder, persisting months into abstinence. The resulting hypodopaminergic baseline produces anhedonia: normal rewards (food, social contact, achievement) no longer generate sufficient dopamine signaling to feel pleasurable. The reward system's gain has been permanently turned down, creating the neurobiological substrate for compulsive use."

- question: "Explain the shift from positive to negative reinforcement in stimulant addiction. What neurobiological change underlies this transition, and why does it make the addiction so difficult to stop?"
  type: short-answer
  answer: "Initially, stimulants produce intense pleasure via massive dopamine elevation in the nucleus accumbens — positive reinforcement (approaching reward). But chronic overstimulation triggers D2 receptor downregulation, establishing a hypodopaminergic baseline. The user now experiences anhedonia during abstinence because the reward system has adapted to drug-elevated dopamine as its new normal. Avoiding this misery — not seeking euphoria — becomes the primary motive: negative reinforcement (escaping aversion). Quitting requires tolerating prolonged anhedonia while D2 receptor density slowly recovers over months. The difficulty is not simply craving pleasure; it is escaping a chronically dysphoric state that only the drug temporarily relieves."
  explanation: "The transition from positive to negative reinforcement marks a qualitative shift in the nature of dependence. Positive reinforcement means the drug competes against other rewards for approach behavior. Negative reinforcement means the drug's absence creates a distinct aversive state (beyond baseline) that the drug alone relieves. This is why addiction is described as compulsive rather than merely habitual: the cost of not using becomes high, not just the benefit of using. D2 downregulation is the neurobiological mechanism that transforms the reward signal."
```

## Explainer

From your study of monoamine synthesis and catabolism, you know that after dopamine is released into the synapse, the **dopamine transporter (DAT)** acts like a vacuum — it pumps dopamine back into the presynaptic neuron for repackaging or degradation. This reuptake is the primary off-switch for dopaminergic signaling. Both cocaine and methamphetamine disable that off-switch, but they do it in fundamentally different ways, with important consequences for their neurotoxicity and addiction potential.

**Cocaine** is a **competitive reuptake inhibitor** — it binds directly to the DAT and physically blocks the transporter's binding pocket. Dopamine already in the synapse cannot be cleared, so it accumulates and keeps stimulating postsynaptic receptors. Crucially, cocaine does not itself trigger release; it only prevents clearance. The effect is rapid and short-lived, because cocaine is quickly metabolized (plasma half-life of about 60 minutes). This creates a steep spike-and-crash dopamine profile, and the intense craving following offset drives repeated dosing. Cocaine also blocks norepinephrine and serotonin transporters, contributing to cardiovascular effects and mood disruption.

**Methamphetamine** works via a more aggressive mechanism. As an amphetamine-type compound, it enters the presynaptic terminal (partly through DAT itself) and causes **reverse transport** — it literally forces DAT to run backwards, flooding the synapse with dopamine from the cytoplasm regardless of vesicular release. This bypasses the normal action potential requirement for release. The result is a much larger and more prolonged dopamine surge. Methamphetamine is also lipid-soluble enough to cross into mitochondria and inhibit oxidative phosphorylation, generating reactive oxygen species. This oxidative stress, combined with the massive dopamine flood, causes direct damage to dopaminergic terminals — especially in the striatum and prefrontal cortex — explaining methamphetamine's greater long-term neurotoxicity compared to cocaine.

From your knowledge of D1 and D2 receptor subtypes and their downstream G-protein signaling, the consequences of chronic overstimulation become predictable. Postsynaptic neurons exposed to persistently elevated dopamine downregulate receptor density, particularly D2 receptors in the nucleus accumbens. PET imaging studies confirm dramatically reduced D2 availability in people with stimulant use disorder, even after months of abstinence. This hypodopaminergic state produces **anhedonia** — the inability to experience normal pleasure — because the reward system's gain has been chronically turned down to compensate for artificial overstimulation. The user now needs the drug to feel normal, not just to feel good. The transition from wanting the drug for pleasure to needing it to avoid the misery of its absence is the shift from positive to **negative reinforcement** that defines compulsive use.
