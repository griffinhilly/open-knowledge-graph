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

## Questions

```yaml
- question: "A cell has abundant CDK2 protein but no cyclin E. What happens at the G1/S transition?"
  type: multiple-choice
  options:
    - "The cell proceeds through G1/S normally — CDK2 is the active enzyme and its presence is sufficient."
    - "The cell arrests permanently in G1 and cannot re-enter S phase under any circumstances."
    - "The G1/S transition is blocked — CDK2 is inactive without its cyclin E partner, so the cell cannot commit to DNA replication."
    - "The cell bypasses G1 and enters S phase using an alternative CDK that compensates for missing cyclin E."
  answer: 2
  explanation: "CDKs are always present in the cell but are inactive on their own — they require cyclin binding to become active. This is the key insight: it is cyclin levels, not CDK levels, that gate phase transitions. Cyclin E accumulates in late G1, binds CDK2, and the resulting active complex commits the cell to DNA replication. Without cyclin E, CDK2 sits idle regardless of its abundance. The oscillation of cyclin levels — not CDK expression — is the molecular clock of the cell cycle. Option A is the common misconception: knowing CDK2 is present doesn't tell you whether it's active."

- question: "Why is the restriction point in late G1 described as the most important decision point in the cell cycle?"
  type: multiple-choice
  options:
    - "It is the only point where DNA replication errors can be detected and corrected before mitosis."
    - "It is where most regulatory inputs converge — growth factor signals, DNA damage, contact inhibition — and crossing it commits the cell to division even if signals are withdrawn."
    - "It is where the cell decides between mitosis and meiosis, with meiosis selected when DNA damage is present."
    - "It is the rate-limiting step for overall cell cycle speed — G1 duration controls how quickly cells proliferate."
  answer: 1
  explanation: "The restriction point (R-point) in late G1 is where the cell becomes committed to division: before R, the cell needs continuous growth factor stimulation; after R, it proceeds even if growth factors are withdrawn. This is where cyclin D-CDK4/6 phosphorylates Rb, releasing E2F to drive S-phase gene expression. DNA damage signals (via p53 → p21), growth factor deprivation (reducing cyclin D), contact inhibition, and differentiation signals all converge at this point to restrain or permit progression. Cancer fundamentally involves bypass of this checkpoint — making it the primary site of oncogenic mutations."

- question: "Mutations that inactivate CDK inhibitors like p21 or delete p16 can contribute to cancer by allowing cells to bypass the restriction point and proliferate without appropriate growth signals."
  type: true-false
  answer: true
  explanation: "CDK inhibitors (CKIs) like p21 and p27 restrain CDK-cyclin complexes in response to growth factor withdrawal, DNA damage, and cellular stress. p21 is induced by p53 in response to DNA damage, blocking CDK2 activity and arresting cells in G1 for repair. p16 inhibits CDK4/6, keeping Rb in its growth-suppressive form. Inactivating these inhibitors — whether by mutation, deletion, or epigenetic silencing — removes the brakes at the restriction point, allowing cells to enter S phase and proliferate inappropriately. This is why loss of p16, loss of p21, and mutation of p53 are common events in cancer."

- question: "CDKs are expressed only during the phases they regulate — CDK2 is absent during G2 and M, CDK1 is absent during G1 and S — which is why cyclin oscillation drives phase transitions."
  type: true-false
  answer: false
  explanation: "CDKs are constitutively present throughout the cell cycle — their expression does not oscillate. What oscillates is cyclin abundance. Different cyclins are synthesized and degraded in a phase-specific pattern, and because CDKs only become active when bound to a cyclin partner, it is cyclin levels that determine when each CDK is active and thus which phase transition is driven. This is precisely why the cell cycle machinery is built around oscillating cyclins rather than oscillating kinases: the kinase is always ready; the regulatory 'switch' is whether the appropriate cyclin is present to activate it."

- question: "Explain the logic of why CDK activity is controlled by cyclin levels rather than by regulating CDK expression directly. What does this design accomplish?"
  type: short-answer
  answer: "CDKs are constitutively expressed at stable levels throughout the cell cycle, while cyclins are synthesized and degraded in a phase-specific pattern. CDK activity is therefore gated by cyclin availability: when the right cyclin accumulates, it binds and activates its CDK partner, driving the next phase transition; when cyclin is degraded, CDK activity falls. This design creates a rapid, switchlike response — CDK activity can rise or fall quickly depending on cyclin synthesis and degradation rates, without requiring changes in CDK gene expression. It also enables the cell to integrate multiple regulatory inputs (growth factors, damage signals) at the level of cyclin levels, since all these inputs converge on whether cyclin D accumulates in G1."
  explanation: "The separation between stable kinase and oscillating regulatory subunit allows fine-grained control with rapid dynamics. Degrading cyclin is faster than turning off gene expression; synthesizing a specific cyclin is faster than making a new kinase. The design also allows the same CDK (like CDK1) to drive different transitions when paired with different cyclins (cyclin A vs cyclin B), expanding the toolkit without multiplying kinase genes. Cancer exploits this logic by overexpressing cyclins or deleting CKIs to constitutively activate CDK complexes."
```

## Explainer

From the cell cycle overview, you know that cells grow, duplicate their DNA, and divide. The phases and transitions topic adds the molecular machinery that controls *when* each step happens — and, critically, what prevents a cell from proceeding when conditions are wrong. The cell cycle is divided into four phases arranged in order: **G1** (gap 1), **S** (synthesis), **G2** (gap 2), and **M** (mitosis plus cytokinesis). G1, S, and G2 together constitute **interphase**, the long period between divisions when the cell is growing, metabolizing, and (during S phase) replicating its DNA.

The transitions between phases are not automatic — they are controlled by a family of enzymes called **cyclin-dependent kinases (CDKs)**. CDKs are protein kinases that are always present in the cell but are inactive on their own. They become active only when bound to a specific **cyclin** partner, and cyclin levels rise and fall in a predictable pattern across the cell cycle. This means CDK activity is determined by which cyclin is currently abundant. In late G1, **cyclin D** accumulates in response to growth factor signaling and activates CDK4/6, which phosphorylates the retinoblastoma protein (Rb), releasing the E2F transcription factor to drive expression of S-phase genes. At the G1/S boundary, **cyclin E-CDK2** commits the cell to DNA replication. During S phase, **cyclin A-CDK2** helps fire replication origins and prevents re-replication. At the G2/M transition, **cyclin B-CDK1** (historically called MPF, maturation-promoting factor) triggers the dramatic events of mitosis: chromosome condensation, nuclear envelope breakdown, and spindle assembly.

The **restriction point** in late G1 is the most important decision point in the cell cycle. Before this point, the cell requires continuous growth factor stimulation to proceed; after it, the cell is committed to division even if growth factors are withdrawn. This is where most regulatory inputs converge: DNA damage activates p53, which induces the CDK inhibitor **p21**, arresting the cell in G1 to allow repair. Growth factor deprivation reduces cyclin D levels, stalling CDK4/6 activity. Contact inhibition and differentiation signals similarly halt the cycle here. Cells that exit the cycle enter a quiescent state called **G0**, from which they may re-enter G1 if stimulated.

Understanding these transitions explains why cancer is fundamentally a disease of cell cycle control. Mutations that constitutively activate cyclins (cyclin D overexpression), inactivate CDK inhibitors (p16 deletion, p21 loss), or disable checkpoint proteins (p53 mutation) allow cells to bypass the restriction point and proliferate without appropriate signals. This is why so many cancer therapies — including CDK4/6 inhibitors like palbociclib — target the cell cycle machinery directly. The logic of the cell cycle is the logic of controlled proliferation, and its failure is the logic of cancer.
