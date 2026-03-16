---
id: antibody-affinity-and-avidity
title: 'Antibody Affinity and Avidity: Quantifying Antibody-Antigen Interactions'
domain: biology
course: immunology
prerequisites:
- id: antibody-structure-and-function
  type: hard
- id: somatic-hypermutation-and-affinity-maturation
  type: hard
builds-toward:
- affinity-maturation-somatic-hypermutation
tags:
- antibody-affinity
- avidity
- Kd
- binding-kinetics
- cross-linking
stage: advanced
status: draft
---

# Antibody Affinity and Avidity: Quantifying Antibody-Antigen Interactions

## Core Idea
Affinity is the intrinsic strength of antibody-antigen binding (Kd, typically 10^−9 to 10^−11 M), determined by complementarity of binding pockets and measured by surface plasmon resonance or ELISA. Avidity is the overall strength of polyvalent interaction (e.g., IgG binding two epitopes on a virus), which can be very high despite modest individual affinities. Affinity maturation increases affinity 100–1000-fold; high avidity compensates for low affinity in some contexts.

## How It's Best Learned
Study how somatic hypermutation increases affinity during germinal center reactions. Understand why avidity is often more relevant than affinity for in vivo function.

## Common Misconceptions
High affinity does not guarantee in vivo effectiveness; avidity and appropriate epitope distribution matter. Antibodies with similar apparent titers can have vastly different functional potency due to avidity differences.

## Explainer

From your study of antibody structure, you know that each antibody has two identical antigen-binding sites formed by the variable regions of the heavy and light chains. From somatic hypermutation and affinity maturation, you know that the immune system progressively improves the fit between these binding sites and their target antigen. **Affinity** and **avidity** are the two ways to quantify how well an antibody holds onto its target, and understanding the distinction between them is essential for interpreting immune responses, vaccine efficacy, and therapeutic antibody design.

**Affinity** refers to the binding strength of a single antigen-binding site for a single epitope. It is measured by the **dissociation constant (Kd)** — the concentration of antigen at which half the binding sites are occupied at equilibrium. A lower Kd means tighter binding: an antibody with a Kd of 10^-10 M binds its antigen ten times more tightly than one with a Kd of 10^-9 M. Affinity depends on the sum of noncovalent interactions — hydrogen bonds, van der Waals forces, electrostatic attractions, and hydrophobic contacts — between the complementarity-determining regions (CDRs) of the antibody and the epitope surface. During affinity maturation in germinal centers, somatic hypermutation introduces random point mutations into the variable regions, and B cells whose mutations happen to improve this molecular complementarity are preferentially selected, driving Kd values from ~10^-7 M in early responses down to 10^-10 or 10^-11 M in mature responses.

**Avidity** is the overall functional binding strength when multiple binding sites engage multiple epitopes simultaneously. Consider an IgM molecule: it has ten antigen-binding sites, each with relatively modest individual affinity. But when a pathogen surface displays many copies of the same epitope — as most viruses and bacteria do — multiple IgM arms can bind simultaneously. The probability that all ten binding sites release at exactly the same moment is vanishingly small, so the **effective off-rate** drops dramatically even though each individual site has the same intrinsic affinity. This is why IgM, despite its low per-site affinity, is highly effective in early immune responses before affinity maturation has occurred. Even IgG, with its two binding sites, benefits from avidity when binding to surfaces with clustered epitopes — the functional binding strength of bivalent IgG to a viral capsid is far greater than the monovalent Kd would predict.

The distinction matters practically. In diagnostic assays like ELISA, high-avidity serum (indicating a mature immune response) gives stronger signals than low-avidity serum (indicating recent infection), which is why **avidity testing** can distinguish recent from past infections — a tool used in clinical settings for pathogens like CMV and toxoplasma. In therapeutic antibody design, engineers must consider both parameters: a monoclonal antibody may have exquisite affinity for a soluble cytokine (where avidity contributes little) but need both high affinity and favorable geometry to neutralize a virus with spaced epitopes. The immune system optimizes both — affinity through somatic hypermutation and avidity through isotype switching to multivalent formats like IgM and IgA — creating a layered strategy for pathogen clearance.
