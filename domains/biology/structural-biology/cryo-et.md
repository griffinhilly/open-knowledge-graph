---
id: cryo-et
title: Cryo-ET
domain: biology
course: structural-biology
prerequisites:
- id: cryo-em
  type: hard
builds-toward:
- macromolecular-assemblies
tags:
- cryo-electron-tomography
- tomography
- in-situ-structural-biology
- subtomogram-averaging
- FIB-milling
stage: expert
status: validated
---
# Cryo-ET

## Core Idea
Cryo-electron tomography (cryo-ET) images biological structures in their native cellular context by collecting a tilt series — a sequence of cryo-EM images of the same specimen tilted from approximately -60 to +60 degrees — and computationally reconstructing a three-dimensional volume (tomogram). Unlike single-particle cryo-EM (which images purified molecules in isolation), cryo-ET can visualize macromolecular complexes directly inside cells, revealing their spatial organization, interactions with other cellular components, and functional states in situ. Focused ion beam (FIB) milling thins frozen cells to electron-transparent lamellae (~100-200 nm), and subtomogram averaging of repeated structures within tomograms can achieve sub-nanometer resolution.

## Questions

```yaml
- question: "What is the key difference between single-particle cryo-EM and cryo-electron tomography?"
  type: multiple-choice
  options:
    - "Single-particle cryo-EM uses electrons; cryo-ET uses X-rays"
    - "Single-particle cryo-EM images many identical copies of purified molecules and averages them for a high-resolution structure; cryo-ET images individual, unique biological objects (cells, organelles) by tilting to reconstruct their 3D volume, sacrificing resolution for the ability to see structures in their native context"
    - "Cryo-ET requires crystals; single-particle cryo-EM does not"
    - "There is no difference; they are the same technique"
  answer: 1
  explanation: "Single-particle cryo-EM achieves high resolution by averaging many images of identical (purified) molecules — the information deficit from low-dose imaging of each particle is overcome by having millions of copies. Cryo-ET images unique objects (a specific region of a specific cell) and achieves 3D information by tilting rather than by having multiple copies. This means cryo-ET typically achieves lower resolution (~20-40 Angstroms for a single tomogram), but it reveals the native cellular context — where complexes are located, what they interact with, and how they are organized in the cell. Subtomogram averaging of repeated structures can improve resolution to ~5-10 Angstroms."

- question: "Cryo-ET can image the interior of a whole mammalian cell at high resolution without any sample preparation beyond vitrification."
  type: true-false
  answer: false
  explanation: "Mammalian cells are too thick (5-10 micrometers) for electrons to penetrate — the electron beam can only pass through specimens ~200-500 nm thick. Intact mammalian cells must be thinned by focused ion beam (FIB) milling, which uses a gallium or xenon ion beam to ablate frozen cellular material, leaving a thin lamella (~100-200 nm) that is electron-transparent. FIB milling is performed on the frozen, vitrified specimen and preserves the native cellular ultrastructure within the lamella. Small cells (bacteria, thin cellular extensions) can be imaged directly. FIB-milling has been a transformative advance for cryo-ET, making the interior of any cell type accessible to tomographic imaging."

- question: "How does subtomogram averaging improve the resolution achievable by cryo-ET?"
  type: short-answer
  answer: "When the same macromolecular complex (e.g., a ribosome, a nuclear pore complex, or a coat protein on a vesicle) appears multiple times within a tomogram or across multiple tomograms, each instance can be extracted as a 'subtomogram' — a small 3D volume. These subtomograms are then aligned and averaged, just as single-particle cryo-EM averages 2D particle images. The averaging improves signal-to-noise and resolution because the noise in each subtomogram is random while the signal (the common structure) reinforces. With enough copies (~1,000-100,000), subtomogram averaging can achieve sub-nanometer resolution — approaching that of single-particle cryo-EM, but with the advantage that the structures were imaged in their native cellular environment."
  explanation: "Subtomogram averaging bridges the gap between cellular imaging (low resolution, native context) and structural biology (high resolution, purified sample). It has been used to determine in-situ structures of ribosomes on the endoplasmic reticulum, nuclear pore complexes in the nuclear envelope, and coat proteins on transport vesicles — revealing how these machines function in their actual cellular setting."
```

## Explainer

Single-particle cryo-EM produces beautiful atomic-resolution structures, but of purified molecules in isolation. The molecule has been removed from the cell, stripped of its interaction partners, and frozen in a thin layer of ice. **Cryo-electron tomography** takes the opposite approach: it images molecules where they actually function — inside cells, attached to membranes, assembled into higher-order structures — revealing not just what a molecule looks like but where it is and what it does in its native environment.

The principle is analogous to medical CT scanning. A tilt series is collected: the specimen is imaged at many different tilt angles (typically -60 to +60 degrees in 1-3 degree increments), producing a set of 2D projections from different viewing angles. These projections are computationally combined (back-projected) to reconstruct a 3D volume — the **tomogram**. Each tomogram is a complete 3D snapshot of a biological scene at the moment of vitrification: ribosomes decorating the ER surface, vesicles budding from the Golgi, cytoskeletal filaments spanning the cytoplasm, all captured in their native spatial relationships.

The resolution of a single tomogram (~20-40 Angstroms) is limited by the low electron dose (to prevent radiation damage), the missing wedge (the specimen cannot be tilted to 90 degrees, creating a gap in angular coverage), and the specimen thickness (thicker samples scatter electrons more, reducing image quality). **FIB-milling** addresses the thickness problem: a focused ion beam is used to thin a frozen cell to a ~100-200 nm lamella, creating an electron-transparent window into the cell interior. This technology has opened essentially any cell type to tomographic imaging.

**Subtomogram averaging** bridges the resolution gap between cellular tomography and atomic structural biology. When a macromolecular complex appears many times in tomograms (ribosomes on the ER, nuclear pore complexes in the nuclear envelope, coat proteins on vesicles), each instance can be extracted as a small 3D volume, and these volumes can be aligned and averaged — identical in principle to the averaging that drives single-particle cryo-EM. With sufficient copies (thousands to tens of thousands), subtomogram averaging achieves sub-nanometer resolution while preserving the cellular context. Recent studies have determined near-atomic resolution structures of ribosomes, proteasomes, and viral capsid proteins directly inside cells — a goal that seemed impossibly ambitious just a decade ago. Cryo-ET is the frontier of structural biology, connecting molecular structure to cellular function in a way that no other technique can match.
