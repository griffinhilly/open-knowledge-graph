---
id: convolution-continuous-discrete-systems
title: Convolution in Continuous and Discrete Time
domain: engineering
course: signals-and-systems
prerequisites:
- id: lti-systems-and-impulse-response
  type: hard
- id: integral-calculus
  type: soft
- id: convolution-theorem-and-applications
  type: hard
builds-toward:
- convolution-theorem-and-applications
- fourier-transform-definition-properties
tags:
- convolution
- systems
- lti
stage: advanced
status: draft
---

# Convolution in Continuous and Discrete Time

## Core Idea
Convolution y(t) = ∫ x(τ)h(t−τ)dτ (continuous) or y[n] = Σ x[k]h[n−k] (discrete) computes the output of an LTI system by sliding and multiplying the impulse response with the input. Convolution is commutative, associative, and distributive over addition.
