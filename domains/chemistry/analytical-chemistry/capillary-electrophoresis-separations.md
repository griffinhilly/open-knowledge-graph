---
id: capillary-electrophoresis-separations
title: Capillary Electrophoresis Separations
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: electrochemistry-basics
  type: hard
- id: capillary-electrophoresis-cze-methods
  type: soft
tags:
- capillary electrophoresis
- CE
- electrophoresis
stage: advanced
status: validated
---
# Capillary Electrophoresis Separations

## Core Idea
Capillary electrophoresis separates charged analytes by applying high voltage across a narrow capillary, exploiting differences in charge-to-size ratio. CE offers high resolution, minimal sample requirements, and rapid analysis times.

## Questions

```yaml
- question: "A researcher runs a CE experiment at standard buffer pH and observes both cationic and anionic analytes arriving at the cathode-end detector in the same run. How is it possible for anions to reach the detector, given that they should migrate toward the anode?"
  type: multiple-choice
  options:
    - "At standard buffer pH, anions are protonated and temporarily neutral, so they do not migrate toward the anode"
    - "The high voltage reverses anion migration direction at CE field strengths"
    - "Electroosmotic flow carries the bulk solution — including anions — toward the cathode at a rate that exceeds the anions' electrophoretic migration toward the anode"
    - "Anions bind to the positively charged capillary wall and are swept toward the cathode by convection"
  answer: 2
  explanation: "This is the defining feature of electroosmotic flow (EOF) in CE. The silica capillary wall carries negative charges (deprotonated silanols) that attract a layer of cations from the buffer. When voltage is applied, this cation layer is driven toward the cathode, dragging the bulk solution with it. EOF is typically strong enough that it exceeds the electrophoretic velocity of anions moving in the opposite direction, so the net displacement of anions is still toward the cathode — just slower than for cations. This means cations, neutrals, and anions can all be detected in a single pass, with cations arriving first (moving with EOF + own electrophoresis) and anions last (moving with EOF − own electrophoresis)."

- question: "What is the primary reason CE achieves far higher theoretical plate counts — and therefore better resolution — than HPLC for comparable separation lengths?"
  type: multiple-choice
  options:
    - "CE uses much higher voltages than HPLC, which drives analytes through the column faster and prevents diffusion"
    - "CE uses smaller sample volumes, so there are fewer analyte molecules to separate"
    - "EOF in CE produces a flat (plug-like) flow profile that minimizes band broadening, whereas HPLC's pressure-driven parabolic flow profile causes significant dispersion"
    - "CE operates at higher temperatures that increase diffusion coefficients and speed up mass transfer"
  answer: 2
  explanation: "In pressure-driven flow (HPLC), the velocity of the mobile phase is fastest at the center of the column and zero at the walls — a parabolic profile. Analyte molecules near the wall spend more time in the column than those in the center, causing band broadening. EOF has a flat profile: the entire bulk solution moves at nearly uniform velocity from wall to center, because the driving force (the charged wall attracting buffer cations) acts at the surface and the resulting plug-like flow is nearly dispersion-free. This eliminates a major source of band broadening, enabling plate counts of 100,000 to 1,000,000 compared to 10,000–100,000 for typical HPLC."

- question: "In CE, two molecules with identical charge but different sizes will migrate at the same velocity because separation is based solely on charge."
  type: true-false
  answer: false
  explanation: "CE separation is based on electrophoretic mobility, which depends on the charge-to-size ratio (specifically, charge divided by hydrodynamic radius). A large molecule with the same charge as a small molecule will migrate more slowly because friction with the surrounding solution increases with size. Two molecules with the same charge but different sizes will have different charge-to-size ratios and therefore different mobilities — they will be resolved. This is analogous to falling through a viscous medium: a larger sphere falls more slowly than a smaller one despite the same gravitational force, because hydrodynamic drag increases with size."

- question: "Electroosmotic flow in CE results from the migration of cations attracted to the negatively charged capillary wall, which drags the bulk solution toward the cathode."
  type: true-false
  answer: true
  explanation: "The mechanism is straightforward: deprotonated silanol groups on the inner silica surface create a negative wall charge at typical buffer pH. Buffer cations are attracted to this surface, forming an electrical double layer. When a high voltage is applied, these surface-bound cations are driven toward the cathode, and because they are solvated and interact with adjacent water molecules, they drag the bulk solution along with them in a plug-like flow. The strength of EOF depends on the surface charge density (related to pH) and the zeta potential — which is why adjusting buffer pH is a primary tool for controlling EOF in CE."

- question: "Explain why the flat flow profile of electroosmotic flow leads to higher resolution in CE compared to the parabolic flow profile in conventional liquid chromatography."
  type: short-answer
  answer: "In pressure-driven HPLC, flow velocity is highest at the column center and zero at the walls, creating a parabolic profile. Molecules in the fast-moving center traverse the column faster than molecules near the slow walls, so a narrow band of injected analyte spreads out into a broad zone over time — this is called axial dispersion or band broadening. In CE, EOF generates plug flow: the entire cross-section of the capillary moves at nearly the same velocity, because the driving force acts uniformly along the wall rather than in the center. There is no differential velocity across the capillary radius, so injected bands remain narrow. Fewer theoretical plates are 'lost' to flow dispersion, and the total plate count (a measure of separation efficiency) is dramatically higher."
  explanation: "The flat-profile insight also explains why CE can achieve its performance in narrow capillaries rather than packed columns. The geometry (very small diameter, thin annular region) combined with plug flow means that diffusion across the capillary diameter is rapid relative to the time analytes spend in the capillary, which further suppresses band broadening. This is the physical basis for CE's exceptional resolution with minimal sample volume."
```

## Explainer

From your study of electrochemistry, you know that charged species migrate in an electric field — cations toward the cathode and anions toward the anode. **Capillary electrophoresis** (CE) takes this principle and confines it inside a very narrow fused-silica capillary, typically 25–75 micrometers in internal diameter and 30–100 cm long. By applying a high voltage (typically 10–30 kV) across the capillary filled with a buffer solution, ions migrate at speeds determined by their **electrophoretic mobility**, which depends on the ratio of their charge to their hydrodynamic size. Small, highly charged ions move fastest; large, weakly charged ions move slowest. This simple physical principle produces remarkably efficient separations.

What makes CE unique among separation techniques is the role of **electroosmotic flow** (EOF). The inner surface of a silica capillary carries negative charges (deprotonated silanol groups) at typical buffer pH values. These negative charges attract a layer of cations from the buffer, and when voltage is applied, this cation layer drags the bulk solution toward the cathode. The result is a flat flow profile — unlike the parabolic flow in HPLC columns — which means virtually no band broadening from flow dynamics. EOF is usually strong enough to carry even anions (which would otherwise migrate toward the anode) toward the detector at the cathode end, so cations, neutral species, and anions can all be detected in a single run, separated by their different net velocities.

In practice, a CE experiment requires remarkably little: nanoliter injection volumes, a few milliliters of buffer, and a standard UV or fluorescence detector positioned near the capillary outlet. This makes CE ideal for situations where sample is precious — biological fluids, forensic evidence, or single-cell analysis. The technique achieves theoretical plate counts of 100,000 to 1,000,000, far exceeding typical HPLC performance, because the flat EOF profile and narrow capillary minimize all major sources of band broadening. Variants of the technique extend its reach: **capillary zone electrophoresis** (CZE) separates ions in free solution, **micellar electrokinetic chromatography** (MEKC) adds surfactant micelles to separate neutral molecules, and **capillary gel electrophoresis** (CGE) uses a gel-filled capillary for size-based separations of proteins and DNA fragments.
