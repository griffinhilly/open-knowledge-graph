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
stage: advanced
status: draft
---

# Viral Attachment, Tropism, and Host Cell Entry

## Core Idea
Viral attachment is mediated by spike proteins or surface glycoproteins that recognize specific cellular receptors (proteins, carbohydrates, or lipids), determining viral host range and tissue tropism. Entry mechanisms include receptor-mediated endocytosis (influenza, HIV), membrane fusion triggered by receptor binding (measles, Ebola), and direct genome injection (bacteriophages). The specificity of these interactions explains why viruses productively infect particular cell types and species.

## Questions

```yaml
- question: "HIV infects helper T cells but not liver cells, even though both cell types are present in an infected person. A student suggests this is because HIV 'seeks out' immune cells. What actually accounts for this specificity?"
  type: multiple-choice
  options:
    - "HIV contains internal signal sequences that direct it to lymphoid tissue after entry into the bloodstream"
    - "HIV's gp120 surface protein binds specifically to the CD4 receptor, which is expressed on helper T cells but not on hepatocytes — receptor availability on the cell surface determines which cells can be productively infected"
    - "The immune system concentrates incoming viruses in lymphoid organs, where T cells happen to be abundant"
    - "HIV replicates faster in T cells because they divide more rapidly, giving the virus a selective advantage there"
  answer: 1
  explanation: "Viral tropism is determined at the molecular level by receptor-ligand specificity. HIV's gp120 envelope protein binds the CD4 receptor (and a co-receptor, CCR5 or CXCR4). Hepatocytes do not express CD4, so HIV cannot attach to them regardless of how much virus is present. The virus has no 'sensing' mechanism — it simply binds cells that happen to display the right receptor. This molecular lock-and-key principle explains why different viruses cause disease in different tissues and species."

- question: "Influenza virus is taken up by receptor-mediated endocytosis and fuses with the endosomal membrane rather than with the plasma membrane at the cell surface. What specifically triggers fusion inside the endosome?"
  type: multiple-choice
  options:
    - "Lysosomal proteases cleave the viral hemagglutinin, exposing its hydrophobic fusion peptide"
    - "The acidic pH of the maturing endosome triggers a conformational change in hemagglutinin that exposes the fusion peptide and drives viral and endosomal membranes together"
    - "Calcium ions released from the endosomal lumen activate the viral fusion machinery"
    - "Hydrolysis of the viral RNA genome releases energy that powers the membrane fusion event"
  answer: 1
  explanation: "Influenza exploits the endosomal acidification that normally occurs as endosomes mature. Hemagglutinin is a spring-loaded protein: at neutral pH, it holds the fusion peptide shielded. When the endosome acidifies to pH ~5, hemagglutinin undergoes an irreversible conformational change — it extends like a harpoon and embeds its fusion peptide into the endosomal membrane, pulling the two membranes together. This pH-triggered mechanism is why drugs that prevent endosomal acidification (like chloroquine) inhibit influenza infection. It also illustrates how viruses hijack normal cellular processes for entry."

- question: "Non-enveloped viruses enter host cells by membrane fusion, the same mechanism used by enveloped viruses like HIV and measles."
  type: true-false
  answer: false
  explanation: "Membrane fusion requires two lipid bilayers to merge — the viral envelope and the host membrane. Non-enveloped viruses lack an outer membrane altogether; they consist only of a protein capsid surrounding the genome. Without a membrane to fuse, they must use a fundamentally different strategy: disrupting the host membrane to deliver their genome. Common mechanisms include lysis of the endosomal membrane (adenoviruses escape the endosome by rupturing it) or forming pores in the membrane. Bacteriophages take the most distinct approach — injecting their genome directly through the cell wall while the capsid remains outside."

- question: "The specificity of the match between a viral attachment protein and its cellular receptor is the primary determinant of which host species and cell types a virus can productively infect."
  type: true-false
  answer: true
  explanation: "This receptor-tropism relationship is the central principle of viral host range and tissue specificity. HIV-CD4, influenza hemagglutinin-sialic acid, SARS-CoV-2 spike-ACE2 — in each case the identity of the receptor constrains which cells the virus can enter. A virus cannot productively infect a cell that lacks its receptor, regardless of what happens after entry. This principle also explains species barriers: a virus adapted to a bird receptor may bind poorly to the human homolog of that receptor, limiting zoonotic transmission unless mutations improve affinity."

- question: "Why can most viruses not easily jump between host species, and what must change at the molecular level for a successful cross-species transmission event to occur?"
  type: short-answer
  answer: "Viruses are adapted to bind specific receptor molecules, and the receptor for a given viral attachment protein in one species may differ enough from the same receptor in another species that the virus cannot bind efficiently. For cross-species transmission to succeed, the viral attachment protein must acquire mutations that improve its affinity for the new host's receptor variant. For example, SARS-CoV-2's spike protein binds human ACE2 effectively because mutations in its receptor-binding domain increased affinity relative to the bat coronavirus from which it descended. Without such mutations, the virus cannot attach, enter, and replicate in the new host at levels needed to establish infection."
  explanation: "This is why pandemic potential is assessed partly by monitoring mutations in attachment proteins (like influenza's hemagglutinin). Each mutation that improves binding to a human receptor represents a step toward a variant capable of human-to-human transmission. The receptor-binding interface is also the primary target for neutralizing antibodies and antiviral drugs, since blocking attachment before entry prevents infection altogether."
```

## Explainer

From your study of viral attachment glycoproteins, you know that viruses carry surface proteins capable of binding to molecules on host cells. The critical next question is: what determines *which* cells a virus can infect? The answer lies in **viral tropism** — the specificity of the match between a viral surface protein and its cellular receptor. Just as a key fits only certain locks, a viral spike protein binds only to cells displaying the right receptor molecule. HIV's gp120 protein binds CD4 receptors found primarily on helper T cells, which is why HIV destroys the immune system rather than, say, liver tissue. Influenza's hemagglutinin binds sialic acid residues on respiratory epithelial cells, confining the initial infection to the airways. The receptor determines the target; the target determines the disease.

Once a virus has attached, it must cross the cell membrane — the lipid bilayer barrier you studied in cell membrane structure. Enveloped viruses (those wrapped in a stolen patch of host membrane) typically enter by **membrane fusion**: the viral envelope merges directly with the host membrane, dumping the viral genome into the cytoplasm. This fusion can happen at the cell surface, as with measles virus, or inside an endosome after the virus has been swallowed by receptor-mediated endocytosis, as with influenza. Influenza exploits the acidic pH of the endosome as a trigger — its hemagglutinin protein undergoes a dramatic conformational change at low pH, driving the viral and endosomal membranes together like a spring-loaded harpoon.

Non-enveloped viruses face a different challenge: they lack a membrane to fuse. Instead, they must punch through or destabilize the host membrane to deliver their genome. Adenoviruses, for example, lyse the endosomal membrane after endocytosis, escaping into the cytoplasm. Bacteriophages take the most elegant approach of all — **direct genome injection**. A phage lands on a bacterial cell, attaches via tail fibers, and contracts its tail sheath to drive a hollow needle through the bacterial cell wall, injecting DNA while the protein coat remains outside. This is why phage infection was historically described as working like a hypodermic syringe.

The specificity of attachment and entry has profound practical consequences. It explains why most viruses cannot jump easily between species — a virus adapted to bind chicken receptors may not recognize the human version of that protein. When cross-species jumps do occur (as with SARS-CoV-2 binding human ACE2), it often requires mutations in the viral attachment protein that improve affinity for the new receptor. Understanding these molecular handshakes is also the basis for antiviral drug design: blocking the attachment protein or the fusion machinery can prevent infection before the viral genome ever reaches the cell interior.
