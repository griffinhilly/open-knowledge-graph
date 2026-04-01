---
id: time-resolved-structural-methods
title: Time-Resolved Structural Methods
domain: biology
course: structural-biology
prerequisites:
- id: x-ray-crystallography
  type: hard
- id: cryo-em
  type: hard
- id: molecular-dynamics-simulations
  type: soft
builds-toward: []
tags:
- XFEL
- serial-crystallography
- pump-probe
- time-resolved-cryo-EM
- structural-dynamics
- femtosecond
stage: expert
status: validated
---
# Time-Resolved Structural Methods

## Core Idea
Time-resolved structural methods capture macromolecular structures at defined time points during a biological process, providing atomic-resolution movies of conformational changes, catalytic cycles, and ligand binding. Standard crystallography and cryo-EM produce static, time-averaged structures — they reveal where atoms are but not how they move. Time-resolved approaches overcome this limitation through several strategies: **serial femtosecond crystallography (SFX)** at X-ray free-electron lasers (XFELs) collects diffraction from microcrystals before radiation damage occurs (the "diffraction-before-destruction" principle), enabling room-temperature structures and pump-probe experiments where a light pulse or substrate triggers the reaction and the XFEL pulse captures the structure at a defined delay time. **Time-resolved cryo-EM** captures intermediates by rapid mixing or photolysis followed by plunge-freezing at controlled time points. These methods have revealed catalytic intermediates in enzymes, light-driven conformational changes in photoreceptors, and the structural dynamics of molecular machines in real time.

## Questions

```yaml
- question: "What is the 'diffraction-before-destruction' principle at an XFEL, and why does it enable room-temperature crystallography?"
  type: multiple-choice
  options:
    - "The crystal is protected from radiation by a special coating"
    - "XFEL pulses are so intense (10^12 photons in ~10-50 femtoseconds) that the crystal diffracts before the radiation damage cascade destroys it. The pulse is shorter than the time needed for atomic motion in response to ionization (~100 femtoseconds), so the diffraction pattern captures the undamaged structure. This eliminates the need for cryogenic cooling (which standard crystallography uses to slow radiation damage), enabling data collection at room temperature where proteins occupy their physiologically relevant conformational ensemble"
    - "The XFEL uses low-energy X-rays that do not damage the crystal"
    - "Each crystal is imaged many times before it is destroyed"
  answer: 1
  explanation: "In conventional crystallography at synchrotrons, X-ray exposure progressively damages the crystal (breaking disulfide bonds, decarboxylating glutamates, reducing metal centers). Cryogenic cooling (100 K) slows this damage, allowing data collection but trapping the protein in a cryo-artifact conformational state. XFEL pulses are ~10^9 times brighter than synchrotron beams but last only 10-50 femtoseconds. The crystal is completely vaporized by each pulse, but the diffraction pattern is recorded before the atoms have time to move — the Coulomb explosion happens after the diffraction is complete. Each crystal gives one diffraction pattern (one orientation), so data from thousands of randomly oriented microcrystals are merged to reconstruct the full dataset (serial crystallography)."

- question: "Time-resolved crystallography at an XFEL can capture any biological process at atomic resolution, regardless of the timescale."
  type: true-false
  answer: false
  explanation: "XFEL time-resolved crystallography works best for processes that can be synchronously triggered across the crystal. Light-activated processes (photoreceptors, photosynthetic reaction centers, light-driven ion pumps) are ideal because a laser pulse simultaneously triggers all molecules in the crystal within femtoseconds. For processes triggered by substrate binding (enzymatic catalysis), the limitation is diffusion time — substrate must diffuse into the crystal, which takes milliseconds to seconds depending on crystal size and substrate concentration. This sets a lower limit on the time resolution for diffusion-initiated experiments. Additionally, the process must be fast enough relative to the crystal lattice tolerance — large conformational changes may crack the crystal or disrupt the lattice. Mix-and-inject serial crystallography (MISC) with microcrystals (reducing diffusion path) pushes the time limit to ~milliseconds, while photocaged substrates (released by a light pulse) can synchronize non-light-driven processes on faster timescales."

- question: "How does time-resolved cryo-EM differ from time-resolved crystallography in its approach to capturing structural intermediates?"
  type: short-answer
  answer: "Time-resolved cryo-EM captures intermediates by rapidly mixing a macromolecule with its substrate or trigger, allowing the reaction to proceed for a defined time, and then rapidly freezing the sample by plunge-freezing into liquid ethane to trap the intermediate state in vitreous ice. The time resolution is limited by the mixing time (~milliseconds using microfluidic rapid-mixing devices) and the freezing time (~1 millisecond for vitrification). Unlike crystallography, cryo-EM works with molecules in solution (no crystal lattice constraints), so large conformational changes that would destroy a crystal are readily captured. Additionally, cryo-EM's ability to computationally classify particles into different conformational states means that a heterogeneous mixture of intermediates can be sorted after the fact — each particle is assigned to a conformational class, and 3D reconstructions of each class reveal the structural ensemble present at that time point."
  explanation: "Time-resolved cryo-EM has been applied to ribosome translocation (capturing pre- and post-translocation states after GTP hydrolysis), to GroEL-GroES chaperonin cycling (trapping ATP-driven conformational changes), and to spliceosomes (resolving multiple catalytic intermediates). The combination of millisecond time resolution and the ability to handle conformational heterogeneity makes it complementary to XFEL approaches, which offer femtosecond-to-millisecond resolution but require crystal-compatible motions."

- question: "What structural insights about enzyme catalysis have been uniquely revealed by time-resolved serial crystallography that could not be obtained from static structures?"
  type: short-answer
  answer: "Time-resolved serial crystallography has revealed transient catalytic intermediates — structural states that exist for femtoseconds to milliseconds during the catalytic cycle and cannot be trapped by conventional methods. Key examples include: (1) in bacteriorhodopsin (a light-driven proton pump), XFEL time series captured the complete photocycle at near-atomic resolution, showing the retinal isomerization, water wire rearrangement, and protein conformational changes that move protons across the membrane — individual intermediates lasting picoseconds were resolved; (2) in fluorescent proteins, the chromophore excited state and early photochemistry were captured before thermal relaxation; (3) in cytochrome c oxidase, intermediates in the oxygen reduction mechanism were trapped. These experiments revealed that enzyme active sites undergo coordinated sub-angstrom motions during catalysis — correlated movements of residues, water molecules, and substrates that facilitate bond breaking and formation — details invisible in static endpoint structures."
  explanation: "The bacteriorhodopsin work by Nango et al. (2016) and Nogly et al. (2018) is the landmark demonstration: 13 time points from femtoseconds to milliseconds produced an atomic-resolution movie of proton pumping, revealing water molecule rearrangements and hydrogen bond switches that mechanistic models had predicted but never been observed. This represents the fulfillment of structural biology's longstanding goal of watching molecular machines in action."
```

## Explainer

For most of its history, structural biology has produced **static pictures** of molecules. A crystal structure shows where atoms are on average; a cryo-EM map shows a frozen snapshot. But biological function is inherently dynamic: enzymes catalyze reactions through sequences of conformational changes, molecular machines like the ribosome and ATP synthase cycle through multiple structural states, and signaling proteins switch between active and inactive conformations. Time-resolved structural methods aim to add the dimension of time — capturing not just where atoms are, but how they move during biological processes.

**X-ray free-electron lasers (XFELs)** represent the most dramatic advance in time-resolved structural biology. An XFEL generates X-ray pulses of extraordinary brightness (10^12 photons per pulse) and ultrashort duration (10-50 femtoseconds). These pulses are so intense that they vaporize any crystal they hit — but the diffraction pattern is recorded before the crystal is destroyed, because the pulse duration is shorter than the timescale of radiation-induced atomic motion (the **diffraction-before-destruction** principle). This has two transformative consequences. First, data can be collected at **room temperature** rather than the cryogenic temperatures (100 K) required at synchrotrons, capturing proteins in their native conformational ensemble rather than cryo-trapped states. Second, **pump-probe experiments** become possible: a laser pulse (the pump) triggers a reaction in the crystal (e.g., photoisomerization of a chromophore), and the XFEL pulse (the probe) captures the structure at a precisely controlled delay time (from femtoseconds to seconds). By varying the delay, a molecular movie is assembled frame by frame.

**Serial femtosecond crystallography (SFX)** is the data collection strategy that makes XFEL crystallography practical. Since each crystal is destroyed by one pulse, a continuous stream of microcrystals (1-30 micrometers) is injected across the XFEL beam. Each crystal diffracts in a random orientation, producing a single still image (no oscillation). Tens of thousands of such images are merged using algorithms (CrystFEL, cctbx.xfel) that index each pattern and scale the reflections, reconstructing a complete dataset from the partial observations. The requirement for large numbers of microcrystals is both a challenge (growing sufficient microcrystals is nontrivial) and an advantage (many proteins form microcrystals more readily than the large single crystals needed for synchrotron work). For time-resolved experiments, the pump laser illuminates the crystal stream microseconds to seconds before the XFEL pulse, and different delay times are interleaved during the experiment.

**Time-resolved cryo-EM** takes a complementary approach suited to larger conformational changes and non-crystalline samples. The strategy involves rapidly mixing the macromolecule with its substrate or trigger using microfluidic devices (achieving mixing times of ~1 millisecond), allowing the reaction to proceed for a controlled interval (milliseconds to seconds), and then plunge-freezing to trap the intermediate state. Because cryo-EM works on individual particles in solution, there is no crystal lattice to constrain conformational changes, and the computational classification methods developed for single-particle analysis can separate a mixed population of intermediates into distinct structural classes — effectively performing the temporal sorting after data collection rather than requiring temporal synchrony in the sample. This approach has captured ribosome dynamics during translocation, ATP-driven conformational changes in chaperonins, and catalytic intermediates in spliceosomes. Together, XFEL serial crystallography and time-resolved cryo-EM are fulfilling structural biology's ambition of watching molecular machines in action, providing atomic-resolution understanding of how structure changes drive biological function.
