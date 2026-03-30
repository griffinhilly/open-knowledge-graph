---
id: maternal-mortality-prevention-multilevel
title: Maternal Mortality Prevention Framework
domain: health-and-human-development
course: public-health
prerequisites:
- id: disease-prevention-levels
  type: hard
- id: epidemiology-foundations
  type: hard
builds-toward:
- health-systems-and-financing
- global-burden-of-disease
tags:
- maternal-health
- prevention
- global-health
stage: advanced
status: validated
---

# Maternal Mortality Prevention Framework

## Core Idea
Maternal mortality prevention operates across three levels: primary prevention through contraception and family planning reducing unintended pregnancies; secondary prevention through prenatal care, skilled birth attendance, and facility delivery; tertiary prevention through emergency obstetric care for life-threatening complications. Different settings face different bottlenecks—remote areas often lack emergency infrastructure, while some urban areas have low contraception use. Effective strategies address locally identified barriers.

## How It's Best Learned
Analyze maternal mortality data for a country and identify which prevention level represents the greatest gap.

## Common Misconceptions
Assuming similar interventions work equally across settings—access to skilled providers differs dramatically from access to family planning.

## Questions

```yaml
- question: "A rural district has high maternal mortality. An audit finds that most deaths occur in women who reached the facility in time but died waiting for blood products or surgical intervention. Which prevention level and bottleneck should the program prioritize?"
  type: multiple-choice
  options:
    - "Primary prevention — the program should expand contraception access to reduce pregnancies in high-risk women"
    - "Secondary prevention — the program should train more skilled birth attendants for community-level delivery"
    - "Tertiary prevention — the program should strengthen emergency obstetric care capacity at the facility (blood products, surgical capability)"
    - "Secondary prevention — the program should improve prenatal screening to catch complications before labor"
  answer: 2
  explanation: "The three-delays model identifies three possible bottlenecks: delay in deciding to seek care, delay in reaching a facility, and delay in receiving adequate care once there. In this scenario, women are reaching the facility — so delays 1 and 2 are not the primary problem. Deaths are occurring because care at the facility is inadequate (missing blood products, no surgical capacity). This points directly to tertiary prevention — comprehensive emergency obstetric care (CEmOC). Interventions at the other prevention levels, however worthwhile in general, would not address the identified bottleneck and would likely not reduce mortality in this setting."

- question: "What makes skilled birth attendance the highest-impact secondary prevention intervention for maternal mortality, compared to traditional birth attendants?"
  type: multiple-choice
  options:
    - "Skilled birth attendants are more culturally trusted, increasing the likelihood that women choose facility delivery"
    - "Skilled birth attendants can manage postpartum hemorrhage with oxytocin, recognize complications, and make timely referrals — capabilities traditional birth attendants lack regardless of experience"
    - "Skilled birth attendants reduce the need for emergency obstetric care by preventing complications from occurring at all"
    - "Traditional birth attendants are equally capable for normal deliveries; skill only matters for high-risk pregnancies identified in prenatal care"
  answer: 1
  explanation: "70–80% of maternal deaths occur during or immediately after delivery. The critical interventions at this moment — administering oxytocin for postpartum hemorrhage, recognizing obstructed labor, performing or facilitating emergency referral — require clinical training and equipment. Traditional birth attendants, regardless of experience, cannot provide these. Experience with normal deliveries does not substitute for clinical competency with complications. This is why traditional birth attendant training programs historically had limited impact on maternal mortality rates, while scale-up of skilled birth attendance consistently shows mortality reductions. The skill gap is not about familiarity — it's about clinical capability at the moment of crisis."

- question: "Traditional birth attendants with extensive delivery experience can effectively substitute for clinically trained skilled birth attendants in resource-limited settings where skilled attendants are unavailable."
  type: true-false
  answer: false
  explanation: "Evidence consistently shows that traditional birth attendants (TBAs), regardless of experience, cannot substitute for clinically trained skilled birth attendants in preventing maternal death. The interventions that avert maternal mortality at the time of delivery — managing postpartum hemorrhage with uterotonics, recognizing and responding to eclampsia, performing or arranging emergency obstetric procedures — require clinical training that TBA experience does not provide. Large-scale evaluations of TBA training programs found no significant reductions in maternal mortality. This doesn't mean TBAs are without value (they provide support, recognize the need for referral, and are often the only present care), but they cannot prevent the cascade of fatal complications that clinical skill can interrupt."

- question: "Expanding access to contraception and family planning services constitutes primary prevention for maternal mortality because it reduces the incidence of the condition that causes death — pregnancy itself, specifically unintended or high-risk pregnancies."
  type: true-false
  answer: true
  explanation: "Primary prevention prevents the disease or condition from occurring in the first place. Maternal death requires a pregnancy; therefore preventing unintended pregnancies, high-parity births, adolescent pregnancies, and short-interval pregnancies directly prevents the exposure. This is particularly important because unsafe abortion — itself a major cause of maternal mortality in settings with restricted access — is almost entirely a consequence of unintended pregnancy. Contraception access is often underfunded relative to clinical interventions, yet it carries high population-level impact per dollar. Understanding it as primary prevention — not just family planning — clarifies its role in the mortality reduction framework."

- question: "Describe the three-delays model of maternal mortality and explain why identifying the dominant delay is essential before designing an intervention program."
  type: short-answer
  answer: "The three-delays model identifies three points where delay can convert a survivable obstetric complication into a death: (1) delay in deciding to seek care — due to financial barriers, lack of awareness of danger signs, cultural norms, or poor prior facility experiences; (2) delay in reaching a facility — due to distance, transport unavailability, or poor roads; and (3) delay in receiving adequate care once at the facility — due to absent staff, missing equipment, blood products, or surgical capacity. Each delay requires a different intervention: community education and financial support address delay 1; transport systems and maternity waiting homes address delay 2; facility capacity building addresses delay 3. Designing an intervention without identifying which delay dominates is why many programs fail — installing operating theatres in communities where women never reach them doesn't save lives, just as community mobilization in places where facilities lack blood products shifts deaths to a later point in the system."
  explanation: "The three-delays framework is a diagnostic tool as much as a classification system. Different settings have different bottleneck delays, and the same intervention bundle can succeed in one context and fail in another. Effective programs start with local data — auditing actual deaths to determine where the delay occurred — before selecting interventions."
```

## Explainer

From your study of disease prevention levels, you know that primary prevention stops disease before it occurs, secondary prevention detects and treats it early, and tertiary prevention limits harm once disease is established. Maternal mortality maps cleanly onto this framework, but with a crucial contextual layer: the same woman who experiences an obstetric complication may live or die depending on where she is — not just on the biology of the complication. This is why maternal mortality rates vary more than 100-fold between high-income and low-income countries despite the complications themselves (hemorrhage, sepsis, eclampsia, unsafe abortion) being broadly the same everywhere.

**Primary prevention** addresses a driver that is often underappreciated: unwanted or high-risk pregnancy. A pregnancy that doesn't occur cannot cause maternal death. Contraception access and family planning services reduce maternal mortality by reducing unintended pregnancies, high-parity births (risk compounds with each subsequent delivery), adolescent pregnancies (under 18 carry disproportionately high mortality), and short-interval pregnancies. In settings where contraception is inaccessible, unsafe abortion becomes a significant cause of maternal death — a preventable outcome that primary prevention directly addresses. This level of prevention is frequently underfunded relative to clinical interventions yet carries high population-level impact per dollar.

**Secondary prevention** — prenatal care and skilled birth attendance — interrupts the pathway from complication to death. Most obstetric complications are not fully preventable, but they are survivable if recognized early and managed correctly. Preeclampsia can be screened for and managed antenatally; gestational diabetes is identified through glucose testing; malpresentation can be detected before labor. Critically, 70–80% of maternal deaths occur during or just after delivery. A **skilled birth attendant** — one who can recognize abnormal labor, manage postpartum hemorrhage with oxytocin, and make a timely referral — represents the single highest-impact intervention at this level. Traditional birth attendants without clinical training cannot substitute here, regardless of their experience.

**Tertiary prevention** — emergency obstetric care — is the backstop when complications occur despite earlier efforts. Hemorrhage kills in minutes; eclamptic seizures can cause cerebral hemorrhage; sepsis progresses rapidly without antibiotics and surgical intervention. **Comprehensive emergency obstetric care (CEmOC)** requires blood products, surgical capability (for cesarean delivery), magnesium sulfate for eclampsia, and intravenous antibiotics. Delays in receiving this care account for the majority of preventable deaths, structured by the **three-delays model**: delay in deciding to seek care, delay in reaching a facility, and delay in receiving adequate care once there. Effective programs identify which delay dominates in the specific local context — remote areas typically face transport delays, while some urban areas have low care-seeking. The same intervention bundle that saves lives in one setting may be mismatched to the actual bottleneck in another.
