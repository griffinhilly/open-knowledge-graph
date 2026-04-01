---
id: coagulation-cascade-extrinsic-intrinsic-common
title: 'Coagulation Cascade: Extrinsic, Intrinsic, and Common Pathways'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: hemostasis-pathophysiology
  type: hard
- id: hemostasis-coagulation-cascade
  type: hard
- id: complement-activation-pathways
  type: soft
builds-toward:
- thrombosis-pathophysiology
- disseminated-intravascular-coagulation
tags:
- coagulation
- tissue-factor
- intrinsic-pathway
- thrombin
- prothrombin
stage: advanced
status: validated
---

# Coagulation Cascade: Extrinsic, Intrinsic, and Common Pathways

## Core Idea
Blood coagulation is triggered by tissue factor (TF) or contact activation, proceeding through extrinsic and intrinsic pathways that converge on the common pathway. The extrinsic pathway (tissue damage → TF + VII → X activation) is rapid and physiologically important. The intrinsic pathway (contact → XII → XI → IX, amplified by VIII) may be an artifact of in vitro testing. Both converge on factor X activation, leading to prothrombin (II) → thrombin (IIa) → fibrinogen → fibrin polymerization and crosslinking by factor XIII.

## How It's Best Learned
Use the tissue factor pathway model, which emphasizes that tissue factor initiation is the physiologically relevant trigger. Study coagulation factor deficiencies and their clinical presentations. Understand vitamin K's role in γ-carboxylation of factors II, VII, IX, X.

## Common Misconceptions
The intrinsic pathway is largely a laboratory artifact; in vivo coagulation is primarily initiated by tissue factor. Factor deficiencies in the 'intrinsic' pathway (VIII, IX, XI) cause bleeding because they amplify the TF-initiated response.

## Questions

```yaml
- question: "A patient has a severe deficiency of factor XII (Hageman factor). Surprisingly, they have no abnormal bleeding. Which explanation best accounts for this clinical finding?"
  type: multiple-choice
  options:
    - "Factor XII deficiency is compensated by upregulation of factor VII, maintaining normal extrinsic pathway activity"
    - "Factor XII initiates the intrinsic pathway through contact activation — a process relevant in test tubes but not the physiological trigger for in vivo coagulation, which is initiated by tissue factor"
    - "Factor XII is only required for fibrin crosslinking by factor XIII, which is rarely essential for primary hemostasis"
    - "Factor XII deficiency causes thrombosis rather than bleeding because the contact system normally inhibits coagulation"
  answer: 1
  explanation: "The intrinsic (contact activation) pathway, which begins with factor XII, is primarily a laboratory phenomenon triggered when blood contacts artificial surfaces like glass or kaolin. In vivo, coagulation is overwhelmingly initiated by tissue factor (extrinsic pathway), which is exposed when vessel walls are injured. Patients with factor XII deficiency have normal hemostasis precisely because their in vivo clotting mechanism — tissue factor initiation — is intact. In contrast, deficiencies in factors VIII and IX (also 'intrinsic' pathway components) DO cause bleeding because these factors serve as critical amplifiers that sustain the TF-initiated response, not because contact activation itself is physiologically important."

- question: "A patient with hemophilia A (factor VIII deficiency) bleeds severely despite an intact tissue factor pathway. Factor VIII is part of the intrinsic pathway. Why does its absence cause bleeding if the extrinsic pathway can still activate factor X directly?"
  type: multiple-choice
  options:
    - "Factor VIII is required to activate tissue factor, so the extrinsic pathway cannot function without it"
    - "The initial TF burst activates only a small amount of factor X; factors VIII and IX form the tenase complex that amplifies this signal — without amplification, initial thrombin generation is insufficient to form an adequate clot"
    - "Factor VIII directly converts prothrombin to thrombin in the common pathway, completely bypassing factor X activation"
    - "Factor VIII is required for platelet plug formation, and without a platelet plug the coagulation cascade cannot proceed at all"
  answer: 1
  explanation: "The tissue factor pathway generates an initial burst of thrombin, but this burst is quickly shut down by TFPI (tissue factor pathway inhibitor). Sustained coagulation requires amplification through the intrinsic pathway's tenase complex: factor IXa (activated by the TF-VIIa complex) combines with factor VIIIa (as cofactor) to activate factor X far more efficiently than TF-VIIa alone. In hemophilia A, factor VIII is absent, so the tenase amplification loop cannot form. The initial TF-triggered clot forms slowly and is too weak to stop bleeding from significant wounds. This explains why hemophilia A is treated with factor VIII replacement — restoring the amplifier, not the initiator."

- question: "A patient taking warfarin for atrial fibrillation shows a prolonged PT/INR with a normal aPTT. This pattern specifically indicates a defect in the intrinsic pathway."
  type: true-false
  answer: false
  explanation: "The opposite is true: PT/INR tests the extrinsic and common pathway (factors VII, X, V, II, fibrinogen). A prolonged PT with normal aPTT is the classic early warfarin pattern — factor VII has the shortest half-life of the vitamin K-dependent factors and falls first, affecting the extrinsic pathway before the intrinsic factors (IX, X, II) are significantly depleted. The aPTT tests the intrinsic and common pathway (factors XII, XI, IX, VIII, X, V, II, fibrinogen); it is prolonged in hemophilia A and B (factor VIII or IX deficiency) or with heparin therapy. Knowing which test probes which pathway is essential for interpreting coagulation results mechanistically."

- question: "Thrombin's role in the coagulation cascade extends beyond converting fibrinogen to fibrin — it also amplifies its own production by activating upstream coagulation factors."
  type: true-false
  answer: true
  explanation: "Thrombin is the central amplifier of the entire cascade. Once small amounts are generated by the TF-VIIa complex, thrombin activates factors V and VIII (converting them to their active cofactor forms Va and VIIIa), which dramatically accelerates formation of the prothrombinase and tenase complexes respectively. This creates a powerful positive feedback loop: a tiny initial thrombin signal triggers assembly of the complexes that generate massive amounts of additional thrombin. Thrombin also activates factor XIII (which crosslinks fibrin into a covalent mesh) and activates platelets. This multi-level amplification is what allows the cascade to produce an explosive clot response within seconds of injury initiation."

- question: "Warfarin anticoagulates effectively despite not directly inhibiting thrombin or factor Xa. Explain the mechanism, connecting it to the cascade's structural architecture."
  type: short-answer
  answer: "Warfarin blocks vitamin K epoxide reductase, preventing the recycling of vitamin K. Without active vitamin K, the gamma-carboxylation of glutamate residues on factors II (prothrombin), VII, IX, and X cannot occur. This carboxylation is required for these factors to bind calcium ions, which in turn allows them to anchor to negatively charged phospholipid surfaces (predominantly on activated platelets). Without membrane anchoring, the prothrombinase complex (Xa + Va) and tenase complexes (IXa + VIIIa) cannot assemble efficiently, and prothrombin-to-thrombin conversion collapses. By disabling four critical nodes spanning both pathways and the common pathway, warfarin effectively blocks the entire cascade from amplifying beyond the initial TF burst."
  explanation: "This mechanism explains the clinical properties of warfarin: it takes 2–3 days to reach full effect (because existing carboxylated factors must be cleared), it is reversed by vitamin K (which restores carboxylation capacity), and it affects multiple factors with different half-lives (factor VII falls first, explaining why PT/INR rises before aPTT). The PT/INR is used to monitor warfarin specifically because it tests factors VII, X, V, II — the vitamin K-dependent factors that warfarin depletes most predictably. Understanding the gamma-carboxylation mechanism also explains why neonates and patients with malabsorption syndromes develop bleeding diatheses resembling warfarin overdose: they lack adequate vitamin K."
```

## Explainer

You already understand that hemostasis involves a platelet plug followed by a fibrin mesh — the coagulation cascade is the molecular mechanism that builds that mesh. Think of the cascade as a signal amplification system: each activated factor activates many molecules of the next, so a tiny initiating signal produces an explosive burst of thrombin. Without amplification, bleeding would continue for minutes while the body slowly produced a response; with it, significant fibrin can form within seconds at a wound site.

The **extrinsic pathway** is the physiologically dominant trigger. When a vessel is cut, subendothelial cells that are normally hidden from blood expose **tissue factor (TF)** — a membrane protein that rapidly binds circulating factor VII. The TF-VIIa complex activates both factor X (entering the common pathway) and factor IX (cross-activating the intrinsic pathway's amplification arm). This TF initiation model replaced the older classroom diagram that treated both pathways as equals. The **intrinsic pathway** begins with factor XII activation by contact with foreign surfaces — relevant in a test tube, but patients with factor XII deficiency do not bleed abnormally because this contact activation is not the in vivo trigger. The intrinsic pathway matters clinically because factors VIII and IX (absent in hemophilia A and B) are the amplification machinery that sustains coagulation after TF initiation begins it.

The **common pathway** starts where both pathways converge: activated factor X pairs with factor Va as a **prothrombinase complex** on phospholipid surfaces (primarily activated platelet membranes) to convert **prothrombin (factor II)** into **thrombin (factor IIa)**. Thrombin is the central enzyme of the whole cascade — it cleaves **fibrinogen** into fibrin monomers that spontaneously polymerize, and it activates factor XIII, which crosslinks fibrin polymers into a covalently bonded, mechanically strong clot. Thrombin also powerfully amplifies its own production by activating factors V and VIII upstream.

**Vitamin K** connects directly to this cascade in a clinically important way. Factors II, VII, IX, and X — all of which appear at critical nodes — require vitamin K-dependent γ-carboxylation to bind calcium and anchor to phospholipid surfaces. Without this modification, the prothrombinase and tenase complexes cannot assemble properly. Warfarin works by blocking vitamin K recycling, thus anticoagulating by starving these factors of their calcium-binding modification. Laboratory tests map directly onto the pathways: **PT/INR** tests the extrinsic and common pathways (VII, X, V, II, I) and is prolonged by warfarin; **aPTT** tests the intrinsic and common pathways (XII, XI, IX, VIII, X, V, II) and is prolonged in hemophilia. Knowing which pathway each factor belongs to lets you interpret these tests mechanistically rather than memorizing normal values in isolation.
