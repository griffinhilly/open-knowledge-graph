---
id: short-term-plasticity-presynaptic
title: 'Short-Term Synaptic Plasticity: Facilitation and Depression'
domain: biology
course: neuroscience
prerequisites:
- id: synaptic-transmission
  type: hard
- id: voltage-clamp-recording
  type: soft
builds-toward:
- critical-developmental-periods
tags:
- synaptic-plasticity
- presynaptic-mechanisms
- temporal-dynamics
stage: expert
status: draft
---

# Short-Term Synaptic Plasticity: Facilitation and Depression

## Core Idea
Short-term plasticity operates on timescales of 100 ms to seconds through presynaptic (residual Ca2+, release probability changes) and postsynaptic (receptor desensitization) mechanisms. Synaptic facilitation increases transmission during high-frequency activity, while depression decreases it, allowing neurons to encode temporal patterns of input.

## Questions

```yaml
- question: "A facilitating synapse receives two action potentials separated by 20 ms. Why does the second action potential typically trigger a larger postsynaptic response than the first?"
  type: multiple-choice
  options:
    - "The postsynaptic membrane inserts additional receptors during the 20 ms interval"
    - "The second action potential propagates faster because the axon is already partially depolarized"
    - "Residual calcium from the first action potential adds to the calcium influx triggered by the second, increasing vesicle release probability"
    - "The presynaptic terminal synthesizes and docks new vesicles in the 20 ms between stimuli"
  answer: 2
  explanation: "Facilitation operates through residual calcium. After the first action potential, calcium pumps and buffers clear Ca²⁺ from the terminal, but not instantaneously — a residual signal persists for tens of milliseconds. When the second spike arrives during this window, its Ca²⁺ influx adds to the residual, producing a higher peak concentration. Because vesicle fusion probability is a steep nonlinear function of calcium (roughly proportional to Ca²⁺ to the fourth power), even a modest residual boost causes a dramatically larger release. Options A and D describe processes that operate on much longer timescales."

- question: "A sensory circuit uses a depressing synapse to encode the onset of a stimulus rather than its sustained duration. This strategy works because:"
  type: multiple-choice
  options:
    - "Depression strengthens the synapse during continuous stimulation, amplifying sustained signals"
    - "The depressing synapse has an exceptionally large readily-releasable vesicle pool that sustains transmission indefinitely"
    - "Depression attenuates responses to sustained input, so only the onset — a change from silence — produces a strong response"
    - "Postsynaptic receptor desensitization enhances the response during continuous stimulation"
  answer: 2
  explanation: "A depressing synapse acts as a change detector or novelty filter. Rapid vesicle depletion means that each successive stimulus in a train draws from an increasingly depleted pool, producing progressively smaller postsynaptic currents. A constant stimulus therefore generates a declining neural response — adaptation. The circuit fires strongly to the onset (the transition from no stimulus to stimulus) but signals very little during sustained input. This is exploited in auditory circuits to encode onset timing with high precision rather than tracking steady-state sounds."

- question: "Short-term synaptic plasticity refers to changes in synaptic strength that persist for hours or days after high-frequency activity, similar to long-term potentiation (LTP)."
  type: true-false
  answer: false
  explanation: "False. Short-term plasticity operates on timescales of approximately 100 milliseconds to a few seconds — far shorter than LTP or LTD, which last hours to a lifetime. Short-term plasticity is also mechanistically distinct: it relies on presynaptic calcium dynamics and vesicle pool depletion, not on the protein synthesis and receptor trafficking that underlie long-term changes. The defining feature of short-term plasticity is that it is transient and reverses naturally as calcium is cleared and vesicle pools refill."

- question: "A facilitating synapse acts as a high-pass filter because it responds weakly to isolated, low-frequency inputs but strongly to high-frequency bursts of activity."
  type: true-false
  answer: true
  explanation: "True. At low firing frequencies, calcium is fully cleared between spikes, so each action potential encounters the same baseline release probability — low, because the initial release probability at facilitating synapses is typically low. At high frequencies, residual calcium accumulates faster than it is cleared, progressively boosting release probability with each spike in the burst. The synapse is therefore selective for high-frequency information — it 'passes' bursts while attenuating sparse, low-rate activity, exactly the behavior of a high-pass filter."

- question: "Explain how synaptic depression transforms a synapse into a 'novelty detector,' and why this is useful for sensory processing."
  type: short-answer
  answer: "A depressing synapse depletes its readily-releasable vesicle pool during sustained stimulation, so each successive release event draws from a smaller pool and produces a weaker postsynaptic response. A continuous sensory input therefore drives progressively diminishing neural responses — the circuit adapts. Only a change in the stimulus (onset, offset, or shift in intensity) replenishes relative vesicle availability and generates a strong response. This makes depressing synapses useful for detecting transitions and novelty rather than tracking steady background signals."
  explanation: "This temporal filtering function is exploited widely in sensory systems. In the auditory brainstem, depression at the calyx of Held synapse sharpens onset responses used for sound localization. In visual cortex, adaptation suppresses responses to static stimuli while preserving sensitivity to moving or changing inputs. The key insight is that synaptic strength is not fixed — it encodes the history of recent activity, making the synapse an active participant in signal processing rather than a passive relay."
```

## Explainer

You already understand that synaptic transmission involves calcium-triggered vesicle fusion and that voltage-clamp recording allows you to measure synaptic currents precisely. **Short-term plasticity** refers to changes in synaptic strength that last from tens of milliseconds to a few minutes — far shorter than the hours-to-lifetime changes of LTP and LTD. These rapid, reversible adjustments mean that synapses are not fixed-gain relays; instead, the strength of a synapse depends on its recent history of activity. This gives neural circuits a built-in ability to filter, amplify, or adapt to temporal patterns in their inputs.

**Synaptic facilitation** occurs when a second action potential arrives shortly after the first and produces a larger postsynaptic response. The mechanism is elegantly simple: calcium. When the first action potential triggers Ca²⁺ influx into the presynaptic terminal, the calcium is cleared by pumps and buffers, but not instantaneously — a residual calcium signal lingers for tens of milliseconds. When the second action potential arrives during this window, its calcium influx adds to the residual calcium, producing a higher peak Ca²⁺ concentration. Because vesicle fusion probability is a steep, nonlinear function of calcium concentration (roughly proportional to Ca²⁺ raised to the fourth power), even a modest increase in peak calcium can dramatically increase the number of vesicles released. The result is a progressively larger postsynaptic response with each successive stimulus in a train — the synapse "facilitates."

**Synaptic depression** is the opposite: repeated stimulation produces progressively smaller responses. The dominant presynaptic mechanism is **vesicle depletion** — each round of release draws from a limited pool of readily releasable vesicles, and if stimulation is fast enough, release outpaces replenishment. Synapses with a high initial release probability are especially prone to depression because they empty their vesicle pool quickly. Postsynaptic receptor desensitization also contributes: prolonged or repeated exposure to neurotransmitter causes ionotropic receptors to enter a non-conducting conformation, reducing the postsynaptic response even if transmitter release is constant. In practice, most synapses show a mixture of facilitation and depression, with the balance depending on the synapse type, initial release probability, and stimulation frequency.

The functional consequences of short-term plasticity are profound. A **facilitating synapse** acts as a high-pass filter — it responds weakly to isolated, low-frequency inputs but strongly to bursts of high-frequency activity. This means it selectively transmits information carried in bursts. A **depressing synapse** acts as a low-pass or adaptation filter — it responds strongly to the onset of activity but then attenuates, effectively signaling changes or novelty rather than sustained input. Many sensory systems exploit depressing synapses to implement adaptation: a constant stimulus produces a diminishing neural response, freeing the circuit to detect new changes against the background. In the auditory brainstem, short-term depression at the calyx of Held synapse helps neurons encode the onset timing of sounds with microsecond precision, discarding sustained input that carries less spatial information. Short-term plasticity thus transforms synapses from simple connectors into temporal filters that shape what information passes through a circuit.
