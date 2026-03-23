---
id: binding-energy-stability-curve
title: Binding Energy and the Nuclear Stability Curve
domain: physics
course: modern-physics
prerequisites:
- id: mass-energy-equivalence-relativity
  type: hard
- id: strong-nuclear-force
  type: soft
builds-toward:
- spontaneous-radioactive-decay
tags:
- nuclear-physics
- energy
stage: advanced
status: validated
---

# Binding Energy and the Nuclear Stability Curve

## Core Idea
The binding energy BE = (Z·m_p + N·m_n − M)c² is the energy released in assembling a nucleus from free nucleons. Binding energy per nucleon BE/A is maximum (~8.8 MeV) near iron, declining for lighter and heavier nuclei. The stability curve plots N versus Z for stable nuclei: light nuclei have N ≈ Z, while heavy nuclei have N > Z (more neutrons) to reduce proton-proton repulsion. Nuclei far from this curve are unstable and undergo radioactive decay.

## How It's Best Learned
Calculate binding energies for a few nuclei using atomic mass tables. Plot binding energy per nucleon versus mass number to visualize the curve.

## Questions

```yaml
- question: "Both nuclear fusion (combining hydrogen into helium) and nuclear fission (splitting uranium) release energy, even though one combines nuclei and the other splits them. The unifying explanation is:"
  type: multiple-choice
  options:
    - "Both reactions produce lighter nuclei, and lighter nuclei always have more binding energy"
    - "Both reactions destroy neutrons, releasing the energy stored in neutron mass"
    - "Both reactions move product nuclei toward the peak of the binding energy per nucleon curve near iron, producing more tightly bound products"
    - "Fission releases energy because uranium is radioactive, while fusion releases energy because hydrogen has too few neutrons"
  answer: 2
  explanation: "The binding energy per nucleon curve peaks near iron (A ≈ 56). Light nuclei like hydrogen are on the left side of the peak; heavy nuclei like uranium are on the right. Fusion moves light nuclei up the left slope toward iron (more tightly bound products), releasing energy. Fission moves heavy nuclei down the right slope toward iron (more tightly bound fragments), also releasing energy. Both processes converge on iron from opposite sides. The unifying principle is that both reactions produce products with higher binding energy per nucleon than the starting material."

- question: "A massive star fuses hydrogen into helium, then helium into carbon, and so on up the periodic table until it builds up a core of iron. Why does fusion stop producing energy at iron?"
  type: multiple-choice
  options:
    - "Iron nuclei are too large for the strong nuclear force to bind any additional nucleons"
    - "Iron is chemically inert and its electrons prevent nuclei from getting close enough to fuse"
    - "Iron sits at the peak of the binding energy per nucleon curve; fusing or fissioning iron would produce less tightly bound products, requiring energy input rather than releasing it"
    - "Iron has too many neutrons relative to protons to undergo further fusion reactions"
  answer: 2
  explanation: "Iron (A ≈ 56) is at the bottom of the nuclear energy valley — the most tightly bound configuration of nucleons. Any reaction that moves nuclei away from iron (either toward lighter or heavier products) requires energy; any reaction toward iron releases energy. Stars 'fall downhill' toward iron during nucleosynthesis. Once the core is iron, there is no further energy to extract from nuclear reactions, and the core collapses under gravity — triggering a supernova."

- question: "Heavy stable nuclei (like lead or bismuth) have roughly equal numbers of protons and neutrons, just as light nuclei like helium-4 do."
  type: true-false
  answer: false
  explanation: "For light nuclei, N ≈ Z is stable. But for heavier nuclei, the stability curve curves above the N = Z line: heavy stable nuclei have more neutrons than protons. The reason is electrostatic repulsion: as Z increases, the cumulative proton-proton repulsion becomes substantial and destabilizes the nucleus. Extra neutrons provide additional strong-force binding without adding to the Coulomb repulsion, diluting the proton density. Bismuth-209 (the heaviest stable nucleus) has 83 protons and 126 neutrons. Nuclei on the N = Z line at high mass number are unstable and undergo beta-plus decay or proton emission."

- question: "The binding energy of a nucleus represents the energy that must be supplied to completely disassemble it into free, separated protons and neutrons."
  type: true-false
  answer: true
  explanation: "This is the definition: BE = (Z·m_p + N·m_n − M_nucleus)·c². The mass defect — the 'missing' mass of the assembled nucleus compared to its free constituents — has been converted into binding energy that holds the nucleus together. To reverse the process (disassemble the nucleus into free nucleons), you must supply exactly this energy. A larger binding energy means more tightly bound, more stable nucleus. The binding energy per nucleon (BE/A) allows comparison across nuclei of different sizes and is the quantity plotted on the stability curve."

- question: "Using the binding energy per nucleon curve, explain why a nuclear power plant (fissioning uranium) and the sun (fusing hydrogen) both extract energy from nuclear reactions, even though one splits nuclei and the other combines them."
  type: short-answer
  answer: "The binding energy per nucleon curve peaks near iron (A ≈ 56) at about 8.8 MeV/nucleon. Uranium (A ≈ 235) sits on the right side of the peak at a lower BE/A. When uranium fissions into two medium-weight fragments (near A ≈ 90-140), those fragments sit closer to the peak and have higher BE/A — the products are more tightly bound than the reactant. The difference in binding energy per nucleon is released as kinetic energy and radiation. Hydrogen (A = 1) sits far to the left of the peak at nearly zero BE/A. When hydrogen fuses to helium-4 (BE/A ≈ 7 MeV), the helium is much more tightly bound, releasing about 7 MeV per nucleon. Both reactions extract energy by moving toward the iron peak from opposite sides."
  explanation: "The key conceptual step is recognizing that 'more tightly bound' = lower mass (via mass defect = binding energy / c²). Reactions that produce more tightly bound products release the mass difference as energy. The curve is a map of nuclear stability, and both fission and fusion navigate downhill on this map toward iron."
```

## Explainer

Your prerequisite — mass-energy equivalence, E = mc² — tells you that mass and energy are interchangeable. When protons and neutrons bind together to form a nucleus, the resulting nucleus is *lighter* than the sum of its free parts. This "missing" mass, called the **mass defect**, has been converted into the binding energy that holds the nucleus together: BE = (Z·m_p + N·m_n − M_nucleus)·c². The binding energy is the energy you would need to supply to completely disassemble the nucleus into isolated protons and neutrons. A larger binding energy means a more tightly bound, more stable nucleus.

Dividing by the number of nucleons A gives the **binding energy per nucleon**, which is the most useful comparative quantity. When you plot BE/A against mass number A, you find a characteristic curve: it rises steeply from hydrogen (essentially zero), peaks near iron (A ≈ 56, BE/A ≈ 8.8 MeV), and then gradually declines for heavier nuclei out to uranium and beyond. Iron and nickel sit at the bottom of the energy valley — they are the most tightly bound nuclei in nature, the "ashes" of stellar nucleosynthesis that no further nuclear reaction can squeeze energy out of.

The shape of this curve directly explains nuclear fission and fusion. **Fusion** — combining light nuclei — releases energy because the product lies higher on the curve (more bound per nucleon) than the reactants: hydrogen fusing to helium gains roughly 7 MeV per nucleon. This is the energy source of stars. **Fission** — splitting heavy nuclei — also releases energy because the fragments land higher on the curve than the original heavy nucleus: uranium splitting into two medium-weight fragments releases about 0.9 MeV per nucleon. Both processes move nuclei toward the peak at iron. Once you reach iron, neither fusion nor fission releases energy.

The **stability curve** (N vs. Z for stable nuclei) tells a complementary story about which combinations of protons and neutrons are stable. For light nuclei, N ≈ Z: roughly equal numbers of each are needed. For heavier nuclei, the line curves above the N = Z diagonal — stable heavy nuclei have progressively more neutrons than protons. The reason: protons repel each other electrically, and for large Z this repulsion becomes substantial. Adding extra neutrons dilutes the proton density and supplies additional strong-force glue without adding to the electromagnetic repulsion. Nuclei that fall far from the stability curve are radioactive, decaying toward it by beta decay, alpha emission, or other processes.
