---
id: coronary-circulation-myocardial-oxygen
title: Coronary Circulation and Myocardial Oxygen Supply-Demand Balance
domain: biology
course: physiology
prerequisites:
- id: cardiovascular-system-overview
  type: hard
- id: mitochondrion-energy-production
  type: soft
builds-toward:
- blood-pressure-regulation
tags:
- cardiac
- coronary
- oxygen
- metabolism
stage: formal-systems
status: draft
---

# Coronary Circulation and Myocardial Oxygen Supply-Demand Balance

## Core Idea
The heart has exceptional metabolic demands—continuously consuming ~70-80% of delivered oxygen (compared to ~25% in resting skeletal muscle)—requiring precise matching of coronary blood flow to myocardial oxygen consumption. Coronary arteries branch from the aorta, perfusing the ventricular wall, with flow occurring primarily during diastole when ventricular pressure is low. Myocardial oxygen delivery depends on coronary blood flow and arterial oxygen content; oxygen consumption correlates tightly with cardiac work (heart rate × contractility). Coronary autoregulation maintains relatively constant flow despite blood pressure changes through metabolic mechanisms (adenosine, ATP depletion) and endothelial-derived factors (nitric oxide).

## How It's Best Learned
Measure coronary blood flow and oxygen saturation using angiography or Doppler ultrasound. Study how increased cardiac work (pacing or exercise) increases oxygen consumption and coronary vasodilation.

## Common Misconceptions
Coronary blood flow occurs continuously during both systole and diastole, not only during diastole as sometimes oversimplified; however, most flow does occur in diastole.

## Questions

```yaml
- question: "During vigorous exercise, a person's heart rate and cardiac output increase substantially. How does the heart increase its oxygen supply to meet this demand?"
  type: multiple-choice
  options:
    - "By extracting more oxygen from the blood already passing through the coronary arteries, since extraction is far below maximum at rest"
    - "By reducing contractile force to lower oxygen consumption while maintaining cardiac output"
    - "By dilating coronary arteries to increase blood flow per minute, since the heart already extracts nearly all delivered oxygen at rest"
    - "By recruiting dormant coronary collateral vessels that were inactive at rest"
  answer: 2
  explanation: "The heart's near-maximal resting oxygen extraction (70–80%) means the reserve for increased extraction is nearly exhausted — skeletal muscle extracts only ~25% at rest and can triple this during exercise, but the heart cannot match that flexibility. When the myocardium needs more oxygen, it must receive more blood per minute. Metabolic vasodilators — especially adenosine released when ATP is consumed faster than it can be replenished — relax coronary arteriolar smooth muscle, increasing flow up to 4–5 fold. This is precisely why coronary artery disease is dangerous during exertion: atherosclerotic narrowing limits the vessel's ability to dilate, capping oxygen delivery below what the heart needs."

- question: "A patient with severe left coronary artery stenosis experiences chest pain during exercise but not at rest. Which physiological explanation best accounts for this pattern?"
  type: multiple-choice
  options:
    - "At rest, autoregulation compensates by dilating downstream arterioles; during exercise, increased demand exhausts the coronary flow reserve that stenosis has already reduced"
    - "At rest, higher blood pressure forces blood through the stenosis; during exercise, lower pressure cannot drive adequate flow"
    - "Angina only occurs during exercise because physical activity directly irritates the atherosclerotic plaque"
    - "The stenosis worsens during exercise because the contracting muscle compresses the already-narrowed artery"
  answer: 0
  explanation: "Coronary autoregulation maintains adequate resting flow despite moderate stenosis by dilating downstream arterioles — the coronary flow reserve compensates for the restriction. During exercise, increased cardiac work demands more oxygen delivery, requiring further vasodilation. But downstream arterioles are already near-maximally dilated just to maintain resting flow through the stenosis; there is no remaining reserve to increase flow during exercise. The mismatch between supply (capped by the stenosis) and demand (rising with exercise) causes ischemia and angina. Rest removes the increased demand, restoring the balance — the hallmark pattern of stable coronary artery disease."

- question: "Tachycardia (high heart rate) increases myocardial oxygen demand while simultaneously reducing the time available for coronary filling, creating a double threat to oxygen supply-demand balance."
  type: true-false
  answer: true
  explanation: "Each cardiac contraction consumes oxygen proportionally to the heart's work; more contractions per minute means higher total oxygen demand. Simultaneously, most coronary blood flow to the left ventricle occurs during diastole, when the myocardium relaxes and the intramural coronary vessels are no longer compressed. As heart rate increases, each cardiac cycle shortens — diastole shortens disproportionately more than systole. The result is less diastolic filling time per cycle. Tachycardia thus increases demand (more work) while decreasing supply (less coronary filling time) — both factors that determine ischemic risk move in opposite, unfavorable directions simultaneously."

- question: "Because the heart extracts such a high fraction of delivered oxygen, it can partially compensate for reduced coronary blood flow by simply extracting more from each unit of blood."
  type: true-false
  answer: false
  explanation: "The extraction reserve is nearly exhausted at baseline. Resting myocardium already takes 70–80% of delivered oxygen, leaving only 20–30% potentially available for increased extraction. Exercising skeletal muscle, by contrast, starts at ~25% extraction and can roughly triple that. The heart cannot meaningfully increase extraction — it is already operating near maximum. This constraint is precisely why coronary artery disease is so clinically significant: the heart has no backup extraction strategy when flow is limited. Any condition that restricts coronary blood flow — stenosis, spasm, thrombosis — rapidly produces ischemia because the extraction fallback is not available."

- question: "Why do local metabolic signals such as adenosine primarily control coronary vasodilation during exercise, rather than neural signals from the autonomic nervous system?"
  type: short-answer
  answer: "Neural control would be too slow and too coarse for the beat-by-beat precision that coronary regulation requires. The heart's oxygen demand varies continuously with heart rate and contractile force, and appropriate blood flow must track these changes within seconds. Metabolic signals — adenosine released from ATP-depleted myocytes, rising CO₂, falling oxygen tension — arise directly in the tissue that needs more blood and act locally on adjacent coronary arterioles almost immediately. This creates an intrinsic self-regulating feedback loop: increased work → increased ATP consumption → adenosine release → vasodilation → increased flow. The system does not need central nervous system involvement because signal and response are both local to the tissue."
  explanation: "This local metabolic regulation also explains coronary autoregulation — the maintenance of relatively constant flow over a wide range of systemic blood pressures (roughly 60–140 mmHg). If pressure rises, arterioles constrict to hold flow constant; if pressure falls, they dilate. This pressure-independent flow matching is a hallmark of metabolic regulation and protects the heart from both hypotension (by dilating) and hypertension (by preventing excess flow-induced damage). Coronary flow reserve — the 4–5 fold increase available during maximal vasodilation — is the clinical measure of how much of this capacity atherosclerosis has consumed."
```

## Explainer

From your cardiovascular overview, you know that the heart pumps blood to every organ in the body. But the heart itself is a muscle — a very hard-working one — and it needs its own blood supply. The **coronary arteries** are that supply, and they face a unique engineering problem: the organ they feed is the same organ whose contractions threaten to crush them shut. Understanding coronary circulation means understanding how the heart feeds itself despite this paradox.

The heart's metabolic demands are extraordinary. Even at rest, the myocardium extracts **70–80% of the oxygen** delivered to it — far more than skeletal muscle, which takes only about 25%. This near-maximal extraction has a critical consequence: when the heart needs more oxygen (during exercise, stress, or increased cardiac output), it cannot simply extract more from the existing blood flow. It has already taken almost everything available. Instead, the heart must **increase coronary blood flow itself** — it must dilate its coronary arteries to deliver a larger volume of oxygen-rich blood per minute. This is why coronary artery disease is so dangerous: atherosclerotic narrowing limits the vessel's ability to dilate, creating a ceiling on oxygen delivery that the heart may hit during exertion.

The timing of coronary flow is also unusual. During **systole** (ventricular contraction), the contracting myocardium compresses the coronary vessels embedded within it, especially in the left ventricle where wall pressures are highest. This compression physically squeezes blood out of the intramural vessels and impedes inflow. As a result, the majority of left coronary artery flow occurs during **diastole**, when the ventricular muscle relaxes and the compressed vessels spring open. The right ventricle, which generates much lower pressures, allows more continuous flow. This diastolic dependence explains why a rapid heart rate is a double threat: not only does tachycardia increase oxygen demand (more contractions per minute means more work), but it also shortens diastole — the very phase when most coronary filling occurs. The heart simultaneously needs more oxygen and has less time to receive it.

**Coronary autoregulation** ensures that flow matches demand across a wide range of conditions. The primary mechanism is metabolic: when myocardial cells consume more oxygen and ATP, they release **adenosine** and other metabolites that act as potent vasodilators on the smooth muscle of coronary arterioles. Low oxygen tension and increased CO₂ also directly relax vascular smooth muscle. The endothelium contributes by releasing **nitric oxide** in response to shear stress from flowing blood. Together, these mechanisms can increase coronary flow 4–5 fold above resting levels during intense exercise — a range called **coronary flow reserve**. When atherosclerosis narrows a coronary artery beyond about 70% of its diameter, resting flow may still be maintained (the autoregulatory mechanisms compensate by dilating downstream arterioles), but the reserve is exhausted. The vessel can no longer increase flow to meet the demands of exertion, producing the chest pain of **angina pectoris** — and if a plaque ruptures and occludes the vessel entirely, the result is myocardial infarction.
