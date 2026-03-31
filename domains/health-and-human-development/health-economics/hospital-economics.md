---
id: hospital-economics
title: Hospital Economics
domain: health-and-human-development
course: health-economics
prerequisites:
- id: healthcare-market-structure
  type: hard
- id: healthcare-financing
  type: soft
builds-toward:
- health-system-performance
tags:
- hospital
- DRG
- cost-shifting
- consolidation
- nonprofit
- capacity
stage: advanced
status: validated
---

# Hospital Economics

## Core Idea
Hospitals are the largest component of healthcare spending in most countries, and their economic behavior departs significantly from standard competitive markets. Hospitals have substantial fixed costs (buildings, equipment, staffing infrastructure), operate in markets with few competitors (especially in rural areas), and face complex payment systems (DRG-based prospective payment, per diem, fee-for-service, capitation). The hospital industry is characterized by an unusual nonprofit dominance (most US hospitals are nonprofit), persistent cross-subsidization (profitable services like orthopedics subsidize unprofitable ones like emergency care), and a trend toward consolidation that increases market power and prices. Hospital competition does not always reduce prices — in concentrated markets with insured patients, competition may occur on quality and amenities rather than price, a phenomenon that distinguishes healthcare from most other industries.

## Questions

```yaml
- question: "The DRG (Diagnosis-Related Group) payment system pays hospitals a fixed amount per admission based on the patient's diagnosis, regardless of actual costs incurred. What incentive does this create?"
  type: multiple-choice
  options:
    - "Hospitals are incentivized to provide as many services as possible during each admission"
    - "Hospitals are incentivized to minimize costs per admission (shorter stays, fewer tests) because they keep the difference between the DRG payment and actual costs — but may also be incentivized to upcode (classify patients into higher-paying DRGs) or discharge patients prematurely"
    - "DRGs eliminate all financial incentives because payment is fixed"
    - "Hospitals are incentivized to admit more patients regardless of medical necessity"
  answer: 1
  explanation: "DRG-based payment creates a powerful efficiency incentive: if the hospital can treat a patient for $8,000 when the DRG pays $10,000, it keeps the $2,000 margin. This has dramatically reduced average lengths of stay since DRGs were introduced (Medicare, 1983). The downsides are the incentive to reduce care below the appropriate level (premature discharge, skimping on tests), to upcode patients into higher-paying DRGs, and to avoid admitting patients whose expected costs exceed the DRG payment (cream-skimming). Quality monitoring and coding audits are the regulatory responses."

- question: "Hospital mergers and consolidation tend to increase prices for privately insured patients. This occurs because consolidated hospital systems have greater bargaining power with insurers."
  type: true-false
  answer: true
  explanation: "Decades of research consistently show that hospital mergers, particularly in already-concentrated markets, increase prices by 20-40% for privately insured patients without corresponding quality improvements. When a hospital is the only option in a region, insurers must include it in their network — patients demand access to the nearby hospital. This gives the hospital leverage to negotiate higher reimbursement rates. The result is higher premiums for the insured population. Antitrust enforcement has been inconsistent in blocking hospital mergers, partly because courts have accepted hospital efficiency claims that the economic evidence does not support."

- question: "Explain why most US hospitals are organized as nonprofits and whether their behavior differs meaningfully from for-profit hospitals."
  type: short-answer
  answer: "Nonprofit hospital status reflects the historical origin of hospitals as charitable institutions and the information asymmetry in healthcare — patients cannot easily evaluate care quality, so the nonprofit form signals that the institution is not motivated by profit extraction. Nonprofit hospitals receive tax exemptions in exchange for community benefit (charity care, medical education, research). Empirically, the behavioral differences are smaller than the organizational distinction suggests: nonprofit hospitals pursue revenue, accumulate surpluses, pay executives competitively, and respond to financial incentives similarly to for-profits. The main differences are in payer mix (nonprofits serve more uninsured patients) and the use of surpluses (reinvested rather than distributed to shareholders)."
  explanation: "The economic theory explaining nonprofit hospital prevalence is the 'contract failure' theory (Hansmann, 1980): when consumers cannot verify quality, they trust organizations that have no shareholders demanding profit maximization. Whether this trust is empirically justified is debated — studies find modest differences in quality, charity care, and pricing between nonprofit and for-profit hospitals, but the differences are not as large as the tax-exempt status would suggest."
```

## Explainer

Hospitals consume roughly one-third of healthcare spending in the US and similar proportions in other high-income countries. Understanding their economics is essential for understanding why healthcare costs rise and what policy levers might control them. Hospitals are not typical firms: they have enormous fixed costs, complex product lines (emergency, surgical, medical, obstetric, psychiatric services), and operate in markets where standard competitive dynamics often fail.

**Payment systems** shape hospital behavior more than any other factor. Under **fee-for-service**, hospitals are paid for each service provided — creating an incentive to do more. Under **DRG-based prospective payment**, hospitals receive a fixed amount per admission based on the diagnosis — creating an incentive to minimize costs per case. Under **capitation** or **global budgets**, hospitals receive a fixed amount per population served per year — creating an incentive to keep people out of the hospital entirely. Each system creates its own distortions: FFS encourages overtreatment, DRGs encourage undertreatment and gaming, and global budgets may lead to underfunding. Modern payment reform attempts to blend these incentives.

**Market structure** in the hospital industry has shifted dramatically toward consolidation. In the US, the number of independent hospitals has declined steadily as systems acquire competitors, forming regional or national chains. The economic evidence on consolidation is stark: hospital mergers in concentrated markets increase prices for privately insured patients by 20-40% on average, with negligible quality effects. The mechanism is increased bargaining power — a hospital that is the only option in a geographic market can demand higher reimbursement from insurers, who must include it in their network. This is one of the clearest examples in healthcare economics where market structure directly translates to higher costs.

The **nonprofit puzzle** is distinctive to hospitals. In most industries, nonprofits are a marginal presence. In the US hospital industry, they account for the majority of hospitals and beds. The economic explanation is that healthcare's information asymmetry makes patients more trusting of organizations without a profit motive. Empirically, however, the differences between nonprofit and for-profit hospitals are modest — both respond to financial incentives, both accumulate revenue over expenses, and both employ similar pricing strategies. The nonprofit tax exemption costs the public billions in foregone tax revenue, and whether the community benefit provided in return justifies this subsidy is an active policy debate.
