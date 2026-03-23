---
id: immunodeficiency-and-transplant-immunity
title: Immunodeficiency Disorders and Transplant Immunology
domain: biology
course: immunology
prerequisites:
- id: innate-immune-response
  type: soft
- id: adaptive-immune-response
  type: hard
tags:
- immunodeficiency
- transplant
- rejection
stage: expert
status: validated
---

# Immunodeficiency Disorders and Transplant Immunology

## Core Idea
Primary immunodeficiencies affect innate immunity (IRAK4, MyD88 mutations), T cell development (DiGeorge syndrome), B cell development (X-linked agammaglobulinemia), or lymphocyte function (SCID). Secondary immunodeficiencies follow infection (HIV), malignancy, or medications (chemotherapy, corticosteroids). Transplant rejection occurs when donor MHC alloantigens trigger T cell and antibody responses: acute cellular rejection (7-90 days, T cell-mediated), acute humoral rejection (hours-days, alloantibody-mediated), and chronic rejection (months-years, progressive vasculitis). Immunosuppression with calcineurin inhibitors, mTOR inhibitors, and depleting antibodies prolongs graft survival.

## How It's Best Learned
Map primary immunodeficiencies to affected immune components (innate, T cell, B cell, lymphocyte function). Compare rejection mechanisms and immunosuppressive strategies.

## Common Misconceptions
- Immunodeficiency always causes severe infections (some defects cause specific vulnerabilities, e.g., C3 deficiency predisposes to pneumococcal infection). - Transplant rejection is a single process (acute and chronic rejection use different mechanisms).

## Questions

```yaml
- question: "A child presents with recurrent bacterial pneumonias caused by encapsulated organisms (Streptococcus pneumoniae, Haemophilus influenzae) but has no unusual viral or fungal infections. Which immune component is most likely deficient?"
  type: multiple-choice
  options:
    - "T cells, because cell-mediated immunity handles all bacterial infections"
    - "Natural killer cells, because they are the primary defense against extracellular bacteria"
    - "B cells or antibody production, because opsonization of encapsulated bacteria requires IgG and complement activation"
    - "Complement components C5–C9, because the membrane attack complex clears all bacterial pathogens"
  answer: 2
  explanation: "The pattern of infection reveals the missing component. Encapsulated bacteria evade phagocytosis by hiding behind their polysaccharide capsule — the primary defense is antibody-mediated opsonization (IgG coating the bacterium for phagocyte recognition) and complement activation. Susceptibility specifically to these organisms with no unusual viral or fungal infections points to a B cell or antibody deficiency (such as X-linked agammaglobulinemia). T cell deficiency would cause susceptibility to viral, fungal, and intracellular bacterial infections. Complement deficiency (especially C5–C9) causes susceptibility to Neisseria species specifically, not encapsulated bacteria broadly."

- question: "A transplant patient on calcineurin inhibitors develops Pneumocystis jirovecii pneumonia (PJP), a fungal infection normally controlled by T cell-mediated immunity. What principle does this illustrate?"
  type: multiple-choice
  options:
    - "Calcineurin inhibitors have unexpected antifungal effects that paradoxically increase fungal susceptibility"
    - "Immunosuppression to prevent transplant rejection creates iatrogenic immunodeficiency, recreating the same vulnerability profile as a primary T cell defect"
    - "The patient must also have an undiagnosed primary immunodeficiency that became apparent under stress"
    - "PJP is a side effect of calcineurin inhibitors, not a true immunodeficiency complication"
  answer: 1
  explanation: "Calcineurin inhibitors block NFAT-driven T cell activation, suppressing the T cell responses that would otherwise reject the transplant. But T cells are also essential for controlling intracellular pathogens, fungi, and viruses — precisely the pathogens that cause disease in primary T cell deficiencies like DiGeorge syndrome. By suppressing T cell function to prevent rejection, immunosuppressive therapy recreates the susceptibility profile of a primary T cell immunodeficiency. This is the fundamental tradeoff in transplant medicine: preventing rejection requires suppressing the same adaptive immune mechanisms that protect against infection and malignancy."

- question: "X-linked agammaglobulinemia results in susceptibility to extracellular bacterial infections but relatively preserved immunity against intracellular pathogens and most viruses, because T cell function remains intact."
  type: true-false
  answer: true
  explanation: "XLA is caused by mutations in Bruton's tyrosine kinase (BTK), which is required for B cell development. Without functional B cells, patients cannot produce antibodies — making them vulnerable to encapsulated extracellular bacteria that require opsonization. However, T cell development and function are unaffected, so cell-mediated immunity against viruses, intracellular bacteria, and fungi is largely preserved. This is the key insight of immunodeficiency diagnosis: the pattern of infections maps to the missing component, allowing clinicians to identify the defect from clinical presentation."

- question: "Chronic transplant rejection is simply a slower, attenuated version of acute cellular rejection, driven by the same T cell mechanism at lower intensity."
  type: true-false
  answer: false
  explanation: "Chronic and acute rejection differ in both mechanism and pathology. Acute cellular rejection (days to months) is driven primarily by recipient T cells recognizing donor MHC alloantigens. Chronic rejection (months to years) is a progressive vasculopathy involving both cellular and humoral mechanisms — ongoing immune-mediated injury leads to intimal proliferation, fibrosis, and gradual graft dysfunction. It is not merely attenuated acute rejection but a distinct process, which is why it responds poorly to the same immunosuppressive agents that prevent acute rejection. Understanding this distinction matters clinically because chronic rejection remains the leading cause of long-term graft failure despite successful prevention of acute rejection."

- question: "Explain how the same adaptive immune mechanisms that protect against infection make transplant rejection inevitable without immunosuppression, and what fundamental tradeoff this creates."
  type: short-answer
  answer: "The adaptive immune system's power comes from its exquisite ability to recognize non-self MHC molecules — the same mechanism that allows T cells to kill virally infected cells. Donor organs express allogeneic HLA molecules that recipient T cells have never learned to tolerate, triggering T cell activation and alloantibody production as if the graft were a pathogen. Without immunosuppression, rejection is the immune system functioning correctly. Immunosuppressive drugs (calcineurin inhibitors, mTOR inhibitors, depleting antibodies) suppress these adaptive responses broadly, preventing rejection but also reducing responses to actual pathogens — creating iatrogenic immunodeficiency. This tradeoff (graft survival vs. infection susceptibility) is the central clinical challenge of transplant medicine."
  explanation: "This question asks students to integrate two halves of the topic into a unified principle. The insight is that immunodeficiency and transplant rejection are not opposite problems but two faces of the same adaptive immune mechanism: the recognition of non-self. A fully functional immune system rejects transplants for exactly the same reasons it clears infections. The clinical resolution — immunosuppression — solves one problem by creating a controlled version of the other, which is why transplant patients require lifelong prophylaxis against opportunistic infections and monitoring for post-transplant malignancies."
```

## Explainer

Immunodeficiency disorders and transplant rejection may seem like opposite problems — too little immunity versus too much — but they are deeply connected through the same principles of adaptive and innate immune function that you have already studied. Understanding immunodeficiency reveals which immune components are essential for which types of defense, while transplant immunology shows what happens when a fully competent immune system encounters foreign tissue that it was never meant to tolerate.

**Primary immunodeficiencies** are inherited genetic defects that impair specific branches of immunity, and the clinical pattern of infections reveals which branch is compromised. Defects in **B cells or antibody production** (such as X-linked agammaglobulinemia, caused by mutations in Bruton's tyrosine kinase) result in recurrent bacterial infections of the respiratory and gastrointestinal tracts — the encapsulated bacteria that antibodies and complement normally handle. Defects in **T cell development** (such as DiGeorge syndrome, caused by thymic aplasia from a 22q11 deletion) lead to susceptibility to viral, fungal, and intracellular bacterial infections — the pathogens that require cell-mediated immunity. **Severe combined immunodeficiency (SCID)** affects both T and B cell lineages (often through mutations in the common gamma chain of cytokine receptors or in RAG recombinases) and is fatal without intervention because virtually all adaptive immunity is absent. **Secondary immunodeficiencies** arise from external causes — HIV destroys CD4+ T cells, chemotherapy kills dividing lymphocytes, and corticosteroids suppress immune activation broadly.

**Transplant rejection** occurs because the adaptive immune system evolved to recognize non-self MHC molecules with extraordinary sensitivity. Donor organs express **allogeneic MHC** (HLA) molecules that differ from the recipient's, and these foreign MHC molecules are the dominant targets of rejection. Rejection is classified by mechanism and timing. **Hyperacute rejection** (minutes to hours) occurs when preformed recipient antibodies against donor MHC or ABO antigens activate complement and destroy graft vasculature — this is largely prevented by pre-transplant crossmatching. **Acute cellular rejection** (days to months) is driven by recipient T cells that recognize donor MHC molecules either directly (T cells bind intact donor MHC on graft antigen-presenting cells) or indirectly (recipient APCs process and present donor MHC peptides). **Chronic rejection** (months to years) involves a slow, progressive vasculopathy driven by both cellular and humoral mechanisms, leading to graft fibrosis and eventual failure.

Modern transplant medicine relies on **immunosuppressive drugs** that target the very adaptive immune mechanisms you have studied. **Calcineurin inhibitors** (cyclosporine, tacrolimus) block the calcium-dependent signaling pathway that activates NFAT and drives T cell IL-2 production — essentially silencing T cell activation at the transcriptional level. **mTOR inhibitors** (sirolimus) block the proliferation signal downstream of IL-2 receptor engagement. **Mycophenolate** inhibits purine synthesis required for lymphocyte proliferation. **Anti-thymocyte globulin** and **anti-CD20 antibodies** (rituximab) deplete T cells and B cells respectively. The fundamental tradeoff is unavoidable: suppressing rejection creates a state of **iatrogenic immunodeficiency**, increasing susceptibility to the same opportunistic infections and malignancies seen in primary immunodeficiency. Balancing graft survival against infection risk is the central clinical challenge of transplant medicine.
