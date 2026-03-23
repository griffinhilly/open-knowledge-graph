---
id: valvular-disease-stenosis-and-regurgitation
title: 'Valvular Disease: Stenosis and Regurgitation'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: cardiac-cycle-and-heart-function
  type: hard
- id: blood-pressure-regulation
  type: soft
builds-toward:
- heart-failure-types-and-mechanisms
tags:
- valve-disease
- stenosis
- regurgitation
- hemodynamics
stage: expert
status: validated
---

# Valvular Disease: Stenosis and Regurgitation

## Core Idea
Valve stenosis (narrowed orifice) increases afterload on the upstream chamber, causing concentric hypertrophy and eventual dysfunction. Aortic stenosis causes LV hypertrophy, diastolic dysfunction, and ischemia; mitral stenosis increases LA and pulmonary pressures. Valve regurgitation (insufficient closure) causes volume overload, eccentric hypertrophy, and chamber dilation of the upstream chamber. Acute versus chronic regurgitation have different compensatory mechanisms—chronic regurgitation is better tolerated due to gradual chamber remodeling. Combined lesions (e.g., mitral stenosis + regurgitation) have complex hemodynamic consequences.

## How It's Best Learned
Study the hemodynamic consequences of each lesion using pressure-volume diagrams. Understand why aortic stenosis progresses to heart failure (increased afterload, myocardial ischemia). Trace the progression from compensation through decompensation in each lesion.

## Common Misconceptions
Stenotic lesions are not 'narrowed by fat'; they are from leaflet pathology (calcification, fibrosis, endocarditis). Regurgitation is not always hemodynamically significant early—the heart compensates through eccentric hypertrophy. Mitral stenosis (narrowing) increases pulmonary pressure, predisposing to atrial fibrillation and thrombus.

## Questions

```yaml
- question: "A patient with severe chronic aortic regurgitation has remained asymptomatic for 15 years. The primary mechanism that allows this prolonged compensation is:"
  type: multiple-choice
  options:
    - "Concentric hypertrophy normalizing wall stress by thickening the ventricular wall in response to pressure overload"
    - "Eccentric hypertrophy accommodating the increased volume load while maintaining forward stroke volume via the Frank-Starling mechanism"
    - "Decreased systemic vascular resistance reducing afterload on the left ventricle"
    - "Diastolic dysfunction slowing ventricular filling and reducing the regurgitant fraction"
  answer: 1
  explanation: "Aortic regurgitation creates volume overload — the ventricle receives both normal pulmonary return and the regurgitant diastolic volume. Compensation is eccentric hypertrophy: the chamber dilates (sarcomeres added in series) to accommodate the extra volume, and increased preload drives Frank-Starling-mediated maintenance of stroke volume. This gradual remodeling can sustain normal cardiac output for years. Concentric hypertrophy (option A) is the response to pressure overload — the pattern seen in stenosis, not regurgitation."

- question: "In aortic stenosis, exertional syncope occurs because:"
  type: multiple-choice
  options:
    - "The hypertrophied ventricular wall becomes ischemic during effort, triggering a vagal response and bradycardia"
    - "The stenotic valve fixes cardiac output — it cannot increase to match peripheral vasodilation that exercise demands"
    - "The regurgitant fraction reduces net forward output during the increased metabolic demands of exercise"
    - "Atrial fibrillation from elevated left ventricular end-diastolic pressure causes sudden hemodynamic compromise"
  answer: 1
  explanation: "In severe aortic stenosis, the stenotic valve limits the maximum rate of forward flow. At rest, this fixed output may be sufficient. Exercise demands increased cardiac output and induces peripheral vasodilation. When the stenotic valve cannot allow output to increase to match vasodilation, blood pressure falls and cerebral perfusion is transiently inadequate — syncope. This 'fixed output' physiology is distinct from the diastolic dysfunction driving exertional angina, or the elevated filling pressures causing dyspnea."

- question: "Acute aortic regurgitation is better tolerated than chronic aortic regurgitation because the heart has had time to adapt gradually to the volume load."
  type: true-false
  answer: false
  explanation: "The opposite is true. Chronic regurgitation allows gradual eccentric remodeling — the ventricle dilates over years to accommodate extra volume, keeping filling pressures from rising sharply. Acute regurgitation (from endocarditis or aortic dissection) gives no time for adaptation: the normal-sized ventricle is suddenly overwhelmed, filling pressures spike acutely, and pulmonary edema can develop within hours — a cardiac emergency. The compensation that makes chronic regurgitation tolerable for years is entirely absent in the acute setting."

- question: "Mitral stenosis elevates left atrial pressure, which can predispose patients to atrial fibrillation and intracardiac thrombus formation."
  type: true-false
  answer: true
  explanation: "Mitral stenosis impedes flow from the left atrium into the left ventricle, causing chronic left atrial pressure elevation and progressive atrial dilation. The enlarged, hypertensive atrium develops a substrate for atrial fibrillation — disorganized electrical activity replacing coordinated contraction. Atrial fibrillation is doubly harmful: it eliminates the atrial 'kick' (20–30% of ventricular filling) and causes blood stasis in the atrial appendage, predisposing to thrombus formation and embolic stroke. This chain — stenosis → pressure → dilation → AF → thrombus — follows directly from the hemodynamics of the lesion."

- question: "Explain why stenosis and regurgitation produce different types of ventricular hypertrophy, relating each pattern to the specific mechanical stress imposed on the chamber."
  type: short-answer
  answer: "Stenosis creates pressure overload — the ventricle must generate higher pressure to force flow across a narrowed orifice. By Laplace's law (wall stress = pressure × radius / 2 × wall thickness), the ventricle normalizes wall stress by adding sarcomeres in parallel, thickening the wall without increasing chamber volume: concentric hypertrophy. Regurgitation creates volume overload — extra volume fills the chamber each cycle. The ventricle accommodates this by adding sarcomeres in series, dilating the chamber (increasing radius) while wall thickness increases proportionally: eccentric hypertrophy. The type of mechanical stress — pressure versus volume — determines the direction of sarcomere addition."
  explanation: "Laplace's law is the bridge between mechanics and morphology. Pressure overload increases the numerator (pressure), so the compensatory response must increase wall thickness to normalize stress — concentric pattern. Volume overload increases the radius term from dilation, and both thickness and radius increase together — eccentric pattern. These are geometrically distinct responses to distinct hemodynamic insults, and recognizing which is occurring tells you what type of valvular lesion is present."
```

## Explainer

Valve disease follows directly from the cardiac cycle you already know: the heart is a pressure pump that relies on one-way valves to direct flow efficiently. The left ventricle generates ~120 mmHg of systolic pressure to eject blood into the aorta; this only works if the aortic valve opens fully and the mitral valve seals completely. Any deviation — a valve that won't open enough (**stenosis**) or a valve that won't close completely (**regurgitation**) — forces the heart to work differently, and understanding how the heart compensates reveals both why patients can remain asymptomatic for years and why they eventually decompensate.

**Stenosis** creates a pressure overload problem. In **aortic stenosis**, the left ventricle faces a narrowed outflow valve — it must generate much higher pressure to force the same flow across a smaller orifice. The response is **concentric hypertrophy**: the ventricular wall thickens (more sarcomeres added in parallel) to normalize wall stress per the law of Laplace. This initially preserves ejection fraction, but thick walls are stiff walls. The ventricle loses compliance (diastolic dysfunction), requiring higher filling pressures to achieve adequate preload. Patients develop the classic triad — angina (hypertrophied muscle outstrips coronary supply), syncope (fixed cardiac output cannot respond to vasodilation on exertion), and heart failure (elevated filling pressures cause pulmonary congestion). In **mitral stenosis**, the problem is upstream: the left atrium cannot empty efficiently, pressure backs up into the pulmonary veins, and elevated pulmonary capillary pressure causes dyspnea, pulmonary hypertension, and eventually right heart failure. The chronically elevated left atrial pressure also causes atrial enlargement and atrial fibrillation — which simultaneously eliminates the atrial "kick" that accounts for 20–30% of ventricular filling, further compromising hemodynamics.

**Regurgitation** creates a volume overload problem — a fundamentally different stress. In **aortic regurgitation**, blood ejected into the aorta refluxes back into the left ventricle during diastole. The ventricle now receives both normal pulmonary return and the regurgitant volume. It compensates with **eccentric hypertrophy**: the chamber dilates (sarcomeres added in series) to accommodate the extra volume, and increased preload (Frank-Starling mechanism) maintains stroke volume. Chronic regurgitation can be remarkably well tolerated for years — the gradual remodeling prevents sudden pressure rises. This is why acute regurgitation (from endocarditis or aortic dissection) is dramatically more dangerous: the ventricle has no time to remodel, filling pressure spikes suddenly, and pulmonary edema develops within hours. The challenge in managing chronic regurgitation is that compensation masks symptoms until the ventricle is irreversibly dilated and systolic function begins to fall — surgical timing aims to intervene before this point of no return.

The difference in compensation also predicts the ausculatory findings. Stenosis creates turbulence as blood is forced through a narrowed orifice — aortic stenosis produces a crescendo-decrescendo systolic ejection murmur (blood accelerates then decelerates through the stenotic valve); mitral stenosis produces a low-pitched diastolic rumble (blood flows through the narrowed mitral valve during ventricular filling). Regurgitation produces murmurs of backward flow — aortic regurgitation creates a high-pitched early diastolic decrescendo murmur; mitral regurgitation creates a holosystolic murmur radiating to the axilla. Each murmur tells you the phase of the cardiac cycle when backward or turbulent flow occurs, which traces directly back to the valve anatomy and the pressure gradients driving flow in each phase.
