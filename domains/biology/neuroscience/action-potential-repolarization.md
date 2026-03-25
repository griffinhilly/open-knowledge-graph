---
id: action-potential-repolarization
title: Action Potential Repolarization and Undershoot
domain: biology
course: neuroscience
prerequisites:
- id: action-potential-initiation
  type: hard
- id: voltage-gated-potassium-channels
  type: hard
builds-toward:
- voltage-clamp-recording
- absolute-refractory-period
tags:
- action-potential
- repolarization
- temporal-dynamics
stage: advanced
status: validated
---

# Action Potential Repolarization and Undershoot

## Core Idea
After reaching peak depolarization, the action potential repolarizes as voltage-gated Na+ channels inactivate while K+ channels (which activated more slowly) reach peak conductance, driving outward K+ current. The delayed peak of K+ conductance often causes undershoot—hyperpolarization beyond resting potential—before the membrane returns to baseline.

## Questions

```yaml
- question: "At the peak of an action potential (+30 mV), the membrane begins to repolarize back toward resting potential. What is the primary mechanism driving this repolarization?"
  type: multiple-choice
  options:
    - "Voltage-gated Na+ channels begin closing in response to the positive membrane potential"
    - "The Na+/K+ ATPase pump immediately activates and restores the ion gradients"
    - "Voltage-gated Na+ channels have inactivated while voltage-gated K+ channels have now reached peak conductance, producing outward K+ current"
    - "Ca2+ channels open and compete with Na+ channels, diluting the inward current"
  answer: 2
  explanation: "Repolarization is driven by a timing mismatch between two channel populations. Voltage-gated Na+ channels activate fast but also inactivate fast — within ~1 ms, an inactivation gate blocks the pore even as the activation gate remains open. This stops Na+ influx. Meanwhile, voltage-gated K+ channels, which activate much more slowly, are now reaching peak open probability. The resulting outward K+ current drives the membrane back toward the K+ equilibrium potential (~−80 mV). The Na+/K+ ATPase (option B) is far too slow to drive repolarization — it restores ion gradients over much longer timescales."

- question: "Why does the action potential 'undershoot' — transiently hyperpolarizing below resting membrane potential after repolarization?"
  type: multiple-choice
  options:
    - "The Na+/K+ ATPase pumps extra K+ in during recovery, lowering the membrane potential"
    - "Voltage-gated Na+ channels reopen briefly after inactivation, generating an inward current that overshoots"
    - "K+ channels reach peak conductance after the membrane has passed through resting potential, so K+ continues flowing outward before channels close"
    - "Cl- channels open during repolarization and pull the membrane below resting potential"
  answer: 2
  explanation: "The undershoot occurs because K+ channel closing is delayed. These channels reach peak open probability as the membrane is falling from +30 mV, and they are still maximally open as the membrane passes through resting potential (~−65 mV). Because the K+ equilibrium potential (~−80 mV) is below resting, K+ continues flowing outward, pulling the membrane below resting potential. Only as K+ channels gradually close does the membrane drift back to its resting value — purely a consequence of slow K+ channel kinetics, not an active pumping process."

- question: "Voltage-gated K+ channels reach their maximum open probability later in the action potential than voltage-gated Na+ channels — after Na+ channels have already inactivated."
  type: true-false
  answer: true
  explanation: "This timing difference is the entire mechanistic basis of repolarization. Both channel types respond to the same membrane depolarization, but Na+ channels activate within a fraction of a millisecond while K+ channels activate much more slowly. By the time K+ conductance peaks, Na+ channels have already inactivated. The resulting brief window of dominant K+ conductance — unopposed by inward Na+ current — drives the membrane back toward the K+ equilibrium potential and produces the undershoot."

- question: "Inactivation of voltage-gated Na+ channels during an action potential is the same process as channel closing — both return the channel to a resting state ready to reopen on the next stimulus."
  type: true-false
  answer: false
  explanation: "Inactivation and closing (deactivation) are distinct conformational states. A closed channel can reopen when the membrane depolarizes again. An inactivated channel cannot reopen until the membrane repolarizes — a cytoplasmic 'ball' has physically blocked the pore, and this state requires hyperpolarization to reverse. This distinction is crucial: during the absolute refractory period, Na+ channels are inactivated, not just closed, which is why no stimulus (however strong) can trigger another action potential until inactivation is reversed."

- question: "Explain why the afterhyperpolarization (undershoot) makes it harder to fire another action potential immediately after the first. What is the functional significance of this for the neuron?"
  type: short-answer
  answer: "During the undershoot, the membrane potential is below resting potential — farther from the threshold for firing. A stronger-than-normal depolarizing stimulus is therefore required to reach threshold, defining the relative refractory period. This limits maximum firing rate. Combined with the absolute refractory period (when Na+ channels are inactivated), the undershoot also ensures that action potentials propagate in only one direction — the region behind a propagating spike is refractory and cannot be re-excited."
  explanation: "The refractory period is not a bug but a feature. It encodes temporal separation between signals (minimum inter-spike interval), enforces unidirectional propagation along axons, and allows partial restoration of ion gradients before the next spike. Without it, a single stimulus could set off a reverberating wave that bounced back and forth indefinitely. The undershoot's contribution to the relative refractory period is one of the elegant self-limiting mechanisms of neural signaling."
```

## Explainer

You already understand how an action potential begins: depolarization opens voltage-gated Na+ channels, Na+ rushes in, and the membrane potential shoots toward +30 to +40 mV. But what brings the membrane back down? The answer lies in the different timing of two channel populations you have studied — and understanding this timing mismatch is the key to the entire repolarization phase.

**Voltage-gated Na+ channels** open fast but also **inactivate** fast. Within about a millisecond of opening, a ball-and-chain inactivation gate swings into the channel pore, blocking further Na+ influx even though the channel's activation gate is still open. This is not the same as closing — inactivation is a distinct conformational state that cannot be reversed until the membrane repolarizes. So at the peak of the action potential, Na+ entry has already been shut off by inactivation. Meanwhile, **voltage-gated K+ channels** have been responding to the same depolarization, but they activate much more slowly. They are just reaching their peak open probability as the Na+ channels are inactivating. This temporal offset — fast Na+ activation followed by slow K+ activation — is the fundamental mechanism of repolarization.

With Na+ channels inactivated and K+ channels now wide open, the dominant current shifts to outward K+ flow. Potassium ions leave the cell, driven by both the electrical gradient (the interior is still positive) and the concentration gradient (K+ is more concentrated inside). This outward current rapidly pulls the membrane potential back toward the K+ equilibrium potential (around −80 mV). Because K+ conductance peaks *after* the membrane has already started falling from +30 mV, the K+ channels are maximally open at a time when the membrane potential is passing through resting potential. The result is **undershoot** (also called **afterhyperpolarization**): the membrane transiently dips below resting potential, sometimes reaching −80 to −90 mV, before K+ channels finally close and the membrane drifts back to its resting value near −65 to −70 mV.

The undershoot is not a malfunction — it has functional significance. During the undershoot, the membrane is farther from threshold than at rest, making it harder to fire another action potential. This contributes to the **relative refractory period**, during which a stronger-than-normal stimulus is needed to trigger firing. Combined with the absolute refractory period (when Na+ channels are still inactivated and firing is impossible), the undershoot helps enforce unidirectional propagation of action potentials along the axon and sets an upper limit on firing frequency. Think of it as the neuron's built-in cooldown: fast Na+ channels create the spike, slow K+ channels clean it up, and the timing gap between them shapes everything from signal direction to maximum firing rate.
