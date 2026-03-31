---
id: health-insurance-design
title: Health Insurance Design
domain: health-and-human-development
course: health-economics
prerequisites:
- id: moral-hazard-health-insurance
  type: hard
- id: adverse-selection-insurance
  type: hard
builds-toward:
- managed-care-economics
- universal-health-coverage-economics
tags:
- insurance-design
- deductible
- copay
- coinsurance
- VBID
- high-deductible
stage: advanced
status: validated
---

# Health Insurance Design

## Core Idea
Health insurance design involves structuring the financial relationship between the insurer and the insured to balance risk protection (the reason insurance exists), moral hazard control (reducing overconsumption of low-value care), and administrative feasibility. Key design elements include deductibles (patient pays the first N dollars), copayments (fixed dollar amount per service), coinsurance (patient pays a percentage of cost), and out-of-pocket maximums (caps total patient exposure). High-deductible health plans (HDHPs) reduce premiums and moral hazard but increase financial risk and may deter necessary care. Value-based insurance design (VBID) sets cost-sharing based on clinical value rather than cost — reducing barriers to high-value care while maintaining barriers to low-value care. Every design parameter trades off competing goals; the optimal design depends on the population's health, income, and the clinical value distribution of available services.

## Questions

```yaml
- question: "A high-deductible health plan ($3,000 deductible) reduces premiums and discourages low-value utilization. However, research shows that HDHPs also reduce the use of preventive services and chronic disease medications among low-income enrollees. Why?"
  type: multiple-choice
  options:
    - "Low-income enrollees do not understand the difference between preventive and non-preventive care"
    - "The deductible applies equally to all services, creating a financial barrier to both low-value and high-value care — low-income patients cannot afford to spend $3,000 before insurance kicks in, so they defer all care including necessary preventive care and chronic disease management"
    - "HDHPs are designed to reduce all utilization equally"
    - "Preventive services are not covered under HDHPs"
  answer: 1
  explanation: "This is the fundamental limitation of blunt cost-sharing: deductibles and copays do not distinguish between valuable and wasteful care. A patient who cannot afford the deductible will forgo a diabetes medication ($200/month) as readily as an unnecessary imaging study. The financial barrier falls hardest on low-income patients, who have the most to lose from deferred care. The ACA mitigated this by requiring first-dollar coverage of specified preventive services, but the general problem — cost-sharing reduces both appropriate and inappropriate utilization — remains."

- question: "Value-based insurance design (VBID) reduces copays for high-value services (e.g., statins for heart disease patients) and increases copays for low-value services (e.g., brand-name drugs with generic equivalents). How does this differ from traditional insurance design?"
  type: short-answer
  answer: "Traditional insurance design sets cost-sharing based on the cost of the service — more expensive services have higher copays. VBID sets cost-sharing based on the clinical value of the service for the specific patient — cost-sharing is low when evidence shows the service is highly beneficial (regardless of cost) and high when evidence shows limited benefit. This means a diabetic patient might pay nothing for their statin (high-value) while paying more for a marginal imaging study (low-value). Traditional design treats all services as if they have equal clinical value; VBID incorporates clinical evidence into the financial incentive structure."
  explanation: "The evidence on VBID is promising but still accumulating. Studies of reduced copays for chronic disease medications (statins, antihypertensives, diabetes drugs) show improved adherence with modest or neutral effects on total spending (medication costs rise but hospitalizations fall). The challenge is operationalizing 'clinical value' — it requires evidence review, clinical consensus, and IT infrastructure to implement condition-specific copay tiers."

- question: "An out-of-pocket maximum caps total patient spending in a year. Once the maximum is reached, insurance covers 100%. This feature protects against catastrophic costs but increases moral hazard for patients who hit the cap early in the year."
  type: true-false
  answer: true
  explanation: "Once a patient reaches the out-of-pocket maximum, their marginal cost for additional care drops to zero, eliminating any financial incentive to limit utilization. A patient who undergoes expensive surgery in January, hitting the $6,000 cap, faces zero cost for all subsequent care that year. This can increase utilization of discretionary services (elective procedures, specialist visits) in the remaining months. The tradeoff is intentional: the OOP max exists to prevent financial ruin from serious illness, accepting some moral hazard as the price of risk protection. The design challenge is setting the cap high enough to maintain cost-sharing for routine care but low enough to provide meaningful catastrophic protection."
```

## Explainer

Insurance design is the art of balancing three competing objectives. **Risk protection** demands low patient exposure — the whole point of insurance is to prevent financial catastrophe from illness. **Moral hazard control** demands high patient exposure — when patients pay more, they consume less low-value care. **Access** demands that cost-sharing not deter necessary care — a deductible that prevents a diabetic patient from filling their insulin prescription defeats the purpose of health coverage. Every design element represents a position on these tradeoffs.

**Deductibles** require the patient to pay the first N dollars of annual costs before insurance activates. This eliminates insurance claims for minor, routine expenses (reducing administrative costs and moral hazard) but exposes patients to significant upfront costs. A $3,000 deductible means a patient must pay $3,000 out of pocket before any insurance benefit. For a healthy person with rare medical expenses, this is a good deal (low premiums). For a chronically ill person with monthly medication costs, the deductible is a major financial burden that may cause medication non-adherence.

**Copayments** (fixed dollar amounts per service) and **coinsurance** (percentage of cost) apply at the point of service. A $30 copay per physician visit creates a predictable cost that discourages trivial visits. 20% coinsurance on a $10,000 procedure ($2,000 patient share) creates a proportional cost that scales with the expense. Both maintain patient "skin in the game" after the deductible is met. The **out-of-pocket maximum** caps annual patient spending, providing catastrophic protection regardless of how much care is needed — once the cap is reached, insurance covers 100%.

**Value-based insurance design** represents the frontier of insurance design thinking. Rather than applying uniform cost-sharing across all services, VBID adjusts cost-sharing based on the clinical value of the service for the specific patient. Medications with strong evidence of benefit for a given condition have low or zero copays; services with weak evidence or better alternatives have high copays. This aligns financial incentives with clinical evidence — patients are steered toward value, not away from all care indiscriminately. The conceptual elegance is clear; the implementation challenge is that clinical value varies by patient, condition, and context, requiring sophisticated systems to implement effectively.
