---
id: spring-mass-system
title: Spring-Mass Oscillator
domain: physics
course: classical-mechanics
prerequisites:
- id: simple-harmonic-motion
  type: hard
- id: potential-energy
  type: hard
- id: conservation-of-energy
  type: soft
- id: differential-equations-intro
  type: soft
- id: elastic-potential-energy
  type: soft
tags:
- spring
- oscillation
- Hooke-law
- SHM
stage: formal-systems
status: validated
---
# Spring-Mass Oscillator

## Core Idea
A mass on a spring is the canonical SHM system. The spring exerts a restoring force F = −kx (Hooke's law), giving angular frequency ω = √(k/m) and period T = 2π√(m/k). Energy oscillates between kinetic (½mv²) and potential (½kx²) with total mechanical energy E = ½kA². At equilibrium the speed is maximum; at amplitude the speed is zero and PE is maximum.

## How It's Best Learned
Experimentally vary k (using different springs) and m and measure T, then compare to T = 2π√(m/k). Track energy at several positions during a cycle to verify E = ½kA² throughout.

## Common Misconceptions
- Thinking a stiffer spring leads to a longer period: stiffer (larger k) actually increases ω and decreases T.
- Forgetting that T = 2π√(m/k) assumes no damping and that the spring obeys Hooke's law throughout the motion.

## Questions

```yaml
- question: "A spring-mass oscillator has spring constant k and mass m. If you replace the spring with one that is four times stiffer (4k) while keeping the same mass, what happens to the period?"
  type: multiple-choice
  options:
    - "The period doubles — a stiffer spring has more force, so it takes longer to complete a cycle"
    - "The period halves — the system oscillates twice as fast"
    - "The period decreases by a factor of √2"
    - "The period is unchanged — it depends only on mass"
  answer: 1
  explanation: "T = 2π√(m/k). With k replaced by 4k, T becomes 2π√(m/4k) = 2π·(1/2)√(m/k) = T/2. The period halves. The common misconception is that a stiffer spring should move more slowly because it exerts a larger force — but larger k means larger restoring force at every displacement, which produces faster acceleration back to equilibrium and therefore faster oscillation. Stiffer springs always decrease period."

- question: "A student pulls a mass on a spring to amplitude A and releases it, timing the period. Then they pull the same mass to amplitude 2A and release it again. What do they measure for the second period?"
  type: multiple-choice
  options:
    - "Double the first period — a larger amplitude requires more distance to travel"
    - "√2 times the first period — energy is proportional to A², so velocity scales as √2"
    - "The same period as the first — period is amplitude-independent in SHM"
    - "Half the first period — more energy means faster oscillation"
  answer: 2
  explanation: "Period T = 2π√(m/k) depends only on k and m, not on amplitude. Doubling amplitude doubles the distance traveled in a cycle AND doubles the maximum velocity (v_max = Aω), so both effects cancel and the period is unchanged. This amplitude-independence is a unique and important property of SHM. The energy stored (½kA²) increases with amplitude, but energy determines how vigorously the system oscillates, not how fast."

- question: "The total mechanical energy of a spring-mass system equals ½kA² at every point in the oscillation cycle, including the equilibrium position."
  type: true-false
  answer: true
  explanation: "By conservation of energy, PE + KE = constant = ½kA² throughout the cycle. At equilibrium (x = 0), PE = 0 and KE = ½mv_max² = ½kA². At maximum displacement (x = A), KE = 0 and PE = ½kA². At any intermediate point, the two forms trade off but the sum is always ½kA². The total energy is set by the amplitude; the frequency is set by k and m independently."

- question: "A stiffer spring (larger k) results in a longer period because the larger restoring force means the mass takes more time to complete each oscillation."
  type: true-false
  answer: false
  explanation: "This intuition is backwards. A stiffer spring exerts a larger restoring force at every displacement, so the acceleration back toward equilibrium is larger, and the system oscillates faster. T = 2π√(m/k): since k is in the denominator under the square root, increasing k decreases T. The confusion arises from conflating 'larger force' with 'slower motion' — in SHM, the larger force produces larger accelerations and therefore faster oscillation."

- question: "Why can you change the amplitude of a spring-mass oscillator without affecting its frequency of oscillation?"
  type: short-answer
  answer: "Frequency depends only on k and m (ω = √(k/m)), not on how far the mass is displaced. Amplitude sets the energy stored (E = ½kA²) and the maximum speed (v_max = Aω), but both scale together — the extra distance of a larger amplitude is traversed at proportionally higher speeds. Physically, a larger amplitude means larger restoring forces AND larger velocities at every point, so the two effects cancel and the time per cycle is unchanged."
  explanation: "This amplitude-independence comes directly from Hooke's law being linear. Because F = −kx grows proportionally with displacement, doubling amplitude doubles both the force (and hence acceleration) and the distance, leaving the time to traverse the cycle unchanged. Nonlinear restoring forces break this symmetry, causing period to depend on amplitude — which is why large-angle pendulums drift and why this approximation is only valid for small displacements."
```

## Explainer

The spring-mass oscillator is the simplest physical system that oscillates, and it serves as the template for understanding oscillation everywhere — electrical circuits, molecular vibrations, sound waves, and quantum mechanics. From your prerequisite on **simple harmonic motion**, you know the kinematic description: position varies sinusoidally as x(t) = A·cos(ωt + φ). The spring-mass system explains *why* that description is correct by deriving it from Newton's second law and Hooke's law.

Hooke's law gives the restoring force: F = −kx. When the mass is displaced from equilibrium by distance x, the spring pulls it back with a force proportional to that displacement, always directed toward equilibrium. Applying Newton's second law: −kx = m·a = m·(d²x/dt²), which rearranges to d²x/dt² = −(k/m)·x. This is the equation of simple harmonic motion: acceleration is proportional to, and opposite in sign to, displacement. The proportionality constant is ω² = k/m, giving **angular frequency** ω = √(k/m) and **period** T = 2π/ω = 2π√(m/k). A stiffer spring (larger k) increases ω and *decreases* T — the system oscillates faster, not slower, which is the most common intuition error.

The **energy picture** is equally important and connects directly to your prerequisites on **potential energy** and **conservation of energy**. The spring stores elastic potential energy PE = ½kx². At maximum displacement x = A, all energy is potential: PE = ½kA², KE = 0. At equilibrium x = 0, all energy is kinetic: KE = ½mv_max², PE = 0. Conservation of energy means PE + KE = ½kA² throughout the cycle — the two forms trade off continuously. Setting ½mv_max² = ½kA² gives v_max = A√(k/m) = Aω. The energy stored — and therefore the amplitude — is set by initial conditions; the frequency is set by k and m independently. This means you can change how vigorously the system oscillates without changing how fast it oscillates.

The spring-mass system is a model, not just a specific calculation, because Hooke's law is a **linearization** that applies to *any* stable equilibrium under small displacements. If you have a potential energy minimum — a marble in a bowl, an atom in a crystal lattice, a pendulum hanging at rest — the potential energy near the bottom is well approximated by a parabola: PE ≈ ½kx² for some effective spring constant k. This means every stable equilibrium oscillates like a spring-mass system for small perturbations. Understanding the spring-mass system in full gives you a reusable template: whenever you encounter an oscillating system in physics, chemistry, or engineering, the first question is always "what is the effective k and effective m?" — and then the period, frequency, energy, and velocity relations all follow immediately from the results you know here.
