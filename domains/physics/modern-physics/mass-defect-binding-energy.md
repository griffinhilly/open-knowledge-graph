---
id: mass-defect-binding-energy
title: Mass Defect and Nuclear Binding Energy
domain: physics
course: modern-physics
prerequisites:
- id: mass-energy-equivalence
  type: hard
- id: nuclear-force-binding-mechanism
  type: hard
builds-toward:
- nuclear-stability-binding-curve
tags:
- nuclear-physics
- binding-energy
- mass-energy
stage: advanced
status: draft
---

# Mass Defect and Nuclear Binding Energy

## Core Idea
The mass of a nucleus is less than the sum of its constituent nucleon masses by the mass defect Δm. The binding energy is BE = Δm c². This energy must be supplied to disassemble the nucleus into individual nucleons. Binding energy per nucleon BE/A varies with A, peaking around A ≈ 56 (iron), indicating that iron-56 is the most tightly bound nucleus.

## How It's Best Learned
Calculate mass defects and binding energies for light and heavy nuclei using atomic mass tables. Plot BE/A versus A and identify the peak. Relate to fusion and fission energy release.

## Common Misconceptions
The mass defect is not zero for any nucleus (even hydrogen-1, the proton, has a well-defined internal structure). Heavy nuclei have lower binding energy per nucleon than intermediate-mass nuclei, making fission energetically favorable.

## Explainer

Your prerequisite on mass-energy equivalence (E = mc²) gave you the conceptual foundation for understanding why mass and energy are interchangeable. Now apply it to a specific, measurable phenomenon: when protons and neutrons bind together to form a nucleus, the resulting system has less mass than the sum of its parts. This **mass defect** Δm = (Zm_p + Nm_n) − M_nucleus is real and measurable using mass spectrometers with extraordinary precision. Multiplying by c² converts it into the **binding energy** BE = Δmc² — the energy that was released when the nucleus formed, and the energy that must be supplied to pull it apart again.

Think of it by analogy with gravitational potential energy. Two masses far apart have more energy than two masses close together in a bound orbit (you had to supply energy to separate them). Similarly, free nucleons far apart have more rest energy than the same nucleons bound in a nucleus. The binding energy is the depth of the "nuclear potential well." The nuclear force (the strong force you've studied) holds nucleons together, and the binding energy quantifies the strength of that hold on a per-particle basis. A useful quantity is **binding energy per nucleon**, BE/A, which tells you how tightly the average nucleon is bound.

The BE/A curve as a function of mass number A is one of the most information-dense plots in physics. At low A (hydrogen through helium), BE/A rises steeply — small nuclei are loosely bound. The curve peaks around A ≈ 56 at approximately 8.8 MeV per nucleon — iron and nickel isotopes are the most tightly bound nuclei in existence. Beyond A ≈ 56, BE/A gradually decreases — heavy nuclei like uranium (A ≈ 235) are bound at only about 7.6 MeV per nucleon. This one curve determines which nuclear processes release energy and which require it.

The implications are immediate. For light nuclei (A < 56), **fusion** — combining them into a heavier nucleus — moves up the BE/A curve toward the peak, releasing energy. This is the power source of stars: hydrogen fuses to helium, releasing ~26 MeV per reaction. For heavy nuclei (A > 56), **fission** — splitting them into mid-size fragments — also moves up the BE/A curve toward the peak, releasing energy. When uranium-235 splits into barium and krypton, the products have higher BE/A than the original nucleus, and the energy difference (~200 MeV per fission event) is released as kinetic energy of fragments and radiation. Both fusion and fission are ultimately consequences of the shape of the BE/A curve — and the curve's shape is a consequence of the competition between the attractive nuclear force (which scales with volume, proportional to A) and the repulsive electrostatic force between protons (which scales more steeply with proton number Z). Iron is at the peak because it represents the optimal balance of these competing forces.
