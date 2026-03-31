---
id: equity-in-healthcare
title: Equity in Healthcare
domain: health-and-human-development
course: health-economics
prerequisites:
- id: healthcare-market-structure
  type: hard
- id: healthcare-financing
  type: soft
builds-toward:
- universal-health-coverage-economics
tags:
- equity
- horizontal-equity
- vertical-equity
- social-determinants
- health-disparities
- concentration-index
stage: advanced
status: validated
---

# Equity in Healthcare

## Core Idea
Equity in healthcare encompasses two distinct principles: horizontal equity (equal treatment for equal need — people with the same health condition should receive the same care regardless of income, race, or geography) and vertical equity (appropriately unequal treatment for unequal need — sicker people should receive more care). Health inequity is the systematic, avoidable, and unjust difference in health outcomes or healthcare access between population groups. Health economics measures equity through concentration indices (plotting the cumulative share of health or healthcare against the cumulative share of the population ranked by income), benefit incidence analysis (who actually receives publicly funded healthcare?), and decomposition of health inequalities into contributing factors. The distinction between inequality (any observable difference) and inequity (differences that are unfair and avoidable) is normative — it requires a value judgment about what differences are unjust.

## Questions

```yaml
- question: "Two patients with identical symptoms of appendicitis present to different hospitals. Patient A (high-income, insured) receives surgery within 2 hours. Patient B (low-income, uninsured) waits 8 hours in the emergency department. This violates which equity principle?"
  type: multiple-choice
  options:
    - "Vertical equity — the patients have equal need but should receive different treatment"
    - "Horizontal equity — patients with equal need should receive equal treatment regardless of their socioeconomic characteristics"
    - "No equity principle is violated — faster service for paying customers is normal market behavior"
    - "Allocative efficiency — resources are not being used optimally"
  answer: 1
  explanation: "Horizontal equity requires equal treatment for equal need. Both patients have the same clinical condition (appendicitis) and the same need for surgery, but they receive different treatment because of their income and insurance status. This is a paradigmatic violation of horizontal equity. The market-based defense (option C) illustrates why healthcare is not treated as a normal market good in most societies — the principle that access should be based on need, not ability to pay, is foundational to health equity."

- question: "The concentration index for healthcare utilization in a country is -0.15. This means healthcare utilization is concentrated among the poor (pro-poor distribution). Does this indicate an equitable system?"
  type: multiple-choice
  options:
    - "Yes — any negative concentration index indicates equity"
    - "Not necessarily — if the poor are sicker (greater need), a pro-poor distribution of utilization may simply reflect horizontal equity (equal care for equal need). A truly equitable system would have a need-adjusted concentration index near zero"
    - "No — utilization should be equally distributed regardless of income"
    - "Yes — the poor should always receive more healthcare"
  answer: 1
  explanation: "Raw utilization distributions must be interpreted relative to need. The poor generally have worse health and greater healthcare needs. A concentration index of -0.15 might reflect that the poor use slightly more healthcare — but if their need is substantially greater (concentration index of need = -0.30), they may actually be receiving less care relative to their need. The horizontal equity index compares actual utilization to need-predicted utilization, adjusting for the fact that equal utilization is not equitable if need is unequal."

- question: "Explain why the distinction between health inequality and health inequity is normative rather than empirical."
  type: short-answer
  answer: "Health inequality is any measurable difference in health outcomes between groups — it is a descriptive, factual statement (men die younger than women, rural residents have higher mortality). Health inequity adds a value judgment: the difference is unjust, avoidable, and caused by systemic social disadvantage. Whether a specific inequality is an inequity depends on the cause: if men die younger partly due to biology, that is an inequality but arguably not an inequity. If Black Americans have higher infant mortality due to structural racism and unequal access to care, that is an inequity. The distinction requires normative reasoning about what differences are morally unacceptable, which cannot be settled by data alone."
  explanation: "This distinction matters for policy: not all health inequalities require policy intervention (we do not expect to equalize biological sex differences in lifespan), but health inequities demand action because they result from unjust social arrangements. The WHO Commission on Social Determinants of Health (2008) defined health inequities as differences in health 'which are not only unnecessary and avoidable but, in addition, are considered unfair and unjust.'"
```

## Explainer

Equity is a core value in health economics — distinct from efficiency and sometimes in tension with it. An efficient allocation maximizes total health from available resources; an equitable allocation ensures fair distribution of health and healthcare across population groups. A perfectly efficient system could concentrate all resources on the patients who benefit most per dollar, which might systematically favor the wealthy, educated, and urban populations who are easier and cheaper to treat. Equity constraints force the system to also serve hard-to-reach, expensive-to-treat, and disadvantaged populations.

**Horizontal equity** (equal treatment for equal need) is the most widely accepted equity principle. It means that two patients with the same condition should receive the same quality and timeliness of care regardless of income, insurance status, race, gender, geography, or other non-clinical characteristics. Violations are pervasive: studies consistently show that racial minorities receive less aggressive treatment for cardiac disease, less pain management, and lower-quality surgical care than white patients with identical conditions. Income-based disparities in access, wait times, and treatment quality are documented in every country, including those with universal coverage.

**Vertical equity** (appropriately unequal treatment for unequal need) requires that sicker people receive more care — a principle that sounds obvious but is violated when cost-sharing deters the poor and chronically ill from seeking care, when rural populations lack access to specialist services, or when insurance benefits are structured to favor healthy enrollees. Progressive financing (those with higher income contributing proportionally more) is a vertical equity principle applied to the funding side.

Measuring equity requires both data and normative choices. The **concentration index** is the standard tool: it plots the cumulative share of healthcare utilization (or health outcomes) against the cumulative share of the population ranked by income. A concentration index of zero indicates equal distribution; positive values indicate concentration among the rich; negative values indicate concentration among the poor. But raw utilization data must be adjusted for need — if the poor are sicker, equal utilization represents inequity (they need more care than they are receiving). The **horizontal inequity index** adjusts for need, revealing whether the system provides equal care for equal need or systematically favors particular income groups.
