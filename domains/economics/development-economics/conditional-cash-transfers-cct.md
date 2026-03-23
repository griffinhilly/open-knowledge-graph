---
id: conditional-cash-transfers-cct
title: Conditional Cash Transfers and Social Policy
domain: economics
course: development-economics
prerequisites:
- id: human-capital-accumulation-development
  type: hard
- id: randomized-experiments-development
  type: soft
tags:
- CCT
- social-policy
stage: expert
status: validated
---

# Conditional Cash Transfers and Social Policy

## Core Idea
Conditional Cash Transfers (CCTs) provide cash to poor households contingent on behaviors like school attendance or health checkups, directly addressing poverty while creating human capital investment incentives. Mexico's Progresa and Brazil's Bolsa Família became flagship programs. Randomized evidence shows CCTs increase enrollment and health utilization; long-run income effects remain under evaluation.

## Questions

```yaml
- question: "A government replaces its CCT program (which conditions payments on school attendance) with an unconditional cash transfer of equal size. Based on the evidence from programs like Progresa and Bolsa Família, which outcome is most likely?"
  type: multiple-choice
  options:
    - "Health and nutrition outcomes would stay roughly the same, but school enrollment might fall — conditionality matters more for attendance than for health behaviors"
    - "All outcomes would improve because households now have more flexibility and no monitoring burden"
    - "School enrollment would increase further because removing conditions reduces resentment and increases program take-up"
    - "All outcomes would fall substantially, because the conditions are the primary driver of all behavioral changes in CCT programs"
  answer: 0
  explanation: "Evidence suggests that for health and nutrition outcomes, unconditional cash transfers often perform similarly to CCTs — households tend to spend more on food and basic health care when income rises, regardless of conditions. But for school attendance, conditionality appears to make a meaningful difference. Older children who attend school cannot simultaneously work, so the opportunity cost of attendance is high. The condition directly offsets this cost and creates a clear incentive. Removing it could reduce attendance among households where child labor income is significant."

- question: "A government implements a well-funded CCT program requiring school attendance in a rural region. Evaluators find that after two years, enrollment has increased but test scores and literacy have not improved. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The cash transfers are too small to offset the opportunity cost of schooling"
    - "The conditions are being monitored too strictly, creating perverse incentives"
    - "The program is a demand-side intervention but the schools lack sufficient teachers, materials, or quality — the supply side remains broken"
    - "CCT programs are only effective for health outcomes, not for education"
  answer: 2
  explanation: "CCTs are demand-side interventions: they make it financially feasible and incentivized for families to send children to school. But if the supply side is inadequate — too few teachers, overcrowded classrooms, poor materials — increased attendance does not translate into human capital gains. Getting children through the school door is a necessary but not sufficient condition for learning. This is called the supply-side constraint, and it is one of the core limitations of CCTs as a standalone policy."

- question: "CCT programs typically transfer cash to mothers rather than fathers because evidence suggests maternal control of household resources leads to better outcomes for children."
  type: true-false
  answer: true
  explanation: "True. A consistent finding in development economics is that money controlled by mothers is more likely to be spent on children's nutrition, health, and schooling than money controlled by fathers. Programs like Progresa explicitly designed transfers to be received by mothers based on this evidence, and evaluations have confirmed better child outcomes under this design. This is not merely an assumption but an empirically validated feature of CCT program architecture."

- question: "The primary purpose of the conditions in CCT programs is to ensure recipients work toward self-sufficiency so they eventually no longer need government transfers."
  type: true-false
  answer: false
  explanation: "False. The conditions — school attendance, health checkups, nutrition workshops — are not designed to test self-sufficiency or create a path off the program. They are designed to offset the opportunity cost of human capital investments (especially child labor income foregone when children attend school) and to steer additional income toward behaviors that build long-run productivity. The conditions change investment decisions, not program duration. A secondary function noted in the literature is political: conditions make transfers to the poor more acceptable to legislators who might oppose unconditional 'free money,' but this is a political economy rationale, not the program's developmental purpose."

- question: "Why might conditionality on school attendance matter more for enrollment outcomes than conditionality on health checkup visits, even if both behaviors are valuable investments in human capital?"
  type: short-answer
  answer: "School attendance carries a high and direct opportunity cost: children who attend school full-time cannot simultaneously engage in paid labor or household production. For families near subsistence, this forgone income can make schooling unaffordable even when parents genuinely value education. The attendance condition, combined with cash calibrated to offset that opportunity cost, makes staying in school financially viable. Health checkup visits typically involve lower opportunity costs — they are infrequent and do not preclude work — and households tend to spend more on basic health care whenever income rises, regardless of formal conditions. So the incremental behavioral impact of conditionality is larger where the opportunity cost is higher."
  explanation: "This distinction explains why the evidence shows UCTs and CCTs perform similarly on health and nutrition metrics but diverge on school enrollment, particularly for older children and adolescents where the labor market opportunity cost of attendance is greatest. It also explains the program design choice of calibrating the cash amount to the grade level and to gender-specific dropout risk, since the opportunity cost varies systematically along these dimensions."
```

## Explainer

From your study of human capital accumulation, you know that education and health are investments: they cost resources today but yield higher productivity and earnings in the future. Poor households often underinvest in these areas — not because parents do not value their children's futures, but because they face binding constraints. School fees, lost child labor income, and the cost of clinic visits make human capital investments unaffordable or too risky when families live near subsistence. **Conditional cash transfers** attack this problem from both sides at once: the cash relaxes the budget constraint, and the conditionality steers spending toward human capital.

The basic CCT design is straightforward. Eligible households (identified through a poverty targeting mechanism) receive regular cash payments — typically to the mother — provided they meet conditions such as keeping children enrolled in school with minimum attendance rates (usually 80–85%), bringing children for regular health checkups, or attending nutrition workshops. The cash amount is usually calibrated to offset the opportunity cost of the required behavior. Mexico's **Progresa** (later Oportunidades, now Prospera) pioneered this structure in 1997, providing differentiated payments that increased with grade level and were higher for girls, who faced greater dropout risk.

The randomized evaluation of Progresa became one of the most influential studies in development economics, demonstrating the power of the experimental methods you studied. By randomly phasing in the program across villages, researchers could compare treatment and control groups cleanly. Results showed enrollment increases of 3–4 percentage points for primary school and larger gains for secondary school, increased use of preventive health services, and improved child nutrition. Brazil's **Bolsa Família**, which eventually covered over 50 million people, showed similarly positive results at massive scale, contributing to a significant decline in Brazilian inequality during the 2000s.

A central debate in CCT design is whether the **conditions actually matter** or whether the cash alone would produce the same outcomes. Unconditional cash transfers (UCTs) are cheaper to administer because they require no monitoring infrastructure. Some evidence suggests that for health and nutrition outcomes, UCTs perform nearly as well — households that receive money tend to spend more on food and health regardless of conditions. But for schooling, where the opportunity cost of attendance is high (especially for teenagers who could be working), conditionality appears to make a meaningful difference. The conditions may also provide political cover, making transfers to the poor more acceptable to taxpayers and legislators who might resist "free money."

CCTs are not without limitations. They require functioning schools and health clinics — transferring cash to send children to school accomplishes little if the school has no teachers or materials. This is a **supply-side constraint** that CCTs, as demand-side interventions, cannot address alone. Long-run evidence on whether CCT recipients earn more as adults is still accumulating, with early results from Mexico showing modest but positive effects on labor market outcomes a decade later. The broader lesson from CCTs is that well-designed programs can simultaneously reduce current poverty and build future human capital, but they work best as part of a package that also addresses the quality and availability of public services.
