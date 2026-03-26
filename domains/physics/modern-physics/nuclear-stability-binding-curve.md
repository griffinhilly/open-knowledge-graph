---
id: nuclear-stability-binding-curve
title: Nuclear Stability and the Binding Energy per Nucleon Curve
domain: physics
course: modern-physics
prerequisites:
- id: mass-defect-binding-energy
  type: hard
builds-toward:
- nuclear-shell-model-magic-numbers
tags:
- nuclear-physics
- stability
- binding
stage: advanced
status: validated
---

# Nuclear Stability and the Binding Energy per Nucleon Curve

## Core Idea
The binding energy per nucleon BE/A increases from light nuclei, peaks near ⁵⁶Fe (~8.8 MeV per nucleon), and decreases for heavy nuclei. Nuclei near the peak are most stable. Light nuclei prefer equal numbers of protons and neutrons (N ≈ Z), while heavy stable nuclei have more neutrons than protons (due to Coulomb repulsion). Nuclei far from the stability valley are radioactive.

## How It's Best Learned
Plot the valley of beta stability (N vs Z for stable isotopes) and compare with the binding energy curve. Explain why fusion of light nuclei and fission of heavy nuclei both release energy.

## Common Misconceptions
The most abundant element (iron) is not necessarily the most abundant in the universe (iron-56 is most tightly bound, but helium is more abundant due to primordial nucleosynthesis). Instability is not sudden; nuclei gradually decay as they move away from the stability line.

## Questions

```yaml
- question: "A student argues that fission releases energy because heavy nuclei 'break apart,' releasing stored energy like a compressed spring, while fusion releases energy because small nuclei 'snap together.' What is fundamentally wrong with this explanation?"
  type: multiple-choice
  options:
    - "It is incorrect about fusion — fusion absorbs energy rather than releasing it"
    - "It incorrectly implies the two processes have different underlying reasons for releasing energy; both release energy for the same reason: the products are more tightly bound per nucleon than the reactants, so both reactions move nuclei toward the peak of the binding energy curve"
    - "It overstates the energy released by fission — fission is less energetic per nucleon than fusion"
    - "It ignores the role of neutrons, which must be emitted in both processes to conserve baryon number"
  answer: 1
  explanation: "Both fusion and fission release energy for the same underlying reason: the products sit higher on the BE/A curve (are more tightly bound per nucleon) than the reactants. Fusion of light nuclei climbs the left slope toward iron; fission of heavy nuclei slides down the right slope toward iron. In both cases, the products are more stable — more tightly bound — and the energy difference is released. The 'spring' and 'snap' analogy treats them as opposite phenomena when they are actually the same phenomenon applied to opposite ends of the same curve."

- question: "Why do stable heavy nuclei like lead (Pb, Z=82) have a neutron-to-proton ratio much greater than 1, while stable light nuclei like carbon-12 (Z=6) have N ≈ Z?"
  type: multiple-choice
  options:
    - "Heavy nuclei are formed by neutron-capture processes in stars and simply retain the excess neutrons from their formation"
    - "Neutrons contribute strong nuclear force but no Coulomb repulsion, so extra neutrons compensate for the growing long-range proton-proton repulsion as the nucleus enlarges"
    - "Heavy nuclei require more neutrons to maintain the correct nuclear density for the strong force to operate"
    - "The strong force acts only between neutrons in heavy nuclei, while proton-proton interactions are mediated by different forces"
  answer: 1
  explanation: "As nuclei grow larger, Coulomb repulsion — which is long-range and acts between every pair of protons — grows faster than the binding gain from the short-range strong force. Protons repel each other throughout the nucleus; neutrons do not. Adding extra neutrons increases the strong-force binding without adding any Coulomb penalty, partially counteracting the destabilizing proton repulsion. For light nuclei, Coulomb repulsion is small enough that N ≈ Z suffices. For very heavy nuclei, no ratio of N/Z fully compensates, which is why elements beyond bismuth have no stable isotopes."

- question: "Both nuclear fusion of light elements and fission of heavy elements release energy because both reactions produce nuclei with higher binding energy per nucleon than the starting material."
  type: true-false
  answer: true
  explanation: "The BE/A curve peaks near iron-56. Fusion of light nuclei (moving up the left slope) and fission of heavy nuclei (moving down the right slope) both move reactants toward the peak — toward more tightly bound configurations. When the products are more tightly bound per nucleon than the reactants, the excess binding energy is released. This single principle — 'moving toward iron releases energy' — unifies the explanation of both processes. Stars burn hydrogen to helium to carbon, etc., releasing energy at each step up the left slope; the sun ultimately derives its power from this ascent."

- question: "Iron-56 is the most abundant element in the universe because it is the most tightly bound nucleus — once stars produce iron, they can seldom produce anything more stable."
  type: true-false
  answer: false
  explanation: "This conflates stability with cosmic abundance. Hydrogen and helium are far more abundant than iron in the universe, because the Big Bang produced mostly hydrogen and helium (primordial nucleosynthesis), and stars have not had time to convert all of it to heavier elements. Iron is indeed the most tightly bound common nucleus, and a star that has fused its core to iron can release no further nuclear energy — this is why massive stars collapse when their iron core exceeds the Chandrasekhar limit. But 'most tightly bound' does not mean 'most cosmically abundant.'"

- question: "Why is iron-56 called the 'thermodynamic endpoint' of nuclear burning? What does this mean for the energy a star can extract from nuclear reactions?"
  type: short-answer
  answer: "Iron-56 sits at the peak of the BE/A curve — it has the highest binding energy per nucleon of any common nucleus. All nuclear reactions that release energy move nuclei toward iron: fusion of lighter elements climbs the left slope toward the peak, and fission of heavier elements descends the right slope toward the peak. Once a stellar core has been converted to iron-56, no further nuclear reaction can release energy — any fusion of iron would climb back down the left slope (absorbing energy rather than releasing it), and iron is too stable to fission spontaneously. At this point, the star's nuclear energy source is exhausted."
  explanation: "'Thermodynamic endpoint' means the state from which no further spontaneous energy release is possible — the nuclear analog of chemical equilibrium. For massive stars, reaching an iron core triggers gravitational collapse because there is no longer an energy source to support the star against its own gravity. The binding energy curve thus sets an absolute limit on stellar nuclear energy generation: you can fuse or fission your way toward iron, but you cannot go further."
```

## Explainer

You already know from mass defect and binding energy that assembling a nucleus releases energy — the total mass of the nucleus is less than the sum of its parts, and the "missing" mass appears as binding energy via E = mc². The **binding energy per nucleon**, BE/A, is the average energy that would be needed to remove a single nucleon from the nucleus. It is a measure of how tightly bound each nucleon is on average, and it varies dramatically across the periodic table.

The **binding energy curve** — a plot of BE/A versus mass number A — has a characteristic shape: it rises steeply from hydrogen (essentially zero, since ¹H is just a proton), passes through a hump in the light elements, continues rising more gradually, peaks near **⁵⁶Fe at about 8.8 MeV per nucleon**, and then gently falls for heavier nuclei. The peak represents the most stable nuclei: iron-56 holds its nucleons together most tightly per particle. This is the nuclear "valley floor" — nuclei on either side are less stable and will release energy by moving toward iron.

The shape of the curve reflects two competing forces. The **strong nuclear force** is short-range and attractive, acting between any pair of neighboring nucleons. Adding more nucleons increases binding, but only up to the range of the force — beyond about A ~ 60, new nucleons don't "see" all the other nucleons. Meanwhile, the **Coulomb repulsion** between protons is long-range: every proton repels every other proton throughout the nucleus regardless of size. For large A, the Coulomb penalty grows faster than the strong-force gain, which is why BE/A decreases for heavy nuclei and why heavy stable nuclei need more neutrons than protons (neutrons contribute strong force but no Coulomb repulsion).

The practical consequences of the curve's shape explain both fusion and fission as energy sources. **Fusion** of light nuclei (H → He or He → C) moves up the left slope of the curve toward higher BE/A, releasing the difference in binding energy per nucleon times the number of nucleons involved. **Fission** of heavy nuclei (uranium → barium + krypton, roughly) moves down the right slope toward higher BE/A, again releasing energy. Both processes move nuclei *toward* iron — both release energy for the same underlying reason: the products are more tightly bound per nucleon than the reactants. Iron-56 is the thermodynamic endpoint of all nuclear burning; a star made entirely of iron-56 could release no further nuclear energy.
