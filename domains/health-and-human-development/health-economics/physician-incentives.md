---
id: physician-incentives
title: Physician Payment and Incentives
domain: health-and-human-development
course: health-economics
prerequisites:
- id: healthcare-market-structure
  type: hard
- id: moral-hazard-health-insurance
  type: soft
builds-toward:
- managed-care-economics
- health-system-performance
tags:
- physician
- fee-for-service
- capitation
- salary
- supplier-induced-demand
- pay-for-performance
stage: advanced
status: validated
---

# Physician Payment and Incentives

## Core Idea
Physician payment methods create incentives that powerfully shape clinical behavior. Fee-for-service (FFS) pays per service delivered, incentivizing volume (more visits, more procedures, more tests). Capitation pays a fixed amount per enrolled patient per period, incentivizing efficiency but also potential underservice. Salary eliminates volume incentives but may reduce productivity. Supplier-induced demand — the physician's ability to generate demand for their own services by exploiting the information asymmetry with patients — is a uniquely important phenomenon in health economics, because the physician is simultaneously the patient's agent (advisor) and the supplier (provider). Pay-for-performance (P4P) attempts to align incentives with quality by tying payment to measurable outcomes or process measures, though evidence for its effectiveness is mixed.

## Questions

```yaml
- question: "When Medicare reduced reimbursement rates for certain physician services by 10%, physicians increased the volume of those services, partially offsetting the revenue loss. What economic concept does this illustrate?"
  type: multiple-choice
  options:
    - "Price elasticity of demand — lower prices increase demand"
    - "Supplier-induced demand — physicians, acting as both advisor and provider, recommended more services to maintain their income"
    - "Moral hazard — patients demanded more services at lower prices"
    - "The substitution effect — physicians switched to cheaper services"
  answer: 1
  explanation: "This is the classic evidence for supplier-induced demand (SID): when the price per service falls, physicians increase volume to compensate. In a standard market, a price cut reduces quantity supplied. In healthcare, the physician controls both the recommendation and the provision of the service, and can shift the patient's demand curve outward by recommending additional tests, follow-up visits, or procedures. The evidence for SID is strongest for procedures where physician discretion is high (elective surgery, imaging) and weakest where it is low (emergency care)."

- question: "A health system switches from fee-for-service to capitation for primary care physicians. What behavioral changes would economic theory predict?"
  type: short-answer
  answer: "Capitation pays a fixed amount per enrolled patient regardless of services provided, so the physician maximizes income by enrolling many patients and providing fewer services per patient. Predicted changes include shorter visits, fewer follow-up appointments, fewer referrals to specialists (since these represent costs the physician bears under full capitation), and more emphasis on prevention (which reduces future costly care). The risk is that capitation incentivizes underservice — skimping on necessary care to save costs — and cherry-picking healthy patients who require little care while avoiding complex, expensive patients."
  explanation: "The shift from FFS to capitation fundamentally changes the physician's marginal incentive from 'more services = more revenue' to 'more services = more cost.' Neither extreme is ideal: FFS overserves, capitation underserves. Blended payment models (a capitated base plus FFS bonuses for preventive care and quality targets) attempt to balance these competing incentives."

- question: "Pay-for-performance programs that tie physician bonuses to measurable quality indicators (e.g., percentage of diabetic patients with controlled HbA1c) have consistently produced large improvements in healthcare quality."
  type: true-false
  answer: false
  explanation: "The evidence on P4P is surprisingly disappointing. Most large-scale evaluations (including the UK's Quality and Outcomes Framework and US Medicare P4P programs) show modest or no improvements in quality, partly because the measured indicators capture a small fraction of what constitutes good care, physicians may focus on measured targets at the expense of unmeasured aspects (teaching to the test), and the financial incentives are often too small relative to physician income to change behavior. P4P works best when the target behavior is clearly defined, measurable, and under the physician's control, and when the incentive is financially meaningful."
```

## Explainer

The physician is the central decision-maker in healthcare — they decide what tests to order, what medications to prescribe, whether to recommend surgery, and when to refer to a specialist. Patients delegate these decisions because they lack the expertise to make them independently. This **agency relationship** means that physician payment methods have outsized effects on healthcare utilization, cost, and quality — far more than in industries where the consumer makes independent purchasing decisions.

**Fee-for-service** is the most common payment method globally and the simplest: do more, earn more. A physician paid per visit has an incentive to schedule more visits. A surgeon paid per procedure has an incentive to recommend surgery over watchful waiting. This volume incentive has been identified as a major driver of healthcare cost growth, particularly in the US, where FFS dominates and physician incomes are among the highest in the world. The phenomenon of **supplier-induced demand** — where physicians generate demand for their own services by leveraging information asymmetry — is most acute under FFS. The evidence is compelling: when fee schedules are cut, physicians increase volume; regions with more physicians have more per-capita utilization without better outcomes.

**Capitation** inverts the incentive. A physician paid $100 per month per enrolled patient earns the same whether the patient visits zero times or ten times. The marginal service is now a cost, not a revenue source. This creates efficiency: capitated physicians order fewer tests, make fewer referrals, and emphasize prevention. But it also creates the risk of **underservice** — withholding beneficial care to save costs — and **cream-skimming** — attracting healthy patients and avoiding sick ones. The HMO backlash of the 1990s was driven partly by patient perception (often justified) that capitated physicians were denying necessary care.

Modern payment reform recognizes that no single method perfectly aligns physician incentives with patient welfare. **Blended models** combine a capitated base (for efficiency) with FFS components for preventive services and quality bonuses (for access and quality). **Accountable Care Organizations** give physician groups shared savings when they reduce total spending below a benchmark while maintaining quality. **Bundled payments** cover an entire episode of care (e.g., hip replacement from surgery through rehabilitation) at a fixed price, incentivizing coordination across providers. Each of these represents an attempt to balance the fundamental tension between paying for volume (FFS) and paying for value (outcomes-based payment).
