---
id: sticky-wages-labor-market-frictions
title: Sticky Wages and Labor Market Frictions
domain: economics
course: macroeconomics
prerequisites:
- id: natural-rate-hypothesis
  type: soft
builds-toward:
- wage-price-dynamics-and-inflation
tags:
- sticky-wages
- labor-market-friction
- nominal-rigidity
- contracts
stage: advanced
status: draft
---

# Sticky Wages and Labor Market Frictions

## Core Idea
Sticky wages arise from long-term contracts, efficiency wage considerations (firms maintain above-market wages to motivate workers), and worker resistance to nominal cuts due to fairness norms. Wage stickiness is stronger than price stickiness.

## How It's Best Learned
Use examples: during recessions, firms lay off workers rather than cutting all wages proportionally, reflecting morale and fairness concerns. Compare to prices, which fall more readily.

## Common Misconceptions
- Assuming wages are as flexible as prices; downward rigidity is much stronger.
- Treating all wage stickiness as contractual.
- Forgetting sticky wages slow adjustment and trap economy in recessions.

## Questions

```yaml
- question: "A factory faces a sudden 15% drop in demand for its products during a recession. Under efficiency wage theory, why might the factory owner choose to lay off 15% of workers rather than cut all workers' wages by 15%?"
  type: multiple-choice
  options:
    - "Labor contracts make wage cuts legally impossible in the short run"
    - "Wage cuts would trigger unionized workers to strike, causing greater output losses than layoffs"
    - "Cutting wages reduces worker productivity, loyalty, and retention enough that the firm loses more in output than it saves in wages"
    - "A 15% wage cut would violate minimum wage law in most jurisdictions"
  answer: 2
  explanation: "Efficiency wage theory holds that above-market wages are not just a cost but a productivity investment. Workers paid above their outside options have more to lose from being fired, so they shirk less, quit less frequently (reducing turnover costs), and are more motivated. If a wage cut undermines these productivity gains — through reduced effort, higher quit rates, and lower morale — the apparent labor-cost savings are offset by higher effective costs per unit of output. The rational profit-maximizing choice is often to maintain high wages for retained workers while shedding headcount, which is the pattern observed in recessions."

- question: "Why do nominal wage cuts cause greater worker resistance and morale damage than equivalent real wage erosion through inflation, even when the economic outcome is identical?"
  type: multiple-choice
  options:
    - "Nominal wages are legally protected from cuts in ways that inflation-eroded real wages are not"
    - "Workers suffer money illusion and genuinely cannot distinguish real from nominal wage changes"
    - "Workers evaluate wage changes relative to a nominal reference point; a cut feels like a breach of the implicit employment relationship, while inflation is experienced as a background condition"
    - "Inflation is always accompanied by raises in other sectors, making workers feel relatively unharmed"
  answer: 2
  explanation: "Bewley's survey evidence shows that workers use their current nominal wage as an anchor. A direct cut below that anchor is experienced as an active breach of the employment relationship — it signals the employer is willing to make the worker worse off — triggering resentment, reduced effort, and quit intentions. Inflation that erodes the real wage does not carry this social meaning; it is a general background condition rather than a targeted action by the employer. This is why firms in recessions accept the unemployment-generating consequences of sticky wages rather than impose cuts that damage retained workers' productivity."

- question: "A nominal wage cut of 5% and an inflation rate of 5% with no nominal wage change produce identical real outcomes, but they have different effects on worker morale and firm productivity."
  type: true-false
  answer: true
  explanation: "This is the key empirical finding from behavioral economics and survey research (Bewley's work). Workers anchor on their nominal wage and experience a nominal cut as a breach of trust, even when the real outcome is the same as inflation-eroded wages. The firm that cuts nominal wages faces resentment, increased turnover, and reduced effort; the firm that holds nominal wages flat while inflation erodes real wages avoids these consequences. This asymmetry is the behavioral foundation of downward nominal wage rigidity."

- question: "Wage stickiness and price stickiness are roughly symmetric: both prices and wages are about equally resistant to downward adjustment in response to falling demand."
  type: true-false
  answer: false
  explanation: "The topic explicitly states that wage stickiness is stronger than price stickiness, and downward rigidity is much stronger for wages than for prices. Prices can fall more readily in response to weak demand — retailers discount goods, commodity prices fall, and competitive pressures push prices down. Wages resist downward adjustment through multiple reinforcing mechanisms: long-term contracts, efficiency wage considerations, and strong fairness norms around nominal wage cuts. This asymmetry means a negative demand shock primarily hits employment rather than wages, prolonging recessions."

- question: "Explain why efficiency wages create a situation where a firm rationally maintains wages above the market-clearing level, even when it could legally cut them."
  type: short-answer
  answer: "Efficiency wage theory argues that worker productivity depends on the wage level. When a firm pays above-market wages, workers have more to lose from being fired (their outside option is worth less), so they exert more effort and shirk less. Higher wages also reduce costly turnover: workers earning above-market rates are less likely to quit voluntarily, saving recruitment and training costs. If cutting wages undermines these productivity gains — through reduced effort, higher quit rates, and lower morale — the wage cut that appears to save money actually costs more through lost productivity. The profit-maximizing response is to maintain high wages and shed workers by layoff when demand falls."
  explanation: "The key insight reverses the usual intuition. Normally we model wage as purely a cost that firms minimize. Efficiency wages show that wage level affects the quantity and quality of labor services purchased. When the productivity effect is large enough, the wage bill per unit of output is actually lower at above-market wages — the firm gets so much more per worker that paying more per hour is economical. This is why the wage rigidity created by efficiency wages is rational behavior, not a market imperfection."
```

## Explainer

If markets always cleared instantly, a recession would simply push wages down until employers were willing to hire again — unemployment would be brief and self-correcting. But wages don't behave like tomato prices. Understanding why requires grasping three distinct mechanisms, each rooted in the incentives you've already studied at the firm and household level.

The first source is **long-term labor contracts**. Firms and workers often negotiate wages months or years in advance, trading wage certainty against the risk that market conditions shift. A worker locked into a two-year contract at $50/hour cannot have that wage cut to $40 just because demand fell — the contract is legally binding. Even when contracts are informal, implicit agreements do similar work: workers accept a "deal" that includes wage stability in exchange for loyalty and predictability. During a recession, these commitments become economic anchors that keep nominal wages above where a spot market would set them.

The second source is **efficiency wage theory**, and it turns the usual story on its head. Normally we think high wages are a cost firms want to minimize. But a firm paying above-market wages may actually *benefit* — workers are more productive, less likely to shirk (since getting fired is expensive), and less likely to quit (reducing costly turnover). If cutting wages undermines these productivity gains, the wage cut that looks like savings on paper actually costs the firm more in lost output and higher quit rates. So firms choose to hold wages up even when they could legally cut them. This is a rational, profit-maximizing choice, not irrationality.

The third source is **fairness norms and worker morale**. Experimental evidence and survey studies (famously summarized by Truman Bewley) show that workers experience nominal wage cuts as a breach of trust, even when real wages have already eroded through inflation. A 5% wage cut triggers resentment, sabotage risk, and resignations in ways that a 5% raise-minus-5%-inflation does not, even though the real outcome is identical. Firms understand this psychology and avoid nominal cuts to preserve team cohesion and effort norms. The result is that **downward nominal wage rigidity** — the tendency for wages to resist falling even when unemployment rises — is much stronger than the symmetric reluctance of prices to fall.

When these mechanisms combine with the natural rate hypothesis you've already studied, the macroeconomic implication is stark: a negative demand shock doesn't quickly lower wages and re-employ workers. Instead, firms respond to lower demand by laying off workers while keeping wages high for those who remain. Unemployment rises and persists until either demand recovers or (over a longer horizon) wage norms gradually erode. This mechanism is central to Keynesian and New Keynesian explanations for why recessions last as long as they do — and why stimulative policy can reduce unemployment without waiting for the market to self-correct through wage adjustment.
