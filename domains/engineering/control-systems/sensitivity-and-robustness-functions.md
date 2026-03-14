---
id: sensitivity-and-robustness-functions
title: Sensitivity and Complementary Sensitivity Functions
domain: engineering
course: control-systems
prerequisites:
- id: model-uncertainty-robust-stability
  type: hard
- id: feedback-control-fundamentals
  type: soft
builds-toward:
- state-feedback-control-design
tags:
- sensitivity
- robustness
- transfer-functions
- performance
stage: advanced
status: draft
---

# Sensitivity and Complementary Sensitivity Functions

## Core Idea
Sensitivity function S(s) = 1/(1+L(s)) quantifies output deviation per unit plant perturbation; complementary sensitivity T(s) = L(s)/(1+L(s)) quantifies closed-loop response relative to open-loop. Trade-off: S and T are complementary (S + T = 1), so reducing error sensitivity at some frequencies increases it elsewhere. Design balances sensitivity and robustness across frequency range.
