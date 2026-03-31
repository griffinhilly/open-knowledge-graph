---
id: occupational-choice
title: Occupational Choice
domain: economics
course: labor-economics
prerequisites:
- id: human-capital-theory
  type: hard
- id: compensating-wage-differentials
  type: soft
tags:
- occupation
- sorting
- Roy-model
- comparative-advantage
- self-selection
stage: advanced
status: validated
---

# Occupational Choice

## Core Idea
Occupational choice theory models how individuals select among occupations based on comparative advantage, preferences, and expected returns. The Roy model (1951) provides the foundational framework: individuals self-select into the occupation where their earnings are highest, given their sector-specific skills. This selection generates sorting — individuals with high ability in finance cluster in finance, those with high ability in teaching cluster in teaching — and this sorting has implications for wage distributions within occupations and for the interpretation of observed wage differentials. Understanding self-selection is essential because naive comparisons of wages across occupations confound the causal effect of the occupation with the characteristics of who selects into it.

## Questions

```yaml
- question: "In the Roy model, a worker chooses between two occupations (A and B). The worker selects occupation A if..."
  type: multiple-choice
  options:
    - "Occupation A pays a higher average wage"
    - "The worker's expected earnings in A exceed their expected earnings in B, given their individual skills"
    - "Occupation A has higher social status"
    - "The worker's parents were in occupation A"
  answer: 1
  explanation: "The Roy model is based on self-selection according to comparative advantage. A worker chooses the occupation that maximizes their individual expected earnings (or utility, in extended models). A person with strong mathematical skills but average verbal skills might choose engineering even if the average wage in law is higher, because their personal return in engineering exceeds their personal return in law. This individual-level selection based on comparative advantage, not average occupational wages, drives the model."

- question: "Self-selection into occupations means that observed wage differences between occupations directly measure the causal effect of the occupation on earnings."
  type: true-false
  answer: false
  explanation: "Self-selection confounds the occupation effect with the characteristics of who enters it. If the most talented and ambitious people self-select into high-paying occupations, the observed wage premium for those occupations reflects both the occupation's causal effect on earnings AND the pre-existing advantages of the people in it. A doctor earns more than a teacher partly because medical training increases earnings (causal effect) and partly because people with characteristics correlated with high earnings (high ability, long time horizons) select into medicine (selection effect). Disentangling these requires techniques like natural experiments or structural models."

- question: "What is 'comparative advantage' in the context of occupational choice, and how does it differ from absolute advantage?"
  type: short-answer
  answer: "Comparative advantage means being relatively better at one occupation compared to another, regardless of absolute skill levels. A person with absolute advantage in both law and plumbing (they would be a great lawyer AND a great plumber) still has comparative advantage in one — whichever offers the larger relative return given their skill profile. They should specialize in the occupation where their advantage is greatest, even if they could succeed in both. This drives efficient sorting: each person enters the occupation where their relative productivity is highest."
  explanation: "Comparative advantage in occupational choice is directly analogous to comparative advantage in international trade theory. A brilliant physicist who is also an excellent chef has absolute advantage in both occupations, but if their relative advantage is greater in physics (they are the world's best physicist but only a moderately better-than-average chef), their comparative advantage lies in physics. The earnings differential between their physics potential and their cooking potential determines the efficient allocation. The Roy model formalizes this intuition with sector-specific skill distributions."
```

## Explainer

Why do people end up in the occupations they occupy? The answer involves a complex interaction of abilities, preferences, constraints, and expectations — and understanding this selection process is crucial for interpreting virtually any empirical finding in labor economics. Observed wage differences across occupations, gender gaps in occupational composition, and returns to education within occupations are all affected by who selects into what.

The Roy model provides the theoretical foundation. Named after A.D. Roy's 1951 paper (which used the example of hunting vs. fishing), the model assumes individuals have sector-specific skills and choose the sector offering the highest earnings given their personal skill profile. If skills are distributed differently across sectors (some people are disproportionately skilled at analytical work, others at manual work), the result is sorting: each sector attracts the individuals for whom it offers the highest return. This sorting is efficient in the sense that individuals are allocated to their comparative advantage.

The selection implications are profound for empirical work. Consider comparing the earnings of lawyers to those of teachers. The observed difference includes the causal effect of the occupations (legal training commands a premium) plus the selection effect (people who become lawyers differ from people who become teachers in ability, motivation, time preferences, and other characteristics that independently affect earnings). If you randomly assigned people to occupations, the wage difference might be quite different from what we observe — possibly smaller (if lawyer self-selection attracts high-earners) or larger (if teacher self-selection attracts people who would earn less anywhere). Heckman's sample selection correction and structural Roy model estimation were developed precisely to address this problem.

Occupational choice is also shaped by factors beyond pure comparative advantage. Information and expectations play a role — young people choosing careers have imperfect information about their own abilities and about the returns to different occupations. Social norms influence choice — gendered expectations about "appropriate" occupations channel men and women into different fields independently of ability. Constraints limit choice — financial barriers to education, geographic access to training, and family obligations restrict the feasible set. Discrimination closes off options — historical exclusion of women and minorities from certain occupations shapes current occupational distributions through path dependence even after legal barriers are removed.

The interaction between occupational choice and inequality operates through multiple channels. Rising returns to specific occupations (technology, finance) attract more talent, potentially at the expense of occupations with positive externalities (teaching, public service). Occupational licensing creates barriers that restrict entry and raise incumbents' wages, with ambiguous effects on quality. Occupational segregation by gender and race, whether driven by discrimination, norms, or comparative advantage, contributes to group-level wage gaps. Understanding the full chain — from individual choice to occupational composition to wage outcomes — requires integrating the Roy model framework with institutional analysis and careful attention to the selection processes that generate observed patterns.
