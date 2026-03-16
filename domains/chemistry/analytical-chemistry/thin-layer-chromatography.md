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

## Explainer

You already understand from chromatography fundamentals that separation depends on differential partitioning between a stationary phase and a mobile phase. Thin-layer chromatography applies that principle in the simplest possible format: a glass or plastic plate coated with a thin layer of **adsorbent** (usually silica gel), a shallow pool of solvent in a closed chamber, and capillary action doing all the work. You spot your sample near the bottom of the plate, stand the plate upright in the solvent, and wait. The solvent climbs the plate by capillary action, carrying dissolved compounds with it at different rates depending on how strongly each compound interacts with the silica surface versus the moving solvent.

The key metric is the **Rf value** — the ratio of the distance a compound travels to the distance the solvent front travels. An Rf of 0 means the compound stuck to the start line (it loves the stationary phase), while an Rf of 1 means it rode the solvent front all the way up (it loves the mobile phase). Because silica gel is polar, polar compounds cling to it and travel slowly (low Rf), while nonpolar compounds dissolve readily in a nonpolar solvent and travel fast (high Rf). This is where your knowledge of intermolecular forces pays off: hydrogen bonding, dipole-dipole interactions, and London dispersion forces determine how tightly each analyte adsorbs to the silica surface versus how easily the mobile phase pulls it away.

Choosing the right **eluent** (mobile phase solvent) is the main experimental decision. A very nonpolar eluent like hexane barely moves polar compounds, compressing all spots near the origin. A very polar eluent like methanol pushes everything to the solvent front. The practical target is an Rf between 0.3 and 0.5 for the compounds of interest, which gives the best separation. You tune polarity by mixing solvents — for example, adding small percentages of ethyl acetate to hexane — and running test plates until the spots resolve cleanly. This same logic of polarity tuning transfers directly to HPLC column chromatography later.

Once the plate is developed and dried, you need to **visualize** the spots, since most organic compounds are colorless. The most common method is shining a UV lamp on a plate containing a fluorescent indicator: compounds that absorb UV light appear as dark spots against a glowing green background. For compounds that do not absorb UV, you can expose the plate to iodine vapor (which stains unsaturated compounds brown) or dip it in a chemical stain like potassium permanganate. In practice, TLC is used constantly in organic chemistry labs — you spot a reaction mixture at several time points on the same plate alongside authentic starting material and product standards. Watching the starting material spot fade and the product spot grow gives you real-time feedback on whether your reaction is working, all in about ten minutes and with micrograms of material.
