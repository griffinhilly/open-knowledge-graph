---
id: mitosis-stages-regulation
title: 'Mitosis: Regulated Chromosome Distribution'
domain: biology
course: cell-biology
prerequisites:
- id: mitosis
  type: hard
- id: cytokinesis
  type: hard
- id: cytoskeleton-cellular-framework
  type: hard
tags:
- mitosis
- division
- cytokinesis
stage: formal-systems
status: validated
---

# Mitosis: Regulated Chromosome Distribution

## Core Idea
Mitosis (prophase, prometaphase, metaphase, anaphase, telophase) precisely distributes replicated chromosomes to daughter cells through spindle fiber attachment to kinetochores. Sister chromatids separate and migrate to opposite poles. Cytokinesis divides cytoplasm (cleavage furrow in animals, cell plate in plants). This process is exquisitely regulated; errors cause aneuploidy and developmental abnormalities.

## How It's Best Learned
Observe each mitotic stage with fluorescent markers (DNA, tubulin, centrosomes). Use live-cell imaging to measure spindle dynamics and chromosome movement.

## Common Misconceptions
Mitosis is a single process—it is four distinct stages. Sister chromatids separate in anaphase I—that is meiosis I; mitosis separates sister chromatids in anaphase. Cytokinesis is always equal—some are asymmetric, producing daughter cells of different sizes.

## Questions

```yaml
- question: "During mitosis, one kinetochore on a chromosome fails to attach to microtubules from either pole. What happens next?"
  type: multiple-choice
  options:
    - "The cell proceeds to anaphase immediately, since one unattached kinetochore does not significantly delay division"
    - "The cell arrests in metaphase — the spindle assembly checkpoint detects the unattached kinetochore and inhibits the APC/C, preventing cohesin cleavage and chromatid separation"
    - "The cell skips anaphase and proceeds directly to telophase, distributing chromosomes unequally"
    - "The unattached chromosome is degraded, and mitosis continues with the remaining chromosomes"
  answer: 1
  explanation: "The spindle assembly checkpoint (SAC) is exquisitely sensitive: a single unattached or improperly attached kinetochore is sufficient to halt the entire process. The unattached kinetochore generates a 'wait' signal that inhibits the anaphase-promoting complex (APC/C). The APC/C is the ubiquitin ligase that would normally trigger cleavage of the cohesin proteins holding sister chromatids together. As long as the inhibitory signal persists, anaphase cannot begin. Only when all kinetochores are properly attached to microtubules from opposite poles is the checkpoint satisfied and division allowed to proceed."

- question: "What is the functional significance of chromosomes aligning at the metaphase plate before anaphase begins?"
  type: multiple-choice
  options:
    - "Alignment at the equator allows chromosomes to condense fully before being separated"
    - "Alignment ensures that each kinetochore is under tension from microtubules attached from opposite poles, which the spindle assembly checkpoint uses to confirm correct bi-orientation before allowing chromatid separation"
    - "Alignment reduces the distance chromosomes must travel to reach each pole, speeding up anaphase"
    - "Alignment at the metaphase plate is merely an artifact of balanced pulling forces with no regulatory significance"
  answer: 1
  explanation: "Metaphase plate alignment is not incidental — it reflects a mechanically verified state. A chromosome is bi-oriented when microtubules from both poles attach to its two sister kinetochores and place the chromosome under tension at the equator. This tension is sensed by the kinetochore and signals correct attachment. Chromosomes pulled toward only one pole (mono-oriented) are not under this tension and continue to generate the 'wait' signal. The metaphase plate is therefore a visual indicator that bi-orientation — and hence checkpoint satisfaction — is being achieved across all chromosomes."

- question: "In anaphase of mitosis, homologous chromosomes separate to opposite poles."
  type: true-false
  answer: false
  explanation: "This is the most common confusion between mitosis and meiosis. In anaphase of mitosis, sister chromatids separate to opposite poles — the cohesin holding the two copies of each replicated chromosome is cleaved, and each copy moves to a different pole. Homologous chromosome separation occurs in anaphase I of meiosis (the reductive division). Mitosis produces two genetically identical daughter cells, each with the same chromosome number as the parent; meiosis I produces cells with half the chromosome number by separating homologs."

- question: "The spindle assembly checkpoint can delay anaphase onset indefinitely, regardless of how many kinetochores are unattached, until all kinetochores achieve proper bi-oriented attachment."
  type: true-false
  answer: true
  explanation: "The checkpoint operates as a zero-tolerance system: as long as even one kinetochore remains unattached or incorrectly attached, it continues to produce inhibitory signals that block APC/C activation. This is not a counting mechanism that tolerates a few errors — it is an all-or-nothing gate. The biological logic is clear: if even one chromosome is misattached and distributed incorrectly, the daughter cells receive the wrong chromosome number (aneuploidy), which can cause developmental defects or cancer. The checkpoint's stringency ensures near-perfect fidelity."

- question: "Explain how the spindle assembly checkpoint prevents aneuploidy, and describe what happens in cells where this checkpoint fails."
  type: short-answer
  answer: "The spindle assembly checkpoint monitors kinetochore attachment during metaphase. Any unattached or mono-oriented kinetochore produces an inhibitory signal that prevents the anaphase-promoting complex (APC/C) from triggering cohesin cleavage. This delays anaphase until all chromosome pairs achieve bi-orientation — attachment by microtubules from opposite poles under tension. When the checkpoint is satisfied, the inhibitory signal ceases, APC/C is activated, cohesin is cleaved, and sister chromatids separate to opposite poles with high fidelity. When the checkpoint fails (as it commonly does in cancer cells due to mutations in checkpoint components), cells proceed to anaphase with improperly attached chromosomes, resulting in daughter cells with extra or missing chromosomes (aneuploidy). Aneuploidy drives genomic instability and contributes to tumor progression."
  explanation: "The key insight is that the checkpoint is a surveillance system, not a timer. It does not wait a fixed amount of time — it actively monitors attachment state and releases the brake only when mechanical bi-orientation is confirmed. Failure is catastrophic at the cellular level because each misattached chromosome produces one aneuploid daughter, and aneuploidy is associated with nearly all solid tumor cancers."
```

## Explainer

You already understand the basic concept of mitosis and cytokinesis as the processes that divide a cell into two genetically identical daughters. What this topic adds is the precise choreography of each stage and the regulatory machinery that makes the process extraordinarily reliable. Think of mitosis as a carefully scripted sequence where the cytoskeleton — the structural framework you studied earlier — is completely reorganized to build a **mitotic spindle**, a bipolar machine made of microtubules whose sole job is to pull chromosomes apart with near-perfect accuracy.

The five stages unfold in a specific order. In **prophase**, chromosomes condense from diffuse chromatin into compact rods, and the centrosomes migrate to opposite sides of the cell while nucleating microtubules. During **prometaphase**, the nuclear envelope breaks down and microtubules from each pole attach to protein structures called **kinetochores** on each sister chromatid — this attachment is the critical mechanical link between the spindle and the chromosomes. **Metaphase** is the alignment checkpoint: chromosomes line up along the cell's equator (the metaphase plate), and the cell verifies that every kinetochore is properly attached to microtubules from opposite poles. Only when this **spindle assembly checkpoint** is satisfied does the cell proceed to **anaphase**, where the cohesin proteins holding sister chromatids together are cleaved, and the separated chromatids are pulled to opposite poles by shortening microtubules. Finally, in **telophase**, nuclear envelopes reform around each set of chromosomes, and the chromatin decondenses.

The regulation of this process is what makes it biologically remarkable. The spindle assembly checkpoint acts as a surveillance system — if even a single kinetochore is unattached or improperly attached, the checkpoint delays anaphase by inhibiting the **anaphase-promoting complex (APC/C)**, a ubiquitin ligase that would otherwise trigger chromatid separation. This is why errors in chromosome distribution (aneuploidy) are rare in normal cells: the checkpoint literally halts the process until attachment is correct. When this checkpoint fails — as it often does in cancer cells — daughter cells receive the wrong number of chromosomes, driving genomic instability.

Cytokinesis, the physical division of the cytoplasm, overlaps with telophase and uses a fundamentally different mechanism than chromosome segregation. In animal cells, a **contractile ring** of actin and myosin filaments pinches the membrane inward to form a **cleavage furrow**. In plant cells, which have rigid cell walls, vesicles delivered by the cytoskeleton fuse at the midline to build a **cell plate** from the inside out. Not all cytokinesis is symmetric — stem cells, for example, often divide asymmetrically, distributing cell fate determinants unequally so that one daughter remains a stem cell while the other differentiates.
