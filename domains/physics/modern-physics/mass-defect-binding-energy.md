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

## Questions

```yaml
- question: "A student argues: 'Fission of uranium releases energy. Therefore fusion of uranium would require energy input.' This reasoning is:"
  type: multiple-choice
  options:
    - "Correct — if splitting a nucleus releases energy, combining it with another must absorb the same energy"
    - "Correct in principle but wrong in detail — uranium fusion would release only a small amount of energy"
    - "Incorrect — it confuses the BE/A curve with a simple reversal principle; whether a reaction releases energy depends on whether it moves the products toward the iron-56 peak"
    - "Incorrect — fission of uranium actually requires energy input, not the reverse"
  answer: 2
  explanation: "The student's symmetry argument fails because nuclear energy release is not about reversal — it is about position on the BE/A curve. Uranium (A ≈ 235) sits to the right of the iron-56 peak with lower BE/A. Fission moves its fragments toward the peak, releasing energy. Light nuclei (H, He) sit to the left of the peak; fusion also moves products toward the peak, also releasing energy. Both processes release energy for opposite reasons: both move toward higher BE/A. The misconception is treating fission and fusion as simple reverses of each other."

- question: "The mass defect of a nucleus being Δm = 0.5 u means:"
  type: multiple-choice
  options:
    - "Half a proton's mass was permanently destroyed when the nucleus formed"
    - "The nucleus has 0.5 u more mass than the sum of its constituent nucleons"
    - "An energy of Δmc² was released when the nucleons bound together, and must be supplied to disassemble the nucleus"
    - "The nucleus is unstable and will spontaneously release 0.5 u of mass as radiation"
  answer: 2
  explanation: "Mass defect does not mean mass was destroyed — it was converted to binding energy (released when the nucleus formed, consistent with E = mc²). The nucleus has *less* mass than the sum of its parts by Δm, and the binding energy BE = Δmc² is what holds the nucleus together. This energy must be supplied to pull the nucleus apart. The nucleus is not unstable by virtue of having a mass defect — all stable nuclei have positive mass defects."

- question: "Heavy nuclei like uranium are more tightly bound per nucleon than iron-56, which is why they are so massive."
  type: true-false
  answer: false
  explanation: "The opposite is true. Iron-56 sits at the peak of the BE/A curve at approximately 8.8 MeV per nucleon — it is the most tightly bound nucleus. Uranium (A ≈ 235) has a lower BE/A of about 7.6 MeV per nucleon. Heavy nuclei are massive because they contain more nucleons, not because each nucleon is more tightly bound. Their lower BE/A is precisely why fission releases energy: moving to mid-mass fragments increases BE/A toward the iron peak."

- question: "The mass defect of a nucleus is a real, experimentally measurable quantity — not merely a theoretical prediction."
  type: true-false
  answer: true
  explanation: "Mass spectrometers can measure nuclear masses with extraordinary precision (to parts in a billion). The difference between the measured nuclear mass and the sum of the constituent nucleon masses — the mass defect — has been experimentally confirmed for thousands of nuclides. Binding energy values computed from these measurements agree with independent determinations from nuclear reaction energetics. Mass defect is one of the most precisely verified predictions of special relativity applied to nuclear systems."

- question: "Why does the BE/A curve having a peak at iron-56 mean that both nuclear fusion AND fission can release energy, depending on which nucleus is involved?"
  type: short-answer
  answer: "The BE/A curve measures how tightly bound the average nucleon is. Any nuclear process in which the products have higher BE/A than the reactants releases energy — because higher BE/A means less mass per nucleon, and the mass difference is released as energy (E = Δmc²). For nuclei lighter than iron-56, fusion combines them into a heavier product closer to the peak, increasing BE/A and releasing energy. For nuclei heavier than iron-56, fission splits them into mid-mass fragments closer to the peak, also increasing BE/A and releasing energy. Iron-56 itself cannot release energy from either process, because any change moves it away from the peak."
  explanation: "The common misconception is to think that if fission releases energy, fusion must require it (or vice versa). This reversal logic fails because it treats the curve as symmetric around iron. The curve is not symmetric — it rises steeply on the left (light nuclei side) and falls gradually on the right (heavy nuclei side). Both fusion of light nuclei and fission of heavy nuclei move products toward the peak, releasing energy. The peak is the energetic attractor, not a midpoint in a simple reversal."
```

## Explainer

Your prerequisite on mass-energy equivalence (E = mc²) gave you the conceptual foundation for understanding why mass and energy are interchangeable. Now apply it to a specific, measurable phenomenon: when protons and neutrons bind together to form a nucleus, the resulting system has less mass than the sum of its parts. This **mass defect** Δm = (Zm_p + Nm_n) − M_nucleus is real and measurable using mass spectrometers with extraordinary precision. Multiplying by c² converts it into the **binding energy** BE = Δmc² — the energy that was released when the nucleus formed, and the energy that must be supplied to pull it apart again.

Think of it by analogy with gravitational potential energy. Two masses far apart have more energy than two masses close together in a bound orbit (you had to supply energy to separate them). Similarly, free nucleons far apart have more rest energy than the same nucleons bound in a nucleus. The binding energy is the depth of the "nuclear potential well." The nuclear force (the strong force you've studied) holds nucleons together, and the binding energy quantifies the strength of that hold on a per-particle basis. A useful quantity is **binding energy per nucleon**, BE/A, which tells you how tightly the average nucleon is bound.

The BE/A curve as a function of mass number A is one of the most information-dense plots in physics. At low A (hydrogen through helium), BE/A rises steeply — small nuclei are loosely bound. The curve peaks around A ≈ 56 at approximately 8.8 MeV per nucleon — iron and nickel isotopes are the most tightly bound nuclei in existence. Beyond A ≈ 56, BE/A gradually decreases — heavy nuclei like uranium (A ≈ 235) are bound at only about 7.6 MeV per nucleon. This one curve determines which nuclear processes release energy and which require it.

The implications are immediate. For light nuclei (A < 56), **fusion** — combining them into a heavier nucleus — moves up the BE/A curve toward the peak, releasing energy. This is the power source of stars: hydrogen fuses to helium, releasing ~26 MeV per reaction. For heavy nuclei (A > 56), **fission** — splitting them into mid-size fragments — also moves up the BE/A curve toward the peak, releasing energy. When uranium-235 splits into barium and krypton, the products have higher BE/A than the original nucleus, and the energy difference (~200 MeV per fission event) is released as kinetic energy of fragments and radiation. Both fusion and fission are ultimately consequences of the shape of the BE/A curve — and the curve's shape is a consequence of the competition between the attractive nuclear force (which scales with volume, proportional to A) and the repulsive electrostatic force between protons (which scales more steeply with proton number Z). Iron is at the peak because it represents the optimal balance of these competing forces.
