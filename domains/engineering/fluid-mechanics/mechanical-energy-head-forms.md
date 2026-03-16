---
id: mechanical-energy-head-forms
title: Mechanical Energy and Head Forms
domain: engineering
course: fluid-mechanics
prerequisites:
- id: energy-equation-steady-flow
  type: hard
builds-toward:
- pipe-flow-network-analysis
tags:
- energy
- head
- applications
stage: formal-systems
status: draft
---

# Mechanical Energy and Head Forms

## Core Idea
The total head H consists of elevation head (z), pressure head (P/ρg), and velocity head (V²/2g). In pipe flow, head loss represents mechanical energy converted to heat through friction and local resistance. The hydraulic grade line (HGL) shows pressure head variation along a pipe, while the energy grade line (EGL) accounts for velocity head changes.

## How It's Best Learned
Draw energy grade lines (EGL) and hydraulic grade lines (HGL) on pipe system sketches. Use piezometers along a pipe to measure actual pressure head at different locations and compare with calculated hydraulic grade line.

## Common Misconceptions
- Head is the same as pressure (head is pressure divided by ρg, with units of length; they are different but proportional).
- The hydraulic grade line is always parallel to the pipe (HGL is parallel to the energy grade line only when velocity is constant; they have different slopes when velocity changes).

## Explainer

From the energy equation for steady flow, you already know that the sum of pressure energy, kinetic energy, and potential energy is conserved along a streamline (with corrections for losses and work inputs). The **head form** of Bernoulli's equation divides every energy term by ρg, converting units from joules per kilogram (J/kg) into meters (m). This is not just a bookkeeping trick — expressing energy as a height of fluid column allows you to literally draw energy on a diagram, which makes pipe system analysis visual and intuitive.

The three components of total head H = z + P/(ρg) + V²/(2g) each have a clear physical meaning. The **elevation head** z is the potential energy per unit weight — how high the fluid sits. The **pressure head** P/(ρg) is the height of fluid column that would produce that pressure; it is what a vertical piezometer tube attached to the pipe wall would show. The **velocity head** V²/(2g) is the kinetic energy per unit weight — for typical pipe flows it is often a small fraction of the total, but in high-velocity sections (constrictions, nozzles) it becomes dominant.

The **energy grade line** (EGL) plots total head H = z + P/(ρg) + V²/(2g) along the pipe. In a frictionless flow with no pumps or turbines, the EGL is horizontal — total energy is conserved. In real flow, the EGL slopes downward in the direction of flow because **head loss** h_L converts mechanical energy into heat through viscous friction. At a pump, the EGL jumps upward by h_pump (energy added per unit weight of fluid); at a turbine, it drops by h_turbine. The **hydraulic grade line** (HGL) plots only z + P/(ρg), omitting velocity head. The EGL sits above the HGL by exactly V²/(2g), so the two lines are parallel only when velocity (and hence pipe cross-section) is constant.

These two lines are diagnostic tools. If the HGL drops below the pipe centerline, the gauge pressure is negative — the fluid is in tension, which physically means cavitation risk. A sudden drop in the EGL signals a local loss (valve, elbow, sudden expansion). A constriction raises velocity, so V²/(2g) grows and the HGL dips sharply even though the EGL drops only slightly. By sketching EGL and HGL on any pipe network, you can instantly identify where energy is being lost, where flow might cavitate, and whether pumps have enough head to push fluid to the desired elevation. This visual language is the practical power of the head representation.
