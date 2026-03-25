---
id: school-attendance-and-incentives
title: School Attendance, Incentives, and Learning
domain: economics
course: development-economics
prerequisites:
- id: human-capital-accumulation-development
  type: hard
- id: cash-transfers-and-incentives
  type: soft
tags:
- education
- incentives
- attendance
stage: expert
status: validated
---

# School Attendance, Incentives, and Learning

## Core Idea
Reducing school costs (eliminating user fees, providing transport, meals) increases enrollment. CCTs tied to attendance or health checkups further boost attendance. However, attendance ≠ learning; quality of instruction, teacher effort, and curriculum matter. Some interventions increase attendance without improving test scores, suggesting quality constraints are binding in many countries.

## Questions

```yaml
- question: "A government in a low-income country introduces a conditional cash transfer (CCT) program that pays families for each day their child attends school. After three years, school attendance rises from 60% to 90%, but standardized test scores remain flat. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The CCT was too small to change behavior meaningfully; families only sent children to collect the payment without caring about education"
    - "Attendance was not the binding constraint — quality-side factors like teacher absenteeism, poor curriculum, or overcrowded classrooms are limiting learning even with higher attendance"
    - "Test scores are a lagging indicator; learning gains will appear in 5–10 years once the cohort matures"
    - "CCTs are ineffective at changing school attendance; the rise must reflect other concurrent reforms"
  answer: 1
  explanation: "This scenario illustrates the attendance-learning gap, the central insight of this topic. CCTs work as designed — they successfully changed the household cost-benefit calculation and increased attendance. But attendance is a necessary, not sufficient, condition for learning. If the school's instructional quality is poor (teacher absenteeism, rote pedagogy, curriculum mismatched to student level), children sitting in desks will not learn. Option C is tempting but ignores the vast empirical evidence that three years of attendance with no test score gains signals a supply-side constraint, not just a measurement lag."

- question: "Which of the following best describes the 'opportunity cost' that prevents poor families from sending children to school, even when schooling is officially free?"
  type: multiple-choice
  options:
    - "The psychological cost of children being separated from their parents during school hours"
    - "The value of children's time in productive activities — farm work, childcare, fetching water — that must be given up for school attendance"
    - "The direct cost of textbooks and uniforms, which are always required even when tuition fees are eliminated"
    - "The risk that children will develop preferences for urban life and leave the family farm"
  answer: 1
  explanation: "Opportunity cost here is the economic value of what is sacrificed when a child attends school rather than working. For poor families near subsistence, children are economically productive — they assist in farming, care for younger siblings, haul water. The lost labor value often exceeds the forgone tuition in terms of household impact. This is why simply eliminating fees (which removes direct costs) is necessary but sometimes insufficient — cash transfers address the opportunity cost by compensating families for the child's foregone labor. Option C is partially true in some contexts but is a direct cost, not an opportunity cost."

- question: "Eliminating school user fees in developing countries has been shown to increase school enrollment."
  type: true-false
  answer: true
  explanation: "This is well-supported by evidence. When Uganda abolished primary school fees in 1997, enrollment roughly doubled. Similar effects were seen in Kenya and other countries. Direct costs (fees, uniforms, books) are real barriers for poor households. Removing them shifts the household cost-benefit calculation in favor of attendance. The effect is particularly large for girls, secondary school students, and the poorest households, who face the tightest budget constraints."

- question: "A program that successfully increases school attendance rates can be considered a successful education intervention, since attending school is how children acquire skills."
  type: true-false
  answer: false
  explanation: "This is the core misconception this topic addresses. Attendance is necessary but not sufficient for learning. The attendance-learning gap — documented extensively in India, Kenya, Pakistan, and elsewhere — shows that many children who attend school for years remain unable to read or do basic arithmetic. When supply-side quality constraints are binding (poor teachers, inappropriate curriculum, overcrowding), sitting in a classroom produces little learning. A truly successful education intervention must address both why children don't attend AND what they learn when they do. Evaluating only attendance metrics misses half the problem."

- question: "Why might a program that dramatically increases school attendance fail to improve student learning outcomes, and what would a more complete intervention look like?"
  type: short-answer
  answer: "Attendance gets children into seats but does nothing about what happens once they are there. If teachers are frequently absent, if the curriculum is pitched far above students' actual skill level, or if classrooms have 60+ students with rote instruction, attendance produces little learning. A complete intervention must address supply-side quality: teacher accountability and training, teaching-at-the-right-level curricula matched to student ability, and instructional methods that produce genuine comprehension rather than memorization."
  explanation: "The key insight is that education production requires inputs on both the demand side (children present) and the supply side (effective instruction). Demand-side programs like CCTs, fee elimination, and school meals are often easier to design and implement because they work through financial transfers. Supply-side reforms — improving teacher quality, restructuring curriculum, creating accountability — are harder and slower but necessary for learning. Development economists now distinguish 'access' interventions (do children attend?) from 'quality' interventions (do they learn?), and evidence increasingly shows quality is the binding constraint in many low-income countries."
```

## Explainer

From your study of human capital in development, you know that education is one of the highest-return investments a poor household can make — each additional year of schooling is associated with 8–13% higher adult earnings in developing countries. From your understanding of cash transfers and incentives, you know that financial barriers and behavioral nudges can powerfully shape household decisions. School attendance sits at the intersection of these ideas: it is the mechanism through which education investments are supposed to generate returns, but getting children consistently into classrooms turns out to be a more complex problem than simply building schools.

The **demand-side barriers** to school attendance are well documented. Direct costs include fees, uniforms, books, and transport. Indirect costs — the **opportunity cost** of a child's time — are often larger: children who attend school cannot work in the family farm, tend livestock, fetch water, or care for younger siblings. For poor families living close to subsistence, pulling a child out of productive work to attend school is a genuine economic sacrifice whose returns are uncertain and distant. Programs that reduce these costs have consistently increased enrollment: eliminating user fees in Uganda and Kenya produced dramatic enrollment surges, free school meals programs in India boosted attendance by 10–15%, and deworming programs (which reduce illness-related absenteeism) increased attendance in Kenya by roughly 7 percentage points.

**Conditional Cash Transfers** tied to attendance represent a more targeted approach. By paying families directly for keeping children in school, CCTs change the household's cost-benefit calculation: the immediate financial reward of attendance offsets the opportunity cost of lost child labor. Mexico's Progresa program increased secondary enrollment by 5–8 percentage points, with larger effects for girls, who faced higher baseline dropout rates. But the evidence reveals an important subtlety: attendance is a necessary but not sufficient condition for learning. Programs that successfully get children into seats do not automatically produce educated children.

This is the **attendance-learning gap**, and it has reshaped how development economists think about education interventions. Studies in India, Kenya, and Pakistan have found that many children who attend school for years cannot read a simple paragraph or perform basic arithmetic. The binding constraint in these settings is not demand (whether children show up) but supply (what happens when they do). Teacher absenteeism, rote-based pedagogy, curricula pitched far above students' actual level, and multigrade classrooms with 60+ students all undermine learning even when attendance is high. The implication is that getting children into school is only the first step — and potentially the easier one. Improving what they learn once there requires tackling much harder problems of teacher training, accountability, and instructional quality. Effective education policy must address both the demand side (reducing barriers to attendance) and the supply side (ensuring attendance translates into actual skill acquisition).
