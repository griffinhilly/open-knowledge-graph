---
id: spike-timing-dependent-plasticity
title: Spike-Timing-Dependent Plasticity
domain: biology
course: neuroscience
prerequisites:
- id: long-term-potentiation
  type: hard
- id: long-term-depression
  type: hard
- id: nmda-receptor-structure
  type: hard
builds-toward:
- hebbian-learning
- circuit-development
- learning-memory
tags:
- stdp
- spike-timing
- causality
stage: advanced
status: draft
---

# Spike-Timing-Dependent Plasticity

## Core Idea
Spike-timing-dependent plasticity is Hebbian learning where timing of presynaptic and postsynaptic spikes determines synaptic change: presynaptic firing before postsynaptic (causal, positive Δt) causes LTP; reverse timing causes LTD. The learning window spans tens of milliseconds and reflects NMDA receptor-mediated calcium signaling.

## How It's Best Learned
Use voltage clamp with precise spike pairings. Plot plasticity magnitude vs. spike timing.

## Common Misconceptions
STDP always follows one rule—rules vary across synapses. All synapses use STDP—it's one of several plasticity mechanisms.
