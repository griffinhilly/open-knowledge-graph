---
id: inherited-thrombophilia-pathophysiology
title: 'Inherited Thrombophilia: Factor V Leiden, Prothrombin Mutation, and Antithrombin
  Deficiency'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: coagulation-cascade-tissue-factor-pathway
  type: hard
- id: thrombosis-pathophysiology
  type: hard
builds-toward:
- venous-thromboembolism
- recurrent-thrombosis-prophylaxis
tags:
- thrombophilia
- factor-v-leiden
- prothrombin-mutation
stage: advanced
status: draft
---

# Inherited Thrombophilia: Factor V Leiden, Prothrombin Mutation, and Antithrombin Deficiency

## Core Idea
Factor V Leiden (activated protein C resistance), prothrombin G20210A, and antithrombin/protein C/protein S deficiency increase thrombosis risk by impairing coagulation feedback inhibition or enhancing thrombin generation. These traits predispose to spontaneous or provoked venous thromboembolism, especially when combined with acquired risk factors.

## Questions

```yaml
- question: "A 28-year-old woman with heterozygous Factor V Leiden starts combined oral contraceptives. Her physician notes a dramatically elevated DVT risk compared to either risk factor alone. What best explains this synergistic interaction?"
  type: multiple-choice
  options:
    - "Estrogen causes Factor V Leiden to become homozygously expressed in the presence of exogenous hormones"
    - "Estrogen independently increases coagulation factor levels while Factor V Leiden impairs the protein C response that would normally compensate, removing the same brake from two directions simultaneously"
    - "Combined OCP directly activates Factor V Leiden, converting it to a pro-thrombotic enzyme"
    - "The interaction is additive, not synergistic — each factor contributes an equal, independent increment of risk"
  answer: 1
  explanation: "The synergy arises because estrogen and Factor V Leiden attack the same anticoagulant system from two directions. Estrogen in OCPs increases levels of coagulation factors (II, VII, X) and decreases protein S, independently shifting the system toward hypercoagulability. Factor V Leiden then makes the situation worse: even as protein C is activated (the normal compensatory response to thrombin generation), it cannot effectively cleave Factor Va because of the Arg506Gln mutation. So the brake that would normally offset estrogen-driven procoagulant activity is simultaneously impaired. The result is multiplicative risk — not just additive — because the two factors interfere with the same regulatory pathway."

- question: "A patient with antithrombin deficiency requires anticoagulation for a DVT. Which statement best describes the treatment implication of this specific thrombophilia?"
  type: multiple-choice
  options:
    - "Direct oral anticoagulants are absolutely contraindicated; only warfarin is safe"
    - "Heparin therapy will be partially ineffective because heparin works by binding antithrombin and accelerating its activity, which is already diminished"
    - "Antithrombin deficiency means the patient's thrombus will resolve faster spontaneously and less anticoagulation is needed"
    - "Standard heparin dosing is sufficient; antithrombin levels do not affect heparin pharmacodynamics"
  answer: 1
  explanation: "Heparin's anticoagulant mechanism depends on antithrombin. Heparin binds to antithrombin and accelerates its inactivation of thrombin and Factor Xa by approximately 1,000-fold. In antithrombin deficiency, there is less substrate for heparin to work with, so heparin becomes partially or substantially ineffective. Patients with antithrombin deficiency may require higher heparin doses, fresh frozen plasma (as a source of antithrombin), or antithrombin concentrates to achieve therapeutic anticoagulation. This is a direct, mechanism-driven treatment implication — understanding the biology dictates the clinical approach."

- question: "Factor V Leiden causes thrombosis by directly accelerating the forward coagulation cascade and increasing thrombin generation from the start."
  type: true-false
  answer: false
  explanation: "Factor V Leiden does not accelerate forward coagulation — it impairs the braking mechanism. In normal physiology, activated protein C cleaves Factor Va at Arg506, switching off the amplification loop and limiting thrombin generation to the site of injury. Factor V Leiden (Arg506Gln) makes Factor Va resistant to this cleavage, so the off-switch fails and thrombin generation is prolonged after it has begun. The initial coagulation stimulus and forward cascade are normal; the defect is in the feedback inhibition. This distinction matters: these patients are not continuously hypercoagulant but are rather unable to properly down-regulate coagulation once it starts."

- question: "Most heterozygous Factor V Leiden carriers will develop at least one venous thrombotic event during their lifetime if they do not receive anticoagulation."
  type: true-false
  answer: false
  explanation: "Factor V Leiden is a risk modifier, not a deterministic cause of thrombosis. Heterozygous carriers have approximately 3–5x elevated venous thrombosis risk compared to non-carriers, but the absolute lifetime risk remains relatively low. Many carriers live decades without experiencing a thrombotic event. Clinical thrombosis typically requires the inherited background to combine with an acquired trigger from Virchow's triad — immobility, endothelial injury, or a hypercoagulable state (surgery, pregnancy, OCPs). The mutation shifts the threshold; it does not guarantee the outcome. This is why routine anticoagulation of all Factor V Leiden carriers is not recommended — risk stratification based on personal and family history is required."

- question: "Explain why inherited thrombophilias are described as 'risk modifiers' rather than direct causes of thrombosis, using Factor V Leiden as your example."
  type: short-answer
  answer: "Factor V Leiden shifts the threshold at which thrombosis occurs, but it doesn't directly cause clot formation on its own. The mutation impairs activated protein C's ability to cleave Factor Va, prolonging thrombin generation once coagulation starts. But coagulation must first be initiated — by endothelial injury, stasis, or a procoagulant state. Most heterozygous carriers never develop a DVT in calm circumstances; the clinical event typically requires an acquired trigger (surgery, immobility, pregnancy, oral contraceptives) layered on top of the inherited background. The mutation lowers the threshold for clotting, so triggers that would be subclinical in a non-carrier may precipitate thrombosis in a carrier. This is why clinical management focuses on risk stratification — identifying when acquired risks are high enough to warrant prophylaxis — rather than universally anticoagulating all carriers."
  explanation: "The 'risk modifier' framing has direct clinical implications: it explains why thrombophilia testing is most useful in patients with an unprovoked thrombosis (where you'd expect the background risk to be low), and why counseling carriers about high-risk situations (surgery, pregnancy, estrogen-containing contraceptives) is more important than ongoing anticoagulation for most patients."
```

## Explainer

From the coagulation cascade, you know that the tissue factor pathway generates a burst of thrombin — the enzyme that converts fibrinogen to fibrin and amplifies its own production by activating factors V, VIII, and XI. But you may have noticed a tension: if thrombin amplifies itself, what stops the clot from growing indefinitely and occluding the entire circulation? The answer is a set of anticoagulant feedback loops that normally contain clot formation to the site of injury. **Inherited thrombophilias** are mutations that selectively break these brakes without disrupting forward coagulation — the result is a system biased toward clotting.

The most common is **Factor V Leiden**, a single point mutation (Arg506Gln) that makes Factor Va resistant to cleavage by **activated protein C (APC)**. In normal physiology, thrombomodulin on endothelial cells converts thrombin into an anticoagulant enzyme that activates protein C; protein C then cleaves and inactivates Factors Va and VIIIa, switching off the amplification loop. Factor V Leiden interferes with the off-switch: Va remains active longer, thrombin generation is prolonged, and the clot-forming tendency is amplified. Heterozygotes have ~3–5x increased venous thrombosis risk; homozygotes have ~50–80x increased risk.

**Prothrombin G20210A** works differently: it is a variant in the 3' untranslated region of the prothrombin gene that increases mRNA stability and leads to elevated prothrombin levels in plasma. More substrate means more thrombin can be generated from any given coagulation stimulus. **Antithrombin deficiency** removes a different brake entirely — antithrombin normally inactivates thrombin and Factor Xa directly, and heparin works by binding antithrombin and dramatically accelerating this inactivation. People with antithrombin deficiency are also relatively resistant to heparin therapy, which has practical treatment implications. Protein C and protein S deficiencies impair the same APC pathway as Factor V Leiden, but from the opposite direction: the brake is intact, but there isn't enough of it.

The key clinical insight is that these mutations are **risk modifiers**, not deterministic disease causes. Most heterozygous carriers live without a thrombotic event for decades — the inherited defect merely shifts the threshold. What precipitates a clinical DVT or pulmonary embolism is usually a combination of the inherited background with an acquired trigger from Virchow's triad: immobility (stasis), surgery or trauma (endothelial injury), or pregnancy and oral contraceptives (hypercoagulable state). A young woman with Factor V Leiden who starts combined oral contraceptives has a synergistic risk increase — estrogen independently increases coagulation factors while the mutation impairs the compensatory protein C response. Recognizing this multiplicative interaction guides decisions about anticoagulation and contraceptive choice.
