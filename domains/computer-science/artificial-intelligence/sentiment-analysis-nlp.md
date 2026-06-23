---
id: sentiment-analysis-nlp
title: Sentiment Analysis in NLP
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: nlp-language-models
  type: hard
- id: neural-networks-intro
  type: hard
- id: word-embeddings
  type: soft
- id: text-classification
  type: soft
tags:
- nlp
- text-classification
- sentiment
- opinion-mining
stage: expert
status: validated
---

# Sentiment Analysis in NLP

## Core Idea
Sentiment analysis classifies text as positive, negative, or neutral by learning associations between words/phrases and sentiment labels. Approaches range from bag-of-words with linear classifiers to RNNs and transformers that capture context and word interactions; aspect-based sentiment analysis distinguishes opinions about different entities or aspects within text.

## How It's Best Learned
Train sentiment classifiers using different approaches (Naive Bayes, logistic regression, LSTM, transformer) and compare their ability to handle negation, sarcasm, and domain-specific language.

## Questions

```yaml
- question: "A bag-of-words sentiment classifier trained on product reviews is given the sentence: 'I wouldn't say this is anything less than remarkable.' It predicts negative sentiment. What explains this error?"
  type: multiple-choice
  options:
    - "The training data lacked enough examples of double negations for the model to learn them"
    - "Bag-of-words discards word order, so 'wouldn't' and 'less' register as negative signals without any representation of how they combine to negate each other"
    - "The word 'remarkable' was not in the training vocabulary, so the model defaulted to negative"
    - "The sentence is genuinely ambiguous and the classifier correctly flagged uncertainty as negative"
  answer: 1
  explanation: "The sentence means 'this is remarkable' — two negations ('wouldn't say... less than') produce a positive sentiment. A bag-of-words model sees features like 'wouldn't' and 'less' (which carry negative signal in training data) and 'remarkable' (positive), but with no information about order or structure, it cannot compute how 'wouldn't... less than' inverts the word 'remarkable.' This is not a data problem; it is a fundamental limitation of ignoring word order. Sequential or attention-based models learn that negation words modify what follows them."

- question: "A restaurant review reads: 'The pasta was divine, but the 45-minute wait and rude server ruined the evening.' A single-score document-level classifier assigns it 0.55 (mildly positive). What does this reveal about the classifier's limitation?"
  type: multiple-choice
  options:
    - "The classifier needs more training data, since mildly positive is clearly wrong for this review"
    - "Single-score classification cannot distinguish that food sentiment and service sentiment are different aspects requiring separate targets — a task requiring aspect-based sentiment analysis"
    - "Transformer-based models would also fail on this sentence because of the contrastive conjunction 'but'"
    - "The classifier is interpreting the review correctly; 'divine pasta' outweighs the service complaints"
  answer: 1
  explanation: "The review expresses strongly positive sentiment about the food and strongly negative sentiment about the service. A single document-level score collapses these into one number, losing the critical distinction. Aspect-based sentiment analysis (ABSA) identifies target entities (pasta, wait time, server) and assigns separate sentiment labels to each. This is not a training-data problem — it is a structural limitation of document-level models that output one label per text."

- question: "Transformer-based sentiment models outperform bag-of-words models on sentences with negation because attention mechanisms allow them to learn how words modify each other's meaning within a sentence."
  type: true-false
  answer: true
  explanation: "Transformers process all words simultaneously and learn attention weights that capture relationships between tokens. In 'not good,' the attention mechanism learns that 'not' is closely related to 'good' and modifies its representation. The model can learn that 'not + [positive word]' maps to negative sentiment. Bag-of-words models cannot represent this relationship because they treat each word as an independent feature, discarding all positional and structural information."

- question: "A bag-of-words model that correctly identifies strong sentiment-bearing words ('excellent,' 'awful') will reliably classify sentences containing those words, because individual word polarity is the primary determinant of sentence sentiment."
  type: true-false
  answer: false
  explanation: "Sentence sentiment depends on the compositional structure of the sentence, not just the polarity of individual words. Negation ('not awful' = positive), irony ('what an excellent idea' said sarcastically), qualification ('it was somewhat excellent but mostly mediocre'), and aspect targeting all change how individual word polarity contributes to sentence-level sentiment. Bag-of-words models succeed in simple cases but systematically fail wherever context determines how words modify each other — which is common in real language use."

- question: "Why do bag-of-words models fail on negated phrases like 'not bad,' and what property of LSTM or transformer architectures allows them to handle negation correctly?"
  type: short-answer
  answer: "Bag-of-words models discard word order, representing 'not bad' and 'bad' with nearly identical feature vectors — both contain the feature 'bad' as a negative signal. The model cannot represent the semantic effect of 'not' reversing 'bad.' LSTMs process the sequence left to right, updating a hidden state as each word is read; the LSTM gate mechanism learns to modify the representation when a negation word like 'not' is encountered, so the subsequent word 'bad' is interpreted in a negated context. Transformers use bidirectional attention, learning that in 'not bad,' 'bad' attends strongly to 'not' and should have its sentiment flipped. Both architectures can represent the compositional structure that gives negation its semantic force."
  explanation: "The core issue is that meaning in language is compositional — the meaning of a phrase is a function of the meanings of its parts AND how they are structurally combined. Bag-of-words captures the parts but ignores the structure; sequential and attention-based models capture both."
```

## Explainer

**Sentiment analysis** is the task of automatically determining whether a piece of text expresses a positive, negative, or neutral opinion. It is one of the most intuitive NLP applications because it maps directly to something humans do constantly — reading a product review and deciding whether the reviewer liked the product. Building on your understanding of language models, neural networks, and word embeddings, sentiment analysis shows how these tools combine to solve a concrete text classification problem.

The simplest approach treats text as a **bag of words**: ignore word order, count how often each word appears, and feed those counts into a classifier like logistic regression or Naive Bayes. This works surprisingly well for many cases because sentiment-bearing words ("excellent," "terrible," "disappointing") are strong signals on their own. But bag-of-words models fail on constructions where context matters. "Not bad" is positive despite containing "bad." "I expected it to be great but it wasn't" is negative despite containing "great" and "expected." These failures reveal why sequential and contextual models are needed.

Neural approaches address these limitations by preserving word order and learning contextual representations. Word embeddings give each word a dense vector capturing semantic similarity, so the model knows that "fantastic" and "excellent" are related even without seeing both in training data. RNNs and LSTMs process the sentence sequentially, building up a representation that captures how words modify each other — so the negation in "not good" flips the sentiment of "good." Transformer-based models like BERT go further, using bidirectional attention to understand that in "The food was great but the service was awful," the sentiment toward food and service are different and both must be captured.

This last observation leads to **aspect-based sentiment analysis**, which goes beyond assigning a single label to an entire text. A restaurant review might be positive about food but negative about wait times. Aspect-based systems identify the **target entities** (food, service, ambiance) and assign separate sentiment labels to each. This requires the model to associate opinion words with their targets, a harder problem that leverages the full power of contextual language models. Whether you are building a simple review classifier or a fine-grained opinion mining system, the progression from bag-of-words to contextual models illustrates a recurring theme in NLP: capturing more context almost always improves performance, at the cost of more data and computation.
