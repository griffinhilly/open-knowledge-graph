---
id: text-classification
title: Text Classification
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: nlp-language-models
  type: hard
- id: supervised-learning-intro
  type: hard
builds-toward:
- sentiment-analysis-nlp
tags:
- text-classification
- document-classification
stage: advanced
status: validated
---

# Text Classification

## Core Idea
Text classification assigns documents to predefined categories (spam, sentiment, topic, intent). Approaches range from TF-IDF with logistic regression to RNNs and Transformers. Class imbalance, large vocabularies, and variable document lengths are common challenges. Transfer learning from pretrained language models (BERT, GPT) dramatically improves performance.

## Questions

```yaml
- question: "A fraud detection dataset contains 99.9% legitimate transactions and 0.1% fraudulent ones. A classifier that always predicts 'not fraud' achieves 99.9% accuracy. What does this reveal?"
  type: multiple-choice
  options:
    - "The model is performing well — 99.9% accuracy is excellent for any classification task"
    - "Accuracy is a misleading metric here; the model detects zero fraud while appearing to succeed"
    - "The dataset must be balanced to 50/50 before any classifier can be trained"
    - "This problem requires unsupervised learning because labeled fraud examples are too rare"
  answer: 1
  explanation: "This is the class imbalance problem. Overall accuracy is dominated by the majority class frequency, masking total failure on the class of interest. A model predicting the majority class always has recall of 0% for the minority class — the exact metric that matters for fraud detection. Precision, recall, and F1-score per class are the appropriate evaluation tools: they reveal whether the model actually learns to identify the rare class rather than simply predicting the majority. Evaluation metric selection determines whether you can tell if your model is working."

- question: "Why does fine-tuning a pretrained language model like BERT typically require far less labeled training data than training a classifier using TF-IDF features from scratch?"
  type: multiple-choice
  options:
    - "BERT compresses text more efficiently, so fewer examples are needed to fill its parameter space"
    - "BERT's pretraining has already learned rich language representations, so fine-tuning adapts existing knowledge rather than learning from zero"
    - "TF-IDF classifiers require more data because they use more model parameters"
    - "BERT processes examples more data-efficiently through its attention mechanism"
  answer: 1
  explanation: "Pretrained language models are trained on massive corpora to develop contextual representations of words, syntax, and semantics. This general language understanding is encoded in the model's weights before any task-specific data is seen. Fine-tuning adapts this existing knowledge to a specific classification task — the model already 'knows' what 'not good' means differently from 'good.' A TF-IDF + logistic regression system starts with zero language knowledge; every linguistic pattern must be learned from task-specific labeled examples. This is why thousands of fine-tuning examples can match what tens of thousands of examples achieve with classical methods."

- question: "Bag-of-words models discard word order entirely, yet they can still achieve reasonable performance on many text classification tasks such as spam detection and topic classification."
  type: true-false
  answer: true
  explanation: "For many coarse classification tasks, the presence or absence of specific words carries most of the signal regardless of order. 'Mortgage,' 'refinance,' and 'urgent' appearing in an email strongly suggests spam in any arrangement. Bag-of-words representations are therefore surprisingly effective for topic classification, language identification, and spam filtering. The limitation becomes critical for tasks where meaning depends on order — sentiment analysis, negation detection, or temporal reasoning — where 'not good' and 'good' are identical to a bag-of-words model but opposite in meaning."

- question: "Preprocessing steps like lowercasing and stop word removal usually improve text classification performance and should be applied universally."
  type: true-false
  answer: false
  explanation: "Preprocessing decisions are task-dependent and can help or hurt performance. Removing stop words may improve efficiency for topic classification (where function words carry little signal) but destroys meaning for tasks involving negation — 'not good' becomes 'good' if 'not' is removed. Lowercasing helps generalize ('Dog' and 'dog' are the same entity) but loses information where capitalization is meaningful (proper nouns, acronyms). Modern pretrained models often benefit from minimal preprocessing because they can learn which elements matter. 'Always improve' is false; always evaluate empirically."

- question: "Explain why overall accuracy is an insufficient evaluation metric for a text classifier trained on a severely imbalanced dataset, and what metrics should be used instead."
  type: short-answer
  answer: "When classes are imbalanced, a classifier can achieve high overall accuracy by always predicting the majority class while detecting zero examples of the minority class. Overall accuracy is dominated by majority class frequency and masks total failure on the class of interest. Per-class precision, recall, and F1-score are needed because they reveal whether the model actually learns to identify each class — especially the rare one that often carries the highest practical importance."
  explanation: "The stakes of missing the minority class frequently exceed the cost of majority-class errors: undetected fraud, undiagnosed disease, missed safety alerts. If recall for the minority class is 0%, the classifier is useless for its intended purpose despite high accuracy. F1-score balances precision (how often the model is right when it predicts positive) and recall (how often it catches actual positives). Reporting these per-class reveals the real picture. Additionally, metrics like the area under the precision-recall curve (PR-AUC) are often more informative than ROC-AUC for highly imbalanced problems."
```

## Explainer

Text classification is the task of assigning a document — an email, a tweet, a product review, a support ticket — to one or more predefined categories. You have already encountered supervised learning and language models as prerequisites, and text classification sits at their intersection: it applies supervised learning to text data, using the representations that language modeling provides. The fundamental challenge is that text is variable-length, unstructured, and high-dimensional. A vocabulary of 50,000 words means each document lives in a 50,000-dimensional space, most of which is zeros. The history of text classification is largely a story of finding better ways to represent documents as fixed-length numerical vectors that classifiers can consume.

The classical approach is **bag-of-words** with **TF-IDF** weighting. Each document becomes a vector of word frequencies, weighted so that common words like "the" count less and distinctive words like "mortgage" count more. A logistic regression or support vector machine trained on these vectors works surprisingly well for many tasks — spam detection, topic classification, language identification. The bag-of-words representation discards word order entirely ("dog bites man" and "man bites dog" are identical), yet for many classification tasks, the presence or absence of key words carries most of the signal. This is the same insight that makes naive Bayes effective: which words appear matters more than how they are arranged, at least for coarse categorization.

When word order and context matter — as in sentiment analysis, where "not good" means the opposite of "good" — sequential and contextual models take over. Recurrent neural networks process text word by word, maintaining a hidden state that accumulates context, and the final hidden state serves as a document representation for classification. Convolutional models slide filters over word sequences to capture local n-gram patterns. But the dominant modern approach is **transfer learning** from pretrained Transformer-based language models like BERT. These models are trained on massive text corpora to develop rich, contextual word representations, and they can be **fine-tuned** for classification by adding a simple classification layer on top. Fine-tuning adapts the general language understanding to your specific task with relatively little labeled data — a few thousand examples often suffice where bag-of-words methods might need tens of thousands.

Practical text classification involves several recurring challenges. **Class imbalance** is common: in fraud detection, 99.9% of transactions are legitimate, so a classifier that always predicts "not fraud" achieves 99.9% accuracy while being useless. Strategies include oversampling the minority class, undersampling the majority, or adjusting the loss function to penalize minority-class errors more heavily. **Preprocessing** decisions — lowercasing, stemming, removing stop words, handling out-of-vocabulary tokens — can significantly affect performance, especially for classical methods. And **evaluation** must go beyond accuracy: precision, recall, and F1-score per class reveal whether the model is actually learning the categories you care about, particularly the rare ones.
