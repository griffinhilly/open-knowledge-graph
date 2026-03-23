---
id: complement-cascade-and-pathways
title: Complement System Activation Pathways
domain: biology
course: immunology
prerequisites:
- id: innate-immune-response
  type: hard
- id: protein-structure-and-function
  type: soft
builds-toward:
- inflammation-innate-response
- antibody-isotypes
tags:
- complement
- cascade
- innate-immunity
stage: expert
status: draft
---

# Complement System Activation Pathways

## Core Idea
The complement system is a cascade of ~30 proteins that amplifies inflammation and promotes pathogen destruction through three activation pathways: classical (IgM/IgG binding), alternative (pathogen surfaces), and lectin (mannose-binding lectin). All three converge at C3 activation, generating the C3b opsonin and C3a chemoattractant, ultimately forming the C5b-9 membrane attack complex (MAC). Complement amplification is tightly regulated to prevent self-tissue damage.

## How It's Best Learned
Diagram all three pathways from initiation to MAC formation, highlighting convergence at C3 and C5. Identify the key proteases (C1q, factor B, MASP2) and regulatory proteins in each pathway.

## Common Misconceptions
- Complement only functions through the classical pathway with antibodies (the alternative and lectin pathways function independently). - All complement proteins are equally abundant (C3 and C4 are highly concentrated; later components are scarce).

## Questions

```yaml
- question: "A patient has a complete deficiency in C1q, disabling the classical complement pathway. They encounter a bacterial pathogen for the first time (no antibodies present yet). What happens to complement activation?"
  type: multiple-choice
  options:
    - "No complement activation occurs — without C1q, the cascade cannot start"
    - "The alternative and lectin pathways can still activate complement independently, converging at C3"
    - "Complement activates but cannot proceed past C3b deposition"
    - "The lectin pathway is also disabled because it shares C1q as an initiator"
  answer: 1
  explanation: "The classical pathway requires C1q binding to antibody-antigen complexes — it bridges innate and adaptive immunity. But the lectin pathway uses MBL/ficolins to recognize mannose arrays on microbial surfaces, and the alternative pathway activates constitutively through C3 'tick-over' on any surface lacking host regulatory proteins. Both are antibody-independent. A C1q-deficient patient still has two functional pathways that converge at C3 cleavage, meaning C3b opsonization and MAC formation can still proceed. This is why the misconception 'complement only works with antibodies' is wrong — the lectin and alternative pathways evolved specifically for antibody-independent early defense."

- question: "C3b has been deposited on the surface of an invading bacterium. What is the primary functional consequence?"
  type: multiple-choice
  options:
    - "C3b directly punches a hole in the bacterial membrane, causing osmotic lysis"
    - "C3b acts as an opsonin, marking the bacterium for phagocytosis via complement receptors on macrophages and neutrophils"
    - "C3b triggers intersystem crossing within the bacterium's electron transport chain"
    - "C3b activates caspases in the bacterium, initiating bacterial apoptosis"
  answer: 1
  explanation: "C3b is the central opsonin of the complement system. When C3b cleaves from C3, a highly reactive thioester bond is exposed that covalently attaches C3b to the pathogen surface within milliseconds. Phagocytes (macrophages and neutrophils) express complement receptors (CR1, CR3) that bind C3b, greatly enhancing phagocytosis efficiency — a process called complement-mediated opsonization. C3b also serves as the nucleation point for assembly of the C5 convertase, which eventually generates the MAC. Direct lysis via MAC (the pore-forming complex) is actually a downstream event assembled from C5b-9, not from C3b itself."

- question: "The alternative complement pathway requires antibody binding to a pathogen surface before it can be activated."
  type: true-false
  answer: false
  explanation: "The alternative pathway is entirely antibody-independent. It operates through spontaneous hydrolysis of C3 in plasma ('tick-over'), generating small amounts of C3(H₂O) continuously. This reactive form of C3 deposits on nearby surfaces. On host cells, regulatory proteins (DAF/CD55, Factor H) immediately degrade the deposited complement components. On pathogen surfaces, which lack these regulators, the deposited components are stabilized and amplification proceeds. The alternative pathway is therefore always 'on' at a low level, ready to amplify on any foreign surface — it represents the oldest, most evolutionarily primitive arm of complement."

- question: "Host cells are protected from complement-mediated lysis in part by surface proteins that block MAC assembly."
  type: true-false
  answer: true
  explanation: "CD59 (protectin) is a GPI-anchored surface protein on host cells that binds C8 and C9 during MAC assembly, preventing the polymerization of poly-C9 that forms the actual transmembrane pore. DAF (CD55) provides additional protection upstream by accelerating decay of C3 convertases, reducing C3b deposition. The disease paroxysmal nocturnal hemoglobinuria (PNH) arises from a somatic mutation in the enzyme that attaches GPI anchors — red blood cells lacking CD55 and CD59 are destroyed by complement-mediated hemolysis, causing the characteristic hemoglobinuria and anemia."

- question: "Why is tight regulation of the complement system essential, and what happens when this regulation fails?"
  type: short-answer
  answer: "Complement is an amplifying proteolytic cascade — each activated component cleaves multiple copies of the next, producing rapid and massive effector responses. Without tight regulation, this amplification would attack host cells as readily as pathogens, since complement proteins do not intrinsically distinguish self from non-self. Host cells are protected by surface-bound regulators (DAF/CD55 prevents C3 convertase assembly; CD59 blocks MAC formation; Factor H redirects the alternative pathway away from self surfaces). When these fail — as in paroxysmal nocturnal hemoglobinuria, where loss of GPI-anchored proteins removes CD55 and CD59 from red blood cells — complement attacks host cells, causing hemolysis. Conversely, complement deficiencies (especially C3 or early classical pathway components) remove a critical layer of innate defense, predisposing to recurrent bacterial infections, particularly with encapsulated bacteria."
  explanation: "The complement system illustrates a general principle in immunology: powerful effector systems require equally powerful checkpoints. The same logic applies to the coagulation cascade, cytokine signaling, and adaptive immune activation. Understanding the regulators is as important as understanding the effectors — both for understanding disease and for designing therapies (e.g., eculizumab, which blocks C5, is used to treat PNH)."
```

## Explainer

From your study of innate immunity, you know that the body's first line of defense relies on pattern recognition — detecting molecular features common to pathogens but absent from host cells. The **complement system** is one of the most powerful effector arms of innate immunity: a cascade of approximately 30 serum proteins, mostly produced by the liver, that circulate in inactive forms and become sequentially activated at sites of infection. Think of it as a molecular domino chain — once triggered, each activated component cleaves and activates the next, producing rapid amplification from a small initial signal.

Three distinct pathways trigger the cascade, each recognizing pathogens through a different mechanism. The **classical pathway** begins when the C1 complex (specifically C1q) binds to antibodies (IgM or IgG) that are already bound to a pathogen surface — this is where complement bridges innate and adaptive immunity. The **lectin pathway** is triggered when **mannose-binding lectin (MBL)** or ficolins recognize specific sugar patterns (like mannose arrays) on microbial surfaces, which are rare on mammalian cells. The **alternative pathway** is constitutively active at a low level through spontaneous hydrolysis of C3 ("tick-over") and amplifies on any surface that lacks the regulatory proteins found on host cells. Despite their different triggers, all three pathways converge at the same critical step: cleavage of **C3** into **C3a** and **C3b**.

This convergence point is where the real power of complement lies. **C3b** covalently attaches to the pathogen surface and serves as an **opsonin** — a molecular "eat me" flag recognized by complement receptors on phagocytes like macrophages and neutrophils. Each deposited C3b can also recruit more complement components, creating a positive feedback loop that coats the pathogen in thousands of C3b molecules within minutes. Meanwhile, **C3a** (and later **C5a**) are released as **anaphylatoxins** — small soluble fragments that recruit inflammatory cells, increase vascular permeability, and trigger mast cell degranulation. The downstream cascade continues through C5 cleavage, generating C5b, which nucleates the assembly of C6, C7, C8, and multiple copies of C9 into the **membrane attack complex (MAC)** — a transmembrane pore that punctures the pathogen's membrane and causes osmotic lysis.

The complement system's destructive power makes tight regulation essential. Host cells are protected by surface-bound regulatory proteins like **decay-accelerating factor (DAF/CD55)**, which accelerates the breakdown of C3 convertases, and **CD59 (protectin)**, which blocks MAC assembly. Deficiencies in these regulators cause diseases in which complement attacks the body's own cells — paroxysmal nocturnal hemoglobinuria (PNH) results from loss of DAF and CD59 on red blood cells, leading to chronic complement-mediated hemolysis. Conversely, complement deficiencies (especially in C3 or the early classical pathway components) predispose individuals to recurrent bacterial infections, underscoring the system's central role in host defense.
