---
id: antimicrobial-peptides-and-lysozyme
title: Antimicrobial Peptides and Natural Host Defenses
domain: biology
course: microbiology
prerequisites:
- id: innate-immune-response
  type: hard
- id: inflammatory-response-cellular
  type: soft
builds-toward:
- antibiotic-resistance-genetic-mechanisms
tags:
- antimicrobial
- innate-immunity
- peptides
stage: advanced
status: validated
---

# Antimicrobial Peptides and Natural Host Defenses

## Core Idea
Antimicrobial peptides (defensins, cathelicidins, histatins) and lysozyme are innate immune molecules that kill or inhibit bacteria and fungi. These molecules disrupt membranes, inhibit cell-wall synthesis, or target nucleic acids. Resistance to these defenses drives bacterial pathogenesis and biofilm formation.

## Questions

```yaml
- question: "Defensins are small, cationic (positively charged) peptides that form pores in bacterial membranes and kill bacteria. Why don't they also lyse the human cells they contact?"
  type: multiple-choice
  options:
    - "Defensins are too large to insert into the tightly packed lipid bilayer of mammalian cell membranes"
    - "Mammalian cell membranes present a neutral outer leaflet (stabilized by cholesterol) while bacterial membranes expose negatively charged phospholipids, so defensins are selectively attracted to bacterial surfaces"
    - "Human cells produce receptor proteins that sequester and neutralize defensins before they reach the membrane"
    - "Defensins require peptidoglycan to trigger insertion, and mammalian cells lack this structure"
  answer: 1
  explanation: "The selectivity of cationic AMPs depends on charge complementarity: bacterial membranes are rich in negatively charged phospholipids (like phosphatidylglycerol) exposed on the outer leaflet, while mammalian outer leaflets are predominantly neutral, with cholesterol dampening any surface charge. Defensins are electrostatically attracted to the negatively charged bacterial surface, insert into it, and form pores. On mammalian cells, the electrostatic attraction is minimal, so defensins do not insert efficiently. This charge-based discrimination is why AMPs kill bacteria at concentrations that leave host cells unharmed."

- question: "Gram-negative bacteria are generally less susceptible to lysozyme than Gram-positive bacteria. What structural feature explains this difference?"
  type: multiple-choice
  options:
    - "Gram-negative bacteria produce a lysozyme-degrading protease in their periplasmic space"
    - "Gram-negative bacteria have a thicker peptidoglycan layer that is harder for lysozyme to penetrate than the thin layer of Gram-positives"
    - "Gram-negative bacteria have an outer membrane that shields their thin peptidoglycan layer from lysozyme access"
    - "Gram-negative bacteria lack N-acetylmuramic acid, so the lysozyme cleavage target is absent from their cell walls"
  answer: 2
  explanation: "Gram-positive bacteria have a thick, exposed peptidoglycan layer directly accessible on the cell surface — lysozyme cleaves its glycosidic bonds, destroying wall integrity. Gram-negative bacteria have a thin peptidoglycan layer buried between an inner membrane and an outer membrane; the outer membrane is a lipopolysaccharide-containing barrier that prevents lysozyme from reaching its substrate. This structural difference is why Gram-positive organisms are especially vulnerable to lysozyme in tears and saliva."

- question: "Antimicrobial peptides and conventional antibiotics work by the same basic mechanism — both disrupt specific enzymatic reactions or protein synthesis steps within bacteria."
  type: true-false
  answer: false
  explanation: "Conventional antibiotics typically target specific bacterial proteins — cell wall synthesis enzymes (penicillin targets transpeptidases), ribosomes (tetracyclines, aminoglycosides), or DNA gyrase (fluoroquinolones). Most AMPs work by physically disrupting the membrane through electrostatic insertion and pore formation, exploiting the charge differential between bacterial and host cells. This physical mechanism, rather than protein-target specificity, is part of why bacteria have greater difficulty evolving resistance to AMPs compared to conventional antibiotics."

- question: "Bacterial pathogens that successfully colonize human tissues have often evolved mechanisms to modify their membrane surface charge, reducing the electrostatic attraction that drives AMP binding."
  type: true-false
  answer: true
  explanation: "Modifying surface charge is a key virulence mechanism in many bacterial pathogens. For example, some bacteria add positively charged amino acids to lipid A in their LPS, reducing the net negative charge of the outer surface and decreasing defensin binding. Others produce proteases that degrade AMPs, or form biofilms whose polysaccharide matrix physically excludes AMPs. These adaptations directly reflect evolutionary pressure from host AMP production and help explain why certain organisms are pathogenic while related species remain harmless commensals."

- question: "Why does the charge difference between bacterial and mammalian membranes allow antimicrobial peptides to selectively kill bacteria without destroying host tissues?"
  type: short-answer
  answer: "Bacterial membranes expose negatively charged phospholipids on their outer surface, providing an electrostatic target for cationic (positively charged) AMPs. Mammalian cell outer leaflets are predominantly neutral — phosphatidylcholine and sphingomyelin dominate, with cholesterol dampening surface charge — so there is no electrostatic attraction to drive AMP insertion. AMPs are thus selectively concentrated at bacterial membranes, where they insert and form pores, while mammalian membranes are largely ignored."
  explanation: "This selectivity is the evolutionary and practical key to AMPs as innate defenses: they kill bacteria at concentrations found in tears, saliva, and neutrophil granules without causing tissue damage. It also explains why loss of AMP production — through burns, genetic defects, or chronic disease — dramatically increases susceptibility to surface infections. The host uses membrane composition as the discrimination criterion between self and microbial non-self."
```

## Explainer

Before the adaptive immune system even knows an infection is underway, the body has already deployed a chemical arsenal at every surface exposed to the environment. You know from your study of innate immunity that the first line of defense is rapid and nonspecific. **Antimicrobial peptides** (AMPs) and **lysozyme** are the molecular weapons of that first line — proteins that kill microbes directly, without needing to recognize specific antigens or wait for lymphocyte activation.

**Lysozyme** is the simplest to understand. It is an enzyme found in tears, saliva, nasal secretions, and the granules of neutrophils. Its target is **peptidoglycan**, the rigid mesh that gives bacterial cell walls their structural integrity. Lysozyme cleaves the β-1,4 glycosidic bond between N-acetylmuramic acid and N-acetylglucosamine — the same bond that holds peptidoglycan chains together. Without an intact wall, bacteria in a hypotonic environment (like tears or saliva) undergo osmotic lysis. Gram-positive bacteria, with their thick exposed peptidoglycan layer, are especially vulnerable. Gram-negative bacteria gain partial protection from their outer membrane, which shields the thinner peptidoglycan layer beneath.

Antimicrobial peptides work differently. **Defensins** — small, cationic (positively charged) peptides produced by epithelial cells and neutrophils — exploit a fundamental difference between microbial and host cell membranes. Bacterial membranes are rich in negatively charged phospholipids (like phosphatidylglycerol), while mammalian cell membranes have their negative charges mostly on the inner leaflet, with neutral cholesterol stabilizing the outer surface. Defensins are electrostatically attracted to bacterial membranes, insert into the lipid bilayer, and form pores that collapse the membrane potential and cause cell death. **Cathelicidins** (such as LL-37 in humans) work similarly but also have immunomodulatory roles — they recruit immune cells, promote wound healing, and can neutralize bacterial lipopolysaccharide. **Histatins**, found in saliva, are particularly effective against fungi like *Candida*, disrupting mitochondrial function in yeast cells.

The evolutionary pressure these defenses exert is enormous. Pathogens that successfully colonize human tissues have evolved countermeasures: modifying their surface charge to repel cationic peptides, producing proteases that degrade AMPs, or forming **biofilms** — structured communities encased in a protective matrix that AMPs cannot easily penetrate. Understanding this arms race is essential because it explains why certain organisms are pathogenic while closely related species are harmless commensals. It also explains why the loss of AMP production — through genetic defects, burns, or chronic disease — dramatically increases susceptibility to infection at epithelial surfaces.
