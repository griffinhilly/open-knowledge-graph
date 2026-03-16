---
id: hodgkin-huxley-model
title: The Hodgkin-Huxley Model
domain: biology
course: neuroscience
prerequisites:
- id: cable-theory-axonal-conduction
  type: hard
- id: voltage-gated-sodium-channels
  type: hard
- id: voltage-gated-potassium-channels
  type: hard
- id: differential-equations-intro
  type: soft
- id: systems-of-first-order-linear-odes
  type: soft
builds-toward:
- action-potential-initiation
- action-potential-repolarization
tags:
- hh-model
- conductance
- gating-variables
stage: advanced
status: draft
---

# The Hodgkin-Huxley Model

## Core Idea
The Hodgkin-Huxley model captures action potential generation using differential equations for voltage-dependent sodium and potassium conductances. Gating variables (m, h, n) describe channel opening probability: dV/dt = (gL(EL−V) + gNam³h(ENa−V) + gKn⁴(EK−V) + Iapp)/Cm. This minimal model explains threshold, regenerative firing, and refractory periods.

## How It's Best Learned
Implement HH equations numerically. Vary parameters and observe emergent behaviors like threshold-spike response.

## Common Misconceptions
HH fully explains neuronal firing. HH is a conductance-based approximation valid near rest. Different neurons require modified parameters.

## Explainer

You know how voltage-gated sodium and potassium channels work individually — sodium channels open rapidly to depolarize the membrane, then inactivate, while potassium channels open more slowly to repolarize it. You also know from cable theory that current spreads passively along an axon with distance-dependent decay. The **Hodgkin-Huxley model** is the mathematical framework that puts all of these pieces together into a single system of equations that explains how an action potential actually works, quantitatively, from first principles.

The central equation treats the membrane as an electrical circuit. The membrane capacitance (Cm) stores charge, and three parallel conductance pathways allow current to flow: a **sodium conductance** (gNa), a **potassium conductance** (gK), and a **leak conductance** (gL) representing all other passive ion flow. Each conductance is multiplied by its driving force — the difference between the membrane voltage and that ion's reversal potential. The membrane voltage equation is: Cm·dV/dt = gL(EL−V) + gNa·m³h(ENa−V) + gK·n⁴(EK−V) + Iapp. The leak term is constant, but the sodium and potassium conductances are voltage-dependent and time-dependent — this is where the **gating variables** come in.

Three gating variables — **m**, **h**, and **n** — each range from 0 to 1 and represent the probability that a particular gate is in its open configuration. The sodium conductance depends on m³h: three **activation gates** (m) that open rapidly with depolarization, and one **inactivation gate** (h) that closes slowly. The potassium conductance depends on n⁴: four activation gates that open with a delay. Each gating variable follows its own first-order differential equation: dX/dt = α(V)(1−X) − β(V)X, where α and β are voltage-dependent rate constants that Hodgkin and Huxley determined empirically from voltage-clamp experiments on the squid giant axon. The interplay of these time constants — fast m, slow h, delayed n — produces the characteristic action potential waveform.

Here is why this matters beyond the equations themselves. The HH model demonstrates that the action potential is an **emergent property** of interacting conductances, not a single mechanism. The threshold exists because sodium activation (m) is regenerative: a small depolarization opens some sodium channels, which depolarizes the membrane further, opening more channels. The refractory period emerges because h (sodium inactivation) recovers slowly while n (potassium activation) remains elevated. You do not need to memorize the rate constants — the insight is architectural. By writing differential equations for each conductance and coupling them through voltage, Hodgkin and Huxley showed that complex neural behavior arises from the dynamics of a small number of interacting components. This framework has been extended to model virtually every type of neuron by adding or modifying conductances — calcium channels, hyperpolarization-activated channels, persistent sodium currents — while keeping the same mathematical structure.
