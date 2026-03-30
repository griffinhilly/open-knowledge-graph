---
id: sample-complexity-bounds
title: Sample Complexity Bounds
domain: computer-science
course: machine-learning-theory
prerequisites:
- id: pac-learning-framework
  type: hard
- id: vc-dimension
  type: hard
- id: concentration-inequalities
  type: hard
tags:
- learning-theory
- sample-complexity
- upper-bounds
- lower-bounds
stage: expert
status: validated
---

# Sample Complexity Bounds

## Core Idea
Sample complexity bounds answer the most practical question in learning theory: how many training examples are necessary and sufficient to learn a concept class to a desired accuracy? Upper bounds show that m(epsilon, delta) samples suffice for any algorithm (typically ERM); lower bounds show that no algorithm can learn with fewer. For realizable PAC learning with VC dimension d, the sample complexity is Theta((d/epsilon) * log(1/epsilon) + (1/epsilon) * log(1/delta)). For agnostic learning, it is Theta(d/epsilon^2 + log(1/delta)/epsilon^2). These bounds bridge theory and practice by converting abstract complexity measures (VC dimension) into concrete data requirements.

## Questions

```yaml
- question: "A hypothesis class has VC dimension 20. You want to achieve epsilon = 0.01 error with delta = 0.05 confidence in the realizable setting. Approximately how many samples do you need?"
  type: multiple-choice
  options:
    - "About 2,000 samples — roughly d/epsilon"
    - "About 20,000 samples — roughly (d/epsilon) * log(1/epsilon) = (20/0.01) * log(100) ≈ 2000 * 4.6 ≈ 9,200, plus the (1/epsilon)*log(1/delta) ≈ 100 * 3 term"
    - "About 200,000 samples — roughly d/epsilon^2"
    - "About 200 samples — roughly d * log(1/epsilon)"
  answer: 1
  explanation: "In the realizable setting, sample complexity is O((d/epsilon) * log(1/epsilon) + (1/epsilon) * log(1/delta)). For d=20, epsilon=0.01, delta=0.05: the first term is (20/0.01) * log(100) ≈ 2000 * 4.6 = 9,200. The second term is (1/0.01) * log(20) ≈ 100 * 3 = 300. Total: approximately 9,500 samples. The d/epsilon * log(1/epsilon) term dominates for small epsilon. In the agnostic setting, this would be d/epsilon^2 = 20/0.0001 = 200,000 — an order of magnitude more, reflecting the price of agnosticism."

- question: "The sample complexity bound Theta(d/epsilon^2) for agnostic learning means that to halve the error, you need four times as many samples."
  type: true-false
  answer: true
  explanation: "If the sample complexity is proportional to d/epsilon^2, then reducing epsilon by half (from epsilon to epsilon/2) requires d/(epsilon/2)^2 = 4d/epsilon^2 samples — four times as many. This quadratic relationship means that achieving high accuracy is expensive: going from 10% error to 1% error requires 100 times more data. This is a fundamental property of estimation from noisy data — the 1/epsilon^2 scaling comes from the variance of statistical estimation and cannot be improved in the worst case. (In the realizable setting, the scaling is 1/epsilon, which is more forgiving — halving epsilon only doubles the sample requirement.)"

- question: "Sample complexity bounds depend only on the VC dimension and the accuracy parameters (epsilon, delta). They are independent of the data distribution."
  type: true-false
  answer: true
  explanation: "This is the distribution-free property inherited from the PAC framework. The sample complexity bound using VC dimension holds for any distribution D over the input space. The same number of samples suffices whether the data is uniformly distributed, concentrated on a few points, or arranged in any other way. This makes the bounds robust but potentially conservative — for specific 'easy' distributions, fewer samples might actually suffice. Distribution-dependent bounds (using Rademacher complexity or local Rademacher complexity) can be tighter for specific distributions but require knowledge of or assumptions about the distribution."

- question: "Explain the role of matching upper and lower bounds in establishing tight sample complexity characterizations, and why both are needed."
  type: short-answer
  answer: "An upper bound shows that some algorithm succeeds with at most m(epsilon, delta) samples — it is a sufficiency result. A lower bound shows that no algorithm can succeed with fewer than m'(epsilon, delta) samples — it is a necessity result. When the upper and lower bounds match (up to constant factors), the sample complexity is 'tight' or 'characterized': we know exactly how many samples are needed, not just an order of magnitude. Without a matching lower bound, an upper bound might be loose — a better algorithm could need fewer samples. Without a matching upper bound, a lower bound might not be achievable — the stated difficulty might be harder than what any algorithm can handle. For agnostic PAC learning with VC dimension d, the matching bounds Theta(d/epsilon^2) mean that the sample complexity is known exactly (up to constants): O(d/epsilon^2) samples suffice (proved via ERM + uniform convergence), and Omega(d/epsilon^2) are necessary (proved via information-theoretic arguments). No improvement is possible."
  explanation: "Matching bounds are the strongest form of theoretical result in learning theory. They close a problem completely — no further research on the sample complexity of that setting can improve the bounds. This is why establishing tight bounds, rather than just upper bounds, is highly valued."
```

## Explainer

Sample complexity bounds are where learning theory meets practice most directly. They answer the question every practitioner implicitly asks: "how much data do I need?" While the bounds are worst-case and often conservative, they provide the correct scaling relationships — how data requirements grow with model complexity, desired accuracy, and confidence level.

The realizable case (where the target function is in the hypothesis class) gives the cleanest bounds. The upper bound, proved via uniform convergence, states that m = O((d/epsilon) * log(1/epsilon) + (1/epsilon) * log(1/delta)) samples suffice, where d is the VC dimension. The matching lower bound, proved via information-theoretic arguments, shows that Omega(d/epsilon + log(1/delta)/epsilon) samples are necessary. These match up to the log(1/epsilon) factor, which is known to be tight. The key insight is the linear dependence on d — each additional unit of VC dimension adds a proportional amount to the data requirement.

The agnostic case (where the best hypothesis in the class may have nonzero error) has tighter matching bounds: Theta(d/epsilon^2 + log(1/delta)/epsilon^2). The extra factor of 1/epsilon compared to the realizable case reflects the statistical cost of estimating error rates rather than detecting the absence of errors. This quadratic dependence on 1/epsilon has significant practical implications: achieving 1% error requires 100 times more data than achieving 10% error, and achieving 0.1% error requires 10,000 times more than 10%. The implication is clear — pushing accuracy to very low levels requires enormous datasets or strong inductive biases.

Beyond the basic PAC bounds, sample complexity theory has been refined for specific hypothesis classes and learning settings. For linear classifiers in d dimensions (VC dimension d+1), the bound is Theta(d/epsilon^2). For kernel methods with margin gamma, the effective dimension is R^2/gamma^2 (where R is the data radius), which can be much smaller than the ambient dimension. For deep networks, the sample complexity is less well-characterized — it depends on the complexity measure used (spectral norms, PAC-Bayes, compression) and the resulting bounds are often loose. The general principle remains: sample complexity is proportional to the effective complexity of the hypothesis class (however measured) and inversely proportional to the square of the desired accuracy. This principle guides decisions about model selection, data collection, and the feasibility of learning tasks.
