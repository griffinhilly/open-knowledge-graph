---
id: big-bang-nucleosynthesis
title: Big Bang Nucleosynthesis and Primordial Abundances
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: hubble-law-and-cosmic-expansion
  type: hard
- id: nuclear-chemistry
  type: soft
- id: atomic-structure-and-atoms
  type: soft
builds-toward:
- cosmic-inflation-and-early-universe
tags:
- big-bang-nucleosynthesis
- primordial-abundances
- early-universe
stage: formal-systems
status: validated
---

# Big Bang Nucleosynthesis and Primordial Abundances

## Core Idea
Seconds after the Big Bang, the hot, dense early universe underwent nuclear fusion, creating primordial hydrogen, helium, and trace amounts of deuterium and lithium. Nucleosynthesis predictions depend sensitively on baryon density and the expansion rate, allowing observational tests of cosmological models and constraints on dark matter.

## Questions

```yaml
- question: "An astronomer observes a chemically pristine gas cloud that has never been processed through stars. What helium-4 mass fraction does BBN predict for this cloud?"
  type: multiple-choice
  options:
    - "Less than 5% — most helium is produced by stellar hydrogen burning, not the Big Bang"
    - "About 25% — the robust BBN prediction from the baryon-to-photon ratio"
    - "About 50% — protons and neutrons formed in roughly equal numbers, so half should become helium"
    - "Near 100% — helium-4 is the most stable light nucleus and the inevitable endpoint of fusion"
  answer: 1
  explanation: "BBN predicts ~75% hydrogen and ~25% helium by mass, determined almost entirely by the neutron-to-proton ratio at freeze-out (~1:7) and the baryon-to-photon ratio. This is not from stellar sources — stars add helium on top of this floor, but the primordial 25% sets the baseline. Option A describes a common misconception: stellar helium is real, but primordial helium is also substantial and observed in metal-poor environments."

- question: "Why is the primordial deuterium abundance a particularly powerful probe of cosmology?"
  type: multiple-choice
  options:
    - "Deuterium is the most abundant product of BBN, so small measurement errors matter less"
    - "Its abundance depends sensitively on the baryon-to-photon ratio, allowing precise constraints on total ordinary matter"
    - "Deuterium is only produced in the Big Bang, never in stars or interstellar space"
    - "Its nuclear binding energy uniquely fingerprints the temperature at BBN freeze-out"
  answer: 1
  explanation: "Deuterium is a stepping stone to helium-4: at higher baryon density, more deuterium gets converted to helium, leaving less behind. The surviving deuterium fraction changes by orders of magnitude across the plausible baryon density range, making it an exquisitely sensitive probe. Measuring deuterium in pristine quasar absorption systems pins down the baryon-to-photon ratio independently of the CMB — the agreement between these two measurements is one of the great concordances of modern cosmology."

- question: "The helium produced in Big Bang nucleosynthesis was eventually fused into heavier elements once the first stars ignited."
  type: true-false
  answer: false
  explanation: "Stellar nucleosynthesis does not 'use up' primordial helium — stars convert hydrogen to helium (adding to the pool) or fuse helium into carbon and heavier elements in later stages. But the bulk of primordial helium persists as helium-4. Observationally, the helium mass fraction in metal-poor dwarf galaxies (where stellar processing is minimal) clusters around 24–25%, confirming the primordial floor predicted by BBN rather than showing depletion."

- question: "The fact that BBN predictions fully account for all ordinary baryonic matter provides independent evidence from nuclear physics that dark matter must be non-baryonic."
  type: true-false
  answer: true
  explanation: "BBN predicts the total amount of baryonic matter from the baryon-to-photon ratio inferred by deuterium measurements. This baryonic density is only about 5% of the critical density — far less than the ~30% needed to explain galaxy rotation curves and large-scale structure. The missing mass cannot be baryonic (ordinary matter), so it must be some non-baryonic form of matter. This is a completely independent line of evidence for dark matter that doesn't rely on gravitational observations."

- question: "Why did Big Bang nucleosynthesis stop at light elements (H, He, Li) rather than building up to carbon, oxygen, and iron as stellar nucleosynthesis does?"
  type: short-answer
  answer: "Two factors halted BBN at light elements. First, there are no stable nuclei with mass numbers 5 or 8 — helium-5 and beryllium-8 decay almost instantly, blocking efficient pathways to heavier nuclei and creating a bottleneck. Stars bridge this gap with the triple-alpha process (three helium nuclei fusing to carbon-12) but only at the high densities and long timescales of stellar cores. Second, the universe expanded and cooled too rapidly — the window for nuclear fusion lasted only about 20 minutes before temperatures dropped below the threshold for further reactions. Stellar environments provide millions of years at high temperature and density, enabling the slow reactions that build heavy elements."
  explanation: "The mass-5 and mass-8 gaps are a consequence of nuclear structure, not Big Bang physics specifically. BBN's brief 20-minute window simply didn't allow time to bridge them. The distinct roles of BBN and stellar nucleosynthesis explain why hydrogen and helium are cosmically abundant while carbon, oxygen, and iron require stellar deaths to spread into the interstellar medium."
```

## Explainer

You know from Hubble's law that the universe is expanding, and running that expansion backward implies an early universe that was much hotter and denser than today. **Big Bang nucleosynthesis** (BBN) describes the brief window — roughly from 10 seconds to 20 minutes after the Big Bang — when temperatures were high enough for nuclear fusion but low enough for newly formed nuclei to survive. This is the period that set the chemical starting conditions for the entire universe.

Before nucleosynthesis began, the universe was a soup of protons, neutrons, electrons, and photons in thermal equilibrium. As the temperature dropped below about 10 billion kelvin, neutrons and protons began fusing. The process started with the simplest reaction: a proton and neutron combining to form **deuterium** (heavy hydrogen). Deuterium then served as a stepping stone to **helium-4**, the most stable light nucleus, through a chain of reactions. The process also produced small amounts of **helium-3**, **lithium-7**, and trace beryllium. Crucially, the lack of stable nuclei at mass 5 and mass 8 created a bottleneck — there was no efficient pathway to build heavier elements. By about 20 minutes after the Big Bang, the universe had cooled too much for further fusion, and the process froze out.

The resulting abundances are remarkably specific: roughly 75% hydrogen and 25% helium by mass, with deuterium at about one part in 30,000 and lithium-7 at roughly one part in 10 billion. These predictions depend almost entirely on a single free parameter — the **baryon-to-photon ratio**, which measures how much ordinary matter exists relative to radiation. A higher baryon density means more collisions, faster deuterium processing, and slightly more helium. The sensitivity of deuterium abundance to baryon density makes it an especially precise cosmological probe: measuring primordial deuterium in distant gas clouds pins down the total amount of ordinary matter in the universe.

The agreement between BBN predictions and observations is one of the strongest pieces of evidence for the hot Big Bang model. The predicted helium abundance matches what astronomers measure in the most chemically pristine regions of the universe. The deuterium measurements from quasar absorption spectra independently confirm the baryon density derived from the cosmic microwave background. This concordance also constrains what the universe *cannot* be made of: since BBN accounts for all the ordinary (baryonic) matter, any additional mass needed to explain galaxy rotation curves and large-scale structure must be non-baryonic — providing independent evidence for **dark matter** from nuclear physics alone.
