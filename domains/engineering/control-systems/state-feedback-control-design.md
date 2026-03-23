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
stage: expert
status: draft
---

# State Feedback Control and Pole Placement

## Core Idea
State feedback u = -Kx moves closed-loop poles to arbitrary locations (if system is controllable) by feeding back weighted state variables. Unlike transfer function design, state feedback directly assigns poles without iterative methods. Design involves: (1) specifying desired closed-loop poles from performance specs, (2) computing feedback gain K using pole placement, (3) verifying stability and margins.

## Questions

```yaml
- question: "A 3rd-order system has one uncontrollable mode. An engineer applies state feedback u = −Kx and attempts to move all three poles to stable locations in the left half-plane. What will actually happen?"
  type: multiple-choice
  options:
    - "All three poles can be placed arbitrarily if the gain K is chosen large enough"
    - "The two controllable modes can be placed anywhere, but the uncontrollable mode remains fixed at its open-loop location"
    - "The feedback will stabilize all modes because u = −Kx affects the full state vector x"
    - "Ackermann's formula will find a valid K regardless of controllability"
  answer: 1
  explanation: "The pole placement theorem is precise: arbitrary pole assignment is possible if and only if the system is controllable. An uncontrollable mode is completely disconnected from the input — no choice of K can affect it, because the control signal never reaches that mode. The gain K acts on all elements of x, but if a mode of the dynamics does not respond to u, the feedback has no leverage there. Ackermann's formula will fail (the controllability matrix will be rank-deficient), and the uncontrollable pole stays put."

- question: "An engineer designs state feedback poles very far into the left half-plane to achieve extremely fast settling. What practical concern does this raise?"
  type: multiple-choice
  options:
    - "The system will lose controllability as the poles move farther left"
    - "Poles in the far left half-plane produce imaginary eigenvalues of (A − BK)"
    - "Large feedback gains amplify sensor noise and may saturate actuators, causing real behavior to diverge from the linear model"
    - "The observer design that follows will be unable to estimate the state quickly enough"
  answer: 2
  explanation: "Placing poles far to the left requires large entries in K, which means the control signal u = −Kx becomes very sensitive to the state — including measurement noise in each state variable. High-gain feedback amplifies noise, potentially driving actuators into saturation where the linear model no longer applies. The design trade-off is fundamental: faster response costs proportionally more control effort and increases sensitivity to noise and model uncertainty. Option D is a concern but is separate from the pole placement design step itself."

- question: "In state feedback design, the closed-loop poles are the eigenvalues of the matrix (A − BK)."
  type: true-false
  answer: true
  explanation: "This follows directly from the closed-loop dynamics. With u = −Kx substituted into ẋ = Ax + Bu, we get ẋ = Ax + B(−Kx) = (A − BK)x. The eigenvalues of (A − BK) are the closed-loop poles — the values that determine stability and transient response. By choosing K to shape (A − BK), the designer moves those eigenvalues to desired locations. This is the mathematical core of state feedback design."

- question: "Because u = −Kx feeds back the full state vector x, state feedback automatically handles situations where some states cannot be directly measured with sensors."
  type: true-false
  answer: false
  explanation: "This is a common and important misconception. State feedback requires access to the complete state vector x, but in real systems many states are not directly measurable — for example, you might measure position but not velocity, or angular displacement but not angular rate. State feedback assumes x is available; when it is not, a state observer (Luenberger observer or Kalman filter) must be designed to estimate x from available measurements. This is precisely why observer design is the next topic in the sequence: the mathematical elegance of u = −Kx depends on having x, which in practice must often be reconstructed."

- question: "Why does controllability determine whether state feedback can place closed-loop poles at arbitrary locations, and what happens physically when a mode is uncontrollable?"
  type: short-answer
  answer: "Controllability means every mode of the system dynamics can be influenced by the input u. An uncontrollable mode has a direction in state space that the input cannot reach — the control signal effectively has zero leverage on that mode's behavior. When you apply u = −Kx, the feedback modifies the closed-loop matrix to (A − BK), but an uncontrollable mode corresponds to a direction where BK has no effect, so the eigenvalue associated with that mode is unchanged regardless of K. Physically, it means some aspect of the system's natural dynamics is completely decoupled from the actuator."
  explanation: "The controllability matrix C = [B, AB, A²B, ...] spans exactly the subspace reachable by control inputs. If this matrix is rank-deficient, there are modes the input cannot excite. These modes evolve on their own according to the open-loop dynamics — they are invisible to the feedback law. This is why controllability is a prerequisite: pole placement only works in the controllable subspace, and an uncontrollable unstable mode cannot be stabilized by state feedback alone."
```

## Explainer

You already know that a system in state-space form evolves as ẋ = Ax + Bu. The matrix A determines the open-loop poles — the eigenvalues of A — which govern whether the natural response decays, grows, or oscillates. If those eigenvalues are in the right half-plane, the system is unstable. The core idea of **state feedback** is that you can modify those eigenvalues by feeding the state back through a gain matrix K, setting u = −Kx. Substituting into the state equation gives ẋ = (A − BK)x, so the closed-loop poles are the eigenvalues of (A − BK). By choosing K appropriately, you move those eigenvalues to wherever you want them.

This is where controllability — your other prerequisite — becomes essential. The pole placement theorem states that you can assign the eigenvalues of (A − BK) to any set of locations in the complex plane if and only if the system is controllable. A system fails controllability if some mode of the dynamics is completely disconnected from the input — no choice of K can affect an uncontrollable mode because the control signal never reaches it. Once you've confirmed controllability, you translate your performance specifications (desired settling time, damping ratio, bandwidth) into a set of desired closed-loop pole locations, then solve for K. For low-order systems (2nd or 3rd order), you can do this by hand by matching characteristic polynomials; for higher-order systems, Ackermann's formula or numerical methods are standard.

The design trade-off is cost of control effort. Placing poles far into the left half-plane gives fast, well-damped responses, but requires large gains in K, which means large actuator commands. High-gain feedback amplifies sensor noise and can saturate actuators, causing real systems to behave very differently from the linear model. A useful intuition: each unit of speed you demand from your closed-loop system tends to cost proportionally more in control energy. A well-designed state feedback controller balances response speed against the practical limits of the actuator.

Consider an inverted pendulum — unstable open-loop, with a pole in the right half-plane. The control task is to compute the cart force u at each instant based on the full state (cart position, cart velocity, angle, angular rate) to keep the pendulum upright. With full state feedback u = −Kx, you choose K so that all four closed-loop poles land in the left half-plane at locations that give acceptable transient response. This is precisely what happens in practice with self-balancing robots: they measure the complete state many times per second and apply state feedback to stay upright. The mathematical design step — selecting K — is elegant, but real engineering challenges lie in obtaining the full state (which motivates the observer design that builds on this topic).
