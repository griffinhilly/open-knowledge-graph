---
id: graft-rejection-mechanisms
title: 'Graft Rejection: Acute, Chronic, and Hyperacute'
domain: biology
course: immunology
prerequisites:
- id: transplant-immunology
  type: hard
- id: major-histocompatibility-complex
  type: hard
- id: cd8-cytotoxic-t-cells
  type: soft
builds-toward:
- graft-versus-host-disease-gvhd
- immunosuppression-and-tolerance-induction
tags:
- graft-rejection
- acute-rejection
- chronic-rejection
- HLA-matching
- alloimmunity
stage: expert
status: validated
---

# Graft Rejection: Acute, Chronic, and Hyperacute

## Core Idea
Graft rejection occurs when the recipient's immune system recognizes donor tissue as foreign. Hyperacute rejection (minutes to hours) is antibody-mediated against ABO or HLA; acute rejection (days to months) involves T cell and B cell responses against donor MHC; chronic rejection (months to years) involves slow fibrosis and vasculopathy. HLA matching and immunosuppression reduce but do not eliminate risk.

## How It's Best Learned
Examine the molecular basis of direct and indirect allorecognition. Study how immunosuppressive drugs (calcineurin inhibitors, mTOR inhibitors) prevent each rejection type.

## Common Misconceptions
Hyperacute rejection can be predicted by pretransplant crossmatching and prevented by ABO matching. Chronic rejection involves immune-independent mechanisms (recurrence of original disease); immunosuppression may slow but not stop it.

## Questions

```yaml
- question: "A kidney transplant recipient develops severe graft dysfunction within 3 hours of surgery. The organ appears dark and necrotic, with widespread vascular thrombosis. What is the most likely mechanism?"
  type: multiple-choice
  options:
    - "CD8+ cytotoxic T cells rapidly killed graft endothelial cells through direct allorecognition"
    - "Preformed antibodies against donor ABO or HLA antigens activated complement, triggering vascular thrombosis"
    - "NK cells recognized missing self-MHC on donor cells and initiated cytotoxic killing"
    - "An unusually rapid acute rejection response caused by prior sensitization from a previous transplant"
  answer: 1
  explanation: "The timing (minutes to hours) and the pattern (vascular thrombosis, necrosis) are hallmarks of hyperacute rejection. This requires preformed antibodies already circulating in the recipient before surgery — against ABO antigens or anti-HLA antibodies from prior transfusions, pregnancies, or transplants. These antibodies bind immediately to donor endothelium, fix complement, and cause rapid thrombosis and organ death. T cell-mediated acute rejection (options A and D) takes days to weeks to develop — the adaptive immune response requires time for clonal expansion. This scenario illustrates why pretransplant crossmatching is mandatory."

- question: "Which type of graft rejection is most resistant to intensified immunosuppressive therapy once it is established?"
  type: multiple-choice
  options:
    - "Hyperacute rejection — preformed antibodies are not affected by immunosuppression"
    - "Acute rejection — T cells become refractory to calcineurin inhibitors over time"
    - "Chronic rejection — involves fibrosis and vasculopathy with both immune and non-immune components"
    - "All three types respond equally once adequate immunosuppressive levels are achieved"
  answer: 2
  explanation: "Chronic rejection is the leading cause of long-term graft loss and currently has no reliable treatment once established. It involves progressive transplant vasculopathy (fibrosis and thickening of graft vessel walls) driven by a combination of immune factors (ongoing low-grade T cell and antibody responses) and non-immune factors (ischemia-reperfusion injury, drug toxicity, recurrence of original disease). Unlike acute rejection, which responds well to high-dose corticosteroids and calcineurin inhibitors, chronic rejection progresses despite immunosuppression. Hyperacute rejection (A) is prevented, not treated; acute rejection (B) is the primary target of standard immunosuppression and responds well when caught early."

- question: "Pretransplant crossmatch testing primarily aims to prevent hyperacute rejection by detecting preformed recipient antibodies against donor antigens."
  type: true-false
  answer: true
  explanation: "Crossmatch testing mixes recipient serum with donor lymphocytes before surgery. If the recipient has preformed antibodies against donor HLA molecules, they will bind donor cells and produce a positive crossmatch — a contraindication to transplantation. This test directly screens for the preformed antibodies that cause hyperacute rejection. Together with ABO blood group compatibility, crossmatch testing has made hyperacute rejection rare in modern transplant medicine, though it was a common cause of immediate graft loss before these protocols were established."

- question: "Chronic graft rejection is a purely immune-mediated process and can be fully prevented by maintaining adequate immunosuppression throughout the life of the graft."
  type: true-false
  answer: false
  explanation: "Chronic rejection involves both immune and non-immune mechanisms, which is why it responds poorly to immunosuppression even when intensified. Non-immune contributors include ischemia-reperfusion injury at the time of transplant, nephrotoxicity from calcineurin inhibitors themselves, hypertension, dyslipidemia, and recurrence of the original kidney disease. Even perfectly controlled immune rejection doesn't eliminate these factors. This mixed etiology explains why chronic rejection is the leading cause of long-term graft failure despite excellent short-term results with modern immunosuppression — and why HLA matching (reducing the immune stimulus) matters more than simply increasing drug doses."

- question: "Explain why HLA matching between donor and recipient reduces both acute and chronic rejection. Connect the mechanism to each type."
  type: short-answer
  answer: "HLA matching reduces the number of foreign allogeneic HLA molecules the recipient's immune system encounters. In acute rejection, T cells recognize donor MHC molecules as foreign alloantigens — each HLA mismatch represents a set of epitopes that can activate recipient T cell clones through direct or indirect allorecognition. More mismatches mean more T cell clones activated, a stronger and harder-to-control rejection response. In chronic rejection, ongoing low-grade immune responses against mismatched HLA molecules drive the progressive vasculopathy and fibrosis. Better HLA matching reduces the antigenic stimulus driving both processes: fewer foreign HLA molecules means weaker T cell activation, less antibody production against donor antigens, and slower accumulation of immune-mediated vascular damage. HLA matching thus improves both short-term rejection control and long-term graft survival."
```

## Explainer

From your study of transplant immunology and MHC molecules, you understand that every individual expresses a unique set of HLA proteins on their cell surfaces, and that the immune system is trained to recognize "self" MHC as friendly. When tissue from a genetically different donor is transplanted into a recipient, the donor's HLA molecules look foreign — they are **alloantigens**, and the recipient's immune system mounts a response against them. **Graft rejection** is this immune attack on transplanted tissue, and it manifests in three distinct forms defined by their timing and mechanism.

**Hyperacute rejection** is the fastest and most dramatic form, occurring within minutes to hours after transplantation. It happens when the recipient already has **preformed antibodies** against donor antigens — typically anti-ABO blood group antibodies or anti-HLA antibodies from prior transfusions, pregnancies, or transplants. These circulating antibodies bind immediately to the donor endothelium (the blood vessel lining of the graft), activate the complement cascade, and trigger massive thrombosis within the graft vasculature. The organ turns dark and necrotic, and there is no treatment — it must be removed. The good news is that hyperacute rejection is almost entirely preventable today through ABO blood type matching and **crossmatch testing**, where recipient serum is mixed with donor cells before surgery to check for preformed antibodies.

**Acute rejection** develops over days to weeks (sometimes months) and involves the full force of the adaptive immune response. The recipient's **T cells** recognize donor MHC molecules through two pathways: **direct allorecognition**, where recipient T cells bind directly to intact donor MHC molecules on donor antigen-presenting cells (which look like self-MHC loaded with foreign peptide), and **indirect allorecognition**, where recipient APCs process shed donor MHC molecules and present donor-derived peptides on self-MHC. Both CD4+ helper T cells and CD8+ cytotoxic T cells participate — cytotoxic T cells directly kill graft cells, while helper T cells drive inflammation and activate B cells to produce anti-donor antibodies. Acute rejection is the most common form encountered clinically and is the primary target of **immunosuppressive drugs** like cyclosporine and tacrolimus (calcineurin inhibitors that block T cell activation) and mycophenolate (which inhibits lymphocyte proliferation).

**Chronic rejection** is the slowest and most insidious form, developing over months to years and currently the leading cause of long-term graft loss. It involves progressive fibrosis and thickening of graft blood vessel walls (**transplant vasculopathy**), gradually strangling the organ's blood supply. The mechanisms are incompletely understood but involve both immune factors (ongoing low-grade T cell and antibody responses against donor antigens) and non-immune factors (ischemia-reperfusion injury, drug toxicity, and recurrence of the original disease). Unlike acute rejection, chronic rejection responds poorly to increased immunosuppression — there is no reliable treatment once it is established. This is why HLA matching remains so important: better matching reduces the alloimmune stimulus driving both acute and chronic rejection, improving long-term graft survival.
