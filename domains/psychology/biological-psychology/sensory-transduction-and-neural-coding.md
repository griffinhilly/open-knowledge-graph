---
id: sensory-transduction-and-neural-coding
title: Sensory Transduction and Neural Coding
domain: psychology
course: biological-psychology
prerequisites:
- id: thalamus-structure-and-sensory-relay
  type: hard
builds-toward:
- visual-system-anatomy-and-physiology
- auditory-system-anatomy-and-physiology
- somatosensory-and-pain-perception
- olfaction-gustation-and-chemical-sensing
tags:
- transduction
- coding
- receptors
- perception
stage: advanced
status: draft
---

# Sensory Transduction and Neural Coding

## Core Idea
Sensory transduction converts physical energy (light, sound, pressure, chemicals, temperature) into neural signals through activation of specialized receptor proteins that open ion channels or activate second messengers. Information is encoded in spike rate (rate coding: stronger stimulus → faster firing), temporal patterns (temporal coding: spike timing carries information), and distributed population codes (different neurons have different stimulus preferences). Adaptation reduces responsiveness to constant stimuli, enhancing sensitivity to changes.

## How It's Best Learned
Study mechanoreceptor subtypes and their tuning properties. Examine rate-level functions showing spike frequency vs. stimulus intensity. Record from sensory neurons to compare temporal and rate coding. Study adaptation kinetics.

## Common Misconceptions
One receptor encodes one sensation / stronger stimulus always causes faster spikes / adaptation is always undesirable / sensory coding uses only one strategy.

## Explainer

You already know from studying the thalamus that sensory information is relayed and gated before reaching cortex—the thalamus acts as a switchboard that forwards, filters, and modulates sensory signals. But before any of that relay happens, there's a more fundamental transformation: converting the physical world into the brain's language of action potentials. **Sensory transduction** is that conversion step. Each sensory system has specialized receptor cells equipped with molecular machinery—ion channels, G-protein-coupled receptors, or mechanically sensitive proteins—tuned to respond to a particular form of energy. The receptor cell is the interface between the physical world and the neural world.

Consider touch. When you press your fingertip against a surface, mechanosensitive ion channels in skin nerve endings deform physically and open, allowing ions to flow in. This creates a **receptor potential**—a graded electrical change proportional to the stimulus intensity. If the receptor potential is large enough, it triggers action potentials in the sensory neuron. The same logic applies in every modality: photoreceptors contain light-sensitive proteins that trigger cascade-driven hyperpolarization when photons arrive; hair cells in the cochlea have stereocilia that deflect with sound waves, mechanically opening ion channels. In each case, a physical event is translated into a graded electrical signal, which is then converted into all-or-nothing action potentials that can travel long distances along sensory nerves.

How information is represented *within* that electrical signal is the domain of **neural coding**. The most intuitive code is **rate coding**: stronger stimuli cause faster firing. A dim light causes a few spikes per second from a retinal ganglion cell; a bright light causes many. Rate coding works for encoding stimulus intensity but loses information about fine timing. **Temporal coding** uses the precise timing of spikes—not just how many, but exactly when they occur—to carry additional information. In the auditory system, neurons phase-lock their spikes to the frequency of a tone at low frequencies, encoding the sound wave's periodicity directly in spike timing rather than firing rate. Many real neural signals exploit both strategies simultaneously, and at the population level, **distributed coding** across neurons with different tuning preferences allows richer representation than any single neuron could provide.

**Adaptation** is the phenomenon where sensory responses decrease over time even as the stimulus continues. You've experienced this: a smell that is strong when you first walk into a room becomes unnoticeable after a few minutes. Adaptation isn't a failure—it's a feature. By reducing responses to unchanging stimuli, the system frees up processing resources for detecting *changes*, which are typically more behaviorally relevant. **Rapidly adapting receptors** respond strongly at stimulus onset and sometimes offset but fall silent in between; **slowly adapting receptors** maintain their response throughout sustained contact. This distinction explains why you feel the weight of a backpack most acutely when you first put it on and less so after standing still—the rapidly adapting Meissner's corpuscles signal the onset event, while the slowly adapting Merkel discs maintain a lower-level tonic signal. The combined output of multiple receptor subtypes gives the nervous system both transient event detection and sustained intensity information from the same physical stimulus.
