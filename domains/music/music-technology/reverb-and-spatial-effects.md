---
id: reverb-and-spatial-effects
title: Reverb and Spatial Effects
domain: music
course: music-technology
prerequisites:
- id: audio-signal-chain
  type: hard
builds-toward: []
tags:
- reverb
- spatial-effects
- mixing
- time-based-effects
stage: advanced
status: validated
---

# Reverb and Spatial Effects

## Core Idea
Reverb simulates the acoustic reflections that occur in physical spaces — rooms, halls, chambers, plates — placing sounds in a perceived environment. When sound is produced in a real space, reflections bounce off walls, floors, and ceilings, reaching the listener's ears at slightly different times and from different directions. The brain interprets these patterns as spatial information: room size, surface materials, and the source's position within the space.

Digital reverb algorithms recreate these reflection patterns through mathematical models. Algorithmic reverb (used in most hardware units and software plugins) generates early reflections — discrete initial echoes that convey room dimensions — followed by a dense, decaying reverberation tail. The key parameters are: pre-delay (the time gap between the dry signal and the first reflection, simulating distance from walls), decay time or RT60 (how long the tail takes to fade 60 dB, indicating room size), diffusion (how quickly reflections become dense), and high-frequency damping (simulating absorptive materials that attenuate high frequencies faster than lows).

Convolution reverb takes a different approach: it captures the acoustic fingerprint of a real space through an impulse response (IR) recording — a starter pistol shot or sine sweep in a cathedral, stairwell, or scoring stage. The IR is then convolved with the dry audio signal using FFT-based processing, mathematically placing the sound in that exact acoustic environment. The result can be uncannily realistic but requires more CPU and offers less real-time control than algorithmic approaches.

Delay effects repeat the signal at discrete intervals, creating echo effects that range from subtle timing reinforcement (slapback at 50–120ms) to rhythmic dotted-eighth or triplet delays synchronized to the song's tempo. Chorus, flanger, and phaser use very short delay lines (1–30ms) modulated by LFOs to create movement, width, and psychoacoustic thickness.

## Questions

```yaml
- question: "What is pre-delay in reverb?"
  type: multiple-choice
  options:
    - "Time before reverb processing begins in the CPU"
    - "The gap between the dry signal and the first reflection"
    - "A shorter, earlier reverb tail"
    - "How long reverb takes to stop"
  answer: 1
  explanation: "Pre-delay creates a gap between the original sound and the first reflection, simulating larger rooms and preventing the reverb from muddying the dry signal's attack."

- question: "True or false: Delay and reverb are the same effect."
  type: true-false
  answer: false
  explanation: "Delay repeats the signal at regular intervals (echo). Reverb simulates many simultaneous reflections decaying into a tail (ambience). They are distinct effects with different sonic characters and uses."

- question: "What does decay time refer to in reverb?"
  type: short-answer
  answer: "The time it takes for the reverb tail to fade 60 dB (to inaudibility) after the source signal stops — also called RT60."
  explanation: "Short decay (0.5–1s) simulates small rooms or studios. Long decay (3+ seconds) simulates cathedrals or arenas. Matching decay time to the tempo and character of the music is essential for a natural-sounding mix."

- question: "Why is wet/dry mix important for reverb?"
  type: multiple-choice
  options:
    - "It changes how much reverb is heard versus the dry signal"
    - "It determines the reverb color and frequency response"
    - "It affects the attack time of the reverb"
    - "It controls the pre-delay amount"
  answer: 0
  explanation: "The wet/dry mix controls the balance between the reverb effect and the original signal. On a send/return setup, the reverb plugin is typically set to 100% wet, with blend controlled by the send level."

```

## Explainer

Reverb is one of the most powerful mixing tools because it fundamentally affects perceived space and depth. Dry, un-reverbed sounds feel close and present; heavy reverb pushes elements back and creates a sense of large acoustic environments. Strategic use of different reverb types and amounts creates a three-dimensional mix where elements occupy distinct positions in a simulated acoustic space.

The choice between algorithmic and convolution reverb depends on the application. Convolution excels when accuracy to a specific real space matters — film scoring on virtual stages, orchestral simulation, acoustic guitar in a specific concert hall. Algorithmic excels for creative sound design, real-time flexibility, and the warmth of classic hardware units (like the EMT 140 plate, Lexicon 480L, or Bricasti M7) that have been used on iconic recordings.

The interplay between reverb and EQ is particularly important. Applying high-pass and low-pass filters to a reverb — cutting below 200–300 Hz and above 8–10 kHz — prevents the reverb from muddying low-end elements while allowing the tail to breathe in the mid-high range. This technique, called EQ on the reverb return, is standard practice in professional mixing.
