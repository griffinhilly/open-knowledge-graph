---
id: thin-layer-chromatography
title: Thin-Layer Chromatography (TLC)
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: chromatography-fundamentals
  type: hard
- id: intermolecular-forces
  type: soft
builds-toward:
- hplc
tags:
- TLC
- Rf value
- silica gel
- normal phase
- visualization
stage: advanced
status: validated
---

# Thin-Layer Chromatography (TLC)

## Core Idea
Thin-layer chromatography separates analytes on a thin layer of adsorbent (typically silica gel or alumina) coated on a plate, using a liquid mobile phase that migrates by capillary action. The Rf value (distance traveled by analyte / distance traveled by solvent) characterizes each compound under fixed conditions and is used for identity comparison. TLC is rapid, inexpensive, and requires minimal sample; it is used for reaction monitoring, purity checking, and mobile phase scouting for HPLC. Spots are visualized by UV fluorescence quenching, iodine staining, or chemical derivatization.

## How It's Best Learned
Monitor an organic reaction by TLC at multiple time points, comparing starting material, product, and authentic standards on the same plate. Systematically varying eluent polarity to optimize Rf values (target 0.3–0.5) teaches solvent-selectivity principles applicable to HPLC.

## Common Misconceptions
- Rf values are not absolute constants — they vary with adsorbent activity, mobile phase saturation of the chamber, and temperature, so co-spotting with a standard on the same plate is essential.
- Comigration (same Rf) does not confirm identical compounds; multiple eluent systems are needed.

## Questions

```yaml
- question: "A chemist runs a silica TLC plate with hexane as the eluent and observes that a polar compound barely moves from the origin (Rf ≈ 0.05). What change to the eluent would best increase the compound's Rf to the target range of 0.3–0.5?"
  type: multiple-choice
  options:
    - "Add a small amount of a more polar solvent (e.g., ethyl acetate) to the hexane"
    - "Use a less polar stationary phase (alumina instead of silica)"
    - "Increase the volume of hexane in the chamber to saturate the atmosphere"
    - "Re-spot the sample with a higher concentration"
  answer: 0
  explanation: "In normal-phase TLC (polar silica stationary phase), polar compounds stick tightly to the silica and need a polar mobile phase to compete with them for the silica surface. Adding a more polar solvent like ethyl acetate to hexane increases the mobile phase's ability to pull the polar compound off the silica, raising its Rf. Chamber saturation (option C) helps reproducibility but doesn't change the relative polarity. Sample concentration (option D) affects spot darkness but not Rf. Option B would reduce stationary-phase polarity which could help, but changing the solvent is the standard first approach."

- question: "Two unknown compounds are co-spotted on a silica TLC plate and run in ethyl acetate/hexane. Both spots comigrate at Rf = 0.42. What is the most appropriate conclusion?"
  type: multiple-choice
  options:
    - "The compounds are identical, since they have the same Rf under identical conditions"
    - "The compounds are identical only if they also show the same color under UV light"
    - "The compounds may be identical or different — same Rf in one system is insufficient to confirm identity; multiple eluent systems are needed"
    - "The compounds are definitely different, because two distinct substances cannot have the same Rf"
  answer: 2
  explanation: "Same Rf in a single solvent system does not confirm identity — different compounds can have the same Rf by coincidence if their overall polarity happens to be similar. Confirmation requires co-spotting in at least 2–3 different solvent systems with different polarity characteristics. If the spots comigrate in all systems, identity becomes much more likely (though NMR or mass spectrometry provides definitive confirmation). This is a classic TLC pitfall: comigration ≠ same compound."

- question: "Increasing the polarity of the mobile phase in a normal-phase (silica) TLC experiment will increase the Rf values of the compounds being separated."
  type: true-false
  answer: true
  explanation: "In normal-phase TLC, compounds compete with the mobile phase for adsorption sites on the polar silica stationary phase. A more polar mobile phase competes more effectively with compounds for silica binding, pulling them along with the solvent front and increasing their Rf values. This is why switching from hexane (nonpolar) to ethyl acetate (polar) causes spots to move farther up the plate, and why a very polar solvent like methanol pushes everything near the solvent front (Rf → 1)."

- question: "An Rf value measured in one experiment can be reliably compared to Rf values reported in the literature from a different laboratory to confirm compound identity."
  type: true-false
  answer: false
  explanation: "Rf values are not absolute constants — they depend on adsorbent activity (how hydrated the silica is), mobile phase saturation of the chamber, temperature, plate batch, and solvent purity. Even small differences in these conditions between labs will shift Rf values. The correct approach is to always co-spot an authentic reference standard on the same plate in the same run, so any variation in conditions affects both compounds equally. Comparing raw Rf numbers across different experiments or laboratories is unreliable."

- question: "Why must you co-spot an unknown compound with an authentic standard on the same TLC plate in the same run rather than comparing Rf values from separate experiments?"
  type: short-answer
  answer: "Rf values shift with adsorbent activity, chamber saturation, temperature, and solvent composition. Co-spotting ensures both compounds experience identical conditions, making Rf comparison meaningful. Comparing values from separate runs introduces experimental variation that can make different compounds appear identical or the same compound appear different."
  explanation: "The key misconception to avoid is treating Rf as a physical constant like a melting point. It is a ratio measured under experimental conditions that are difficult to exactly replicate. By running the unknown and standard side by side on the same plate, you eliminate all sources of inter-run variability — any differences in spot position are then meaningful rather than artifacts of condition changes."
```

## Explainer

You already understand from chromatography fundamentals that separation depends on differential partitioning between a stationary phase and a mobile phase. Thin-layer chromatography applies that principle in the simplest possible format: a glass or plastic plate coated with a thin layer of **adsorbent** (usually silica gel), a shallow pool of solvent in a closed chamber, and capillary action doing all the work. You spot your sample near the bottom of the plate, stand the plate upright in the solvent, and wait. The solvent climbs the plate by capillary action, carrying dissolved compounds with it at different rates depending on how strongly each compound interacts with the silica surface versus the moving solvent.

The key metric is the **Rf value** — the ratio of the distance a compound travels to the distance the solvent front travels. An Rf of 0 means the compound stuck to the start line (it loves the stationary phase), while an Rf of 1 means it rode the solvent front all the way up (it loves the mobile phase). Because silica gel is polar, polar compounds cling to it and travel slowly (low Rf), while nonpolar compounds dissolve readily in a nonpolar solvent and travel fast (high Rf). This is where your knowledge of intermolecular forces pays off: hydrogen bonding, dipole-dipole interactions, and London dispersion forces determine how tightly each analyte adsorbs to the silica surface versus how easily the mobile phase pulls it away.

Choosing the right **eluent** (mobile phase solvent) is the main experimental decision. A very nonpolar eluent like hexane barely moves polar compounds, compressing all spots near the origin. A very polar eluent like methanol pushes everything to the solvent front. The practical target is an Rf between 0.3 and 0.5 for the compounds of interest, which gives the best separation. You tune polarity by mixing solvents — for example, adding small percentages of ethyl acetate to hexane — and running test plates until the spots resolve cleanly. This same logic of polarity tuning transfers directly to HPLC column chromatography later.

Once the plate is developed and dried, you need to **visualize** the spots, since most organic compounds are colorless. The most common method is shining a UV lamp on a plate containing a fluorescent indicator: compounds that absorb UV light appear as dark spots against a glowing green background. For compounds that do not absorb UV, you can expose the plate to iodine vapor (which stains unsaturated compounds brown) or dip it in a chemical stain like potassium permanganate. In practice, TLC is used constantly in organic chemistry labs — you spot a reaction mixture at several time points on the same plate alongside authentic starting material and product standards. Watching the starting material spot fade and the product spot grow gives you real-time feedback on whether your reaction is working, all in about ten minutes and with micrograms of material.
