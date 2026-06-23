---
id: sensory-transduction-and-encoding
title: Sensory Transduction and Encoding
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: sensory-systems-anatomy
  type: hard
- id: ion-channels-selectivity
  type: hard
- id: sensory-receptor-transduction-adaptation
  type: soft
- id: neural-transmission-and-synaptic-integration
  type: soft
tags:
- transduction
- sensory-receptor
- adaptation
- coding
stage: formal-systems
status: validated
---
# Sensory Transduction and Encoding

## Core Idea
Sensory receptors convert physical stimuli (light, sound, pressure, temperature, chemicals) into electrical signals through opening or closing ion channels. The strength of sensory stimuli is encoded by the frequency of action potentials in sensory neurons, not by the amplitude of individual potentials. Sensory adaptation—reduction of responsiveness to constant stimuli—allows the nervous system to detect changes rather than absolute stimulus intensity.

## Questions

```yaml
- question: "A student argues that a very loud sound produces larger action potentials in the auditory nerve than a quiet sound — that's how the brain tells them apart. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Auditory nerve fibers do not conduct action potentials; they use graded potentials throughout"
    - "Action potentials are all-or-none events with fixed amplitude; loudness is encoded by firing frequency, not spike size"
    - "The brain cannot distinguish loudness at all — it only detects presence or absence of sound"
    - "Louder sounds actually produce fewer action potentials because adaptation rapidly silences the auditory nerve"
  answer: 1
  explanation: "Action potentials are all-or-none: once threshold is reached, the spike fires at a fixed amplitude regardless of how strong the stimulus is. There is no mechanism to make an individual spike bigger. Instead, a stronger receptor potential brings the neuron back to threshold more quickly after each spike, increasing firing rate. Loudness is coded in the frequency of spikes, not their size — this is the fundamental principle of frequency coding."

- question: "A constant weight is placed on a subject's palm. They feel it initially, stop noticing it after a few seconds, then notice again when it is removed. Which receptor type best explains this pattern?"
  type: multiple-choice
  options:
    - "Slowly adapting tonic receptors, which sustain their firing as long as a stimulus is present"
    - "Rapidly adapting phasic receptors, which fire at stimulus onset and offset but go silent during sustained stimulation"
    - "Nociceptors, which only activate when the stimulus crosses a tissue-damage threshold"
    - "Thermoreceptors, which respond to temperature changes in the skin caused by the weight"
  answer: 1
  explanation: "Rapidly adapting (phasic) receptors signal change, not maintained conditions. They fire briskly when the weight is applied (onset), fall silent during constant pressure, and fire again when the weight is removed (offset). Meissner's and Pacinian corpuscles work this way. Slowly adapting (tonic) receptors would maintain firing throughout and would not explain why the subject stops noticing the constant weight."

- question: "A stronger stimulus produces larger-amplitude action potentials in sensory neurons, which is how the nervous system encodes stimulus intensity."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about neural coding. Action potentials are all-or-none — once the membrane reaches threshold, the spike fires at a fixed, stereotyped amplitude. A stronger stimulus produces a larger receptor potential, but this translates into a higher action potential firing rate, not bigger spikes. Stimulus intensity is encoded in frequency (rate coding), not spike amplitude."

- question: "Sensory adaptation reduces the nervous system's responsiveness to constant stimuli, which allows it to remain sensitive to changes in the environment."
  type: true-false
  answer: true
  explanation: "Sensory adaptation is a design feature, not a flaw. By reducing firing in response to sustained, unchanging stimuli, the nervous system filters out background 'noise' and keeps higher brain centers available to respond to new, potentially significant events. The trade-off is reduced sensitivity to slowly-building threats, but the benefit is that the system remains tuned to what is novel and therefore more likely to require action."

- question: "Why must stimulus intensity be encoded in the frequency of action potentials rather than in their amplitude?"
  type: short-answer
  answer: "Because action potentials are all-or-none events. Once the membrane depolarizes to threshold, the spike fires at a fixed amplitude regardless of how much the threshold was exceeded. There is no way to make a single action potential larger. Instead, a larger receptor potential (caused by a stronger stimulus) depolarizes the neuron more strongly after each spike, reducing the interspike interval and increasing firing rate. Frequency is the only variable available to carry graded intensity information forward from the receptor potential to the central nervous system."
  explanation: "This is the core logic of frequency coding. The conversion from graded receptor potential to all-or-none action potentials could have been a lossy bottleneck — but evolution solved the problem by using firing rate as the channel for intensity information. Understanding this also explains why sensory pathways have upper limits (refractory periods set a maximum firing rate) and why adaptation matters (reducing background firing preserves the dynamic range for detecting changes)."
```

## Explainer

Every sensory experience — the warmth of sunlight, the pressure of a handshake, the taste of salt — begins with the same fundamental event: a physical or chemical stimulus changes the permeability of a membrane to specific ions. From your study of ion channels, you already know that ion channels are highly selective gated pores, and that their opening or closing shifts the membrane potential. **Sensory transduction** is exactly this process applied to specialized receptor cells. A photon of light strikes rhodopsin in a rod cell, triggering a G-protein cascade that closes Na⁺ channels. A sound wave flexes hair cells in the cochlea, mechanically pulling open K⁺ channels. Pressure on the skin deforms the membrane of a Meissner's corpuscle, directly stretching open mechanically gated channels. In each case, the same downstream result occurs: a graded **receptor potential** is produced, where greater stimulus intensity produces a larger depolarization.

Here is the critical transition: receptor potentials are **graded** (their amplitude varies with stimulus strength), but action potentials are **all-or-none** (fixed amplitude). So how does information about stimulus intensity survive this conversion? The answer is **frequency coding**. A stronger stimulus produces a larger receptor potential, which depolarizes the neuron more strongly, which triggers action potentials at a higher rate. A gentle touch might generate 5 action potentials per second in a sensory afferent; a firm press might generate 50. The code is in the *timing* between spikes, not in the size of each spike. This is why action potential frequency, not amplitude, is the relevant variable for stimulus intensity.

**Sensory adaptation** reveals a design principle: the nervous system is built to detect *change*, not maintain a constant readout of the environment. Receptors fall into two functional classes. **Rapidly adapting (phasic) receptors** respond briskly at stimulus onset and offset but quickly reduce firing during sustained stimulation — they signal that something *changed*. Meissner's corpuscles and Pacinian corpuscles work this way; they detect movement and vibration precisely because they go silent during static pressure. **Slowly adapting (tonic) receptors** maintain firing as long as the stimulus is present — they signal sustained conditions. Merkel's discs and Ruffini endings behave this way, providing ongoing information about sustained skin deformation. This is why you notice when a fly lands on your arm (phasic), but stop noticing the constant pressure of your chair (tonic adaptation).

The design logic becomes clear when you consider the alternative: if every sensory receptor maintained maximal firing regardless of whether conditions had changed, your nervous system would be overwhelmed by constant background noise. Adaptation filters out the static, freeing higher brain centers to attend to what is new and potentially relevant. The trade-off is that adaptation can cause the nervous system to fail to detect slow-building, gradually intensifying threats — a design constraint that has real consequences for pain perception, temperature tolerance, and toxic exposure.
