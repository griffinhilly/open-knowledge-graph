---
id: midi-protocol-and-sequencing
title: MIDI Protocol and Sequencing
domain: music
course: music-technology
prerequisites:
- id: pitch-and-frequency
  type: soft
builds-toward: []
tags:
- midi
- sequencing
- music-production
- digital-instruments
stage: advanced
status: validated
---

# MIDI Protocol and Sequencing

## Core Idea
MIDI (Musical Instrument Digital Interface) is a communication protocol that transmits performance data between electronic musical instruments, computers, and other devices. Introduced in 1983 and standardized across manufacturers, MIDI fundamentally separated the act of performing music from the act of producing sound — enabling a single controller to trigger any synthesizer or sampler, and allowing performances to be recorded, edited, and replayed with perfect accuracy.

MIDI transmits messages, not audio. A note-on message contains the note number (0–127, where 60 = middle C), velocity (0–127, representing how hard a key was pressed), and channel (1–16). A note-off message ends the note. This distinction is essential: MIDI data is descriptive (what to play) while audio data is acoustic (the actual sound). The synthesizer or sample player receiving MIDI generates the audio — the MIDI controller only directs it.

Beyond note data, MIDI carries continuous controller (CC) messages for parameters like volume (CC7), pan (CC10), expression (CC11), and modulation (CC1). Pitch bend uses a 14-bit resolution (0–16383) for smooth portamento. Program change messages switch between preset sounds. System Exclusive (SysEx) messages allow device-specific parameter control not covered by the standard spec.

MIDI sequencing in a DAW records these messages as time-stamped data in a piano roll or step sequencer, where notes appear as horizontal blocks positioned on a pitch grid. Unlike audio recordings, MIDI data is infinitely editable: notes can be moved, transposed, quantized to the nearest grid division, or given entirely new velocities — all without audio degradation. This malleability makes MIDI central to electronic, hip-hop, and pop production workflows.

## Questions

```yaml
- question: "What does MIDI actually transmit?"
  type: multiple-choice
  options:
    - "Audio waveforms"
    - "Note-on/off messages and controller data"
    - "Pre-recorded samples"
    - "Timing only"
  answer: 1
  explanation: "MIDI is data, not audio. It sends messages like 'note C4 velocity 100'. The synthesizer or sample library generates the actual sound from that instruction."

- question: "True or false: MIDI data can only be sent between one pair of devices."
  type: true-false
  answer: false
  explanation: "MIDI supports 16 channels per cable, and multiple devices can communicate via MIDI hubs, allowing complex instrument chains and multi-channel productions."

- question: "What is a program change in MIDI?"
  type: short-answer
  answer: "A MIDI message that switches between preset sounds on a synthesizer or instrument without interrupting the performance."
  explanation: "Program changes let you switch synth sounds mid-sequence without manually adjusting parameters. Combined with bank select (CC0/CC32), they access large libraries of presets."

- question: "What are control change (CC) messages in MIDI?"
  type: multiple-choice
  options:
    - "Messages that switch sounds"
    - "Messages that modulate continuous parameters like volume, filter cutoff, or modulation wheel"
    - "Messages that control recording"
    - "Old MIDI messages no longer used"
  answer: 1
  explanation: "CC messages let you automate continuous parameters. CC7 = volume, CC1 = modulation wheel, CC74 = filter cutoff. They are essential for expressive, dynamic MIDI performances and automation."

```

## Explainer

MIDI transformed electronic music production by decoupling performance from sound generation. Before MIDI, instruments from different manufacturers could not communicate. After standardization, a single keyboard could trigger drum machines, synthesizers, and samplers simultaneously — and a DAW could record all of that performance data for later editing.

The enduring relevance of MIDI 1.0 (despite its age) reflects a design that matched musical intuition precisely. The 128-note, 128-velocity, 16-channel architecture covers the full practical range of acoustic instruments, and the CC message space has proven flexible enough to control everything from hardware synthesizers to software parameters.

MIDI 2.0, ratified in 2020, dramatically expands resolution (32-bit parameter control vs. 7-bit), adds per-note expression, and enables bidirectional device discovery. As hardware and software adopt MIDI 2.0, the increased expressiveness — per-note pitch bend, pressure, and timbre on any note simultaneously — approaches the expressive range of acoustic instruments.

Sequencing in a DAW builds on MIDI's data structure: the piano roll visualizes note messages as positioned blocks, quantization aligns note times to a rhythmic grid, and automation lanes record CC streams as editable curves. This paradigm, developed in the 1980s, remains the primary interface for composing and arranging electronic music today.
