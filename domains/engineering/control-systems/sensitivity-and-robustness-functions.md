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
stage: expert
status: validated
---

# Sensitivity and Complementary Sensitivity Functions

## Core Idea
Sensitivity function S(s) = 1/(1+L(s)) quantifies output deviation per unit plant perturbation; complementary sensitivity T(s) = L(s)/(1+L(s)) quantifies closed-loop response relative to open-loop. Trade-off: S and T are complementary (S + T = 1), so reducing error sensitivity at some frequencies increases it elsewhere. Design balances sensitivity and robustness across frequency range.

## Questions

```yaml
- question: "A control engineer wants to design a feedback controller that simultaneously achieves: (1) excellent disturbance rejection at ALL frequencies (|S(jω)| ≈ 0 for all ω) and (2) perfect tracking at ALL frequencies (|T(jω)| ≈ 1 for all ω). Is this achievable?"
  type: multiple-choice
  options:
    - "Yes — sufficiently high loop gain achieves both goals simultaneously"
    - "Yes — a minimum-phase plant with no right-half-plane zeros allows both"
    - "No — the identity S + T = 1 makes it impossible to have |S| ≈ 0 and |T| ≈ 1 at different frequencies simultaneously"
    - "No — but only because real actuators saturate and cannot provide infinite gain"
  answer: 2
  explanation: "S + T = 1 is an algebraic identity that holds at every frequency. If |T(jω)| ≈ 1 at some frequency, then |S(jω)| ≈ 0 there — which is actually good for tracking. The problem is at high frequencies: making T large there to achieve tracking amplifies sensor noise into the control signal. Conversely, any frequency where |S| is forced small forces |T| ≈ 1 there, which is fine for low frequencies but harmful at high frequencies. The fundamental constraint is not actuator saturation but the mathematical identity S + T = 1 itself."

- question: "A designer adds integral control to eliminate steady-state tracking error, which forces S(0) = 0 (zero sensitivity at DC). What does Bode's sensitivity integral theorem imply about S(jω) at other frequencies?"
  type: multiple-choice
  options:
    - "The sensitivity function remains near zero at all frequencies due to the integral's persistent correction"
    - "The sensitivity function must peak above 1 at some finite frequency to compensate, because the integral of log|S(jω)| over all frequencies must equal zero"
    - "The sensitivity function becomes exactly 1 at all frequencies above the crossover frequency"
    - "No constraint is imposed — the sensitivity function can be made arbitrarily small at all frequencies with a high-gain integral controller"
  answer: 1
  explanation: "Bode's sensitivity integral states that for a stable, minimum-phase loop, ∫log|S(jω)|dω = 0. If integral action pushes log|S| strongly negative at DC (large negative contribution), the integral constraint forces a compensating positive region — a sensitivity peak — at some finite frequency. This is the 'waterbed effect': pushing S down in one band forces it up in another. The integral controller trades excellent DC rejection for a sensitivity hump at moderate frequencies, which manifests as oscillatory transients in the step response."

- question: "The identity S(s) + T(s) = 1 means that reducing sensitivity to disturbances at some frequencies necessarily increases sensitivity at other frequencies."
  type: true-false
  answer: true
  explanation: "This is the waterbed effect, formalized by Bode's sensitivity integral. S + T = 1 is an algebraic identity: wherever |S| is small (good disturbance rejection), |T| is close to 1 (good tracking, but also high susceptibility to sensor noise at that frequency). More importantly, Bode's integral theorem shows that suppressing |S| in one frequency band must be compensated by amplification in another. There is no 'free lunch' in feedback design — every improvement in one frequency region comes at a cost somewhere else."

- question: "Increasing loop gain uniformly across most frequencies reduces the sensitivity function S(jω) everywhere, simultaneously improving disturbance rejection and tracking without any penalty."
  type: true-false
  answer: false
  explanation: "While increasing loop gain does reduce |S| at frequencies where it was already large (improving disturbance rejection and tracking there), the waterbed effect prevents a uniform reduction everywhere. At high frequencies, high loop gain means the feedback loop amplifies sensor noise — large |T| at high frequencies. Additionally, practical plants have phase lag that causes the loop to become unstable at sufficiently high gain. Bode's sensitivity integral formally shows that reducing sensitivity below its open-loop value in one band requires a compensating sensitivity increase elsewhere. Uniform improvement across all frequencies is mathematically impossible for any realizable system."

- question: "What is the 'waterbed effect' in control systems, and why does it make it impossible to achieve arbitrarily good disturbance rejection across all frequencies simultaneously?"
  type: short-answer
  answer: "The waterbed effect refers to the consequence of Bode's sensitivity integral: for a stable, minimum-phase feedback loop, the area under log|S(jω)| over all frequencies is fixed (equals zero for minimum-phase systems). Suppressing sensitivity in one frequency band — like adding integral action to eliminate DC error — creates a compensating sensitivity peak at another frequency. You cannot push the 'water' down everywhere; reducing it in one region forces it up in another. This is why every feedback design involves tradeoffs: tight performance at low frequencies, where disturbances matter, comes at the cost of reduced robustness at higher frequencies, where unmodeled dynamics and sensor noise dominate."
  explanation: "The waterbed effect is not an engineering limitation that better technology could overcome — it is a mathematical constraint on the class of stable feedback systems. It explains why there is no universally optimal controller: every controller design is a choice about where to push the sensitivity waterbed, trading off low-frequency performance against high-frequency robustness. Understanding this constraint is central to robust control design and explains why bandwidth limitations are fundamental rather than incidental."
```

## Explainer

Start with the loop transfer function L(s) = C(s)P(s) — the product of controller and plant gains around the feedback loop. You learned from feedback control fundamentals that high loop gain reduces steady-state error. The **sensitivity function** S(s) = 1/(1 + L(s)) quantifies exactly how much error persists: if the plant changes by a small fraction δ, the output changes by S(jω) × δ at frequency ω. Where |L(jω)| is large, S is small and the feedback loop is tight — disturbances are well rejected. Where |L(jω)| is small (high frequencies), S approaches 1 and the loop has little authority.

The **complementary sensitivity function** T(s) = L(s)/(1 + L(s)) is the closed-loop transfer function from reference to output. It measures tracking performance: T close to 1 means the output faithfully follows the reference. The identity S + T = 1 is not just algebra — it is the fundamental conservation law of feedback. You cannot simultaneously reduce S and T at the same frequency. Making the loop tight for tracking (T ≈ 1) forces S ≈ 0 at those frequencies, which is good. But trying to make S small at high frequencies necessarily makes T large there, which means high-frequency noise on the sensor gets amplified into the control output.

This constraint has a deeper form known as Bode's sensitivity integral: for a stable, minimum-phase loop, the integral of log|S(jω)| over all frequencies equals zero. Suppressing sensitivity in one frequency band creates a "waterbed" — sensitivity must rise elsewhere to compensate. This is why integral controllers that eliminate steady-state error (pushing S to zero at DC) inevitably create a sensitivity peak at some finite frequency. You chose the location and height of that peak when you designed the controller.

For robust stability, the model uncertainty analysis you already know connects directly to T. If the true plant is P(1 + Δ), where |Δ(jω)| ≤ l_m(ω) is the multiplicative uncertainty bound, the closed-loop remains stable for all such plants if and only if |T(jω)| < 1/l_m(ω) at all frequencies. Large T — good tracking — conflicts with small T required for robustness to high-frequency uncertainty. This trade-off is inescapable and defines the bandwidth of any feedback system: push the crossover frequency too high and uncertainty grows faster than T falls, causing instability; too low and the loop is sluggish. The sensitivity and complementary sensitivity functions are the quantitative language for navigating this design space.
