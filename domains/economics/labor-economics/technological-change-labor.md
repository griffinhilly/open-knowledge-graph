---
id: technological-change-labor
title: Technological Change and Labor Markets
domain: economics
course: labor-economics
prerequisites:
- id: labor-demand-theory
  type: hard
- id: human-capital-theory
  type: soft
tags:
- technology
- skill-biased-change
- automation
- polarization
- task-model
stage: advanced
status: validated
---

# Technological Change and Labor Markets

## Core Idea
Technological change transforms labor markets by altering the demand for different types of skills and tasks. Skill-biased technological change (SBTC) — the hypothesis that technology complements high-skilled workers while substituting for low-skilled workers — was the dominant explanation for rising wage inequality from the 1980s through the 2000s. The task-based model (Autor, Levy, Murnane) refined this by distinguishing routine tasks (codifiable procedures susceptible to automation) from non-routine tasks (requiring creativity, judgment, or interpersonal skills). This produces job polarization: employment grows at the top (non-routine cognitive) and bottom (non-routine manual) of the skill distribution while hollowing out the middle (routine cognitive and manual), with corresponding effects on the wage distribution.

## Questions

```yaml
- question: "The 'task-based' model of technological change differs from the skill-biased technological change (SBTC) hypothesis by..."
  type: multiple-choice
  options:
    - "Arguing that technology has no effect on labor markets"
    - "Focusing on which tasks can be automated (routine vs. non-routine) rather than which skill levels are affected (high vs. low)"
    - "Claiming that only manufacturing jobs are affected by technology"
    - "Assuming that all workers are equally affected by technological change"
  answer: 1
  explanation: "SBTC treats technology as uniformly complementing educated/skilled workers and substituting for uneducated/unskilled workers, predicting a monotonic relationship between skill and demand. The task model is more nuanced: technology automates routine tasks (which are concentrated in middle-skill jobs like bookkeeping, manufacturing assembly, and clerical work) while complementing non-routine cognitive tasks (analysis, management, creativity) and having little effect on non-routine manual tasks (janitor, home health aide). This explains job polarization — a U-shaped pattern of employment growth that SBTC cannot."

- question: "Job polarization — the simultaneous growth of high-skill and low-skill employment with declining middle-skill employment — contradicts the simple skill-biased technological change hypothesis."
  type: true-false
  answer: true
  explanation: "SBTC predicts that technology uniformly increases demand for high-skilled workers and decreases demand for low-skilled workers — a monotonic pattern. Job polarization shows a non-monotonic pattern: middle-skill jobs decline (routine tasks automated) while both high-skill (non-routine cognitive) and low-skill (non-routine manual) jobs grow. This pattern, documented by Autor and Dorn (2013) in the US and by Goos and Manning (2007) in Europe, is better explained by the task model's focus on routine vs. non-routine tasks than by SBTC's focus on high vs. low skill."

- question: "What determines whether a particular task is susceptible to automation?"
  type: short-answer
  answer: "A task is susceptible to automation when it can be described by explicit rules and procedures (codified), follows a predictable pattern, and operates in a structured environment. Routine cognitive tasks (data entry, bookkeeping, basic calculation) and routine manual tasks (assembly line work, sorting) meet these criteria. Non-routine tasks resist automation because they require flexibility, judgment, creativity (non-routine cognitive) or physical dexterity in unstructured environments (non-routine manual). However, advances in AI and machine learning are expanding the frontier of automatable tasks into previously non-routine domains."
  explanation: "Autor, Levy, and Murnane's (2003) 'routineness' criterion was the key theoretical contribution: the relevant distinction is not skill level but task structure. A PhD mathematician doing statistical analysis (non-routine cognitive) and a janitor navigating a cluttered room (non-routine manual) both resist automation — though for different reasons. A bookkeeper following accounting rules (routine cognitive) and a factory assembler performing repetitive motions (routine manual) are both automatable — though one is 'white collar' and the other is 'blue collar.' The task framework cuts across the traditional skill hierarchy."
```

## Explainer

Technology has always transformed work — from the mechanical loom to the assembly line to the personal computer. But the pace and pattern of technological change in recent decades have created particularly dramatic shifts in labor market structure, and understanding these shifts requires more than the simple intuition that "technology replaces workers."

The skill-biased technological change (SBTC) hypothesis dominated labor economics from the 1980s through the early 2000s. The core story: computers and information technology complement educated workers (who use technology to become more productive) and substitute for less-educated workers (whose routine tasks are automated). This explains the widening college wage premium — the gap between earnings of college graduates and high school graduates roughly doubled from 1980 to 2010 in the US. The SBTC explanation was clean and parsimonious: a race between education (increasing supply of skilled workers) and technology (increasing demand), with technology winning the race and widening inequality.

The task-based model, developed by Autor, Levy, and Murnane (2003), refined SBTC by recognizing that technology does not uniformly affect all tasks at a given skill level. The key insight: what determines a task's susceptibility to automation is not the skill required but the routineness of the task — whether it can be described by explicit rules and executed by following a codifiable procedure. Many middle-skill jobs (bookkeeping, clerical work, manufacturing assembly, bank telling) are highly routine and therefore automatable, while many low-skill jobs (cleaning, food service, personal care) require non-routine physical dexterity and interpersonal interaction that machines handle poorly.

Job polarization is the empirical phenomenon the task model was designed to explain. Across developed economies, employment has grown at the top (managerial, professional, technical jobs) and the bottom (service jobs in food, cleaning, personal care, and security) while shrinking in the middle (production, clerical, sales, and administrative jobs). The wage distribution has followed a similar pattern, with wages growing most at the top and stagnating or declining in the middle. This U-shaped pattern is inconsistent with SBTC (which predicts monotonically increasing demand by skill level) but perfectly consistent with the task model (routine middle-skill jobs are automated, non-routine jobs at both ends are not).

The frontier is rapidly evolving. Large language models, robotics advances, and machine learning are expanding the set of automatable tasks into domains previously considered safe — medical diagnosis, legal research, creative writing, software development. The question of whether AI will primarily complement workers (augmenting productivity in non-routine tasks) or substitute for them (replacing tasks previously thought non-routine) is one of the most consequential economic questions of the coming decades. The task-based framework provides the analytical structure for thinking about this question, but the speed of technological change may outpace the labor market's ability to adjust, creating transition costs even if the long-run outcome is productive.
