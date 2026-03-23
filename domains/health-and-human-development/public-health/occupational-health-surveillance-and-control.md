---
id: occupational-health-surveillance-and-control
title: Occupational Health Surveillance and Hazard Control
domain: health-and-human-development
course: public-health
prerequisites:
- id: environmental-hazard-assessment-and-risk
  type: hard
- id: disease-surveillance-systems
  type: soft
tags:
- occupational-health
- surveillance
- hazard-control
stage: expert
status: validated
---

# Occupational Health Surveillance and Hazard Control

## Core Idea
Occupational health surveillance detects work-related diseases through medical surveillance (health screening of workers), hazard surveillance (monitoring environmental exposures), or passive reporting. Surveillance informs hierarchy-of-controls: elimination of hazard, substitution with safer materials, engineering controls, administrative controls, and personal protective equipment. Effective programs use surveillance data to target control efforts.

## How It's Best Learned
Examine an occupational disease (silicosis, asthma from latex exposure, lead poisoning in battery manufacturing) through surveillance data, identify the exposure dose-response, and evaluate what control measures at different levels of the hierarchy would be feasible.

## Common Misconceptions
- Personal protective equipment is the primary control; it should be last-line defense after engineering controls are exhausted.
- Occupational hazards are only acute; many cause chronic disease with long latency, requiring prospective surveillance.

## Questions

```yaml
- question: "Workers in a ceramics factory are exposed to high concentrations of respirable crystalline silica. Management responds by issuing N95 respirators to all workers. Which statement best evaluates this response?"
  type: multiple-choice
  options:
    - "This is the optimal control because respirators directly protect each worker from inhaling silica"
    - "This is appropriate as a short-term emergency measure, but engineering controls such as local exhaust ventilation should be the primary long-term solution"
    - "This is sufficient because PPE is the most reliable control when properly used"
    - "This is appropriate because administrative controls should be exhausted before engineering controls are considered"
  answer: 1
  explanation: "Respirators are last in the hierarchy of controls. They depend entirely on correct use at every exposure moment — they leak around facial hair, workers remove them when hot, and they provide no protection when forgotten. Local exhaust ventilation (an engineering control) captures silica dust at the source before it reaches breathing zones, without relying on worker behavior. Option C is the classic misconception that PPE is 'direct protection' — in practice, it is the most failure-prone control."

- question: "A pulmonologist notices a cluster of workers at a shipyard with abnormal chest X-rays suggesting asbestosis. She contacts the occupational health unit. What surveillance stream should this trigger?"
  type: multiple-choice
  options:
    - "Passive reporting only, since the disease has already appeared and prospective surveillance is no longer useful"
    - "Medical surveillance only, to screen remaining workers for early disease"
    - "Hazard surveillance — measuring airborne asbestos fiber levels — to assess current exposure and prevent further disease"
    - "Both hazard surveillance (airborne fiber monitoring) and intensified medical surveillance of remaining workers"
  answer: 3
  explanation: "The two surveillance streams are complementary and should be triggered together. Medical surveillance (screening remaining workers for subclinical disease) identifies who else may be affected. Hazard surveillance (measuring current asbestos levels) determines whether ongoing exposure continues — it is possible current workers are still being exposed decades after the original cohort. The two streams feed each other: medical findings prompt exposure investigation; exposure findings intensify health monitoring."

- question: "Personal protective equipment is the least preferred control in the hierarchy because it provides no protection to the worker."
  type: true-false
  answer: false
  explanation: "PPE does provide protection — when used correctly. The reason it is last in the hierarchy is that it depends entirely on consistent correct use by the worker at every exposure moment, making it the most failure-prone control. Engineering controls (which remove or isolate the hazard) and elimination/substitution (which remove the hazard entirely) are preferred because they work independently of worker behavior."

- question: "Occupational medical surveillance for diseases with long latency periods — such as asbestosis or silicosis — must begin at the time of initial employment, long before any symptoms appear."
  type: true-false
  answer: true
  explanation: "Silicosis takes 10–20 years of cumulative exposure to manifest clinically; mesothelioma presents 30–40 years after asbestos exposure. By the time symptoms appear, irreversible fibrosis is already established and the causal exposures are decades in the past. Longitudinal baseline measurements (pulmonary function tests, chest X-rays, audiograms) from initial employment create a surveillance record that detects trends — slowly declining FEV₁, for example — long before clinical disease, allowing intervention before irreversible damage occurs."

- question: "Explain why engineering controls are ranked above administrative controls in the hierarchy of controls for occupational hazards."
  type: short-answer
  answer: "Engineering controls physically remove or isolate the hazard — local exhaust ventilation captures dust before it reaches breathing zones; enclosure prevents worker exposure entirely — without depending on worker behavior. Administrative controls (job rotation, shift limits, access restrictions) reduce exposure by modifying work organization, but still leave the hazard present and rely on consistent procedural compliance from workers and supervisors. Since human behavior is more variable and failure-prone than physical systems, controls that function regardless of worker behavior are more reliable and therefore ranked higher."
  explanation: "This principle — that controls higher in the hierarchy work independently of human reliability — is why the hierarchy is ordered by effectiveness, not convenience. PPE at the bottom requires correct use at every exposure moment; elimination at the top removes the problem completely regardless of what anyone does."
```

## Explainer

From environmental hazard assessment, you know that risk is the product of hazard and exposure — and that exposure has dose, duration, and route dimensions. Occupational settings concentrate this exposure problem: workers spend 8+ hours daily in environments shaped by industrial processes, often with chemicals, dusts, noise, and ergonomic stressors at levels far higher than the general public encounters. **Occupational health surveillance** is the systematic collection and analysis of data about this worker-hazard interface, designed to detect problems before they cause irreversible disease or death.

There are two distinct surveillance streams that work together. **Hazard surveillance** monitors the work environment itself — measuring airborne concentrations of respirable silica, blood lead levels in battery plant workers, noise decibel levels in machine shops, or radiation dosimetry for radiologic technicians. This is prospective: you measure the exposure and assess whether it exceeds safe thresholds before workers become ill. **Medical surveillance** monitors the workers directly — pulmonary function tests for miners, audiograms for workers near loud machinery, periodic chest X-rays for asbestos workers. Medical surveillance catches early subclinical disease and identifies individuals with unusual susceptibility. The two streams feed back to each other: an unexpected cluster of abnormal chest X-rays should trigger investigation of workplace dust levels; elevated silica air sampling should intensify pulmonary function monitoring.

The **hierarchy of controls** is the conceptual framework for what to do once surveillance identifies a hazard. It is ordered from most to least effective, not from most to least convenient. **Elimination** — removing the hazard entirely — is always preferable if feasible; replacing a carcinogenic solvent with a safer one eliminates the exposure rather than managing it. **Substitution** swaps the hazard for a less dangerous alternative (water-based instead of solvent-based paints). **Engineering controls** isolate workers from the hazard without relying on their behavior: local exhaust ventilation captures silica dust at the point of generation before it reaches breathing zones; enclosing a noisy process reduces sound levels for everyone nearby. **Administrative controls** — job rotation, limiting shift length in extreme heat, restricting access to high-hazard areas — reduce exposure through work organization rather than physical modification of the environment. **Personal protective equipment (PPE)** — respirators, hearing protection, gloves — sits at the bottom of the hierarchy because it depends entirely on correct use by the worker at every exposure moment. Respirators leak around poor facial-hair seals; workers remove them when hot; they provide no protection if left in the locker.

The chronic latency problem is why prospective surveillance cannot be replaced by reactive reporting. Silicosis (from crystalline silica in mining, sandblasting, and ceramics) takes 10–20 years of cumulative exposure before clinical disease appears. Mesothelioma from asbestos presents 30–40 years after the original exposure. By the time workers develop symptoms, the causal exposures are decades in the past and often irreversible fibrosis has occurred. Biological exposure indices and health screening must begin at the time of employment, creating a longitudinal record that can detect trends — a cohort of workers with slowly declining FEV₁ values identifies a hazard long before anyone reaches clinical COPD. This is why occupational medicine emphasizes surveillance as continuous system monitoring rather than episodic clinical response.
