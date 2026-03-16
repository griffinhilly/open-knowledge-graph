---
id: autoimmune-disease-pathophysiology-adv
title: Autoimmune Disease Pathophysiology (Advanced)
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: autoimmune-disease-mechanisms
  type: hard
- id: regulatory-t-cells-immune-tolerance
  type: hard
- id: loss-of-central-tolerance
  type: soft
- id: immune-tolerance-central-and-peripheral
  type: soft
builds-toward:
- systemic-lupus-erythematosus
- rheumatoid-arthritis-pathophysiology
tags:
- autoimmune-disease
- immune-tolerance
- self-reactivity
stage: advanced
status: draft
---

# Autoimmune Disease Pathophysiology (Advanced)

## Core Idea
Autoimmune diseases arise from loss of self-tolerance through breakdown of central (thymic) and peripheral mechanisms. Genetic predisposition (HLA associations), environmental triggers (infection, molecular mimicry), and epigenetic changes converge to activate autoreactive T and B cells.

## How It's Best Learned
Study organ-specific (type 1 diabetes, Hashimoto's) vs. systemic (lupus, rheumatoid arthritis) autoimmunity. Review disease-specific autoantibodies and their pathogenic roles. Understand Treg dysfunction and loss of anergy as mechanisms.

## Common Misconceptions
Autoantibodies are not always pathogenic—they may be bystanders. HLA association does not determine disease; penetrance is low, and environmental factors are required. Not all autoimmune diseases involve Th1 responses; many involve Th17 or Tfh cells.

## Explainer

From your study of immune tolerance, you know that the immune system faces a fundamental engineering problem: it must attack foreign pathogens while leaving the body's own tissues alone. Central tolerance, carried out in the thymus, deletes T cells that bind too strongly to self-antigens displayed on thymic stromal cells — negative selection. Peripheral tolerance — anergy, Treg suppression, activation-induced cell death — catches autoreactive cells that escape the thymus. Autoimmune disease occurs when both layers fail, and autoreactive lymphocytes are not merely present (they exist in everyone at low levels) but are activated, expanded, and sustained.

The triggering of autoimmunity typically requires a convergence of factors. **Genetic susceptibility** is the foundation: HLA alleles explain more genetic risk for autoimmune diseases than any other locus, because HLA molecules determine which self-peptides can be presented during thymic selection and which peripheral antigens trigger responses. HLA-DR4 is strongly associated with rheumatoid arthritis; HLA-B27 with ankylosing spondylitis; specific HLA-DR alleles with type 1 diabetes. But HLA is not sufficient — concordance in identical twins for most autoimmune diseases is only 30–50%, meaning environmental triggers must act on susceptible genotypes. **Molecular mimicry** is one such trigger: an infectious pathogen displays peptide sequences similar enough to self-proteins that T cells expanded against the pathogen cross-react with self-tissue once the infection resolves. Streptococcal M protein mimicking cardiac myosin in rheumatic fever is the canonical example; similar mechanisms are hypothesized for multiple sclerosis following Epstein-Barr virus infection.

Once autoreactive T cells are activated, the downstream pathology depends on which self-antigen is targeted and which T helper subset dominates. **Th1-driven** responses (IFN-γ, macrophage activation) produce tissue destruction through cytotoxic T cells — characteristic of type 1 diabetes (islet cell destruction) and multiple sclerosis (myelin destruction). **Th17-driven** responses (IL-17, neutrophil recruitment) produce neutrophilic inflammation characteristic of rheumatoid arthritis synovitis and inflammatory bowel disease. **Tfh (T follicular helper)**-driven responses amplify B cell activation and autoantibody production, central to lupus, myasthenia gravis, and Graves' disease. Autoantibodies can act through three distinct mechanisms: directly blocking a receptor (anti-AChR antibodies in myasthenia gravis), stimulating a receptor (anti-TSH receptor in Graves' disease), or forming immune complexes that deposit in tissue and activate complement (anti-dsDNA antibodies in lupus nephritis).

**Regulatory T cells** expressing FoxP3 are the brake on all of this. Treg deficiency or dysfunction — through mutations in FOXP3 (causing the catastrophic multi-organ IPEX syndrome), or through cytokine microenvironments that convert Tregs to effector cells — allows autoreactive responses to escape suppression. In many established autoimmune diseases, the immunological balance tips chronically toward inflammation: IL-6 promotes Th17 differentiation while simultaneously inhibiting Treg differentiation, creating a positive feedback loop that sustains disease even after the original trigger is long gone. This is why autoimmune diseases tend to be relapsing-remitting or chronically progressive rather than self-limited — the immune architecture that should suppress autoimmunity has been remodeled by the disease itself. Understanding this framework maps directly onto modern therapeutics: anti-TNF drugs target macrophage-mediated inflammation, anti-IL-17 and anti-IL-23 target the Th17 axis, rituximab depletes B cells, and abatacept blocks T cell co-stimulation. Each is most effective when the pathway it targets is the dominant one in a specific disease.
