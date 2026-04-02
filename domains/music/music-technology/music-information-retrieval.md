---
id: music-information-retrieval
title: Music Information Retrieval
domain: music
course: music-technology
prerequisites:
- id: digital-audio-fundamentals
  type: hard
builds-toward: []
tags:
- music-information-retrieval
- audio-analysis
- machine-learning
- signal-processing
stage: expert
status: validated
---

# Music Information Retrieval

## Core Idea
Music Information Retrieval (MIR) is the research field and engineering discipline concerned with extracting musically meaningful information from audio signals — automatically and computationally. MIR enables technologies like music recommendation (Spotify's Discover Weekly), automatic chord recognition, tempo detection, key estimation, music transcription, cover song identification, and genre classification.

MIR begins with feature extraction — computing numerical descriptors from audio that capture musically relevant properties. Temporal features describe signal energy and changes over time: RMS energy, zero-crossing rate, onset detection (finding the start of new notes or percussion hits). Spectral features describe the frequency content: spectral centroid (perceived brightness), spectral rolloff, spectral flux (rate of change between frames). Mel-frequency cepstral coefficients (MFCCs) are derived from a perceptually-scaled frequency representation (the Mel scale) and computed via a cepstral transformation — they efficiently encode the timbre and vocal/instrumental quality of audio and are the most widely used features in speech and music recognition.

Pitch estimation and chord recognition require identifying the fundamental frequency of pitched sounds from polyphonic audio. Constant-Q Transform (CQT) provides a frequency representation with logarithmic frequency resolution that aligns with musical pitch spacing (each octave spanning the same number of bins, matching how humans perceive pitch). Chromagram representations fold pitch into pitch class (the 12 notes of the chromatic scale, discarding octave information), enabling key and chord analysis.

Beat tracking and tempo estimation use onset detection and autocorrelation to find the pulse underlying rhythmic audio. Dynamic time warping (DTW) aligns two audio sequences of different tempos or durations, enabling score-to-audio alignment, cover song detection, and performance comparison.

## Questions

```yaml
- question: "What are MFCCs (Mel-Frequency Cepstral Coefficients) and what audio property do they primarily capture?"
  type: multiple-choice
  options:
    - "MFCCs measure tempo and rhythm patterns in audio"
    - "MFCCs capture the spectral envelope (timbre) of audio using a perceptually-scaled frequency transformation, making them effective for characterizing instrument and vocal sounds"
    - "MFCCs directly encode pitch and note information for transcription"
    - "MFCCs measure the loudness and dynamic range of audio"
  answer: 1
  explanation: "MFCCs compress the spectral shape of audio (its timbre) into a compact representation by applying the Mel frequency scale (perceptually-spaced) and a cepstral transformation. This makes them effective for distinguishing instruments, voices, and musical styles without capturing absolute pitch."

- question: "True or false: A chromagram preserves the octave information of detected pitches."
  type: true-false
  answer: false
  explanation: "A chromagram folds all detected pitches into 12 pitch classes (C, C#, D... B), ignoring octave. Middle C, C4, and low C all contribute to the same 'C' bin. This makes chromagrams useful for chord and key analysis but removes octave register information."

- question: "What is Dynamic Time Warping (DTW) used for in MIR?"
  type: short-answer
  answer: "DTW finds the optimal alignment between two time series of different lengths or tempos by allowing elastic warping of the time axis. In MIR, it aligns audio recordings of the same piece performed at different tempos, enabling cover song detection, score-to-audio alignment, and performance comparison."
  explanation: "Direct comparison of audio sequences fails when they have different tempos. DTW finds the minimum-cost path through a distance matrix between the two sequences, warping time to find the best correspondence."

- question: "Why does the Constant-Q Transform (CQT) have advantages over the standard STFT for musical pitch analysis?"
  type: multiple-choice
  options:
    - "The CQT is faster to compute than the FFT"
    - "The CQT uses logarithmically-spaced frequency bins matching musical pitch spacing, so each octave spans the same number of bins — aligning with how musicians and listeners perceive pitch"
    - "The CQT provides better time resolution for fast transients"
    - "The CQT does not require windowing, reducing spectral leakage"
  answer: 1
  explanation: "The STFT has linear frequency spacing, meaning low octaves get few bins while high octaves get many. The CQT's logarithmic spacing gives equal resolution across all octaves — matching musical note relationships and making chord, key, and melody analysis more natural."

```

## Explainer

Music Information Retrieval sits at the intersection of signal processing, machine learning, and musicology. Early MIR research (1990s–2000s) focused on handcrafted features and classical machine learning (SVM, k-NN, random forests). Modern MIR is dominated by deep learning: convolutional neural networks applied to mel spectrograms learn to classify genre, detect chords, or transcribe music directly from learned feature representations rather than handcrafted ones.

The applications of MIR are ubiquitous in the music industry. Streaming platforms use audio fingerprinting (based on spectral peak matching) for copyright identification (Shazam's algorithm, Gracenote). Recommendation systems combine audio feature similarity with collaborative filtering (user behavior). Automatic mixing systems (AI mastering services) use MIR to analyze tracks and apply genre-appropriate processing. Music education apps (Yousician, Simply Piano) use pitch detection to give real-time feedback on performance.

Research challenges in MIR include: polyphonic transcription (converting audio with multiple simultaneous notes into symbolic notation), lyrics alignment (finding where each sung word occurs in the audio), musical genre classification (inherently subjective and culture-dependent), and source separation (isolating individual instruments from a mixed recording). Demucs and Spleeter demonstrate recent deep learning progress on source separation, with commercially deployed applications in stem extraction services used by DJs, producers, and remix artists.
