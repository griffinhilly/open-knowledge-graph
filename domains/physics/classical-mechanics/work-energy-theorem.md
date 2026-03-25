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
- id: rotational-kinetic-energy
  type: soft
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

## Questions

```yaml
- question: "A book slides across a table. Three forces act on it: gravity (downward), normal force (upward), and friction (backward). Which forces contribute nonzero work to W_net?"
  type: multiple-choice
  options:
    - "Only friction, since it's the only force that changes the book's speed"
    - "Gravity and friction — normal force contributes nothing to W_net"
    - "All three forces contribute to W_net"
    - "Only friction and normal force; gravity cancels since the book stays on the table"
  answer: 0
  explanation: "For horizontal motion, both gravity and the normal force are perpendicular to the displacement (cos 90° = 0), so both do zero work. Only friction — acting opposite to displacement — does nonzero (negative) work. So W_net = W_friction alone for this scenario. This is a common misconception trap: W_net includes all forces, but many forces happen to be perpendicular to motion and thus contribute zero. Identifying which forces actually do work requires checking the angle between each force and the displacement."

- question: "The work-energy theorem W_net = ΔKE is best understood as:"
  type: multiple-choice
  options:
    - "A new postulate independent of Newton's laws"
    - "Newton's second law (F = ma) integrated over displacement rather than time"
    - "A special case that only applies when no friction is present"
    - "The statement that total mechanical energy is conserved"
  answer: 1
  explanation: "The work-energy theorem is not a separate law — it is derived from F_net = ma. Using the chain rule to write a = v(dv/ds) and integrating both sides over displacement gives ∫F_net ds = ΔKE. It is Newton's second law rewritten in energy terms. This is why it holds whenever F = ma holds, including when friction is present. Option D (energy conservation) is a different, stronger claim that requires separating conservative and nonconservative forces."

- question: "The normal force acting on an object moving across a flat surface does zero work, regardless of how large the normal force is."
  type: true-false
  answer: true
  explanation: "Work is W = F·d·cos θ, where θ is the angle between force and displacement. The normal force is always perpendicular to the surface and therefore perpendicular to the direction of motion (θ = 90°, cos 90° = 0). No matter how large the normal force, it contributes nothing to W_net. This is why pressing down harder on a sliding book doesn't directly change its speed through the work-energy theorem — though it does increase the friction force magnitude, which does negative work."

- question: "The work-energy theorem W_net = ΔKE fails to apply when friction acts, because friction dissipates energy and violates energy conservation."
  type: true-false
  answer: false
  explanation: "The work-energy theorem holds for all forces, including friction. W_net is the total work done by every force, including the negative work done by friction. When friction acts, W_net < 0 and kinetic energy decreases — the theorem correctly accounts for this. The work-energy theorem does NOT require energy conservation; it is more primitive than energy conservation. Energy conservation is a separate (stronger) statement that splits W_net into conservative and nonconservative components."

- question: "Why must you include ALL forces — not just the 'main' applied force — when computing W_net in the work-energy theorem?"
  type: short-answer
  answer: "Because ΔKE equals the total work done by every force on the object. W_net is defined as the sum of work contributions from all forces. The theorem derives from F_net = ma, where F_net is the vector sum of all forces. Omitting any force makes W_net incorrect, and the predicted ΔKE will be wrong. For instance, ignoring friction's negative work overestimates the final speed."
  explanation: "A complete free-body diagram is the essential first step. Every force on the diagram must have its work calculated (W = Fd cos θ), and these are summed to get W_net. Only then does W_net = ΔKE give the correct final kinetic energy. Forces perpendicular to motion contribute zero, but you must check each force — you cannot assume which ones matter without computing the angle."
```

## Explainer

You already know that **work** is W = F · d = Fd cosθ for a constant force, and that the **dot product** generalizes this to vectors at arbitrary angles. You also know that **kinetic energy** is KE = ½mv². The work-energy theorem is the mathematical bridge connecting these two quantities, and its derivation reveals why the bridge exists: both work and kinetic energy originate from the same equation — Newton's second law.

The derivation is clean. Start with F_net = ma. Write a = dv/dt. Use the chain rule: a = (dv/ds)(ds/dt) = v(dv/ds), where s is displacement along the path. Then F_net ds = mv dv. Integrate both sides: ∫F_net ds (the net work W_net) = ∫mv dv = ½mv_f² − ½mv_i² = ΔKE. That's it. **W_net = ΔKE** is not a separate postulate — it is Newton's second law rewritten in energy terms by integrating over displacement rather than over time. The moment you accept F = ma, the work-energy theorem follows automatically.

The word "net" carries enormous practical weight. Net work means the total work done by *all* forces acting on the object — gravity, normal force, friction, applied forces, tension, everything. A common error is computing only the work done by the "interesting" force (say, a push) and forgetting that friction does negative work and the normal force does zero work. Because the normal force is always perpendicular to motion, it contributes nothing to W_net regardless of its magnitude — cosθ = 0. Because friction opposes motion, it always contributes negative work, reducing the final kinetic energy. Getting W_net right requires a complete free-body diagram and careful sign conventions.

The theorem's power comes from what it ignores. Unlike Newton's second law applied directly, the work-energy theorem does not require you to track the details of the force over the entire path — only the total work done. If you can compute W_net (often by adding up W = Fd for each force), you immediately get Δ(½mv²). This makes it the method of choice for "what is the final speed?" questions where forces are known but you don't want to solve a differential equation. The theorem is also the stepping stone to conservation of energy: if you split W_net into work by conservative forces (expressible as −ΔPE) and nonconservative forces (friction, etc.), you get the full energy conservation equation. But the work-energy theorem itself is more primitive and more general — it holds even when energy is not conserved, because it tracks the actual net work, including dissipation.
