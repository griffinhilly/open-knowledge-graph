---
id: viral-attachment-and-entry-mechanisms
title: Viral Attachment, Tropism, and Host Cell Entry
domain: biology
course: microbiology
prerequisites:
- id: viral-attachment-glycoproteins
  type: hard
- id: cell-membrane-structure
  type: hard
builds-toward:
- viral-replication-strategies-rna-vs-dna
- viral-pathogenesis-and-disease
tags:
- viral-entry
- attachment
- tropism
- receptor
stage: formal-systems
status: draft
---

# Viral Attachment, Tropism, and Host Cell Entry

## Core Idea
Viral attachment is mediated by spike proteins or surface glycoproteins that recognize specific cellular receptors (proteins, carbohydrates, or lipids), determining viral host range and tissue tropism. Entry mechanisms include receptor-mediated endocytosis (influenza, HIV), membrane fusion triggered by receptor binding (measles, Ebola), and direct genome injection (bacteriophages). The specificity of these interactions explains why viruses productively infect particular cell types and species.

## Explainer

From your study of viral attachment glycoproteins, you know that viruses carry surface proteins capable of binding to molecules on host cells. The critical next question is: what determines *which* cells a virus can infect? The answer lies in **viral tropism** — the specificity of the match between a viral surface protein and its cellular receptor. Just as a key fits only certain locks, a viral spike protein binds only to cells displaying the right receptor molecule. HIV's gp120 protein binds CD4 receptors found primarily on helper T cells, which is why HIV destroys the immune system rather than, say, liver tissue. Influenza's hemagglutinin binds sialic acid residues on respiratory epithelial cells, confining the initial infection to the airways. The receptor determines the target; the target determines the disease.

Once a virus has attached, it must cross the cell membrane — the lipid bilayer barrier you studied in cell membrane structure. Enveloped viruses (those wrapped in a stolen patch of host membrane) typically enter by **membrane fusion**: the viral envelope merges directly with the host membrane, dumping the viral genome into the cytoplasm. This fusion can happen at the cell surface, as with measles virus, or inside an endosome after the virus has been swallowed by receptor-mediated endocytosis, as with influenza. Influenza exploits the acidic pH of the endosome as a trigger — its hemagglutinin protein undergoes a dramatic conformational change at low pH, driving the viral and endosomal membranes together like a spring-loaded harpoon.

Non-enveloped viruses face a different challenge: they lack a membrane to fuse. Instead, they must punch through or destabilize the host membrane to deliver their genome. Adenoviruses, for example, lyse the endosomal membrane after endocytosis, escaping into the cytoplasm. Bacteriophages take the most elegant approach of all — **direct genome injection**. A phage lands on a bacterial cell, attaches via tail fibers, and contracts its tail sheath to drive a hollow needle through the bacterial cell wall, injecting DNA while the protein coat remains outside. This is why phage infection was historically described as working like a hypodermic syringe.

The specificity of attachment and entry has profound practical consequences. It explains why most viruses cannot jump easily between species — a virus adapted to bind chicken receptors may not recognize the human version of that protein. When cross-species jumps do occur (as with SARS-CoV-2 binding human ACE2), it often requires mutations in the viral attachment protein that improve affinity for the new receptor. Understanding these molecular handshakes is also the basis for antiviral drug design: blocking the attachment protein or the fusion machinery can prevent infection before the viral genome ever reaches the cell interior.
