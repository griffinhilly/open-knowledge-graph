---
id: voice-leading-error-recognition-and-correction
title: Voice Leading Error Recognition and Correction
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: voice-leading-error-detection
  type: hard
- id: voice-leading-principles
  type: hard
tags:
- error-detection
- part-writing
- voice-leading
- correction
stage: formal-systems
status: draft
---

# Voice Leading Error Recognition and Correction

## Core Idea
Common voice leading errors include parallel fifths and octaves, crossed voices, poor spacing, improper resolution of dissonance, awkward leaps without direction, and loss of voice independence. Recognizing these errors requires checking each voice independently for smooth motion while simultaneously checking all pairs of voices for parallel motion. Correction requires understanding the underlying principle rather than memorizing rules: parallel perfect intervals obscure voice independence, so rewriting to move voices in contrary or oblique motion solves the problem.

## How It's Best Learned
Practice identifying and correcting voice leading errors in short four-part excerpts. Start with obvious errors, then work with subtle cases where fixing one error might create another that requires rethinking the entire progression.

## Explainer

From your prerequisite study of voice-leading error detection, you know how to identify the surface symptoms of poor voice leading. This topic asks the deeper question: not just "what is wrong?" but "why does it violate the underlying principles, and how do you correct it without creating a new problem?" Correction requires understanding the reason behind each rule well enough to know what the corrected version must accomplish.

The most common errors cluster around **parallel perfect intervals** — particularly parallel fifths and octaves. The prohibition is not arbitrary: when two voices move in the same direction by the same proportional interval (both moving up a step, creating a fifth at each step), they temporarily fuse into a single doubled voice rather than two independent melodic lines. The listener loses the sense that two separate voices are in conversation. The standard correction is to change the **type of motion** between the offending voices: where both moved in parallel, introduce contrary motion (one voice moves up, the other down), oblique motion (one voice stays, the other moves), or at minimum similar motion to a non-perfect interval. The goal is not to comply with a rule but to restore the independence of the two voices.

**Voice crossing** and **voice overlap** are spatial errors that disrupt the registral logic of four-part writing. Voice crossing occurs when a lower voice moves above a higher voice (bass moving higher than tenor, for instance). Voice overlap occurs when a voice moves higher than the previous position of the voice above it, even if they do not cross in the present moment. Both create confusion about which line is which, and both are easiest to catch by tracing each voice horizontally as an independent melody — a visual sweep that makes register violations immediately apparent. The correction is usually to choose a different soprano or bass note that keeps each voice within its natural range.

The most important principle for correction is **looking ahead**. Many voice leading errors are not local mistakes but inevitable consequences of choices made a chord or two earlier. A seventh that is introduced without preparation will need to resolve downward by step; if the voice has no natural downward path at the point of resolution, the problem must be fixed in the chord where the seventh first appeared. A leading tone that resolves downward when it should resolve upward usually means the leading tone was placed in a voice that needed to move down for other reasons — the solution is to reassign which voice carries the leading tone. This is why **constraint propagation** is the right mental model: fixing one note can create a new problem in the next chord, which creates a new constraint on the chord after that. The goal is not to fix the marked error in isolation but to write a passage where each voice flows naturally from beginning to end, with every constraint satisfied simultaneously.
