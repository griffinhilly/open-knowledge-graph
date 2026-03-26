---
id: prediction-in-language-processing
title: Prediction in Language Processing
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: working-memory-sentence-comprehension
  type: hard
tags:
- psycholinguistics
- prediction
- comprehension
stage: expert
status: validated
---

# Prediction in Language Processing

## Core Idea
Language comprehension is actively predictive: comprehenders anticipate upcoming content based on semantic and syntactic constraints. When reading 'The detective examined the evidence,' readers predictively activate typical continuations. Eye-tracking and neuroimaging show that failed predictions ('The detective examined the... potatoes') cause processing difficulty, demonstrating that comprehension proceeds through prediction and confirmation, not purely reactive analysis.

## Questions

```yaml
- question: "In a visual world eye-tracking experiment, participants look at a display of objects while hearing 'Pick up the can...' Their eyes move toward the candle before the word is completed. What does this demonstrate?"
  type: multiple-choice
  options:
    - "Comprehension is sequential — listeners wait for full words before processing meaning"
    - "Prediction operates on partial phonological input, activating candidates before a word is identified"
    - "Listeners guess randomly based on visual salience, not linguistic prediction"
    - "The brain processes syntax before semantics in online comprehension"
  answer: 1
  explanation: "Anticipatory eye movements to phonologically consistent objects before a word is completed demonstrate that the comprehension system activates multiple candidates based on partial input — not just after word recognition is complete. This is a signature of predictive processing: the system is running ahead of the input, committing to likely interpretations before they are confirmed. Option A describes a sequential bottom-up model inconsistent with this finding."

- question: "A perfectly grammatical sentence ends with a semantically unexpected word ('The detective examined the potatoes'). The N400 amplitude for 'potatoes' is larger than for 'evidence'. What does this pattern reveal?"
  type: multiple-choice
  options:
    - "The brain flags 'potatoes' as ungrammatical and generates an error signal"
    - "The brain had pre-activated semantically likely continuations; the unexpected word requires revising a prior prediction"
    - "The N400 reflects the number of syllables in a word, which is greater for 'potatoes'"
    - "The finding shows that syntactic and semantic processing are completely independent"
  answer: 1
  explanation: "The sentence is grammatically correct, so the N400 cannot be a grammaticality signal. The N400 scales with the violation of semantic expectation — the degree to which the word conflicts with what was pre-activated. The brain already committed to likely continuations (evidence, witness, clues) before 'potatoes' arrived. The large N400 reflects the cost of updating a prior prediction. This is the key evidence that comprehension involves continuous prediction, not reactive word-by-word analysis."

- question: "The N400 is an most-or-very little signal that fires primarily when a word is semantically anomalous or ungrammatical."
  type: true-false
  answer: false
  explanation: "The N400 is a graded signal, not binary. Its amplitude is inversely proportional to the predictability of a word in context — even highly predictable, perfectly acceptable words produce a smaller N400 than moderately unexpected but acceptable words. This grading shows that the brain is continuously tracking probability distributions over upcoming words, not just detecting errors. If it were binary, all acceptable words would produce no N400 at all."

- question: "Language comprehension involves active prediction: the brain pre-activates likely upcoming words based on syntactic, semantic, and discourse constraints before those words arrive."
  type: true-false
  answer: true
  explanation: "This is the central claim of the predictive processing account of language comprehension, supported by N400 amplitude patterns, visual world eye-tracking, and reading time data. The evidence consistently shows that unexpected words — even when grammatical — cost extra processing time and produce larger neural responses, demonstrating that predictions were made and must be revised. Comprehension is not merely reactive integration of each word as it arrives."

- question: "How does the N400 EEG component provide evidence that language comprehension is predictive rather than purely reactive? What specific feature of the N400 response is key?"
  type: short-answer
  answer: "The N400 amplitude is inversely graded by how predictable a word is in context — not just whether the word is semantically anomalous. Highly predictable words produce smaller N400s; moderately unexpected but acceptable words produce larger ones. If comprehension were purely reactive, all acceptable words should produce the same response. The grading shows the brain pre-activates candidates and shows less neural effort when predictions are confirmed, more when they must be revised."
  explanation: "The graded nature of the N400 is what distinguishes prediction from mere anomaly detection. An anomaly detector would fire only for violations; a predictor generates a continuous probability distribution and signals surprise proportional to how unexpected the input was. The N400's gradient across a range of predictability values is direct evidence for the latter model."
```

## Explainer

From your study of working memory and sentence comprehension, you know that processing language in real time requires holding incomplete structures in memory while integrating new words. Prediction in language processing builds directly on this: rather than passively holding open slots until they are filled, the comprehension system actively generates expectations about what will come next. Comprehension, on this view, is not a purely bottom-up process (reading each word and integrating it) but a **predictive coding** process in which incoming input is checked against prior expectations.

The evidence for prediction comes from several converging paradigms. In **eye-tracking during reading**, readers slow down at unexpected words — the "garden path" effect you may already know — but prediction goes beyond structural garden paths. Even when syntax is unambiguous, words that are semantically unexpected ("The detective examined the potatoes") produce longer fixation times than semantically expected continuations ("The detective examined the evidence"). This happens even though both sentences are perfectly grammatical. The processing cost reflects the effort of revising a prediction that had already been committed to. In **visual world eye-tracking** (where participants look at pictures while hearing speech), listeners move their eyes to the likely referent before the word naming it is complete — demonstrating that prediction is operating on partial phonological input, not just after words are recognized.

The **N400** effect in EEG is perhaps the most direct neural signature of prediction. The N400 is a negative deflection in the EEG signal occurring roughly 400ms after an unexpected word; it scales with how semantically anomalous the word is in context. Crucially, the N400 is not just a "surprise" signal — its amplitude is reduced when a word is *more predictable* than average, even for words that are perfectly acceptable. This means the brain is not simply processing unexpected items harder; it is continuously generating predictions and showing reduced effort when those predictions are confirmed. The signal is graded, not binary.

What drives prediction? Both **syntactic constraints** and **semantic/pragmatic knowledge** contribute. Syntactic structure creates strong predictions: after "The girl was chased by the," a noun phrase is predicted, and a transitive agent is likely. World knowledge contributes independently: after "The detective examined the," *clues*, *evidence*, and *witness* are highly activated regardless of syntactic structure. Context at the discourse level modulates both: a story about cooking will raise the probability of food-related words throughout, even in semantically neutral sentence frames. The comprehension system integrates all available constraints simultaneously, which is why prediction feels effortless — it is the normal mode of operation, not an occasional strategy.

The theoretical implication is significant: comprehension and production share more machinery than a purely modular view would predict. To predict the next word, the comprehension system must be running something like a production simulation — activating words based on what would be contextually appropriate to say. This convergence of comprehension and production processes, mediated by prediction, is one of the most active research frontiers in psycholinguistics.
