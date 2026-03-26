---
id: sequence-labeling
title: Sequence Labeling and CRFs
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: named-entity-recognition
  type: soft
- id: hidden-markov-models
  type: hard
tags:
- sequence-labeling
- crf
- structured
stage: advanced
status: validated
---

# Sequence Labeling and CRFs

## Core Idea
Sequence labeling assigns labels to each element in a sequence (part-of-speech tagging, named entity recognition). Conditional Random Fields (CRFs) model label dependencies, capturing that consecutive labels influence each other. As discriminative models, CRFs typically outperform generative HMMs for sequence labeling tasks.

## Questions

```yaml
- question: "An HMM and a CRF are trained on the same part-of-speech tagging dataset. The CRF achieves significantly higher accuracy. What is the most likely reason?"
  type: multiple-choice
  options:
    - "The CRF uses a more powerful inference algorithm than Viterbi, finding globally optimal label sequences that HMMs cannot"
    - "The CRF can incorporate arbitrary features of the input — capitalization, word suffixes, neighboring words — without the HMM's independence constraint that observation probability depends only on the current tag"
    - "The CRF captures longer-range label-to-label dependencies, whereas HMMs only model adjacent tag pairs"
    - "The CRF uses a larger tag vocabulary, distinguishing more fine-grained parts of speech"
  answer: 1
  explanation: "The CRF's key advantage is discriminative modeling: it learns P(tags|words) directly, allowing feature functions that examine any part of the input sequence. An HMM must model P(words, tags) jointly, which means the probability of each word must be modeled given only its tag — it cannot easily use features like 'ends in -ing' or 'the previous word is a determiner' without dramatically expanding the state space. Both models use Viterbi for inference and both model adjacent-tag dependencies; the feature richness is the decisive difference."

- question: "A student argues that CRFs outperform HMMs because CRFs model dependencies between consecutive labels, whereas HMMs treat each label independently. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "The student is correct — HMMs assume all labels are independent and cannot model transitions"
    - "HMMs also model label-to-label dependencies through transition probabilities; the actual CRF advantage is discriminative modeling that allows arbitrary input features without requiring a generative model of observations"
    - "CRFs cannot model label dependencies — they score each label position independently and then pick the best combination"
    - "Both models are equivalent in practice; performance differences come only from training data size"
  answer: 1
  explanation: "HMMs explicitly model P(tag_t | tag_{t-1}) as transition probabilities — label dependencies are central to HMM design. CRFs also capture label-to-label interactions through pairwise feature functions on adjacent labels. The real difference is the generative vs. discriminative distinction: HMMs model how observations are generated (P(word|tag)), forcing a strong independence assumption; CRFs model the conditional distribution directly (P(tags|words)), freeing them to use any observable feature of the input sequence."

- question: "Both Hidden Markov Models and linear-chain CRFs use the Viterbi algorithm to find the most probable label sequence at inference time."
  type: true-false
  answer: true
  explanation: "The Viterbi algorithm is a dynamic programming approach that efficiently finds the most probable path through a sequence of states or labels — it applies to any model where the score of a label sequence decomposes into local scores at each position and at each adjacent pair. Both HMMs and linear-chain CRFs have this factorization structure, so Viterbi works for both. The partition function (for training) is computed with the forward algorithm in both cases. The algorithms are shared; the difference is what is being computed — joint probability in HMMs, conditional probability in CRFs."

- question: "A CRF's main advantage over an HMM is that it captures label-to-label dependencies that HMMs fundamentally can rarely model."
  type: true-false
  answer: false
  explanation: "HMMs do model label dependencies — they are the core of the HMM design, encoded as transition probabilities P(tag_t | tag_{t-1}). The CRF's actual advantage is discriminative modeling: it directly models P(labels|observations) without requiring a generative story for how observations arise. This allows arbitrary feature functions on the input, such as 'does the current word end in -tion?' or 'is the next word capitalized?' — features that would be awkward or impossible for an HMM to use without expanding its state space enormously."

- question: "Explain why a CRF can incorporate features like 'the word ends in -ing' or 'the previous word is a title' more effectively than an HMM, even though both models capture dependencies between adjacent labels."
  type: short-answer
  answer: "An HMM models the joint probability P(words, tags) by factoring it into emission probabilities P(word|tag) and transition probabilities P(tag|prev_tag). To use a feature like 'ends in -ing', the HMM must model the probability of observing a word ending in -ing given a particular tag — it must generate the feature, treating it as part of the observation model. This requires estimating many parameters and assumes the feature's distribution is independent of other features given the tag. A CRF models P(tags|words) directly, so features can be arbitrary functions of the entire observation sequence — it doesn't need to model how features are generated, only how they correlate with labels. This makes CRFs naturally suited to rich, overlapping feature sets."
  explanation: "The generative vs. discriminative distinction is fundamental: generative models (HMMs) must model the full data distribution P(x,y), which constrains what they can condition on. Discriminative models (CRFs) only model P(y|x), which means any observable property of x can be a feature for free. This is why feature engineering dominated NLP before deep learning: CRFs could absorb any handcrafted feature, while HMMs struggled with feature-rich inputs."
```

## Explainer

From your study of Hidden Markov Models, you understand the basic structure of sequence labeling: given a sequence of observations (words in a sentence, characters in a string, signals in a time series), assign a label to each position. In part-of-speech tagging, the input "The cat sat" gets labels [DET, NOUN, VERB]. In named entity recognition, "Barack Obama visited Paris" might get [B-PER, I-PER, O, B-LOC]. The challenge is that labels are not independent — knowing the current word is tagged as a determiner makes it much more likely that the next word is a noun.

HMMs handle these dependencies by modeling the joint probability P(observations, labels) as a product of emission probabilities (how likely is this word given this tag?) and transition probabilities (how likely is this tag given the previous tag?). But HMMs make a strong independence assumption: the probability of observing a word depends *only* on its tag, not on the surrounding words or any other features. This means an HMM cannot easily use rich features like "the word ends in -ing" or "the previous word is capitalized" without dramatically expanding the state space.

**Conditional Random Fields (CRFs)** solve this by modeling the conditional probability P(labels | observations) directly, without modeling how observations are generated. This discriminative approach means CRFs can incorporate arbitrary **feature functions** that examine any part of the input sequence — the current word, neighboring words, capitalization patterns, suffixes, prefixes — without worrying about their joint distribution. A linear-chain CRF defines a score for each label sequence as a weighted sum of feature functions evaluated at each position and each pair of adjacent labels, then normalizes over all possible label sequences to produce a valid probability distribution.

Training a CRF means finding feature weights that maximize the conditional likelihood of the correct label sequences in the training data. Inference — finding the most probable label sequence for a new input — uses the **Viterbi algorithm**, the same dynamic programming approach you learned for HMMs. The partition function (normalizing constant) is computed with the **forward algorithm**, again borrowed from HMMs. The algorithmic machinery is familiar; the difference is entirely in what is being modeled. Because CRFs are discriminative and feature-rich, they consistently outperform HMMs on tasks like POS tagging and NER. Modern systems often combine a neural network (BiLSTM or Transformer) to produce contextualized features with a CRF layer on top to enforce label consistency — getting the best of learned representations and structured prediction.
