---
id: metabolic-hormones-and-gluconeogenesis
title: Metabolic Hormones and Their Regulatory Targets
domain: biology
course: biochemistry
prerequisites:
- id: metabolic-integration-hormonal-regulation
  type: hard
- id: hormone-signaling-mechanisms
  type: soft
builds-toward:
- fed-state-metabolism
- fasted-state-metabolism
tags:
- insulin
- glucagon
- epinephrine
- cortisol
stage: advanced
status: draft
---

# Metabolic Hormones and Their Regulatory Targets

## Core Idea
Insulin (fed state) promotes glucose uptake, glycolysis, fatty acid synthesis, and protein synthesis while inhibiting gluconeogenesis and lipolysis. Glucagon and epinephrine (fasted state) promote glycogenolysis and gluconeogenesis. Cortisol (stress) promotes proteolysis and gluconeogenesis. Each hormone acts on specific tissues via kinase cascades to alter enzyme phosphorylation state and gene expression.

## Questions

```yaml
- question: "Blood glucose drops during a prolonged fast and glucagon is released. What is the primary molecular sequence by which glucagon stimulates hepatic glucose output?"
  type: multiple-choice
  options:
    - "Glucagon binds receptor tyrosine kinases and activates PI3K/Akt signaling to promote GLUT2 expression"
    - "Glucagon directly activates glycogen phosphorylase by allosteric binding in the cytoplasm"
    - "Glucagon binds GPCRs on hepatocytes, activating adenylyl cyclase → cAMP → PKA, which phosphorylates and activates glycogen phosphorylase"
    - "Glucagon crosses the hepatocyte membrane and binds nuclear receptors to immediately upregulate gluconeogenic enzyme genes"
  answer: 2
  explanation: "Glucagon signals through G-protein-coupled receptors (GPCRs) on hepatocyte surfaces, activating adenylyl cyclase to produce cAMP, which activates protein kinase A (PKA). PKA then phosphorylates metabolic enzymes: glycogen phosphorylase kinase is activated (ultimately activating glycogen phosphorylase to break down glycogen), while glycogen synthase is simultaneously inhibited. This cAMP-PKA cascade produces rapid glucose mobilization — acting in minutes. Option D describes cortisol's mechanism (steroid hormone → nuclear receptor → gene expression), which operates on a much longer timescale. Option A describes insulin's signaling pathway, the opposite of glucagon."

- question: "Which statement correctly describes insulin's metabolic effects?"
  type: multiple-choice
  options:
    - "Insulin promotes glycogenolysis and lipolysis while suppressing fatty acid synthesis"
    - "Insulin activates cAMP-PKA signaling in muscle and adipose to mobilize stored fuel"
    - "Insulin promotes GLUT4 translocation to cell surfaces, glycogen and fatty acid synthesis, and suppresses gluconeogenesis and lipolysis"
    - "Insulin primarily acts on the liver to upregulate gluconeogenic enzymes like PEPCK and glucose-6-phosphatase"
  answer: 2
  explanation: "Insulin is the hormone of the fed (anabolic) state. It acts through receptor tyrosine kinases and the PI3K/Akt pathway to achieve three coordinated effects: (1) GLUT4 translocation to cell surfaces in muscle and adipose, increasing glucose uptake; (2) activation of anabolic pathways — glycolysis, glycogen synthesis, fatty acid synthesis, protein synthesis; and (3) suppression of catabolic pathways — gluconeogenesis, glycogenolysis, and lipolysis. Options A and B describe glucagon/epinephrine effects. Option D describes what cortisol and glucagon promote — insulin does the opposite, suppressing gluconeogenic enzymes."

- question: "Epinephrine and glucagon both activate protein kinase A via cAMP signaling, but epinephrine's metabolic effects are broader because it acts on liver, muscle, and adipose tissue while glucagon primarily targets the liver."
  type: true-false
  answer: true
  explanation: "Both hormones use the same intracellular mechanism — GPCR → adenylyl cyclase → cAMP → PKA — but tissue distribution of their receptors differs. Glucagon receptors are highly expressed in hepatocytes and to a lesser extent in adipose. Epinephrine receptors (β-adrenergic) are expressed broadly: in liver (promoting glycogenolysis and gluconeogenesis), muscle (promoting glycogenolysis for local ATP, importantly without releasing glucose since muscle lacks glucose-6-phosphatase), and adipose (activating hormone-sensitive lipase to release fatty acids). This broader reach makes epinephrine the hormone of the acute fight-or-flight response, while glucagon maintains basal glucose homeostasis during fasting."

- question: "Cortisol rapidly raises blood glucose within minutes of release by activating existing glycogen phosphorylase through phosphorylation."
  type: true-false
  answer: false
  explanation: "Cortisol is a steroid hormone that crosses cell membranes and binds intracellular glucocorticoid receptors. These receptor-hormone complexes then act as transcription factors, altering gene expression — a process that takes hours, not minutes. Cortisol's effects include upregulating gluconeogenic enzyme genes (PEPCK, glucose-6-phosphatase), promoting muscle proteolysis to supply amino acid substrates, and suppressing GLUT4 expression in peripheral tissues. Rapid glucose mobilization within seconds to minutes is epinephrine's role via the pre-existing cAMP-PKA cascade. Cortisol provides sustained gluconeogenic support during prolonged stress or starvation."

- question: "Explain why PKA phosphorylation simultaneously activates glycogenolysis and inhibits glycogen synthesis. What does this reveal about how hormones coordinate opposing metabolic pathways?"
  type: short-answer
  answer: "PKA phosphorylates glycogen phosphorylase kinase (activating it, which in turn activates glycogen phosphorylase → glycogen breakdown) and simultaneously phosphorylates glycogen synthase (inactivating it → glycogen synthesis stops). These enzymes are regulated in opposite directions by the same phosphorylation signal because they catalyze opposing reactions — allowing the same cAMP pulse to coherently switch the liver from glycogen storage mode to glycogen release mode without futile cycling. This reveals a general principle: hormonal control often works by phosphorylating enzyme pairs that catalyze opposing reactions in opposite directions, ensuring coordinated metabolic switching rather than simultaneous activation of competing pathways."
  explanation: "This coordinated co-regulation is not coincidental — it is the molecular basis of metabolic switching. If glycogen phosphorylase were activated without inhibiting glycogen synthase, the cell would simultaneously break down and rebuild glycogen, wasting ATP. The design of the PKA cascade ensures that one hormone signal flips the entire pathway in one direction. The same principle applies to fatty acid metabolism: PKA activates hormone-sensitive lipase (releasing fatty acids) and inhibits acetyl-CoA carboxylase (blocking fatty acid synthesis), achieving a coherent shift to fat mobilization."
```

## Explainer

From your study of metabolic integration and hormonal regulation, you understand that the body coordinates metabolism across tissues rather than letting each cell act independently. The hormones insulin, glucagon, epinephrine, and cortisol are the primary messengers that enforce this coordination, and their logic follows a simple principle: **match fuel availability to fuel demand**. When food is abundant, store it. When food is scarce, mobilize stored fuel and manufacture glucose.

**Insulin** is the hormone of the fed state. After a meal, rising blood glucose triggers pancreatic β-cells to secrete insulin. Insulin binds receptor tyrosine kinases on target cells and activates downstream signaling cascades (PI3K/Akt pathway) that produce three major effects: it stimulates glucose uptake in muscle and adipose tissue by promoting GLUT4 transporter translocation to the cell surface; it activates anabolic pathways like glycolysis, glycogen synthesis, fatty acid synthesis, and protein synthesis; and it suppresses catabolic pathways like gluconeogenesis, glycogenolysis, and lipolysis. The net result is that excess nutrients are stored as glycogen and fat, and blood glucose returns to baseline.

**Glucagon** is insulin's metabolic mirror. Secreted by pancreatic α-cells when blood glucose falls, glucagon binds G-protein-coupled receptors primarily on hepatocytes and activates **adenylyl cyclase → cAMP → protein kinase A (PKA)**. PKA phosphorylates key metabolic enzymes, flipping their activity states: glycogen phosphorylase is activated (promoting glycogenolysis), glycogen synthase is inhibited, and the transcription factor CREB is activated to upregulate gluconeogenic enzymes like PEPCK and glucose-6-phosphatase. **Epinephrine** uses a similar cAMP-PKA mechanism but acts more broadly — on liver, muscle, and adipose tissue — to rapidly mobilize fuel during the fight-or-flight response. In adipose tissue, PKA activates hormone-sensitive lipase, releasing fatty acids as an alternative fuel source.

**Cortisol**, the stress hormone released from the adrenal cortex, operates on a longer timescale. As a steroid hormone, it crosses the cell membrane and binds intracellular receptors that act as transcription factors, altering gene expression over hours. Cortisol promotes proteolysis in muscle, freeing amino acids as gluconeogenic substrates, and upregulates gluconeogenic enzymes in the liver. It also suppresses glucose uptake in peripheral tissues, ensuring that newly synthesized glucose is preserved for the brain. The interplay of these hormones creates a robust system: insulin dominates after meals, glucagon and epinephrine dominate during fasting and stress, and cortisol provides sustained gluconeogenic support during prolonged deprivation. Understanding these opposing signals and their molecular mechanisms is essential for grasping metabolic diseases like diabetes, where insulin signaling is defective and the counter-regulatory hormones operate without adequate opposition.
