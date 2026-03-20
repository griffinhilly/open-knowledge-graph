---
id: viral-attachment-glycoproteins
title: Viral Attachment Proteins and Receptor Binding
domain: biology
course: microbiology
prerequisites:
- id: viral-envelope-lipids-glycoproteins
  type: hard
- id: cell-membrane-structure
  type: soft
builds-toward:
- viral-replication-dna-polymerase
- viral-replication-rna-polymerase
tags:
- attachment
- receptor-binding
- tropism
stage: advanced
status: draft
---

# Viral Attachment Proteins and Receptor Binding

## Core Idea
Viral attachment proteins (e.g., spike proteins, gp120) recognize and bind specific host cell receptors, determining tissue tropism and host range. Receptor binding is highly specific and can be blocked by host immune responses; mutations in attachment proteins are a major mechanism of viral immune escape and emergence of new viral strains.

## Explainer

From your study of viral envelopes, you know that enveloped viruses are surrounded by a lipid bilayer studded with glycoproteins. **Viral attachment proteins** are the specific glycoproteins responsible for the very first step of infection: recognizing and binding a molecule on the host cell surface. This interaction is the molecular handshake that determines whether a virus can infect a given cell type, tissue, or even species. Without a successful attachment event, the virus cannot enter the cell, and infection cannot begin.

The specificity of this interaction is remarkably precise — think of it as a lock-and-key fit between the viral attachment protein and a host **receptor**. HIV's gp120 protein binds the CD4 receptor found on helper T cells, which is why HIV specifically destroys the immune system rather than, say, liver cells. SARS-CoV-2's spike protein binds ACE2 receptors, which are abundant on cells lining the respiratory tract and blood vessels, explaining the virus's respiratory tropism and vascular complications. Influenza hemagglutinin binds sialic acid residues on respiratory epithelial cells. In each case, the distribution of the receptor across host tissues defines the virus's **tropism** — which cells and organs it can infect — and across species defines its **host range**.

Because attachment proteins are exposed on the viral surface, they are prime targets for the host immune system. **Neutralizing antibodies** work largely by binding to the attachment protein and physically blocking its interaction with the host receptor — like jamming a key so it cannot enter the lock. This is why most vaccines aim to generate antibodies against attachment proteins: the spike protein in COVID-19 vaccines, hemagglutinin in influenza vaccines. However, attachment proteins are also under intense evolutionary pressure precisely because they are so exposed. Mutations in the receptor-binding domain can alter the protein's shape enough to escape existing antibodies while still maintaining receptor binding — a process called **antigenic variation** or immune escape.

This evolutionary arms race has profound consequences. Influenza's hemagglutinin undergoes both gradual mutation (**antigenic drift**) and wholesale segment exchange with animal influenza strains (**antigenic shift**), which is why new flu vaccines are needed annually and why pandemic strains occasionally emerge. When a mutation in an attachment protein allows a virus to bind a receptor in a new host species — for example, when an avian influenza hemagglutinin acquires mutations enabling it to bind human-type sialic acid linkages — a zoonotic spillover event can occur. Understanding the molecular details of viral attachment is therefore central to predicting pandemic risk, designing vaccines, and developing antiviral drugs that block the very first step of infection.
