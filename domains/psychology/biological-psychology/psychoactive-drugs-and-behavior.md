---
id: psychoactive-drugs-and-behavior
title: 'Psychoactive Drugs: Mechanisms of Action and Behavioral Effects'
domain: psychology
course: biological-psychology
prerequisites:
- id: pharmacology-agonists-antagonists
  type: hard
- id: gaba-glutamate-neurotransmission-balance
  type: soft
- id: dopamine-pathways-reward-motivation
  type: soft
builds-toward:
- substance-use-disorder
tags:
- drugs
- pharmacology
- behavior
stage: formal-systems
status: validated
---

# Psychoactive Drugs: Mechanisms of Action and Behavioral Effects

## Core Idea
Psychoactive drugs alter behavior by modulating neurotransmission. Depressants (alcohol, benzodiazepines) enhance GABA inhibition; stimulants (cocaine, amphetamines) increase dopamine; hallucinogens modulate serotonin and glutamate; opioids activate mu receptors. The behavioral effect depends on drug class, dosage, administration route, individual neurochemistry, and context. Chronic use causes tolerance (reduced response), withdrawal (compensatory changes), and sensitization (enhanced response to cues).

## Questions

```yaml
- question: "A patient who has taken benzodiazepines daily for six months abruptly stops. Based on their mechanism of action, which withdrawal symptoms should the clinician anticipate?"
  type: multiple-choice
  options:
    - "Sedation and slowed breathing — the drug's effects persist in tissues after stopping"
    - "Hyperexcitability, anxiety, and potentially seizures — the brain's compensatory changes are unmasked"
    - "Intense cravings but no physical symptoms — benzodiazepines only cause psychological dependence"
    - "Depression and fatigue — losing enhanced GABA activity causes the brain to become underactive"
  answer: 1
  explanation: "Benzodiazepines enhance GABA inhibition. With chronic use, the brain compensates by downregulating GABA receptors and reducing inhibitory tone — so the patient's nervous system is in a new, drug-dependent equilibrium. When the drug is removed, the compensatory changes are unmasked: the brain is now abnormally hyperexcitable. This can manifest as anxiety, tremors, and in severe cases, life-threatening seizures. Option A describes the drug's direct effects, not withdrawal. Option C confuses psychological with physical dependence. Option D inverts the logic: losing enhanced inhibition causes hyper-, not hypo-excitability."

- question: "Both cocaine and amphetamines dramatically increase synaptic dopamine. What is the key mechanistic difference between them?"
  type: multiple-choice
  options:
    - "Cocaine increases dopamine synthesis; amphetamines prevent dopamine breakdown"
    - "Cocaine blocks the dopamine transporter (DAT), preventing reuptake; amphetamines reverse the transporter, actively pumping dopamine out of the presynaptic cell"
    - "Cocaine acts on D2 receptors; amphetamines act on D1 receptors, producing different behavioral effects"
    - "There is no meaningful mechanistic difference — both simply block the dopamine transporter equally"
  answer: 1
  explanation: "Cocaine is a reuptake blocker: it binds to the dopamine transporter and prevents it from clearing dopamine from the synapse, letting existing dopamine accumulate. Amphetamines are more aggressive: they are substrates for the transporter and, once inside the presynaptic terminal, reverse the transporter's direction so it pumps dopamine *out* rather than in. This produces a larger and faster dopamine surge. Option A describes biosynthesis/degradation mechanisms, which are not the primary targets. Option C incorrectly assigns receptor selectivity. Option D is factually wrong — the mechanism matters for addiction pharmacology and for designing treatments."

- question: "Sensitization to a drug means that with repeated use, the subjective 'high' becomes more intense over time."
  type: true-false
  answer: false
  explanation: "This conflates two different types of neural adaptation. The subjective high typically *tolerates* — the brain compensates for repeated drug exposure (e.g., by downregulating receptors), so more drug is needed to achieve the same pleasure. Sensitization refers specifically to an *enhanced* reactivity to drug-associated cues (sights, smells, locations) — not to the drug's direct rewarding effects. After repeated use, encountering a cue associated with the drug can trigger powerful cravings even years after abstinence, even when the person no longer experiences strong pleasure from the drug itself. This dissociation between wanting (sensitized) and liking (tolerating) is central to addiction theory."

- question: "Opioids increase dopamine in the reward circuit by directly binding to and activating dopamine neurons."
  type: true-false
  answer: false
  explanation: "Opioids use an indirect mechanism: they activate mu-opioid receptors on GABAergic *interneurons* in the reward circuit (particularly in the ventral tegmental area). These interneurons normally inhibit dopamine neurons. When opioids suppress the interneurons, the inhibition is lifted — dopamine neurons are *disinhibited* — and they fire more, releasing dopamine. This is called 'disinhibition.' The distinction matters clinically and scientifically: the reward effect is two synapses removed from the opioid receptor, and disrupting GABA circuits has consequences for many other brain functions beyond just dopamine release."

- question: "Why is withdrawal from depressants like alcohol and benzodiazepines medically dangerous in a way that stimulant withdrawal typically is not?"
  type: short-answer
  answer: "Depressants enhance GABA inhibition, so the brain adapts by reducing inhibitory tone — it becomes chronically underinhibited relative to the drug-free state. When the drug is removed, the compensatory hyperexcitability is fully expressed: the brain is now too excitable, which can escalate to uncontrolled neuronal firing (seizures) and autonomic instability that can be fatal. Stimulant withdrawal, by contrast, unmasks underactivity in reward circuits — causing fatigue, depression, and craving — but does not produce runaway excitation. The asymmetry is about what the compensatory changes are: hyperexcitability (depressant withdrawal) is more acutely life-threatening than hypoactivity (stimulant withdrawal)."
  explanation: "This is why alcohol and benzodiazepine withdrawal in dependent patients is medically managed (often with tapering doses of benzodiazepines to gradually reduce the hyperexcitability), while stimulant withdrawal, though deeply uncomfortable, rarely requires emergency hospitalization. The underlying principle is that any drug that chronically tips the balance toward inhibition will cause compensatory excitatory changes that are dangerous when revealed by abrupt cessation."
```

## Explainer

From your study of pharmacology, you know that drugs act as agonists (mimicking or enhancing a signal) or antagonists (blocking it). Psychoactive drugs apply this principle to specific neurotransmitter systems, and the behavioral outcome maps predictably onto which system is targeted. The brain's **excitatory/inhibitory balance** — maintained by glutamate and GABA — is the foundation. **Depressants** like alcohol and benzodiazepines tip this balance toward inhibition by enhancing GABA activity, producing sedation, anxiolysis, and at high doses, anesthesia. This is why a few drinks feel relaxing: you are globally reducing neural excitability. The flip side is that their withdrawal is dangerous — removing the enhanced inhibition leaves a hyperexcitable brain.

**Stimulants** work primarily through the dopamine system, which you know mediates reward and motivation. Cocaine blocks the **dopamine transporter (DAT)**, preventing reuptake and flooding the synapse. Amphetamines are more aggressive: they reverse the transporter, actively pumping dopamine *out* of the presynaptic cell. Both produce intense reward, increased energy, and focused arousal, but through slightly different mechanisms. The reward is disproportionate to what any natural stimulus produces, which is why stimulant use can make natural rewards feel flat by comparison — a process that underlies tolerance and the motivational deficits of addiction.

**Hallucinogens** like LSD and psilocybin primarily act as partial agonists at serotonin **5-HT₂A** receptors in the cortex. This receptor normally helps modulate how the cortex integrates sensory information with predictions and prior beliefs. When overactivated, the thalamic "gate" that filters sensory input loosens, and cortical circuits that are normally quiet become active — producing perceptual distortions, altered sense of self, and novel associative thinking. **Opioids** occupy a different mechanism entirely: they activate **mu-opioid receptors** on GABAergic interneurons in the reward circuit, effectively disinhibiting dopamine neurons and releasing a flood of dopamine. They also directly suppress pain by acting on receptors in the spinal cord and periaqueductal gray.

**Tolerance**, **withdrawal**, and **sensitization** are the three ways the brain adapts to repeated drug exposure, and they point in different directions. Tolerance occurs when the brain compensates for a drug's presence (e.g., downregulating receptors), requiring more drug for the same effect. Withdrawal is the rebound when the drug is removed and the compensatory changes are unmasked. Sensitization is more interesting: while the subjective high often tolerates, the brain can become *more* reactive to drug-associated cues — the sight of a needle, a familiar smell, a location. This cue-induced sensitization explains why cravings can be triggered even after years of abstinence, and why context matters so much in treatment settings. The same pharmacological mechanism that produces a drug's acute effect is often the seed of both its therapeutic value and its potential for misuse.
