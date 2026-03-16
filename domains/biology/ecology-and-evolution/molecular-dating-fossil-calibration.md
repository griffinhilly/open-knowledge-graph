---
id: molecular-dating-fossil-calibration
title: Molecular Clock Calibration and Fossil Dating
domain: biology
course: ecology-and-evolution
prerequisites:
- id: molecular-clock-hypothesis
  type: hard
- id: molecular-evolution
  type: hard
- id: phylogenetic-inference
  type: soft
- id: poisson-distribution
  type: soft
builds-toward:
- paleontology-fossil-record
tags:
- molecular-clock
- dating
- fossil-calibration
- divergence-time
stage: formal-systems
status: draft
---

# Molecular Clock Calibration and Fossil Dating

## Core Idea
Molecular clocks estimate divergence times by assuming constant substitution rates. Fossil evidence provides calibration points; a fossil constrains the minimum age of a node. Relaxed clock models account for rate variation among lineages. Uncertainty in fossils and rate variation limits dating precision, especially for older divergences.

## Explainer

The molecular clock hypothesis, which you have already studied, proposes that DNA and protein sequences accumulate substitutions at a roughly constant rate over time. This converts sequence divergence into a measure of elapsed time — but the clock only gives you *relative* time. To translate "these two species differ by 2% at this gene" into "they diverged approximately 10 million years ago," you need an external anchor. That anchor comes from the fossil record.

**Fossil calibration** works by assigning age constraints to specific nodes on a phylogenetic tree. When a fossil is found that clearly belongs to a particular lineage, its geological age — determined by radiometric dating of surrounding rock layers — sets a **minimum age** for the node where that lineage diverges from its sister group. It is a minimum because the actual divergence must have occurred at or before the time the fossil organism lived; the fossil only records the earliest known appearance. For example, if the oldest known bat fossil is 52 million years old, the divergence of bats from their sister group must be at least that old. Some calibrations also set soft maximum ages based on the absence of fossils in well-sampled older strata, but these are inherently less certain.

The practical challenge is that substitution rates are not truly constant. Rates vary among lineages (mice evolve faster than elephants), among genes (mitochondrial DNA evolves faster than most nuclear genes), and even over time within a lineage. **Relaxed clock models** address this by allowing rates to vary across branches of the tree according to statistical distributions, rather than enforcing a single rate everywhere. These models use Bayesian inference to simultaneously estimate branch-specific rates and divergence times, given the sequence data, the tree topology, and the fossil calibration points. The result is a posterior distribution of divergence times — not a single answer but a range reflecting uncertainty in both rates and calibrations.

The quality of molecular dating depends heavily on the quality of the calibrations. A single misidentified fossil — placed on the wrong branch or dated to the wrong stratum — can distort the entire time-scale. Using multiple independent calibration points spread across the tree helps, because errors in one calibration are partially corrected by the others. Even so, deep divergences (hundreds of millions of years) remain difficult to date precisely because rate variation accumulates and the fossil record becomes sparse. The interplay between molecular and paleontological evidence makes this field inherently interdisciplinary: good molecular dating requires not just computational sophistication but also careful paleontological judgment about which fossils are reliable calibration points and where they belong on the tree.
