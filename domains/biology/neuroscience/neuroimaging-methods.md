---
id: neuroimaging-methods
title: 'Functional Brain Imaging: EEG and fMRI'
domain: biology
course: neuroscience
prerequisites:
- id: resting-membrane-potential
  type: soft
- id: central-vs-peripheral-nervous-system
  type: soft
tags:
- eeg
- fmri
- imaging
- measurement
stage: advanced
status: validated
---

# Functional Brain Imaging: EEG and fMRI

## Core Idea
EEG records electrical activity from scalp electrodes with millisecond temporal resolution but limited spatial specificity. fMRI measures blood oxygen-level-dependent (BOLD) changes reflecting regional neural activity with good spatial but poor temporal resolution. Both require careful interpretation: EEG measures summated synaptic currents; fMRI indirectly reflects metabolic demand.

## How It's Best Learned
Analyze real EEG and fMRI datasets from open databases. Practice source localization for EEG.

## Common Misconceptions
fMRI shows where thoughts are—it shows where blood flows. EEG shows everything—it's mainly sensitive to synchronous local currents.

## Questions

```yaml
- question: "A researcher wants to determine the precise timing of neural responses to an auditory tone — specifically, whether the brain response occurs within the first 50 milliseconds. Which method is most appropriate?"
  type: multiple-choice
  options:
    - "fMRI, because its millimeter spatial resolution can localize the auditory cortex precisely"
    - "EEG, because it captures electrical changes on the millisecond timescale"
    - "fMRI, because the BOLD signal is directly proportional to neural firing rate"
    - "EEG, because it records individual action potentials from single cortical neurons"
  answer: 1
  explanation: "fMRI's BOLD signal peaks approximately 5–6 seconds after neural activity — orders of magnitude too slow to capture 50 ms responses. EEG captures summed postsynaptic potentials with millisecond resolution, making it the correct tool for studying response timing. Option 3 is also wrong: EEG does not record individual action potentials (too brief, too deep) but rather summated synaptic currents from thousands of synchronously active neurons. Option 2 is wrong about fMRI's measurement basis — BOLD reflects metabolic demand, not directly firing rate."

- question: "A brain region shows elevated BOLD signal during a spatial navigation task. What does this most directly indicate?"
  type: multiple-choice
  options:
    - "That spatial memories are stored and retrieved specifically from that region"
    - "That neurons in that region are firing faster than in any other brain region"
    - "That there is increased local blood flow and oxygenation reflecting greater metabolic demand in that region"
    - "That the region is uniquely and exclusively responsible for spatial navigation"
  answer: 2
  explanation: "BOLD signal measures hemodynamic response — increased blood flow and blood oxygenation — which is an indirect proxy for metabolic demand. It does not directly measure neural firing (option 1), does not imply that region fires faster than all others (other regions may be active without being the experimental contrast), and does not support exclusivity claims about function (option 3). The inferential gap from 'elevated BOLD' to 'this region computes spatial navigation' requires careful experimental design, appropriate baseline contrasts, and statistical rigor — it cannot be read directly from the signal."

- question: "EEG has excellent temporal resolution because it directly records action potentials from individual neurons near the surface of the cortex."
  type: true-false
  answer: false
  explanation: "EEG's temporal resolution is indeed excellent (milliseconds), but the explanation in this statement is wrong. Individual action potentials are too brief (~1 ms) and too spatially distributed to produce detectable scalp voltages. EEG records the summed postsynaptic potentials (not action potentials) of thousands to millions of pyramidal neurons firing in synchrony. Their aligned dendritic currents sum to produce fields large enough to be detected at the scalp. EEG is also insensitive to neurons that fire asynchronously or in orientations perpendicular to the scalp."

- question: "fMRI and EEG measure complementary aspects of brain activity, making simultaneous EEG-fMRI recordings more informative than either method alone."
  type: true-false
  answer: true
  explanation: "fMRI provides spatial resolution (millimeters, telling you where metabolic demand increased) but poor temporal resolution (seconds, due to the slow hemodynamic response). EEG provides temporal resolution (milliseconds, capturing when electrical activity changes) but poor spatial resolution (the inverse problem makes source localization mathematically underdetermined). Combining them allows researchers to identify both when and where a neural process occurs. The tradeoff is technical: MRI's magnetic field distorts EEG signals, requiring specialized equipment and signal correction."

- question: "Why is the phrase 'fMRI shows where thoughts occur' misleading, and what does fMRI actually measure?"
  type: short-answer
  answer: "fMRI measures the BOLD signal — blood oxygenation changes reflecting increased metabolic demand in a region. It does not directly record neural activity or 'locate' cognition. The inferential leap from 'blood flow increased here' to 'this is where the thought is' requires careful experimental design: comparing active and baseline conditions to isolate the process of interest, statistical thresholding to separate signal from noise, and replication to confirm reliability. Additionally, most cognitive functions are distributed across multiple regions simultaneously, not located in a single spot. The phrase implies a precision and directness the measurement cannot support."
  explanation: "The hemodynamic response — the chain from neural activity to metabolic demand to blood flow to BOLD signal — introduces several layers of indirection. The BOLD signal reflects aggregate metabolic demand, not specific neural computations; it peaks seconds after the neural event; it varies with vascular health and baseline cerebral blood flow; and the region 'lighting up' is defined relative to a contrast condition, not as an absolute measure. Understanding these limitations is essential for critically reading neuroimaging literature."
```

## Explainer

From your understanding of resting membrane potential and the organization of the central nervous system, you know that neurons generate electrical signals and that the brain is organized into functionally distinct regions. Neuroimaging methods allow us to observe brain activity in living humans without surgery, but each method captures a different shadow of the underlying neural reality — and understanding what each method actually measures is essential to interpreting results correctly.

**Electroencephalography (EEG)** places electrodes on the scalp to record voltage fluctuations generated by the brain. What the electrodes detect is not individual action potentials — those are too brief and too deep to reach the scalp — but rather the summed **postsynaptic potentials** of thousands of neurons firing in synchrony. When large populations of cortical pyramidal neurons receive excitatory input simultaneously, their aligned dendritic currents sum to produce electrical fields strong enough to be measured at the surface. EEG's great strength is temporal resolution: it captures changes on the order of milliseconds, making it ideal for studying the timing of cognitive processes, sleep stages, and seizure activity. Its weakness is spatial resolution — because electrical signals spread and distort as they pass through cerebrospinal fluid, skull, and scalp, pinpointing the exact source of an EEG signal (the "inverse problem") is mathematically underdetermined.

**Functional magnetic resonance imaging (fMRI)** takes the opposite approach. It exploits the fact that active neurons consume more oxygen and glucose, triggering local increases in blood flow and blood oxygenation. Oxygenated and deoxygenated hemoglobin have different magnetic properties, so an MRI scanner can detect the **blood-oxygen-level-dependent (BOLD)** signal — a proxy for regional metabolic demand. fMRI achieves spatial resolution of a few millimeters, allowing researchers to localize activity to specific brain structures. However, the hemodynamic response peaks about 5–6 seconds after neural activity occurs, so temporal resolution is poor compared to EEG. The BOLD signal also reflects aggregate metabolic activity rather than specific neural computations — a region "lighting up" on fMRI means increased blood flow, not necessarily increased firing of a particular neuron type.

In practice, EEG and fMRI are often complementary. EEG tells you **when** something happened in the brain with millisecond precision; fMRI tells you **where** it happened with millimeter precision. Researchers sometimes combine both in simultaneous EEG-fMRI recordings to get the best of both worlds, though this introduces technical challenges (the MRI's magnetic field distorts EEG signals). The critical lesson for interpreting any neuroimaging study is to remember that these tools measure indirect correlates of neural activity — electrical field summation for EEG, metabolic demand for fMRI — and that the inferential leap from signal to cognitive function requires careful experimental design and statistical rigor.
