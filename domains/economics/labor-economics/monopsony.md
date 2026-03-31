---
id: monopsony
title: Monopsony
domain: economics
course: labor-economics
prerequisites:
- id: labor-market-equilibrium
  type: hard
- id: labor-demand-theory
  type: hard
tags:
- monopsony
- employer-market-power
- wage-setting
- Manning
stage: advanced
status: validated
---

# Monopsony

## Core Idea
Monopsony refers to labor markets where employers have market power in wage-setting — they face an upward-sloping labor supply curve (they must raise wages to attract additional workers) rather than taking the wage as given. In the pure monopsony model (one buyer of labor), the firm hires fewer workers at a lower wage than the competitive equilibrium because the marginal cost of labor exceeds the wage (raising the wage for the marginal worker means raising it for all inframarginal workers too). Modern monopsony theory (Manning, 2003) extends this beyond the single-employer case to any market where search frictions, switching costs, geographic immobility, or differentiated job attributes give employers some wage-setting power. Monopsony has major implications: it means minimum wage increases can raise employment, firms earn profits from underpaying workers, and the competitive model systematically overpredicts wages.

## Questions

```yaml
- question: "In a monopsony labor market, the firm pays a wage that is..."
  type: multiple-choice
  options:
    - "Equal to the marginal revenue product of labor, as in competition"
    - "Below the marginal revenue product of labor because the firm exploits its market power to set wages below the competitive level"
    - "Above the marginal revenue product of labor because the firm must attract workers"
    - "Determined entirely by worker preferences"
  answer: 1
  explanation: "A monopsonist maximizes profit by hiring until marginal revenue product equals marginal cost of labor (MCL), not the wage. Because MCL > w (hiring an extra worker requires raising the wage for all workers), the firm hires fewer workers at a lower wage than competition would produce. The gap between MRPL and the wage represents monopsonistic exploitation — the firm captures rents by paying workers less than their contribution to revenue. This is analogous to a monopolist charging above marginal cost in the product market."

- question: "A moderate minimum wage increase in a monopsonistic labor market necessarily reduces employment."
  type: true-false
  answer: false
  explanation: "This is one of the most counterintuitive results in labor economics. In a monopsony, the firm is already hiring below the competitive employment level. A binding minimum wage above the monopsony wage but below the competitive wage forces the firm to pay more but also flattens the marginal cost of labor curve — the firm no longer needs to raise wages for all workers when hiring one more. This can increase both the wage AND employment, moving toward the competitive outcome. This theoretical result has been central to interpreting Card and Krueger's empirical finding of zero or positive employment effects from minimum wage increases."

- question: "What makes modern monopsony theory (Manning) different from the classical single-employer monopsony model?"
  type: short-answer
  answer: "Classical monopsony requires a single employer (e.g., a company town). Manning's modern monopsony shows that monopsony power arises whenever employers face upward-sloping labor supply curves — which occurs due to search frictions (workers cannot costlessly find and switch to better-paying jobs), geographic immobility (workers cannot easily relocate), job differentiation (workers prefer certain employers for non-wage reasons), and imperfect information (workers do not know all available wages). These frictions give every employer some degree of wage-setting power, making monopsony a matter of degree rather than an all-or-nothing market structure."
  explanation: "This insight transforms monopsony from a rare special case (company towns) to a pervasive feature of labor markets. Evidence for pervasive monopsony power includes: job-to-job wage gains (workers who switch employers earn significantly more, implying they were underpaid before), the employment effects of minimum wages (consistent with monopsony predictions), concentration effects (more concentrated employer markets have lower wages), and the persistence of wage differences across firms for identical workers."
```

## Explainer

The standard competitive model assumes that firms are wage-takers — they face a perfectly elastic labor supply curve and hire as many workers as they want at the market wage. Monopsony inverts this assumption: firms face an upward-sloping labor supply curve and must raise wages to attract additional workers. This apparently simple change in the supply curve's slope has far-reaching consequences for wages, employment, and policy.

In the classical monopsony model — literally, one buyer — the firm's hiring decision differs from competition because the marginal cost of labor (MCL) exceeds the wage. To hire one more worker, the firm must raise the wage — not just for the new hire but for all existing workers. This makes each additional hire more expensive than their wage alone would suggest. The firm hires until MRPL = MCL (not MRPL = w), resulting in fewer workers at a lower wage than competition would produce. The wage gap between MRPL and w represents the monopsony rent — the firm's profit from its market power.

Manning's reconceptualization broadened monopsony from an extreme market structure to a pervasive phenomenon. In any labor market with frictions — and all labor markets have frictions — employers possess some degree of wage-setting power. A worker who would prefer to work for a higher-paying firm across town cannot switch costlessly: job search takes time, the better job may not be advertising, interviews are uncertain, relocation is expensive, and the current employer may offer non-wage benefits (familiarity, social networks, commute convenience) that a purely monetary comparison misses. These frictions mean that if one employer cuts wages slightly below the market, it does not instantly lose all workers — some stay because switching is costly. This residual retention is the hallmark of monopsony power.

The minimum wage implication is the most policy-relevant result. In a competitive market, a minimum wage above the equilibrium wage creates a surplus of workers (unemployment) — the standard textbook prediction. In a monopsony, a minimum wage above the monopsony wage but below the competitive wage can increase employment. The mechanism is that the minimum wage eliminates the firm's need to raise wages for inframarginal workers when hiring one more, flattening the MCL curve and making additional hiring profitable. This result is central to interpreting Card and Krueger's (1994) influential study of fast-food employment in New Jersey versus Pennsylvania, which found that a minimum wage increase in New Jersey did not reduce employment — a finding consistent with monopsony but puzzling under competition.

Empirical evidence for labor market monopsony power has accumulated rapidly. Studies of employer concentration (measured by the Herfindahl-Hirschman Index for local labor markets) find that higher concentration is associated with lower wages, controlling for worker characteristics. Analysis of job-to-job transitions shows significant wage gains when workers switch employers, suggesting they were underpaid at the previous employer. Patent data and non-compete agreement studies show that restrictions on worker mobility reduce wages, consistent with firms exploiting reduced outside options. The emerging consensus is that monopsony power is not a rare curiosity but a quantitatively important feature of many labor markets, with implications for wage stagnation, inequality, and the optimal design of labor market institutions.
