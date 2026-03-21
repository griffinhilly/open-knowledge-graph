---
id: nuclear-mass-binding-energy
title: Nuclear Mass, Binding Energy, and the Mass-Energy Relation
domain: physics
course: modern-physics
prerequisites:
- id: mass-defect-binding-energy
  type: hard
- id: relativistic-kinetic-energy
  type: hard
builds-toward:
- alpha-decay-emission
tags:
- nuclear
- binding-energy
- mass-defect
stage: advanced
status: draft
---

# Nuclear Mass, Binding Energy, and the Mass-Energy Relation

## Core Idea
The nuclear binding energy is the energy released when nucleons (protons and neutrons) combine to form a nucleus: BE = (Zmp + Nmn − Mnucleus)c². Binding energy per nucleon peaks at iron-56, reflecting the strong nuclear force's strength and range. Nuclei lighter or heavier than iron are energetically unfavorable, driving fusion and fission processes.

## Questions

```yaml
- question: "A star fuses two carbon nuclei (A=12) to form magnesium (A=24). Does this reaction release or absorb energy, and why?"
  type: multiple-choice
  options:
    - "Absorbs energy — combining nuclei always costs energy"
    - "Releases energy — both carbon and magnesium are lighter than iron on the binding energy curve, so moving toward iron releases energy"
    - "Releases energy — magnesium has a higher total binding energy than two separate carbon nuclei"
    - "Absorbs energy — the product has more protons, increasing Coulomb repulsion"
  answer: 1
  explanation: "The key is binding energy *per nucleon*, not total binding energy. Both carbon and magnesium lie on the rising portion of the BE/A curve below the iron-56 peak. Fusing them moves the products closer to iron — up the curve — which releases energy equal to the mass difference times c². Option C tempts students who correctly note that Mg has more total binding energy, but the *reason* this releases energy is the per-nucleon gain, not just the total."

- question: "A student says 'uranium-238 is more stable than helium-4 because it has a much larger total binding energy.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — total binding energy is the correct measure of nuclear stability"
    - "Total binding energy grows with mass number, so it cannot distinguish stability; binding energy per nucleon shows that helium-4 is actually more tightly bound per nucleon than uranium-238"
    - "Uranium is actually more stable per nucleon because the strong force acts on more nucleons"
    - "The comparison is invalid because uranium and helium are in different decay chains"
  answer: 1
  explanation: "Total binding energy always increases with the number of nucleons — a uranium nucleus has 238 nucleons contributing. But stability depends on how tightly bound *each* nucleon is on average. Uranium-238 has a BE/A of about 7.6 MeV/nucleon, while helium-4 has about 7.1 MeV/nucleon and iron-56 has the maximum at 8.8 MeV/nucleon. The binding energy *curve* (BE/A vs. A) is the correct measure, and iron-56 sits at its peak."

- question: "A nucleus always has less mass than the sum of its free constituent protons and neutrons."
  type: true-false
  answer: true
  explanation: "This is the mass defect: when nucleons bind together, the energy released (the binding energy) comes at the cost of mass, precisely as E = mc² predicts. The bound nucleus is lighter than its separated parts because some mass has been converted to the energy that holds it together. There are no exceptions — every stable or long-lived nucleus has a positive binding energy and therefore a mass defect."

- question: "Heavier nuclei always have greater binding energy per nucleon than lighter nuclei."
  type: true-false
  answer: false
  explanation: "The binding energy per nucleon curve peaks at iron-56 (≈8.8 MeV/nucleon) and *decreases* for heavier nuclei. In heavy elements like uranium, the Coulomb repulsion between the many protons grows (∝Z²) while the short-range strong force cannot compensate at large nuclear radii, reducing the per-nucleon binding energy to about 7.6 MeV/nucleon. This is precisely why fission of heavy nuclei releases energy — the fragments are closer to the iron peak and more tightly bound per nucleon."

- question: "Why can both nuclear fusion (of light nuclei) and nuclear fission (of heavy nuclei) release energy, even though these processes seem like opposites?"
  type: short-answer
  answer: "Both processes move their products closer to the peak of the binding energy per nucleon curve at iron-56. Light nuclei (hydrogen, helium) are below the peak — fusing them increases binding energy per nucleon, releasing the mass difference as energy. Heavy nuclei (uranium, plutonium) are above the peak — splitting them produces fragments closer to iron with higher binding energy per nucleon, again releasing energy. Iron itself cannot release energy by either process because it sits at the top of the curve."
  explanation: "The binding energy curve is not monotonic — it has a single maximum at iron-56. Any nuclear reaction that moves products toward that peak releases energy; any reaction moving away from it requires energy. This single curve explains why stellar fusion terminates at iron (further fusion costs energy rather than releasing it), why fission reactors use heavy elements, and why fusion reactors need light isotopes like deuterium and tritium."
```

## Explainer

From relativistic kinetic energy, you know that mass and energy are equivalent: E = mc². This isn't just a curiosity — it's directly measurable in the nucleus. When protons and neutrons bind together, the resulting nucleus is *lighter* than the sum of its free constituents. This missing mass, the **mass defect**, has been converted into binding energy — the energy that holds the nucleus together against the electromagnetic repulsion of the protons and the tendency of the strong force to be short-ranged.

The binding energy formula BE = (Zmp + Nmn − Mnucleus)c² quantifies this. You add up the masses of Z free protons and N free neutrons, subtract the actual nuclear mass, and multiply by c² to get energy. For helium-4 (two protons, two neutrons), the mass defect is about 0.030 u, giving BE ≈ 28 MeV — or about 7 MeV per nucleon. The quantity **binding energy per nucleon** (BE/A) is the most informative ratio: it tells you how tightly bound each nucleon is, on average, in that nucleus.

The **binding energy curve** — BE/A plotted against mass number A — has a characteristic shape: it rises steeply from hydrogen (0 MeV/nucleon), peaks around iron-56 at about 8.8 MeV/nucleon, then decreases slowly for heavier elements. The peak at iron represents the most stable configuration: iron-56 is the "valley floor" of nuclear stability. Lighter nuclei are less tightly bound because the strong force hasn't yet had enough nucleons to reach its full binding strength — fusing them releases energy. Heavier nuclei are less tightly bound because proton-proton repulsion grows (Coulomb energy ∝ Z²), outcompeting the strong force which only acts at short range — splitting them (fission) releases energy.

This single curve explains the energy sources of the universe. **Stellar fusion** converts hydrogen to helium, then to heavier elements, releasing energy with every step up the binding curve toward iron. When a massive star exhausts its nuclear fuel at iron, fusion no longer releases energy and the star collapses. **Nuclear fission** in reactors and bombs exploits the downslope: uranium-235 splits into fragments near the iron peak, and the energy difference (roughly 200 MeV per fission) is released. In both cases, the liberated energy equals exactly the mass difference between reactants and products times c² — the same E = mc² you used for relativistic kinetic energy, now applied to the strong nuclear force rather than particle motion.
