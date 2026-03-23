---
id: synaptic-transmission-neurotransmitter-release
title: Synaptic Transmission and Neurotransmitter Release
domain: psychology
course: biological-psychology
prerequisites:
- id: action-potential-and-neural-signaling
  type: hard
- id: neurotransmitter-synthesis-storage
  type: hard
- id: synaptic-vesicle-release-exocytosis
  type: hard
- id: exocytosis-snare-proteins-membrane-fusion
  type: hard
builds-toward:
- receptor-subtypes-and-signaling
- synaptic-plasticity-mechanisms
- gaba-glutamate-neurotransmission-balance
tags:
- synapses
- communication
- vesicle-dynamics
stage: formal-systems
status: draft
---

# Synaptic Transmission and Neurotransmitter Release

## Core Idea
Synaptic transmission couples electrical signals in the presynaptic neuron to chemical release of neurotransmitters, which then act on postsynaptic receptors. Calcium influx through voltage-gated channels triggers SNARE-mediated exocytosis of vesicles. The strength of transmission depends on presynaptic calcium, vesicle availability, and postsynaptic receptor density.

## Questions

```yaml
- question: "A researcher applies a drug that blocks voltage-gated calcium channels in presynaptic terminals. An action potential arrives at the terminal. What happens to neurotransmitter release?"
  type: multiple-choice
  options:
    - "Release is unaffected — the action potential directly opens vesicle fusion pores without requiring calcium"
    - "Release is abolished or severely reduced — calcium influx is the required trigger for synaptotagmin activation and SNARE-mediated vesicle fusion"
    - "Release increases — blocking calcium prevents inactivation of the release machinery"
    - "Release is delayed but not reduced — vesicles can fuse spontaneously given sufficient time"
  answer: 1
  explanation: "Calcium influx through voltage-gated Ca²⁺ channels is the critical trigger between electrical depolarization and chemical release. Without calcium, synaptotagmin cannot activate the SNARE complex, and vesicle fusion does not occur. The action potential depolarizes the terminal membrane, but depolarization alone is insufficient — calcium is the essential intermediate. The misconception (option A) confuses the electrical trigger for calcium channel opening with a direct trigger for vesicle fusion."

- question: "A neuron fires repeatedly at high frequency. After many action potentials, the postsynaptic response becomes progressively weaker, even though each action potential remains normal in amplitude and shape. What is the most likely presynaptic cause?"
  type: multiple-choice
  options:
    - "The postsynaptic receptors have been permanently desensitized by excess neurotransmitter"
    - "Voltage-gated calcium channels are being blocked by released neurotransmitter"
    - "The readily-releasable pool of docked vesicles has been depleted faster than it can be replenished"
    - "The action potential is no longer propagating to the axon terminal"
  answer: 2
  explanation: "Short-term synaptic depression results from presynaptic vesicle depletion. The readily-releasable pool near the active zone is finite; with rapid repeated firing, vesicles fuse and release transmitter faster than the replenishment machinery can dock and prime new ones. Each successive action potential releases less neurotransmitter. Option A is possible with some receptor types but is typically reversible and slower in onset; the question specifies a pattern that matches progressive presynaptic depletion."

- question: "Calcium entering the presynaptic terminal through voltage-gated channels is required to trigger neurotransmitter release during normal synaptic transmission."
  type: true-false
  answer: true
  explanation: "Calcium binds to synaptotagmin, the calcium sensor on synaptic vesicles, which then activates the SNARE complex to drive membrane fusion. This calcium requirement is universal across chemical synapses. The action potential opens voltage-gated Ca²⁺ channels by depolarizing the terminal; the resulting calcium influx is what bridges the electrical signal to chemical release."

- question: "The strength of synaptic transmission between two neurons is fixed once the synapse has formed and cannot be altered by neural activity."
  type: true-false
  answer: false
  explanation: "Synaptic strength is dynamically regulated at three points: (1) presynaptic calcium entry — modulatory receptors on the terminal can amplify or reduce Ca²⁺ influx per action potential; (2) vesicle availability — the size of the readily-releasable pool changes with recent activity; (3) postsynaptic receptor density — more receptors produce a larger response to the same amount of transmitter. This dynamic regulation is the molecular basis of short-term synaptic plasticity and ultimately forms the substrate for learning and memory."

- question: "Why is calcium influx — rather than membrane depolarization alone — the trigger for neurotransmitter release at chemical synapses?"
  type: short-answer
  answer: "Synaptic vesicles are held in a primed but unfused state near the active zone by SNARE proteins. Membrane depolarization alone does not activate fusion; a specific calcium signal is required to complete it. Calcium binds to synaptotagmin, a protein on the vesicle membrane, which then undergoes a conformational change that activates the SNARE complex and drives lipid bilayer fusion. This calcium requirement provides precise temporal control: release occurs only milliseconds after the action potential opens the Ca²⁺ channels, ensuring that chemical signaling is tightly coupled to electrical signaling."
  explanation: "The calcium step also allows modulation: anything that changes the amount of calcium entering the terminal (autoreceptors, neuromodulators, plasticity mechanisms) directly scales the amount of transmitter released per action potential — giving synapses enormous dynamic range."
```

## Explainer

The fundamental challenge the nervous system faces is this: neurons communicate electrically within themselves but chemically between each other. The synapse is where the handoff happens — and understanding that handoff requires connecting the electrical story you already know (action potentials, membrane potential) to a precise molecular machine. Think of synaptic transmission as a triggered release system: the electrical signal sets a timer, and when the impulse arrives, a burst of chemistry follows.

When an **action potential** travels down the axon and reaches the axon terminal, it depolarizes the membrane of the presynaptic bouton. Embedded in that terminal membrane are **voltage-gated calcium channels** — channels that stay closed at resting potential but open in response to depolarization. Calcium (Ca²⁺) floods in from the extracellular space, where its concentration is much higher. This calcium influx is the critical trigger. The faster and larger the calcium entry, the more neurotransmitter gets released. Calcium concentration directly controls the probability that a synaptic vesicle will fuse with the membrane.

This is where your knowledge of SNARE proteins and exocytosis connects. Synaptic vesicles — membrane-bound sacs loaded with neurotransmitter molecules during synthesis — are primed near the active zone, positioned at the presynaptic membrane but not yet fused. The **SNARE complex** (involving synaptobrevin on the vesicle, syntaxin and SNAP-25 on the target membrane) physically zippers together when calcium binds to synaptotagmin, pulling the vesicle into the plasma membrane. The vesicle opens, its contents spill into the **synaptic cleft**, and neurotransmitter molecules diffuse across the narrow gap to postsynaptic receptors. The whole sequence from action potential to transmitter release takes less than a millisecond.

**Transmission strength** is not fixed — it is dynamically regulated at each of three points. First, presynaptic calcium: anything that amplifies or reduces calcium entry (such as modulatory receptors on the terminal) will scale up or down how much neurotransmitter is released per action potential. Second, **vesicle availability**: the readily-releasable pool of docked vesicles near the active zone is finite. Rapid repeated firing can deplete this pool faster than vesicles are replenished, causing short-term synaptic depression. Third, **postsynaptic receptor density**: more receptors means more response for the same amount of transmitter. This three-way control — calcium, vesicle supply, receptor count — gives the synapse remarkable dynamic range and is the molecular substrate for forms of plasticity you will study next.
