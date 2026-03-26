---
id: machine-learning-social-science
title: Machine Learning Applications in Social Science
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: computational-social-science-intro
  type: hard
- id: probability-and-statistics
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: optimization-multivariable-basics
  type: hard
- id: matrix-operations
  type: hard
- id: matrices-intro
  type: soft
- id: algorithm-complexity
  type: soft
- id: eigenvalues-and-eigenvectors
  type: soft
- id: linear-algebra-basics
  type: soft
- id: big-data-social-science
  type: soft
- id: text-analysis-social-science
  type: soft
- id: research-integrity-open-science-social
  type: soft
builds-toward:
- interpretable-machine-learning
- fairness-bias-ml
tags:
- machine-learning
- prediction
- algorithmic
- computational
stage: expert
status: validated
---
# Machine Learning Applications in Social Science

## Core Idea
Machine learning algorithms (classification, regression, clustering, dimensionality reduction) scale to large datasets and detect non-linear patterns. In social science, supervised methods predict outcomes (e.g., recidivism, protest participation); unsupervised methods find latent structure (e.g., ideological blocs, ethnic groupings). Challenges include interpretability (why did the algorithm decide?), fairness (does it discriminate?), and causality (prediction ≠ understanding mechanisms). ML is a tool for pattern discovery, not causal inference.

## Questions

```yaml
- question: "A criminal justice agency builds an ML model achieving 89% accuracy at predicting recidivism, using features including prior convictions, neighborhood, and race. A critic argues the model is problematic even given its accuracy. What is the most substantive articulation of this critique?"
  type: multiple-choice
  options:
    - "ML models are never accurate enough for high-stakes decisions — a 99% threshold should be required"
    - "The model encodes historical patterns of discriminatory policing and sentencing; deploying it for parole decisions embeds those patterns into future outcomes and perpetuates the discrimination"
    - "Parole decisions should always be made by human judges regardless of algorithmic accuracy"
    - "The model violates privacy by using demographic data in its predictions"
  answer: 1
  explanation: "The core issue is that ML models learn correlations from historical data. If race predicts recidivism in the training data, it is because of historical patterns of discriminatory policing and sentencing — not because race causes reoffending. A model trained on this data learns the historical discrimination. Deploying it for future decisions bakes those patterns into parole decisions, disproportionately penalizing groups that were already over-policed. High accuracy on historical data does not equal fairness or legitimacy for future decision-making."

- question: "A social scientist uses a gradient-boosted tree model to predict voter turnout with 91% accuracy and announces 'we now understand why people vote.' What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "91% accuracy is below the threshold required for scientific conclusions about social behavior"
    - "Gradient-boosted trees cannot be applied to binary outcomes like voting"
    - "High predictive accuracy demonstrates that the model identifies causes, not just correlates, of voting"
    - "Predictive accuracy means the model finds patterns that forecast outcomes — it says nothing about the causal mechanisms that produce those outcomes"
  answer: 3
  explanation: "Prediction and causal explanation are fundamentally different. A model may achieve high accuracy by exploiting proxies (neighborhood, income, age) that correlate with voting without identifying what causes any individual to vote or abstain. Correlation can arise from confounding, reverse causation, or historical patterns. Understanding 'why people vote' requires theoretical frameworks and causal inference methods (experiments, instrumental variables, regression discontinuity) — not predictive accuracy. ML tells you *where* patterns are; causal inference tells you *why*."

- question: "A machine learning model that achieves high overall accuracy on a prediction task can be assumed to be performing fairly across most demographic subgroups."
  type: true-false
  answer: false
  explanation: "High overall accuracy can mask systematically unequal error rates across subgroups. A recidivism prediction model might have 90% overall accuracy while having a much higher false positive rate for Black defendants than white defendants — incorrectly flagging innocent people as high-risk at disparate rates. Overall accuracy aggregates across all cases; fairness requires examining error rates by subgroup. Equal overall accuracy is compatible with deeply unequal false positive or false negative rates across demographic categories."

- question: "In social science, ML methods are most appropriately used for pattern discovery and generating hypotheses to investigate further, rather than as the final word on causal mechanisms."
  type: true-false
  answer: true
  explanation: "ML excels at finding non-linear patterns in large datasets — it can identify that certain configurations of variables predict an outcome in ways that no researcher thought to specify in advance. This makes it a powerful tool for hypothesis generation: 'this unexpected cluster of features predicts protest participation — why might that be?' But answering 'why' requires causal inference methods. ML's role is as a first-pass pattern detector that tells you where to direct causal investigation, not a replacement for theory and causal design."

- question: "A researcher builds an ML model using neighborhood characteristics to predict mortgage default with 90% accuracy. Why can't this model be taken as evidence that neighborhood characteristics *cause* mortgage default?"
  type: short-answer
  answer: "Because prediction and causal inference are different. The model learns correlations — it finds that certain neighborhood features co-occur with default. But correlation can arise from confounding variables (neighborhood is correlated with income, which causally affects ability to pay), historical discrimination built into the data (redlining produced the correlation), or reverse causation. The model cannot distinguish between 'living in this neighborhood causes default' and 'the factors that put people in this neighborhood also affect their ability to pay.' Establishing causation requires controlling for confounds through experimental or quasi-experimental design."
  explanation: "This is the central limitation of ML in social science: it is a pattern-detection engine, not a causal inference engine. A model can achieve high predictive accuracy by exploiting proxy variables that are correlated with outcomes without being on the causal path. Race, ZIP code, and neighborhood all predict many social outcomes — but they predict because of historical patterns of discrimination and structural inequality, not because they cause outcomes directly. Using predictive models for causal claims (or for policy intervention) requires confronting this distinction explicitly."
```

## Explainer

Your prerequisites in probability, linear algebra, and optimization are the machinery that machine learning runs on. A linear regression you already know minimizes squared prediction error by finding the weights for each feature. ML algorithms extend this logic aggressively: instead of a linear function, they can learn decision trees, neural networks, kernel functions — any structure that fits the training data well. The key idea that unifies them is **supervised learning**: you provide labeled examples (inputs paired with known outputs), and the algorithm learns a function that maps inputs to outputs well enough to generalize to new, unseen cases. Classification predicts discrete categories (will this person vote?); regression predicts continuous values (what wage will this worker earn?). Your matrix operations knowledge is directly relevant — most of these algorithms are best understood as operations on data matrices, where rows are observations and columns are features.

**Unsupervised learning** has no labels — the algorithm finds structure the analyst did not pre-specify. **Clustering** (k-means, hierarchical clustering) groups observations by similarity; it might reveal that survey respondents cluster into three ideological types you didn't know to look for. **Dimensionality reduction** (PCA, t-SNE) compresses many features into fewer dimensions — your eigenvalue/eigenvector background directly explains PCA: the first principal component is the eigenvector of the covariance matrix corresponding to the largest eigenvalue, capturing the direction of maximum variance. In social science, these tools are used to find latent structure in large corpora (text, social networks, behavioral data) that would be invisible to traditional variable-by-variable analysis.

The most important distinction in social science applications is **prediction versus causal inference**. ML excels at prediction: given a new person's characteristics, what is the probability they will be arrested again? But this says nothing about what *causes* recidivism. If the model learns that race predicts recidivism, it is capturing historical patterns of policing and sentencing, not any causal mechanism. Using an ML prediction for policy intervention — arresting people based on predicted risk — embeds those historical patterns in future decisions, a form of **algorithmic discrimination**. Your probability prerequisites help here: a model that is accurate on average (high overall accuracy) can still be systematically wrong for specific subgroups, violating fairness criteria like equal false positive rates across demographic groups.

**Interpretability** is the third challenge. Traditional regression gives you coefficients you can read as marginal effects. A deep neural network with millions of parameters gives you a prediction but no interpretable story about how it arrived there. This "black box" problem is a fundamental tension in social science: we want to understand *why* and *how*, not just predict. Modern interpretability methods (SHAP values, LIME, partial dependence plots) decompose predictions into feature contributions, but these are approximations — they describe the model's behavior, not the underlying social mechanism. ML's proper role in social science is pattern discovery and prediction at scale, not theory testing or causal explanation. Treat it as a powerful first-pass tool that can tell you *where* to look, but not *why* something is happening.
