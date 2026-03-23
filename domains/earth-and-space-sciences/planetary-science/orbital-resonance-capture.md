---
id: orbital-resonance-capture
title: Orbital Resonance Capture and Locked Migration
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: planetary-migration-mechanisms
  type: hard
- id: keplers-laws
  type: soft
- id: kepler-laws-planetary-orbits
  type: hard
builds-toward:
- n-body-planetary-dynamics
- multi-planet-system-architecture
tags:
- resonances
- orbital-dynamics
- migration
- coupled-motion
stage: expert
status: validated
---

# Orbital Resonance Capture and Locked Migration

## Core Idea
Migrating planets can become trapped in orbital resonances (e.g., 2:1, 3:2, 5:2) when their orbital periods lock into simple integer ratios due to gravitational coupling through the disk. Once captured, planets migrate together as a locked pair, dramatically affecting system architecture and long-term stability.

## Questions

```yaml
- question: "A migrating planet approaches a 2:1 resonance with an inner planet. Which condition is required for resonance capture to occur?"
  type: multiple-choice
  options:
    - "The migrating planet must be more massive than the inner planet"
    - "The migration rate must be slow relative to the resonance's capture width"
    - "The planets must be in circular orbits before the encounter"
    - "The gas disk must have already dissipated before the planets interact"
  answer: 1
  explanation: "Resonance capture is a competition between the rate at which the migrating planet drifts through the resonance and the strength of the gravitational restoring force that holds it in resonance. If migration is too rapid, the planet passes through the resonance before the periodic kicks can lock it in place — like pushing a marble past a bowl too quickly. Only when migration is slow enough relative to the 'capture width' does the planet settle into the locked state. Mass and orbital shape are not the determining criteria."

- question: "Observations of a mature planetary system show no pairs in orbital resonance, even though models predict the planets migrated significantly during formation. What best explains this?"
  type: multiple-choice
  options:
    - "The planets migrated too slowly for resonance capture to occur"
    - "Resonances only form between planets of equal mass"
    - "After the gas disk dissipated, gravitational interactions destabilized the resonant chain"
    - "Resonances require circular orbits, which are rare in mature systems"
  answer: 2
  explanation: "Resonant configurations depend on disk damping to remain stable — the dissipative disk damps perturbations that would otherwise grow. When the gas disk disperses, that stabilizing influence vanishes. Gravitational perturbations between the planets can then amplify until the resonant chain breaks, scattering planets into the non-resonant orbits observed in most mature systems. Many systems likely formed in resonance but 'broke out' during a subsequent dynamical instability phase."

- question: "The reason orbital resonances produce strong gravitational effects is that the two planets' gravitational encounters always occur at the same orbital positions, causing kicks to accumulate rather than average out."
  type: true-false
  answer: true
  explanation: "This is the essence of resonance. When two orbiting bodies have a period ratio of exactly 2:1, they meet at the same geometrical configuration on every cycle. The gravitational kicks they exchange are always in the same direction, so they reinforce each other over time. If the periods were incommensurable (not a simple integer ratio), encounter positions would be random and kicks would average to near zero — no resonance effect."

- question: "Once two planets are captured into a 2:1 orbital resonance, their individual orbital periods remain fixed at the values they had at the moment of capture."
  type: true-false
  answer: false
  explanation: "Resonance capture does not freeze the orbital periods — it locks their *ratio*. The two planets continue to migrate together through the disk, so both periods can change substantially after capture. What is preserved is the integer ratio: if one period doubles, so must the other. This 'locked migration' means a resonant pair can travel large distances through a disk while maintaining their 2:1 (or 3:2, etc.) relationship."

- question: "Explain why periodic gravitational interactions at an orbital resonance are more dynamically significant than random encounters between non-resonant planets."
  type: short-answer
  answer: "At a resonance, two planets meet at the same orbital configuration on every cycle, so the gravitational kicks they deliver always act in the same direction. These coherent, repeated perturbations accumulate over time. For non-resonant planets, encounter geometries rotate continuously, so kicks alternate direction and largely cancel out over many orbits. The resonance transforms chaotic averaging into a systematic, growing effect — like repeatedly pushing a swing at exactly the right moment versus pushing at random intervals."
  explanation: "This is the core physical mechanism behind all resonance phenomena. The key is coherence: same phase, same location, same direction on every cycle. The accumulation of coherent kicks is what makes resonances powerful enough to dominate the long-term evolution of planetary systems, even though individual kicks are small."
```

## Explainer

You already know from Kepler's laws that a planet's orbital period depends on its distance from the star — closer planets orbit faster, farther planets orbit slower. You also know that planets embedded in a gas disk can migrate inward or outward as they exchange angular momentum with disk material. Resonance capture happens when these two ideas collide: a migrating planet's period drifts until it falls into a simple integer ratio with a neighboring planet, and gravitational interactions lock the two orbits together.

Think of it like two runners on a circular track. If one runner laps the other at random intervals, their encounters are fleeting and uncoordinated. But if one runner completes exactly two laps for every one lap the other completes, they meet at the same point on the track every cycle. Each meeting delivers a gravitational kick in the same direction, and these repeated, coherent kicks accumulate rather than averaging out. This is the essence of an **orbital resonance** — periodic gravitational interactions that reinforce rather than cancel.

**Resonance capture** occurs when a migrating planet approaches this special period ratio from outside. As the planet drifts closer to resonance, the gravitational perturbations grow stronger and begin to resist further drift. If migration is slow enough relative to the resonance's "capture width," the planet settles into the resonance like a marble rolling into a bowl. The two planets are now **locked**: their orbital periods maintain the integer ratio even as both continue migrating through the disk together. The inner planet's gravitational torque on the outer planet, and vice versa, creates a feedback loop that preserves the period ratio.

This locked migration has profound consequences for planetary system architecture. Resonant chains — where three or more planets are locked in successive resonances like 4:2:1 — can transport entire systems inward while maintaining spacing. The TRAPPIST-1 system, with seven Earth-sized planets in a near-resonant chain, is a striking example. However, resonant configurations are fragile: after the gas disk dissipates and its damping influence vanishes, gravitational perturbations between planets can destabilize the chain. Many systems likely formed in resonance but broke out during a later phase of dynamical instability, scattering planets into the non-resonant orbits we observe in most mature planetary systems.
