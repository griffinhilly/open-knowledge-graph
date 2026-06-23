---
id: skeletal-muscle-contraction
title: Skeletal Muscle Contraction
domain: biology
course: physiology
prerequisites:
- id: neuromuscular-junction
  type: hard
- id: atp-synthesis
  type: hard
- id: active-transport
  type: soft
- id: motor-proteins-cellular-movement
  type: soft
tags:
- muscle contraction
- sliding filament
- sarcomere
- troponin
- calcium
- cross-bridge cycle
stage: formal-systems
status: validated
---

# Skeletal Muscle Contraction

## Core Idea
Skeletal muscle contraction follows the sliding filament model: thin actin filaments slide over thick myosin filaments, shortening each sarcomere without changing the filament lengths. Excitation-contraction coupling begins when muscle action potentials propagate along T-tubules, triggering Ca²⁺ release from the sarcoplasmic reticulum via ryanodine receptors. Ca²⁺ binds troponin C on the thin filament, causing tropomyosin to shift and expose myosin-binding sites on actin. Myosin heads undergo the cross-bridge cycle: bind actin → power stroke (ADP + Pi released) → rigor state → ATP binds → myosin detaches and re-cocks. Relaxation requires SERCA pumps (ATP-driven) to remove Ca²⁺ back into the sarcoplasmic reticulum, allowing tropomyosin to re-cover actin sites.

## How It's Best Learned
Memorize the four-step cross-bridge cycle with ion and nucleotide states at each step: cocked myosin (ATP hydrolyzed, ADP+Pi bound) → binds actin → power stroke (Pi released) → rigor state → ATP binds → detachment. Explain rigor mortis mechanically: ATP is depleted after death, so myosin cannot detach from actin — muscles lock rigid. Then draw a sarcomere at rest and at maximum contraction, labeling A, I, H, and M bands.

## Common Misconceptions
- ATP is required not only to power the power stroke but to detach the myosin head from actin; without ATP, the muscle locks in rigor, not relaxation.
- The muscle membrane conducts its own separate action potential that propagates throughout the fiber — it is distinct from, though triggered by, the neural end-plate potential.
- Muscle does not 'shorten' by compressing the filaments; the filaments remain the same length, and the sarcomere shortens because actin and myosin filaments overlap more.

## Questions

```yaml
- question: "At which step in the cross-bridge cycle does ATP most directly cause myosin to detach from actin?"
  type: multiple-choice
  options:
    - "During the power stroke, when ADP and Pi are released from myosin"
    - "When a new ATP molecule binds to myosin immediately after the rigor state"
    - "When Ca²⁺ binds to troponin C and exposes the myosin-binding sites on actin"
    - "When SERCA pumps Ca²⁺ back into the sarcoplasmic reticulum during relaxation"
  answer: 1
  explanation: "After the power stroke, myosin is in the rigor state — tightly bound to actin with no nucleotide. It is the binding of a fresh ATP molecule to the myosin head that induces a conformational change causing detachment from actin. ATP hydrolysis (to ADP + Pi) then re-cocks the myosin head, preparing it for the next cycle. This is why ATP is required for both contraction and relaxation: without it, myosin cannot release actin."

- question: "During maximal muscle contraction, the actin and myosin filaments themselves shorten, which is why the sarcomere gets shorter."
  type: true-false
  answer: false
  explanation: "The sliding filament model specifies that the filaments do NOT change length. The sarcomere shortens because actin filaments slide further over the myosin filaments, increasing the overlap between them. The A band (thick filament length) stays constant; the I bands and H zone narrow as actin slides inward. This was the key experimental insight from Huxley and Hanson in the 1950s."

- question: "Explain why rigor mortis occurs after death, using the mechanism of the cross-bridge cycle."
  type: short-answer
  answer: "After death, ATP production (oxidative phosphorylation and glycolysis) ceases as oxygen and substrate supplies fail. Without ATP, myosin heads that have completed a power stroke cannot detach from actin — ATP binding is what causes detachment. All cross-bridges become permanently locked in the rigor state, causing muscles to stiffen. Rigor resolves hours later as proteolytic enzymes degrade the contractile proteins."
  explanation: "This is the most direct clinical application of the cross-bridge cycle mechanism. It illustrates that ATP is not 'fuel for contraction' in a simple sense — it is specifically required for the detachment step. Muscles actually lock in a shortened, contracted-like state, not in relaxation, because that is the state myosin occupies when cross-bridges are formed."
```

## Explainer

Skeletal muscle contraction is a beautiful example of molecular machinery scaled from individual protein interactions to whole-body movement. To understand it, start with the architecture: each muscle fiber is packed with myofibrils, and each myofibril is a repeating chain of sarcomeres. A sarcomere is bounded by Z-discs, from which thin (actin) filaments project inward. Thick (myosin) filaments occupy the center. Contraction happens when actin slides over myosin — the filaments themselves stay the same length, but the sarcomere shortens as overlap increases.

The trigger for contraction comes from your nervous system. An action potential travels down the motor neuron, crosses the neuromuscular junction (which you studied as a prerequisite), and generates an end-plate potential in the muscle membrane. This propagates as a muscle action potential along the fiber surface and then dips deep into the fiber via T-tubules. At junctions between T-tubules and the sarcoplasmic reticulum (SR), voltage-sensing proteins (dihydropyridine receptors) detect the action potential and physically gate ryanodine receptors in the SR membrane, releasing a flood of Ca²⁺ into the cytoplasm. This is excitation-contraction coupling — converting the electrical signal into a chemical trigger for the contractile machinery.

Ca²⁺ is the master switch for the thin filament. At rest, tropomyosin physically blocks the myosin-binding sites on actin. When Ca²⁺ binds to troponin C (part of the troponin complex), a conformational change shifts tropomyosin out of the way, exposing the binding sites. Myosin heads — already cocked and loaded with ADP + Pi from the previous hydrolysis — can now bind actin. Binding triggers release of Pi, followed by the power stroke: the myosin head pivots, pulling the actin filament toward the sarcomere center. ADP is released, leaving myosin in the rigor state. When a new ATP binds, myosin detaches; ATP hydrolysis re-cocks the head; and the cycle repeats as long as Ca²⁺ keeps troponin permissive.

Relaxation requires active work: SERCA pumps (Ca²⁺-ATPases in the SR membrane) use ATP to pump Ca²⁺ back into the SR against its concentration gradient. As cytoplasmic Ca²⁺ falls, troponin releases Ca²⁺, tropomyosin re-covers the actin sites, and myosin heads can no longer bind. This is why ATP is needed not just for the power stroke but for relaxation too — a point rigor mortis makes starkly: when ATP is exhausted after death, SERCA stops pumping, Ca²⁺ remains elevated, and myosin remains locked onto actin, stiffening the muscle.
