---
id: is-lm-model
title: The IS-LM Model
domain: economics
course: macroeconomics
prerequisites:
- id: aggregate-demand
  type: hard
- id: interest-rates-and-loanable-funds
  type: hard
- id: fiscal-policy-macroeconomics
  type: hard
- id: monetary-policy-tools
  type: hard
- id: systems-substitution
  type: soft
- id: systems-graphing
  type: soft
- id: fiscal-multiplier
  type: soft
- id: systems-of-linear-equations
  type: hard
builds-toward:
- open-economy-macroeconomics
tags:
- IS-LM
- goods-market
- money-market
- equilibrium
- Keynesian
stage: abstract-reasoning
status: validated
---
# The IS-LM Model

## Core Idea
The IS-LM model describes the joint equilibrium of the goods market (IS curve: combinations of output and interest rate where investment equals saving) and the money market (LM curve: combinations of output and interest rate where money demand equals money supply). The IS curve slopes downward (higher rates reduce investment and output); the LM curve slopes upward (higher output raises money demand and thus rates). Their intersection determines the short-run equilibrium real interest rate and output level. Fiscal policy shifts IS; monetary policy shifts LM. The model reveals why fiscal stimulus can be partially offset by higher interest rates (crowding out).

## How It's Best Learned
Derive each curve from its underlying market condition. Then work through the four standard policy experiments: expansionary fiscal policy (IS right), contractionary fiscal policy (IS left), expansionary monetary policy (LM right), contractionary monetary policy (LM left). Identify equilibrium changes in output and interest rates.

## Common Misconceptions
- The IS-LM model is a short-run framework with a fixed price level — it complements, not replaces, the AS-AD model.
- A liquidity trap occurs when the LM curve is flat (at the zero lower bound on interest rates), making monetary policy ineffective while fiscal policy is fully effective.
- IS-LM was designed by Hicks as an interpretation of Keynes, not by Keynes himself, and some argue it oversimplifies Keynes's theory.

## Questions

```yaml
- question: "The government increases spending without changing taxes. In the IS-LM framework, what is the immediate effect on equilibrium output and the interest rate?"
  type: multiple-choice
  options:
    - "Output falls, interest rate falls"
    - "Output rises, interest rate falls"
    - "Output rises, interest rate rises"
    - "Output is unchanged, interest rate rises"
  answer: 2
  explanation: "Higher government spending shifts IS rightward (more output demanded at every interest rate). With LM unchanged, the new intersection has higher output and a higher interest rate. The higher rate partially crowds out private investment — output rises by less than the full fiscal multiplier would suggest."

- question: "In a liquidity trap, expansionary monetary policy (shifting LM right) is just as effective at raising output as expansionary fiscal policy."
  type: true-false
  answer: false
  explanation: "In a liquidity trap, the LM curve is flat because interest rates are at the zero lower bound — people are indifferent between holding money and bonds, so the money market does not tighten as output rises. Shifting a flat LM curve right has no effect on the equilibrium interest rate or output. Fiscal policy (shifting IS), by contrast, moves along the flat LM curve and raises output fully, without being offset by higher rates."

- question: "What is 'crowding out' in the IS-LM model, and why does it mean fiscal stimulus is less potent than a simple multiplier analysis suggests?"
  type: short-answer
  answer: "Crowding out occurs when fiscal expansion (IS shifts right) raises equilibrium interest rates, which then reduces private investment. In the IS-LM model, the equilibrium moves up along the LM curve: output rises, but the higher interest rate suppresses investment, partially offsetting the stimulus. The net increase in output is smaller than the full multiplier effect because LM 'pushes back' through the interest rate."
  explanation: "A simple Keynesian multiplier ignores the money market. IS-LM adds it back: as output rises, money demand rises, pushing up interest rates. Higher rates discourage investment, dampening the output expansion. The degree of crowding out depends on the slope of LM (how sensitive interest rates are to output) and the slope of IS (how sensitive investment is to interest rates)."
```

## Explainer

You have studied the goods market and the money market separately. IS-LM asks: what happens when they must reach equilibrium at the same time? The answer is a pair of curves in (output, interest rate) space, and their intersection is the short-run macroeconomic equilibrium.

The **IS curve** traces all combinations of output (Y) and the interest rate (r) where the goods market clears — where investment equals saving, or equivalently where total spending equals total output. It slopes downward because higher interest rates reduce investment, which reduces output. Think of it as the goods market's constraint on (Y, r): only points on IS are consistent with spending equilibrium. Fiscal policy (government spending or taxes) shifts IS: more government spending means more output is demanded at every interest rate, so IS moves right.

The **LM curve** traces all combinations of Y and r where the money market clears — where money demand equals money supply. It slopes upward because higher output means more transactions, which raises money demand, which (with a fixed supply) pushes interest rates up. Think of LM as the money market's constraint. Monetary policy shifts LM: when the central bank increases the money supply, the interest rate needed to clear the money market is lower at every output level, so LM moves right (and down).

The intersection of IS and LM simultaneously satisfies both constraints. This is powerful: it shows that fiscal and monetary policy interact. Expansionary fiscal policy shifts IS right, raising output — but also raising interest rates, which crowds out some private investment. The net output gain is less than the simple multiplier predicts, precisely because the higher interest rate dampens investment. This "crowding out" is invisible if you analyze the goods market alone.

One important boundary case is the **liquidity trap**: when interest rates hit zero (or the zero lower bound), the LM curve becomes flat. People hold money and bonds interchangeably because both pay nothing. In this case, expanding the money supply cannot push rates any lower, so it has no effect — LM shifts but the intersection doesn't move. Fiscal policy, however, still works: shifting IS right moves equilibrium output along the flat LM without raising rates. This is exactly the situation many countries faced after 2008 and again during 2020, and it is why central banks turned to unconventional tools (quantitative easing, forward guidance) when their primary lever was exhausted.
