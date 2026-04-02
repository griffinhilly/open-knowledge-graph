---
id: dynamic-range-compression
title: Dynamic Range Compression
domain: music
course: music-technology
prerequisites:
- id: audio-signal-chain
  type: hard
- id: logarithms-intro
  type: soft
builds-toward: []
tags:
- dynamics-processing
- compression
- mixing
- audio-engineering
stage: advanced
status: validated
---

# Dynamic Range Compression

## Core Idea
Dynamic range compression automatically reduces the amplitude of loud signals while leaving quiet ones relatively unchanged, narrowing the difference between the loudest and quietest parts of an audio signal. This controlled reduction of dynamic range serves many purposes: keeping a vocal audible throughout a mix, preventing transient peaks from clipping, adding punch to drums, or gluing disparate elements together.

The compressor is defined by five key parameters. The threshold sets the level above which compression begins — signals below it pass unaffected. The ratio determines how much the compressor attenuates signals that exceed the threshold: a 4:1 ratio means for every 4 dB a signal rises above the threshold, only 1 dB emerges at the output. Extreme ratios (10:1 or higher) approach limiting — hard ceilings on output level. Attack time controls how quickly the compressor responds once the threshold is crossed; a slow attack lets transients pass through before the compressor engages, adding punch. Release time controls how quickly compression disengages after the signal drops below threshold.

Makeup gain compensates for the overall level reduction caused by compression. Because the compressor reduces loud peaks, the average loudness drops; makeup gain brings the compressed signal back to its original loudness while keeping the peaks lower — effectively increasing perceived density.

Different compressor circuit types have distinct sonic characters. VCA (Voltage Controlled Amplifier) compressors like the dbx 160 are fast and transparent. Optical compressors (LA-2A) are slow and program-dependent, responding naturally to musical dynamics. FET compressors (1176) are fast with aggressive character. Tube/variable-mu compressors (Fairchild 670) are slow, smooth, and colored. These hardware characteristics are emulated extensively in software plugins.

## Questions

```yaml
- question: "What does a 4:1 compression ratio mean?"
  type: multiple-choice
  options:
    - "4 dB input = 1 dB output"
    - "For every 4 dB above the threshold, only 1 dB passes through"
    - "Compression is applied 4x per second"
    - "Compressor boosts 4x"
  answer: 1
  explanation: "A 4:1 ratio means for every 4 dB the signal exceeds the threshold, only 1 dB passes through. Higher ratios = more aggressive compression."

- question: "True or false: A faster attack time allows more of the signal peak to pass through."
  type: true-false
  answer: false
  explanation: "A faster attack means the compressor responds more quickly, catching peaks sooner. A slower attack lets more of the transient through before compression engages — which is often desirable for drums."

- question: "What is makeup gain in a compressor?"
  type: short-answer
  answer: "An output level control that brings the compressed signal back to its original average level, compensating for the reduction applied."
  explanation: "Without makeup gain, compressed signals sound quieter. Makeup gain restores overall loudness while maintaining dynamic reduction."

- question: "When mixing vocals, why might you use a slow attack setting?"
  type: multiple-choice
  options:
    - "To compress the vocal more aggressively"
    - "To let the initial consonants and transients through before compression engages, preserving natural articulation"
    - "To remove all dynamics from the vocal"
    - "Slow attack is always wrong for vocals"
  answer: 1
  explanation: "A slow attack lets the initial transient of each syllable pass uncompressed, preserving the natural snap and articulation of consonants while the compressor catches sustained vowel sounds."

```

## Explainer

Dynamic range compression is one of the most used and most misunderstood tools in audio production. Beginners often apply it indiscriminately, but skilled engineers use it with surgical precision: choosing the right threshold, ratio, attack, and release for each source to achieve a specific sonic goal.

The interplay between attack and release is particularly nuanced. Too fast an attack kills transients and makes drums sound flat; too slow a release causes pumping and breathing artifacts when the compressor fails to disengage cleanly between notes. Finding the right settings requires listening carefully to how the compressor interacts with the musical content — its rhythm, envelope, and dynamic variation.

Parallel compression (blending an uncompressed and heavily compressed signal) combines the punch of the original transients with the density of heavy compression. This technique, common in modern mixing, uses the compressor not as a limiter but as a texture engine — adding weight and sustain to drums while preserving the crack of the attack. Understanding compression deeply enables engineers to use it as a creative and corrective tool rather than a problem-solver of last resort.
