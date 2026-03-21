---
id: word-recognition-lexical-access
title: Word Recognition and Lexical Access
domain: psychology
course: cognitive-psychology
prerequisites:
- id: language-comprehension
  type: hard
- id: semantic-processing-temporal-cortex
  type: soft
builds-toward:
- sentence-comprehension-parsing
tags:
- language
- word-recognition
- lexical
- vocabulary
stage: advanced
status: draft
---

# Word Recognition and Lexical Access

## Core Idea
Word recognition is the process of identifying written or spoken words and accessing their meanings. Multiple candidates are initially activated based on phonological or orthographic similarity; context and frequency determine which meaning dominates. Word frequency effects and neighborhood effects reveal that recognition involves parallel activation of related representations.

## How It's Best Learned
Examine lexical decision tasks and eye-tracking studies showing that multiple word meanings are briefly activated even in context where one meaning dominates.

## Questions

```yaml
- question: "A reader encounters 'bank' in the sentence 'She sat by the bank and watched the water.' Eye-tracking shows a brief comprehension delay. What does this most directly suggest about lexical access?"
  type: multiple-choice
  options:
    - "The reader did not know the word 'bank' and had to retrieve it from long-term memory"
    - "Context prevented the financial institution meaning from being activated, but the river meaning took time to identify"
    - "Both meanings of 'bank' were simultaneously activated, and context suppressed the financial meaning a moment later"
    - "The high frequency of the financial institution meaning slowed down activation of the contextually correct meaning"
  answer: 2
  explanation: "Research on ambiguous words consistently shows that both meanings are activated in parallel during lexical access, regardless of context. Contextual information operates with a slight delay — it resolves the competition after the fact rather than preventing the wrong meaning from activating at all. The comprehension delay reflects this competition: the financial meaning was activated and had to be suppressed. Option B is the classic misconception — context doesn't block irrelevant meanings from activating; it selects the winner after multiple candidates have already entered the race."

- question: "A word with many neighbors (words differing by one letter, like 'cat' → 'bat,' 'hat,' 'mat') should be recognized:"
  type: multiple-choice
  options:
    - "Faster, because activation spreads through a densely connected network"
    - "At the same speed, because neighbor words are separate entries that don't interfere"
    - "More slowly, because more competitors are activated simultaneously and must be suppressed"
    - "Faster, because high-frequency words like 'cat' have elevated resting activation regardless of neighborhood"
  answer: 2
  explanation: "High-neighborhood words activate more competitors in parallel, which slows recognition because competition-resolution must suppress more alternatives before the target wins. This is direct evidence that recognition is a competitive process, not a single-path lookup. Option A confuses spreading activation (which does occur) with speed — more spread means more interference in this case. Option D conflates two distinct phenomena: frequency raises resting activation (a real effect), but the question specifically asks about the neighborhood effect, which adds competition overhead."

- question: "Even in a sentence context that makes one meaning of an ambiguous word obvious, both meanings are briefly activated in the mental lexicon."
  type: true-false
  answer: true
  explanation: "Ambiguous-word studies using eye-tracking and priming consistently show that initial lexical activation is 'promiscuous' — context operates with a short delay, so the irrelevant meaning is activated before context can suppress it. This is not poor comprehension; it is the architecture of the parallel-activation system. Skilled readers resolve the competition faster, but they still activate both meanings. This finding rules out purely top-down models in which context filters activation before it begins."

- question: "Word frequency effects in recognition demonstrate that the mental lexicon is organized like a dictionary, with common words positioned near the beginning for faster sequential lookup."
  type: true-false
  answer: false
  explanation: "Word recognition is parallel, not sequential — the mental lexicon is not searched from a starting point. Frequency effects arise through resting activation levels: common words are encountered more often, which raises their baseline activation in the network, so they win the parallel recognition competition faster. A sequential search model might predict faster access to common words if they're 'near the front,' but this is not how the lexicon works. The activation-competition architecture explains frequency effects, neighborhood effects, and priming within a single framework that sequential models cannot."

- question: "Why is word recognition better described as a 'flash auction' than a 'library lookup,' and what evidence supports the auction metaphor?"
  type: short-answer
  answer: "Library lookup implies a sequential, one-at-a-time search that stops when the right entry is found. Word recognition instead activates many candidates simultaneously — the mental lexicon broadcasts the perceptual input and all matching representations bid competitively. The winner is determined by resting activation (frequency), contextual priming, and perceptual match. Evidence includes: neighborhood effects (more competitors = slower win), ambiguous-word delays (two meanings both bid, context must adjudicate), and semantic priming (presenting 'doctor' raises 'nurse's' bid before any conscious search occurs)."
  explanation: "The auction metaphor captures the key features that sequential models miss: parallelism (multiple bids placed simultaneously), weighting (frequency and context adjust bid strength), and competition-resolution as a distinct stage. Poor readers may struggle not at the activation stage but at the resolution stage — multiple activated representations stay in play too long, slowing comprehension. This reframe has practical implications for reading instruction: helping struggling readers resolve lexical competition, not just recognize individual words, may be the relevant skill to target."
```

## Explainer

When you encounter the written word "bank," something remarkable happens in under 200 milliseconds: your brain simultaneously activates both the financial institution and the riverbank meaning, along with dozens of visually or phonologically similar words like "tank," "rank," and "blank." This is not a bug — it is the core architecture of **lexical access**, the process by which printed or spoken words contact their stored representations in long-term memory. Rather than searching sequentially through vocabulary, the cognitive system activates many candidates in parallel and rapidly narrows to the winner.

Your prerequisite work on language comprehension introduced the idea that meaning is not simply "looked up" but constructed. Word recognition is the first stage of that construction. The **mental lexicon** — your stored inventory of word knowledge — is not organized like a dictionary with alphabetical entries. It is a network in which words with similar sounds, spellings, or meanings are densely interconnected. When a word's perceptual input arrives, activation spreads outward through this network. This parallel activation accounts for **word frequency effects**: common words like "house" are recognized faster than rare words like "hovel" because their representations have higher resting activation from past exposure.

A closely related phenomenon is the **neighborhood effect**. A word's "neighborhood" consists of all words that differ from it by one letter substitution (e.g., "cat" → "bat," "hat," "mat," "cut"). Words with many neighbors can be slightly slower to recognize because more competitors are activated simultaneously. This is direct evidence that recognition is a competition among activated candidates, not a single-path lookup. The winning representation is determined by a combination of its resting activation (frequency), contextual priming from surrounding words and sentences, and the degree to which it matches the perceptual input.

The model that best captures this architecture is the **interactive activation model** and its descendants (such as the cohort model for spoken words). These models specify how bottom-up perceptual information activates candidates while top-down context simultaneously biases competition toward likely interpretations. The famous ambiguous-word studies — where eye tracking shows readers briefly considering the less appropriate meaning of a homonym like "bank" before context suppresses it — confirm that initial activation is promiscuous and context operates slightly after the fact. This has implications for reading skill: poor readers may struggle not at the activation stage but at the competition-resolution stage, where context must rapidly suppress irrelevant candidates.

Understanding lexical access reframes reading difficulties. A child who slowly reads "wind" (the noun vs. the verb) is not simply failing to "know" the word — they may be experiencing a bottleneck in the competition-resolution process, where two activated representations remain in play too long. Similarly, priming studies show that presenting "doctor" speeds recognition of "nurse" even without conscious awareness, because semantic activation spreads automatically through the lexical network before any deliberate comprehension occurs. Word recognition is less like finding a book in a library and more like a flash auction — multiple bids are placed instantly, and the highest contextually-weighted bidder wins.

