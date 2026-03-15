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
- support-vector-regression
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
