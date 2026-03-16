---
id: glycogen-metabolism
title: Glycogen Metabolism and Mobilization
domain: biology
course: biochemistry
prerequisites:
- id: disaccharides-and-polysaccharides
  type: hard
- id: glycolysis-mechanism-and-regulation
  type: soft
builds-toward:
- metabolic-integration-hormonal-regulation
tags:
- glycogen
- glycogenesis
- glycogenolysis
- muscle
- liver
- branching
stage: advanced
status: draft
---

# Glycogen Metabolism and Mobilization

## Core Idea
Glycogen is a branched homopolymer of glucose (α-1,4 and α-1,6 linkages) that serves as a mobile carbohydrate reserve in muscle and liver. Glycogenesis (synthesis) is catalyzed by glycogen synthase and occurs when glucose and energy are abundant. Glycogenolysis (breakdown) is catalyzed by phosphorylase and releases glucose-1-phosphate for glycolysis in muscle or glucose from glucose-6-phosphatase in liver. The branched structure of glycogen (with branches every 8-12 residues) enables rapid glucose mobilization from thousands of outer chains.

## Explainer

You already know that glucose is the cell's primary fuel and that polysaccharides store glucose in compact, polymeric form. Glycogen is the animal kingdom's solution to a specific problem: how do you store glucose so that it can be mobilized almost instantly when energy demand spikes? Starch works for plants — they don't sprint — but animals need a storage polymer that trades maximum density for maximum speed of release. Glycogen's extraordinary branching is the key to this tradeoff.

**Glycogenesis** (synthesis) begins with a protein primer called **glycogenin**, which attaches the first few glucose residues to itself. From there, **glycogen synthase** extends α-1,4-linked glucose chains using UDP-glucose as the activated donor — recall from your work on polysaccharides that UDP-glucose is the "charged" form of glucose used in biosynthesis. Once a chain reaches about 11 residues, **branching enzyme** clips off a block of roughly 7 residues and reattaches it via an α-1,6 linkage to create a new branch. This process repeats, building a tree-like structure with branches every 8–12 residues and up to 55,000 glucose units in a single granule. The critical insight is that each branch tip is a potential site for simultaneous degradation — more branches mean more enzymes can attack the molecule at once.

**Glycogenolysis** (breakdown) is not simply the reverse of synthesis — it uses different enzymes and different regulation. **Glycogen phosphorylase** cleaves α-1,4 bonds by phosphorolysis (using inorganic phosphate, not water), releasing **glucose-1-phosphate** directly. This is energetically clever: the product is already phosphorylated and ready to enter glycolysis without spending an ATP. Phosphorylase works inward from each branch tip but stalls four residues from any α-1,6 branch point. A **debranching enzyme** then transfers three of those residues to another chain and hydrolyzes the remaining α-1,6 bond, releasing one free glucose. Glucose-1-phosphate is converted to glucose-6-phosphate by phosphoglucomutase, at which point its fate diverges by tissue.

The tissue-specific logic is essential. In **muscle**, glucose-6-phosphate enters glycolysis directly — muscle cells lack glucose-6-phosphatase and therefore cannot export free glucose. Muscle glycogen is a private fuel reserve, consumed locally during contraction. In **liver**, glucose-6-phosphatase cleaves the phosphate group, producing free glucose that is exported into the blood to maintain blood sugar for the brain and other tissues. This is why liver glycogen depletion causes hypoglycemia while muscle glycogen depletion causes fatigue — they serve fundamentally different physiological roles despite using nearly identical biochemistry.

The synthesis and breakdown pathways are reciprocally regulated by hormones. Insulin promotes glycogenesis; glucagon (liver) and epinephrine (muscle) promote glycogenolysis through cAMP-dependent phosphorylation cascades that activate phosphorylase and inhibit synthase simultaneously. This reciprocal control ensures the cell never wastes energy synthesizing and degrading glycogen at the same time — a principle you will encounter repeatedly as you study metabolic integration.
