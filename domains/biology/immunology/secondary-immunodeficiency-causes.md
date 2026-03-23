---
id: secondary-immunodeficiency-causes
title: 'Secondary Immunodeficiency: Acquired Immune Dysfunction'
domain: biology
course: immunology
prerequisites:
- id: immunodeficiency-and-transplant-immunity
  type: hard
- id: adaptive-immune-response
  type: soft
builds-toward:
- infectious-disease-immunopathology
tags:
- secondary-immunodeficiency
- HIV
- malnutrition
- malignancy
- immunosuppression
stage: expert
status: validated
---

# Secondary Immunodeficiency: Acquired Immune Dysfunction

## Core Idea
Secondary immunodeficiencies result from acquired conditions that compromise immune function: infections (HIV destroying CD4+ T cells), malnutrition (reduced T cell and antibody production), malignancy (immune suppression and lymphoid infiltration), medications (corticosteroids, biologic immunosuppressants), or blood loss. Unlike PIDs, secondary immunodeficiency may be reversible if the underlying cause is treated.

## How It's Best Learned
Study HIV pathogenesis and progressive CD4 decline. Compare immune defects across different causes.

## Common Misconceptions
Immunosuppressive drugs do not uniformly suppress all immune functions; they often selectively inhibit T cells while leaving innate immunity or antibody production intact. Secondary immunodeficiency from malnutrition is reversible with nutritional support.

## Questions

```yaml
- question: "An HIV patient with a CD4+ T cell count of 50 cells/μL develops a severe lung infection. A second patient with X-linked agammaglobulinemia (no functional B cells) develops recurrent pneumonia from Streptococcus pneumoniae. Which pairing of infection type to underlying immune defect is correct?"
  type: multiple-choice
  options:
    - "Both patients have equivalent vulnerability because both lack normal adaptive immunity"
    - "The HIV patient is vulnerable to encapsulated bacteria; the agammaglobulinemia patient is vulnerable to opportunistic fungi"
    - "The HIV patient is vulnerable to intracellular pathogens and fungi like Pneumocystis; the agammaglobulinemia patient is vulnerable to extracellular encapsulated bacteria requiring opsonizing antibodies"
    - "Both patients are most vulnerable to viral infections, since both lack lymphocyte function"
  answer: 2
  explanation: "The specific immune defect predicts the infection vulnerability pattern. CD4+ T helper cells coordinate cell-mediated immunity — essential for clearing intracellular pathogens (Mycobacterium, Toxoplasma) and fungi (Pneumocystis, Cryptococcus) that require macrophage activation. With CD4 counts below 200, these defenses collapse, producing AIDS-defining opportunistic infections. Agammaglobulinemia eliminates antibody production — antibodies opsonize and activate complement against extracellular encapsulated bacteria (S. pneumoniae, H. influenzae) that use polysaccharide capsules to evade phagocytosis without opsonization. Same 'immunodeficiency' label, entirely different vulnerability profiles. Understanding this mapping is central to clinical immunology."

- question: "A cancer patient on rituximab (anti-CD20 monoclonal antibody) develops recurrent bacterial sinusitis and low serum immunoglobulin levels. Which conclusion best explains the clinical picture?"
  type: multiple-choice
  options:
    - "Rituximab broadly suppresses all immune functions, including T cells and neutrophils, causing global immunosuppression"
    - "Rituximab depletes B cells, impairing antibody production while leaving T cell function and innate immunity largely intact — consistent with susceptibility to bacterial infections requiring opsonizing antibodies"
    - "Rituximab causes neutropenia, which predisposes to the bacterial infections seen here"
    - "Rituximab suppresses the innate immune response through toll-like receptor blockade"
  answer: 1
  explanation: "Rituximab is an anti-CD20 antibody that selectively depletes B cells — the cells responsible for antibody production and humoral immunity. B cell depletion leads to hypogammaglobulinemia (low antibody levels), impairing opsonization of encapsulated bacteria and neutralization of pathogens. T cell function, NK cells, and neutrophils remain intact. This selectivity is a core principle: biologic immunosuppressants target specific molecules, creating predictable and specific immune gaps. The clinical picture — recurrent sinusitis and low immunoglobulins — perfectly matches antibody deficiency. Knowing the mechanism of each drug predicts which infections to monitor for."

- question: "Secondary immunodeficiencies, like primary immunodeficiencies, arise from inherited genetic defects in immune system development and are generally not reversible."
  type: true-false
  answer: false
  explanation: "This is the fundamental definitional distinction. Primary immunodeficiencies (PIDs) are genetic — they arise from inherited defects in immune cell development or function and are generally permanent. Secondary immunodeficiencies are *acquired* — a previously functional immune system is compromised by an external cause (HIV infection, malnutrition, immunosuppressive drugs, malignancy). This distinction matters clinically because secondary immunodeficiencies are often reversible: nutritional deficiency corrects with feeding, drug-induced immunosuppression resolves when the drug is stopped or dose-reduced, and HIV-related immunodeficiency partially restores with antiretroviral therapy. Treatment strategy differs fundamentally based on this distinction."

- question: "Protein-calorie malnutrition can cause a combined immunodeficiency with impaired T cell and antibody production, and immune function may be substantially restored with adequate nutritional support."
  type: true-false
  answer: true
  explanation: "Malnutrition is the most common cause of secondary immunodeficiency worldwide. Protein-calorie deficiency impairs thymic function (reducing T cell maturation), decreases circulating lymphocyte counts, reduces immunoglobulin synthesis, and impairs neutrophil function. The resulting immune dysfunction can resemble a combined immunodeficiency affecting both cell-mediated and humoral immunity. Critically, because the underlying cause is nutritional rather than genetic, this immunodeficiency is reversible — adequate nutritional repletion can substantially restore immune function. This separates malnutrition-induced immunodeficiency sharply from PIDs, which cannot be reversed by nutritional support."

- question: "Why must a clinician identify which specific component of the immune system is compromised in a patient with secondary immunodeficiency, rather than simply treating the patient as 'broadly immunosuppressed'?"
  type: short-answer
  answer: "Different immune components protect against different pathogen classes. T helper cells coordinate responses to intracellular pathogens and fungi; antibodies neutralize extracellular bacteria and viruses; complement and opsonins target encapsulated bacteria; neutrophils clear acute bacterial and fungal infections at mucosal surfaces. A patient with T cell deficiency (e.g., HIV) faces opportunistic infections that a healthy T cell count would suppress — Pneumocystis, Toxoplasma, CMV. A patient with B cell/antibody deficiency (e.g., post-rituximab) faces encapsulated bacterial infections. A patient with neutropenia faces fulminant bacterial and fungal infections at skin and mucosa. Treating all these patients identically — for example, giving prophylactic antibiotics only — would fail to address the specific vulnerability. Knowing the defect guides prophylaxis choice, infection surveillance, and the decision about whether immune recovery is possible."
  explanation: "This specificity principle is also what allows understanding of why immunosuppressive drugs cause the particular infections they do. A transplant patient on tacrolimus (calcineurin inhibitor) primarily loses T cell function — expect viral reactivation (CMV, EBV) and opportunistic fungi. A patient on high-dose steroids loses both T cell function and neutrophil recruitment — expect a broader range of bacterial, viral, and fungal infections. The drug mechanism predicts the infection spectrum, which is the clinical payoff of mechanistic immunology."
```

## Explainer

You already know that immunodeficiency means some component of the immune system is missing or malfunctioning, and you have seen how primary immunodeficiencies arise from inherited genetic defects. **Secondary immunodeficiencies** are fundamentally different in origin: they are *acquired* conditions where a previously functional immune system becomes compromised by an external insult — an infection, a drug, a nutritional deficit, or a disease process. The distinction matters clinically because secondary immunodeficiencies are often reversible if you can identify and treat the underlying cause.

The most instructive example is **HIV/AIDS**. HIV selectively infects CD4+ T helper cells — the coordinators of the adaptive immune response you studied earlier. As the virus replicates and destroys these cells over months to years, the CD4 count progressively drops. When it falls below roughly 200 cells per microliter (normal is 500–1500), the patient loses the ability to mount effective cell-mediated and humoral responses, and **opportunistic infections** emerge — organisms like *Pneumocystis jirovecii* and *Cryptococcus neoformans* that a healthy immune system would easily contain. This progression illustrates a general principle: the specific immune defect determines which infections become dangerous. Loss of T cells predisposes to intracellular pathogens and fungi; loss of antibodies predisposes to encapsulated bacteria; loss of neutrophils predisposes to bacterial and fungal skin and mucosal infections.

**Malnutrition** is the most common cause of secondary immunodeficiency worldwide, yet it is often overlooked in clinical teaching. Protein-calorie malnutrition impairs thymic function, reduces circulating T cell numbers, and decreases antibody production — essentially mimicking a combined immunodeficiency. Specific micronutrient deficiencies (zinc, vitamin A, iron) each compromise distinct immune pathways. The critical insight is that nutritional immunodeficiency is fully reversible with adequate nutritional support, which separates it sharply from genetic immunodeficiencies.

Iatrogenic immunosuppression — immune dysfunction caused by medical treatment — is increasingly common. **Corticosteroids** broadly suppress inflammation by blocking NF-κB signaling and reducing cytokine production, but they do not shut down all arms of immunity equally. **Biologic immunosuppressants** like anti-TNF antibodies or anti-CD20 (rituximab) target specific molecules, creating selective immune gaps: rituximab depletes B cells and impairs antibody production while leaving T cell function largely intact, whereas calcineurin inhibitors (cyclosporine, tacrolimus) primarily block T cell activation. Understanding which arm of immunity a drug suppresses lets you predict which infections the patient is now vulnerable to — the same logic you applied to primary immunodeficiencies, but now with the added clinical lever that adjusting or withdrawing the drug can restore immune function.
