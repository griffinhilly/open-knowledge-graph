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

## Explainer

You already understand how fatty acids are synthesized — long hydrocarbon chains built two carbons at a time by fatty acid synthase. And you know from cell membrane structure that phospholipids are the primary building blocks of biological membranes, with their characteristic two fatty acid tails and a polar head group. The question now is: how does the cell actually assemble these components into a finished phospholipid? The answer is the **Kennedy pathway**, named after Eugene Kennedy, who worked it out in the 1950s.

The pathway begins with **glycerol-3-phosphate**, which provides the backbone. This molecule is derived either from the glycolysis intermediate dihydroxyacetone phosphate (DHAP) or directly from glycerol via glycerol kinase. Two successive acylation reactions attach fatty acid chains — first at the sn-1 position, then at the sn-2 position — creating **phosphatidic acid** (PA). The fatty acids are donated as their activated CoA derivatives (the same acyl-CoA molecules you encountered in fatty acid metabolism). Typically, a saturated fatty acid goes to sn-1 and an unsaturated one to sn-2, though this is not absolute. Phosphatidic acid is the branch point: it can be dephosphorylated to **diacylglycerol (DAG)** or converted to CDP-diacylglycerol, each leading to different phospholipid classes.

The DAG branch produces the two most abundant membrane phospholipids. To make **phosphatidylcholine** (PC), the choline head group is first activated with CTP to form CDP-choline, then transferred to DAG. **Phosphatidylethanolamine** (PE) is made by the same logic using CDP-ethanolamine. The CDP-diacylglycerol branch instead produces phosphatidylserine, phosphatidylinositol, and cardiolipin — less abundant but functionally critical lipids. Notice the recurring biochemical strategy: activation with a nucleotide (CTP in this case) to make head-group attachment thermodynamically favorable, much like UTP activates glucose for glycogen synthesis.

Once assembled, phospholipids are not static. **Remodeling enzymes** (the Lands cycle) swap out fatty acid chains at the sn-2 position, allowing the cell to fine-tune membrane properties after initial synthesis. A phospholipase A₂ removes the sn-2 fatty acid, and an acyltransferase installs a different one. This is how cells generate the enormous diversity of phospholipid molecular species found in real membranes — hundreds of combinations of head groups and fatty acid chain lengths and saturation levels — from a relatively simple biosynthetic pathway. The result is a membrane whose fluidity, curvature, and signaling capacity can be precisely adjusted to meet cellular needs.
