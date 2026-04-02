---
id: audio-codecs-and-formats
title: Audio Codecs and File Formats
domain: music
course: music-technology
prerequisites:
- id: digital-audio-fundamentals
  type: hard
builds-toward: []
tags:
- audio-formats
- codecs
- digital-audio
- audio-engineering
stage: advanced
status: validated
---

# Audio Codecs and File Formats

## Core Idea
An audio codec (coder-decoder) is an algorithm for encoding audio data, typically to reduce file size, and decoding it for playback. The choice of codec and container format determines audio quality, file size, playback compatibility, and suitability for specific use cases. Professionals must understand the tradeoffs between lossless and lossy codecs to make appropriate format decisions for recording, editing, delivery, and distribution.

Lossless formats preserve every sample exactly as recorded — the decoded audio is bit-for-bit identical to the original. WAV (Waveform Audio File Format) is the dominant uncompressed format in professional audio — a 24-bit/48kHz stereo file stores approximately 17 MB per minute. AIFF (Audio Interchange File Format) is Apple's equivalent, functionally similar. FLAC (Free Lossless Audio Codec) compresses audio without data loss, reducing WAV by approximately 50–60% — useful for archiving and audiophile streaming (Tidal MQA, Amazon Music HD, Apple Music Lossless use FLAC or ALAC). Broadcast WAV (BWF) embeds timecode and metadata into the WAV container, essential for film and broadcast post-production workflows.

Lossy codecs achieve much greater compression (10:1 or more) by perceptual coding: removing audio content the human auditory system is unlikely to notice — frequencies masked by louder simultaneous sounds, content below the hearing threshold, and temporal post-masking. MP3 (MPEG-1 Audio Layer III) was the dominant consumer format for 25 years. AAC (Advanced Audio Coding) is its successor, used by Apple, YouTube, and streaming platforms — at the same bitrate, AAC sounds better than MP3 due to improved psychoacoustic models. Opus is a highly efficient modern codec (used by Spotify, Discord, WhatsApp) that delivers excellent quality at low bitrates (96–160 kbps) through time-frequency adaptive coding.

Bitrate (kbps — kilobits per second) directly controls the quality/size tradeoff in lossy formats. 128 kbps AAC is sufficient for casual listening; 256–320 kbps is transparent to most listeners; 320 kbps MP3 is the highest standard MP3 bitrate. Variable bitrate (VBR) encoding allocates more bits to complex passages and fewer to simple ones, maintaining consistent perceived quality at lower average file size.

## Questions

```yaml
- question: "What is the fundamental difference between a lossless and a lossy audio codec?"
  type: multiple-choice
  options:
    - "Lossless formats produce larger files and better sound; lossy formats produce smaller files by permanently removing audio data based on perceptual models"
    - "Lossless formats only work on computers; lossy formats work on all devices"
    - "Lossless formats use higher sample rates; lossy formats use lower ones"
    - "Lossy formats are always inaudibly different from the original; lossless formats are audibly better"
  answer: 0
  explanation: "Lossless (WAV, FLAC, AIFF) decodes to the exact original audio. Lossy (MP3, AAC, Opus) permanently discards data deemed perceptually irrelevant, achieving smaller files but with potential quality degradation at low bitrates."

- question: "True or false: Re-encoding a 320 kbps MP3 to FLAC will produce a lossless, high-quality file equivalent to the original recording."
  type: true-false
  answer: false
  explanation: "FLAC is lossless, but it can only preserve what's in the source file. Converting a lossy MP3 to FLAC captures the already-degraded audio losslessly — the data lost during the original MP3 encoding cannot be recovered."

- question: "Why does AAC generally sound better than MP3 at the same bitrate?"
  type: short-answer
  answer: "AAC uses more sophisticated psychoacoustic models — better frequency resolution, improved temporal masking, and more efficient entropy coding. These improvements allow AAC to retain more perceptually important audio data within the same bitrate budget."
  explanation: "MP3's psychoacoustic model was constrained by 1980s computational limits. AAC was designed a decade later with better models for spectral and temporal masking, more efficient quantization, and tonal/noise component separation."

- question: "A sound effects library sells files for professional post-production use. Which format is most appropriate for the library?"
  type: multiple-choice
  options:
    - "128 kbps MP3 — small files are easier to download"
    - "320 kbps AAC — high bitrate provides sufficient quality for most uses"
    - "24-bit/96 kHz WAV or BWF — lossless, full fidelity, compatible with all professional DAWs"
    - "Opus at 256 kbps — modern codec, highly efficient"
  answer: 2
  explanation: "Professional sound effects libraries use lossless, high-resolution WAV or BWF files. Post-production engineers need full fidelity for time-stretching, pitch-shifting, and integration into high-resolution sessions. Lossy compression introduces artifacts that compound under processing."

```

## Explainer

The proliferation of audio formats reflects the tension between audio fidelity and practical constraints of storage, bandwidth, and computational resources. In the early history of digital audio, storage and bandwidth were genuinely scarce — MP3's ability to compress CD audio by a factor of 10 was transformative, enabling music to move over the early internet and portable digital players.

Today, storage is cheap enough that lossless streaming is commercially viable (Apple Music delivers 256 kbps AAC as its standard, with lossless ALAC to all subscribers at no additional cost). The practical need for lossy compression has shifted from storage to real-time communication — Opus at 48 kbps powers Discord, WebRTC, and voice calls while delivering intelligible audio with acceptably low latency.

For audio professionals, format decisions cascade through workflows. Always work in the highest-resolution lossless format available during production — any lossy encoding should be a deliberate final delivery step, not an intermediate storage decision. Applying effects and processing to already-lossy files compounds the artifacts, particularly with lossy codecs at borderline bitrates. The standard practice is: capture and edit in WAV/AIFF, master in WAV, deliver in the format and bitrate specified by each platform's technical requirements.
