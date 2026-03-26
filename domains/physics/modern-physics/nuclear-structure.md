---
id: nuclear-structure
title: Nuclear Structure and Binding Energy
domain: physics
course: modern-physics
prerequisites:
- id: electric-charge-and-coulombs-law
  type: hard
- id: bohr-model
  type: soft
- id: mass-energy-equivalence
  type: soft
builds-toward:
- radioactive-decay
- nuclear-fission-fusion
tags:
- nuclear
- protons
- neutrons
- binding-energy
- strong-force
- mass-defect
stage: advanced
status: validated
---

# Nuclear Structure and Binding Energy

## Core Idea
Atomic nuclei consist of protons and neutrons (nucleons) bound by the strong nuclear force, which is short-range and much stronger than electrostatic repulsion. The mass of a nucleus is less than the sum of its constituent nucleon masses; the difference, converted via E = Δmc², is the binding energy holding the nucleus together. Binding energy per nucleon peaks near iron (A ≈ 56) and decreases for both lighter and heavier nuclei — this is why energy is released in both fusion (combining light nuclei) and fission (splitting heavy ones).

## How It's Best Learned
Calculate the mass defect and binding energy of deuterium and helium-4 numerically. Plot binding energy per nucleon versus mass number to see the iron peak. Discuss the competition between the strong force (attractive, short-range) and Coulomb repulsion (repulsive, long-range).

## Common Misconceptions
- The nucleus is held together by electrons — electrons are in orbitals outside the nucleus; it is the strong force that binds nucleons.
- Heavier nuclei are always more stable — stability peaks at iron; both very heavy and very light nuclei have lower binding energy per nucleon and can release energy by moving toward iron.

## Questions

```yaml
- question: "Why does nuclear fission of uranium-235 release energy, given that fusion of hydrogen isotopes also releases energy — even though fission splits and fusion combines?"
  type: multiple-choice
  options: ["Both processes produce fast neutrons, and the kinetic energy of those neutrons is the released energy", "Both fission and fusion move product nuclei toward lower binding energy per nucleon, releasing the difference as kinetic energy", "Both fission and fusion move product nuclei toward higher binding energy per nucleon, approaching the stability peak near iron, and the binding energy difference is released", "Fission releases energy by breaking electron bonds; fusion releases energy by creating new proton-neutron bonds"]
  answer: 2
  explanation: "Binding energy per nucleon peaks near iron (A ≈ 56). Heavy nuclei like uranium have lower binding energy per nucleon than iron; splitting them produces mid-mass fragments closer to the iron peak — higher binding energy per nucleon — and the energy difference is released. Light nuclei like hydrogen also have lower binding energy per nucleon than iron; fusing them produces helium, which is closer to the peak. In both cases, the products are more tightly bound, and that extra binding energy is released."

- question: "Heavier nuclei generally have greater binding energy per nucleon than lighter nuclei, which is why larger atoms tend to be more stable."
  type: true-false
  answer: false
  explanation: "Binding energy per nucleon is not monotonically increasing with mass number. It rises steeply for the lightest nuclei, peaks near iron-56, and then gradually declines for heavier nuclei. This means very heavy nuclei (like uranium) and very light nuclei (like hydrogen) both have lower binding energy per nucleon than iron. The stability peak is at iron, not at the heaviest element."

- question: "What is the 'mass defect' of a nucleus, and how does it connect to nuclear binding energy?"
  type: short-answer
  answer: "The mass defect is the difference between the sum of the masses of a nucleus's individual protons and neutrons (measured separately) and the actual measured mass of the assembled nucleus. The nucleus is always lighter than the sum of its parts. By E = mc², this missing mass corresponds to energy — specifically, the binding energy that was released when the nucleons came together and that would need to be supplied to pull them apart again."
  explanation: "This is a direct application of mass-energy equivalence. When nucleons bind together, energy is released to the environment (in the form of gamma rays, for instance), and the system's total mass decreases by a corresponding amount. The binding energy is therefore 'stored' as missing mass. A larger mass defect means a more tightly bound nucleus. Calculating Δm and multiplying by c² gives the total binding energy; dividing by the number of nucleons gives binding energy per nucleon."
```

## Explainer

You have already studied Coulomb's law — the electrostatic repulsion between like charges — and mass-energy equivalence, E = mc². Nuclear structure is where both come into play simultaneously, and understanding it requires holding two competing forces in mind at once. Inside a nucleus, protons are packed into a volume roughly 100,000 times smaller than the atom itself. Coulomb repulsion between them is enormous. The fact that nuclei hold together at all means something must overcome that repulsion — and it does: the strong nuclear force.

The strong nuclear force is short-range (it operates only within about 1–2 femtometers, roughly the size of a nucleon) and is far more powerful than electrostatic repulsion at those distances. It acts attractively between any two nucleons — proton-proton, neutron-neutron, or proton-neutron — regardless of charge. Neutrons contribute to binding without adding to the Coulomb repulsion, which is why heavier stable nuclei have an increasing ratio of neutrons to protons: extra neutrons supply additional strong-force attraction to hold the growing number of protons together. Beyond a certain size, however, even this trick fails — nuclei heavier than lead or bismuth are all unstable to some form of radioactive decay.

When nucleons assemble into a nucleus, the assembled nucleus is measurably lighter than the sum of its constituent masses measured separately. This is the mass defect, Δm. By Einstein's mass-energy equivalence, that missing mass corresponds to energy that was released when the nucleus formed — or equivalently, to the energy you would need to supply to pull the nucleus apart into free nucleons. This energy is the binding energy: BE = Δmc². A nucleus with a large mass defect is tightly bound and takes a lot of energy to disassemble. Binding energy per nucleon (BE divided by A, the mass number) is the most useful measure of nuclear stability — it tells you how tightly each nucleon is held, on average.

Plotting binding energy per nucleon against mass number A reveals a striking shape: it rises steeply for the lightest nuclei, peaks near iron-56 (at about 8.8 MeV per nucleon), and then gradually declines for heavier nuclei. Iron-56 is the most tightly bound nucleus per nucleon. This curve is the key to understanding nuclear energy release. Any nuclear reaction that moves nuclei toward the iron peak releases energy, because the products are more tightly bound than the reactants. Heavy nuclei like uranium are on the right side of the peak — splitting them (fission) produces mid-mass fragments closer to iron, with higher binding energy per nucleon, releasing the difference. Light nuclei like hydrogen and helium are on the left side of the peak — fusing them (fusion) produces heavier nuclei closer to iron, again releasing the difference.

The common misconception is that heavier always means more stable. It does not: stability peaks at iron. Both uranium (too heavy) and hydrogen (too light) are 'climbing toward iron' when they undergo fission and fusion respectively, and it is that climb — the gain in binding energy per nucleon — that powers nuclear reactors and stars. The Sun fuses hydrogen to helium; massive stars eventually reach iron in their cores and stop, because there is no more energy to be gained by nuclear reactions beyond that point.
