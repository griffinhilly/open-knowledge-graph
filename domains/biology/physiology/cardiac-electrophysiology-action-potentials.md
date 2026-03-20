---
id: cardiac-electrophysiology-action-potentials
title: Cardiac Electrophysiology and Action Potentials
domain: biology
course: physiology
prerequisites:
- id: action-potential-depolarization-repolarization
  type: hard
- id: ion-channels-selectivity
  type: hard
- id: cardiac-cycle-and-heart-function
  type: soft
builds-toward:
- electrocardiogram-and-heart-rhythm
- pacemaker-automaticity-sinoatrial-node
tags:
- cardiology
- electrophysiology
- ion-channels
stage: advanced
status: draft
---

# Cardiac Electrophysiology and Action Potentials

## Core Idea
The heart's electrical excitability depends on ion channel activity across the cardiac membrane, with different phases of the action potential—depolarization, plateau, and repolarization—corresponding to distinct physiological functions. Understanding cardiac action potentials is essential for interpreting electrocardiograms and predicting how drugs or ischemia affect heart rhythm.

## How It's Best Learned
Study voltage-gated sodium, calcium, and potassium channel activity during each phase using a standard cardiac action potential diagram. Compare to skeletal muscle action potentials to highlight the cardiac plateau phase and its role in sustained contraction.

## Common Misconceptions
- Assuming the cardiac action potential has only three phases like neuronal APs; the cardiac plateau is distinct and prolonged.
- Thinking calcium enters throughout depolarization; calcium influx is primarily during the plateau phase.

## Explainer

You already understand how a neuronal action potential works: voltage-gated Na⁺ channels open rapidly, depolarizing the membrane, then K⁺ channels open to repolarize it, producing a spike lasting one to two milliseconds. The **cardiac action potential** uses the same ion channel logic but adds a critical twist — a prolonged **plateau phase** lasting roughly 200–300 milliseconds — that transforms a brief electrical spike into a sustained signal capable of driving coordinated heart contraction.

The ventricular cardiac action potential unfolds in five numbered phases. **Phase 0** is rapid depolarization, driven by the same fast voltage-gated Na⁺ channels you know from neurons — the membrane rockets from about −90 mV to around +20 mV in a few milliseconds. **Phase 1** is a brief, partial repolarization caused by transient outward K⁺ channels that open and quickly inactivate, creating a small notch in the voltage trace. Then comes the defining feature: **Phase 2**, the plateau. Here, **L-type voltage-gated calcium channels** open, allowing Ca²⁺ to flow inward. This inward Ca²⁺ current exactly balances the outward K⁺ current through delayed rectifier channels, holding the membrane near 0 mV for hundreds of milliseconds. It is this balance — not a single dominant current — that sustains the plateau. As L-type Ca²⁺ channels slowly inactivate and more K⁺ channels open, the balance tips toward repolarization, producing **Phase 3**, a return to the resting potential. **Phase 4** is the stable resting membrane potential maintained by inward rectifier K⁺ channels.

The plateau phase exists for a specific mechanical reason: the heart must contract as a coordinated unit, and contraction takes time. In skeletal muscle, action potentials are brief and individual twitches can summate into tetanus (sustained contraction). The heart cannot afford tetanus — it must relax between beats to refill with blood. The long plateau creates an equally long **refractory period** during which the cardiac muscle cannot be re-excited, preventing tetanic contraction. This is why the heart beats rhythmically rather than locking up.

The calcium entering during Phase 2 is not just an electrical curiosity — it is the trigger for contraction itself. This incoming Ca²⁺ binds to ryanodine receptors on the sarcoplasmic reticulum, triggering a much larger release of stored Ca²⁺ in a process called **calcium-induced calcium release**. The total cytoplasmic Ca²⁺ then drives the same actin-myosin cross-bridge cycling you learned in skeletal muscle contraction. So the plateau phase serves double duty: it prevents re-excitation (electrical protection) and it provides the calcium signal for contraction (mechanical function). Anything that shortens the plateau — certain drugs, electrolyte imbalances, ischemia — both weakens contraction and increases the risk of dangerous re-entrant arrhythmias by allowing premature re-excitation.
