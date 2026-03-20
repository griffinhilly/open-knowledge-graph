---
id: work-energy-theorem
title: The Work-Energy Theorem
domain: physics
course: classical-mechanics
prerequisites:
- id: work-and-energy
  type: hard
- id: kinetic-energy
  type: hard
- id: dot-product
  type: hard
- id: definite-integral-definition
  type: hard
builds-toward:
- conservation-of-energy
tags:
- work-energy-theorem
- net-work
- kinetic-energy
stage: formal-systems
status: validated
---

# The Work-Energy Theorem

## Core Idea
The net work done on an object equals the change in its kinetic energy: W_net = ΔKE = KE_f − KE_i. This powerful result follows directly from Newton's second law by integrating F = ma over displacement. It connects force-based and energy-based descriptions of motion and is often the most efficient tool for finding speeds without tracking forces over time.

## How It's Best Learned
Apply the theorem to problems where forces are known and final speed is sought: W_net = ½mv_f² − ½mv_i². Practice identifying all forces, computing the work each does, summing them, and setting equal to ΔKE.

## Common Misconceptions
- Using only some forces when computing net work — all forces, including friction and normal force, must be included.
- Confusing the work-energy theorem (uses net work) with conservation of energy (separates conservative and nonconservative work).

## Explainer

You already know that **work** is W = F · d = Fd cosθ for a constant force, and that the **dot product** generalizes this to vectors at arbitrary angles. You also know that **kinetic energy** is KE = ½mv². The work-energy theorem is the mathematical bridge connecting these two quantities, and its derivation reveals why the bridge exists: both work and kinetic energy originate from the same equation — Newton's second law.

The derivation is clean. Start with F_net = ma. Write a = dv/dt. Use the chain rule: a = (dv/ds)(ds/dt) = v(dv/ds), where s is displacement along the path. Then F_net ds = mv dv. Integrate both sides: ∫F_net ds (the net work W_net) = ∫mv dv = ½mv_f² − ½mv_i² = ΔKE. That's it. **W_net = ΔKE** is not a separate postulate — it is Newton's second law rewritten in energy terms by integrating over displacement rather than over time. The moment you accept F = ma, the work-energy theorem follows automatically.

The word "net" carries enormous practical weight. Net work means the total work done by *all* forces acting on the object — gravity, normal force, friction, applied forces, tension, everything. A common error is computing only the work done by the "interesting" force (say, a push) and forgetting that friction does negative work and the normal force does zero work. Because the normal force is always perpendicular to motion, it contributes nothing to W_net regardless of its magnitude — cosθ = 0. Because friction opposes motion, it always contributes negative work, reducing the final kinetic energy. Getting W_net right requires a complete free-body diagram and careful sign conventions.

The theorem's power comes from what it ignores. Unlike Newton's second law applied directly, the work-energy theorem does not require you to track the details of the force over the entire path — only the total work done. If you can compute W_net (often by adding up W = Fd for each force), you immediately get Δ(½mv²). This makes it the method of choice for "what is the final speed?" questions where forces are known but you don't want to solve a differential equation. The theorem is also the stepping stone to conservation of energy: if you split W_net into work by conservative forces (expressible as −ΔPE) and nonconservative forces (friction, etc.), you get the full energy conservation equation. But the work-energy theorem itself is more primitive and more general — it holds even when energy is not conserved, because it tracks the actual net work, including dissipation.
