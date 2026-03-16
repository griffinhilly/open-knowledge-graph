---
id: protein-quaternary-structure
title: Protein Quaternary Structure
domain: biology
course: biochemistry
prerequisites:
- id: protein-tertiary-structure
  type: hard
builds-toward:
- allosteric-enzyme-regulation
- enzyme-cooperativity
tags:
- quaternary structure
- subunits
- multimeric proteins
- cooperativity
- homo-oligomers
stage: advanced
status: draft
---

# Protein Quaternary Structure

## Core Idea
Quaternary structure is the arrangement of multiple polypeptide subunits (chains) in a multi-subunit protein complex. Subunits are held together by the same non-covalent interactions that stabilize tertiary structure (hydrophobic effects, hydrogen bonds, ionic interactions). Quaternary structure enables cooperative binding, allosteric regulation, and complex enzymatic functions that single-subunit proteins cannot achieve.

## How It's Best Learned
Study hemoglobin as a classic example of quaternary structure and cooperativity: visualize the T (tense, deoxyhemoglobin) and R (relaxed, oxyhemoglobin) states and see how oxygen binding to one subunit facilitates binding to others.

## Explainer

You already understand how a single polypeptide chain folds into its tertiary structure through hydrophobic interactions, hydrogen bonds, ionic interactions, and disulfide bonds. **Quaternary structure** extends this picture to proteins that are built from more than one polypeptide chain. Each chain is called a **subunit**, and the assembled multi-subunit complex is the functional protein. The forces holding subunits together are the same non-covalent interactions you studied in tertiary structure — hydrophobic surfaces on one subunit pack against complementary hydrophobic patches on another, stabilized by hydrogen bonds and salt bridges at the interface. Some multi-subunit proteins also use disulfide bonds between chains (as in antibodies), but most rely entirely on non-covalent contacts.

Proteins with identical subunits are called **homo-oligomers** (a homodimer has two identical subunits, a homotetramer has four), while those with different subunits are **hetero-oligomers**. Hemoglobin is a classic hetero-oligomer: an α₂β₂ tetramer consisting of two α-globin and two β-globin subunits, each carrying its own heme group. The reason hemoglobin is a tetramer rather than a monomer like myoglobin reveals why quaternary structure matters: it enables **cooperativity**. When the first oxygen molecule binds to one hemoglobin subunit, it triggers a conformational change that is transmitted across the subunit interfaces, shifting the entire tetramer from the **T (tense) state** to the **R (relaxed) state**. This makes the remaining subunits bind oxygen more readily. The result is a sigmoidal oxygen-binding curve — steep in the middle, flat at the extremes — instead of the hyperbolic curve of myoglobin. This sigmoidal behavior allows hemoglobin to load oxygen efficiently in the lungs (where O₂ is abundant) and release it efficiently in the tissues (where O₂ is scarce).

Beyond cooperativity, quaternary structure enables **allosteric regulation** — the binding of regulatory molecules at sites distant from the active site that modulate the protein's activity. In hemoglobin, 2,3-bisphosphoglycerate (2,3-BPG) binds in the central cavity between the β subunits, stabilizing the T state and reducing oxygen affinity — an adaptation that fine-tunes oxygen delivery to tissues. Enzymes like aspartate transcarbamoylase (ATCase) use quaternary structure to separate catalytic and regulatory subunits entirely, allowing feedback inhibitors to control activity without competing at the active site. These behaviors are impossible in a single-chain protein because they require the transmission of conformational signals across subunit interfaces — a property that emerges only at the quaternary level.
