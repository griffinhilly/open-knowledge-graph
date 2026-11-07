---
id: acoustic-phonetics
title: Acoustic Phonetics
domain: language-and-communication
course: linguistics
prerequisites:
- id: articulatory-phonetics
  type: hard
- id: sound-waves-intro
  type: soft
builds-toward:
- suprasegmental-phonology
- intonational-phonology
tags:
- phonetics
- acoustics
- spectrogram
- formants
- source-filter
- voice-onset-time
stage: formal-systems
status: validated
---
# Acoustic Phonetics

## Core Idea
Acoustic phonetics studies the physical properties of speech sounds as sound waves. Vibration of the vocal folds produces a source sound with a fundamental frequency, heard as pitch, plus higher harmonics; the shape of the vocal tract then acts as a filter that strengthens some frequencies, called formants. Different vowels have different formant patterns, mainly in the first two formants, F1 and F2. Spectrograms display these patterns over time, letting phoneticians measure vowels, consonant cues such as voice onset time, and intonation.

## How It's Best Learned
Record your own voice in free software such as Praat and look at the waveform and spectrogram of simple words. Say "heed," "had," "hod," and "who'd" and watch the dark formant bands move. Compare "pin" and "bin" to see the delay before voicing in the voiceless stop. Link each acoustic pattern back to the articulatory gesture that causes it, so the two descriptions reinforce each other.

## Common Misconceptions
- Pitch and formants are the same thing. (Pitch comes from the rate of vocal fold vibration; formants come from vocal tract resonances. You can sing one vowel on many pitches, or many vowels on one pitch.)
- On a spectrogram, words are separated by gaps of silence. (Running speech is mostly continuous; silences often mark the closure of a stop consonant rather than a word boundary.)
- Higher formant frequencies mean a louder sound. (Formant frequency is about where energy is concentrated on the frequency scale, not about overall intensity.)

## Questions

```yaml
- question: "Which pair of vowel properties is most closely linked to the first and second formants?"
  type: multiple-choice
  options:
    - "F1 to lip rounding, F2 to loudness"
    - "F1 to tongue height (inversely), F2 to tongue backness (front vowels have higher F2)"
    - "F1 to pitch, F2 to duration"
    - "F1 to voicing, F2 to nasality"
  answer: 1
  explanation: "High vowels such as /i/ and /u/ have low F1, and low vowels such as /ɑ/ have high F1. Front vowels such as /i/ have high F2, and back vowels such as /u/ have low F2. Lip rounding also lowers formants, but the height and backness links are the main ones."

- question: "In the source-filter model of speech, what plays the role of the filter?"
  type: multiple-choice
  options:
    - "The lungs"
    - "The vocal folds"
    - "The vocal tract above the larynx"
    - "The listener's ear"
  answer: 2
  explanation: "The vocal folds produce the source, a buzz rich in harmonics. The throat, mouth, and nasal cavities shape that buzz, amplifying some frequencies (the formants) and damping others. Changing tongue and lip position changes the filter."

- question: "A speaker can produce the vowel /a/ at a low pitch and then at a high pitch without changing which vowel listeners hear."
  type: true-false
  answer: true
  explanation: "Pitch depends on the fundamental frequency of vocal fold vibration, while vowel identity depends mainly on the formant pattern set by the vocal tract. The two can vary independently, which is why singers can hold one vowel across a melody."

- question: "What is voice onset time (VOT), and how does it help distinguish English 'pin' from 'bin'?"
  type: short-answer
  answer: "VOT is the time between the release of a stop consonant and the start of vocal fold vibration. In English 'pin,' the /p/ has a long delay with a burst of aspiration before voicing starts; in 'bin,' voicing begins at or very soon after release, so VOT is short."
  explanation: "VOT is one of the main acoustic cues to the voicing contrast in stops. Languages draw the voiced-voiceless boundary at different points along the VOT scale."
```

## Explainer

Articulatory phonetics describes how we make speech sounds. Acoustic phonetics describes what those sounds are physically: patterns of air pressure that travel as waves to a listener's ear. The two descriptions connect closely, and the acoustic one can be measured with a microphone and a computer.

Start with the **source**. When you speak a vowel, your vocal folds open and close rapidly. The rate of that cycle is the **fundamental frequency (F0)**, measured in hertz, and listeners hear it as pitch. The folds produce a buzz made of the fundamental and many **harmonics** at multiples of it.

Next comes the **filter**. The buzz passes through the throat, mouth, and sometimes the nose. Like a tube, this space resonates at certain frequencies and boosts the harmonics near them. These resonance peaks are **formants**. Moving the tongue and lips changes the shape of the tube, so it changes the formants. This explanation is called the **source-filter model**, developed in detail by the Swedish scientist Gunnar Fant.

The first two formants carry most vowel information:

- **F1** is inversely related to tongue height. High vowels like /i/ ("heed") have low F1; low vowels like /ɑ/ ("hod") have high F1.
- **F2** is related to tongue backness. Front vowels like /i/ have high F2; back vowels like /u/ ("who'd") have low F2.

For a typical adult male speaker of American English, /i/ has an F1 near 300 Hz and an F2 above 2,000 Hz, while /u/ has a similar F1 but an F2 below 1,000 Hz. Exact values differ by speaker, since longer vocal tracts produce lower formants.

The main tool for seeing all this is the **spectrogram**. Time runs left to right, frequency runs bottom to top, and darkness shows intensity. Vowels appear as dark horizontal bands, the formants. Fricatives such as /s/ appear as fuzzy, noisy energy, high in frequency for /s/. Stops such as /t/ appear as a short gap of silence (the closure) followed by a burst.

Spectrograms also reveal **voice onset time**. In English "pin," voicing begins well after the /p/ is released, with a puff of aspiration in between. In "bin," voicing starts at or soon after release. Listeners use this timing difference to hear the contrast.

Acoustic phonetics is the basis for speech technology, forensic voice comparison, and the study of intonation and tone, all of which depend on measuring sound rather than describing it by ear.
