---
id: bifurcation-analysis-ode
title: Bifurcation Analysis in ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: autonomous-equations-phase-lines
  type: hard
- id: implicit-differentiation
  type: soft
builds-toward:
- linearization-nonlinear-systems
tags:
- bifurcation
- parameter-variation
- dynamical-systems
stage: advanced
status: draft
---

# Bifurcation Analysis in ODEs

## Core Idea
Bifurcation occurs when a small change in a parameter causes qualitative changes in solution behavior. Common types include saddle-node (equilibria collide and annihilate), transcritical (equilibria exchange stability), and pitchfork (one stable state splits into two). Bifurcation analysis reveals how systems transition between regimes as parameters vary.

## Questions

```yaml
- question: "For dx/dt = r + x², a student calculates that the equilibria are x = ±1 when r = −1, and x = ±2 when r = −4. The student concludes that as r increases the equilibria simply move closer together. Why is this conclusion incomplete?"
  type: multiple-choice
  options:
    - "The student's arithmetic is incorrect — the equilibria don't actually move as r varies"
    - "The student correctly describes quantitative changes but misses the qualitative event: at r = 0 the two equilibria collide and annihilate, and for r > 0 there are no real equilibria at all — this saddle-node bifurcation is a qualitative change in the phase portrait, not just a quantitative shift"
    - "The student should track equilibrium stability rather than position, which tells the complete story"
    - "The equilibria approach each other indefinitely but never actually meet for any finite value of r"
  answer: 1
  explanation: "The student's calculation is correct as far as it goes, but misses the essential point of bifurcation analysis: what happens at r = 0. The two equilibria (one stable, one unstable) collide into a single non-isolated equilibrium, then disappear entirely for r > 0. This is not just the equilibria moving — it is the global qualitative structure of the phase portrait changing. For r > 0, any initial condition flows off to infinity with no equilibria to attract or repel it. Seeing only the quantitative trend misses this transition."

- question: "In the transcritical bifurcation dx/dt = rx − x², two equilibria exist for all values of r. What happens at r = 0?"
  type: multiple-choice
  options:
    - "Both equilibria disappear temporarily, then reappear as r moves away from zero"
    - "The equation has only one equilibrium at r = 0 because x = 0 and x = r coincide"
    - "A new third equilibrium appears between the original two"
    - "The two equilibria coincide at x = 0 and exchange stability — the equilibrium that was stable becomes unstable, and the one that was unstable becomes stable"
  answer: 3
  explanation: "At r = 0, the two equilibria x = 0 and x = r both sit at x = 0 — they coincide but do not annihilate. For r < 0, x = 0 is stable and x = r (negative) is unstable. For r > 0, x = r is now positive and stable, and x = 0 has become unstable. At r = 0 they swap roles — this exchange of stability is the defining feature of the transcritical bifurcation, distinguishing it from the saddle-node where equilibria actually cease to exist."

- question: "In a bifurcation diagram, solid curves represent stable equilibria and dashed curves represent unstable equilibria, allowing the entire qualitative structure of a parametric family to be read from a single picture."
  type: true-false
  answer: true
  explanation: "The bifurcation diagram is a powerful compression tool: the horizontal axis shows the parameter value, the vertical axis shows equilibrium positions, and the solid/dashed distinction encodes stability. Without this diagram, you would need to draw a separate phase line for each parameter value to determine how many equilibria exist and which are stable. The bifurcation diagram shows all of this simultaneously, making the saddle-node fold, the transcritical crossing, and the pitchfork split immediately visible as geometric features."

- question: "A bifurcation is simply a large quantitative change in equilibrium position — it occurs when a parameter change moves an equilibrium value by more than some threshold amount."
  type: true-false
  answer: false
  explanation: "A bifurcation is a qualitative change in the phase portrait: the number of equilibria changes, or their stability type changes, at a precise critical parameter value. The size of the parameter change and the size of the equilibrium shift are irrelevant. You can have arbitrarily large shifts in equilibrium position with no bifurcation (purely quantitative change), and bifurcations can occur with infinitesimally small parameter perturbations from the critical value. The concept is about topological structure — what the phase line looks like — not about magnitude."

- question: "What is the qualitative difference between a saddle-node bifurcation and a transcritical bifurcation? How would you distinguish them on a bifurcation diagram?"
  type: short-answer
  answer: "In a saddle-node bifurcation, two equilibria (one stable, one unstable) approach each other as the parameter changes, collide at the bifurcation value, and then cease to exist — for parameter values beyond the bifurcation point, that region of the phase line has no equilibria. On the bifurcation diagram this looks like a fold or parabola: a solid branch and a dashed branch meet at a turning point, and for parameter values beyond the fold there is no curve at all. In a transcritical bifurcation, two equilibria always exist but pass through each other at the bifurcation value and exchange stability. On the bifurcation diagram this looks like two crossing lines (an X): one branch switches from solid to dashed and the other from dashed to solid at the crossing, but both branches continue past the intersection."
  explanation: "The practical consequence differs importantly: past a saddle-node bifurcation, initial conditions that previously settled to a stable equilibrium now diverge to infinity (or to some other attractor). Past a transcritical bifurcation, the stable equilibrium is still present — just at a different location. This distinction matters for understanding hysteresis and tipping points in applied models."
```

## Explainer

From your work on autonomous equations and phase lines, you know how to classify a fixed point as stable or unstable based on whether the phase line arrows point toward it or away from it. That analysis was done for a given equation. Bifurcation analysis asks a deeper question: what happens to the structure of the phase line — the number and stability of equilibria — as a **parameter** in the equation varies continuously? Sometimes the answer is "nothing changes"; sometimes crossing a critical parameter value causes the entire qualitative picture to reorganize.

The simplest example is the **saddle-node bifurcation**. Consider dx/dt = r + x². The equilibria satisfy r + x² = 0, so x = ±√(−r). When r < 0, two equilibria exist: a stable one at x = −√(−r) and an unstable one at x = +√(−r). As r increases toward zero, these two equilibria approach each other. At r = 0 they collide into a single non-isolated equilibrium at x = 0. For r > 0, there are no real equilibria at all — the phase line is now a single arrow pointing in one direction, and any initial condition flows off to infinity. Two equilibria appeared from nowhere (or vanished), which is the defining signature of a saddle-node bifurcation.

In a **transcritical bifurcation**, two equilibria always exist but exchange stability as the parameter crosses a critical value. The canonical form is dx/dt = rx − x². The equilibria are x = 0 and x = r. When r < 0, x = 0 is stable and x = r (negative) is unstable; when r > 0, x = r is stable and x = 0 is unstable. They swap roles at r = 0 when they coincide. The **pitchfork bifurcation** is the symmetric version: at the critical parameter value, one stable equilibrium splits into two stable ones with an unstable one between them (supercritical pitchfork), or one unstable equilibrium spawns two unstable flankers and a stable center disappears (subcritical). Pitchfork bifurcations arise naturally in systems with left-right symmetry.

The primary tool for visualizing this is the **bifurcation diagram**: plot the parameter r on the horizontal axis and the equilibrium values on the vertical axis. Solid curves indicate stable branches; dashed curves indicate unstable branches. The saddle-node bifurcation looks like a parabola — the two branches meet at a fold point. The transcritical looks like a crossing X. The supercritical pitchfork looks like a pitchfork tine splitting from a single stem. Reading the bifurcation diagram tells you instantly how many equilibria exist for any parameter value, and whether they are stable — information that would require re-drawing the phase line separately for each parameter value otherwise.
