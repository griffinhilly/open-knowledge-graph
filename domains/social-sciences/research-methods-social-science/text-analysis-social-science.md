---
id: text-analysis-social-science
title: Computational Text Analysis for Social Data
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: content-analysis-systematic
  type: hard
- id: computational-social-science-intro
  type: soft
builds-toward:
- topic-modeling-lda
- sentiment-analysis-methods
tags:
- text
- nlp
- computational
- qualitative-quantitative
stage: advanced
status: draft
---

# Computational Text Analysis for Social Data

## Core Idea
Computational text analysis uses algorithms to extract patterns, themes, and meanings from large text corpora—news articles, social media, interviews, historical documents. Methods range from counting word frequencies and calculating sentiment to unsupervised topic modeling and supervised classification. These techniques bridge qualitative and quantitative approaches, enabling systematic analysis of textual data at scales humans cannot manually process.

## Questions

```yaml
- question: "A researcher completes a study using LDA topic modeling on 10 years of congressional speeches and reports: 'The algorithm identified 8 distinct political themes organizing the corpus.' What is the most critical missing element in this claim?"
  type: multiple-choice
  options:
    - "The software package and computational resources used to run the model"
    - "The number of documents and average document length in the corpus"
    - "The researcher's substantive interpretation of what the statistical word clusters actually mean — the algorithm produces patterns, not meaning"
    - "Validation metrics showing the statistical fit of the model to the data"
  answer: 2
  explanation: "LDA produces statistical clusters of co-occurring words — it identifies patterns in which words appear together across documents. What those patterns mean substantively requires the researcher to interpret the word lists using domain knowledge. The algorithm cannot identify 'political themes'; it identifies word co-occurrence patterns. Presenting the output as directly meaningful without documenting the interpretive step misrepresents how the method works, makes the analysis unreproducible, and conflates statistical pattern-finding with substantive understanding."

- question: "A researcher uses a validated dictionary of economic anxiety terms to measure that concept across 50,000 news articles. What is the most fundamental assumption this method requires?"
  type: multiple-choice
  options:
    - "That the articles represent a representative sample of media coverage during the study period"
    - "That economic anxiety appears in text in ways that prior theory can specify — that the dictionary words reliably indicate the concept across diverse linguistic contexts in the corpus"
    - "That the dictionary was developed on a corpus similar to the one being analyzed"
    - "That the researcher has manually read at least a sample of the articles to validate the results"
  answer: 1
  explanation: "Dictionary methods work by counting how often words associated with a concept appear. This assumes that the concept manifests in language in predictable, theory-specified ways that the dictionary captures. If economic anxiety is sometimes expressed through understatement, irony, or the absence of certain words, the dictionary will miss it. If dictionary words appear in contexts where the concept isn't meant (e.g., academic discussions of economic anxiety), it will overcount. This assumption — confident prior theory about how the concept appears linguistically — is substantial and must be validated, not assumed."

- question: "In supervised text classification, biases that researchers introduce during the hand-labeling stage can propagate systematically into the trained model's classifications across the full corpus."
  type: true-false
  answer: true
  explanation: "Supervised classification works by learning patterns from hand-labeled examples and applying those learned patterns to new documents. If human coders systematically label certain types of documents in ways that reflect their biases — coding ambiguous cases in one direction, applying different standards across demographic groups, or operationalizing concepts inconsistently — the trained model learns and amplifies those patterns. The model scales human judgment, including human error, which is why strong inter-coder reliability, transparent documentation of coding rules, and validation on held-out data are essential safeguards."

- question: "Bag-of-words models are called 'bag-of-words' because they capture words along with their grammatical and sequential context within sentences."
  type: true-false
  answer: false
  explanation: "Bag-of-words models treat documents as unordered collections of word tokens — sequence and grammar are discarded. 'Bag' is the key metaphor: just as items in a bag have no inherent order, words in a bag-of-words model are simply counted, not sequenced. This means 'the bank repossessed the house' and 'the house repossessed the bank' have identical representations. This is a significant limitation for capturing meaning that depends on word order, negation, or syntax — though for many research purposes (broad thematic analysis, topic modeling), the loss of sequence is an acceptable tradeoff for scalability."

- question: "Why does having a larger corpus not automatically solve validity problems in computational text analysis?"
  type: short-answer
  answer: "Scale amplifies whatever patterns the method is measuring — if the method is measuring the wrong thing, more data produces more precise measurements of the wrong thing. A dictionary method that miscategorizes a concept will misclassify millions of articles at scale. A supervised classifier trained on flawed labels will propagate those flaws across millions of documents. Validity — whether the method captures the construct of interest — is a conceptual and design problem that must be solved through careful operationalization and validation, not through additional data."
  explanation: "This is the fundamental distinction between reliability (consistent results) and validity (measuring what you intend). Computational methods are often highly reliable — they produce the same output from the same input — but reliability does not guarantee validity. Big data can produce reliably wrong answers at impressive scale. The solution is validation: reading samples of documents, checking whether model outputs correspond to human judgment, testing on cases where the correct answer is known, and documenting assumptions transparently so others can evaluate whether the method actually captures the intended concept."
```

## Explainer

You already know how to conduct content analysis: define categories, systematically code text, and report frequencies and patterns. Computational text analysis scales this process from hundreds of documents to millions, automating what human coders would take years to accomplish. The intellectual shift is not just about scale — it also changes which research questions become tractable.

The simplest computational approaches count words. **Bag-of-words** models treat a document as an unordered collection of tokens — word frequencies and co-occurrence patterns become the data, with grammar and sequence discarded. From your content analysis background, this resembles manifest coding without context. More useful are **dictionary methods**: you build or borrow a validated list of words associated with a concept (economic anxiety, democratic legitimacy, moral outrage) and measure how frequently those words appear across documents. Widely used examples include LIWC and Moral Foundations dictionaries. Dictionary methods are transparent and replicable but require confident prior theory about how the concept appears in language — a substantial assumption.

**Unsupervised methods** like Latent Dirichlet Allocation (LDA) **topic modeling** ask what themes organize a corpus without the researcher specifying them in advance. LDA treats each document as a mixture of topics and each topic as a probability distribution over words. The output is a set of word clusters that typically cohere around interpretable themes — "economy, jobs, wages, growth" cluster together because they appear in similar documents. The skill is interpreting what those statistical clusters mean substantively, which requires deep domain knowledge. The algorithm finds patterns; the researcher supplies meaning.

**Supervised classification** works differently: you hand-label a sample of documents (positive/negative sentiment, protest/non-protest, policy/non-policy), train a statistical model on those labels, and apply the trained model to classify the remaining corpus. This approach leverages human judgment at the labeling stage and scales it computationally. The danger is that the model learns whatever pattern the coders introduced — including their biases. Validation, transparent documentation of training data, and strong inter-coder reliability in the labeled sample are essential safeguards. Across all methods, computational text analysis is most powerful when it enables comparisons that humans genuinely cannot make manually: tracking how a political frame evolves across a decade of congressional speeches, mapping sentiment across millions of social media posts in real time, or detecting subtle differences in how rival news outlets cover the same event.
