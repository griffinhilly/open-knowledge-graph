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

## Explainer

You know from infectious disease surveillance that population-level disease monitoring is distinct from clinical diagnosis — it is not about determining what is wrong with one patient, but about detecting patterns across thousands of people and events. The key design question for any surveillance system is: what proportion of true cases in the population will actually appear in the data? This proportion is the system's **sensitivity** (or ascertainment fraction), and it is almost always less than one. Most surveillance data represent not a count of all cases, but a *sample* — filtered through a chain of steps that determines who gets counted.

That filtering chain works like this: a person must (1) become infected or ill, (2) develop symptoms severe enough to seek care, (3) encounter a health-care provider who suspects the diagnosis, (4) have a test performed and the correct test ordered, (5) receive a positive result, and (6) have that result reported to public health authorities. At each step, cases fall out. Mild illnesses may never prompt care-seeking. Providers may not consider unusual diagnoses. Tests may not be available or may have imperfect sensitivity. Reporting may be incomplete or delayed. The result is **underreporting**, which is not a data quality failure in some simple sense — it is a predictable structural feature of passive surveillance that must be accounted for in interpretation.

**Passive** versus **active** surveillance represent a fundamental tradeoff. Passive reporting (clinicians and labs report cases to public health when they occur) is cheap and scalable but systematically underestimates incidence. **Active surveillance** — where public health officials proactively contact providers, labs, or households to search for cases — is more sensitive but resource-intensive. **Sentinel surveillance** finds a middle ground: a small network of high-quality reporting sites is used to monitor trends, even if it cannot capture total case counts. The choice among these strategies depends on the disease (severity, treatability), the surveillance objective (detect outbreaks vs. estimate burden), and available resources.

Your background in **information bias** is directly relevant here. Surveillance data are subject to **differential misclassification** when the likelihood of a case being detected or correctly classified varies across subgroups. Testing patterns are a classic driver: if testing intensity increases during an outbreak (more people get tested, so more mild cases are found), apparent incidence rises even if true incidence is flat. Conversely, if testing is concentrated in symptomatic hospitalized patients, the reported case fatality rate will be elevated because mild cases are not captured in the denominator. Before interpreting any surveillance trend, the epidemiologist must ask: could a change in detection explain this pattern?

Evaluating a surveillance system involves assessing several performance attributes: **sensitivity** (are true cases captured?), **specificity** (are false-positive reports minimized?), **representativeness** (does the detected sample reflect the true distribution by geography, age, severity?), **timeliness** (are cases detected early enough to allow response?), and **simplicity** (is the system operationally feasible?). These attributes often trade off — systems designed for maximum sensitivity frequently sacrifice simplicity and timeliness, and systems optimized for rapid reporting often miss less severe cases. Understanding these tradeoffs is what enables an epidemiologist to interpret surveillance data critically, rather than treating case counts as direct estimates of true incidence.

