---
id: cell-cycle-phases-transitions
title: Cell Cycle Phases and Phase Transitions
domain: biology
course: cell-biology
prerequisites:
- id: cell-cycle-overview
  type: hard
builds-toward:
- cell-differentiation-lineage
tags:
- cell-cycle
- phases
- g1-s-g2-m
- cyclin-cdk
stage: advanced
status: draft
---

# Cell Cycle Phases and Phase Transitions

## Core Idea
The cell cycle is divided into G1 (gap 1, cell growth), S (DNA synthesis), G2 (gap 2, growth and preparation for mitosis), and M (mitosis and cytokinesis). Progression through phase transitions is controlled by cyclin-dependent kinases (CDKs) activated by cyclins: G1/S transition requires cyclin-CDK2; S/G2 and G2/M transitions require cyclin-CDK1. CDK inhibitors (p21, p27) restrain progression in response to growth factor withdrawal, DNA damage, or stress. Understanding these transitions is essential for understanding cancer, where CDK inhibitors are often inactivated.

## How It's Best Learned
Track cyclin expression and CDK activity across the cell cycle via Western blotting; measure DNA content by flow cytometry to assess cell cycle phase.

## Common Misconceptions
The cell cycle is often drawn as a simple wheel with equal phases. In reality, G1 is highly variable (hours to years in quiescent cells); S is relatively constant (~8 h); G2 is brief (~4 h); M is fastest (~1 h).

## Explainer

From the cell cycle overview, you know that cells grow, duplicate their DNA, and divide. The phases and transitions topic adds the molecular machinery that controls *when* each step happens — and, critically, what prevents a cell from proceeding when conditions are wrong. The cell cycle is divided into four phases arranged in order: **G1** (gap 1), **S** (synthesis), **G2** (gap 2), and **M** (mitosis plus cytokinesis). G1, S, and G2 together constitute **interphase**, the long period between divisions when the cell is growing, metabolizing, and (during S phase) replicating its DNA.

The transitions between phases are not automatic — they are controlled by a family of enzymes called **cyclin-dependent kinases (CDKs)**. CDKs are protein kinases that are always present in the cell but are inactive on their own. They become active only when bound to a specific **cyclin** partner, and cyclin levels rise and fall in a predictable pattern across the cell cycle. This means CDK activity is determined by which cyclin is currently abundant. In late G1, **cyclin D** accumulates in response to growth factor signaling and activates CDK4/6, which phosphorylates the retinoblastoma protein (Rb), releasing the E2F transcription factor to drive expression of S-phase genes. At the G1/S boundary, **cyclin E-CDK2** commits the cell to DNA replication. During S phase, **cyclin A-CDK2** helps fire replication origins and prevents re-replication. At the G2/M transition, **cyclin B-CDK1** (historically called MPF, maturation-promoting factor) triggers the dramatic events of mitosis: chromosome condensation, nuclear envelope breakdown, and spindle assembly.

The **restriction point** in late G1 is the most important decision point in the cell cycle. Before this point, the cell requires continuous growth factor stimulation to proceed; after it, the cell is committed to division even if growth factors are withdrawn. This is where most regulatory inputs converge: DNA damage activates p53, which induces the CDK inhibitor **p21**, arresting the cell in G1 to allow repair. Growth factor deprivation reduces cyclin D levels, stalling CDK4/6 activity. Contact inhibition and differentiation signals similarly halt the cycle here. Cells that exit the cycle enter a quiescent state called **G0**, from which they may re-enter G1 if stimulated.

Understanding these transitions explains why cancer is fundamentally a disease of cell cycle control. Mutations that constitutively activate cyclins (cyclin D overexpression), inactivate CDK inhibitors (p16 deletion, p21 loss), or disable checkpoint proteins (p53 mutation) allow cells to bypass the restriction point and proliferate without appropriate signals. This is why so many cancer therapies — including CDK4/6 inhibitors like palbociclib — target the cell cycle machinery directly. The logic of the cell cycle is the logic of controlled proliferation, and its failure is the logic of cancer.
