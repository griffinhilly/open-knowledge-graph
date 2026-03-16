---
id: coarticulation-speech-context
title: Coarticulation and Phonetic Context Effects in Speech
domain: psychology
course: cognitive-psychology
prerequisites:
- id: phoneme-perception-categorical
  type: hard
- id: speech-production-planning
  type: hard
builds-toward:
- language-comprehension
tags:
- language
- speech
- production
- perception
stage: formal-systems
status: draft
---

# Coarticulation and Phonetic Context Effects in Speech

## Core Idea
In speech production, the same phoneme is articulated differently depending on surrounding phonemes—this is coarticulation. The /d/ in 'deed' is produced with different tongue positions than the /d/ in 'dood' due to anticipatory and carryover effects. Listeners must compensate for coarticulation during comprehension, inferring intended phoneme categories from highly variable acoustic signals. This variation-invariance problem reveals that speech perception is inferential, not passive acoustic analysis.

## How It's Best Learned
Demonstrate spectrograms showing acoustic variability in the same phoneme across different contexts. Play acoustic examples showing how listeners compensate using contextual information—a token ambiguous between /b/ and /d/ may be heard as /b/ after 'al' but /d/ after 'il.'

## Common Misconceptions
- Assuming speech is produced as a sequence of discrete phoneme units; coarticulation shows production is continuous and overlapping.
- Treating acoustic-phonetic variability as a barrier to perception; listeners use context to resolve the variability.

## Explainer

From your study of categorical perception, you know that listeners hear phoneme categories discretely — a continuum from /ba/ to /pa/ is heard as one or the other, not as a gradient. And from speech production planning, you know that producing speech requires coordinating dozens of articulators according to abstract phonological targets. Coarticulation is what happens at the intersection of those two facts: the abstract phonological targets are implemented by a physical vocal tract that can't teleport between positions, so each phoneme's articulation bleeds into and is shaped by its neighbors.

**Coarticulation** means that the articulatory gestures for neighboring phonemes overlap in time rather than occurring in strict sequence. When you say "stew," your lips round in anticipation of the /uː/ vowel before you've finished the /st/ consonant cluster — this **anticipatory coarticulation** can begin many segments early for features like lip rounding. **Carryover coarticulation** goes the other direction: the articulatory state from a preceding phoneme persists into the following one. The /d/ in "deem" is produced with the tongue already raised toward the high front position of /iː/; the /d/ in "doom" is produced with the tongue backed and lowered toward /uː/. The acoustic result is that the same phoneme, /d/, produces systematically different acoustic signals depending on what comes next. The "same" phoneme is never acoustically identical across contexts.

This creates the **variation-invariance problem**: the input to the perceptual system is highly variable, yet the output of perception is stable categorical identification. How do listeners map variable acoustics onto stable phoneme categories? The answer is that perception is **inferential**, not passive acoustic analysis. Listeners do not map raw acoustic features to phonemes; they recover the *intended phonological gesture* from the acoustic signal, using context to compensate for coarticulation. A key demonstration is **perceptual compensation**: if you excise a /d/ from the word "dim" and place it before "oom," listeners hear it as /d/ even though the acoustic token was produced with the formant transitions appropriate for a high-front-vowel context. The auditory system does not simply classify the acoustic signal; it reverses-engineers the coarticulation to infer the intended segment.

The broader implication is that speech perception is not merely auditory pattern matching — it is a constrained inference process that draws on knowledge of production. The **motor theory of speech perception** takes this further, proposing that what listeners perceive are the underlying motor gestures, not the acoustic signals themselves. While the strong form of that theory is controversial, the data from coarticulation research firmly establishes the weaker claim: perception is inherently context-sensitive, actively compensating for the phonetic context in which a segment occurs. This makes speech a remarkable feat — each conversation requires both speaker and listener to solve, in real time, the problem of recovering discrete linguistic structure from a continuous, context-saturated acoustic stream.
