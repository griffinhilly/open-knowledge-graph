---
id: bacteriophage-taxonomy-lytic-lysogenic
title: 'Bacteriophages: Taxonomy and Lytic-Lysogenic Cycles'
domain: biology
course: microbiology
prerequisites:
- id: viral-classification-and-genome-types
  type: hard
- id: lysogenic-conversion-virulence-factors
  type: soft
builds-toward:
- crispr-cas-systems-bacterial-defense
tags:
- bacteriophages
- lytic
- lysogenic
stage: advanced
status: validated
---

# Bacteriophages: Taxonomy and Lytic-Lysogenic Cycles

## Core Idea
Bacteriophages (phages) are viruses that infect bacteria. The lytic cycle produces progeny and lyses the host; the lysogenic cycle integrates the prophage into the chromosome for dormant replication. Temperate phages can switch between cycles in response to stress. Phages are the most abundant organisms on Earth and shape microbial ecology and evolution.

## How It's Best Learned
Perform phage plaque assays to quantify viral titer. Observe lysogenic bacteria immune to superinfection by the same phage.

## Common Misconceptions
Lysogenic bacteria do not produce phage continuously—they are usually immune. Integration is not always exact; some prophages carry only partial genes, affecting virulence.

## Questions

```yaml
- question: "A lysogenic bacterium carrying a prophage is exposed to intense UV radiation that damages its DNA. What is the most likely outcome?"
  type: multiple-choice
  options:
    - "The prophage remains silently dormant — UV radiation affects only chromosomal DNA, not integrated prophage sequences"
    - "The bacterium's SOS DNA damage response inactivates the phage repressor, triggering prophage excision and a lytic replication cycle"
    - "The bacterium spontaneously releases phage particles from membrane vesicles to infect neighbors"
    - "The prophage degrades alongside the damaged bacterial chromosome without producing progeny"
  answer: 1
  explanation: "DNA damage triggers the bacterial SOS response, which activates RecA protein. Activated RecA cleaves the phage CI repressor (the protein that maintains lysogeny by blocking lytic gene expression). With the repressor inactivated, lytic genes are de-repressed, the prophage excises from the chromosome, and the lytic replication cycle begins. This is not a malfunction — it is the prophage's adaptive escape mechanism: when the host is doomed by severe DNA damage, it is advantageous for the phage to abandon ship and produce new particles."

- question: "A lysogenic bacterium carrying prophage λ is superinfected with additional λ phage particles from outside the cell. What happens to the incoming phage?"
  type: multiple-choice
  options:
    - "The cell undergoes double lysogeny, integrating both copies of the phage genome"
    - "The superinfecting phage immediately triggers the lytic cycle in the already-lysogenic cell"
    - "The incoming phage is excluded because the resident prophage's repressor protein blocks lytic gene expression in any new λ phage that enters"
    - "The new phage DNA recombines with the prophage, producing defective hybrid particles"
  answer: 2
  explanation: "Superinfection immunity is one of the most important consequences of lysogeny. The CI repressor encoded by the prophage diffuses throughout the cell and binds the operator sequences of any newly incoming λ phage, preventing its lytic genes from being expressed. The superinfecting phage's DNA enters the cell but cannot replicate or kill the host. This immunity is specific to phages of the same type — it provides no protection against phages with different repressor specificity. It is a key observable phenotype used to confirm true lysogeny."

- question: "Lysogenic bacteria continuously produce and release low levels of phage particles throughout their normal growth cycle, maintaining a constant low-level infection in the population."
  type: true-false
  answer: false
  explanation: "This is a common misconception. In the lysogenic state, the prophage is silently integrated and replicated passively with the bacterial chromosome — no phage particles are assembled or released. The lysogenic bacterium behaves like a normal, uninfected cell (and is in fact more resistant to infection than one, due to superinfection immunity). Phage particles are only produced if the lytic cycle is induced — typically by SOS-activating stress. The distinction between dormant prophage and active lytic replication is the essence of the lysogenic life cycle."

- question: "The decision of a temperate phage to enter either the lytic or lysogenic cycle after infecting a new bacterium can be influenced by environmental conditions experienced by the host."
  type: true-false
  answer: true
  explanation: "Temperate phages like λ 'sense' host physiology when deciding between lytic and lysogenic outcomes. A well-nourished, healthy bacterium signals good conditions for integration — riding along with a healthy host is a better bet. High multiplicity of infection (many phage per bacterium) also favors lysogeny, since lysis of all hosts simultaneously would leave no survivors to infect. Conversely, a stressed host with activated SOS pathways signals danger, biasing toward lytic replication. This decision is mediated by the relative activities of phage gene products (CI repressor vs. Cro protein) and their response to host signals — a molecular logic circuit, not a random choice."

- question: "Why is the lysogenic cycle described as 'molecular bet-hedging,' and what specific signal triggers the switch from lysogeny to lytic replication?"
  type: short-answer
  answer: "Bet-hedging describes a strategy where an organism maintains two alternative states — one safe under good conditions, one effective under bad — rather than committing fully to either. In lysogeny, the phage integrates into the bacterial chromosome and replicates passively with the host: safe, invisible, and long-lived in a healthy bacterial population. The risk is that if the host dies from non-phage causes, the phage dies with it. The trigger for switching to lytic replication is the bacterial SOS response — specifically, DNA damage activating RecA, which cleaves the phage CI repressor. This is a reliable signal that the host is doomed, making it adaptive for the phage to exit, replicate, and find new hosts before the bacterium dies."
  explanation: "The bet-hedging logic explains why temperate phages are so evolutionarily successful: they survive boom times by hiding in healthy hosts and escape bust times by abandoning doomed ones. The SOS system is the phage's way of reading the host's stress status without any direct sensory apparatus of its own."
```

## Explainer

From viral classification, you know that viruses are categorized by their genome type (DNA or RNA, single- or double-stranded) and replication strategy. Bacteriophages — viruses that infect bacteria — follow these same principles but add a dimension that most animal viruses lack: the choice between immediate destruction of the host and long-term coexistence with it.

**Phage taxonomy** mirrors general viral classification. Phages are grouped into families based on morphology and genome type. The tailed phages (order *Caudovirales*) are the most abundant and well-studied, featuring an icosahedral head packed with double-stranded DNA and a tail apparatus that attaches to the bacterial surface and injects the genome. Other phage families include filamentous phages (like M13, with circular single-stranded DNA), RNA phages, and small icosahedral DNA phages. Despite this diversity, the core replication logic is the same: attach, inject genetic material, hijack the host's machinery, and produce progeny.

The critical distinction is between **lytic** and **lysogenic** life cycles. A strictly **lytic phage** (also called a virulent phage) follows a one-way path: it injects its DNA, immediately commandeers the host's ribosomes and polymerases to make phage proteins and replicate phage DNA, assembles new phage particles inside the cell, and then produces lysozyme or holin proteins that rupture the bacterial cell wall, releasing typically 50–200 new phage particles to infect neighboring cells. The entire cycle takes 20–60 minutes. From the bacterium's perspective, infection is a death sentence.

**Temperate phages** have a second option. After injecting their DNA, they can enter the **lysogenic cycle** instead: the phage genome integrates into the bacterial chromosome (becoming a **prophage**) and replicates passively every time the bacterium divides. The bacterium suffers no harm and is, in fact, immune to superinfection by the same phage type — a repressor protein encoded by the prophage blocks expression of lytic genes and prevents additional copies of the same phage from initiating a lytic cycle. The prophage can remain dormant for hundreds of bacterial generations. However, when the host cell encounters severe stress — DNA damage, UV radiation, nutrient starvation — the SOS response inactivates the repressor, the prophage excises from the chromosome, and the lytic cycle resumes. This "molecular bet-hedging" strategy allows temperate phages to ride along safely during good times and escape from a doomed host during bad times, making them extraordinarily successful in microbial ecosystems.
