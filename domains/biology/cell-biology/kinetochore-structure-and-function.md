---
id: kinetochore-structure-and-function
title: Kinetochore Structure and Function
domain: biology
course: cell-biology
prerequisites:
- id: dna-structure
  type: hard
- id: mitotic-spindle-checkpoint
  type: hard
builds-toward:
- sister-chromatid-cohesion-cohesin-proteins
- anaphase-promoting-complex-cell-cycle-control
tags:
- kinetochore
- chromosome-segregation
- spindle-attachment
stage: advanced
status: draft
---

# Kinetochore Structure and Function

## Core Idea
The kinetochore is a megadalton protein assembly on centromeric chromatin serving as the attachment site for spindle microtubules during chromosome segregation. Over 100 proteins organized into distinct subcomplexes (KMN network: KNL1, MIS12, NDC80 complex) mediate dynamic interactions with kinetochore microtubules and transmit tension signals. The kinetochore also functions as a molecular checkpoint: it monitors biorientation (amphitelic attachment) and prevents anaphase until all sister chromatid pairs achieve proper attachment.

## How It's Best Learned
Visualize kinetochore structure by cryo-EM or immunofluorescence; measure kinetochore-microtubule dynamics using live-cell imaging. Use purified components to reconstitute kinetochore assembly and test force generation.

## Common Misconceptions
- Kinetochores are static; they dynamically remodel as microtubules polymerize and depolymerize. - One kinetochore attaches to many microtubules; tension is distributed across the attachment site.

## Explainer

You already know that DNA is packaged into chromosomes and that the mitotic spindle checkpoint prevents cells from proceeding to anaphase until chromosomes are properly attached. The kinetochore is the molecular structure that connects these two systems — it is the physical bridge between a chromosome and the spindle microtubules that will pull it to one pole of the dividing cell. Think of it as a sophisticated coupling device: one face grips the centromeric DNA, while the other face grabs onto the dynamic plus-ends of spindle microtubules.

The **kinetochore** is not a single protein but a megadalton assembly of over 100 proteins organized into layers. The inner kinetochore sits directly on centromeric chromatin, built around specialized histone variants (CENP-A) that mark where the kinetochore should assemble. The outer kinetochore faces the cytoplasm and contains the **KMN network** — three subcomplexes called KNL1, MIS12, and NDC80. The NDC80 complex is the primary microtubule-binding component: its long, rod-shaped structure reaches out and directly contacts the tubulin subunits of kinetochore microtubules. Each kinetochore binds not just one microtubule but a bundle of them (around 20–25 in human cells), distributing the mechanical load of chromosome movement.

What makes the kinetochore remarkable is that it maintains attachment to microtubules that are constantly growing and shrinking. Microtubule plus-ends undergo **dynamic instability** — switching between polymerization and depolymerization — and the kinetochore rides these changes. During chromosome congression, the kinetochore tracks a depolymerizing microtubule end inward toward the pole and a polymerizing end outward. This requires the NDC80 complex and associated factors to form low-affinity, rapidly exchanging contacts with tubulin, rather than a rigid lock.

The kinetochore also serves as the platform for the **spindle assembly checkpoint** you studied earlier. When a kinetochore is unattached or incorrectly attached, checkpoint proteins (Mad1, Mad2, BubR1) accumulate there and generate a "wait" signal that inhibits the anaphase-promoting complex. The critical distinction is between **amphitelic attachment** — where sister kinetochores connect to microtubules from opposite poles, generating tension — and erroneous attachments like syntelic (both sisters to the same pole) or merotelic (one kinetochore to both poles). Tension across the kinetochore stretches the structure, physically separating kinase substrates from their phosphatases, which stabilizes correct attachments and destabilizes incorrect ones. Only when every chromosome achieves amphitelic attachment and sufficient tension does the checkpoint silence, allowing the cell to proceed into anaphase.
