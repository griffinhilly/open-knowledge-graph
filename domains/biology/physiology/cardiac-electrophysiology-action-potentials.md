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
- cardiac-pacemaker-activity-sinoatrial-node
tags:
- cardiology
- electrophysiology
- ion-channels
stage: formal-systems
status: validated
---

# Cardiac Electrophysiology and Action Potentials

## Core Idea
The heart's electrical excitability depends on ion channel activity across the cardiac membrane, with different phases of the action potential—depolarization, plateau, and repolarization—corresponding to distinct physiological functions. Understanding cardiac action potentials is essential for interpreting electrocardiograms and predicting how drugs or ischemia affect heart rhythm.

## How It's Best Learned
Study voltage-gated sodium, calcium, and potassium channel activity during each phase using a standard cardiac action potential diagram. Compare to skeletal muscle action potentials to highlight the cardiac plateau phase and its role in sustained contraction.

## Common Misconceptions
- Assuming the cardiac action potential has only three phases like neuronal APs; the cardiac plateau is distinct and prolonged.
- Thinking calcium enters throughout depolarization; calcium influx is primarily during the plateau phase.

## Questions

```yaml
- question: "A pharmacologist administers a drug that selectively blocks L-type voltage-gated calcium channels in cardiac muscle. Which effect on the ventricular action potential and cardiac function would you predict?"
  type: multiple-choice
  options:
    - "Phase 0 (rapid depolarization) is abolished because L-type Ca²⁺ channels drive the initial depolarization"
    - "The plateau phase is shortened or eliminated, weakening contraction and reducing the refractory period"
    - "The action potential duration is unchanged; only heart rate is affected because Ca²⁺ controls the SA node"
    - "Repolarization is slowed because Ca²⁺ efflux normally helps restore the negative resting potential"
  answer: 1
  explanation: "L-type Ca²⁺ channels are the key inward current sustaining the Phase 2 plateau. Blocking them removes the inward Ca²⁺ current that balances outward K⁺ current, collapsing the plateau. Two consequences follow: (1) Contraction weakens because Ca²⁺ entry triggers calcium-induced calcium release from the SR, which drives actin-myosin cross-bridging — less Ca²⁺ entry means weaker contraction. (2) The refractory period shortens because it depends on the long plateau, and a shorter AP allows premature re-excitation and risk of arrhythmia. Option A is the key misconception: Phase 0 is driven by fast Na⁺ channels, not Ca²⁺."

- question: "Why does the cardiac action potential last roughly 200–300 milliseconds while a neuronal action potential lasts only 1–2 milliseconds?"
  type: multiple-choice
  options:
    - "Cardiac Na⁺ channels inactivate much more slowly than neuronal Na⁺ channels, prolonging Phase 0"
    - "L-type voltage-gated Ca²⁺ channels open during Phase 2 and sustain an inward current that balances outward K⁺ current, holding the membrane near 0 mV for hundreds of milliseconds"
    - "The cardiac muscle cell has a much larger surface area, requiring more time to fully depolarize"
    - "Delayed rectifier K⁺ channels are absent in cardiac muscle, so repolarization must rely on slow Ca²⁺ channel inactivation alone"
  answer: 1
  explanation: "The plateau is the defining feature of the cardiac action potential. After Phase 0 (fast Na⁺-driven depolarization, identical in principle to neurons), L-type Ca²⁺ channels open. Their inward Ca²⁺ current is balanced by outward K⁺ current through delayed rectifier channels, holding the membrane potential near 0 mV — this is Phase 2, lasting 200–300 ms. No comparable plateau exists in neurons because neurons lack this sustained Ca²⁺ influx after depolarization. The plateau is not a side effect; it is functionally essential for both contraction and rhythm."

- question: "The long plateau of the cardiac action potential creates an extended refractory period that prevents the heart from entering sustained tetanic contraction."
  type: true-false
  answer: true
  explanation: "The refractory period — during which cardiac muscle cannot be re-excited — lasts nearly as long as the plateau, because fast Na⁺ channels remain inactivated until repolarization nears completion. This means the heart cannot receive another stimulus and contract again until the current contraction cycle is almost complete. In skeletal muscle, the brief action potential and short refractory period allow repeated stimuli to summate into tetanus. The cardiac design deliberately prevents this: tetanus would lock the heart in systole, blocking ventricular filling and eliminating cardiac output."

- question: "Calcium influx into the cardiac cell is greatest during Phase 0 (rapid depolarization), which is why Phase 0 triggers the contractile machinery."
  type: true-false
  answer: false
  explanation: "Phase 0 is driven by fast voltage-gated Na⁺ channels, not Ca²⁺ channels. Calcium influx occurs primarily during Phase 2 (the plateau), when L-type Ca²⁺ channels open. This Ca²⁺ then binds ryanodine receptors on the sarcoplasmic reticulum, triggering a much larger Ca²⁺ release (calcium-induced calcium release) that activates the contractile apparatus. The plateau phase, not Phase 0, is the trigger for contraction."

- question: "The Phase 2 plateau of the cardiac action potential serves two distinct physiological functions. What are they, and how does each protect the heart?"
  type: short-answer
  answer: "First, the plateau creates an extended refractory period: fast Na⁺ channels remain inactivated throughout the plateau, making the cardiac muscle unexcitable until repolarization is nearly complete. This prevents tetanic contraction and ensures the ventricle can refill between beats. Second, the plateau delivers the Ca²⁺ signal for contraction: L-type Ca²⁺ channel opening during Phase 2 triggers calcium-induced calcium release from the SR, providing the cytoplasmic Ca²⁺ that drives actin-myosin cross-bridge cycling."
  explanation: "These two functions are inseparably linked by the plateau's duration. Shortening the plateau (e.g., by L-type Ca²⁺ channel blockers, hypokalemia, or ischemia) simultaneously weakens contraction (less Ca²⁺ trigger) and increases arrhythmia risk (shorter refractory period allows premature re-excitation and re-entrant circuits). This dual role explains why antiarrhythmic drugs that modulate cardiac Ca²⁺ channels must be used carefully — the same channel that prevents arrhythmia when open is the same one that drives contraction."
```

## Explainer

You already understand how a neuronal action potential works: voltage-gated Na⁺ channels open rapidly, depolarizing the membrane, then K⁺ channels open to repolarize it, producing a spike lasting one to two milliseconds. The **cardiac action potential** uses the same ion channel logic but adds a critical twist — a prolonged **plateau phase** lasting roughly 200–300 milliseconds — that transforms a brief electrical spike into a sustained signal capable of driving coordinated heart contraction.

The ventricular cardiac action potential unfolds in five numbered phases. **Phase 0** is rapid depolarization, driven by the same fast voltage-gated Na⁺ channels you know from neurons — the membrane rockets from about −90 mV to around +20 mV in a few milliseconds. **Phase 1** is a brief, partial repolarization caused by transient outward K⁺ channels that open and quickly inactivate, creating a small notch in the voltage trace. Then comes the defining feature: **Phase 2**, the plateau. Here, **L-type voltage-gated calcium channels** open, allowing Ca²⁺ to flow inward. This inward Ca²⁺ current exactly balances the outward K⁺ current through delayed rectifier channels, holding the membrane near 0 mV for hundreds of milliseconds. It is this balance — not a single dominant current — that sustains the plateau. As L-type Ca²⁺ channels slowly inactivate and more K⁺ channels open, the balance tips toward repolarization, producing **Phase 3**, a return to the resting potential. **Phase 4** is the stable resting membrane potential maintained by inward rectifier K⁺ channels.

The plateau phase exists for a specific mechanical reason: the heart must contract as a coordinated unit, and contraction takes time. In skeletal muscle, action potentials are brief and individual twitches can summate into tetanus (sustained contraction). The heart cannot afford tetanus — it must relax between beats to refill with blood. The long plateau creates an equally long **refractory period** during which the cardiac muscle cannot be re-excited, preventing tetanic contraction. This is why the heart beats rhythmically rather than locking up.

The calcium entering during Phase 2 is not just an electrical curiosity — it is the trigger for contraction itself. This incoming Ca²⁺ binds to ryanodine receptors on the sarcoplasmic reticulum, triggering a much larger release of stored Ca²⁺ in a process called **calcium-induced calcium release**. The total cytoplasmic Ca²⁺ then drives the same actin-myosin cross-bridge cycling you learned in skeletal muscle contraction. So the plateau phase serves double duty: it prevents re-excitation (electrical protection) and it provides the calcium signal for contraction (mechanical function). Anything that shortens the plateau — certain drugs, electrolyte imbalances, ischemia — both weakens contraction and increases the risk of dangerous re-entrant arrhythmias by allowing premature re-excitation.
