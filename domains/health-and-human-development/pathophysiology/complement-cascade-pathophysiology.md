---
id: complement-cascade-pathophysiology
title: Complement Cascade Pathophysiology
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: complement-system-overview
  type: hard
- id: acute-inflammation-pathophysiology
  type: soft
- id: complement-cascade-and-pathways
  type: soft
builds-toward:
- sepsis-and-sirs-pathophysiology
- autoimmune-disease-pathophysiology-adv
tags:
- complement
- c3
- c5
- anaphylatoxins
- inflammation
stage: advanced
status: validated
---

# Complement Cascade Pathophysiology

## Core Idea
The complement system is a cascade of serum and membrane proteins activated by three pathways (classical, alternative, lectin) that converge on C3 cleavage, generating C3a and C3b. C3b opsonizes pathogens for phagocytosis, C3a and C5a are potent anaphylatoxins driving inflammation, and the membrane attack complex (MAC) directly lyses cells. Complement dysregulation causes excessive inflammation (sepsis), tissue damage (hemolytic anemia), or inadequate clearance of pathogens and immune complexes (autoimmune disease).

## How It's Best Learned
Trace all three activation pathways to the C3 convertase. Understand opsonization and MAC formation as effector mechanisms. Study inherited and acquired complement deficiencies and their clinical consequences (recurrent infections with C5-8 defects; SLE with C1q deficiency).

## Common Misconceptions
Complement is not only activated by antibodies—the alternative and lectin pathways provide immediate recognition of pathogens. Complement deficiency is not uniformly protective; some deficiencies increase infection risk while others cause autoimmunity.

## Questions

```yaml
- question: "A patient develops episodic destruction of their own red blood cells with no evidence of infection. Lab workup reveals a somatic mutation that eliminates complement regulatory proteins CD55 and CD59 on red blood cells. What best explains this pathophysiology?"
  type: multiple-choice
  options:
    - "Activated T cells are targeting red blood cells as a bystander effect of chronic inflammation"
    - "Absence of CD55 and CD59 allows the membrane attack complex to lyse the patient's own red blood cells, which can no longer be distinguished from pathogens"
    - "C3b opsonizes the red blood cells, triggering antibody-dependent cellular cytotoxicity"
    - "The alternative pathway is continuously activated by a hidden pathogen residing in erythrocytes"
  answer: 1
  explanation: "This is paroxysmal nocturnal hemoglobinuria (PNH). CD55 and CD59 are regulatory proteins that protect host cells from complement deposition. Without them, MAC (C5b-9) assembles on the red cell surface and lyses it by osmotic disruption — with no infection involved. The common misconception is that complement only acts in response to pathogens; in fact, complement is always primed and host cells require continuous regulatory protection to avoid self-attack."

- question: "In sepsis, massive systemic complement activation leads to worse patient outcomes despite active pathogen clearance. Which mechanism best explains this paradox?"
  type: multiple-choice
  options:
    - "Complement depletion leaves bacteria unopsonized, allowing them to proliferate unchecked"
    - "C5a floods the circulation, driving neutrophil activation, endothelial damage, and cytokine release that causes widespread tissue injury beyond the infection site"
    - "MAC formed in the bloodstream lyses bacteria too slowly, allowing them to release toxins first"
    - "Classical pathway activation is suppressed during sepsis, impairing antibody-mediated killing"
  answer: 1
  explanation: "The paradox arises from complement's double-edged nature. C5a is a potent anaphylatoxin: locally it recruits neutrophils appropriately, but when generated systemically it activates neutrophils throughout the body, damages endothelial cells in the lung, kidney, and liver, and triggers cytokine cascades that amplify injury far beyond the infection site. The harm comes not from the pathogen but from the complement-driven inflammatory response directed against the host's own tissues — the 'friendly fire' of SIRS."

- question: "Deficiency of early complement components such as C1q or C4 protects patients from autoimmune disease by reducing the overall inflammatory drive of the complement system."
  type: true-false
  answer: false
  explanation: "This is the opposite of what occurs. C1q and C4 are required for clearance of apoptotic cells and immune complexes. When these components are absent, immune complexes accumulate and apoptotic debris goes uncleared — both of which trigger autoimmune responses. C1q deficiency is one of the strongest known genetic risk factors for systemic lupus erythematosus. The misconception conflates 'less complement activation' with 'less inflammation,' ignoring complement's essential housekeeping role in preventing immune complex disease."

- question: "In ischemia-reperfusion injury, complement can attack viable host cells in tissue that survived the initial ischemia, extending the zone of tissue damage beyond the original infarct."
  type: true-false
  answer: true
  explanation: "During ischemia, stressed cells may express neoantigens or downregulate complement regulatory proteins. When blood flow is restored, complement activated in the newly oxygenated tissue deposits MAC on these stressed but viable cells, killing them. The total zone of destruction after reperfusion therefore exceeds the zone caused by ischemia alone — a clinically important mechanism in myocardial infarction that helps explain the paradox of 'reperfusion injury.'"

- question: "Why does complement dysregulation produce two seemingly opposite clinical outcomes — increased infection susceptibility in some deficiencies and autoimmune disease in others?"
  type: short-answer
  answer: "Which outcome depends on which component is deficient and what function it serves. Terminal components (C5-C9) form the MAC needed to lyse encapsulated bacteria like Neisseria; deficiencies here remove a killing mechanism and increase infection risk. Early components (C1q, C3, C4) opsonize pathogens and clear immune complexes and apoptotic debris; deficiencies here impair immune housekeeping, allowing complexes to accumulate and trigger autoimmunity. Complement is not a single-purpose attack system — it performs surveillance, tagging, and clearance functions that serve different goals at different stages of the cascade."
  explanation: "The key insight is that 'complement deficiency' describes many different conditions with different consequences. MAC is primarily for killing; C3b is for opsonization and clearance; C3a/C5a are inflammatory signals. Removing different effectors produces predictably different defects. Understanding this requires treating complement as a system with distinct roles rather than as a monolithic attack mechanism whose absence is uniformly protective or harmful."
```

## Explainer

The complement system's power comes from amplification: a small initiating signal — a few antibodies bound to a bacterium, or surface molecules recognized by lectins — triggers a cascade that rapidly deposits thousands of effector molecules on the target. You already know from your complement overview that three pathways (classical, alternative, lectin) converge on **C3 convertase**, the enzyme that cleaves C3 into C3a and C3b. In the context of pathophysiology, the question shifts from "how does complement work?" to "what goes wrong when it is mis-regulated or misdirected?"

Start with C3b. When C3b opsonizes a pathogen, it is a defense success — the bacterium gets tagged for phagocytosis and destroyed. But C3b can also deposit on **host cells** if regulatory proteins fail. Complement regulation proteins (CD46, CD55, CD59, factor H) continuously protect normal cells from accidental complement deposition. When these regulators are mutated, depleted, or blocked by autoantibodies, the complement system attacks the body's own cells. The clinical example is **paroxysmal nocturnal hemoglobinuria (PNH)**, in which a somatic mutation eliminates CD55 and CD59 on red blood cells, making them vulnerable to complement-mediated lysis. This is not infection — it is the immune system consuming red blood cells it can no longer distinguish from pathogens.

The small cleavage fragments — **C3a** and **C5a** — are the inflammatory messengers. As **anaphylatoxins**, they bind G-protein-coupled receptors on mast cells, basophils, and endothelial cells, triggering histamine release, vasodilation, and increased vascular permeability. This is useful in a localized infection but catastrophic when complement activates systemically. In **sepsis**, massive complement activation floods the circulation with C5a. C5a drives neutrophil activation, endothelial damage, and cytokine release — contributing to the runaway inflammation of systemic inflammatory response syndrome. The lung, kidney, and liver are particularly vulnerable to complement-mediated endothelial injury under these conditions.

The third effector — the **membrane attack complex (MAC)** formed by C5b-9 — directly punches holes in lipid bilayers, killing cells by osmotic lysis. MAC is essential for killing encapsulated bacteria like Neisseria meningitidis, which is why patients with C5-C9 deficiencies suffer recurrent meningococcal infections. But MAC inserted into host cells contributes to tissue damage in ischemia-reperfusion injury: after blood flow is restored to ischemic tissue, complement activated during the reperfusion phase deposits MAC on viable but stressed cells, extending the zone of injury beyond the original infarct. Understanding complement pathophysiology therefore means recognizing it as a double-edged system — essential for defense, capable of amplifying any initial inflammatory signal into widespread tissue destruction if not precisely regulated.
