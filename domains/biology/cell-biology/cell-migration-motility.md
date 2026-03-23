---
id: cell-migration-motility
title: Cell Migration and Cytoskeletal Dynamics
domain: biology
course: cell-biology
prerequisites:
- id: eukaryotic-cell-compartmentalization
  type: soft
builds-toward:
- cell-adhesion-tissue
tags:
- cell-migration
- cytoskeleton
- actin
- motility
stage: formal-systems
status: validated
---

# Cell Migration and Cytoskeletal Dynamics

## Core Idea
Cell migration depends on dynamic remodeling of the actin cytoskeleton and microtubules. At the leading edge, Arp2/3 complex nucleates actin polymerization, creating branched filaments that polymerize against the membrane, generating lamellipodial protrusions. Myosin-II motors in the cell body contract actin bundles (stress fibers), generating pulling force. Focal adhesions link the cytoskeleton to the extracellular matrix through integrin receptors. Cells sense extracellular gradients (chemokines, matrix stiffness, adhesion ligands) and migrate toward or away from signals, fundamental to development, immunity, and wound healing.

## Questions

```yaml
- question: "What drives the extension of the lamellipodium at the leading edge of a migrating cell?"
  type: multiple-choice
  options:
    - "Myosin-II motor proteins pulling the membrane forward along actin stress fibers"
    - "Actin polymerization: Arp2/3 nucleates branched filaments that push the membrane outward as monomers add to their ends"
    - "Microtubule polymerization extending outward from the centrosome toward the cell periphery"
    - "Integrin receptors pulling the membrane forward by engaging extracellular matrix proteins"
  answer: 1
  explanation: "Lamellipodial protrusion is driven by actin polymerization, not motor proteins. The Arp2/3 complex (activated by upstream signals) nucleates new actin filaments that branch off existing ones at 70° angles, creating a dense pushing meshwork. As monomers add to filament ends pressed against the membrane, they generate mechanical force that physically pushes the membrane forward through the thermodynamics of polymerization — no motor protein is required for this step. Myosin-II (option A) drives contraction in the cell body, not protrusion at the leading edge."

- question: "What is the role of small GTPases Rac1 and RhoA in directed cell migration?"
  type: multiple-choice
  options:
    - "Rac1 and RhoA both promote actin polymerization throughout the cell to generate movement in all directions"
    - "Rac1 promotes actin branching at the leading edge while RhoA promotes myosin contraction at the rear, establishing front-rear polarity"
    - "Rac1 regulates focal adhesion assembly and RhoA regulates microtubule dynamics during migration"
    - "Both are required for integrin binding to the extracellular matrix at the leading edge"
  answer: 1
  explanation: "The spatial segregation of Rac1 (front) and RhoA (rear) creates the front-rear polarity that ensures movement is directional rather than random. Rac1 activates Arp2/3, promoting branched actin polymerization and lamellipodial protrusion. RhoA promotes myosin-II assembly and activity, driving contraction of stress fibers that pull the cell body forward and retract the tail. Without this polarity, the cell would extend protrusions in all directions and go nowhere."

- question: "Cell migration requires motor proteins at the leading edge to pull the membrane forward, similar to how myosin pulls actin filaments during muscle contraction."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Leading-edge protrusion is driven entirely by actin polymerization — the thermodynamic force of adding monomers to filament ends pressed against the membrane. No motor protein is needed for this step. Myosin-II is critical for migration, but it acts in the cell body (contracting stress fibers to pull the bulk of the cell forward) and at the trailing edge (retracting the tail). Protrusion and contraction are mechanistically distinct processes."

- question: "Focal adhesions must both form at the leading edge and disassemble at the trailing edge for a cell to migrate forward."
  type: true-false
  answer: true
  explanation: "Migration requires a cycle of adhesion and de-adhesion. New focal adhesions form in the newly extended lamellipodium, anchoring it to the extracellular matrix and providing traction for myosin-mediated contraction. Old focal adhesions at the trailing edge must disassemble to allow the tail to retract and the cell to advance. If adhesions are too strong, the tail gets stuck and the cell cannot move; if too weak, there is no traction. The balance of adhesion dynamics is as important as the actin and myosin machinery."

- question: "Describe the four-step cycle of cell migration and identify the primary molecular player responsible for each step."
  type: short-answer
  answer: "Step 1 — Protrusion: Arp2/3 complex nucleates branched actin polymerization, pushing the membrane forward to form a lamellipodium. Step 2 — Adhesion: integrin receptors in the new lamellipodium engage the extracellular matrix, forming focal adhesions that anchor the extension. Step 3 — Contraction: myosin-II motors slide along actin stress fibers in the cell body, generating pulling force that moves the bulk of the cell toward the leading edge. Step 4 — Retraction: focal adhesions at the trailing edge disassemble and myosin-II contraction snaps the tail forward."
  explanation: "The four-step cycle resembles a hand-over-hand movement: reach forward (protrusion), grab (adhesion), pull the body up (contraction), release the old grip (retraction). Understanding which molecule drives which step explains what happens when any component is inhibited — block Arp2/3 and protrusion fails; inhibit myosin-II and the cell body cannot follow; disrupt integrin engagement and there is no traction to pull against."
```

## Explainer

From your understanding of eukaryotic cell compartmentalization, you know that cells have an internal cytoskeleton that provides structural support and organizes the interior. Cell migration takes this further: the cytoskeleton is not just scaffolding — it is a dynamic engine that can propel the entire cell forward. The process is remarkably coordinated, involving simultaneous construction at the front, contraction in the middle, and disassembly at the rear.

The cycle of migration has four repeating steps. First, the cell extends a flat, sheet-like protrusion called a **lamellipodium** at its leading edge. This is driven by **actin polymerization**: the **Arp2/3 complex** (activated by signals from the cell surface) nucleates new actin filaments that branch off existing ones at 70° angles, creating a dense, pushing meshwork. As actin monomers add to filament ends pressed against the membrane, they generate a mechanical force that physically pushes the membrane forward — no motor protein is needed for this step, just the thermodynamics of polymerization. Second, the newly extended membrane must **attach** to the surface it is crawling on. New **focal adhesions** form as integrin receptors in the extended lamellipodium engage extracellular matrix proteins, creating anchor points.

Third, the cell body must follow the leading edge. This is where **myosin-II** motors come in. Myosin-II assembles into bipolar filaments that slide along actin **stress fibers** — bundled, contractile actin cables that run through the cell body — generating a squeezing force that pulls the bulk of the cell forward. Think of the leading edge as a hand reaching forward to grab a handhold, and myosin contraction as the arm pulling the body up to meet the hand. Fourth, adhesions at the **trailing edge** must release, and the rear of the cell must retract. This involves disassembly of old focal adhesions and myosin-powered contraction that snaps the tail forward.

What makes migration purposeful rather than random is **directional sensing**. Cells detect shallow gradients of chemical signals (**chemotaxis**), substrate stiffness (**durotaxis**), or adhesion molecule density (**haptotaxis**) and preferentially extend lamellipodia toward the signal source. Small GTPases — particularly **Rac1** at the leading edge (promoting Arp2/3 activation and actin branching) and **RhoA** at the rear (promoting myosin contraction and tail retraction) — create front-rear polarity. This polarity ensures the cell moves in one direction rather than extending protrusions everywhere at once. Cell migration is essential throughout life: neutrophils chase bacterial signals to sites of infection, fibroblasts migrate into wounds to deposit new matrix, and during embryonic development, neural crest cells migrate enormous distances to form structures ranging from facial bones to the enteric nervous system.
