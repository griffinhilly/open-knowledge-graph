---
id: auditory-system-anatomy-and-physiology
title: Auditory System Anatomy and Physiology
domain: psychology
course: biological-psychology
prerequisites:
- id: sensory-transduction-and-neural-coding
  type: hard
- id: auditory-processing-pathway
  type: soft
- id: auditory-system-cochlea-cortex
  type: hard
- id: auditory-transduction
  type: hard
tags:
- hearing
- cochlea
- sound
- tonotopy
stage: advanced
status: validated
---

# Auditory System Anatomy and Physiology

## Core Idea
Sound pressure waves drive the basilar membrane in the cochlea, where hair cells detect mechanical motion. Frequency is coded by position along the basilar membrane (tonotopy): high frequencies are detected near the oval window, low frequencies near the apex. Auditory nerve fibers extract interaural timing differences (time of arrival at each ear) and intensity differences for sound localization. Auditory cortex integrates complex acoustic features (spectral changes, temporal patterns) for perception of speech and music.

## How It's Best Learned
Study cochlear mechanics and frequency selectivity using traveling wave models. Examine tonotopic organization in cochlea and auditory cortex. Measure interaural time and intensity differences for sound localization. Study auditory scene analysis.

## Common Misconceptions
Cochlea works like a microphone / all frequencies are equally resolved / timing and intensity cues are processed independently / auditory cortex simply decodes peripheral information.

## Questions

```yaml
- question: "A patient suffers noise-induced hearing loss after prolonged exposure to very loud high-frequency sounds. Which part of the cochlea is most likely damaged, and why?"
  type: multiple-choice
  options:
    - "The apex, because high frequencies cause peak displacement there"
    - "The base near the oval window, because high frequencies cause peak displacement there"
    - "The entire basilar membrane equally, because loud sounds affect all regions"
    - "The middle of the cochlea, because that region is most mechanically vulnerable"
  answer: 1
  explanation: "Tonotopy maps high frequencies to the base of the cochlea (near the oval window) and low frequencies to the apex. Because loud sounds damage the region of peak displacement, high-frequency noise destroys outer hair cells near the base first. This is why noise-induced hearing loss characteristically affects high-frequency perception before low-frequency perception — and why the apex (option A) is wrong despite being what many students incorrectly assume from 'base' meaning 'fundamental.'"

- question: "When a sound arrives slightly earlier at the right ear than the left, which brain structure primarily processes this cue, and for what purpose?"
  type: multiple-choice
  options:
    - "The lateral superior olive, to compute interaural level differences for high-frequency localization"
    - "The medial geniculate nucleus, to relay frequency information to cortex"
    - "The medial superior olive, to detect microsecond interaural timing differences for low-frequency localization"
    - "The auditory cortex, which reconstructs spatial position from spectral patterns"
  answer: 2
  explanation: "Interaural time differences (ITDs) — microsecond differences in sound arrival time between ears — are processed by the medial superior olive (MSO), which contains coincidence-detection neurons tuned to specific delays. ITDs dominate localization for low-frequency sounds. High-frequency localization relies instead on interaural level differences (ILDs) processed by the lateral superior olive (LSO). Confusing ITD/ILD and MSO/LSO is extremely common; the key link is: timing → MSO → low frequencies; level → LSO → high frequencies."

- question: "Outer hair cells in the cochlea can actively contract in response to basilar membrane motion, amplifying vibration at their characteristic frequency."
  type: true-false
  answer: true
  explanation: "Outer hair cells are active mechanical amplifiers — they contain the motor protein prestin and can rapidly change their length in response to membrane depolarization, boosting basilar membrane motion at their characteristic frequency by up to ~40 dB. This active mechanism sharpens frequency tuning and extends the dynamic range of hearing. It is also the reason ototoxic drugs and loud noise cause such severe hearing loss: destroying outer hair cells removes this amplification, dramatically reducing sensitivity and frequency resolution."

- question: "The auditory cortex functions primarily as a passive relay station that simply decodes the frequency-sorted signals arriving from the medial geniculate nucleus."
  type: true-false
  answer: false
  explanation: "The auditory cortex is an active, hierarchical processor analogous to visual cortex, not a passive decoder. It performs complex pattern analysis — extracting spectral and temporal features that distinguish vowels from consonants, familiar voices from unfamiliar ones, and music from noise. Cortical responses are not merely a readout of tonotopic input; they are shaped by attention, context, and learning. Single-axis tonotopic organization visible in primary auditory cortex gives way to increasingly complex feature selectivity in higher auditory areas."

- question: "Why does the basilar membrane act as a mechanical Fourier transform, and why does this matter for how frequency information is encoded in the auditory nerve?"
  type: short-answer
  answer: "The basilar membrane is narrow and stiff near the base (oval window) and wide and flexible near the apex, creating a continuous gradient of mechanical resonance. Different sound frequencies cause peak displacement at different positions — high frequencies at the base, low frequencies at the apex. Because hair cells sit at fixed positions along this membrane, each hair cell responds maximally to one frequency (its characteristic frequency). The auditory nerve therefore encodes frequency spatially (place coding): different nerve fibers carry information about different frequencies, and this tonotopic map is preserved through all auditory brainstem nuclei up to cortex."
  explanation: "The key insight is that the brain doesn't need to compute frequency — the mechanics of the cochlea perform this decomposition before any neural processing begins. This is why cochlear damage causes frequency-specific hearing loss (damage at the base → high-frequency loss; damage at the apex → low-frequency loss), and why cochlear implants with electrode arrays positioned along the cochlea can partially restore frequency discrimination by stimulating tonotopically appropriate positions."
```

## Explainer

From your work on sensory transduction and auditory transduction, you understand the general principle: a physical stimulus is converted into neural signals by specialized receptor cells. In the auditory system, the physical stimulus is a pressure wave — alternating compressions and rarefactions of air molecules — and the receptor cells are **hair cells** in the cochlea. What makes the auditory system particularly elegant is the mechanical preprocessing that happens *before* transduction, which encodes frequency information purely through physics rather than computation.

When sound enters the cochlea through the oval window, it creates a traveling wave along the **basilar membrane** — a long, tapered structure that runs the length of the cochlear spiral. The basilar membrane is not uniform: it is narrow and stiff near the base (the oval window end) and wide and flexible near the apex. Because of this gradient, different frequencies cause maximum displacement at different locations. High-frequency sounds cause peak vibration near the base; low-frequency sounds near the apex. This spatial mapping of frequency to location is called **tonotopy**, and it is preserved all the way up through the auditory cortex. The cochlea is performing a mechanical Fourier transform — decomposing a complex sound into its frequency components and sorting them spatially.

Hair cells sitting atop the basilar membrane convert displacement into neural signals through the **tip link mechanism** you studied in auditory transduction: as the membrane vibrates, stereocilia deflect, tip links open mechanosensitive ion channels, potassium influx depolarizes the cell, and neurotransmitter is released onto auditory nerve fibers. What's noteworthy is that the frequency tuning of each hair cell is partly passive (mechanical, from basilar membrane position) and partly active: **outer hair cells** can actively contract and amplify basilar membrane motion at their characteristic frequency, acting as a biological amplifier that sharpens tuning and extends the range of audible sounds by about 40 dB. This active mechanism is energetically expensive and highly vulnerable to damage from loud noise and ototoxic drugs.

Sound localization requires comparing signals arriving at two ears and relies on two distinct cues. **Interaural time differences (ITDs)** — microsecond differences in when a sound arrives at each ear — are used for low-frequency localization and are processed in the medial superior olive, which contains neurons specialized for coincidence detection. **Interaural level differences (ILDs)** — differences in intensity caused by the head casting an acoustic shadow — dominate for high frequencies and are processed in the lateral superior olive. These two pathways converge in the inferior colliculus and project to the auditory cortex via the medial geniculate nucleus of the thalamus. The auditory cortex is not a passive receiver of already-decoded information; it performs complex pattern analysis — extracting the spectral and temporal features that distinguish a vowel from a consonant, or a familiar voice from an unfamiliar one — making it an active, hierarchical processor in the same sense as the visual cortex.
