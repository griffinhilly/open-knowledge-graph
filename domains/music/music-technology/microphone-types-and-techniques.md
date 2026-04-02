---
id: microphone-types-and-techniques
title: Microphone Types and Recording Techniques
domain: music
course: music-technology
prerequisites:
- id: audio-signal-chain
  type: soft
builds-toward: []
tags:
- microphones
- recording
- studio-techniques
- transducers
stage: advanced
status: validated
---

# Microphone Types and Recording Techniques

## Core Idea
A microphone is a transducer that converts acoustic pressure variations (sound) into electrical signals. Different transducer technologies and polar patterns make microphones suited to very different recording situations, and choosing the right mic for a source is one of the most consequential decisions in recording.

The three dominant transducer types each have distinct characteristics. Dynamic microphones (like the Shure SM57 and SM58) use a moving coil attached to a diaphragm — sound pressure moves the coil through a magnetic field, inducing current. Dynamics are robust, handle high SPL (sound pressure levels) without distorting, require no power, and have a natural high-frequency roll-off that suits loud sources like guitar cabinets and snare drums. Condenser microphones use a thin charged diaphragm near a backplate — sound pressure changes the capacitance and generates voltage. Condensers are more sensitive, have wider and flatter frequency responses, and capture transient detail better, making them preferred for acoustic instruments, vocals, and overheads. They require phantom power (+48V). Ribbon microphones use a thin corrugated metal ribbon in a magnetic field. Ribbons have a natural figure-8 polar pattern, warm high-frequency rolloff, and excellent transient response — they are prized for brass instruments, room ambience, and vintage vocal sounds, but are fragile and can be damaged by phantom power.

Polar patterns define which directions a microphone is most sensitive to. Cardioid picks up primarily from the front, rejecting the rear. Supercardioid and hypercardioid are narrower, with small rear lobes. Omnidirectional picks up equally from all directions — useful for capturing room sound and free of proximity effect. Figure-8 (bidirectional) picks up front and back equally, rejecting the sides — used in mid-side (M/S) stereo recording and as ribbon microphones' natural pattern.

Placement technique dramatically affects the recorded sound. The proximity effect — a bass boost that occurs in directional microphones as the sound source moves closer — can be used intentionally for warmth or managed to avoid excessive low frequencies. Distance from the source determines the ratio of direct sound to room reflections; closer placement captures more detail and isolation, while further placement captures more natural room ambience.

## Questions

```yaml
- question: "Why do condenser microphones require phantom power (+48V) while dynamic microphones do not?"
  type: multiple-choice
  options:
    - "Condenser mics use more signal and need extra voltage to amplify"
    - "The condenser transducer requires an electrical charge on the diaphragm to function, supplied by phantom power"
    - "Dynamic mics generate their own power through the moving coil"
    - "Phantom power prevents hum in condenser circuits"
  answer: 1
  explanation: "Condenser microphones operate on capacitive principles — the diaphragm must be electrically charged (or have a permanently charged electret layer) to produce a signal. Phantom power supplies this voltage through the balanced cable."

- question: "True or false: The proximity effect causes a treble boost as a directional microphone moves closer to the sound source."
  type: true-false
  answer: false
  explanation: "Proximity effect causes a bass (low-frequency) boost in directional (cardioid, figure-8) microphones as the source moves closer. This can add warmth to vocals or cause muddiness if not managed."

- question: "What is the advantage of an omnidirectional polar pattern over cardioid when recording in a well-treated room?"
  type: short-answer
  answer: "Omnidirectional microphones have no proximity effect, flatter low-frequency response, and capture the room ambience evenly from all directions. In a good-sounding room, this produces a more natural, open recording."
  explanation: "Cardioid rejection of room sound is useful in noisy or poorly treated spaces, but in great-sounding rooms the ambience is desirable. Omnis also tend to have more extended and accurate frequency response."

- question: "A recording engineer is capturing a loud guitar amplifier at close range. Which microphone type is most appropriate?"
  type: multiple-choice
  options:
    - "A large-diaphragm condenser — wider frequency response captures all the harmonics"
    - "A ribbon microphone — the figure-8 pattern rejects the room"
    - "A dynamic microphone — handles high SPL without distortion and rolls off harsh high frequencies naturally"
    - "A boundary microphone — placement on the floor captures maximum bass"
  answer: 2
  explanation: "Dynamic mics like the SM57 are the industry standard for guitar cabs. They handle the high SPL without distortion, have a midrange emphasis that complements guitar harmonics, and are mechanically robust."

```

## Explainer

Microphone selection and placement is where a recording begins — every subsequent processing decision is shaped by the quality and character of the initial capture. A great microphone placement in a good-sounding room with an appropriate mic for the source will always yield better results than extensive corrective processing downstream.

Recording technique encompasses not just microphone choice but room treatment, source positioning, and the psychological management of performer comfort in the recording environment. Session engineers learn to assess each situation — source level, room acoustics, desired tonal character, isolation requirements — and make a rapid, informed placement decision.

Stereo recording techniques like spaced pair (AB), coincident pair (XY), near-coincident (ORTF), and mid-side (M/S) use multiple microphones to capture a natural stereo image. Each technique makes different tradeoffs between stereo width, mono compatibility, and phase coherence. Understanding these techniques, along with transducer and polar pattern characteristics, forms the foundational vocabulary of recording practice.
