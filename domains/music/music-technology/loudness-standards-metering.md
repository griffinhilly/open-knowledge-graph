---
id: loudness-standards-metering
title: Loudness Standards and Metering
domain: music
course: music-technology
prerequisites:
- id: audio-signal-chain
  type: hard
- id: dynamic-range-compression
  type: soft
builds-toward: []
tags:
- loudness
- metering
- mastering
- broadcast-standards
stage: advanced
status: validated
---

# Loudness Standards and Metering

## Core Idea
Loudness measurement in audio is far more complex than simply reading peak levels. Human loudness perception is frequency-dependent, time-dependent, and context-dependent — none of which peak meters capture. Modern loudness standards address this by measuring integrated loudness in LUFS (Loudness Units Full Scale), a unit that correlates with perceived loudness much better than peak level.

The LUFS standard (defined in ITU-R BS.1770) applies frequency-weighted filtering (K-weighting) that mimics human hearing — boosting sensitivity in the 2–5 kHz range and reducing sensitivity at low frequencies. It then averages this weighted measurement over time. The result is a number that reflects how loud audio actually sounds, rather than how high its peak amplitude goes.

Platform loudness normalization has fundamentally changed mastering practice. Spotify normalizes to -14 LUFS integrated; Apple Music to -16 LUFS; YouTube to -14 LUFS; broadcast television (EBU R128) to -23 LUFS; streaming game audio typically -24 LUFS. If a master is louder than the target, the platform turns it down. If it is quieter, it is turned up (or left as-is, depending on platform). This means the loudness war — the practice of hyper-compressing masters to competitive loudness — is largely self-defeating: an excessively compressed, dynamically flat master at -8 LUFS will simply be turned down to -14 LUFS, arriving at the same loudness as a more dynamic master while sounding worse due to lost transient information.

Three metering values matter for professional delivery: integrated LUFS (overall program loudness), true peak (the highest peak level accounting for inter-sample peaks that exceed sample-level readings, to prevent distortion in DAC reconstruction), and loudness range (LRA), which describes the dynamic variability of the content. Mastering engineers targeting streaming delivery aim for integrated levels around -14 to -16 LUFS with true peaks no higher than -1 dBTP.

## Questions

```yaml
- question: "What does LUFS measure that a standard peak meter does not?"
  type: multiple-choice
  options:
    - "The maximum sample value in the audio file"
    - "The frequency-weighted, time-integrated loudness that correlates with perceived loudness"
    - "The average bit depth across all samples"
    - "The ratio of low to high frequencies"
  answer: 1
  explanation: "LUFS applies K-weighting (mimicking human frequency sensitivity) and integrates over time to measure perceived loudness. A peak meter only reads maximum instantaneous sample values, which don't predict perceived loudness."

- question: "True or false: Mastering a track to a higher LUFS (e.g., -8 LUFS) guarantees it will sound louder on streaming platforms."
  type: true-false
  answer: false
  explanation: "Streaming platforms apply loudness normalization, turning down anything above their target (e.g., -14 LUFS for Spotify). A -8 LUFS master arrives at the same perceived loudness as a -14 LUFS master, but with less dynamic range and potentially worse transient reproduction."

- question: "What is a true peak meter, and why is it important for streaming delivery?"
  type: short-answer
  answer: "A true peak meter uses oversampling to detect inter-sample peaks — levels that can exceed 0 dBFS during digital-to-analog reconstruction even when no sample reaches 0 dBFS. Streaming platforms require true peaks below -1 dBTP to prevent distortion during codec encoding."
  explanation: "Sample-domain peak meters can miss inter-sample peaks. When audio is decoded by streaming codecs, these peaks can clip. True peak metering prevents this by simulating the reconstruction filter."

- question: "What loudness standard applies to music on Spotify's platform, and what does this mean for mastering?"
  type: multiple-choice
  options:
    - "-23 LUFS; masters must be extremely compressed to hit this target"
    - "-14 LUFS integrated; masters louder than this are turned down, making excessive limiting counterproductive"
    - "-0 dBFS peak; no dynamic range is permitted"
    - "-8 LUFS; all streaming platforms use the same standard"
  answer: 1
  explanation: "Spotify targets -14 LUFS. Tracks louder than this are turned down via normalization. This effectively ends the competitive value of loudness-maximized masters — the extra compression only costs dynamic range, it doesn't buy loudness."

```

## Explainer

Loudness standards emerged from the broadcast industry's need to prevent jarring volume jumps between programs and advertisements. EBU R128 (Europe) and ATSC A/85 (USA) mandated loudness-normalized broadcast, and streaming platforms subsequently adopted similar approaches. This shift fundamentally changed mastering economics: the "louder is better" logic that drove the loudness wars of the 1990s–2000s no longer applies in streaming-first contexts.

For mastering engineers, this means optimizing for quality rather than loudness — preserving the dynamic interest of a mix, managing true peak levels to prevent distortion in codec encoding, and targeting appropriate integrated loudness for each delivery format. A film mix at -23 LUFS, a pop song at -14 LUFS, and a podcast at -16 LUFS are all appropriate targets for their respective contexts.

Metering practice has evolved accordingly. Modern mastering sessions monitor LUFS alongside traditional peak meters and RMS meters, compare against reference tracks at matched loudness, and check loudness range (LRA) to ensure sufficient dynamic variation. The mastering engineer's role has shifted from loudness maximizer to quality guardian — ensuring that the final delivery conveys the artistic intent of the mix at appropriate levels for every platform.
