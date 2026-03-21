---
id: sodium-potassium-atpase
title: 'The Na+/K+-ATPase: Maintaining Ion Gradients'
domain: biology
course: neuroscience
prerequisites:
- id: active-transport
  type: hard
- id: neuronal-compartments
  type: soft
- id: atp-hydrolysis-and-free-energy
  type: hard
builds-toward:
- resting-membrane-potential
- nernst-equation
tags:
- ion-transport
- energy-metabolism
- homeostasis
stage: advanced
status: draft
---

# The Na+/K+-ATPase: Maintaining Ion Gradients

## Core Idea
The Na+/K+-ATPase pumps three Na+ ions out and two K+ ions into the cell using ATP hydrolysis, maintaining the steep concentration gradients essential for neuronal excitability. Although the pump generates a small electrogenic (outward) current, its primary role is establishing chemical driving forces that ion channels subsequently exploit for electrical signaling.

## Questions

```yaml
- question: "You suddenly block the Na+/K+-ATPase in a resting neuron using ouabain. In the first few seconds, what happens to the neuron's ability to fire action potentials?"
  type: multiple-choice
  options:
    - "The neuron immediately loses its resting potential and cannot fire, because the pump directly generates the resting potential"
    - "The neuron can still fire normally for many minutes — a single action potential moves only a tiny fraction of the total ion gradient, so blocking the pump has no immediate effect"
    - "The neuron fires spontaneously and uncontrollably, because without the pump's hyperpolarizing current it cannot maintain inhibitory tone"
    - "The neuron's action potential amplitude immediately halves, because the pump contributes exactly half the resting membrane potential"
  answer: 1
  explanation: "The Na+/K+-ATPase maintains ion gradients, but each individual action potential uses only a tiny fraction of the total stored gradient — the concentration changes per action potential are negligible. The pump's electrogenic contribution is only −3 to −5 mV. In the short term, blocking the pump has almost no effect because the existing gradients are sufficient for continued firing. Over minutes to hours without pumping, the gradients slowly dissipate (Na+ accumulates inside, K+ leaks out), and eventually the resting potential depolarizes and action potentials fail. The pump is a long-term battery charger, not the immediate power source for each spike."

- question: "What is the PRIMARY function of the Na+/K+-ATPase in maintaining neuronal excitability?"
  type: multiple-choice
  options:
    - "To directly generate the resting membrane potential through its net outward current of one positive charge per cycle"
    - "To establish and maintain the steep Na+ and K+ concentration gradients that ion channels subsequently exploit for electrical signaling"
    - "To provide the energy for action potentials by hydrolyzing ATP directly at the membrane during firing"
    - "To regulate intracellular Ca2+ levels by exchanging Na+ for Ca2+ across the membrane"
  answer: 1
  explanation: "The pump's electrogenic contribution (3 Na+ out, 2 K+ in = net outward current) accounts for only about −3 to −5 mV of the resting potential — a small fraction. Its far more important role is maintaining the concentration gradients: high Na+ outside (~145 mM vs. ~15 mM inside) and high K+ inside (~140 mM vs. ~5 mM outside). These gradients are the stored electrochemical energy that voltage-gated ion channels exploit when they open. The pump did the uphill work in advance; channels let ions coast downhill to produce electrical signals. Without the gradients, channels opening would produce no current."

- question: "The Na+/K+-ATPase directly generates most of the resting membrane potential through its electrogenic outward current."
  type: true-false
  answer: false
  explanation: "The pump's net outward current (3 Na+ out, 2 K+ in) is electrogenic and makes the inside slightly more negative — but only by about −3 to −5 mV. The resting membrane potential (typically −65 to −70 mV in neurons) is primarily established by the selective permeability of the membrane to K+ through leak channels, exploiting the K+ concentration gradient the pump maintains. The pump's direct electrical contribution is small; its major role is thermodynamic — maintaining the gradients that give K+ efflux through leak channels its driving force. Blocking the pump does not immediately collapse the resting potential; it does so only gradually as the gradients dissipate."

- question: "The Na+/K+-ATPase must consume ATP even in a resting neuron that is not generating action potentials."
  type: true-false
  answer: true
  explanation: "Even at rest, ion gradients slowly dissipate: Na+ leaks inward and K+ leaks outward through resting conductances (leak channels, imperfect membrane impermeability). The pump must continuously run to counteract this passive leakage and maintain the gradients. This is why the brain consumes ~20% of the body's energy at rest and why neurons are so vulnerable to ischemia (loss of blood flow and thus ATP). Without continuous pump activity, the gradients would decay within minutes even without a single action potential being fired."

- question: "Why is the Na+/K+-ATPase described as a 'battery charger' rather than as the 'battery' itself in the context of neuronal electrical signaling?"
  type: short-answer
  answer: "The 'battery' metaphor refers to the stored electrochemical energy in the ion concentration gradients — the high Na+ outside and high K+ inside. When ion channels open, ions flow down these gradients and that flow constitutes the electrical signal. The Na+/K+-ATPase is the 'charger' because it does the thermodynamic work of restoring the gradients after they are partially discharged by ion flow during action potentials and resting leakage. The pump consumes ATP to push ions uphill against their gradients, reloading the stored energy. Ion channels are the 'devices' that discharge the battery; the pump continuously recharges it."
  explanation: "This analogy clarifies the pump's role in neuronal physiology. The pump does not generate action potentials directly — it is not active during the spike itself. Rather, it maintains the conditions (the gradients) that make electrical signaling possible. When the pump is blocked (e.g., by ouabain), neurons can continue firing for minutes on existing gradient reserves, just as a phone can run on battery power after the charger is unplugged. Failure comes only when the 'battery' runs down — when Na+ and K+ have equilibrated to the point that opening channels produces no driving force."
```

## Explainer

You already understand that active transport moves molecules against their concentration gradient using energy, and that ATP hydrolysis releases free energy that can power cellular work. The **Na⁺/K⁺-ATPase** (also called the sodium-potassium pump) is the single most important active transporter in neurons — and arguably in all animal cells. It consumes roughly 20–40% of the brain's total energy budget, and without it, neurons would lose their ability to fire within minutes.

The pump is a transmembrane protein that operates through a repeating conformational cycle. In its inward-facing state, it binds three Na⁺ ions from the cytoplasm. ATP then binds and is hydrolyzed, transferring a phosphate group to the pump itself — this **phosphorylation** triggers a conformational change that opens the pump to the extracellular side and releases the three Na⁺ ions outside the cell. In this outward-facing, phosphorylated state, the pump binds two K⁺ ions from the extracellular fluid. Dephosphorylation then triggers the reverse conformational change, returning the pump to its inward-facing state and releasing the two K⁺ ions into the cytoplasm. One complete cycle: 3 Na⁺ out, 2 K⁺ in, 1 ATP consumed. Each pump completes this cycle roughly 100–300 times per second.

The asymmetry of the pump — three positive charges out for every two in — means it generates a small net outward current, making the inside of the cell slightly more negative. This is the **electrogenic** contribution of the pump, but it accounts for only about −3 to −5 mV of the resting potential. The pump's far more important role is maintaining the **concentration gradients** themselves: high Na⁺ outside (~145 mM) and low inside (~15 mM); high K⁺ inside (~140 mM) and low outside (~5 mM). These gradients are the stored energy that ion channels exploit. When a voltage-gated Na⁺ channel opens during an action potential, Na⁺ rushes inward down the concentration gradient the pump established — the pump did the work of pushing Na⁺ uphill in advance, and the channel lets it flow back downhill to generate the electrical signal.

Think of the Na⁺/K⁺-ATPase as a battery charger. Ion channels are like the devices that drain the battery — each action potential lets a small amount of Na⁺ in and K⁺ out, slightly dissipating the gradients. The pump continuously recharges the system by restoring those gradients. A single action potential moves only a tiny fraction of the total ions (the concentration change is negligible), so a neuron can fire thousands of times before the gradients degrade noticeably even if the pump were suddenly stopped. But over the long term, the pump is essential — block it with the cardiac glycoside **ouabain**, and within minutes the ion gradients collapse, the resting potential depolarizes, and the neuron can no longer generate action potentials. The Na⁺/K⁺-ATPase thus provides the thermodynamic foundation upon which all electrical signaling in the nervous system is built.
