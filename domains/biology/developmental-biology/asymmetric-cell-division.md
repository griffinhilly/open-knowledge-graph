---
id: asymmetric-cell-division
title: Asymmetric Cell Division
domain: biology
course: developmental-biology
prerequisites:
- id: cell-fate-determination
  type: hard
- id: mitosis
  type: hard
builds-toward: []
tags:
- asymmetric-division
- cell-polarity
- Par-complex
- Numb
- neuroblast
stage: expert
status: validated
---
# Asymmetric Cell Division

## Core Idea
Asymmetric cell division produces two daughter cells with different fates by unequally distributing fate determinants (proteins or mRNAs) to one side of the dividing cell and then placing the cleavage plane such that each daughter inherits a different set of determinants. The mechanism requires cell polarity (establishing molecular asymmetry within the cell, typically via Par protein complexes), asymmetric localization of fate determinants (like Numb, Prospero, Miranda), and mitotic spindle orientation aligned with the polarity axis. Asymmetric division is fundamental to stem cell self-renewal (one daughter remains a stem cell, the other differentiates) and to the generation of cell-type diversity during development.

## Questions

```yaml
- question: "In Drosophila neuroblast division, the Par complex (Par3/Par6/aPKC) localizes to the apical side and Numb localizes to the basal side. If the Par complex is mutated so that it distributes uniformly, what happens to the division?"
  type: multiple-choice
  options:
    - "Division becomes symmetric — both daughters adopt the same fate because the asymmetric localization of determinants like Numb is disrupted"
    - "The cell fails to divide entirely"
    - "Both daughters become neurons immediately"
    - "The cell divides normally because Par proteins are not involved in asymmetric division"
  answer: 0
  explanation: "The Par complex is the master regulator of cell polarity during asymmetric division. It excludes basal determinants (Numb, Miranda/Prospero) from the apical cortex, concentrating them at the basal side. When Par complex function is lost, Numb distributes uniformly, and both daughters receive equal amounts — producing symmetric division where both daughters adopt the same fate (typically both self-renew, leading to neuroblast overproliferation and tumor formation). This demonstrates that fate asymmetry requires active polarization machinery, not just the presence of fate determinants."

- question: "Asymmetric cell division is the only mechanism by which stem cells produce one self-renewing and one differentiating daughter."
  type: true-false
  answer: false
  explanation: "While intrinsic asymmetric division (unequal distribution of fate determinants) is one mechanism, an alternative is extrinsic (niche-mediated) asymmetry: a stem cell divides symmetrically, producing two initially equivalent daughters, but one remains in the stem cell niche (retaining stem cell identity due to niche signals) while the other is displaced from the niche and differentiates due to loss of self-renewal signals. This 'population asymmetry' mechanism is used by intestinal stem cells and some other tissue stem cells. The two mechanisms are not mutually exclusive — both can operate in the same tissue."

- question: "How does spindle orientation ensure that asymmetrically localized determinants are correctly partitioned between the two daughter cells?"
  type: short-answer
  answer: "The mitotic spindle must align with the axis of cell polarity so that the cleavage plane bisects the cell perpendicular to the polarity axis, placing apical determinants in one daughter and basal determinants in the other. Spindle orientation is controlled by cortically anchored proteins (like Pins/LGN and Mud/NuMA in Drosophila/vertebrates) that capture astral microtubules and pull the spindle poles toward specific cortical positions. If spindle orientation is randomized (by disrupting the anchoring machinery), the cleavage plane no longer correlates with the determinant distribution, and both daughters receive a mixture — abolishing fate asymmetry. Correct spindle orientation is thus as essential as determinant localization for functional asymmetric division."
  explanation: "In Drosophila neuroblasts, the Pins/Mud complex anchors to the apical cortex (defined by the Par complex), pulling one spindle pole apically and the other basally. This ensures the division plane separates the apical and basal cortical domains, partitioning apical (self-renewal) and basal (differentiation) determinants into different daughters."
```

## Explainer

When a cell divides, the default outcome is two identical daughters. But development and tissue maintenance often require divisions that produce two different daughters — a stem cell and a committed progenitor, or a neuron and a glial cell. **Asymmetric cell division** achieves this by introducing molecular differences within the parent cell before it divides, then partitioning those differences into the two daughters through controlled placement of the division plane.

The mechanism involves three coordinated steps. First, **cell polarity** is established. In Drosophila neuroblasts (the best-studied system), the **Par complex** (Par3/Bazooka, Par6, and aPKC) localizes to the apical cortex. This polarity is not intrinsic — it is established in response to cues from the overlying epithelium and maintained by self-reinforcing interactions between Par complex components. Second, **fate determinants are asymmetrically localized**. The Par complex excludes certain proteins from the apical domain, concentrating them at the basal cortex. In neuroblasts, the adaptor protein **Miranda** (carrying the transcription factor Prospero) and the Notch inhibitor **Numb** are confined to a basal crescent by aPKC-mediated phosphorylation. Third, the **mitotic spindle orients** along the apical-basal polarity axis, ensuring that the cleavage plane separates the apical and basal cortical domains into different daughters.

The result is two daughters with fundamentally different molecular compositions. The apical daughter inherits the Par complex and self-renewal signals, maintaining neuroblast identity. The basal daughter inherits Numb (which inhibits Notch signaling, promoting differentiation) and Prospero (which activates cell-cycle exit genes and neuronal differentiation genes). From a single division, the mother cell produces one daughter that remains a stem cell and one that begins differentiating — the essence of asymmetric division.

Asymmetric division is widespread: mammalian neural progenitors, Drosophila germline stem cells, C. elegans zygotes (the P lineage), and hematopoietic stem cells all employ variations of this mechanism. The molecular details differ (different polarity cues, different fate determinants), but the logic is conserved: polarize the cell, localize determinants, align the spindle, divide. Defects in asymmetric division have direct pathological consequences — in Drosophila, loss of polarity in neuroblasts produces symmetric self-renewing divisions that generate brain tumors. In mammals, disrupted asymmetric division in stem cell compartments is implicated in cancer initiation, connecting this fundamental developmental mechanism to one of the most consequential problems in medicine.
