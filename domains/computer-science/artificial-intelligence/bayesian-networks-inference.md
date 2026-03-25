---
id: bayesian-networks-inference
title: Bayesian Networks and Inference
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: bayes-theorem-and-inference
  type: hard
- id: conditional-probability
  type: hard
- id: bayes-theorem
  type: soft
- id: semantic-networks
  type: soft
tags:
- probabilistic-reasoning
- graphical-models
- inference
stage: advanced
status: validated
---
# Bayesian Networks and Inference

## Core Idea
Bayesian networks encode conditional independence as directed acyclic graphs, with nodes representing variables and edges indicating dependencies. Inference computes posterior probabilities of unknown variables given observations. Exact inference uses message passing; approximate methods use sampling.

## Questions

```yaml
- question: "A Bayesian network models 20 binary variables. How does the storage requirement of the network compare to storing the full joint probability distribution?"
  type: multiple-choice
  options:
    - "Both require the same storage, since they encode equivalent probabilistic information about the 20 variables"
    - "The full joint requires up to 2²⁰ entries; the network requires only the sum of CPT entries (one per variable per combination of parent states), typically orders of magnitude fewer"
    - "The Bayesian network requires more storage because it must also store the graph structure, edge weights, and metadata"
    - "Both require exactly 20 parameters, one marginal probability per variable"
  answer: 1
  explanation: "This is the core efficiency argument for Bayesian networks. A full joint distribution over 20 binary variables requires 2²⁰ ≈ 1 million entries. A Bayesian network exploits conditional independence: a variable with k parents requires only 2^k entries in its CPT, not 2^(number of all other variables). If most variables have few parents (sparse graph), the total CPT entries can be in the hundreds rather than millions. The savings become even more dramatic with more variables — a 50-variable full joint would need 2⁵⁰ entries, while a sparse network might need only a few thousand."

- question: "In a medical Bayesian network, you observe that a patient has both a cough and a fever. You want to compute P(Flu | Cough=true, Fever=true). What does exact inference require?"
  type: multiple-choice
  options:
    - "Simply reading the prior probability of flu from the Flu node's marginal distribution — observations don't change priors in a static network"
    - "Summing out all unobserved variables to obtain the posterior probability, weighting each configuration by its probability given the evidence"
    - "Multiplying all CPT entries together and normalizing — inference is a single multiplication step"
    - "Running Monte Carlo simulation, since exact computation is always intractable in any network with more than 10 nodes"
  answer: 1
  explanation: "Inference in a Bayesian network requires computing a conditional distribution, which means summing (marginalizing) over all possible states of unobserved variables. P(Flu | evidence) ∝ Σ_{hidden} P(Flu, hidden, evidence), where the sum is over all combinations of hidden variable values. For tree-structured networks this can be done efficiently via belief propagation in two passes; for general networks, algorithms like variable elimination do it systematically. The prior (option A) ignores the evidence entirely. Option D overstates the difficulty — exact inference is tractable for many practical network structures."

- question: "In a Bayesian network, a variable is conditionally independent of ALL other variables in the network once you observe its direct parent nodes."
  type: true-false
  answer: false
  explanation: "A variable is conditionally independent of its non-descendants given its parents — not of all other variables. Descendants can still carry evidence that propagates back up the network and affects probabilities. More subtly, observing a common child of two parent nodes creates a dependency between those parents that didn't exist before — the 'explaining away' effect. For example, if Flu and Allergies both cause Cough, and you observe Cough=true, Flu and Allergies become negatively correlated even though they were independent a priori. The correct independence structure is determined by d-separation rules, not simply 'observed parents block everything.'"

- question: "The efficiency of Bayesian networks comes from assuming that most variables are conditionally independent of most other variables given their parents, allowing the joint distribution to factor into a product of local conditional probability tables."
  type: true-false
  answer: true
  explanation: "This is exactly the key factorization: P(X₁, ..., Xₙ) = ∏ P(Xᵢ | parents(Xᵢ)). This works because each variable's CPT captures only the dependencies that actually exist. The number of parameters needed is the sum of CPT sizes, which is small when the graph is sparse (few parents per node). Crucially, the factorization is not an approximation — it is exact for any distribution that is consistent with the conditional independence assumptions encoded in the graph structure. Adding more edges (more dependencies) increases storage; removing unjustified independence assumptions makes the model less efficient but more accurate."

- question: "Observing evidence about one variable in a Bayesian network can change the probability of variables not directly connected to it in the graph. Explain why, using a concrete example."
  type: short-answer
  answer: "Evidence propagates through the network via shared connections. In a structure where Flu and Allergies both cause Cough (a common-cause structure), Flu and Allergies are marginally independent — knowing someone has flu tells you nothing about whether they have allergies. But if you observe Cough=true, the two causes become negatively correlated: learning the patient has allergies reduces the probability that flu explains their cough (explaining away). This dependency travels through the Cough node even though there is no direct edge between Flu and Allergies. More generally, evidence can propagate in any direction through the network — up to parents, down to descendants, or laterally through shared effects — governed by d-separation rules."
  explanation: "This is one of the most counterintuitive aspects of probabilistic graphical models. Dependencies are not just structural (from edges) but also evidential (from observations). Observing a node can 'activate' dependencies between its parents that were previously blocked, and can block dependencies between nodes that were previously connected. The d-separation framework formalizes exactly when observing a set of variables blocks or activates an information path between two other variables, allowing you to read off conditional independence relationships directly from the graph structure."
```

## Explainer

You already know Bayes' theorem: P(A|B) = P(B|A)P(A)/P(B). This works beautifully for updating a single hypothesis given evidence. But real-world reasoning involves many interrelated variables — a patient's symptoms, test results, medical history, and possible diseases all influence each other. Computing the full joint probability distribution over n binary variables requires 2ⁿ entries, which quickly becomes intractable. **Bayesian networks** solve this by exploiting the fact that most variables are conditionally independent of most other variables, dramatically reducing the number of parameters needed.

A Bayesian network is a **directed acyclic graph (DAG)** where each node represents a random variable and each directed edge represents a direct dependency. The key structural assumption is that each variable is conditionally independent of its non-descendants given its parents. This means that instead of storing the full joint distribution, you only need to store a **conditional probability table (CPT)** for each node given its parents. For example, in a medical diagnosis network, the node "Cough" might depend on "Flu" and "Lung Disease" but be conditionally independent of "Headache" once you know the state of those two diseases. The joint probability of all variables factors as: P(X₁, ..., Xₙ) = ∏ P(Xᵢ | parents(Xᵢ)), which is the chain rule of probability simplified by conditional independence.

**Inference** is the process of computing the posterior probability of some query variables given observed evidence. Suppose you observe that a patient has a cough and fever — what is the probability they have the flu? This requires summing over all possible states of the unobserved variables, weighted by their probabilities. For tree-structured networks, exact inference can be done efficiently using **message passing** (also called belief propagation): each node sends messages to its neighbors summarizing the evidence below it, and these messages propagate through the tree in two passes (leaves-to-root, then root-to-leaves). For more general networks, exact algorithms like **variable elimination** systematically sum out variables in an efficient order, and **junction tree** methods convert the network into a tree structure that supports exact message passing.

When the network is too large or densely connected for exact inference, **approximate methods** become necessary. The most common approach is **Monte Carlo sampling**: generate many random samples from the joint distribution, then estimate posterior probabilities by counting how often the query variables take particular values among samples consistent with the evidence. Variants like **likelihood weighting** and **Gibbs sampling** improve efficiency by focusing samples on configurations compatible with observed evidence rather than wasting samples on unlikely states. The power of Bayesian networks lies in making probabilistic reasoning tractable — they let you answer complex "what if" questions about systems with dozens or hundreds of interacting variables, from medical diagnosis to spam filtering to fault detection in industrial systems.
