---
id: discrimination-economics
title: "Discrimination: Becker and Statistical Models"
domain: economics
course: labor-economics
prerequisites:
- id: wage-determination
  type: hard
- id: labor-market-equilibrium
  type: soft
tags:
- discrimination
- Becker
- taste-based
- statistical-discrimination
- wage-gaps
stage: advanced
status: validated
---

# Discrimination: Becker and Statistical Models

## Core Idea
Economic models of labor market discrimination explain persistent wage gaps between demographic groups through two distinct mechanisms. Becker's taste-based discrimination model (1957) treats prejudice as a preference — discriminating employers, coworkers, or customers have a "taste for discrimination" that leads them to avoid or underpay minority workers. The model predicts that competitive market forces should erode taste-based discrimination over time (non-discriminating firms earn higher profits by hiring underpriced minority workers). Statistical discrimination (Phelps, Arrow) operates through rational Bayesian inference under imperfect information — employers use group membership as a signal of productivity when individual information is costly to acquire, even without prejudice. The two models have different policy implications: taste-based discrimination may respond to competition and anti-discrimination law, while statistical discrimination requires improving information or prohibiting the use of group statistics.

## Questions

```yaml
- question: "In Becker's taste-based discrimination model, a discriminating employer acts as if hiring a minority worker imposes an additional cost d (the discrimination coefficient). This means the employer will hire a minority worker only if..."
  type: multiple-choice
  options:
    - "The minority worker's wage is at least d above the majority worker's wage"
    - "The minority worker's wage is at least d below the majority worker's wage, compensating for the psychic cost of employing them"
    - "The minority worker is at least twice as productive as the majority worker"
    - "The government mandates hiring through affirmative action"
  answer: 1
  explanation: "The discriminating employer treats hiring a minority worker as costing w_m + d rather than just w_m, where d is the psychic cost of discrimination. To compete with a majority worker earning w_M, the minority worker must be willing to work for w_m ≤ w_M - d. The discrimination coefficient d thus functions as a tax on minority workers, reducing their market wage. Becker showed that competitive forces should erode this: non-discriminating firms face no such tax and can hire equally productive minority workers at the lower wage, earning higher profits."

- question: "Statistical discrimination is not really discrimination because it is based on rational inference rather than prejudice."
  type: true-false
  answer: false
  explanation: "Statistical discrimination produces real harm regardless of the employer's motives. When employers use group averages (e.g., average quit rates, average productivity) to evaluate individuals, high-performing members of disadvantaged groups are systematically underpaid or excluded based on group statistics rather than their own characteristics. Moreover, statistical discrimination can be self-reinforcing: if employers invest less in workers from groups perceived as less productive, those workers have fewer opportunities to develop skills, confirming the initial statistical generalization. The absence of animus does not mean the absence of discrimination."

- question: "Why does Becker's model predict that competitive market forces should eventually eliminate taste-based discrimination?"
  type: short-answer
  answer: "Non-discriminating firms can hire equally productive minority workers at a discount (because discriminating firms depress minority wages). This cost advantage makes non-discriminating firms more profitable. In a competitive market, these firms should expand and discriminating firms should lose market share and exit, gradually eliminating the wage gap. The persistence of wage gaps despite this competitive pressure suggests either that competition is insufficiently strong, that discrimination comes from non-employer sources (customers, coworkers), or that additional mechanisms (statistical discrimination, structural barriers) sustain the gaps."
  explanation: "This is one of the most famous predictions in labor economics — and its empirical failure (wage gaps persist decades after Becker's model) has driven the search for complementary explanations. Possible explanations for persistence include: (1) market power — many firms have enough market power that competitive pressure is weak; (2) customer and coworker discrimination — which cannot be arbitraged away; (3) statistical discrimination — rational but discriminatory inference that competition alone does not eliminate; and (4) structural barriers (residential segregation, school quality, network effects) that perpetuate group differences in skills and opportunities."
```

## Explainer

Discrimination in labor markets is one of the most consequential and contentious topics in economics. Persistent wage gaps between racial and gender groups — even after controlling for education, experience, occupation, and other observable characteristics — demand explanation. Economic theory provides two fundamentally different models, each with distinct implications for why discrimination persists and what can be done about it.

Becker's taste-based model, published in 1957, treated discrimination as a preference. Some employers, coworkers, or customers derive disutility from interacting with members of certain groups. The employer's discrimination coefficient d represents the additional psychic cost they incur from hiring a minority worker. Formally, the employer acts as if the cost of a minority worker is their wage plus d, making minority workers less attractive at any given wage. In equilibrium, minority workers earn less — the competitive wage discount reflects the average discrimination intensity in the market.

Becker's model has a provocative implication: competitive markets should erode discrimination. Non-discriminating firms face no psychic cost d and can therefore hire equally productive minority workers at their (depressed) market wage, earning higher profits per worker than discriminating firms. In the long run, competitive pressure should cause discriminating firms to lose market share and exit, driving the wage gap toward zero. The persistence of discrimination despite decades of competitive markets suggests that either competitive pressures are insufficient (many employers have market power), discrimination comes from non-arbitrageable sources (customer preferences, coworker hostility), or other mechanisms sustain the gaps.

Statistical discrimination models (Phelps, 1972; Arrow, 1973) offer a complementary explanation that does not require prejudice. When employers cannot perfectly observe individual productivity, they rationally use observable group characteristics (gender, race, age, education) as signals. If an employer knows that, on average, group A has higher productivity or lower quit rates than group B, they will statistically prefer group A candidates when individual information is costly or noisy. This is Bayesian-rational behavior — the employer is using available information efficiently — but it produces discriminatory outcomes: high-productivity members of disadvantaged groups are systematically undervalued.

Statistical discrimination has a particularly pernicious self-reinforcing property. If employers invest less in training workers from a group they perceive as less productive (or more likely to quit), those workers accumulate less human capital, confirming the initial statistical generalization. This feedback loop can sustain group-level productivity differences that originated from historical discrimination or arbitrary initial conditions, even in the complete absence of prejudice. Breaking the cycle requires interventions that either improve information (so employers can evaluate individuals rather than groups), ban the use of group statistics (anti-discrimination law), or directly invest in human capital for disadvantaged groups.

The empirical decomposition of wage gaps uses Oaxaca-Blinder decomposition, which separates the observed gap into a "explained" component (attributable to differences in observable characteristics like education and experience) and an "unexplained" residual often interpreted as an upper bound on discrimination. For the US gender wage gap, roughly half is explained by observable differences and half remains unexplained. For the racial wage gap, the unexplained component is larger. However, the unexplained residual captures not just discrimination but any omitted productivity-related variable, making its interpretation as "discrimination" approximate. Audit studies — sending identical resumes with different-sounding names — provide cleaner evidence, consistently finding significant discrimination in callback rates.
