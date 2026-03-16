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
stage: advanced
status: draft
---

# Action Potential Initiation: Threshold, All-or-None, and Depolarization

## Core Idea
When membrane potential depolarizes past threshold (typically around −50 mV), voltage-gated Na+ channels open faster than K+ channels, creating a positive feedback loop where inward Na+ current further depolarizes the membrane. This regenerative depolarization is the essence of excitability: subthreshold stimuli produce no action potential, while suprathreshold stimuli trigger a full stereotyped spike regardless of stimulus magnitude.

## Explainer

You already know that neurons maintain a **resting membrane potential** around −70 mV, with Na⁺ concentrated outside and K⁺ inside. You also know that voltage-gated sodium channels can open in response to depolarization, allowing Na⁺ to rush inward. The action potential is what happens when these ingredients combine into a self-amplifying explosion of electrical activity.

Imagine a neuron sitting at rest at −70 mV. A small excitatory input depolarizes the membrane to −60 mV. A few voltage-gated Na⁺ channels sense this change and open, allowing Na⁺ to flow in, which depolarizes the membrane further — say to −55 mV. Now more Na⁺ channels open, more Na⁺ enters, and the membrane depolarizes even more. This is the critical concept: **positive feedback**. Each increment of depolarization recruits more channels, which produce more depolarization, which recruits still more channels. Below a critical voltage called **threshold** (typically around −50 to −55 mV), the small number of opening Na⁺ channels is counterbalanced by resting K⁺ leak channels that pull the voltage back down. But once depolarization crosses threshold, inward Na⁺ current overwhelms all outward currents and the membrane voltage rockets upward toward the Na⁺ equilibrium potential (around +50 mV). This is the rising phase of the action potential.

The **all-or-none principle** follows directly from this positive feedback loop. There is no such thing as a half-sized action potential. Either the stimulus is too weak to reach threshold — in which case the membrane simply relaxes back to rest — or it crosses threshold and the full regenerative cycle fires. A stimulus twice as strong as threshold does not produce a spike twice as large; it produces the same stereotyped spike. This is analogous to lighting a match: you either generate enough friction to ignite it or you don't, but once lit, the flame doesn't burn hotter because you struck harder. Neurons encode information not by varying spike amplitude but by varying **firing rate** — the number of spikes per second.

The site where action potentials typically initiate is the **axon initial segment** (also called the axon hillock region), where voltage-gated Na⁺ channels are packed at especially high density. Synaptic inputs arriving at dendrites and the soma produce graded potentials that spread passively — decreasing with distance, as predicted by the Goldman equation you studied. These graded potentials summate at the axon initial segment, and if their combined effect crosses threshold there, the action potential fires and propagates down the axon. This spatial arrangement means the axon initial segment acts as the neuron's decision point: a final integrator that converts the analog sum of thousands of synaptic inputs into a discrete, all-or-none digital output.
