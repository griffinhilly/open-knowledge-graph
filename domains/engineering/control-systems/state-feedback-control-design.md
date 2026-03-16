---
id: state-feedback-control-design
title: State Feedback Control and Pole Placement
domain: engineering
course: control-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: controllability-and-observability
  type: hard
builds-toward:
- observer-state-estimation-design
- separation-principle-control-theory
tags:
- state-feedback
- pole-placement
- state-space
- design
stage: advanced
status: draft
---

# State Feedback Control and Pole Placement

## Core Idea
State feedback u = -Kx moves closed-loop poles to arbitrary locations (if system is controllable) by feeding back weighted state variables. Unlike transfer function design, state feedback directly assigns poles without iterative methods. Design involves: (1) specifying desired closed-loop poles from performance specs, (2) computing feedback gain K using pole placement, (3) verifying stability and margins.

## Explainer

You already know that a system in state-space form evolves as ẋ = Ax + Bu. The matrix A determines the open-loop poles — the eigenvalues of A — which govern whether the natural response decays, grows, or oscillates. If those eigenvalues are in the right half-plane, the system is unstable. The core idea of **state feedback** is that you can modify those eigenvalues by feeding the state back through a gain matrix K, setting u = −Kx. Substituting into the state equation gives ẋ = (A − BK)x, so the closed-loop poles are the eigenvalues of (A − BK). By choosing K appropriately, you move those eigenvalues to wherever you want them.

This is where controllability — your other prerequisite — becomes essential. The pole placement theorem states that you can assign the eigenvalues of (A − BK) to any set of locations in the complex plane if and only if the system is controllable. A system fails controllability if some mode of the dynamics is completely disconnected from the input — no choice of K can affect an uncontrollable mode because the control signal never reaches it. Once you've confirmed controllability, you translate your performance specifications (desired settling time, damping ratio, bandwidth) into a set of desired closed-loop pole locations, then solve for K. For low-order systems (2nd or 3rd order), you can do this by hand by matching characteristic polynomials; for higher-order systems, Ackermann's formula or numerical methods are standard.

The design trade-off is cost of control effort. Placing poles far into the left half-plane gives fast, well-damped responses, but requires large gains in K, which means large actuator commands. High-gain feedback amplifies sensor noise and can saturate actuators, causing real systems to behave very differently from the linear model. A useful intuition: each unit of speed you demand from your closed-loop system tends to cost proportionally more in control energy. A well-designed state feedback controller balances response speed against the practical limits of the actuator.

Consider an inverted pendulum — unstable open-loop, with a pole in the right half-plane. The control task is to compute the cart force u at each instant based on the full state (cart position, cart velocity, angle, angular rate) to keep the pendulum upright. With full state feedback u = −Kx, you choose K so that all four closed-loop poles land in the left half-plane at locations that give acceptable transient response. This is precisely what happens in practice with self-balancing robots: they measure the complete state many times per second and apply state feedback to stay upright. The mathematical design step — selecting K — is elegant, but real engineering challenges lie in obtaining the full state (which motivates the observer design that builds on this topic).
