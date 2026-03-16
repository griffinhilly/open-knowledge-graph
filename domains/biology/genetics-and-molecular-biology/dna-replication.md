---
id: dna-replication
title: DNA Replication
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-structure
  type: hard
- id: enzyme-structure-and-function
  type: soft
builds-toward:
- dna-mutations
- dna-repair-mechanisms
- pcr
- genomics-overview
tags:
- replication
- DNA polymerase
- semi-conservative
- Okazaki fragments
stage: abstract-reasoning
status: validated
---

# DNA Replication

## Core Idea
DNA replication copies the genome before cell division using a semi-conservative mechanism: each daughter molecule retains one original strand and one newly synthesized strand. DNA polymerase reads the template 3' to 5' and synthesizes the new strand 5' to 3', requiring a short RNA primer to initiate. The leading strand is synthesized continuously, while the lagging strand is built in discontinuous Okazaki fragments that are later joined by DNA ligase. Multiple origins of replication on eukaryotic chromosomes allow the large genome to be replicated efficiently.

## How It's Best Learned
Draw the replication fork showing helicase unwinding, primase adding primers, and both polymerases extending. Work through why one strand is continuous and the other discontinuous given the 5'-to-3' constraint.

## Common Misconceptions
- Students confuse the template strand direction with the synthesis direction; polymerase always extends in 5'→3'.
- 'Semi-conservative' is sometimes misunderstood as each daughter getting half of the original strands; each daughter gets one complete parental strand.

## Questions

```yaml
- question: "During DNA replication, DNA polymerase cannot begin synthesizing a new strand from scratch. What is the correct explanation for this limitation?"
  type: multiple-choice
  options: ["DNA polymerase can only extend an existing strand — it requires a free 3'-OH group to add the first nucleotide", "DNA polymerase only works in the 3'→5' direction and needs a primer to reverse direction", "The template strand must be fully unwound before synthesis can begin at any point", "ATP is not available at the start of replication to power the first nucleotide addition"]
  answer: 0
  explanation: "DNA polymerase adds nucleotides exclusively to the 3'-OH end of an existing strand. It cannot initiate synthesis de novo. The RNA primer synthesized by primase provides the initial 3'-OH group so DNA polymerase can begin extension. The primer is later removed and replaced with DNA."

- question: "In semi-conservative replication, each daughter DNA molecule contains a patchwork of old and new nucleotides distributed across both strands."
  type: true-false
  answer: false
  explanation: "Semi-conservative means each daughter molecule retains one complete, intact parental strand paired with one completely new strand — not a mixture within each strand. This was demonstrated by the Meselson-Stahl experiment: after one round of replication in light (¹⁴N) medium, each daughter molecule had exactly one heavy (¹⁵N parental) strand and one light (new) strand."

- question: "Why is the lagging strand synthesized as discontinuous Okazaki fragments rather than as one continuous strand like the leading strand?"
  type: short-answer
  answer: "DNA polymerase can only synthesize DNA in the 5'→3' direction. On the lagging strand template, this means synthesis must proceed away from the replication fork. As helicase unwinds more DNA, new primers must be laid down periodically, generating short Okazaki fragments that are later joined by DNA ligase."
  explanation: "The two template strands are antiparallel. The leading strand template (3'→5' relative to fork movement) allows continuous synthesis toward the fork. The lagging strand template runs 5'→3' toward the fork, so the polymerase must work away from the fork and restart repeatedly as new template is exposed. This is not an inefficiency but an unavoidable consequence of the directionality constraint on DNA polymerase."
```

## Explainer

Every cell division requires an exact copy of the genome to be passed to each daughter cell. DNA replication accomplishes this with remarkable fidelity — but understanding how it works requires thinking carefully about the constraints imposed by DNA chemistry and the enzymes that copy it.

The central feature of replication is that it is *semi-conservative*: each of the two strands of the original double helix serves as a template for synthesizing a new complementary strand. When replication is complete, you have two identical double-stranded molecules, each consisting of one original parental strand and one newly synthesized strand. This was confirmed by the Meselson-Stahl experiment: bacteria grown in heavy-nitrogen (¹⁵N) medium were shifted to normal (¹⁴N) medium, and after one generation the DNA had exactly intermediate density — one ¹⁵N strand and one ¹⁴N strand per molecule — consistent with semi-conservative replication and ruling out both conservative and dispersive models.

The molecular machinery begins at specific DNA sequences called *origins of replication*. Helicase unwinds and separates the two strands, creating a replication fork. Single-strand binding proteins stabilize the exposed strands and prevent them from reannealing. Then comes a critical chemical constraint: DNA polymerase can only add nucleotides to the 3'-OH end of an existing strand — it cannot initiate a new strand from scratch. This is why *primase* (an RNA polymerase) first synthesizes a short RNA primer, providing the 3'-OH group that DNA polymerase needs to begin extension. After replication, these RNA primers are removed and replaced with DNA, and any gaps are sealed by DNA ligase.

The antiparallel nature of the two template strands creates a fundamental asymmetry at the replication fork. DNA polymerase always synthesizes in the 5'→3' direction, reading the template 3'→5'. On the *leading strand*, the template runs 3'→5' in the direction of fork movement, so DNA polymerase can extend continuously toward the fork. On the *lagging strand*, however, the template runs 5'→3' toward the fork — meaning polymerase must work *away* from the fork. As helicase unwinds more template, primase must repeatedly lay down new RNA primers, and polymerase synthesizes short segments called *Okazaki fragments* in the opposite direction to fork movement. These fragments are later joined by DNA ligase into a continuous strand.

Eukaryotic chromosomes are vastly larger than prokaryotic chromosomes, so replicating from a single origin would take weeks. Eukaryotes solve this by firing many *origins of replication* simultaneously — hundreds to thousands per chromosome. Replication proceeds bidirectionally from each origin, creating expanding bubbles that merge as replication converges from neighboring origins. Strict regulation ensures each origin fires exactly once per cell cycle, preventing over-replication. This mechanism allows the entire human genome (about 6 billion base pairs) to be accurately copied within hours during S phase of the cell cycle.
