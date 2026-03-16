---
id: potential-energy
title: 'Potential Energy: Gravitational and Elastic'
domain: physics
course: classical-mechanics
prerequisites:
- id: work-and-energy
  type: hard
- id: gradient-vector
  type: soft
builds-toward:
- conservation-of-energy
- spring-mass-system
tags:
- potential-energy
- gravitational-PE
- elastic-PE
- Hooke-law
stage: abstract-reasoning
status: validated
---

# Potential Energy: Gravitational and Elastic

## Core Idea
Potential energy is stored energy associated with an object's position or configuration. Gravitational PE near Earth's surface is U_g = mgh, measured relative to a chosen reference height. Elastic PE stored in a spring compressed or stretched by x from equilibrium is U_s = ½kx², where k is the spring constant (Hooke's law). Both forms can convert to kinetic energy.

## How It's Best Learned
Define the reference level (h = 0) explicitly for each problem, then compute changes in PE rather than absolute values. Connect spring PE to Hooke's law F = −kx by integrating the restoring force over displacement.

## Common Misconceptions
- Treating PE as absolute rather than relative — only changes in PE are physically meaningful.
- Thinking the spring PE formula requires a signed x: U_s = ½kx² is always positive regardless of the direction of stretch or compression.
- Confusing spring constant k (N/m) with kinetic energy K — these share notation in different textbooks.

## Explainer

From your study of work and energy, you know that work is the transfer of energy through force acting over displacement. A conservative force — one for which the work done depends only on start and end points, not the path taken — can "store" that work and return it later. **Potential energy** is precisely this stored work: it is the energy a system possesses because of its configuration, waiting to be released as kinetic energy when the constraint is removed.

For gravitational PE near Earth's surface, the reasoning is direct. Lifting an object of mass m through height h requires doing work W = mgh against gravity (since gravity pulls down with force mg and you displace the object upward by h). That work is not lost — it is stored in the position of the object. Set the object loose and gravity does exactly that work on it, converting the stored PE back into kinetic energy. The formula U_g = mgh formalizes this, with h measured from whatever reference level you choose. The choice of reference is arbitrary because only **changes in PE** matter: ΔU_g = mgΔh. The book sitting on your desk has "more" gravitational PE than the same book on the floor, but neither value has physical meaning on its own — only the difference does. This is why you can set h = 0 wherever is convenient for a given problem.

For elastic PE, the reasoning connects to Hooke's law you already know: F = −kx, where x is the displacement from equilibrium and the negative sign means the force opposes the displacement (a restoring force). Compressing or stretching a spring by a small amount dx requires doing work dW = kx dx against the restoring force. Integrating from 0 to x gives the total work stored: U_s = ½kx². Note two important features: x appears squared, so the formula is always non-negative regardless of whether the spring is stretched or compressed, and the stored energy grows quadratically — doubling the displacement stores four times the energy. This quadratic dependence is characteristic of elastic systems and underlies the simple harmonic motion you will study next.

The deepest idea in potential energy is the connection between force and energy landscape. If you know U as a function of position, you can recover the force: F = −dU/dx (or in 3D, F = −∇U, using the gradient you may have encountered). This is not just a mathematical trick — it reflects the fundamental structure of conservative mechanics. The gradient of the potential energy field points in the direction of steepest increase; the force points opposite, toward decreasing U. A ball rolling in a bowl settles at the bottom because that is the potential energy minimum. Stability, equilibrium, and oscillation are all features of the potential energy landscape. Understanding this connection transforms PE from a formula to memorize into a geometric tool for reasoning about how any conservative system behaves.
