---
id: action-potential-depolarization-repolarization
title: Action Potential Phases
domain: biology
course: neuroscience
prerequisites:
- id: voltage-gated-sodium-channels
  type: hard
- id: voltage-gated-potassium-channels
  type: hard
- id: resting-membrane-potential
  type: hard
- id: equilibrium-expression-kc-kp-constants
  type: soft
- id: electrochemistry-basics
  type: soft
builds-toward:
- unmyelinated-axon-conduction
tags:
- action-potential
- electrophysiology
stage: expert
status: draft
---

# Action Potential Phases

## Core Idea
Depolarization (Na+ influx toward +30 mV), repolarization (K+ efflux, Na+ inactivation), afterhyperpolarization (delayed K+ closure). All-or-none: threshold crossed triggers full action potential.

## Questions

```yaml
- question: "During repolarization of an action potential, what two events work together to return the membrane potential toward resting?"
  type: multiple-choice
  options: ["Voltage-gated Na+ channels reopen and K+ channels close", "Voltage-gated Na+ channels inactivate and voltage-gated K+ channels open", "The Na+/K+ ATPase pump rapidly restores both ion gradients", "Ca2+ channels open while Na+ channels reset to the closed state"]
  answer: 1
  explanation: "Repolarization is a two-part process: voltage-gated Na+ channels transition from their open state to an inactivated (blocked) state, stopping Na+ influx; simultaneously, voltage-gated K+ channels (which activate more slowly) open and K+ flows out down its electrochemical gradient. This K+ efflux drives the membrane back toward the K+ equilibrium potential (~-80 mV), causing afterhyperpolarization before slow K+ channel closure returns the membrane to resting potential."

- question: "During the absolute refractory period immediately following an action potential, a second stimulus of twice the threshold strength can trigger another action potential in the same axon segment."
  type: true-false
  answer: false
  explanation: "The absolute refractory period exists because Na+ channels are in their inactivated state — a conformation distinct from the closed resting state — and cannot be reopened by any stimulus regardless of strength. Only after the inactivation gate resets (during the relative refractory period) can a suprathreshold stimulus generate a new action potential. This property ensures unidirectional propagation and sets a ceiling on firing frequency."

- question: "Explain why the action potential is described as 'all-or-none' and what determines the threshold that triggers it."
  type: short-answer
  answer: "Once membrane depolarization reaches threshold (~-55 mV), a positive feedback loop is triggered: Na+ channels open, Na+ influx further depolarizes the membrane, opening more Na+ channels. This regenerative process runs to completion regardless of the initial stimulus strength — the resulting action potential is always the same amplitude. Threshold is set by the density and kinetics of voltage-gated Na+ channels; a stimulus must depolarize enough membrane to open enough Na+ channels to initiate this self-sustaining cascade."
  explanation: "The all-or-none property is a direct consequence of the positive feedback between membrane depolarization and Na+ channel opening. Below threshold, K+ leak and Na+ channel closure can restore resting potential; at threshold, the inward Na+ current overwhelms the restoring forces and the spike propagates to full amplitude. This property is what makes neural signals reliable over long distances — the signal regenerates at each node rather than decrementing like a passive cable signal."
```

## Explainer

You already know that neurons maintain a resting membrane potential around -70 mV, created by the unequal distribution of ions across the membrane and the selective permeability of leak channels. An action potential is what happens when that careful balance is temporarily overwhelmed — a brief, dramatic reversal of membrane polarity that propagates along the axon.

The initiating event is depolarization past threshold (~-55 mV). At that point, voltage-gated sodium channels snap open. Na+ ions, driven both by their concentration gradient (high outside) and by the negative membrane potential, flood inward. This influx rapidly drives the membrane potential from -70 mV up toward +30 mV — the peak of the action potential. The key word here is "all-or-none": if depolarization does not reach threshold, channels quickly close and the membrane recovers. If threshold is crossed, a self-reinforcing cascade (more depolarization → more channels open → more Na+ in) runs to completion every time, producing an identical spike regardless of how much the threshold was exceeded.

Repolarization begins almost immediately, driven by two concurrent changes. Voltage-gated Na+ channels transition into an inactivated state — different from their resting closed state — in which they cannot reopen. Simultaneously, voltage-gated K+ channels, which activate more slowly than Na+ channels, open and K+ flows outward down its electrochemical gradient. The combination of stopped Na+ influx and active K+ efflux drives the membrane potential back negative. Because K+ channels close with a slight delay, the membrane transiently overshoots resting potential, dipping to around -80 mV. This afterhyperpolarization is not a separate mechanism; it is simply the membrane following the K+ equilibrium potential until those slow K+ channels finally close.

The absolute refractory period — the window immediately after the spike during which no new action potential can be triggered — occurs because Na+ channels are inactivated and cannot respond to any stimulus. This has two important consequences: it ensures the action potential propagates in only one direction (the region behind the wavefront cannot be re-excited), and it sets a hard upper limit on how fast a neuron can fire. The relative refractory period that follows, when a suprathreshold stimulus *can* trigger a new spike, reflects the gradual recovery of Na+ channels from inactivation and the still-elevated K+ conductance.

Finally, note that the Na+/K+ ATPase pump does not meaningfully contribute to the immediate events of a single action potential — it operates on a much slower timescale. The ion movements during a single action potential are so small relative to the total ion concentration on each side that the gradients are essentially unaffected. The pump's job is maintenance over many spikes, not moment-to-moment restoration. This is a common misconception worth flagging: the action potential is driven by ion channels, not by the pump.
