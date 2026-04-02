---
id: live-performance-technology
title: Live Performance Technology
domain: music
course: music-technology
prerequisites:
- id: audio-signal-chain
  type: hard
- id: microphone-types-and-techniques
  type: soft
builds-toward: []
tags:
- live-sound
- performance-technology
- pa-systems
- audio-engineering
stage: advanced
status: validated
---

# Live Performance Technology

## Core Idea
Live performance technology encompasses the equipment, signal routing, and engineering practices used to amplify, process, and distribute audio for live audiences. It is a distinct discipline from studio recording: there are no second takes, monitoring happens in real time, the acoustic environment is variable and often challenging, and the engineer must make decisions under pressure.

A live sound system consists of the stage input layer (microphones, DI boxes, on-stage monitoring), a signal transport layer (analog multicore snake or digital network protocol like Dante, AES50, or MADI), and the front-of-house (FOH) console layer. The FOH console (Avid Venue, Yamaha CL/QL, DiGiCo, Allen & Heath) mixes the artist signals for the main PA system facing the audience. The monitor console (sometimes the same console with separate mix outputs) sends individual mixes to the performers' in-ear monitors (IEMs) or wedge monitors — each musician needs to hear a personalized mix of themselves, other key instruments, and a click track if relevant.

PA system design involves understanding coverage patterns, speaker placement, time alignment, and gain before feedback. A line array speaker system (vertically curved speaker cabinets with acoustic coupling between elements) provides more uniform coverage at long throw distances than point-source speakers, with the curve's angle calibrated to project more energy at distant audience areas and less at the front rows. Subwoofers handle the low-frequency content (typically below 80–100 Hz) that main array elements cannot efficiently reproduce.

Gain before feedback — the amount of gain achievable before the microphone picks up its own amplified signal and causes feedback — is the fundamental constraint of live sound. It is maximized by: using directional microphones, positioning microphones close to sources, keeping monitors behind (rather than in front of) microphones, using acoustic treatment to reduce room modes, and applying narrow parametric EQ cuts at feedback frequencies (identified through a ring-out process before the show).

## Questions

```yaml
- question: "What is the difference between a front-of-house (FOH) mix and a monitor mix?"
  type: multiple-choice
  options:
    - "FOH is the mix for the recording; monitor mix is for the audience"
    - "FOH is the mix sent to the PA system for the audience; monitor mix is a personalized mix sent to performers on stage"
    - "FOH is the stereo mix; monitor is the mono mix"
    - "There is no difference — both receive the same mix"
  answer: 1
  explanation: "FOH is what the audience hears from the main PA system. Monitor mixes are customized for each performer — a vocalist typically wants their voice louder, a drummer wants more kick and bass, a keyboard player wants the click track prominently."

- question: "True or false: In-ear monitors (IEMs) generally provide better gain-before-feedback performance than wedge monitors."
  type: true-false
  answer: true
  explanation: "IEMs are sealed in the ear canal, completely isolated from the stage's acoustic environment. They cannot feed back through the main PA system and allow lower stage volume, which improves FOH gain before feedback and reduces stage bleed into microphones."

- question: "What is time alignment in a PA system, and why is it important?"
  type: short-answer
  answer: "Time alignment delays signals to different speaker elements so they arrive at the audience simultaneously. Without it, sound from nearby speakers arrives before sound from distant speakers, causing comb filtering (phase cancellation between arrivals) and degraded intelligibility."
  explanation: "Sound travels at approximately 340 meters/second. A speaker 10 meters closer to the audience than another sends its signal 29 ms earlier. Adding a 29 ms delay to the closer speaker aligns their arrivals, producing coherent sum rather than interference."

- question: "During soundcheck, a monitor mix causes feedback through a stage wedge. What is the most surgical fix that preserves monitor intelligibility?"
  type: multiple-choice
  options:
    - "Turn down all monitor levels until feedback stops"
    - "Identify the feedback frequency using a spectrum analyzer and apply a narrow parametric EQ cut at that specific frequency"
    - "Replace the wedge monitor with an omnidirectional speaker"
    - "Increase the main PA volume to mask the feedback"
  answer: 1
  explanation: "Feedback occurs at specific room resonant frequencies. A narrow EQ notch (high Q, 3–6 dB cut) at the feedback frequency breaks the loop without significantly degrading the monitor mix. This is more surgical than broad level reduction."

```

## Explainer

Live sound engineering is one of the most demanding audio disciplines because it requires all the technical knowledge of studio work — signal chain, EQ, compression, dynamics — applied without the luxury of time, undo, or second attempts. A live mix engineer must simultaneously manage monitor issues from stage, maintain the FOH mix for thousands of people, troubleshoot technical problems as they arise, and respond to the acoustic changes caused by a full audience versus an empty soundcheck room.

The acoustic behavior of a venue with an audience differs significantly from the same venue empty — bodies absorb high-frequency energy and reduce reflections, lowering the RT60 (reverb decay time) and changing the frequency response of the room. Experienced engineers account for this difference during soundcheck, either through prior experience with a venue or by making mental notes about how to adjust the mix when the room fills.

Digital live consoles transformed the profession. Snapshot recall — saving and recalling complete console states for different songs or acts — removes the risk of misreferencing analog snapshots. Digital signal routing eliminates patching errors. Remote control via tablet allows the engineer to walk the room during soundcheck and adjust while listening from the audience's perspective. These capabilities have raised the baseline quality of live sound significantly, though the fundamental acoustic and psychoacoustic principles that govern the craft remain unchanged.
