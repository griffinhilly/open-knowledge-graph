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
- id: auditory-system-overview
  type: hard
- id: auditory-transduction
  type: hard
tags:
- hearing
- cochlea
- sound
- tonotopy
stage: advanced
status: draft
---

# Auditory System Anatomy and Physiology

## Core Idea
Sound pressure waves drive the basilar membrane in the cochlea, where hair cells detect mechanical motion. Frequency is coded by position along the basilar membrane (tonotopy): high frequencies are detected near the oval window, low frequencies near the apex. Auditory nerve fibers extract interaural timing differences (time of arrival at each ear) and intensity differences for sound localization. Auditory cortex integrates complex acoustic features (spectral changes, temporal patterns) for perception of speech and music.

## How It's Best Learned
Study cochlear mechanics and frequency selectivity using traveling wave models. Examine tonotopic organization in cochlea and auditory cortex. Measure interaural time and intensity differences for sound localization. Study auditory scene analysis.

## Common Misconceptions
Cochlea works like a microphone / all frequencies are equally resolved / timing and intensity cues are processed independently / auditory cortex simply decodes peripheral information.

## Explainer

From your work on sensory transduction and auditory transduction, you understand the general principle: a physical stimulus is converted into neural signals by specialized receptor cells. In the auditory system, the physical stimulus is a pressure wave — alternating compressions and rarefactions of air molecules — and the receptor cells are **hair cells** in the cochlea. What makes the auditory system particularly elegant is the mechanical preprocessing that happens *before* transduction, which encodes frequency information purely through physics rather than computation.

When sound enters the cochlea through the oval window, it creates a traveling wave along the **basilar membrane** — a long, tapered structure that runs the length of the cochlear spiral. The basilar membrane is not uniform: it is narrow and stiff near the base (the oval window end) and wide and flexible near the apex. Because of this gradient, different frequencies cause maximum displacement at different locations. High-frequency sounds cause peak vibration near the base; low-frequency sounds near the apex. This spatial mapping of frequency to location is called **tonotopy**, and it is preserved all the way up through the auditory cortex. The cochlea is performing a mechanical Fourier transform — decomposing a complex sound into its frequency components and sorting them spatially.

Hair cells sitting atop the basilar membrane convert displacement into neural signals through the **tip link mechanism** you studied in auditory transduction: as the membrane vibrates, stereocilia deflect, tip links open mechanosensitive ion channels, potassium influx depolarizes the cell, and neurotransmitter is released onto auditory nerve fibers. What's noteworthy is that the frequency tuning of each hair cell is partly passive (mechanical, from basilar membrane position) and partly active: **outer hair cells** can actively contract and amplify basilar membrane motion at their characteristic frequency, acting as a biological amplifier that sharpens tuning and extends the range of audible sounds by about 40 dB. This active mechanism is energetically expensive and highly vulnerable to damage from loud noise and ototoxic drugs.

Sound localization requires comparing signals arriving at two ears and relies on two distinct cues. **Interaural time differences (ITDs)** — microsecond differences in when a sound arrives at each ear — are used for low-frequency localization and are processed in the medial superior olive, which contains neurons specialized for coincidence detection. **Interaural level differences (ILDs)** — differences in intensity caused by the head casting an acoustic shadow — dominate for high frequencies and are processed in the lateral superior olive. These two pathways converge in the inferior colliculus and project to the auditory cortex via the medial geniculate nucleus of the thalamus. The auditory cortex is not a passive receiver of already-decoded information; it performs complex pattern analysis — extracting the spectral and temporal features that distinguish a vowel from a consonant, or a familiar voice from an unfamiliar one — making it an active, hierarchical processor in the same sense as the visual cortex.
