---
id: phospholipid-biosynthesis
title: Phospholipid Biosynthesis
domain: biology
course: biochemistry
prerequisites:
- id: fatty-acid-synthesis
  type: hard
- id: cell-membrane-structure
  type: soft
builds-toward:
- membrane-protein-biogenesis
tags:
- phospholipids
- lipid-biosynthesis
- membrane-components
stage: advanced
status: draft
---

# Phospholipid Biosynthesis

## Core Idea
Phospholipids are synthesized via the Kennedy pathway: glycerol-3-phosphate is acylated to form phosphatidic acid, then dephosphorylated to diacylglycerol (DAG). DAG is used to synthesize phosphatidylcholine and phosphatidylethanolamine. Remodeling enzymes alter fatty acid composition post-synthesis, generating diverse molecular species.

## Questions

```yaml
- question: "A researcher uses a drug that specifically blocks the phosphatase enzyme converting phosphatidic acid (PA) to diacylglycerol (DAG). Which prediction is MOST accurate about the effect on phospholipid synthesis?"
  type: multiple-choice
  options:
    - "All phospholipid synthesis halts immediately because DAG is required for all phospholipid classes"
    - "Synthesis of phosphatidylcholine and phosphatidylethanolamine is impaired, but phosphatidylinositol and cardiolipin may continue via the CDP-diacylglycerol branch from PA"
    - "Only the fatty acid composition of membrane phospholipids is affected; head group attachment continues normally"
    - "Cholesterol synthesis increases to compensate for the reduced phospholipid content in membranes"
  answer: 1
  explanation: "Phosphatidic acid (PA) is the branch point in the Kennedy pathway. It can either be dephosphorylated to DAG (leading to phosphatidylcholine and phosphatidylethanolamine) or converted to CDP-diacylglycerol (leading to phosphatidylserine, phosphatidylinositol, and cardiolipin). Blocking the PA→DAG step impairs the first branch but not the second. Option A is wrong because PA itself feeds the second branch directly."

- question: "Why is CTP (cytidine triphosphate) required for phospholipid head group attachment in the Kennedy pathway?"
  type: multiple-choice
  options:
    - "CTP directly phosphorylates the glycerol backbone to create phosphatidic acid from glycerol-3-phosphate"
    - "CTP activates the head group (e.g., choline) by forming a high-energy CDP-choline intermediate, making the subsequent transfer to DAG thermodynamically favorable"
    - "CTP removes the sn-2 fatty acid from phosphatidic acid during the Lands cycle remodeling step"
    - "CTP is the primary carbon donor for extending fatty acid chains that are incorporated into the phospholipid backbone"
  answer: 1
  explanation: "The Kennedy pathway uses the same biochemical strategy as other biosynthetic pathways: activation by a nucleotide triphosphate drives an otherwise unfavorable condensation reaction. Choline is first phosphorylated (to phosphocholine), then activated with CTP to form CDP-choline — a high-energy intermediate. This activation makes the transfer of the choline head group to DAG thermodynamically favorable, releasing CMP. This is analogous to UTP activating glucose in glycogen synthesis."

- question: "The Lands cycle allows cells to modify the fatty acid composition of membrane phospholipids after initial synthesis by exchanging the fatty acid at the sn-2 position."
  type: true-false
  answer: true
  explanation: "The Lands cycle is a phospholipid remodeling system: phospholipase A₂ removes the fatty acid at the sn-2 position, and a lysophospholipid acyltransferase installs a different one. This post-synthetic remodeling is how cells generate the enormous diversity of phospholipid molecular species (hundreds of combinations of head groups, chain lengths, and saturation levels) from a relatively simple synthetic pathway, enabling precise tuning of membrane fluidity and curvature."

- question: "Once a phospholipid is assembled via the Kennedy pathway, its fatty acid composition is permanently fixed and cannot be changed without degrading and resynthesizing the entire molecule."
  type: true-false
  answer: false
  explanation: "This is incorrect. The Lands cycle specifically provides a mechanism for remodeling phospholipid fatty acid composition without resynthesis. Phospholipase A₂ cleaves the sn-2 fatty acid, and acyltransferases install a replacement. This is how cells fine-tune membrane properties — adjusting fluidity, curvature, and signaling capacity — in response to changing needs. The Kennedy pathway synthesizes the structural scaffold; the Lands cycle customizes the content."

- question: "What is the role of phosphatidic acid (PA) in the Kennedy pathway, and why is its position at the branch point important for understanding how cells produce diverse phospholipid classes?"
  type: short-answer
  answer: "Phosphatidic acid is the common precursor formed after two fatty acid chains are attached to the glycerol-3-phosphate backbone. Its position at the branch point is critical because it is converted by two different enzymes into two different products: dephosphorylation yields diacylglycerol (DAG), which feeds synthesis of phosphatidylcholine and phosphatidylethanolamine; conversion by CTP yields CDP-diacylglycerol, which feeds synthesis of phosphatidylserine, phosphatidylinositol, and cardiolipin. This single branch point allows one common synthetic route to diverge into all major phospholipid classes, with the relative flux through each branch determining the membrane's lipid composition."
  explanation: "Understanding PA as a branch point explains how mutations or drugs affecting specific enzymes at or after this point selectively impair some phospholipid classes but not others — a conceptually important feature of membrane biochemistry that cannot be inferred from knowing the pathway as a linear sequence."
```

## Explainer

You already understand how fatty acids are synthesized — long hydrocarbon chains built two carbons at a time by fatty acid synthase. And you know from cell membrane structure that phospholipids are the primary building blocks of biological membranes, with their characteristic two fatty acid tails and a polar head group. The question now is: how does the cell actually assemble these components into a finished phospholipid? The answer is the **Kennedy pathway**, named after Eugene Kennedy, who worked it out in the 1950s.

The pathway begins with **glycerol-3-phosphate**, which provides the backbone. This molecule is derived either from the glycolysis intermediate dihydroxyacetone phosphate (DHAP) or directly from glycerol via glycerol kinase. Two successive acylation reactions attach fatty acid chains — first at the sn-1 position, then at the sn-2 position — creating **phosphatidic acid** (PA). The fatty acids are donated as their activated CoA derivatives (the same acyl-CoA molecules you encountered in fatty acid metabolism). Typically, a saturated fatty acid goes to sn-1 and an unsaturated one to sn-2, though this is not absolute. Phosphatidic acid is the branch point: it can be dephosphorylated to **diacylglycerol (DAG)** or converted to CDP-diacylglycerol, each leading to different phospholipid classes.

The DAG branch produces the two most abundant membrane phospholipids. To make **phosphatidylcholine** (PC), the choline head group is first activated with CTP to form CDP-choline, then transferred to DAG. **Phosphatidylethanolamine** (PE) is made by the same logic using CDP-ethanolamine. The CDP-diacylglycerol branch instead produces phosphatidylserine, phosphatidylinositol, and cardiolipin — less abundant but functionally critical lipids. Notice the recurring biochemical strategy: activation with a nucleotide (CTP in this case) to make head-group attachment thermodynamically favorable, much like UTP activates glucose for glycogen synthesis.

Once assembled, phospholipids are not static. **Remodeling enzymes** (the Lands cycle) swap out fatty acid chains at the sn-2 position, allowing the cell to fine-tune membrane properties after initial synthesis. A phospholipase A₂ removes the sn-2 fatty acid, and an acyltransferase installs a different one. This is how cells generate the enormous diversity of phospholipid molecular species found in real membranes — hundreds of combinations of head groups and fatty acid chain lengths and saturation levels — from a relatively simple biosynthetic pathway. The result is a membrane whose fluidity, curvature, and signaling capacity can be precisely adjusted to meet cellular needs.
