---
id: diffusion-tensor-imaging-white-matter
title: Diffusion Tensor Imaging and White Matter Microstructure
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: neuroimaging-methods
  type: hard
- id: myelin-and-myelination
  type: soft
- id: linear-transformation-matrix-representation
  type: soft
- id: vectors-in-3d
  type: soft
builds-toward:
- white-matter-plasticity-learning
- white-matter-development-myelination-trajectory
tags:
- DTI
- white-matter
- microstructure
- neuroimaging
- fiber-tracts
stage: advanced
status: draft
---

# Diffusion Tensor Imaging and White Matter Microstructure

## Core Idea
Diffusion tensor imaging (DTI) measures the anisotropic diffusion of water molecules along myelinated fiber tracts, revealing white matter organization and integrity. Metrics like fractional anisotropy (FA) and mean diffusivity (MD) quantify axonal density, diameter, and myelination. DTI enables mapping of major fiber bundles and assessment of white matter abnormalities in development, learning, and disease.

## Explainer

From your neuroimaging methods background, you know that conventional structural MRI images the brain's gross anatomy using the contrast between tissue types, and fMRI tracks blood oxygenation as a proxy for neural activity. DTI exploits a different physical property: the **directional diffusion of water molecules**. In open fluid (like a glass of water), water molecules diffuse equally in all directions — this is called **isotropic diffusion**. But in the brain's white matter, where axons run in organized bundles wrapped in myelin, diffusion is constrained: water moves much more freely *along* the fiber than *across* it. This directional preference is called **anisotropic diffusion**, and it is the signal DTI measures.

The word "tensor" refers to a mathematical object (from your linear algebra prerequisite) that captures diffusion in all spatial directions simultaneously. At each voxel in the brain, the diffusion tensor is estimated from multiple measurements taken with diffusion gradients applied in different directions — typically at least six, often 30 or more. The tensor can be decomposed into three eigenvectors: the **primary eigenvector** points along the dominant diffusion direction (i.e., the axis of the fiber bundle), while the other two describe diffusion perpendicular to it. Two summary metrics are derived from the eigenvalues: **fractional anisotropy (FA)** measures how directional the diffusion is, ranging from 0 (perfectly isotropic, like gray matter) to 1 (perfectly anisotropic, like a tightly packed, well-myelinated tract). **Mean diffusivity (MD)** captures the overall magnitude of water movement, independent of direction. High FA and low MD indicate dense, well-myelinated, coherently organized fiber tracts; low FA or high MD can signal demyelination, axonal damage, edema, or developmental immaturity.

**Tractography** uses the primary eigenvector at each voxel as a compass heading to reconstruct three-dimensional fiber pathways algorithmically — "following the water" from voxel to voxel to map white matter connections between brain regions. This has made DTI the primary tool for **in vivo human connectome mapping**: identifying tracts like the corticospinal tract (motor control), the arcuate fasciculus (language), the cingulum (limbic connectivity), and the uncinate fasciculus (frontal-temporal connections). Connectivity analyses can compare white matter networks between individuals, developmental stages, or clinical groups.

The main limitations of DTI stem from the simplicity of the single-tensor model. In regions where multiple fiber populations cross within a single voxel — which occurs in roughly 90% of white matter — the tensor model produces spuriously low FA values and may trace incorrect pathways. More advanced models (constrained spherical deconvolution, multi-shell diffusion) can resolve crossing fibers. Despite these limitations, DTI has been transformative: it is the only non-invasive method for mapping white matter microstructure and structural connectivity in the living human brain, making it central to developmental neuroscience, neurological diagnosis, and the emerging field of white matter plasticity.
