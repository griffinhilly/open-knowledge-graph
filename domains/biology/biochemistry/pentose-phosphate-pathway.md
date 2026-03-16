---
id: pentose-phosphate-pathway
title: Pentose Phosphate Pathway
domain: biology
course: biochemistry
prerequisites:
- id: glycolysis-mechanism-and-regulation
  type: hard
builds-toward:
- nucleotide-synthesis
- fatty-acid-synthesis
tags:
- pentose phosphate pathway
- NADPH
- ribose
- oxidative phase
- reductive phase
stage: advanced
status: draft
---

# Pentose Phosphate Pathway

## Core Idea
The pentose phosphate pathway (hexose monophosphate shunt) is an alternative route for glucose metabolism that generates NADPH (for biosynthesis and antioxidant defense) and ribose-5-phosphate (for nucleotide synthesis). The pathway has an oxidative phase producing NADPH and a reductive phase (non-oxidative) that reversibly converts glucose-6-phosphate into three-, four-, five-, six-, and seven-carbon sugars. The pathway is regulated by NADPH availability and the cell's biosynthetic needs rather than by energy status.

## Explainer

You already know glycolysis as the cell's primary route for glucose breakdown, generating pyruvate, ATP, and NADH. But cells have needs that glycolysis cannot meet. They need **NADPH** — the reduced coenzyme that powers biosynthetic reactions like fatty acid synthesis and provides the reducing equivalents for antioxidant defense via glutathione. They also need **ribose-5-phosphate** — the five-carbon sugar backbone of every nucleotide in DNA and RNA. The pentose phosphate pathway exists to supply both of these products, and it branches off from glycolysis at the very first step: glucose-6-phosphate.

The pathway has two distinct phases. The **oxidative phase** is irreversible and produces NADPH. Glucose-6-phosphate is oxidized by **glucose-6-phosphate dehydrogenase** (G6PD), the committed and rate-limiting enzyme, generating 6-phosphoglucono-δ-lactone and one molecule of NADPH. After hydrolysis and a second oxidative decarboxylation step, the six-carbon sugar is converted to the five-carbon **ribulose-5-phosphate**, producing a second NADPH and releasing one CO₂. So for every glucose-6-phosphate that enters the oxidative phase, the cell gains two NADPH molecules and one pentose phosphate.

The **non-oxidative phase** is reversible and reshuffles carbon skeletons. Using **transketolase** (which transfers two-carbon units) and **transaldolase** (which transfers three-carbon units), the pathway interconverts three-, four-, five-, six-, and seven-carbon sugar phosphates. This flexibility is crucial because it allows the cell to match its output to its needs. If the cell needs more NADPH than ribose, the non-oxidative phase recycles pentose phosphates back into glycolytic intermediates (fructose-6-phosphate and glyceraldehyde-3-phosphate), which re-enter glycolysis or are converted back to glucose-6-phosphate to run through the oxidative phase again. If the cell needs ribose for nucleotide synthesis (as in rapidly dividing cells), the non-oxidative phase can generate ribose-5-phosphate from glycolytic intermediates without producing NADPH.

Regulation centers on **NADPH availability**. When the NADPH/NADP⁺ ratio is high, the oxidative phase slows because G6PD is inhibited by NADPH. When biosynthetic demand or oxidative stress consumes NADPH, the ratio drops, NADP⁺ rises, and the pathway accelerates. This is fundamentally different from glycolytic regulation, which responds to energy charge (ATP/AMP ratio). The clinical importance of this pathway is vividly illustrated by **G6PD deficiency**, the most common enzyme deficiency in humans. Without adequate G6PD activity, red blood cells cannot generate enough NADPH to maintain reduced glutathione, leaving them vulnerable to oxidative damage and hemolytic anemia when exposed to oxidant drugs or fava beans.
