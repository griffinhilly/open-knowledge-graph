---
id: disease-surveillance-systems
title: Disease Surveillance Systems and Data Quality
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: infectious-disease-surveillance
  type: hard
- id: outbreak-investigation
  type: soft
- id: information-bias-epidemiology
  type: soft
tags:
- surveillance-methods
- data-quality
- case-reporting
stage: advanced
status: draft
---

# Disease Surveillance Systems and Data Quality

## Core Idea
Public health surveillance systems monitor disease occurrence to detect outbreaks and guide control efforts through passive case reporting, active case finding, and sentinel surveillance strategies. System performance depends on sensitivity (ascertainment of true cases), specificity (avoiding false-positive reports), representativeness of reported cases, and timeliness of reporting. Surveillance data quality issues—underreporting, reporting delays, and case misclassification—substantially affect interpretation. Evaluating and improving surveillance requires understanding disease natural history and the multiple pathways leading to case identification.

## Questions

```yaml
- question: "During a viral outbreak, testing capacity expands significantly — more people are tested, including many with mild symptoms. Reported cases double over two weeks. Which interpretation is most epidemiologically defensible?"
  type: multiple-choice
  options:
    - "True incidence has doubled because the surveillance system is now capturing what was always there"
    - "True incidence has doubled because more testing always reveals previously hidden cases with equal probability"
    - "The observed increase may reflect expanded detection rather than increased true incidence — testing intensity changes the sample, not necessarily the population burden"
    - "The increase confirms the surveillance system was previously functioning well, since it detected the doubling"
  answer: 2
  explanation: "When testing expands, more mild cases enter the reported data — cases that existed before but fell out of the detection chain. This is differential ascertainment, not necessarily a true increase in incidence. Before attributing the doubling to epidemiological change, an epidemiologist must track testing volume and test positivity rates. If testing doubles but positivity stays constant, the ascertainment fraction has increased but true incidence may not have. Option A conflates ascertainment with incidence; option B incorrectly assumes equal detection probability across all testing scenarios."

- question: "A country uses passive surveillance to monitor influenza and consistently reports fewer cases than neighboring countries with active surveillance. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The country has genuinely lower influenza burden due to better public health practices"
    - "Passive surveillance has higher specificity, reducing false positives compared to active surveillance"
    - "Passive surveillance systematically underestimates incidence because case identification depends on patients seeking care and clinicians reporting"
    - "Active surveillance in neighboring countries overcounts through aggressive testing of mild cases"
  answer: 2
  explanation: "Passive surveillance depends on a chain: illness → care-seeking → clinical suspicion → testing → positive result → reporting. Cases fall out at every step, especially mild or asymptomatic infections that never prompt care-seeking. This is a predictable structural feature of passive systems, not a signal of lower burden. Active surveillance proactively finds cases, increasing sensitivity. Without additional evidence, option A is an unwarranted assumption; the structural difference in surveillance design is the parsimonious explanation."

- question: "Underreporting in passive surveillance systems is a data quality failure that, with better training and incentives, could be eliminated entirely."
  type: true-false
  answer: false
  explanation: "Underreporting is not primarily a data quality failure — it is a structural feature of passive surveillance. Even a perfectly compliant reporting system would miss cases where patients don't seek care, clinicians don't consider the diagnosis, or tests aren't available. Mild or asymptomatic infections will always be systematically underrepresented. Recognizing underreporting as a structural feature — rather than a correctable error — is essential for interpreting surveillance data correctly."

- question: "A surveillance system with high sensitivity but poor timeliness may fail to prevent outbreaks even if it eventually detects all cases."
  type: true-false
  answer: true
  explanation: "Timeliness is a critical performance attribute independent of sensitivity. A system that detects cases weeks after symptom onset provides little actionable information for outbreak control — by the time the signal is recognized, the window for early intervention has passed. Highly sensitive systems often require lab confirmation that introduces delays. Both sensitivity and timeliness must be adequate for surveillance to support a timely public health response; maximizing one often sacrifices the other."

- question: "Why can an apparent increase in reported cases during an outbreak reflect changes in surveillance behavior rather than true increases in incidence, and how should an epidemiologist distinguish between the two?"
  type: short-answer
  answer: "Surveillance data counts only cases that pass through the full detection chain. When testing expands or reporting incentives change, more mild cases are captured, inflating reported counts without any change in true incidence. An epidemiologist distinguishes these by tracking surveillance system attributes alongside case counts: testing volume, test positivity rates, case severity distribution, and reporting delays. If testing volume increases while positivity rates fall, the detection threshold has shifted toward milder cases. If severe cases remain constant while mild cases increase, ascertainment — not incidence — has changed."
  explanation: "This is the central interpretive challenge in surveillance epidemiology. Raw case counts are always a joint function of true epidemiology and surveillance behavior. Treating them as direct estimates of incidence leads to systematically wrong conclusions. The key habit is always to ask: could a change in detection explain this pattern before attributing it to a change in the pathogen or population?"
```

## Explainer

You know from infectious disease surveillance that population-level disease monitoring is distinct from clinical diagnosis — it is not about determining what is wrong with one patient, but about detecting patterns across thousands of people and events. The key design question for any surveillance system is: what proportion of true cases in the population will actually appear in the data? This proportion is the system's **sensitivity** (or ascertainment fraction), and it is almost always less than one. Most surveillance data represent not a count of all cases, but a *sample* — filtered through a chain of steps that determines who gets counted.

That filtering chain works like this: a person must (1) become infected or ill, (2) develop symptoms severe enough to seek care, (3) encounter a health-care provider who suspects the diagnosis, (4) have a test performed and the correct test ordered, (5) receive a positive result, and (6) have that result reported to public health authorities. At each step, cases fall out. Mild illnesses may never prompt care-seeking. Providers may not consider unusual diagnoses. Tests may not be available or may have imperfect sensitivity. Reporting may be incomplete or delayed. The result is **underreporting**, which is not a data quality failure in some simple sense — it is a predictable structural feature of passive surveillance that must be accounted for in interpretation.

**Passive** versus **active** surveillance represent a fundamental tradeoff. Passive reporting (clinicians and labs report cases to public health when they occur) is cheap and scalable but systematically underestimates incidence. **Active surveillance** — where public health officials proactively contact providers, labs, or households to search for cases — is more sensitive but resource-intensive. **Sentinel surveillance** finds a middle ground: a small network of high-quality reporting sites is used to monitor trends, even if it cannot capture total case counts. The choice among these strategies depends on the disease (severity, treatability), the surveillance objective (detect outbreaks vs. estimate burden), and available resources.

Your background in **information bias** is directly relevant here. Surveillance data are subject to **differential misclassification** when the likelihood of a case being detected or correctly classified varies across subgroups. Testing patterns are a classic driver: if testing intensity increases during an outbreak (more people get tested, so more mild cases are found), apparent incidence rises even if true incidence is flat. Conversely, if testing is concentrated in symptomatic hospitalized patients, the reported case fatality rate will be elevated because mild cases are not captured in the denominator. Before interpreting any surveillance trend, the epidemiologist must ask: could a change in detection explain this pattern?

Evaluating a surveillance system involves assessing several performance attributes: **sensitivity** (are true cases captured?), **specificity** (are false-positive reports minimized?), **representativeness** (does the detected sample reflect the true distribution by geography, age, severity?), **timeliness** (are cases detected early enough to allow response?), and **simplicity** (is the system operationally feasible?). These attributes often trade off — systems designed for maximum sensitivity frequently sacrifice simplicity and timeliness, and systems optimized for rapid reporting often miss less severe cases. Understanding these tradeoffs is what enables an epidemiologist to interpret surveillance data critically, rather than treating case counts as direct estimates of true incidence.

