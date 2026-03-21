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

## Questions

```yaml
- question: "A producer exports a MIDI file and sends it to a collaborator. The collaborator opens it in a different DAW and hears a completely different set of sounds than the producer intended. What explains this?"
  type: multiple-choice
  options:
    - "The MIDI file was corrupted during export, scrambling the note data"
    - "MIDI files are tied to specific DAWs and cannot be opened cross-platform without conversion"
    - "MIDI contains only performance instructions — note, velocity, timing — not audio; the sounds depend entirely on which instruments the DAW assigns to play them"
    - "The collaborator's computer audio hardware produces different waveforms than the producer's"
  answer: 2
  explanation: "This is the key insight about MIDI: a MIDI file contains no sound whatsoever. It is a set of performance messages — 'play note 60 at velocity 80 for 0.5 seconds' — and those messages are sent to whatever sound-producing module is assigned to receive them. If the producer used a Rhodes piano library and the collaborator's DAW defaults to a synth pad, the notes are identical but the sounds are completely different. MIDI separates musical information from sound production, which is both the source of its power and the reason collaboration requires agreeing on instruments."

- question: "In audio production, what does compression do to a signal?"
  type: multiple-choice
  options:
    - "It reduces the file size by encoding audio more efficiently, like MP3 compression"
    - "It adds simulated room reflections to create a sense of acoustic space"
    - "It reduces the dynamic range by lowering loud peaks relative to quieter moments, producing a denser and punchier sound"
    - "It boosts or cuts specific frequency bands to shape the tonal character of the sound"
  answer: 2
  explanation: "Audio compression (dynamic range compression) is completely different from data compression. It works by detecting loud moments above a threshold and reducing their volume, closing the gap between loud and quiet. This makes the overall level more consistent, allows the mix to sit louder, and gives transients (drums, plucks) a punchy, dense character. Option A is data compression (MP3, FLAC). Option B is reverb. Option D is EQ. All three are distinct signal processing tools with different functions in the mix."

- question: "In a DAW's piano-roll interface, the same MIDI sequence can trigger a string orchestra, a drum kit, or a synthesizer simply by changing which instrument is assigned to receive it."
  type: true-false
  answer: true
  explanation: "True — this is precisely what 'MIDI contains no sound' means in practice. The piano-roll encodes timing, pitch, velocity, and duration as abstract data. That data is routed to a sound-producing module (a virtual instrument, a hardware synthesizer, a sample library), and the module determines the actual sound. Changing the instrument assignment is non-destructive and instantaneous — the MIDI sequence is unchanged. This decoupling of musical content from timbre is one of the most powerful features of electronic composition."

- question: "Adding more tracks and more plugins to an electronic composition generally produces a richer, more professional result."
  type: true-false
  answer: false
  explanation: "False — this is one of the central misconceptions in electronic production. Unlike acoustic composition, where physical constraints limit the number of instruments, electronic composition imposes no natural ceiling. This makes restraint a deliberate choice. Layering too many tracks creates frequency conflicts, mud in the mix, and loss of individual clarity. Each sound should occupy a distinct sonic space (frequency band, rhythmic role, stereo position). Professional electronic music is often characterized by careful subtraction — fewer elements, each with more impact — not addition."

- question: "What is the key difference between the 'musical layer' and the 'sonic layer' in electronic composition, and why does their decoupling matter for composers?"
  type: short-answer
  answer: "The musical layer consists of what notes are played, in what rhythm, at what dynamic — the compositional content. The sonic layer consists of what timbres, spatial qualities, and textures are used — the production decisions. In acoustic music these are inseparable (a violin playing C has a fixed timbre). In electronic composition they are completely decoupled: a MIDI note is abstract, and the timbre is a separate routing decision. This matters because it doubles the compositional decisions: a producer must design both the music and the sound simultaneously, and choices at the sonic layer (reverb depth, compression, EQ) are as expressive as choices at the musical layer."
  explanation: "The decoupling is what makes electronic composition uniquely flexible and uniquely demanding. A melody that feels sparse and fragile with a solo piano patch can feel massive and anthemic with a layered synthesizer pad — the same notes, completely different emotional effect. Conversely, a compelling musical idea can be ruined by poor sound design. Understanding that these are two separate creative dimensions — and that both require deliberate choices — is the foundational insight of electronic composition."
```

## Explainer

Electronic composition requires understanding two separate layers simultaneously: the **musical layer** (what notes are played, in what rhythm, at what dynamic) and the **sonic layer** (what timbres and spatial qualities are used). In acoustic music, these are inseparable — a violin playing C has a specific timbre built into the instrument. In electronic composition, they are completely decoupled: a MIDI note is just a number, and the timbre it triggers is a separate decision made by routing that note to a synthesizer or sample library. This separation is what makes electronic composition uniquely flexible — and uniquely demanding.

**MIDI sequencing** builds directly on your understanding of rhythm, syncopation, and meter. In a piano-roll interface, time runs left to right (you're literally drawing rhythm in space), and pitch runs bottom to top. A note is a rectangle: its horizontal position is its rhythmic placement, its length is its duration, and its vertical position is its pitch. Syncopated rhythms, metric grooves, and polyrhythmic patterns you understand conceptually become visually explicit on this grid. The key insight is that a MIDI sequence contains no sound at all — it is a set of performance instructions sent to a sound-producing module. This is why the same MIDI file can sound like a string orchestra or a drum kit depending on what instrument is assigned to receive it.

**Audio sampling** is the complementary technique: instead of programming abstract MIDI notes, you work with recorded sound directly. A sample is a recorded audio file treated as raw material — you can layer it, loop it, pitch it up or down, or chop it into fragments. When you encountered sine and cosine curves, you were seeing the mathematical foundation of sound: every recorded sample is ultimately a waveform, a graph of air pressure over time. This is why **signal processing** works as it does. Reverb simulates acoustic space by adding time-delayed, decaying copies of the signal — your ear interprets this delay pattern as reflections from surfaces. Compression reduces the ratio between loud and quiet moments, bringing up the floor and containing the peaks. EQ shapes the frequency spectrum, boosting or cutting frequency bands; a low-cut EQ is literally removing the lower-frequency sine wave components from the signal.

The most important compositional principle in electronic music is the same as in acoustic music: **restraint**. The difference is that electronic composition removes natural physical constraints — you can layer 200 tracks, add unlimited reverb, program rhythms no human could perform. This makes restraint a deliberate choice rather than a natural boundary. Building a coherent texture means deciding which sounds occupy which frequency bands, which rhythmic layers sit at which metric levels, and which timbres contrast clearly enough to remain individually audible. Every MIDI velocity choice and timing decision — including the choice to leave timing slightly humanized rather than grid-quantized — is a compositional statement about feel and energy, just as much as the notes themselves.
