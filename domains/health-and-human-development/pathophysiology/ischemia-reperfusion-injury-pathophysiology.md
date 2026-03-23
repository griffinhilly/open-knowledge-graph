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
stage: expert
status: draft
---

# Ischemia and Reperfusion Injury Pathophysiology

## Core Idea
Ischemia deprives tissues of oxygen, forcing reliance on anaerobic glycolysis, ATP depletion, loss of ion gradient maintenance, and cellular swelling (cytotoxic edema). Reperfusion restores oxygen but paradoxically causes additional injury through reactive oxygen species (ROS) generation by mitochondria and NADPH oxidase, calcium overload-induced cardiomyocyte dysfunction, and activation of resident macrophages releasing inflammatory mediators. The tissue damage from reperfusion can exceed ischemic damage alone, particularly in short ischemia times.

## How It's Best Learned
Study the temporal sequence of changes during ischemia (ATP depletion, sodium accumulation, cell swelling) and reperfusion (ROS burst, calcium influx, inflammation). Understand ischemic preconditioning as an adaptive response. Consider therapeutic targets (antioxidants, calcium blockers, reperfusion protocols).

## Common Misconceptions
Longer ischemia time always causes worse outcome—actually, sudden reperfusion after brief ischemia causes disproportionate injury due to ROS generation. Ischemic preconditioning appears paradoxical but reflects upregulation of cellular protective mechanisms.

## Questions

```yaml
- question: "A patient arrives in the emergency department 25 minutes after the onset of a myocardial infarction. The blocked coronary artery is successfully reopened. A medical student says 'restoring blood flow stops the injury — the outcome depends only on how much ischemia already occurred.' What is the most accurate correction?"
  type: multiple-choice
  options:
    - "The student is correct; reperfusion itself causes no further damage once flow is restored"
    - "Reperfusion causes additional injury through reactive oxygen species bursts, calcium overload, and inflammatory activation — potentially exceeding ischemic damage in brief ischemia cases"
    - "Reperfusion is harmful only if ischemia lasted longer than 60 minutes"
    - "The main reperfusion risk is re-occlusion of the artery, not a biochemical injury response"
  answer: 1
  explanation: "Reperfusion paradoxically triggers a second wave of injury. Mitochondria damaged by ischemia and calcium-loaded produce a burst of reactive oxygen species when oxygen returns. pH normalization — which was protective during ischemia because low pH inhibits the mitochondrial permeability transition pore (mPTP) — now causes the mPTP to open, collapsing mitochondrial membrane potential and triggering apoptosis. Resident macrophages activate, recruiting neutrophils that amplify oxidant injury. In cases of brief ischemia, this reperfusion injury can actually exceed the ischemic damage that occurred before flow was restored."

- question: "During ischemia, intracellular pH falls due to anaerobic glycolysis. Why does this low pH, counterintuitively, protect the cell during ischemia — and why does pH normalization at reperfusion cause harm?"
  type: multiple-choice
  options:
    - "Low pH stabilizes mitochondrial membranes by protonating cardiolipin; pH normalization dissolves this protection"
    - "Low pH inhibits the mitochondrial permeability transition pore (mPTP); pH normalization at reperfusion opens the pore, releasing cytochrome c and triggering apoptosis"
    - "Low pH activates lysosomal enzymes that degrade damaged proteins; pH normalization halts this protective autophagy"
    - "Low pH reduces calcium entry through voltage-gated channels; pH normalization reverses this block"
  answer: 1
  explanation: "The mPTP is a large pore in the inner mitochondrial membrane that, when open, collapses the mitochondrial membrane potential and releases pro-apoptotic factors like cytochrome c. During ischemia, the accumulation of protons (falling pH) holds the mPTP closed — a paradoxical protection against cell death. When reperfusion restores oxygen and pH normalizes, this inhibition is lost: the mPTP opens in a cell that is already calcium-loaded and oxidatively stressed, triggering apoptosis in cells that had survived the ischemic phase. This is why the timing and conditions of reperfusion matter, not just the fact of reperfusion."

- question: "Longer ischemia duration always results in greater total tissue damage than shorter ischemia with reperfusion."
  type: true-false
  answer: false
  explanation: "This is a key misconception. Brief ischemia followed by sudden reperfusion can cause disproportionately severe injury because reperfusion injury is substantial when cells are still viable enough to undergo the biochemical cascade (ROS burst, mPTP opening, inflammatory activation). In prolonged ischemia, cells may already be committed to necrosis before reperfusion occurs, so the reperfusion component is relatively less significant. The relationship between ischemia duration and total injury is nonlinear — there is an important period of 'reversible' ischemic injury where reperfusion causes maximum additional harm."

- question: "Ischemic preconditioning — brief, repetitive ischemic episodes before a sustained ischemic insult — reduces total tissue injury by upregulating cellular protective mechanisms such as heat shock proteins, antioxidant enzymes, and survival kinases."
  type: true-false
  answer: true
  explanation: "Ischemic preconditioning is a real and well-characterized protective phenomenon despite its apparent paradox. Brief, sublethal ischemic episodes activate intracellular signaling cascades that upregulate protective responses: heat shock proteins stabilize proteins under stress, antioxidant enzymes (superoxide dismutase, catalase) increase capacity to neutralize the ROS burst during reperfusion, and survival kinases (RISK pathway: PI3K/Akt and ERK) phosphorylate targets that inhibit the mPTP. The cell, having been warned by small insults, is better prepared for the larger one. This finding has driven research into pharmacological mimetics for use before planned ischemic events like cardiac surgery."

- question: "Explain why restoring blood flow to ischemic tissue paradoxically causes additional cellular damage beyond what ischemia alone would have produced."
  type: short-answer
  answer: "Reperfusion delivers oxygen to cells that are already in crisis — ATP-depleted, calcium-loaded, and with partially depolarized mitochondria. The electron transport chain, restarted with oxygen but running chaotically, generates a massive reactive oxygen species burst faster than cellular antioxidants can neutralize. Simultaneously, pH normalization (acidosis was protective by inhibiting the mPTP) causes the mitochondrial permeability transition pore to open, collapsing mitochondrial membrane potential and releasing cytochrome c, triggering apoptosis in cells that survived ischemia. Reperfusion also activates resident macrophages and recruits neutrophils, which amplify oxidant injury via their own oxidative burst."
  explanation: "The paradox of reperfusion injury reveals that oxygen, normally essential for life, is harmful when delivered to cells whose protective machinery has been compromised by ischemia. The same metabolic machinery that generates energy under normal conditions generates toxic oxidants under the disordered conditions of reperfusion. Understanding this has led to therapeutic strategies targeting the ROS burst, the mPTP, and the inflammatory cascade — potentially administered just before reperfusion to limit this 'second hit.'"
```

## Explainer

You already understand from your cell injury prerequisite that cells have a hierarchy of vulnerability: when ATP falls, ion pumps fail, and cells swell. You also know that not all cellular damage leads to death — cells can reverse injury if the insult is removed in time. Ischemia-reperfusion injury challenges this intuition: restoring blood flow after ischemia often makes things worse, not better. This paradox — that the cure can extend the disease — is one of the most clinically important concepts in pathophysiology.

During **ischemia**, the sequence is predictable. ATP depletion begins within seconds of flow interruption. Na⁺/K⁺-ATPase stops working, and sodium floods into the cell. To compensate, the Na⁺/H⁺ exchanger exports protons (formed from anaerobic glycolysis), which drives more sodium in. Calcium follows through the Na⁺/Ca²⁺ exchanger, accumulating in the cytoplasm and mitochondria. Cells swell (cytotoxic edema), mitochondria depolarize, and if ischemia persists long enough, the cell commits to necrosis. Cardiomyocytes and neurons — the cells most dependent on continuous aerobic metabolism — begin dying within minutes.

Reperfusion arrives with oxygen, but that oxygen is handed to a cell in crisis. Mitochondria that have accumulated calcium and been partially depolarized suddenly receive electron donors again, but the electron transport chain runs chaotically: a **reactive oxygen species (ROS) burst** erupts faster than the cell's antioxidant defenses can neutralize it. The ROS damage membrane lipids, proteins, and DNA. Simultaneously, pH normalizes — which was actually protective during ischemia, because low pH inhibited the **mitochondrial permeability transition pore (mPTP)**. As pH rises at reperfusion, the mPTP opens, collapsing the mitochondrial membrane potential and releasing cytochrome c, which triggers apoptosis. Cells that survived ischemia die during reperfusion.

The final layer is inflammation. Reperfusion activates resident macrophages, which release TNF-α, IL-1β, and other cytokines that recruit circulating neutrophils. These neutrophils squeeze through the endothelium and release their own oxidant burst, amplifying injury well beyond the originally ischemic core. **Ischemic preconditioning** — brief, repetitive ischemic episodes before a sustained ischemic insult — counterintuitively reduces total injury by upregulating protective pathways (heat shock proteins, antioxidant enzymes, survival kinases). This protective phenomenon has driven decades of research into pharmacological preconditioning mimetics that might be given before planned ischemic events like cardiac surgery, where the problem of reperfusion injury is both predictable and clinically significant.
