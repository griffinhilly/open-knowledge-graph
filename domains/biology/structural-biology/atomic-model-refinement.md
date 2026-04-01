---
id: atomic-model-refinement
title: Atomic Model Refinement
domain: biology
course: structural-biology
prerequisites:
- id: structure-solution-methods
  type: hard
- id: x-ray-crystallography
  type: hard
- id: diffraction-and-fourier-transforms
  type: soft
builds-toward:
- structure-validation-model-quality
tags:
- refinement
- REFMAC
- PHENIX
- COOT
- electron-density-map
- real-space-refinement
- reciprocal-space-refinement
stage: expert
status: validated
---
# Atomic Model Refinement

## Core Idea
Atomic model refinement is the iterative process of improving a macromolecular structure by adjusting atomic coordinates, B-factors (temperature factors), and occupancies to maximize the agreement between the model and the experimental data while maintaining reasonable stereochemistry. Starting from an initial model (obtained from molecular replacement, experimental phasing, or automated building), refinement alternates between **reciprocal-space refinement** (adjusting parameters computationally to minimize the difference between calculated and observed structure factors, using programs like REFMAC5 or phenix.refine) and **real-space refinement** (manual rebuilding in COOT, where the crystallographer inspects the electron density map and corrects errors in chain tracing, side chain conformers, and ligand placement). Chemical restraints (target bond lengths, angles, torsions from small-molecule databases) prevent the model from adopting physically unreasonable geometry during the optimization, acting as regularization that is especially critical at medium to low resolution where the data do not unambiguously define all atomic positions.

## Questions

```yaml
- question: "Why does crystallographic refinement require geometric restraints, and what happens if they are removed?"
  type: multiple-choice
  options:
    - "Restraints are purely cosmetic and can be safely removed at any resolution"
    - "At typical protein crystallographic resolution (1.5-3.0 A), the number of independent observations (reflections) is comparable to or fewer than the number of model parameters (x, y, z, B per atom). Without geometric restraints that encode known chemistry (ideal bond lengths, angles, dihedral angles from small-molecule structures), the optimization is underdetermined and the model overfits the data — atomic positions drift to unreasonable values that happen to reduce R-factor but violate basic chemistry"
    - "Restraints are only needed for hydrogen atoms"
    - "Removing restraints improves the model because the data are perfectly informative"
  answer: 1
  explanation: "The data-to-parameter ratio is the fundamental issue. At 2.0 A resolution, a protein structure has roughly 1 observation per parameter (the ratio improves at higher resolution). Without restraints, the optimization has too much freedom — it can reduce R by moving atoms to positions that fit the noise in the data, producing unrealistic bond lengths and angles. Geometric restraints (derived from high-resolution small-molecule crystal structures where bond lengths and angles are determined to 0.001 A precision) act as additional 'observations' that regularize the optimization, preventing overfitting. At very high resolution (< 1.0 A, where the data-to-parameter ratio exceeds ~5), restraints can be loosened because the data are sufficient to determine atomic positions independently — this is why small-molecule structures are refined with minimal or no restraints."

- question: "Real-space refinement in COOT and reciprocal-space refinement in REFMAC/PHENIX optimize the same objective function."
  type: true-false
  answer: false
  explanation: "They optimize different but complementary objective functions. Reciprocal-space refinement (REFMAC, phenix.refine) minimizes a target function in reciprocal space — the difference between observed and calculated structure factor amplitudes (|F_obs| - |F_calc|), typically using maximum likelihood targets that weight observations by their estimated uncertainty. It adjusts all atomic parameters simultaneously through gradient-based optimization. Real-space refinement (COOT, phenix.real_space_refine) optimizes the fit of the model to the electron density map in real space — maximizing the correlation between model density and observed density, typically for local regions (a few residues at a time) during manual rebuilding. The crystallographer uses COOT to correct errors (flipped peptides, wrong rotamers, misplaced loops) that reciprocal-space refinement cannot fix because they require large-scale coordinate changes that cross energy barriers in the optimization landscape. The two approaches are complementary: reciprocal-space refinement optimizes globally, real-space rebuilding fixes local errors."

- question: "Describe the typical iterative workflow of model refinement and explain why multiple rounds are usually required."
  type: short-answer
  answer: "Refinement proceeds in cycles: (1) reciprocal-space refinement (REFMAC or PHENIX) optimizes coordinates, B-factors, and occupancies against the diffraction data, producing an updated model and improved electron density maps; (2) the crystallographer examines the updated maps in COOT, comparing the model to the density, correcting errors (wrong side chain rotamers, peptide flips, missing or incorrectly placed residues, water molecules, ligands), and rebuilding disordered regions; (3) the manually corrected model goes back into reciprocal-space refinement. Multiple rounds are needed because each round of reciprocal-space refinement produces better phases (and therefore better maps), revealing errors and features not visible in previous maps. Early maps may be too noisy to build side chains confidently; after a few rounds of refinement, the maps improve enough to resolve ambiguities. The process converges when R-free stops decreasing, the maps no longer show features requiring correction, and the model geometry is satisfactory."
  explanation: "A typical refinement might involve 5-20 rounds, depending on the initial model quality and resolution. Automated pipelines (AutoBuild in PHENIX, Buccaneer in CCP4) can handle many rebuilding tasks computationally, but challenging regions (crystal contacts, active sites, ligand binding poses, disordered loops) usually require expert manual intervention in COOT. The quality of the final model depends critically on the crystallographer's skill in map interpretation."

- question: "What is the difference between an Fo-Fc difference map and a 2Fo-Fc map, and why are both needed during refinement?"
  type: short-answer
  answer: "The 2Fo-Fc map (coefficients 2|F_obs| - |F_calc|, phases from the model) shows the electron density that corresponds to the current model — it reveals the overall shape of the protein and confirms where the model matches the data. The Fo-Fc difference map (coefficients |F_obs| - |F_calc|, phases from the model) shows what the model gets wrong — positive peaks indicate density present in the data but not in the model (missing atoms, unmodeled ligands, water molecules), and negative peaks indicate model features not supported by the data (incorrectly placed atoms, wrong conformations). Both are needed because the 2Fo-Fc map guides overall building (confirming correct placement) while the Fo-Fc map diagnoses errors and reveals missing features. A crystallographer examines both simultaneously in COOT: the 2Fo-Fc map at 1.0 sigma contour to see the overall density, and the Fo-Fc map at +/- 3.0 sigma to spot errors and additions."
  explanation: "The Fo-Fc map is particularly important for identifying ligands and water molecules: a strong positive Fo-Fc peak (> 3 sigma) in the active site after refining the protein alone indicates a bound molecule. The shape of this peak, combined with the biochemical context, guides ligand identification and placement. Many errors in published structures stem from insufficient attention to Fo-Fc maps during refinement."
```

## Explainer

After solving the phase problem and obtaining initial phases (via molecular replacement, isomorphous replacement, or anomalous dispersion), the crystallographer has an electron density map and a rough initial model. This model is far from final — it may have incorrect side chain conformations, missing loops, wrong rotamers, imprecise backbone geometry, and no water molecules or ligands. **Refinement** is the process of systematically improving this model, and it is where the crystallographer spends the majority of their time during structure determination. The goal is a model that simultaneously explains the experimental data (low R-free) and obeys the laws of chemistry (reasonable bond geometry, no steric clashes).

**Reciprocal-space refinement** is the computational workhorse. Programs like REFMAC5 (CCP4 suite) and phenix.refine (PHENIX suite) adjust atomic parameters — the x, y, z coordinates, the B-factor (modeling atomic displacement/disorder), and sometimes occupancy (fraction of molecules in a given conformation) — to minimize a target function that measures the discrepancy between the observed structure factor amplitudes |F_obs| and those calculated from the model |F_calc|. Modern programs use **maximum likelihood** targets that weight each observation by its estimated error, giving more influence to well-measured reflections. The optimization is constrained by **geometric restraints**: target values for bond lengths, bond angles, dihedral angles, and planarity of aromatic rings, derived from the ultra-high-resolution small-molecule structures in the Cambridge Structural Database. These restraints are essential because at typical protein resolution (2-3 A), the data alone do not uniquely determine all atomic positions — restraints provide the additional information needed to keep the model chemically reasonable.

**Real-space refinement and manual rebuilding** in programs like COOT complement the automated reciprocal-space optimization. After each round of reciprocal-space refinement, the crystallographer visualizes the electron density maps — the **2Fo-Fc map** (showing what the density looks like overall) and the **Fo-Fc difference map** (showing where the model disagrees with the data). Positive Fo-Fc peaks indicate unmodeled features (missing atoms, ligands, waters); negative peaks indicate features in the model not supported by the data (wrong conformations, overfitted positions). The crystallographer corrects errors by manually adjusting the model in COOT: flipping peptide bonds, rotating side chains to match the density, adding water molecules into positive difference peaks, and rebuilding loop regions that automated refinement could not handle. This manual step requires expertise — the ability to read electron density maps, recognize common error patterns, and judge when density is clear enough to model versus too ambiguous to interpret.

The refinement cycle — reciprocal-space refinement followed by real-space inspection and rebuilding — typically requires 5-20 rounds before convergence. Each round improves the phases (because the model is better), which improves the maps (because phases are better), which reveals new features and errors that can be corrected in the next round. Convergence is assessed by monitoring **R-free** (which should decrease monotonically if the model is genuinely improving), geometric statistics (Ramachandran plot, MolProbity clashscore), and the crystallographer's judgment that the maps no longer show features requiring correction. The final model, along with its associated structure factor data and validation statistics, is deposited in the Protein Data Bank — but the model is only as good as the refinement process that produced it, which is why understanding refinement is essential for anyone who uses crystal structures.
