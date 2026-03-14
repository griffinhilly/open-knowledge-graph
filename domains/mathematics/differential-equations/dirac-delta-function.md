---
id: dirac-delta-function
title: Dirac Delta Function and Impulse Response
domain: mathematics
course: differential-equations
prerequisites:
- id: convolution-theorem
  type: hard
- id: laplace-transform-of-derivatives
  type: soft
tags:
- laplace-transform
- delta-function
- impulse
stage: advanced
status: draft
---

# Dirac Delta Function and Impulse Response

## Core Idea
The Dirac delta function δ(t - a) is a 'generalized function' that is zero everywhere except t = a, where it is infinite in such a way that ∫δ(t - a)·f(t) dt = f(a). Its Laplace transform is L{δ(t - a)} = e^{-as}, making it ideal for modeling instantaneous impulses in systems.
