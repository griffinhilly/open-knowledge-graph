---
id: cell-migration-in-development
title: Cell Migration in Development
domain: biology
course: developmental-biology
prerequisites:
- id: gastrulation
  type: hard
- id: cell-signaling-intro
  type: soft
builds-toward:
- epithelial-mesenchymal-transition-developmental
tags:
- cell-migration
- chemotaxis
- neural-crest-migration
- collective-migration
- cytoskeleton
stage: expert
status: validated
---
# Cell Migration in Development

## Core Idea
Cell migration is essential throughout development: gastrulation requires massive cell rearrangements, neural crest cells migrate from the dorsal neural tube to distant sites throughout the body, and primordial germ cells navigate from their origin to the gonads. Migrating cells extend protrusions (lamellipodia, filopodia) at their leading edge, driven by actin polymerization, form adhesions with the substrate (extracellular matrix or other cells), generate contractile force through actomyosin, and release adhesions at the trailing edge. Migration is guided by chemotaxis (following soluble gradients), haptotaxis (following substrate-bound cues), and contact guidance. Cells can migrate individually or collectively (as sheets, streams, or clusters), and collective migration involves additional coordination through cell-cell junctions and supracellular organization of the cytoskeleton.

## Questions

```yaml
- question: "Neural crest cells must migrate long distances from the dorsal neural tube to their final destinations. How do they navigate to specific, reproducible target locations?"
  type: multiple-choice
  options:
    - "They follow random walks and end up at their destinations by chance"
    - "They follow a combination of attractive cues (chemotactic signals from targets), repulsive cues (inhibitory signals that prevent wrong paths), permissive substrates (ECM tracks), and cell-cell interactions (contact inhibition of locomotion that maintains stream cohesion)"
    - "They are passively transported by blood flow to their destinations"
    - "Each neural crest cell has a unique GPS-like mechanism encoded in its genome"
  answer: 1
  explanation: "Neural crest migration is guided by multiple, redundant cue systems. Chemotactic signals (SDF-1/CXCL12 from targets) attract cells forward. Repulsive molecules (ephrins, Slit/Robo, semaphorins) create 'no-go zones' that restrict migration to defined corridors. Permissive ECM molecules (fibronectin, laminin) provide migration tracks. Contact inhibition of locomotion (CIL) causes cells that touch each other to repolarize and move apart, maintaining stream flow rather than aggregation. This multi-cue guidance system ensures reproducible migration to the correct destinations despite the complexity of the tissue environment."

- question: "In collective cell migration, only the leader cells at the front sense the directional cue; follower cells are passively dragged along."
  type: true-false
  answer: false
  explanation: "While leader cells do have specialized roles (larger lamellipodia, enhanced chemosensing), collective migration involves active participation by all cells in the group. Follower cells are mechanically coupled to leaders through adherens junctions and transmit forces through the group via supracellular actin cables. Follower cells also sense guidance cues and can become leaders if the original leaders are ablated. The collective responds to guidance cues more accurately than individual cells (a phenomenon called 'collective sensing' or the 'many wrongs principle') because the group averages out individual cell sensing errors. Collective migration is an active, cooperative process, not passive following."

- question: "Explain how contact inhibition of locomotion (CIL) contributes to directional migration of neural crest cell streams."
  type: short-answer
  answer: "When two migrating neural crest cells contact each other, they retract their protrusions at the contact site, repolarize away from the contact, and move in opposite directions. Within a migrating stream, this means cells at the leading edge have free space ahead (no contacts to inhibit them) and contacts behind (pushing them forward), while cells at the rear are constantly pushed forward by contacts from all sides. CIL thus converts random motility into directional, stream-like migration without requiring every cell to independently sense a long-range chemotactic gradient. The leading cells sense the gradient; CIL transmits this directionality through the entire stream."
  explanation: "CIL was first described by Abercrombie in the 1950s for fibroblasts and was rediscovered as a key driver of neural crest migration by Mayor and colleagues. It is mediated by Wnt/PCP signaling and N-cadherin at cell-cell contacts and represents an elegant mechanism for converting local cell-cell interactions into population-level directional movement."
```

## Explainer

Development requires cells to move — often long distances, through complex tissue environments, to precise destinations. **Cell migration** is not a passive process but an active, mechanically driven behavior that involves cytoskeletal reorganization, adhesion dynamics, force generation, and navigation using multiple guidance cues. From the massive cell rearrangements of gastrulation to the long-distance journeys of neural crest cells, migration is one of the most fundamental morphogenetic processes.

At the cellular level, migration follows a cycle: **protrusion** (actin polymerization at the leading edge pushes the membrane forward as a lamellipodium or filopodium), **adhesion** (integrins in the protruded membrane bind extracellular matrix, forming focal adhesions that anchor the cell), **contraction** (myosin II-driven contraction of the actin network generates force that pulls the cell body forward), and **retraction** (adhesions at the trailing edge are disassembled, allowing the rear to release and the cell to advance). This cycle, repeated continuously, propels the cell forward. The direction of migration is set by polarization of the cell: signaling pathways (Rac1 at the front promoting protrusion, RhoA at the rear promoting contraction) create a stable front-rear axis that is oriented by external cues.

Guidance cues come in multiple forms. **Chemotaxis** (migration toward higher concentrations of a soluble attractant, or away from a repellent) is the most studied: SDF-1/CXCL12 guides primordial germ cells and neural crest cells, PDGF guides mesodermal cells during gastrulation. **Haptotaxis** (migration along a gradient of substrate-bound molecules) uses ECM components like fibronectin. **Contact guidance** (migration along physical features like aligned collagen fibers) provides structural tracks. **Repulsive cues** (ephrins, semaphorins, Slits) create boundaries that restrict migration to defined corridors. Real migration in vivo typically involves all of these simultaneously, creating a complex landscape of permissive, attractive, and repulsive signals that guides cells to their correct destinations.

**Collective migration** — cells moving as coordinated groups rather than individuals — is increasingly recognized as the dominant mode during development. Neural crest cells migrate in streams, lateral line primordium cells migrate as a cohesive cluster, and epithelial sheets close wounds through collective movement. Collective migration adds cell-cell communication to the equation: mechanical coupling through adherens junctions, supracellular cytoskeletal organization, and **contact inhibition of locomotion** (CIL, where cell-cell contact triggers repolarization away from the contact) all contribute to the coordination of group movement. The result is migration that is more directional, more robust, and more precisely targeted than individual cell movement — the group is smarter than the sum of its parts.
