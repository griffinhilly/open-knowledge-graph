---
id: pole-placement-observer-design
title: Pole Placement via State Feedback and Observer Design
domain: engineering
course: control-systems
prerequisites:
- id: observability-controllability-tests
  type: hard
- id: state-space-representation-control
  type: soft
- id: eigenvalues-eigenvectors
  type: hard
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- pole-placement
- state-feedback
- observer
- eigenvalue-assignment
stage: formal-systems
status: draft
---

# Pole Placement via State Feedback and Observer Design

## Core Idea
If system is controllable, state feedback u = -Kx can place closed-loop poles at arbitrary locations. Observer estimates unmeasured states from y; if observable, observer poles can be placed arbitrarily. Pole-placement design trade-off: faster response requires higher gain and larger control effort; observer poles typically placed faster than controller poles (separation principle).

## Explainer

From your study of eigenvalues and eigenvectors, you know that the time evolution of a linear system ẋ = Ax is governed by the eigenvalues of A — they determine whether the system is stable, how fast it decays, and whether it oscillates. From observability and controllability, you know when it is *possible* in principle to steer the system's states and observe them. Pole placement is the design method that turns those theoretical possibilities into a concrete algorithm: choose a feedback gain matrix K so that the closed-loop eigenvalues — the **poles** — are exactly where you need them.

The algebra is direct. Applying full-state feedback u = −Kx to the system ẋ = Ax + Bu gives the closed-loop system ẋ = (A − BK)x. The eigenvalues of A − BK are the closed-loop poles, and they depend on K. If the system is **controllable**, the Cayley-Hamilton theorem guarantees that K can be chosen (via Ackermann's formula or direct comparison) to make A − BK have any desired characteristic polynomial — meaning any desired set of eigenvalues. The desired poles encode your performance objectives: poles on the real axis give non-oscillatory response; complex conjugate pairs give damped oscillation with frequency ω_n and damping ratio ζ; poles further left in the complex plane give faster decay. The tradeoff is unavoidable: faster poles require larger entries in K, which means larger control inputs u = −Kx, which eventually saturates actuators, amplifies sensor noise, and makes the design sensitive to modeling errors.

The catch is that full-state feedback requires knowing all n states x(t) at every instant, but you typically only measure the output y = Cx — a low-dimensional projection of the state. An **observer** (Luenberger observer) solves this problem by running a software copy of the system in parallel: x̂̇ = Ax̂ + Bu + L(y − Cx̂). The observer gets the same input u and has access to the measurement y. The correction term L(y − Cx̂) is the **innovation** — the discrepancy between the actual measured output and the model's predicted output — multiplied by the observer gain matrix L. If the system is **observable**, you can choose L to make the estimation error e = x − x̂ decay at any desired rate: the error dynamics ė = (A − LC)e have eigenvalues set by L exactly as the controller eigenvalues were set by K. The rule of thumb is to place observer poles two to five times faster than the controller poles, so the estimated states converge before the controller dynamics are visible.

The **separation principle** is the elegant result that makes this two-piece architecture coherent. When you connect the observer to the controller — using x̂ instead of x in the feedback law u = −Kx̂ — the combined closed-loop system's eigenvalues are simply the union of the controller poles (from K) and the observer poles (from L). They do not interact. This means you can design K and L independently — first choose K to achieve the desired closed-loop response assuming perfect state knowledge, then choose L to make the estimated state converge fast enough that the approximation holds — and the resulting combined system behaves as intended. The separation principle is the theoretical justification for the standard control engineering workflow: specify response, design state feedback, design observer, implement together. It transforms a hard joint optimization into two independent, tractable design steps.
