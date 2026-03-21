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

## Questions

```yaml
- question: "A drug selectively blocks the sodium inactivation gate (the 'h' gating variable) without affecting sodium activation (m) or potassium activation (n). What would happen to action potential firing?"
  type: multiple-choice
  options:
    - "Action potentials would be smaller in amplitude because sodium conductance would be reduced"
    - "The neuron would fail to fire because both m and h are required for any sodium current to flow"
    - "The membrane would become persistently depolarized and the neuron would lose the ability to fire repeated action potentials, because sodium channels could open but never inactivate"
    - "Action potentials would be prolonged but normal in all other respects, because h only controls the duration of the sodium current"
  answer: 2
  explanation: "The h gate is the sodium inactivation gate — it closes slowly during depolarization, terminating the sodium current and allowing repolarization. Without h inactivation, sodium channels that open during depolarization would remain open indefinitely, producing a sustained inward current that holds the membrane depolarized. The neuron would be locked in a depolarized state, unable to repolarize and thus unable to fire another action potential. This is also why scorpion toxins and certain local anesthetic side effects that block sodium inactivation cause sustained depolarization and repetitive firing or paralysis."

- question: "What produces the action potential threshold — the critical membrane voltage above which regenerative firing occurs in the Hodgkin-Huxley model?"
  type: multiple-choice
  options:
    - "A fixed voltage sensor in the sodium channel that triggers simultaneously in all channels when reached"
    - "The point at which sodium influx through activated channels exceeds the repolarizing outward potassium current, creating a self-amplifying positive feedback loop"
    - "A voltage-gated calcium channel that opens at threshold and triggers sodium channel opening"
    - "The equilibrium potential for sodium, which the membrane must approach before further depolarization can occur"
  answer: 1
  explanation: "Threshold is an emergent property of competing currents, not a fixed property of any single channel. As voltage increases, sodium channels begin to open (m increases), producing inward sodium current that further depolarizes the membrane, opening more channels. Below threshold, outward leak and potassium currents are sufficient to counteract this inward current and return the membrane to rest. Above threshold, the inward sodium current wins — the feedback becomes regenerative ('all-or-none'). Threshold is the tipping point of this competition, which is why it is not a sharp fixed value but can vary with recent activity, temperature, and channel availability."

- question: "In the Hodgkin-Huxley model, the refractory period emerges from the combination of slow sodium inactivation recovery (h gate) and sustained potassium activation (n gate), rather than from any single channel property."
  type: true-false
  answer: true
  explanation: "The absolute refractory period occurs when h (sodium inactivation) is near zero and n (potassium activation) is still elevated — sodium channels cannot reopen, and potassium channels are actively hyperpolarizing the membrane. The relative refractory period follows as h slowly recovers but n is still partially activated, requiring a stronger-than-normal stimulus to trigger threshold. No single channel produces this behavior; it is the combined dynamics of m, h, and n with their different time constants. This is a central example of how complex neural behavior is emergent from interacting conductances."

- question: "The Hodgkin-Huxley model can predict action potential firing in any neuron using the same fixed parameters that Hodgkin and Huxley measured from the squid giant axon."
  type: true-false
  answer: false
  explanation: "The HH model framework is general, but the specific parameters — the voltage-dependent rate constants (α and β) for m, h, and n, the maximum conductances, and the reversal potentials — were measured empirically from the squid giant axon and apply precisely only to that preparation. Different neuron types (cerebellar Purkinje cells, dopamine neurons, cardiac cells) have different channel complements, different kinetics, and sometimes entirely different channel types (calcium channels, HCN channels, persistent sodium currents). The HH architecture has been extended to model these neurons by adding conductances and modifying parameters, but the original squid parameters cannot be transplanted directly."

- question: "Why is the action potential threshold not simply a property of sodium channels alone? Explain what makes it an emergent property of the interaction between sodium and potassium conductances."
  type: short-answer
  answer: "Threshold depends on the balance between the inward sodium current (depolarizing) and the combined outward currents — potassium, leak, and any inactivation. At membrane voltages below threshold, a small depolarization opens a few sodium channels (m increases slightly), but the resulting inward sodium current is too small to overcome the outward currents pulling the membrane back to rest. The system is stable. Above threshold, sodium activation becomes self-reinforcing: enough channels open that the inward current outpaces the restorative outward currents, causing further depolarization that opens still more channels. Threshold is the unstable equilibrium point where these competing dynamics are exactly balanced — tip one way and the membrane returns to rest; tip the other and regenerative firing occurs."
  explanation: "This emergent quality is why HH is more than an empirical fit — it provides a mechanistic explanation for why neurons fire in an all-or-none fashion. No single channel has a 'threshold voltage' built in; threshold emerges from the dynamics of a system of coupled differential equations. This insight generalizes: many threshold phenomena in biology (gene expression switches, cell fate decisions) involve the same architecture of competing positive and negative feedback with a tipping point."
```

## Explainer

You know how voltage-gated sodium and potassium channels work individually — sodium channels open rapidly to depolarize the membrane, then inactivate, while potassium channels open more slowly to repolarize it. You also know from cable theory that current spreads passively along an axon with distance-dependent decay. The **Hodgkin-Huxley model** is the mathematical framework that puts all of these pieces together into a single system of equations that explains how an action potential actually works, quantitatively, from first principles.

The central equation treats the membrane as an electrical circuit. The membrane capacitance (Cm) stores charge, and three parallel conductance pathways allow current to flow: a **sodium conductance** (gNa), a **potassium conductance** (gK), and a **leak conductance** (gL) representing all other passive ion flow. Each conductance is multiplied by its driving force — the difference between the membrane voltage and that ion's reversal potential. The membrane voltage equation is: Cm·dV/dt = gL(EL−V) + gNa·m³h(ENa−V) + gK·n⁴(EK−V) + Iapp. The leak term is constant, but the sodium and potassium conductances are voltage-dependent and time-dependent — this is where the **gating variables** come in.

Three gating variables — **m**, **h**, and **n** — each range from 0 to 1 and represent the probability that a particular gate is in its open configuration. The sodium conductance depends on m³h: three **activation gates** (m) that open rapidly with depolarization, and one **inactivation gate** (h) that closes slowly. The potassium conductance depends on n⁴: four activation gates that open with a delay. Each gating variable follows its own first-order differential equation: dX/dt = α(V)(1−X) − β(V)X, where α and β are voltage-dependent rate constants that Hodgkin and Huxley determined empirically from voltage-clamp experiments on the squid giant axon. The interplay of these time constants — fast m, slow h, delayed n — produces the characteristic action potential waveform.

Here is why this matters beyond the equations themselves. The HH model demonstrates that the action potential is an **emergent property** of interacting conductances, not a single mechanism. The threshold exists because sodium activation (m) is regenerative: a small depolarization opens some sodium channels, which depolarizes the membrane further, opening more channels. The refractory period emerges because h (sodium inactivation) recovers slowly while n (potassium activation) remains elevated. You do not need to memorize the rate constants — the insight is architectural. By writing differential equations for each conductance and coupling them through voltage, Hodgkin and Huxley showed that complex neural behavior arises from the dynamics of a small number of interacting components. This framework has been extended to model virtually every type of neuron by adding or modifying conductances — calcium channels, hyperpolarization-activated channels, persistent sodium currents — while keeping the same mathematical structure.
