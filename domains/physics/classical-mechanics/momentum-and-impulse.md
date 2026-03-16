---
id: momentum-and-impulse
title: Momentum and Impulse
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
- id: derivatives
  type: soft
builds-toward:
- conservation-of-momentum
- angular-momentum
tags:
- momentum
- impulse
- force
- time
stage: abstract-reasoning
status: validated
---

# Momentum and Impulse

## Core Idea
Linear momentum is the product of mass and velocity: p = mv. It is a vector quantity measured in kg·m/s. The impulse-momentum theorem states that the net impulse (J = FΔt, or ∫F dt for variable forces) equals the change in momentum: J = Δp. This is just Newton's second law rewritten in terms of momentum, but it is especially useful when forces act over short times (impacts, collisions) where force vs. time data is available.

## How It's Best Learned
Compute impulse from area under force-time graphs and set equal to change in momentum. Compare the impulse-momentum approach to the F = ma approach: both give the same answer, but impulse is easier when force varies with time.

## Common Misconceptions
- Confusing momentum (mv) with kinetic energy (½mv²): both depend on mass and speed, but momentum is a vector and scales linearly with v.
- Thinking impulse requires a long time: a large force over a very short time can deliver a large impulse.

## Questions

```yaml
- question: "Car A has mass 1000 kg moving at 20 m/s. Car B has mass 2000 kg moving at 10 m/s. Which has greater momentum magnitude?"
  type: multiple-choice
  options: ["Car A, because it is faster", "Car B, because it is heavier", "They are equal (both 20,000 kg·m/s)", "Cannot be determined without direction information"]
  answer: 2
  explanation: "Momentum = mv. Car A: 1000 × 20 = 20,000 kg·m/s. Car B: 2000 × 10 = 20,000 kg·m/s. They are equal. This illustrates that momentum balances mass and velocity linearly — unlike kinetic energy (½mv²), which would give Car A (KE = 200,000 J) twice the energy of Car B (KE = 100,000 J)."

- question: "A large impulse always requires a large force acting over a long period of time."
  type: true-false
  answer: false
  explanation: "Impulse is J = FΔt (or ∫F dt for variable force). A very large force acting over a very short time can deliver a large impulse — a golf club striking a ball involves milliseconds of contact but enormous force. What matters is the product FΔt, not either factor alone. This is also why airbags work: they increase Δt to reduce the peak force for the same total impulse."

- question: "A 0.5 kg ball moving at 10 m/s strikes a wall and bounces back at 8 m/s in the opposite direction. What is the magnitude of the impulse delivered to the ball?"
  type: short-answer
  answer: "9 kg·m/s"
  explanation: "Impulse = Δp = m(v_f − v_i). Taking the initial direction as positive: v_i = +10 m/s, v_f = −8 m/s. Δp = 0.5 × (−8 − 10) = 0.5 × (−18) = −9 kg·m/s. The magnitude is 9 kg·m/s. A common error is ignoring the direction reversal and computing 0.5 × (10 − 8) = 1 kg·m/s — but the sign change from the bounce is the whole story here."
```

## Explainer

You already know Newton's second law as F = ma. Momentum rewrites this in a form that turns out to be more general: define p = mv, and Newton's second law becomes F_net = dp/dt. When mass is constant this reduces to the familiar F = ma, but the momentum form applies even when mass changes — for example, a rocket expelling fuel, or a raindrop collecting mass as it falls. Momentum is the more fundamental formulation.

Impulse is the accumulated "dose" of force over time: J = ∫F dt, or J = FΔt when the force is constant. The impulse-momentum theorem J = Δp follows immediately from integrating F = dp/dt — it is not a separate law, just Newton's second law recast. Its practical value is in collision and impact problems where you know the initial and final momenta but the force during impact is complicated and short-lived. Instead of modeling the force in detail, you work with its net effect: the change in momentum.

A critical distinction is between momentum and kinetic energy. Momentum (mv) is a vector and scales linearly with speed. Kinetic energy (½mv²) is a scalar and scales with speed squared. A ball bouncing off a wall at the same speed it arrived has zero change in kinetic energy — but its momentum change is large because the direction reversed. These quantities track different aspects of motion, obey different conservation laws, and are not interchangeable. Keeping them separate will matter especially when you study conservation of momentum and the distinction between elastic and inelastic collisions.

The impulse interpretation as area under a force-time graph has direct practical applications. Real collisions involve forces that spike sharply and then fall to zero. The total area under the F(t) curve is the impulse, regardless of the shape of the spike. This is how impact sensors and crash testing work: integrate the force over time to get the impulse, then infer velocity changes. It also explains safety engineering: a cushioned surface and a hard surface deliver the same total impulse to stop your fall (same Δp, since you go from moving to rest), but the cushion stretches the impulse over more time, reducing the peak force on your body.

As you move toward conservation of momentum, the key insight from this topic is that impulse is the mechanism by which momentum changes. In an isolated system where no external impulse acts, total momentum is conserved. That conservation law — not the impulse-momentum theorem itself — will be the main tool for analyzing collisions. But understanding impulse first grounds the conservation law in Newton's second law rather than treating it as an unexplained postulate.
