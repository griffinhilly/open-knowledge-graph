---
id: managed-care-economics
title: Economics of Managed Care
domain: health-and-human-development
course: health-economics
prerequisites:
- id: health-insurance-design
  type: hard
- id: physician-incentives
  type: soft
- id: moral-hazard-health-insurance
  type: soft
builds-toward:
- health-system-performance
tags:
- managed-care
- HMO
- PPO
- gatekeeping
- utilization-review
- network
stage: advanced
status: validated
---

# Economics of Managed Care

## Core Idea
Managed care organizations (MCOs) integrate the financing and delivery of healthcare to control costs while maintaining quality. Unlike traditional indemnity insurance (which pays any provider any amount), MCOs use provider networks (selective contracting with physicians and hospitals at negotiated rates), gatekeeping (requiring primary care referrals for specialist access), utilization review (prior authorization, concurrent review, retrospective audit of clinical decisions), and financial incentives (capitation, risk-sharing) to manage the volume and cost of care. HMOs (Health Maintenance Organizations) use the tightest controls (closed networks, mandatory gatekeeping, capitation). PPOs (Preferred Provider Organizations) offer broader networks and direct specialist access at higher cost-sharing. The managed care revolution of the 1990s slowed US healthcare cost growth but generated a political backlash driven by perceived restrictions on patient choice and physician autonomy.

## Questions

```yaml
- question: "Managed care plans negotiate discounted rates with a network of providers. A hospital that refuses the discounted rate is excluded from the network. Why does this give managed care plans bargaining power?"
  type: multiple-choice
  options:
    - "Patients will go to any hospital regardless of network status"
    - "Exclusion from the network means losing access to the plan's enrolled population — the threat of lost patient volume gives the MCO leverage to negotiate lower prices"
    - "Hospitals prefer lower prices because they attract more patients"
    - "Network exclusion is illegal under antitrust law"
  answer: 1
  explanation: "The selective contracting mechanism gives MCOs bargaining power that individual patients or traditional insurers lack. A hospital excluded from a major MCO's network loses access to thousands of potential patients who face higher out-of-pocket costs for out-of-network care and will therefore choose in-network alternatives. The threat of this volume loss gives the MCO leverage to negotiate rates below what the hospital charges fee-for-service patients. This is the primary mechanism through which managed care controls prices — it is a demand-side counterweight to provider market power."

- question: "The managed care backlash of the late 1990s was driven primarily by patient and physician dissatisfaction with utilization restrictions, not by evidence that managed care produced worse health outcomes."
  type: true-false
  answer: true
  explanation: "The evidence on managed care quality is mixed but does not support the narrative of systematically worse outcomes. Large studies (including comparisons of HMO and FFS Medicare populations) found similar or slightly better outcomes under managed care for most conditions. The backlash was driven by perceived restrictions: prior authorization denials, narrow networks excluding preferred physicians, and the sense that financial considerations were overriding clinical judgment. The backlash led to 'patients' bill of rights' legislation and the shift from tight HMOs to looser PPOs, effectively trading cost control for patient choice."

- question: "Explain the economic logic of gatekeeping (requiring a primary care referral before seeing a specialist) and why it can both improve and reduce quality of care."
  type: short-answer
  answer: "Gatekeeping reduces costs by filtering out unnecessary specialist visits — the primary care physician can handle most conditions at lower cost and refers only when specialist expertise is genuinely needed. This can improve care coordination (the PCP knows the whole patient) and reduce fragmentation. However, gatekeeping can reduce quality when it delays necessary specialist care — a patient with early symptoms of a serious condition might be managed by a PCP who lacks the expertise to diagnose it promptly. The net effect depends on the quality of the primary care system: strong primary care makes gatekeeping beneficial; weak primary care makes it a barrier."
  explanation: "Countries with strong primary care traditions (UK, Netherlands) use gatekeeping effectively, with PCPs managing 85-90% of patient encounters without specialist referral. In the US, where specialist culture is stronger and patients expect direct access, gatekeeping generated significant resistance. The economic principle is that gatekeeping is a form of rationing that can be efficient (reducing low-value specialist visits) or harmful (delaying high-value specialist care), depending on implementation."
```

## Explainer

Traditional health insurance operates passively: the patient chooses any provider, receives any service the physician orders, and the insurer pays the bill. This arrangement maximizes patient choice and physician autonomy but provides no mechanism to control costs, evaluate necessity, or coordinate care. **Managed care** intervenes in all three areas, fundamentally changing the relationship between insurers, providers, and patients.

The core economic strategy of managed care is **selective contracting**. Instead of paying any willing provider, MCOs negotiate contracts with a limited network of providers at discounted rates. Hospitals and physicians accept lower per-unit prices in exchange for patient volume — being "in-network" channels the MCO's enrolled population toward them. Patients face higher cost-sharing or no coverage for out-of-network care, steering them toward contracted providers. This creates bargaining power that traditional insurance lacks: a large MCO can credibly threaten to exclude a hospital from its network, while individual patients cannot.

**Utilization management** is the second pillar. **Prior authorization** requires the insurer's approval before certain services (expensive imaging, elective surgery, specialty drugs) are delivered. **Concurrent review** monitors ongoing care (e.g., hospital length of stay) against evidence-based guidelines. **Retrospective review** audits claims after the fact to identify patterns of overutilization. These mechanisms directly intervene in clinical decision-making — the MCO's medical director or algorithms override or question the treating physician's judgment, which is the primary source of physician and patient dissatisfaction.

The HMO model represents the tightest integration: capitated payment to physicians, mandatory primary care gatekeeping, closed networks, and strong utilization review. The PPO model is looser: fee-for-service with negotiated discounts, no mandatory gatekeeper, and broader networks with graduated cost-sharing (lower for in-network, higher for out-of-network). The evolution from HMOs to PPOs over the 1990s and 2000s reflected the market's revealed preference: consumers were willing to pay higher premiums for greater choice and fewer restrictions. Current trends are moving back toward managed care principles under different labels — Accountable Care Organizations, narrow networks on ACA exchanges, and value-based contracts all use the same economic tools (selective contracting, utilization management, aligned incentives) in updated packaging.
