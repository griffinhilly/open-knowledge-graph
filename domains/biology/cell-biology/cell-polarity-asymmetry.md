---
id: cell-polarity-asymmetry
title: Cell Polarity and Establishment of Asymmetry
domain: biology
course: cell-biology
prerequisites:
- id: plasma-membrane-organization-dynamics
  type: soft
tags:
- cell-polarity
- asymmetry
- par-proteins
- development
stage: formal-systems
status: draft
---

# Cell Polarity and Establishment of Asymmetry

## Core Idea
Epithelial cells establish distinct apical (exposed to lumen) and basolateral (facing blood) domains with different lipid and protein compositions. PAR proteins (Par3, Par6, PKCζ, Par1) create an apical domain and exclude basolateral proteins; tight junctions (claudins, occludin, JAMs) seal the epithelium and maintain domain separation. Distinct delivery of vesicles to each domain via motility, and selective retention of domain-specific proteins, maintains asymmetry. Cell polarity is essential for proper tissue function; loss of polarity is associated with developmental defects and cancer progression.

## Questions

```yaml
- question: "A researcher uses a genetic approach to eliminate aPKC activity in fully polarized epithelial cells. What is the most likely consequence for the apical and basolateral membrane domains?"
  type: multiple-choice
  options:
    - "The apical domain expands and overruns the basolateral domain, since aPKC normally restrains apical identity"
    - "Polarity collapses — without aPKC activity, the mutual antagonism that excludes basolateral proteins from the apical zone is lost, allowing the domains to mix"
    - "The basolateral domain is lost but apical identity is maintained, since tight junctions physically prevent protein mixing after initial polarization"
    - "Nothing changes immediately, because once tight junctions are established they are sufficient to maintain polarity without ongoing PAR signaling"
  answer: 1
  explanation: "aPKC (part of the Par3/Par6/aPKC complex) maintains polarity through active, ongoing phosphorylation: it phosphorylates Par1 and Lgl to exclude them from the apical domain. Without aPKC activity, this exclusion stops. Par1 and other basolateral determinants can invade the apical zone, while Par3 is no longer maintained away from the basolateral side. The polarity boundary collapses because it is dynamic — maintained by continuous mutual antagonism, not by physical structure alone. Tight junctions do create a fence, but they cannot prevent mixing when the upstream biochemical machinery that establishes distinct domains is disrupted."

- question: "Which statement accurately describes the full role of tight junctions in maintaining epithelial cell polarity?"
  type: multiple-choice
  options:
    - "Tight junctions establish polarity by recruiting PAR proteins to the apical domain during initial polarization"
    - "Tight junctions function only as a paracellular barrier, preventing molecules from passing between adjacent cells"
    - "Tight junctions serve both as a paracellular barrier between cells AND as a membrane fence that prevents apical proteins from drifting laterally into the basolateral domain"
    - "Tight junctions act as scaffolds that anchor the PAR complex and prevent it from being degraded"
  answer: 2
  explanation: "Tight junctions have two distinct and equally important functions in epithelial polarity. First, as a paracellular barrier: composed of claudins, occludin, and JAMs, they stitch adjacent cells so tightly that even small molecules cannot pass between them — forcing transcellular transport and giving the epithelium control over what crosses. Second, as a membrane fence: by sitting at the boundary between apical and basolateral domains, tight junctions prevent membrane proteins from diffusing laterally from one domain to the other. Without this fence, even a well-established apical domain would gradually lose its identity as proteins mix. Option B is the common misconception — recognizing only the paracellular barrier function and missing the membrane fence role."

- question: "Loss of epithelial cell polarity is associated with cancer metastasis because cells that lose their organized architecture can detach from their tissue, invade surrounding structures, and spread to distant sites."
  type: true-false
  answer: true
  explanation: "This connection between polarity loss and cancer is mechanistically grounded. In epithelial-to-mesenchymal transition (EMT), cancer cells disrupt PAR signaling, downregulate tight junction components, and lose the apicobasal organization that anchors them to the epithelium. Without polarity, cells no longer maintain their position within the tissue layer, can degrade the basement membrane, and acquire migratory capacity. The same PAR proteins that establish developmental polarity are tumor suppressors — loss of Lgl, for example, correlates with aggressive cancer phenotypes. Polarity is therefore not merely an organizational feature but a determinant of tissue integrity."

- question: "The PAR complex establishes apical cell polarity by attracting and converting basolateral proteins to an apical identity."
  type: true-false
  answer: false
  explanation: "The PAR complex does not convert basolateral proteins — it excludes them through phosphorylation. aPKC phosphorylates Par1 and Lgl, causing them to be removed from the apical zone and confined to the basolateral domain. Reciprocally, Par1 phosphorylates Par3 to exclude it from the basolateral side. This is mutual antagonism, not conversion: each side actively kicks out the other's determinants. The mechanism creates a sharp, self-reinforcing boundary because each domain's machinery is continuously working to prevent the other from encroaching. Describing this as attraction or conversion fundamentally misrepresents how the polarity boundary is established and maintained."

- question: "How does the mutual antagonism between apical and basolateral polarity determinants create a self-reinforcing boundary, and why is this mechanism more robust than simple physical separation would be?"
  type: short-answer
  answer: "Mutual antagonism creates positive feedback: apical determinants (aPKC) phosphorylate and exclude basolateral determinants (Par1, Lgl), while basolateral determinants (Par1) phosphorylate and exclude apical determinants (Par3). Each domain's machinery actively maintains its own identity while attacking the other. This creates a bistable system — the boundary is sharp because any encroachment by one side triggers increased exclusion by the other. Physical separation alone (like a static fence) is passive and fragile; a membrane protein that diffuses across a physical barrier is not removed. Mutual antagonism is dynamic: even if a basolateral protein transiently reaches the apical zone, the aPKC present there phosphorylates and expels it, restoring the boundary without outside intervention."
  explanation: "The mutual antagonism model explains why polarity is so stable once established and why disrupting even one component can collapse it globally. It also explains why cell polarity requires continuous active maintenance — it is not a structure that persists passively, but a dynamic equilibrium maintained by competing molecular processes. This principle appears in many other biological contexts: bistable gene regulatory networks, cell fate decisions, and developmental patterning all use similar mutual exclusion logic to create sharp, stable boundaries."
```

## Explainer

From your understanding of plasma membrane organization, you know that the membrane is a dynamic mosaic of lipids and proteins that can be laterally organized into distinct regions. **Cell polarity** takes this concept to its functional extreme: an epithelial cell doesn't just have a membrane — it has *two fundamentally different* membrane domains, each with its own lipid composition, protein repertoire, and functional identity. The **apical** surface faces the lumen (the inside of a tube, like your intestine), while the **basolateral** surface contacts neighboring cells and the underlying tissue. These two domains are as different from each other as two different cell types might be.

The establishment of polarity begins with a conserved set of proteins called the **PAR complex** (Par3, Par6, and atypical protein kinase C, or aPKC). Think of the PAR system as a molecular "this end up" label. Par3/Par6/aPKC accumulate at what will become the apical domain and actively exclude basolateral-specifying proteins (like Par1 and Lgl) through phosphorylation — Par1, when phosphorylated by aPKC, is kicked out of the apical zone and confined to the basolateral domain. Reciprocally, Par1 phosphorylates Par3 to exclude it from the basolateral side. This mutual antagonism creates a sharp, self-reinforcing boundary between the two domains, much like two rival gangs enforcing territory lines.

**Tight junctions** serve as the physical fence that maintains this separation. Located at the boundary between apical and basolateral domains, tight junctions are composed of transmembrane proteins (claudins, occludin, and JAMs) that stitch adjacent cells together so tightly that even small molecules cannot pass between them. This **paracellular barrier** forces substances to cross the epithelium *through* the cells (transcellularly), giving the epithelium control over what passes. Equally important, tight junctions act as a **membrane fence** that prevents apical membrane proteins from drifting into the basolateral domain and vice versa — without this fence, the two domains would mix and polarity would collapse.

Maintaining polarity also requires **polarized vesicle trafficking**. The cell's secretory pathway sorts newly synthesized proteins into different vesicle populations destined for either the apical or basolateral surface. Motor proteins carry these vesicles along cytoskeletal tracks to the correct domain. When polarity breaks down — through disruption of PAR signaling, loss of tight junctions, or trafficking defects — epithelial cells lose their organized architecture. This is a hallmark of **epithelial-to-mesenchymal transition (EMT)**, a process central to both embryonic development and cancer metastasis. Cancer cells that lose polarity can detach from their tissue, invade surrounding structures, and spread to distant sites, which is why understanding polarity is not just a cell biology exercise but a window into disease mechanisms.
