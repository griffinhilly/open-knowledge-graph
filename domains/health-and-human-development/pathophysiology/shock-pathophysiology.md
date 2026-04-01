---
id: shock-pathophysiology
title: 'Shock: Cardiogenic, Septic, Hypovolemic, and Anaphylactic'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: blood-pressure-regulation
  type: hard
- id: homeostasis-and-feedback
  type: hard
- id: cardiovascular-system-overview
  type: soft
builds-toward:
- shock-compensation-and-decompensation
- multi-organ-failure
tags:
- shock
- hypoperfusion
- organ-failure
stage: advanced
status: validated
---

# Shock: Cardiogenic, Septic, Hypovolemic, and Anaphylactic

## Core Idea
Shock is inadequate tissue perfusion and oxygenation. Cardiogenic shock results from pump failure (heart attack, arrhythmia); hypovolemic shock from blood loss or dehydration; septic shock from vasodilation and increased capillary permeability; anaphylactic from histamine-mediated vasodilation. Compensation through increased sympathetic tone eventually fails, leading to irreversible tissue damage.

## How It's Best Learned
Use hemodynamic parameters (MAP, cardiac output, SVR) to classify shock type. Understand the three phases: compensated (normal BP, tachycardia), decompensated (falling BP, oliguria), and irreversible (refractory hypotension, organ failure).

## Common Misconceptions
Hypotension is a late sign of shock—tissue hypoperfusion can occur with normal blood pressure. Lactate normalization does not indicate recovery; persistent elevation predicts mortality despite apparent clinical improvement.

## Questions

```yaml
- question: "A patient presents with heart rate of 118 bpm, normal blood pressure, cool clammy skin, and a serum lactate of 4.2 mmol/L (normal <2). Which of the following best describes this patient's status?"
  type: multiple-choice
  options:
    - "Not in shock — blood pressure is normal, so tissue perfusion is adequate"
    - "In compensated shock — compensatory mechanisms are maintaining blood pressure despite inadequate tissue perfusion"
    - "In decompensated shock — falling blood pressure confirms shock has progressed beyond compensation"
    - "In irreversible shock — elevated lactate indicates organ failure has begun"
  answer: 1
  explanation: "This is the critical insight of shock physiology: hypotension is a late sign. This patient shows all the signs of compensated shock — tachycardia (sympathetic activation), cool skin (vasoconstriction diverting flow to core), and most tellingly, elevated lactate indicating cells are performing anaerobic glycolysis because oxygen delivery is insufficient. Blood pressure is maintained by baroreceptor-driven compensation, not because perfusion is adequate. Waiting for hypotension to diagnose shock is dangerous; lactate is the more sensitive marker."

- question: "In septic shock, cardiac output is often initially elevated. Yet patients are critically hypoperfused. What explains this paradox?"
  type: multiple-choice
  options:
    - "The heart is beating faster but ejecting less blood per stroke due to septic myocardial depression"
    - "Massive vasodilation collapses systemic vascular resistance, so MAP falls even with elevated cardiac output; capillary leak also causes functional hypovolemia"
    - "Peripheral tissues consume oxygen abnormally slowly in sepsis, creating a mismatch between delivery and uptake"
    - "Elevated cardiac output in sepsis is a measurement artifact caused by fever-related tachycardia"
  answer: 1
  explanation: "Septic shock is distributive, not pump failure. Bacterial toxins and inflammatory mediators (especially nitric oxide) cause widespread vasodilation, dropping systemic vascular resistance dramatically. Since MAP = cardiac output × SVR, even high cardiac output cannot maintain MAP when SVR has collapsed. Additionally, capillary leak from increased permeability moves plasma into the interstitium, causing 'relative hypovolemia' — the heart has little effective preload despite pumping rapidly. This hemodynamic signature (high CO, low SVR, low MAP) distinguishes sepsis from cardiogenic shock (low CO, high SVR, high filling pressures)."

- question: "A patient in early septic shock can have a normal blood pressure while simultaneously having critically inadequate tissue perfusion."
  type: true-false
  answer: true
  explanation: "True. This is the most dangerous misconception in shock management. Baroreceptor-driven sympathetic activation maintains blood pressure by increasing heart rate, vasoconstriction, and releasing catecholamines — mechanisms that can preserve MAP even while total tissue oxygen delivery is falling. Meanwhile, lactate rises as tissues shift to anaerobic metabolism, signaling cellular oxygen debt. Relying on blood pressure alone to diagnose or monitor shock misses the compensated phase, during which intervention is most effective."

- question: "Normalizing a patient's blood pressure is sufficient evidence that shock has been successfully treated and tissues are being adequately perfused."
  type: true-false
  answer: false
  explanation: "False. Blood pressure normalization is necessary but not sufficient. Compensatory vasoconstriction can restore MAP while microcirculatory maldistribution persists — blood is being delivered to the macrovasculature but not necessarily to the tissues that need it. Modern resuscitation targets lactate clearance (returning lactate to <2 mmol/L) because it directly measures whether cells have adequate oxygen. A patient whose blood pressure is restored but whose lactate remains elevated is still in occult shock and at high risk for organ failure."

- question: "Why is lactate elevated in shock, and why does lactate clearance — rather than blood pressure normalization — serve as the modern target of resuscitation?"
  type: short-answer
  answer: "Lactate rises because inadequate oxygen delivery forces cells to switch from aerobic to anaerobic glycolysis, which produces lactate as a byproduct. Blood pressure can be normalized by compensatory vasoconstriction while cellular oxygen debt persists; lactate directly reflects whether mitochondria have enough oxygen to function. Lactate clearance confirms that oxygen is reaching cells, not just that blood pressure is restored."
  explanation: "This distinction — between macrocirculatory normalization and actual tissue oxygenation — is the central insight of modern shock management. MAP = CO × SVR, and both elements can be manipulated pharmacologically to restore blood pressure without addressing the underlying deficit. Lactate serves as a biochemical readout of mitochondrial oxygen availability: if it clears, oxygen is reaching cells; if it persists, the cellular energy crisis continues regardless of blood pressure."
```

## Explainer

From your study of cardiac output and blood pressure regulation, you know that tissue perfusion depends on two things: an adequate driving pressure (mean arterial pressure, MAP = cardiac output × systemic vascular resistance) and vessels that can distribute flow to where it is needed. **Shock** is the state in which this delivery system fails to meet the oxygen demands of the tissues — not simply low blood pressure, but inadequate cellular oxygenation. The four major types of shock represent four different mechanisms of failure in this delivery system, and understanding each requires asking: which part of the equation broke?

**Hypovolemic shock** is the simplest to conceptualize: the circuit loses volume. Hemorrhage, burns, or severe dehydration reduce venous return, which reduces end-diastolic volume and therefore stroke volume (the Frank-Starling mechanism you know from cardiac physiology). Cardiac output falls, and with it MAP. Compensatory responses — baroreceptor-driven sympathetic activation, tachycardia, vasoconstriction, and ADH release — attempt to restore pressure by squeezing the remaining volume into a narrower vascular bed. **Cardiogenic shock** has the opposite origin: the pump itself fails. A large myocardial infarction destroys enough contractile tissue that stroke volume collapses regardless of adequate filling pressure. The hemodynamic signature is characteristically different from hypovolemia: filling pressures are elevated (the failing ventricle backs up blood into the lungs, causing pulmonary edema), while cardiac output and MAP are low.

**Septic shock** introduces a fundamentally different mechanism — distributive failure. Bacterial endotoxins and inflammatory mediators (nitric oxide, histamine, cytokines) cause massive vasodilation, dropping systemic vascular resistance precipitously. Unlike hypovolemic and cardiogenic shock where the vasculature is constricted, in sepsis the vessels dilate inappropriately, pooling blood in the periphery. Cardiac output is often initially elevated (the heart is pumping faster to compensate), yet MAP is low because SVR has collapsed. Additionally, increased capillary permeability allows plasma to leak into the interstitium — a functional volume loss compounding the distributive problem. **Anaphylactic shock** operates through a similar vasodilatory mechanism but is immunologically triggered: IgE-mediated mast cell and basophil degranulation releases histamine, causing acute massive vasodilation and bronchoconstriction simultaneously.

Your prerequisite knowledge of homeostasis and feedback loops explains the progression through shock's three phases. In **compensated shock**, baroreceptors detect the fall in MAP and activate the sympathetic nervous system — heart rate rises, vessels constrict, and adrenal glands release catecholamines and cortisol. Blood pressure may remain normal or nearly so, but the signs of compensation are already detectable: tachycardia, cool clammy skin (vasoconstriction), and restlessness. In **decompensated shock**, the compensatory mechanisms are overwhelmed. Blood pressure falls, oliguria develops as renal perfusion drops below the autoregulatory threshold, and tissues switch to anaerobic glycolysis — producing the lactic acid that clinically manifests as an elevated lactate level. In **irreversible shock**, prolonged ischemia triggers cell death across multiple organ systems simultaneously, inflammatory cascades become self-amplifying, and restoration of perfusion precipitates further injury through reperfusion — this stage has a very high mortality even with aggressive resuscitation.

The critical clinical insight — and the reason hypotension is a late and dangerous sign — is that MAP can be maintained by compensation even as tissue perfusion is critically impaired. A patient in early septic shock may have a normal blood pressure, normal mentation, and only subtle tachycardia. But their lactate is rising, their microcirculation is maldistributed, and their cells are in oxygen debt. This is why lactate clearance — not blood pressure normalization — is the modern target of resuscitation: it directly measures the adequacy of cellular oxygen delivery in a way that blood pressure alone cannot.
