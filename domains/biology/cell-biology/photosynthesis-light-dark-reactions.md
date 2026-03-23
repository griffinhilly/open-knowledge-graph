---
id: photosynthesis-light-dark-reactions
title: 'Photosynthesis: Light and Dark Reactions'
domain: biology
course: cell-biology
prerequisites:
- id: photosynthesis-overview
  type: hard
- id: light-reactions
  type: hard
- id: calvin-cycle
  type: hard
- id: oxidation-reduction-reactions
  type: soft
- id: oxidation-reduction-basics
  type: soft
tags:
- photosynthesis
- light-reactions
- calvin-cycle
stage: formal-systems
status: draft
---

# Photosynthesis: Light and Dark Reactions

## Core Idea
Photosynthesis occurs in two stages: light reactions (thylakoid membrane) use photon energy to separate charge and generate ATP and NADPH; dark reactions (stroma) use this energy to fix CO₂ into glucose through the Calvin cycle. The two stages are coupled: light reactions depend on CO₂-fixing enzymes regenerating ADP and NADP+.

## How It's Best Learned
Trace photon capture through photosystems, electron flow, proton gradient, and ATP synthesis. Map the Calvin cycle and identify where ATP and NADPH are consumed.

## Common Misconceptions
Dark reactions occur in darkness—they occur in light too but don't directly require it. All light energy is captured—much is lost as heat and fluorescence. Photosynthesis produces only glucose—it produces ATP and NADPH used throughout the plant.

## Questions

```yaml
- question: "On a hot, dry day, a plant closes its stomata to prevent water loss. What is the most likely consequence for the two stages of photosynthesis?"
  type: multiple-choice
  options:
    - "Only the dark reactions slow, because CO₂ cannot enter; the light reactions continue producing ATP and NADPH normally"
    - "Only the light reactions slow, because less water is available to be split at Photosystem II"
    - "Both stages slow: CO₂ depletion stalls the Calvin cycle, which causes NADPH and ATP to accumulate and NADP⁺ and ADP to become depleted, eventually stalling the light reactions too"
    - "Both stages accelerate temporarily because the plant redirects more energy to photosynthesis when water stress is detected"
  answer: 2
  explanation: "The tight coupling between the two stages is the key insight. When stomata close, CO₂ supply drops, slowing the Calvin cycle. The Calvin cycle consumes ATP and NADPH and regenerates ADP and NADP⁺. When it slows, NADPH and ATP accumulate while ADP and NADP⁺ become scarce. The light reactions need NADP⁺ as the terminal electron acceptor and ADP + Pi to make ATP — without these substrates, the electron transport chain backs up and the light reactions stall. Option A is the common mistake: assuming the two stages are independent when they are mutually dependent."

- question: "Why is the term 'dark reactions' considered misleading for the Calvin cycle?"
  type: multiple-choice
  options:
    - "Because the Calvin cycle is actually light-dependent — RuBisCO requires photons directly to catalyze CO₂ fixation"
    - "Because the Calvin cycle occurs in the thylakoid membrane alongside the light reactions, not separately"
    - "Because the Calvin cycle operates during daylight hours and is light-independent (not darkness-requiring) — it can run whenever ATP and NADPH are available"
    - "Because darkness actually inhibits the Calvin cycle by reducing chloroplast pH"
  answer: 2
  explanation: "The Calvin cycle is 'light-independent' in the sense that it does not directly use photons — but it is not 'dark-requiring.' During the day, both stages run simultaneously: light reactions in the thylakoid membranes generate ATP and NADPH, which the Calvin cycle in the stroma immediately consumes. The name 'dark reactions' implies the cycle runs in darkness, but in practice it runs when ATP and NADPH are supplied, which is during light exposure. At night, the Calvin cycle slows because its substrates are depleted."

- question: "Dark reactions in photosynthesis occur only at night, when the light reactions have ceased and their products (ATP and NADPH) have accumulated to sufficient levels."
  type: true-false
  answer: false
  explanation: "This is the misconception targeted by the term 'light-independent reactions.' The Calvin cycle does not require darkness — it requires ATP and NADPH, which are produced by the light reactions during daylight. In practice, both stages run simultaneously in the light. At night, the Calvin cycle actually slows or stops because the light reactions cease and the supply of ATP and NADPH is depleted. The 'dark' label refers to the absence of a direct photon requirement, not to temporal activity during night."

- question: "If the Calvin cycle were completely inhibited (e.g., by an enzyme inhibitor targeting RuBisCO), the light reactions would eventually slow down even though light is still available and photons continue to excite chlorophyll."
  type: true-false
  answer: true
  explanation: "The Calvin cycle regenerates ADP, Pi, and NADP⁺ — the substrates the light reactions need to produce ATP and NADPH. Without Calvin cycle activity, NADPH accumulates and NADP⁺ becomes depleted, and the electron transport chain has no terminal electron acceptor. ATP also accumulates while ADP becomes scarce. The light reactions cannot continue without these substrates, so they stall despite the continued availability of light. This demonstrates the mutual dependence: the light reactions depend on the Calvin cycle just as the Calvin cycle depends on the light reactions."

- question: "Explain the metabolic coupling between the light reactions and the Calvin cycle. What would happen if you could block the Calvin cycle from regenerating ADP and NADP⁺?"
  type: short-answer
  answer: "The light reactions produce ATP and NADPH and consume ADP, Pi, and NADP⁺. The Calvin cycle consumes ATP and NADPH and regenerates ADP, Pi, and NADP⁺. This creates a closed loop: each stage's products are the other stage's substrates. If the Calvin cycle stopped regenerating ADP and NADP⁺, these molecules would be depleted from the system. The light reactions require NADP⁺ as the terminal electron acceptor (at Photosystem I) and ADP + Pi as the substrate for ATP synthase. Without them, electrons would back up in the electron transport chain and proton pumping would cease, halting ATP synthesis. The entire photosynthetic machine would stop, even with abundant light."
  explanation: "This coupling also explains why photosynthetic rate depends on environmental factors that affect only one stage: drought (limiting CO₂ for the Calvin cycle) ultimately limits both stages; cold (slowing Calvin cycle enzymes) also limits the light reactions by depleting their substrates. The two stages are not independent modules that can be regulated separately — they are a single coupled system."
```

## Explainer

You have already studied the light reactions and the Calvin cycle as separate processes. This topic brings them together as a coupled system — two halves of a single metabolic engine where each half depends on the other's outputs. Understanding photosynthesis as an integrated whole means seeing how light energy captured in the thylakoid membranes drives carbon fixation in the stroma, and how the carbon-fixing reactions regenerate the very molecules the light reactions need to keep running.

The **light reactions** occur in the thylakoid membranes of chloroplasts, where chlorophyll and accessory pigments absorb photons. This light energy drives two key events: the splitting of water molecules (releasing O₂ as a byproduct) and the transfer of excited electrons through an electron transport chain. As electrons move through this chain — from Photosystem II to Photosystem I — they lose energy in controlled steps, and that energy is used to pump protons across the thylakoid membrane, building a concentration gradient. Protons flow back through ATP synthase, generating **ATP**. At the end of the chain, Photosystem I re-energizes electrons using a second photon, and these high-energy electrons reduce NADP⁺ to **NADPH**. If you studied oxidation-reduction reactions, you can recognize this as a series of redox steps: water is oxidized, and NADP⁺ is reduced, with light providing the energy to drive an otherwise thermodynamically unfavorable electron transfer.

The **dark reactions** — more accurately called **light-independent reactions** since they occur in the light as well — take place in the chloroplast stroma. The Calvin cycle uses the ATP and NADPH generated by the light reactions to fix atmospheric CO₂ into organic carbon. The enzyme RuBisCO catalyzes the first step, attaching CO₂ to a five-carbon sugar (RuBP) to produce two three-carbon molecules (G3P). ATP provides the phosphorylation energy and NADPH provides the reducing power needed to convert these molecules into usable sugars. For every three CO₂ molecules fixed, the cycle consumes 9 ATP and 6 NADPH, and regenerates the RuBP acceptor molecules so the cycle can continue.

The critical insight is the **coupling** between these two stages. The light reactions produce ATP and NADPH but consume ADP, Pi, and NADP⁺. The Calvin cycle consumes ATP and NADPH but regenerates ADP, Pi, and NADP⁺. Neither stage can run without the other's products. If the Calvin cycle slows down — say, because stomata close during drought and CO₂ becomes scarce — then NADPH and ATP accumulate, NADP⁺ and ADP become depleted, and the light reactions stall because they have no electron acceptors or substrates. This tight coupling explains why photosynthetic rate depends on multiple factors simultaneously: light intensity, CO₂ concentration, temperature (which affects enzyme kinetics in the Calvin cycle), and water availability. The entire system is a finely tuned energy-conversion machine where the thylakoid captures light energy as chemical intermediates, and the stroma uses those intermediates to build the carbon skeletons that sustain nearly all life on Earth.
