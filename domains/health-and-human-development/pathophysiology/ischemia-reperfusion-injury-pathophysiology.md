---
id: ischemia-reperfusion-injury-pathophysiology
title: Ischemia and Reperfusion Injury Pathophysiology
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: cell-injury-and-adaptation
  type: hard
- id: necrosis-vs-apoptosis
  type: soft
- id: atp-energy-currency-synthesis
  type: soft
- id: reactive-oxygen-metabolism
  type: soft
builds-toward:
- myocardial-infarction-pathophysiology
- stroke-pathophysiology
tags:
- ischemia
- reperfusion
- oxidative-stress
- calcium-overload
- inflammation
stage: advanced
status: draft
---

# Ischemia and Reperfusion Injury Pathophysiology

## Core Idea
Ischemia deprives tissues of oxygen, forcing reliance on anaerobic glycolysis, ATP depletion, loss of ion gradient maintenance, and cellular swelling (cytotoxic edema). Reperfusion restores oxygen but paradoxically causes additional injury through reactive oxygen species (ROS) generation by mitochondria and NADPH oxidase, calcium overload-induced cardiomyocyte dysfunction, and activation of resident macrophages releasing inflammatory mediators. The tissue damage from reperfusion can exceed ischemic damage alone, particularly in short ischemia times.

## How It's Best Learned
Study the temporal sequence of changes during ischemia (ATP depletion, sodium accumulation, cell swelling) and reperfusion (ROS burst, calcium influx, inflammation). Understand ischemic preconditioning as an adaptive response. Consider therapeutic targets (antioxidants, calcium blockers, reperfusion protocols).

## Common Misconceptions
Longer ischemia time always causes worse outcome—actually, sudden reperfusion after brief ischemia causes disproportionate injury due to ROS generation. Ischemic preconditioning appears paradoxical but reflects upregulation of cellular protective mechanisms.

## Explainer

You already understand from your cell injury prerequisite that cells have a hierarchy of vulnerability: when ATP falls, ion pumps fail, and cells swell. You also know that not all cellular damage leads to death — cells can reverse injury if the insult is removed in time. Ischemia-reperfusion injury challenges this intuition: restoring blood flow after ischemia often makes things worse, not better. This paradox — that the cure can extend the disease — is one of the most clinically important concepts in pathophysiology.

During **ischemia**, the sequence is predictable. ATP depletion begins within seconds of flow interruption. Na⁺/K⁺-ATPase stops working, and sodium floods into the cell. To compensate, the Na⁺/H⁺ exchanger exports protons (formed from anaerobic glycolysis), which drives more sodium in. Calcium follows through the Na⁺/Ca²⁺ exchanger, accumulating in the cytoplasm and mitochondria. Cells swell (cytotoxic edema), mitochondria depolarize, and if ischemia persists long enough, the cell commits to necrosis. Cardiomyocytes and neurons — the cells most dependent on continuous aerobic metabolism — begin dying within minutes.

Reperfusion arrives with oxygen, but that oxygen is handed to a cell in crisis. Mitochondria that have accumulated calcium and been partially depolarized suddenly receive electron donors again, but the electron transport chain runs chaotically: a **reactive oxygen species (ROS) burst** erupts faster than the cell's antioxidant defenses can neutralize it. The ROS damage membrane lipids, proteins, and DNA. Simultaneously, pH normalizes — which was actually protective during ischemia, because low pH inhibited the **mitochondrial permeability transition pore (mPTP)**. As pH rises at reperfusion, the mPTP opens, collapsing the mitochondrial membrane potential and releasing cytochrome c, which triggers apoptosis. Cells that survived ischemia die during reperfusion.

The final layer is inflammation. Reperfusion activates resident macrophages, which release TNF-α, IL-1β, and other cytokines that recruit circulating neutrophils. These neutrophils squeeze through the endothelium and release their own oxidant burst, amplifying injury well beyond the originally ischemic core. **Ischemic preconditioning** — brief, repetitive ischemic episodes before a sustained ischemic insult — counterintuitively reduces total injury by upregulating protective pathways (heat shock proteins, antioxidant enzymes, survival kinases). This protective phenomenon has driven decades of research into pharmacological preconditioning mimetics that might be given before planned ischemic events like cardiac surgery, where the problem of reperfusion injury is both predictable and clinically significant.
