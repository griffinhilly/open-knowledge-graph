---
id: complement-regulation-and-deficiency
title: Complement Regulation and Disease Associated with Deficiency
domain: biology
course: immunology
prerequisites:
- id: complement-system-overview
  type: hard
- id: complement-activation-pathways
  type: hard
builds-toward:
- primary-immunodeficiency-categories
tags:
- complement-regulation
- complement-deficiency
- C3-nephritic-factor
- atypical-HUS
- meningococcal-sepsis
stage: expert
status: draft
---

# Complement Regulation and Disease Associated with Deficiency

## Core Idea
The complement cascade is tightly regulated by factor H, factor I, C1-inhibitor, and membrane-bound regulators (CD55, CD46) to prevent inadvertent self-damage. Deficiencies in early complement components (C1, C2, C4) increase autoimmune disease risk; deficiencies in alternative pathway components increase infection risk (especially Neisseria meningitidis). Dysregulation (e.g., factor H mutations in atypical HUS) causes complement-mediated tissue damage.

## How It's Best Learned
Map complement regulatory molecules and their binding sites on pathogens. Study how pathogens exploit complement regulation to evade immunity.

## Common Misconceptions
Complement deficiency does not uniformly impair immunity; early component deficiency may increase autoimmunity, while late component deficiency increases bacterial infection risk. Some pathogens hijack complement for cellular entry (e.g., Leishmania via CR1).

## Questions

```yaml
- question: "A patient has recurrent Neisseria meningitidis infections despite normal complement activity through C3. Testing reveals absent activity at the C5 level. What explains the specific susceptibility to this pathogen?"
  type: multiple-choice
  options:
    - "C5 deficiency impairs opsonization, preventing neutrophils from engulfing the bacteria"
    - "C5 deficiency impairs the classical pathway initiation, so antibody-antigen complexes cannot activate complement"
    - "C5 deficiency prevents membrane attack complex formation; Neisseria is specifically vulnerable to MAC-mediated lysis because its thin Gram-negative outer membrane is accessible"
    - "C5 deficiency reduces cytokine production, impairing T cell responses needed to control encapsulated bacteria"
  answer: 2
  explanation: "C5 is the first component of the terminal MAC-forming pathway (C5–C9). Without C5, the MAC cannot assemble and bacteria cannot be lysed. Neisseria meningitidis and N. gonorrhoeae are particularly vulnerable to MAC-mediated killing because they are Gram-negative with accessible outer membranes — unlike Gram-positive bacteria with thick peptidoglycan walls or encapsulated bacteria that resist MAC. This is why terminal complement deficiencies (C5–C9) produce a highly specific phenotype: recurrent Neisseria infections rather than general susceptibility to all pathogens."

- question: "A patient with C2 deficiency is found to have systemic lupus erythematosus. Which mechanism best explains this association?"
  type: multiple-choice
  options:
    - "C2 normally suppresses T cell activation; without it, autoreactive T cells escape deletion"
    - "C2 deficiency causes overactivation of the alternative pathway, which generates inflammatory mediators that damage joint tissue"
    - "Classical pathway components are needed to clear immune complexes and apoptotic debris; when they accumulate, they provide self-antigens that drive autoimmune responses"
    - "C2 deficiency leads to low IgG levels, so immune complexes are not cleared by Fc receptors"
  answer: 2
  explanation: "Early classical pathway components (C1q, C2, C4) have a critical clearance function: they tag immune complexes and apoptotic debris for phagocytosis. When this clearance fails, debris accumulates. Uncleared apoptotic cells release nuclear antigens (DNA, histones, ribonucleoproteins) that are normally hidden from immune surveillance. These become a persistent source of self-antigens that can trigger and sustain autoimmune responses. C1q deficiency is the strongest known genetic risk factor for SLE — not because complement directly prevents autoimmunity, but because its clearance function prevents self-antigen exposure."

- question: "Complement deficiency always increases susceptibility to bacterial infections, because complement is a central component of innate immune defense."
  type: true-false
  answer: false
  explanation: "The direction of clinical consequence depends entirely on where in the cascade the deficiency falls. Early classical pathway deficiencies (C1, C2, C4) are primarily associated with autoimmune disease — particularly SLE — because these components are essential for clearing immune complexes and apoptotic debris, not primarily for killing bacteria. Terminal component deficiencies (C5–C9) do impair MAC formation and increase bacterial infection risk (especially Neisseria). Alternative pathway deficiencies increase susceptibility to encapsulated organisms. The clinical phenotype is specific to the component's function, not a generic 'immunosuppression.'"

- question: "Factor H mutations cause disease not by reducing complement activity, but by allowing uncontrolled complement activation against host tissues."
  type: true-false
  answer: true
  explanation: "This is the key insight about dysregulation vs. deficiency. Factor H normally binds C3b on host cell surfaces (recognizing sialic acid markers of self) and serves as a cofactor for Factor I to inactivate C3b. Without functional Factor H, complement cannot distinguish host cells from pathogens — the alternative pathway amplification loop proceeds unchecked on self surfaces. In atypical HUS (aHUS), Factor H mutations allow the alternative pathway to attack kidney endothelium, causing thrombotic microangiopathy and renal failure. More complement activation is worse here, not better: the disease is caused by losing the brake, not losing the engine."

- question: "Why does early classical pathway complement deficiency (C1, C2, C4) predispose to autoimmune disease rather than to infection, and how does this differ mechanistically from terminal complement deficiency?"
  type: short-answer
  answer: "Early classical pathway components (C1q, C2, C4) play a crucial role in clearing immune complexes and apoptotic debris. When cells die by apoptosis, their nuclear contents (DNA, histones) are normally packaged and cleared rapidly by complement-opsonized phagocytosis. Without early complement components, this clearance fails, debris accumulates, and nuclear self-antigens become chronically exposed to immune cells — driving autoimmune responses, particularly SLE. Terminal complement components (C5–C9) form the MAC, which lyses Gram-negative bacteria. Deficiency there impairs bacterial killing specifically, without disrupting clearance, producing recurrent Neisseria infections rather than autoimmunity."
  explanation: "This clinical logic flows directly from understanding the distinct functions of different complement components: opsonization and clearance vs. direct lysis. Knowing the function of each component predicts the disease associated with its deficiency — a major organizing principle for clinical immunology."
```

## Explainer

From your study of complement activation pathways, you know that the complement cascade is a powerful system of sequentially activated proteases that can opsonize pathogens, recruit inflammatory cells, and directly lyse microbes through the membrane attack complex (MAC). But a system this destructive must be tightly controlled — without regulation, complement would damage the body's own cells just as readily as it attacks pathogens. The regulatory machinery exists at nearly every step of the cascade.

**Fluid-phase regulators** control complement activation in the blood. **C1-inhibitor (C1-INH)** is a serine protease inhibitor that inactivates C1r and C1s, shutting down the classical pathway at its earliest step. Deficiency of C1-INH causes **hereditary angioedema**, characterized by episodic, life-threatening swelling due to uncontrolled generation of vasoactive peptides. **Factor H** and **Factor I** work together to dismantle the alternative pathway C3 convertase: Factor H binds C3b on host cell surfaces (recognizing sialic acid markers of self) and serves as a cofactor for Factor I, which cleaves C3b into inactive iC3b. This is why host surfaces are protected while pathogen surfaces — lacking sialic acid — allow complement amplification to proceed.

**Membrane-bound regulators** provide cell-intrinsic protection. **CD55** (decay-accelerating factor) accelerates the decay of C3 and C5 convertases on host cell surfaces, while **CD46** (membrane cofactor protein) acts as a cofactor for Factor I-mediated cleavage of C3b. **CD59** blocks the final assembly of the MAC by preventing C9 polymerization. Loss of CD55 and CD59 — as occurs in **paroxysmal nocturnal hemoglobinuria (PNH)**, where a defect in GPI-anchor synthesis prevents these regulators from attaching to cell membranes — results in chronic complement-mediated destruction of red blood cells.

The clinical consequences of complement deficiency follow a logical pattern once you understand where each component acts. Deficiencies in **early classical pathway components** (C1q, C2, C4) are strongly associated with **systemic lupus erythematosus** and other autoimmune diseases — not because complement directly prevents autoimmunity, but because these components are essential for clearing immune complexes and apoptotic debris. When debris accumulates, it becomes a source of self-antigens that drive autoimmune responses. In contrast, deficiency of **terminal components** (C5–C9) specifically impairs MAC formation, leaving patients unable to lyse Gram-negative bacteria with thin cell walls — particularly **Neisseria meningitidis** and **N. gonorrhoeae**. Patients with terminal complement deficiencies may experience recurrent meningococcal infections. Mutations in **Factor H** illustrate the danger of dysregulation rather than deficiency: without Factor H to protect host surfaces, the alternative pathway attacks kidney endothelium, causing **atypical hemolytic uremic syndrome (aHUS)**, a devastating condition characterized by thrombotic microangiopathy and renal failure.
