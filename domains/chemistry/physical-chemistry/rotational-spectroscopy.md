---
id: rotational-spectroscopy
title: Rotational (Microwave) Spectroscopy
domain: chemistry
course: physical-chemistry
prerequisites:
- id: rigid-rotor-model
  type: hard
- id: selection-rules-spectroscopy
  type: hard
- id: rotational-kinematics
  type: soft
- id: electromagnetic-spectrum
  type: soft
- id: angular-momentum
  type: soft
builds-toward:
- vibrational-spectroscopy-theory
tags:
- microwave
- rotational-constant
- bond-length
- dipole-moment
- centrifugal-distortion
stage: advanced
status: validated
---

# Rotational (Microwave) Spectroscopy

## Core Idea
Rotational spectroscopy probes transitions between molecular rotational energy levels using microwave radiation (roughly 1–1000 GHz). For a rigid diatomic rotor, allowed transitions occur at frequencies ν = 2B(J+1) where J is the lower-state quantum number, producing a series of equally spaced lines separated by 2B. The rotational constant B = h/(8π²Ic) directly yields the moment of inertia and hence the bond length with high precision. Real spectra show centrifugal distortion (decreasing line spacing at high J) and require a permanent dipole moment for observation.

## How It's Best Learned
Simulate or analyze a diatomic microwave spectrum, extract B from line spacings, and calculate the bond length. Compare your result to known values to assess the accuracy of the rigid rotor approximation.

## Common Misconceptions
- Assuming all molecules show microwave spectra — homonuclear diatomics like N₂ have no dipole and are microwave-inactive.
- Forgetting that line spacings give 2B, not B.

## Questions

```yaml
- question: "A microwave spectrum of a diatomic molecule shows equally spaced absorption lines separated by 20.0 GHz. A student reports the rotational constant B as 20.0 GHz. What is wrong?"
  type: multiple-choice
  options:
    - "Nothing — the line spacing directly equals B"
    - "The spacing equals 2B, so B = 10.0 GHz; the student failed to divide by two"
    - "The spacing equals B/2, so B = 40.0 GHz; the student should have multiplied by two"
    - "B cannot be determined from line spacing alone — you also need the transition frequencies"
  answer: 1
  explanation: "For a rigid diatomic rotor, the transition frequency from J to J+1 is ν = 2B(J+1). The first line (J=0→1) is at 2B, the second at 4B, so adjacent lines are separated by 2B — not B. Dividing the observed spacing by 2 gives B. This is the most common numerical error in rotational spectroscopy problems."

- question: "Why does N₂ show no microwave absorption spectrum despite being a rotating diatomic molecule with well-defined rotational energy levels?"
  type: multiple-choice
  options:
    - "N₂ rotational energy levels are too closely spaced for microwave radiation to resolve"
    - "N₂'s rotational constant B is zero because both atoms have equal mass"
    - "N₂ is homonuclear and has no permanent dipole moment, so microwave radiation has no oscillating electric field component to couple to rotational transitions"
    - "N₂ absorbs in the infrared rather than the microwave region"
  answer: 2
  explanation: "The selection rule requires a permanent dipole moment: microwave radiation interacts with a molecule's rotating electric dipole. Homonuclear diatomics have identical atoms, so there is no charge separation and no dipole. The oscillating electric field of the microwave has nothing to 'grip.' N₂ has well-defined rotational levels but is microwave-inactive. HCl, CO, and other heteronuclear diatomics are microwave-active."

- question: "For a rigid diatomic rotor, the rotational constant B can be extracted directly from the spacing between adjacent lines in the microwave absorption spectrum."
  type: true-false
  answer: true
  explanation: "Adjacent lines are separated by 2B (since ν = 2B(J+1) and consecutive J values differ by 1). Measuring any adjacent pair and dividing by 2 gives B immediately. From B = h/(8π²Ic), you can extract the moment of inertia I, and from I = μr² you get the bond length r. This chain makes microwave spectroscopy the most precise structural technique for simple diatomics."

- question: "At high rotational quantum numbers J, centrifugal distortion causes the spacing between adjacent microwave absorption lines to increase."
  type: true-false
  answer: false
  explanation: "Centrifugal distortion causes the spacing to decrease at high J. As the molecule spins faster at higher J, centrifugal force stretches the bond, increasing the moment of inertia and decreasing the effective rotational constant. The corrected energy expression adds −D_J[J(J+1)]², which progressively reduces the transition frequencies at high J, compressing the line spacing."

- question: "Explain how a microwave spectrum of a diatomic molecule yields the bond length. What measurements and calculations are required?"
  type: short-answer
  answer: "Measure the spacing between any two adjacent absorption lines in the spectrum; this spacing equals 2B. Divide by 2 to get the rotational constant B. Use B = h/(8π²Ic) to calculate the moment of inertia I. For a diatomic, I = μr², where μ = m₁m₂/(m₁+m₂) is the reduced mass (known from atomic masses). Solving for r gives the bond length."
  explanation: "The directness of this chain — spectrum → B → I → r — is what makes rotational spectroscopy uniquely powerful for structural determination. Unlike vibrational or electronic spectroscopy, the bond length drops out with minimal modeling assumptions, giving precision to five or six significant figures."
```

## Explainer

You already know from the rigid rotor model that a diatomic molecule rotating in space has quantized energy levels E_J = BJ(J+1), where B = h/(8π²Ic) is the **rotational constant** and J is the rotational quantum number. Rotational spectroscopy is the experimental technique that measures transitions between these levels, using microwave radiation to drive the molecule from one rotational state to the next. The selection rules you studied tell you that allowed transitions require ΔJ = ±1 and — critically — the molecule must have a **permanent dipole moment**. This is why homonuclear diatomics like H₂ and N₂ are invisible to microwave spectroscopy: with no dipole, the oscillating electric field of the microwave radiation has nothing to grab onto.

For an absorption transition from J to J+1, the transition frequency is ν = 2B(J+1). This produces a beautifully simple pattern: the first line (J=0→1) appears at 2B, the second (J=1→2) at 4B, the third at 6B, and so on. The spectrum is a series of **equally spaced lines separated by 2B**. This uniform spacing is the hallmark of a rigid rotor spectrum, and it makes extracting B almost trivially easy — just measure the gap between adjacent lines and divide by two. From B you get the moment of inertia I = h/(8π²Bc), and from I you extract the bond length r since I = μr² for a diatomic, where μ is the reduced mass. This gives bond lengths with extraordinary precision, often to five or six significant figures.

Real molecules are not perfectly rigid, however. As J increases and the molecule spins faster, centrifugal force stretches the bond slightly, increasing the moment of inertia and decreasing the effective rotational constant. This effect is called **centrifugal distortion**, and it causes the line spacing to decrease gradually at high J values. The corrected energy expression adds a term −D_J[J(J+1)]², where D_J is the centrifugal distortion constant. In practice, D_J is much smaller than B (typically by a factor of 10⁴ or more), so the effect is subtle but measurable — and it actually provides additional information about the bond's stiffness.

The power of rotational spectroscopy lies in its directness: the spacing of microwave absorption lines maps almost one-to-one onto molecular geometry. Unlike electronic or vibrational spectroscopy, where extracting structural parameters requires modeling multiple interacting degrees of freedom, a microwave spectrum of a simple molecule gives you the bond length with minimal interpretation. For polyatomic molecules the analysis grows more complex — you need three rotational constants (A, B, C) for an asymmetric top — but the principle remains the same: rotational transitions reveal the mass distribution of the molecule with remarkable precision.
