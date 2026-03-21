---
id: autoimmunity-mechanisms
title: Autoimmunity and Autoimmune Disease
domain: biology
course: immunology
prerequisites:
- id: regulatory-t-cells-immune-tolerance
  type: hard
- id: hypersensitivity-reactions
  type: soft
tags:
- pathology
- autoimmunity
- tolerance-breakdown
stage: advanced
status: draft
---

# Autoimmunity and Autoimmune Disease

## Core Idea
Autoimmunity results from loss of self-tolerance through genetic predisposition (HLA associations), environmental triggers (infections, molecular mimicry), and breakdown of regulatory mechanisms (Treg deficiency, Breg dysfunction). Autoimmune diseases range from organ-specific (Type 1 diabetes, rheumatoid arthritis) to systemic (lupus). Diagnosis relies on detecting pathogenic autoantibodies and autoreactive T cells.

## Questions

```yaml
- question: "A patient carries HLA-DR4, a risk allele for rheumatoid arthritis. At age 40, following a bacterial infection, she develops joint inflammation and tests positive for anti-citrullinated protein antibodies. Her identical twin, also carrying HLA-DR4, remains healthy at age 55. What best explains this discrepancy?"
  type: multiple-choice
  options:
    - "HLA-DR4 does not actually increase rheumatoid arthritis risk — it is an unrelated genetic marker"
    - "The twin is protected by stronger central tolerance that more efficiently deletes self-reactive T cells"
    - "Autoimmune disease requires multiple converging factors — genetic predisposition alone is insufficient; an environmental trigger and failure of peripheral tolerance must also occur"
    - "The patient's central tolerance is fully intact; peripheral tolerance is her only deficiency"
  answer: 2
  explanation: "This is the multi-hit model of autoimmunity in practice. HLA-DR4 increases risk but is not deterministic — the majority of HLA-DR4 carriers never develop rheumatoid arthritis. The patient required three converging factors: the genetic predisposition (HLA-DR4), an environmental trigger (the bacterial infection, potentially acting through molecular mimicry or releasing sequestered antigens), and a failure of peripheral tolerance (Treg dysfunction or anergy breakdown) that allowed self-reactive cells to persist and expand. The twin, sharing the same genetic risk, did not encounter the necessary environmental and regulatory co-factors."

- question: "Which of the following best describes the mechanism of molecular mimicry in autoimmunity?"
  type: multiple-choice
  options:
    - "Pathogens insert foreign DNA into host immune cells, reprogramming them to attack self-tissue"
    - "Immune responses generated against a pathogen cross-react with structurally similar self-proteins, triggering persistent autoimmune attack after the infection resolves"
    - "Self-reactive T cells that escaped thymic deletion are activated directly by inflammatory cytokines without any pathogen involvement"
    - "Regulatory T cells misidentify self-antigens as foreign and activate autoreactive B cells"
  answer: 1
  explanation: "Molecular mimicry occurs when pathogen proteins share structural (sequence or conformational) similarity with self-proteins. The adaptive immune response generated during infection — T cells and antibodies that effectively clear the pathogen — cross-reacts with the mimicked self-antigen. After the pathogen is cleared, the self-reactive response persists, producing sustained autoimmune damage. Rheumatic fever is the textbook example: antibodies against streptococcal M protein cross-react with cardiac myosin, causing valve damage. The mechanism explains why infections can trigger autoimmunity in genetically susceptible individuals."

- question: "Central tolerance in the thymus eliminates all self-reactive T cells, making peripheral tolerance merely a redundant backup that is rarely needed in healthy individuals."
  type: true-false
  answer: false
  explanation: "Central tolerance is imperfect by design. Some self-antigens are not expressed in the thymus (tissue-specific antigens may be absent or present at too low a level to drive deletion), and the deletion threshold is not absolute — some weakly self-reactive cells survive. Peripheral tolerance is essential and active: anergy, Treg suppression, and activation-induced cell death continuously manage the self-reactive cells that escaped central deletion. IPEX syndrome — caused by FoxP3 mutations that abolish Treg function — produces severe, fatal multi-organ autoimmunity even with intact central tolerance, demonstrating that peripheral tolerance is not merely backup."

- question: "Organ-specific and systemic autoimmune diseases differ primarily in which type of immune effector mediates the damage (antibody-mediated vs. T cell-mediated), not in the scope of the target."
  type: true-false
  answer: false
  explanation: "The primary distinction is the scope of the target, not the effector type. Both organ-specific diseases (Type 1 diabetes, Hashimoto's thyroiditis) and systemic diseases (SLE, rheumatoid arthritis) can involve both autoreactive T cells and autoantibodies — the mechanisms overlap. What differs is whether the immune attack is directed at tissue-specific antigens (pancreatic β cells, thyroid tissue) or at ubiquitous antigens found throughout the body (DNA, nuclear proteins, joint-lining proteins). Systemic diseases cause multi-organ damage precisely because their autoantibody targets are present everywhere."

- question: "Why is it accurate to say that the same features of the adaptive immune system that make it effective against pathogens also make it capable of causing severe autoimmune disease?"
  type: short-answer
  answer: "The adaptive immune system's power comes from its exquisite specificity and clonal expansion — it generates lymphocytes with precise, high-affinity recognition of a target antigen and then amplifies those cells massively. This specificity is generated randomly (through V(D)J recombination) and then shaped by selection to be useful against foreign antigens. But the same mechanism that generates a powerful response against a pathogen can produce self-reactive cells if the selection process fails. When an autoreactive T cell or B cell escapes tolerance and encounters its self-antigen, it uses the same mechanisms of activation, proliferation, and effector function — cytotoxicity, antibody production, inflammatory signaling — that normally eliminate pathogens. The disease is caused by precision-targeted immune destruction, which is why autoimmune diseases are often severe and tissue-specific."
  explanation: "Tolerance mechanisms exist precisely because the adaptive immune system's random receptor generation inevitably produces some self-reactive receptors. Central and peripheral tolerance are the price paid for having a flexible, broadly reactive immune system. When those checkpoints fail, the system's adaptive power — its ability to mount a focused, sustained, high-affinity attack — becomes directed inward with the same intensity it normally reserves for pathogens."
```

## Explainer

From your study of immune tolerance, you know that the immune system actively prevents self-reactivity through multiple checkpoints: central tolerance (deleting self-reactive lymphocytes during development) and peripheral tolerance (mechanisms like regulatory T cells that suppress any self-reactive cells that escape). **Autoimmunity** occurs when these safeguards fail, allowing the adaptive immune system to mount a sustained attack against the body's own tissues. Understanding autoimmunity requires thinking about it as a multi-hit process — no single factor is usually sufficient; instead, genetic susceptibility, environmental triggers, and regulatory failure must converge.

The genetic foundation of autoimmune susceptibility is dominated by **HLA (human leukocyte antigen) genes**, which encode the MHC molecules that present peptides to T cells. Certain HLA alleles are strongly associated with specific autoimmune diseases — for example, HLA-B27 with ankylosing spondylitis and HLA-DR4 with rheumatoid arthritis. The logic is straightforward: if a particular MHC variant happens to bind self-peptides effectively and present them to T cells, it increases the probability that self-reactive T cells will be activated. But HLA associations are not deterministic — most people carrying a risk allele never develop disease. Non-HLA genetic factors also contribute, including polymorphisms in genes encoding cytokines, co-stimulatory molecules, and regulatory pathways (such as CTLA-4 and AIRE, which you encountered in the context of T cell regulation and thymic selection).

Environmental triggers convert genetic susceptibility into active disease. The most studied mechanism is **molecular mimicry**, in which a pathogen's proteins share structural similarity with self-proteins. During an infection, T cells and antibodies generated against the pathogen cross-react with the mimicked self-antigen, triggering an autoimmune response that persists after the infection clears. Rheumatic fever following streptococcal infection is a classic example — antibodies against streptococcal M protein cross-react with cardiac myosin. Other environmental triggers include tissue damage that releases normally sequestered self-antigens (the **cryptic antigen** hypothesis), chronic infection that creates a sustained inflammatory environment, and microbial disruption of regulatory T cell function.

The breakdown of **peripheral tolerance** is the final common pathway. Even healthy individuals harbor some self-reactive T and B cells that escaped central deletion — peripheral tolerance normally keeps these cells in check through mechanisms you studied previously: anergy (functional inactivation), suppression by **regulatory T cells (Tregs)**, and deletion of chronically stimulated self-reactive cells. When Treg numbers or function decline — due to genetic defects, inflammatory signals that override suppression, or cytokine imbalances — self-reactive cells become activated. Autoimmune diseases are classified by their scope: **organ-specific** diseases like Type 1 diabetes (destruction of pancreatic β cells) and Hashimoto's thyroiditis (destruction of thyroid tissue) involve immune attack restricted to one tissue, while **systemic** diseases like systemic lupus erythematosus (SLE) involve widespread autoantibody production against ubiquitous antigens like DNA and nuclear proteins, causing multi-organ damage. In both cases, the fundamental problem is the same: the adaptive immune system's exquisite specificity, normally directed outward, has turned inward.
