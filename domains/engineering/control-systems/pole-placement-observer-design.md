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
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- pole-placement
- state-feedback
- observer
- eigenvalue-assignment
stage: expert
status: validated
---

# Pole Placement via State Feedback and Observer Design

## Core Idea
If system is controllable, state feedback u = -Kx can place closed-loop poles at arbitrary locations. Observer estimates unmeasured states from y; if observable, observer poles can be placed arbitrarily. Pole-placement design trade-off: faster response requires higher gain and larger control effort; observer poles typically placed faster than controller poles (separation principle).

## Questions

```yaml
- question: "A control engineer designs full-state feedback for a 4th-order controllable system. She wants the closed-loop response to have poles at {−1 ± 2j, −5, −6}. What does controllability guarantee about this design?"
  type: multiple-choice
  options:
    - "The closed-loop system will be stable, but the poles can only be placed on the real axis"
    - "A gain matrix K exists such that the eigenvalues of (A − BK) are exactly {−1 ± 2j, −5, −6}"
    - "The system's natural response is already fast enough; additional feedback only slightly adjusts performance"
    - "Controllability guarantees the poles can be placed anywhere, including the right half-plane, for testing purposes"
  answer: 1
  explanation: "Controllability is the precise mathematical condition guaranteeing that K can be chosen to make the closed-loop eigenvalues (poles of A − BK) be any desired set of values. This follows from the Cayley-Hamilton theorem: for a controllable system, the controllability matrix has full rank, enabling Ackermann's formula or direct comparison to solve for K given any target characteristic polynomial. Option A is wrong — poles can be placed anywhere in the complex plane (real or complex), not just on the real axis. Option D is technically true as a mathematical statement but misses the point — instability is of course never desired in practice."

- question: "In an observer-based control system, why are the observer poles typically designed to be 2 to 5 times faster (further left in the complex plane) than the controller poles?"
  type: multiple-choice
  options:
    - "Faster observer poles reduce the control effort required from the actuators"
    - "The separation principle requires observer poles to be faster to ensure the two sets of poles do not interfere"
    - "The estimated states need to converge to true states before the controller dynamics become dominant, so observer errors don't significantly degrade performance"
    - "Faster observer poles increase the system's noise rejection by making the Luenberger gain L larger"
  answer: 2
  explanation: "The full-state feedback controller was designed assuming perfect knowledge of the states. When an observer estimates those states, the controller is fed x̂ instead of x — and x̂ contains estimation error e = x − x̂. If the observer error decays much faster than the controller dynamics unfold, then by the time the controller acts on the estimated states, the estimation error is negligible, and performance is nearly identical to the ideal full-state feedback case. If observer poles are slower than controller poles, significant estimation error persists while the controller is actively responding, degrading performance. Note: faster observer poles also increase L, which can amplify sensor noise — this is the real engineering tradeoff the rule of thumb balances."

- question: "When observer-based state feedback is implemented (substituting x̂ for x in u = −Kx), the combined closed-loop eigenvalues are a complex mixture of the controller and observer poles that interact and is expected to be jointly optimized."
  type: true-false
  answer: false
  explanation: "False — this is precisely what the separation principle disproves. The combined closed-loop system's characteristic polynomial factors into the controller polynomial (from K, eigenvalues of A − BK) and the observer polynomial (from L, eigenvalues of A − LC). These two sets of poles do not interact: the closed-loop eigenvalues are the simple union of the controller poles and observer poles, nothing more. This remarkable result means K can be designed as if perfect state knowledge existed, and L can be designed purely based on convergence speed requirements, with the guarantee that their combination will produce the intended result."

- question: "A system is observable but not controllable. It is still possible to design a Luenberger observer that estimates the system states with arbitrary convergence speed."
  type: true-false
  answer: true
  explanation: "True. Controllability and observability are independent properties. Observability determines whether an observer can reconstruct states from outputs; controllability determines whether state feedback can assign arbitrary closed-loop poles. If the system is observable, the observer gain matrix L can be chosen to make the observer error decay at any desired rate — this requires only observability (that the observability matrix has full rank, enabling arbitrary placement of A − LC eigenvalues). The lack of controllability only means you cannot place the state feedback controller poles arbitrarily — but observer design is unaffected. Of course, a non-controllable system has limited utility even with a perfect observer."

- question: "What is the separation principle, and why does it simplify the practical design of observer-based control systems?"
  type: short-answer
  answer: "The separation principle states that when state feedback u = −Kx̂ is implemented using observed states x̂ from a Luenberger observer, the combined closed-loop eigenvalues are exactly the union of the controller poles (eigenvalues of A − BK) and the observer poles (eigenvalues of A − LC), with no interaction between them. This means K and L can be designed independently: first design K as if perfect state knowledge were available, then design L to make estimation errors converge fast enough. The two designs are then connected without re-optimization, and the combined system behaves as intended."
  explanation: "Without the separation principle, designing an observer-based controller would require jointly optimizing K and L to achieve desired combined eigenvalues — a much harder 2n-dimensional problem for an nth-order system. The principle turns this into two independent nth-order problems. It also provides design intuition: controller poles govern the response the user sees; observer poles govern the hidden estimation dynamics. The convention to place observer poles faster ensures the hidden dynamics resolve before the visible response unfolds."
```

## Explainer

From your study of eigenvalues and eigenvectors, you know that the time evolution of a linear system ẋ = Ax is governed by the eigenvalues of A — they determine whether the system is stable, how fast it decays, and whether it oscillates. From observability and controllability, you know when it is *possible* in principle to steer the system's states and observe them. Pole placement is the design method that turns those theoretical possibilities into a concrete algorithm: choose a feedback gain matrix K so that the closed-loop eigenvalues — the **poles** — are exactly where you need them.

The algebra is direct. Applying full-state feedback u = −Kx to the system ẋ = Ax + Bu gives the closed-loop system ẋ = (A − BK)x. The eigenvalues of A − BK are the closed-loop poles, and they depend on K. If the system is **controllable**, the Cayley-Hamilton theorem guarantees that K can be chosen (via Ackermann's formula or direct comparison) to make A − BK have any desired characteristic polynomial — meaning any desired set of eigenvalues. The desired poles encode your performance objectives: poles on the real axis give non-oscillatory response; complex conjugate pairs give damped oscillation with frequency ω_n and damping ratio ζ; poles further left in the complex plane give faster decay. The tradeoff is unavoidable: faster poles require larger entries in K, which means larger control inputs u = −Kx, which eventually saturates actuators, amplifies sensor noise, and makes the design sensitive to modeling errors.

The catch is that full-state feedback requires knowing all n states x(t) at every instant, but you typically only measure the output y = Cx — a low-dimensional projection of the state. An **observer** (Luenberger observer) solves this problem by running a software copy of the system in parallel: x̂̇ = Ax̂ + Bu + L(y − Cx̂). The observer gets the same input u and has access to the measurement y. The correction term L(y − Cx̂) is the **innovation** — the discrepancy between the actual measured output and the model's predicted output — multiplied by the observer gain matrix L. If the system is **observable**, you can choose L to make the estimation error e = x − x̂ decay at any desired rate: the error dynamics ė = (A − LC)e have eigenvalues set by L exactly as the controller eigenvalues were set by K. The rule of thumb is to place observer poles two to five times faster than the controller poles, so the estimated states converge before the controller dynamics are visible.

The **separation principle** is the elegant result that makes this two-piece architecture coherent. When you connect the observer to the controller — using x̂ instead of x in the feedback law u = −Kx̂ — the combined closed-loop system's eigenvalues are simply the union of the controller poles (from K) and the observer poles (from L). They do not interact. This means you can design K and L independently — first choose K to achieve the desired closed-loop response assuming perfect state knowledge, then choose L to make the estimated state converge fast enough that the approximation holds — and the resulting combined system behaves as intended. The separation principle is the theoretical justification for the standard control engineering workflow: specify response, design state feedback, design observer, implement together. It transforms a hard joint optimization into two independent, tractable design steps.
