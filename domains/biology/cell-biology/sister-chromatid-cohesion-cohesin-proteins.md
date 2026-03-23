---
id: sister-chromatid-cohesion-cohesin-proteins
title: Sister Chromatid Cohesion and Cohesin
domain: biology
course: cell-biology
prerequisites:
- id: dna-replication
  type: hard
- id: mitosis
  type: hard
builds-toward:
- anaphase-promoting-complex-cell-cycle-control
tags:
- sister-chromatids
- cohesin
- chromosome-segregation
stage: formal-systems
status: validated
---

# Sister Chromatid Cohesion and Cohesin

## Core Idea
Sister chromatid cohesion, mediated by the cohesin ring complex (SMC1, SMC3, SCC1, SCC3 subunits), holds newly replicated chromatids together until anaphase onset. Cohesin is loaded onto DNA by Scc2/Scc4 during S phase and forms large rings believed to topologically entrap sister chromatids. Cohesion is released in two stages: arm (non-centromeric) cohesion dissolves during prophase via Wapl-mediated release, while centromeric cohesion persists until APC/C-triggered securin degradation during anaphase.

## How It's Best Learned
Track cohesin loading and dynamics using time-lapse fluorescence microscopy; measure cohesion strength using anaphase bridge assays. Examine cohesin structure by cryo-EM; test its DNA-entrapping function experimentally.

## Common Misconceptions
- Cohesin glues chromatids together via adhesion; it topologically entraps DNA in a ring structure. - All cohesion is released at once; arm and centromeric cohesion have distinct release mechanisms.

## Questions

```yaml
- question: "A mutation eliminates the Shugoshin protein in a dividing cell. What is the most likely consequence during mitosis?"
  type: multiple-choice
  options:
    - "Cohesin fails to load onto chromosomes during S phase, causing premature sister separation before mitosis begins"
    - "Centromeric cohesin is removed during prophase along with arm cohesin, causing sisters to separate before proper spindle attachment"
    - "The cell cannot enter anaphase because securin is not degraded by the APC/C"
    - "Chromosome condensation fails during prophase because arm cohesin removal is blocked"
  answer: 1
  explanation: "Shugoshin protects centromeric cohesin from Wapl-mediated removal during prophase. Without Shugoshin, Wapl removes centromeric cohesin simultaneously with arm cohesin, causing sisters to separate prematurely before the spindle has made proper bioriented attachments. This leads to random chromosome segregation and aneuploidy. The two-step release exists precisely to keep sisters connected at the centromere until the cell is ready to divide."

- question: "Cohesin is described as holding sister chromatids together by 'topological entrapment.' What does this mean?"
  type: multiple-choice
  options:
    - "Cohesin forms a physical adhesive bond to the DNA backbone at multiple sites along the chromatid length"
    - "The cohesin ring encircles both sister chromatid DNA molecules so they are physically trapped inside the ring without covalent bonds to the DNA"
    - "Cohesin wraps tightly around the DNA helix to prevent strand separation under mechanical tension from the spindle"
    - "Cohesin uses ATP-dependent clamping to compress both chromatids together at defined intervals"
  answer: 1
  explanation: "The topological entrapment model means the ring physically surrounds both DNA molecules — they are threaded through the ring interior like two threads through a loop. This is distinct from chemical adhesion (option A) because the ring holds without covalent bonds and can be released simply by opening. This explains why separase cleavage of the SCC1 subunit is sufficient to release cohesion at anaphase: opening the ring allows the DNA molecules to fall out."

- question: "Cohesin is loaded onto chromosomes after DNA replication is complete, so that both sister chromatids can be captured together once they exist."
  type: true-false
  answer: false
  explanation: "Cohesin is loaded *during* S phase, as replication forks pass through — not after replication is complete. The timing is critical: cohesin must be established behind the replication fork so that newly synthesized sister chromatids are captured together the moment they emerge. Loading after replication would miss the window when the sisters are in close proximity and could be co-entrapped by the ring."

- question: "The removal of arm cohesion during prophase requires the protease separase to cleave the SCC1 subunit of cohesin."
  type: true-false
  answer: false
  explanation: "Prophase arm cohesion removal is mediated by *Wapl* — a regulatory protein that opens the cohesin ring — not separase. Separase is the protease responsible only for cleaving centromeric cohesin at the metaphase-to-anaphase transition, and it is held inactive by securin until APC/C activation. This two-step mechanism — Wapl removes arm cohesin, separase cleaves centromeric cohesin — is precisely what defines the two distinct stages of cohesion release."

- question: "Why is the two-stage release of cohesin (arm cohesion in prophase, centromeric cohesion at anaphase) functionally important for accurate chromosome segregation?"
  type: short-answer
  answer: "Arm cohesion removal during prophase allows chromosomes to condense into compact X-shaped structures accessible to the spindle, while retaining centromeric cohesion ensures sisters remain physically connected until the spindle has made proper bioriented attachments at both kinetochores. If all cohesion were released at once — or if centromeric cohesion were lost before biorientation — sisters could segregate randomly, producing aneuploidy. The two-step system couples the final cohesion release to the metaphase-to-anaphase checkpoint, ensuring separation only occurs when the cell is ready."
  explanation: "The spatial logic is key: Shugoshin protects only centromeric cohesin, so arm cohesin (distributed along chromosome arms) is removed first. This staged release trades some compaction benefit against the safety of keeping sisters tethered until the last moment — a design that minimizes segregation errors."
```

## Explainer

From your study of DNA replication and mitosis, you know that each chromosome is copied during S phase, producing two identical **sister chromatids** joined at the centromere. You also know that during mitosis, these sisters must be pulled apart to opposite poles of the cell. But what physically holds them together in the first place? The answer is a ring-shaped protein complex called **cohesin**.

Cohesin is built from four core subunits — **SMC1**, **SMC3**, **SCC1** (also called Rad21), and **SCC3** — that form a large ring roughly 40 nanometers in diameter. The prevailing model is that this ring **topologically entraps** both sister chromatids: rather than binding to DNA through chemical adhesion (like a glue), the ring encircles both DNA molecules, threading them through its interior like two threads through a single loop. This entrapping mechanism is elegant because it holds the sisters together without covalently modifying the DNA and can be released simply by opening the ring.

Cohesin is loaded onto chromosomes by the **Scc2/Scc4** loader complex during S phase, as replication forks pass through. The timing is critical: cohesion must be established behind the replication fork so that newly synthesized sister chromatids are captured together. Once loaded, cohesin holds sisters together along their entire length — not just at the centromere. This is where the **two-step release** mechanism becomes important. During prophase, a protein called **Wapl** removes cohesin from chromosome arms, allowing the arms to separate and chromosomes to condense into the compact X-shaped structures visible under the microscope. However, centromeric cohesin is protected from Wapl by the protein Shugoshin, keeping sisters connected at the centromere.

The final release occurs at the **metaphase-to-anaphase transition**. The anaphase-promoting complex (APC/C) triggers destruction of securin, which had been inhibiting the protease separase. Once freed, separase cleaves the SCC1 subunit of centromeric cohesin, opening the ring and allowing sister chromatids to separate. This two-stage system — prophase arm removal followed by anaphase centromeric cleavage — ensures that chromatids remain connected at the centromere long enough for proper spindle attachment, but separate cleanly when the cell is ready to divide. Defects in cohesin or its regulators lead to chromosome missegregation, aneuploidy, and are implicated in both cancer and developmental disorders like Cornelia de Lange syndrome.
