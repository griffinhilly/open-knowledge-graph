---
id: electronic-composition-basics
title: Electronic Composition Basics
domain: music
course: composition
prerequisites:
- id: texture-in-composition
  type: soft
- id: rhythm-and-syncopation
  type: hard
- id: time-signatures-and-meter
  type: soft
- id: graphing-sine-and-cosine
  type: soft
- id: ratios
  type: soft
tags:
- DAW
- MIDI
- electronic-music
- sequencing
- sampling
- production
stage: formal-systems
status: validated
---

# Electronic Composition Basics

## Core Idea
Electronic composition uses digital audio workstations (DAWs) to record, sequence, and process sound into finished musical works. Core concepts include MIDI sequencing (programming notes via a piano-roll interface, separating musical information from sound production), audio sampling (recording or using pre-recorded sounds as raw material), layering tracks with different timbres to build texture, and using signal processing — reverb for space, compression for density and punch, EQ for timbral shaping — to craft the sonic environment. Unlike acoustic composition, electronic composition requires decisions at both the musical and sonic production levels simultaneously.

## How It's Best Learned
Complete a sequence of exercises in a DAW: program a drum pattern using MIDI, record a melodic instrument part, layer a synthesizer pad, and apply basic reverb and compression — treating each step as a separate compositional decision.

## Common Misconceptions
- More tracks and more plugins do not make a better composition — restraint and clarity in sound selection are as important electronically as they are acoustically.
- MIDI velocity and timing quantization are compositional choices; over-quantizing removes the human rhythmic feel that makes music compelling.

## Explainer

Electronic composition requires understanding two separate layers simultaneously: the **musical layer** (what notes are played, in what rhythm, at what dynamic) and the **sonic layer** (what timbres and spatial qualities are used). In acoustic music, these are inseparable — a violin playing C has a specific timbre built into the instrument. In electronic composition, they are completely decoupled: a MIDI note is just a number, and the timbre it triggers is a separate decision made by routing that note to a synthesizer or sample library. This separation is what makes electronic composition uniquely flexible — and uniquely demanding.

**MIDI sequencing** builds directly on your understanding of rhythm, syncopation, and meter. In a piano-roll interface, time runs left to right (you're literally drawing rhythm in space), and pitch runs bottom to top. A note is a rectangle: its horizontal position is its rhythmic placement, its length is its duration, and its vertical position is its pitch. Syncopated rhythms, metric grooves, and polyrhythmic patterns you understand conceptually become visually explicit on this grid. The key insight is that a MIDI sequence contains no sound at all — it is a set of performance instructions sent to a sound-producing module. This is why the same MIDI file can sound like a string orchestra or a drum kit depending on what instrument is assigned to receive it.

**Audio sampling** is the complementary technique: instead of programming abstract MIDI notes, you work with recorded sound directly. A sample is a recorded audio file treated as raw material — you can layer it, loop it, pitch it up or down, or chop it into fragments. When you encountered sine and cosine curves, you were seeing the mathematical foundation of sound: every recorded sample is ultimately a waveform, a graph of air pressure over time. This is why **signal processing** works as it does. Reverb simulates acoustic space by adding time-delayed, decaying copies of the signal — your ear interprets this delay pattern as reflections from surfaces. Compression reduces the ratio between loud and quiet moments, bringing up the floor and containing the peaks. EQ shapes the frequency spectrum, boosting or cutting frequency bands; a low-cut EQ is literally removing the lower-frequency sine wave components from the signal.

The most important compositional principle in electronic music is the same as in acoustic music: **restraint**. The difference is that electronic composition removes natural physical constraints — you can layer 200 tracks, add unlimited reverb, program rhythms no human could perform. This makes restraint a deliberate choice rather than a natural boundary. Building a coherent texture means deciding which sounds occupy which frequency bands, which rhythmic layers sit at which metric levels, and which timbres contrast clearly enough to remain individually audible. Every MIDI velocity choice and timing decision — including the choice to leave timing slightly humanized rather than grid-quantized — is a compositional statement about feel and energy, just as much as the notes themselves.
