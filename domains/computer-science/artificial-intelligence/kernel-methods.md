---
id: kernel-methods
title: Kernel Methods and the Kernel Trick
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: support-vector-machines
  type: hard
- id: inner-product-spaces
  type: soft
- id: function-composition-and-inverses
  type: soft
- id: dot-product
  type: soft
builds-toward:
  - kernel-ridge-regression
tags:
- kernel
- kernel-trick
- implicit-mapping
stage: advanced
status: draft
---
# Kernel Methods and the Kernel Trick

## Core Idea
The kernel trick enables non-linear learning in linear algorithms by implicitly mapping data to high-dimensional spaces without explicit computation. A kernel function k(x, y) computes dot products in the mapped space. Common kernels include RBF (Gaussian), polynomial, and sigmoid. This makes SVMs and ridge regression applicable to non-linear problems efficiently.

## Explainer

From your work with support vector machines, you know that SVMs find a hyperplane that maximally separates two classes. This works beautifully when the data is linearly separable — but what happens when the decision boundary between classes is curved? Imagine two concentric rings of data points, one class inside the other. No straight line can separate them. The intuition behind kernel methods is that if you lift the data into a higher-dimensional space, the curved boundary in the original space can become a flat hyperplane in the new one.

The mathematical foundation connects directly to dot products and inner product spaces. Recall that the SVM optimization problem depends entirely on dot products between data points — you never need the raw coordinates, only how points relate to each other through their inner products. A **kernel function** k(x, y) computes what the dot product *would be* if you mapped x and y into a higher-dimensional space, without ever performing that mapping explicitly. This is the **kernel trick**: you replace every dot product in the SVM formulation with a kernel evaluation, and the algorithm behaves as though it is operating in the high-dimensional space while doing all its computation in the original space.

Consider a concrete example. Suppose your data lives in two dimensions, and you define a mapping φ that sends each point (a, b) to the six-dimensional space (a², b², √2·ab, √2·a, √2·b, 1). Computing φ(x)·φ(y) directly requires mapping both points and taking a six-dimensional dot product. But the **polynomial kernel** k(x, y) = (x·y + 1)² produces the exact same result using only the original two-dimensional coordinates. As the dimensionality of the mapped space grows — and for the **RBF (Gaussian) kernel**, it is effectively infinite — this computational shortcut becomes not just convenient but essential.

The choice of kernel determines the geometry of the feature space and therefore the kinds of decision boundaries the model can learn. The **linear kernel** k(x, y) = x·y corresponds to no transformation at all — standard SVM. The **polynomial kernel** of degree d captures interactions between features up to order d. The **RBF kernel** k(x, y) = exp(−γ‖x−y‖²) maps to an infinite-dimensional space where every point gets its own bump of influence, making it a universal approximator. The tradeoff is familiar from supervised learning: more expressive kernels risk overfitting, especially with limited data. The kernel width parameter γ in the RBF kernel controls this directly — large γ makes each point influential only in its immediate neighborhood, while small γ produces smoother, more global decision boundaries.
