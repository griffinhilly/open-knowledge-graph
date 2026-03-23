---
id: viral-infection-and-pathogenesis-mechanisms
title: Viral Infection and Pathogenesis Mechanisms
domain: biology
course: microbiology
prerequisites:
- id: viral-attachment-glycoproteins
  type: hard
- id: host-pathogen-interactions
  type: hard
builds-toward:
- bacterial-virulence-mechanisms
tags:
- pathogenesis
- infection
- host-cell
stage: advanced
status: validated
---

# Viral Infection and Pathogenesis Mechanisms

## Core Idea
Viral pathogenesis involves attachment to host receptors, entry (fusion, endocytosis, or injection), gene expression, replication, and egress. Virulence is determined by viral gene products (toxins, immune evasion), host factors (innate immunity, age), and epidemiological context. Cytopathic effects (cell lysis, syncytia, inclusion bodies) are hallmarks of viral infection.

## Questions

```yaml
- question: "HIV specifically infects CD4⁺ T cells rather than neurons or liver cells. What primarily determines this cellular tropism?"
  type: multiple-choice
  options:
    - "The strength of the innate immune response varies by tissue, directing the virus toward less-defended cell types"
    - "HIV preferentially infects rapidly dividing cells, and T cells divide more frequently than neurons"
    - "The specific binding of HIV's surface glycoprotein gp120 to the CD4 receptor on T cells"
    - "The size of the HIV virion matches the membrane pore size of CD4⁺ T cells"
  answer: 2
  explanation: "Tropism is determined at the attachment step by receptor specificity. HIV's gp120 glycoprotein binds specifically to the CD4 receptor (and a co-receptor such as CCR5 or CXCR4). Only cells expressing both receptors — primarily helper T cells, macrophages, and dendritic cells — are susceptible to HIV infection through this pathway. If a cell lacks the receptor, the virus cannot attach and entry cannot proceed. This is why the CCR5-delta32 mutation, which disrupts a co-receptor, confers near-complete resistance to HIV infection — the molecular key no longer fits the lock."

- question: "A newly discovered virus causes infected cells to fuse with neighboring uninfected cells, forming large multinucleate masses visible under the microscope. Which cytopathic effect is this, and what drives it?"
  type: multiple-choice
  options:
    - "Inclusion body formation — viral proteins aggregate inside the nucleus during replication and spill into neighboring cells"
    - "Lysis — infected cells rupture and release virions that physically merge with adjacent cells"
    - "Syncytia formation — viral fusion proteins expressed on the infected cell surface bind receptors on adjacent cells, fusing the membranes"
    - "Integration — the viral genome inserts itself into neighboring cells through membrane contact"
  answer: 2
  explanation: "Syncytia form because the same fusion proteins used during viral entry are expressed on the infected cell's outer surface after replication — where they can engage receptors on neighboring uninfected cells and fuse the two membranes. The result is a giant multinucleate cell representing the merger of many cells. Measles and RSV are classic examples. This is clinically significant because syncytia represent widespread cell destruction and can shield viral particles from antibody neutralization within the merged mass. Inclusion bodies (like the Negri bodies diagnostic of rabies) are a distinct cytopathic pattern — dense aggregates of viral components visible microscopically, not cell-fusion events."

- question: "The severity of a viral infection is determined entirely by the virus's own gene products — more virulent viruses simply encode more destructive proteins."
  type: true-false
  answer: false
  explanation: "Virulence is determined by both viral and host factors. The same virus can cause drastically different outcomes in different hosts: influenza is typically mild in healthy adults but life-threatening in elderly or immunocompromised patients; HIV progresses to AIDS rapidly in some hosts and slowly in others, partly due to host genetic factors like the CCR5-delta32 mutation. Host factors include innate immune response strength, age, nutritional status, prior immune exposure, and genetic variation in immune receptors. Disease outcome is always a dynamic interaction — the virus's offensive capabilities interact with the host's defensive capacity at every stage."

- question: "Receptor specificity at the attachment step is the primary determinant of which cell types a virus can infect."
  type: true-false
  answer: true
  explanation: "Attachment is the first and most specific step of infection. A virus can only infect cells that display the receptor its surface proteins recognize. This receptor specificity defines tropism — which cell types, tissues, and even species are susceptible. HIV targets CD4⁺ T cells because gp120 binds CD4; rabies targets neurons because its glycoprotein G binds the nicotinic acetylcholine receptor. If the receptor is absent or blocked (as with anti-receptor antibodies or the CCR5-delta32 mutation), the virus cannot proceed regardless of other factors. Subsequent steps — entry, replication, immune evasion — determine the infection's severity, but attachment determines whether infection is even possible."

- question: "Why is viral pathogenesis better understood as a dynamic interplay between viral offense and host defense, rather than as a simple cause-and-effect sequence of infection producing disease?"
  type: short-answer
  answer: "Disease outcome is not determined by viral attack alone but by the ongoing contest between what the virus does and how the host responds at each step. Many dangerous viruses are dangerous precisely because they have evolved specific immune evasion strategies — blocking interferon induction, preventing apoptosis, downregulating MHC presentation. If pathogenesis were simply 'virus attacks, disease results,' these evasion mechanisms would be irrelevant. Instead, they are often the primary determinants of virulence: the same viral genome that devastates an immunocompromised host may be cleared asymptomatically in a host with a robust innate response. The outcome is always negotiated between the virus's offensive toolkit and the host's defensive capacity."
  explanation: "This interplay framing has direct therapeutic implications: antivirals can be designed to target any of several steps (blocking receptor binding, inhibiting polymerase, preventing egress), and immunotherapies can bolster the host's defensive side of the contest. Understanding which step is the bottleneck in a given infection guides treatment strategy. It also explains why the same virus produces a spectrum of outcomes across a population — host variation, not just viral variation, is half the equation."
```

## Explainer

From your study of viral attachment glycoproteins and host-pathogen interactions, you know that viruses cannot replicate on their own — they must hijack a host cell's machinery. Viral pathogenesis is the study of how this hijacking unfolds step by step and how it produces disease. The process follows a stereotyped sequence: **attachment**, **entry**, **gene expression and replication**, **assembly**, and **egress**. Each step presents both a vulnerability the host immune system can exploit and a point where the virus has evolved countermeasures.

**Attachment** is the first and most specific step. The viral surface proteins you studied — glycoproteins like HIV's gp120 or influenza's hemagglutinin — bind to particular receptors on host cells. This receptor specificity is what determines **tropism**: which cell types, tissues, and even species a virus can infect. HIV targets CD4⁺ T cells because gp120 binds the CD4 receptor; rabies virus targets neurons because its glycoprotein G binds the nicotinic acetylcholine receptor. After attachment, **entry** occurs by one of three general mechanisms: direct fusion of viral and host membranes (HIV), receptor-mediated endocytosis followed by pH-triggered fusion in the endosome (influenza), or injection of the genome through the cell wall (bacteriophages). The entry route matters clinically because it determines which antiviral strategies can block infection at the earliest stage.

Once inside, the virus redirects host ribosomes, polymerases, and metabolic resources to produce viral proteins and copy the viral genome. This is where **virulence factors** come into play. Some viruses encode proteins that shut down host protein synthesis (poliovirus cleaves eIF4G), redirect immune signaling (Ebola's VP35 blocks interferon induction), or prevent apoptosis so the infected cell survives long enough to produce more virions. The observable damage to infected cells — **cytopathic effects** — takes several characteristic forms: **lysis** (the cell bursts, releasing new virions), **syncytia formation** (viral fusion proteins on the cell surface cause neighboring cells to merge into giant multinucleate masses, as seen with measles and RSV), and **inclusion bodies** (dense aggregates of viral components visible under the microscope, like the Negri bodies diagnostic of rabies).

The outcome of infection depends on the balance between viral offense and host defense. A virus that replicates explosively and lyses cells causes acute disease (influenza, norovirus), while one that integrates into the genome or persists in a latent state causes chronic or recurrent disease (HIV, herpes simplex). The host's innate immune response — interferon signaling, natural killer cells, inflammation — acts as the first line of defense, and many of the most dangerous viruses are dangerous precisely because they have evolved ways to evade or suppress this response. Understanding pathogenesis as a dynamic interplay between viral strategy and host counterstrategy, rather than a simple cause-and-effect, is the key insight that connects molecular virology to clinical medicine.
