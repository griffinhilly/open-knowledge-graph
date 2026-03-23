---
id: action-potential-initiation
title: 'Action Potential Initiation: Threshold, All-or-None, and Depolarization'
domain: biology
course: neuroscience
prerequisites:
- id: resting-membrane-potential
  type: hard
- id: voltage-gated-sodium-channels
  type: hard
- id: goldman-equation
  type: soft
builds-toward:
- action-potential-repolarization
- voltage-clamp-recording
- saltatory-conduction
tags:
- action-potential
- excitability
- nonlinear-dynamics
stage: expert
status: validated
---

# Action Potential Initiation: Threshold, All-or-None, and Depolarization

## Core Idea
When membrane potential depolarizes past threshold (typically around −50 mV), voltage-gated Na+ channels open faster than K+ channels, creating a positive feedback loop where inward Na+ current further depolarizes the membrane. This regenerative depolarization is the essence of excitability: subthreshold stimuli produce no action potential, while suprathreshold stimuli trigger a full stereotyped spike regardless of stimulus magnitude.

## Questions

```yaml
- question: "A neuron at rest (−70 mV) receives two inputs: input A depolarizes it to −52 mV, and input B depolarizes it to −47 mV. If threshold is −50 mV, what happens?"
  type: multiple-choice
  options:
    - "Neither produces an action potential because neither reaches the +40 mV peak of an action potential"
    - "Both produce action potentials, but input B produces a larger one because it depolarizes the membrane more"
    - "Only input B produces an action potential; input A fails to cross threshold and the membrane returns to rest"
    - "Both produce action potentials of identical size, but input B fires with a shorter latency"
  answer: 2
  explanation: "Input A (−52 mV) stays below threshold (−50 mV), so the small Na⁺ channel opening it produces is overwhelmed by resting K⁺ leak, and the membrane returns to −70 mV. Input B (−47 mV) crosses threshold, triggering the positive feedback cycle where Na⁺ channel opening causes depolarization causes more Na⁺ channel opening — and the spike fires to completion. Option A confuses threshold with the peak voltage. Option B violates the all-or-none principle."

- question: "A researcher applies stimulus A at 1.5× threshold intensity and stimulus B at 4× threshold intensity to the same neuron. What is the expected result?"
  type: multiple-choice
  options:
    - "Stimulus B produces a larger action potential because more Na⁺ channels are recruited by the stronger depolarization"
    - "Both stimuli produce identical action potentials, since amplitude is set by the Na⁺ equilibrium potential and channel properties, not by stimulus strength"
    - "Stimulus A produces no action potential; only stimulus B exceeds threshold"
    - "Stimulus B produces a faster action potential because faster depolarization recruits channels more quickly"
  answer: 1
  explanation: "This is the all-or-none principle in action. Once threshold is crossed — by 1.5× or 4× doesn't matter — the same regenerative cycle fires: Na⁺ channels open, membrane rushes toward the Na⁺ equilibrium potential (~+50 mV), and the spike peaks at the same amplitude. Stimulus strength above threshold affects firing rate (how often spikes fire) or latency (how quickly the first spike fires), but not individual spike size. Neurons encode intensity by varying rate, not amplitude."

- question: "A stronger stimulus produces a larger action potential because it opens more voltage-gated Na⁺ channels, driving the membrane to a higher peak voltage."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about action potentials. The all-or-none principle states that once threshold is crossed, the action potential is stereotyped — same amplitude, same shape, same duration — regardless of how far above threshold the stimulus was. Amplitude is determined by the Na⁺ equilibrium potential and the kinetics of voltage-gated channels, not by stimulus intensity. A neuron 'tells' its target cells about stimulus intensity through firing rate (spikes per second), not spike size."

- question: "Neurons can encode the intensity of a stimulus despite the all-or-none nature of individual action potentials by varying the rate at which they fire."
  type: true-false
  answer: true
  explanation: "Since individual spike amplitude is fixed, the only way to signal 'more' is to fire more spikes per second. Stronger stimuli that produce more sustained depolarization cause the neuron to reach threshold repeatedly in quick succession, increasing firing rate. This is frequency coding: sensory neurons signal stronger stimuli with higher firing rates, and motor neurons drive stronger muscle contractions by firing faster. The all-or-none principle is not a limitation — it's the basis of a clean, noise-resistant digital encoding scheme."

- question: "Why does positive feedback make threshold a critical, non-negotiable switching point rather than a gradual continuum of neural excitability?"
  type: short-answer
  answer: "Positive feedback creates a bistable switch. Below threshold, any Na⁺ channel opening is more than counterbalanced by resting K⁺ leak currents, which pull the voltage back toward rest — a stable equilibrium. Above threshold, the inward Na⁺ current exceeds all outward currents, so each increment of depolarization causes more Na⁺ channel opening, which causes more depolarization — a self-amplifying runaway cascade. The threshold is the unstable tipping point between these two stable states (rest and the fully fired spike). There is no gradual middle ground: below threshold, the system returns to rest; above it, the positive feedback loop drives the membrane fully to its peak."
  explanation: "This bistability is what gives action potentials their reliability. The all-or-none property isn't just a curiosity — it ensures that signals propagating down a long axon don't decay, because each node along the way undergoes the same full regenerative firing. Compare this to a passive electrical cable, where voltage decays continuously with distance. The threshold-positive-feedback system solves the long-distance signaling problem by resetting the signal to full amplitude at each point."
```

## Explainer

You already know that neurons maintain a **resting membrane potential** around −70 mV, with Na⁺ concentrated outside and K⁺ inside. You also know that voltage-gated sodium channels can open in response to depolarization, allowing Na⁺ to rush inward. The action potential is what happens when these ingredients combine into a self-amplifying explosion of electrical activity.

Imagine a neuron sitting at rest at −70 mV. A small excitatory input depolarizes the membrane to −60 mV. A few voltage-gated Na⁺ channels sense this change and open, allowing Na⁺ to flow in, which depolarizes the membrane further — say to −55 mV. Now more Na⁺ channels open, more Na⁺ enters, and the membrane depolarizes even more. This is the critical concept: **positive feedback**. Each increment of depolarization recruits more channels, which produce more depolarization, which recruits still more channels. Below a critical voltage called **threshold** (typically around −50 to −55 mV), the small number of opening Na⁺ channels is counterbalanced by resting K⁺ leak channels that pull the voltage back down. But once depolarization crosses threshold, inward Na⁺ current overwhelms all outward currents and the membrane voltage rockets upward toward the Na⁺ equilibrium potential (around +50 mV). This is the rising phase of the action potential.

The **all-or-none principle** follows directly from this positive feedback loop. There is no such thing as a half-sized action potential. Either the stimulus is too weak to reach threshold — in which case the membrane simply relaxes back to rest — or it crosses threshold and the full regenerative cycle fires. A stimulus twice as strong as threshold does not produce a spike twice as large; it produces the same stereotyped spike. This is analogous to lighting a match: you either generate enough friction to ignite it or you don't, but once lit, the flame doesn't burn hotter because you struck harder. Neurons encode information not by varying spike amplitude but by varying **firing rate** — the number of spikes per second.

The site where action potentials typically initiate is the **axon initial segment** (also called the axon hillock region), where voltage-gated Na⁺ channels are packed at especially high density. Synaptic inputs arriving at dendrites and the soma produce graded potentials that spread passively — decreasing with distance, as predicted by the Goldman equation you studied. These graded potentials summate at the axon initial segment, and if their combined effect crosses threshold there, the action potential fires and propagates down the axon. This spatial arrangement means the axon initial segment acts as the neuron's decision point: a final integrator that converts the analog sum of thousands of synaptic inputs into a discrete, all-or-none digital output.
