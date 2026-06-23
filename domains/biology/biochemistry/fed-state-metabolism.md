---
id: fed-state-metabolism
title: Fed State Metabolism
domain: biology
course: biochemistry
prerequisites:
- id: metabolic-hormones-and-gluconeogenesis
  type: hard
- id: carbohydrate-homeostasis
  type: soft
- id: insulin-glucagon-glucose-homeostasis
  type: soft
tags:
- fed-state
- insulin
- anabolism
stage: formal-systems
status: validated
---

# Fed State Metabolism

## Core Idea
In the fed state (high insulin), glucose is oxidized for energy and used for glycogen and fatty acid synthesis. Dietary amino acids are incorporated into proteins or degraded. Lipids are esterified and stored as triglycerides. The liver synthesizes VLDLs to export fatty acids. Blood glucose is tightly controlled by insulin-stimulated glucose uptake and suppression of gluconeogenesis.

## Questions

```yaml
- question: "After a carbohydrate-rich meal, the liver has more acetyl-CoA than it can immediately oxidize in the citric acid cycle. What happens to the excess, and why?"
  type: multiple-choice
  options:
    - "It is exported to muscle as acetyl-CoA for direct oxidation, since the liver cannot store fat"
    - "It is converted to ketone bodies to supply the brain during the fed state"
    - "It is channeled into de novo lipogenesis because the cell's energy charge is high and the citric acid cycle slows when ATP is abundant"
    - "It is transaminated into amino acids to replenish depleted protein stores"
  answer: 2
  explanation: "In the fed state, the cell's ATP is plentiful, so the citric acid cycle slows (high energy charge inhibits key enzymes). Excess acetyl-CoA cannot simply pile up, so it is redirected into de novo fatty acid synthesis — a biosynthetic pathway that consumes NADPH and runs precisely when there is more fuel than the oxidative pathways can handle. Ketone body production (option B) is a fasted-state response to low glucose; it is suppressed by insulin in the fed state."

- question: "Dietary fat packaged as chylomicrons is released by lipoprotein lipase at adipose capillaries. What happens to the freed fatty acids?"
  type: multiple-choice
  options:
    - "They are converted to glucose via gluconeogenesis to maintain blood sugar"
    - "They are taken up by adipose cells and re-esterified into triglycerides for storage"
    - "They remain in the bloodstream as free fatty acids until needed by muscle"
    - "They are transported to the liver for immediate beta-oxidation"
  answer: 1
  explanation: "In the fed state, insulin suppresses hormone-sensitive lipase (preventing fat breakdown) and promotes re-esterification of fatty acids into triglycerides inside adipocytes. The net result is fat storage: dietary lipids flow from chylomicrons → free fatty acids → triglycerides in adipose. Beta-oxidation (option D) is a fasted-state pathway; gluconeogenesis from fatty acids (option A) is not possible because acetyl-CoA cannot be converted back to pyruvate in animals."

- question: "In the fed state, insulin suppresses hormone-sensitive lipase in adipose tissue, ensuring that stored triglycerides are not broken down while dietary nutrients are being absorbed."
  type: true-false
  answer: true
  explanation: "This is a central feature of the fed state's anabolic logic: it would be counterproductive to simultaneously store fat (from dietary lipids) and mobilize fat (via hormone-sensitive lipase). Insulin inhibits hormone-sensitive lipase directly, ensuring the net direction is unidirectionally into storage. In the fasted state, when insulin falls and glucagon rises, this inhibition is removed and lipolysis resumes."

- question: "In the fed state, dietary amino acids are primarily converted to glucose via gluconeogenesis to maintain blood glucose levels between meals."
  type: true-false
  answer: false
  explanation: "This reverses the priority: in the fed state, amino acids are primarily directed toward protein synthesis. Insulin activates the mTOR pathway, which is a potent stimulus for translation, and stimulates uptake of amino acids into muscle. Gluconeogenesis from amino acids is a fasted-state response that occurs when glucose is scarce. Excess amino acids beyond what protein synthesis requires are deaminated and their carbon skeletons enter the citric acid cycle or are converted to fat — but this is secondary to protein synthesis in the fed state."

- question: "Why is the liver's role in the fed state described as 'coordinating,' and what would happen to blood glucose levels if hepatic gluconeogenesis were not suppressed by insulin after a meal?"
  type: short-answer
  answer: "The liver coordinates the fed state because it is the central clearinghouse for absorbed nutrients arriving via the portal vein: it takes up glucose (phosphorylating it with glucokinase), synthesizes glycogen and fatty acids, produces VLDL to export lipids, and processes amino acids. If insulin did not suppress hepatic gluconeogenesis after a meal, the liver would continue producing new glucose from amino acids and glycerol even as dietary glucose was pouring in from the intestine, causing blood glucose to rise to hyperglycemic levels. Insulin's suppression of gluconeogenesis (and glycogenolysis) is essential to the homeostatic control of postprandial blood glucose."
  explanation: "This question highlights why the liver requires insulin signaling specifically — the liver normally produces glucose to supply other organs in the fasted state, and this production must be actively turned off after a meal. Type 2 diabetics often have hepatic insulin resistance, meaning the liver fails to suppress gluconeogenesis even in the fed state, contributing to chronic postprandial hyperglycemia. This is why metformin (which inhibits hepatic gluconeogenesis) is a first-line treatment."
```

## Explainer

From your study of metabolic hormones and gluconeogenesis, you know that insulin and glucagon act as opposing signals that coordinate fuel use across tissues. The **fed state** is the metabolic condition that prevails when insulin is high — typically for several hours after a meal — and it is fundamentally an anabolic state: the body stores fuel rather than mobilizing it. Understanding what happens in this window means tracking how the three major macronutrients (carbohydrates, fats, and amino acids) are routed through the liver, muscle, and adipose tissue under insulin's direction.

When blood glucose rises after a meal, pancreatic β-cells secrete **insulin**, which does two things simultaneously: it stimulates glucose uptake into muscle and adipose tissue (via GLUT4 translocation to the cell surface) and it suppresses hepatic glucose output by inhibiting gluconeogenesis and glycogenolysis. In the liver, incoming glucose is phosphorylated by glucokinase and directed toward **glycogen synthesis** (replenishing liver glycogen stores) and **glycolysis** (generating acetyl-CoA). Excess acetyl-CoA that is not needed for energy is funneled into **de novo lipogenesis** — fatty acid synthesis — because the cell's energy charge is already high and the citric acid cycle slows when ATP is abundant.

Dietary amino acids absorbed from the gut are taken up by the liver and peripheral tissues. In the fed state, amino acids are primarily used for **protein synthesis**, since insulin is a potent anabolic signal that activates the mTOR pathway and stimulates translation. Amino acids in excess of what protein synthesis requires are deaminated; their carbon skeletons enter the citric acid cycle or are converted to glucose or fat. The nitrogen is disposed of via the urea cycle. Meanwhile, dietary lipids — packaged into chylomicrons by the intestine — are broken down by lipoprotein lipase in capillaries, and the released fatty acids are taken up by adipose tissue and re-esterified into **triglycerides** for storage.

The liver plays a unique coordinating role in the fed state. It synthesizes fatty acids from excess glucose, packages them into **VLDL** (very low-density lipoproteins), and exports them to peripheral tissues — primarily adipose tissue for storage. At the same time, insulin suppresses hormone-sensitive lipase in adipose tissue, preventing the breakdown of stored triglycerides. The net effect is a one-way flow: fuel moves from the bloodstream into storage depots. This entire pattern reverses in the fasted state, when glucagon rises and insulin falls, mobilizing glycogen, fat, and eventually protein to maintain blood glucose. The fed state is thus best understood as the storage phase of a continuous metabolic oscillation between feeding and fasting.
