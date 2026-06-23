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
- id: elastic-potential-energy
  type: soft
- id: gravitational-potential-energy
  type: soft
- id: potential-energy-intro
  type: soft
- id: what-is-energy
  type: soft
builds-toward:
- conservation-of-energy
- spring-mass-system
tags:
- potential-energy
- gravitational-PE
- elastic-PE
- Hooke-law
stage: formal-systems
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

## Questions

```yaml
- question: "Student A sets the floor as h = 0 and calculates that a book on a 1-meter-high table has gravitational PE = 10 J. Student B sets the tabletop as h = 0. What is the book's PE according to Student B?"
  type: multiple-choice
  options:
    - "10 J — PE is an absolute property of the object and doesn't change with reference choice"
    - "0 J — because the book is at the reference height, its PE is zero in Student B's framework"
    - "−10 J — Student B's reference is higher, so the floor now has negative PE relative to it"
    - "It is impossible to determine without knowing the book's mass"
  answer: 1
  explanation: "PE is defined relative to a chosen reference level, so its absolute value changes with the choice. Student B chose the table as h = 0, so the book sitting on the table has h = 0 and thus PE = mgh = mg(0) = 0 J. This isn't a contradiction — both students agree on what matters: if the book falls from the table to the floor, ΔPE = −10 J in Student A's framework and also ΔPE = 0 − (−10) = −10 J if Student B extends his coordinates below the table. Only changes in PE are physically meaningful."

- question: "A spring with constant k = 200 N/m is first compressed by 3 cm, then released and stretched by 3 cm. How does the elastic PE stored compare in the two cases?"
  type: multiple-choice
  options:
    - "The compressed spring stores more PE because compression requires more force than stretching"
    - "The stretched spring stores more PE because extension involves greater displacement"
    - "Both store the same PE — the formula U = ½kx² depends only on the magnitude of displacement"
    - "PE is not defined for a compressed spring since it cannot convert to kinetic energy in that direction"
  answer: 2
  explanation: "U_s = ½kx² depends on x², which is always positive regardless of whether x represents compression or extension. When |x| = 3 cm in both cases, U_s = ½(200)(0.03)² = 0.09 J in both cases. The direction of deformation is irrelevant to the stored energy — the spring stores the same energy whether you push it in or pull it out by the same distance. This is why the formula uses x² rather than a signed quantity."

- question: "The work done by gravity as an object falls from height h to the ground equals the decrease in the object's gravitational potential energy."
  type: true-false
  answer: true
  explanation: "This is the fundamental relationship between conservative forces and potential energy. Gravity does positive work W = mgh on a falling object, and simultaneously the object's gravitational PE decreases by exactly mgh (from mgh to 0 if ground is the reference). Work done by a conservative force equals the negative of the change in PE: W = −ΔU. So if PE decreases by 10 J, gravity did 10 J of work — that energy transferred into kinetic energy, consistent with energy conservation."

- question: "An object's gravitational potential energy is uniquely determined by its height above the ground."
  type: true-false
  answer: false
  explanation: "PE has no unique absolute value — only changes in PE are physically meaningful. The value of U_g = mgh depends entirely on where you choose h = 0. The same object at the same height has PE = 10 J if you choose the floor as reference, PE = 0 J if you choose the table as reference, and PE = −5 J if you choose a shelf above the table as reference. This is not a problem because every physical prediction depends on ΔPE, not PE itself. The choice of reference is a matter of convenience, not physics."

- question: "Why is only the change in potential energy — not its absolute value — physically meaningful? What would go wrong if we tried to assign a unique 'true' PE to an object?"
  type: short-answer
  answer: "PE is defined as the work done against a conservative force to move an object to its current position from some reference point. The reference point is arbitrary — there is no physical reason to prefer any particular choice of h = 0. Every measurable prediction (how fast the object moves after falling, how much work can be extracted) depends only on differences in PE between two positions, not on the absolute value at either one. Assigning a unique 'true' PE would require a universal reference point that physics does not provide."
  explanation: "This connects to a deep feature of conservative mechanics: forces are derived from the gradient (spatial derivative) of PE, and gradients are unchanged by adding a constant offset. So shifting the reference level by any amount changes every PE value by the same constant, leaving all force calculations — and therefore all physics — identical. The absolute value is gauge freedom; the differences are physical."
```

## Explainer

From your study of work and energy, you know that work is the transfer of energy through force acting over displacement. A conservative force — one for which the work done depends only on start and end points, not the path taken — can "store" that work and return it later. **Potential energy** is precisely this stored work: it is the energy a system possesses because of its configuration, waiting to be released as kinetic energy when the constraint is removed.

For gravitational PE near Earth's surface, the reasoning is direct. Lifting an object of mass m through height h requires doing work W = mgh against gravity (since gravity pulls down with force mg and you displace the object upward by h). That work is not lost — it is stored in the position of the object. Set the object loose and gravity does exactly that work on it, converting the stored PE back into kinetic energy. The formula U_g = mgh formalizes this, with h measured from whatever reference level you choose. The choice of reference is arbitrary because only **changes in PE** matter: ΔU_g = mgΔh. The book sitting on your desk has "more" gravitational PE than the same book on the floor, but neither value has physical meaning on its own — only the difference does. This is why you can set h = 0 wherever is convenient for a given problem.

For elastic PE, the reasoning connects to Hooke's law you already know: F = −kx, where x is the displacement from equilibrium and the negative sign means the force opposes the displacement (a restoring force). Compressing or stretching a spring by a small amount dx requires doing work dW = kx dx against the restoring force. Integrating from 0 to x gives the total work stored: U_s = ½kx². Note two important features: x appears squared, so the formula is always non-negative regardless of whether the spring is stretched or compressed, and the stored energy grows quadratically — doubling the displacement stores four times the energy. This quadratic dependence is characteristic of elastic systems and underlies the simple harmonic motion you will study next.

The deepest idea in potential energy is the connection between force and energy landscape. If you know U as a function of position, you can recover the force: F = −dU/dx (or in 3D, F = −∇U, using the gradient you may have encountered). This is not just a mathematical trick — it reflects the fundamental structure of conservative mechanics. The gradient of the potential energy field points in the direction of steepest increase; the force points opposite, toward decreasing U. A ball rolling in a bowl settles at the bottom because that is the potential energy minimum. Stability, equilibrium, and oscillation are all features of the potential energy landscape. Understanding this connection transforms PE from a formula to memorize into a geometric tool for reasoning about how any conservative system behaves.
