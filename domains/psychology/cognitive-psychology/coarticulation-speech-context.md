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
status: validated
---

# Coarticulation and Phonetic Context Effects in Speech

## Core Idea
In speech production, the same phoneme is articulated differently depending on surrounding phonemes—this is coarticulation. The /d/ in 'deed' is produced with different tongue positions than the /d/ in 'dood' due to anticipatory and carryover effects. Listeners must compensate for coarticulation during comprehension, inferring intended phoneme categories from highly variable acoustic signals. This variation-invariance problem reveals that speech perception is inferential, not passive acoustic analysis.

## How It's Best Learned
Demonstrate spectrograms showing acoustic variability in the same phoneme across different contexts. Play acoustic examples showing how listeners compensate using contextual information—a token ambiguous between /b/ and /d/ may be heard as /b/ after 'al' but /d/ after 'il.'

## Common Misconceptions
- Assuming speech is produced as a sequence of discrete phoneme units; coarticulation shows production is continuous and overlapping.
- Treating acoustic-phonetic variability as a barrier to perception; listeners use context to resolve the variability.

## Questions

```yaml
- question: "A researcher excises a /d/ token recorded from the word 'dim' (where /d/ is followed by a high-front vowel) and splices it before 'oom.' Listeners still report hearing /d/. What does this best demonstrate?"
  type: multiple-choice
  options:
    - "The acoustic signal for /d/ is consistent regardless of surrounding vowel context, so the token sounds like /d/ in any setting"
    - "The perceptual system compensates for coarticulatory context, recovering the intended phoneme from a signal shaped by a different phonetic environment"
    - "Categorical perception forces a binary consonant choice regardless of the specific acoustic evidence"
    - "Listeners rely on lip reading rather than acoustic signals to identify consonants"
  answer: 1
  explanation: "This is the perceptual compensation phenomenon. The acoustic token was shaped by high-front vowel context (formant transitions appropriate for /iː/), yet listeners identify /d/ — the intended segment — when it occurs before a different vowel. This shows the perceptual system does not passively match acoustic templates; it infers the underlying phonological gesture by factoring out the coarticulatory context. Option A is the central misconception: if consonant acoustics were context-independent, coarticulation would not create a variation-invariance problem in the first place."

- question: "When saying 'stew,' a speaker's lips begin rounding before the /s/ and /t/ consonants are finished. This is best described as:"
  type: multiple-choice
  options:
    - "Carryover coarticulation — articulatory state from a preceding phoneme persisting into the current one"
    - "Anticipatory coarticulation — the gesture for an upcoming phoneme already shaping current articulation"
    - "A production error caused by insufficient articulatory planning"
    - "Evidence that phonemes are produced as discrete, non-overlapping units in a strict sequence"
  answer: 1
  explanation: "Anticipatory coarticulation occurs when an upcoming segment's articulatory requirements begin influencing current production. Lip rounding starting during /st/ in anticipation of the /uː/ vowel is a classic example — the vocal tract is already preparing for a segment that hasn't started yet. Carryover coarticulation (option A) is the reverse: a preceding phoneme's articulatory state persisting into the following one. Option D represents the misconception that coarticulation is designed to refute: speech is not a sequential chain of discrete, non-overlapping gestures."

- question: "The same phoneme produces acoustically consistent signals across different phonetic contexts, and this invariance is what allows listeners to reliably identify phoneme categories."
  type: true-false
  answer: false
  explanation: "This is precisely what coarticulation disproves. The same phoneme produces systematically different acoustic signals depending on what phonemes surround it — the /d/ in 'deed' has different formant transitions than the /d/ in 'dood' because the surrounding vowels shape the tongue position during the consonant. Acoustic variability is the rule, not the exception. The variation-invariance problem is the challenge of explaining how listeners achieve stable perceptual categories despite this variability — not by denying that variability exists."

- question: "Coarticulation means that articulatory gestures for neighboring phonemes overlap in time, so the same phoneme is physically produced differently depending on its phonetic context."
  type: true-false
  answer: true
  explanation: "This is the core definition of coarticulation. Because articulators move continuously rather than teleporting between positions, the gesture for an upcoming phoneme can begin before the current one ends (anticipatory coarticulation), and the state from a preceding phoneme can persist into the following one (carryover coarticulation). This temporal overlap means the same phoneme — say, /d/ — is realized with different articulatory specifics (and different acoustic outputs) in 'deed' versus 'dood.' Understanding this is key to understanding why the variation-invariance problem exists."

- question: "Why does coarticulation evidence support the view that speech perception is inferential rather than passive acoustic analysis?"
  type: short-answer
  answer: "Because the same phoneme produces systematically different acoustic signals in different contexts, yet listeners always identify it correctly. If perception were passive acoustic pattern-matching against stored templates, this variability should cause frequent errors. Instead, listeners correctly identify phonemes even when the acoustic token was shaped by a different phonetic context — demonstrating that the perceptual system actively infers the intended phonological gesture by compensating for the surrounding phonetic environment."
  explanation: "The key logical move is from variability of input to stability of output. Passive analysis predicts errors when the acoustic signal deviates from the stored template for a phoneme. Perceptual compensation experiments show that listeners are robust to exactly this kind of acoustic variation when it is explainable by coarticulation. The system is not asking 'what acoustic pattern do I hear?' but rather 'given this acoustic signal and this phonetic context, what phoneme was the speaker intending to produce?' — an inferential process that uses knowledge of how sounds are produced, not just how they sound."
```

## Explainer

From your study of categorical perception, you know that listeners hear phoneme categories discretely — a continuum from /ba/ to /pa/ is heard as one or the other, not as a gradient. And from speech production planning, you know that producing speech requires coordinating dozens of articulators according to abstract phonological targets. Coarticulation is what happens at the intersection of those two facts: the abstract phonological targets are implemented by a physical vocal tract that can't teleport between positions, so each phoneme's articulation bleeds into and is shaped by its neighbors.

**Coarticulation** means that the articulatory gestures for neighboring phonemes overlap in time rather than occurring in strict sequence. When you say "stew," your lips round in anticipation of the /uː/ vowel before you've finished the /st/ consonant cluster — this **anticipatory coarticulation** can begin many segments early for features like lip rounding. **Carryover coarticulation** goes the other direction: the articulatory state from a preceding phoneme persists into the following one. The /d/ in "deem" is produced with the tongue already raised toward the high front position of /iː/; the /d/ in "doom" is produced with the tongue backed and lowered toward /uː/. The acoustic result is that the same phoneme, /d/, produces systematically different acoustic signals depending on what comes next. The "same" phoneme is never acoustically identical across contexts.

This creates the **variation-invariance problem**: the input to the perceptual system is highly variable, yet the output of perception is stable categorical identification. How do listeners map variable acoustics onto stable phoneme categories? The answer is that perception is **inferential**, not passive acoustic analysis. Listeners do not map raw acoustic features to phonemes; they recover the *intended phonological gesture* from the acoustic signal, using context to compensate for coarticulation. A key demonstration is **perceptual compensation**: if you excise a /d/ from the word "dim" and place it before "oom," listeners hear it as /d/ even though the acoustic token was produced with the formant transitions appropriate for a high-front-vowel context. The auditory system does not simply classify the acoustic signal; it reverses-engineers the coarticulation to infer the intended segment.

The broader implication is that speech perception is not merely auditory pattern matching — it is a constrained inference process that draws on knowledge of production. The **motor theory of speech perception** takes this further, proposing that what listeners perceive are the underlying motor gestures, not the acoustic signals themselves. While the strong form of that theory is controversial, the data from coarticulation research firmly establishes the weaker claim: perception is inherently context-sensitive, actively compensating for the phonetic context in which a segment occurs. This makes speech a remarkable feat — each conversation requires both speaker and listener to solve, in real time, the problem of recovering discrete linguistic structure from a continuous, context-saturated acoustic stream.
