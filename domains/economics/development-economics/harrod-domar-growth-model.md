---
id: harrod-domar-growth-model
title: The Harrod-Domar Growth Model and the Financing Gap
domain: economics
course: development-economics
prerequisites:
- id: savings-investment-identity
  type: hard
- id: production-function-macroeconomics
  type: soft
builds-toward:
- savings-constraints-development
- foreign-aid-effectiveness
tags:
- economic growth
- Harrod-Domar
- capital-output ratio
- saving rate
- financing gap
- foreign aid
- linear stages theories
stage: advanced
status: validated
---

# The Harrod-Domar Growth Model and the Financing Gap

## Core Idea
The Harrod-Domar model, built on work by Roy Harrod (1939) and Evsey Domar (1946), assumes output is proportional to the capital stock, Y = K/v, where v is a fixed capital-output ratio. Since investment equals saving, the capital stock grows by sY − δK each year, which gives the growth rate g = s/v − δ. Growth therefore rises with the saving rate and falls with the amount of capital needed per unit of output. Development agencies used this logic for decades to compute a "financing gap" between the investment needed for a target growth rate and domestic saving, to be filled by foreign aid or borrowing. Its fixed capital-output ratio and neglect of productivity and institutions are its main weaknesses.

## How It's Best Learned
Compute growth for a few combinations of saving rates and capital-output ratios, then reverse the calculation to find the saving or aid needed for a target growth rate. Then compare the model's prediction with cases where high investment did not produce fast growth. That comparison motivates the Solow model and the later emphasis on productivity and institutions.

## Common Misconceptions
- Raising investment always raises a country's growth rate in proportion. (The model assumes a fixed capital-output ratio; in practice returns to capital can fall, and investment can be wasted when institutions are weak.)
- The financing gap tells donors how much aid will produce a given growth rate. (This assumes aid becomes investment one for one and that investment converts to output at a fixed ratio; cross-country evidence does not support such a stable link.)
- Harrod-Domar and Solow are the same model. (Solow allows capital and labor to substitute and assumes diminishing returns to capital, so in his model a higher saving rate raises the level of income but not its long-run growth rate.)

## Questions

```yaml
- question: "In the Harrod-Domar model with no depreciation, a country saves 20% of output and has a capital-output ratio of 4. What is its growth rate?"
  type: multiple-choice
  options: ["4%", "5%", "16%", "80%"]
  answer: 1
  explanation: "g = s/v = 0.20 / 4 = 0.05, or 5% per year. Each year investment adds 20% of output to capital, and since output is capital divided by 4, output grows by 0.20 / 4 = 5%."
- question: "A government targets 7% growth. The capital-output ratio is 3 and depreciation is zero. Domestic saving is 15% of GDP. In financing-gap reasoning, how large is the gap?"
  type: multiple-choice
  options: ["6% of GDP", "7% of GDP", "15% of GDP", "21% of GDP"]
  answer: 0
  explanation: "Required investment is s = g × v = 0.07 × 3 = 21% of GDP. Domestic saving covers 15%, leaving a gap of 6% of GDP to be filled from foreign sources under the model's assumptions."
- question: "In the Harrod-Domar model, a permanent rise in the saving rate permanently raises the growth rate of output."
  type: true-false
  answer: true
  explanation: "Because the capital-output ratio is fixed, growth equals s/v − δ, so a higher s raises g for good. In the Solow model, by contrast, diminishing returns mean a higher saving rate raises growth only during the transition to a new steady state."
- question: "Give two reasons why the Harrod-Domar model is now considered a poor guide to development policy."
  type: short-answer
  answer: "First, it treats the capital-output ratio as fixed, ignoring diminishing returns and the ways technology and efficiency change how much output capital produces. Second, it treats saving and investment as sufficient for growth, ignoring institutions, human capital, and incentives that determine whether investment is productive; aid also need not become investment one for one."
  explanation: "William Easterly's 1999 critique of the financing-gap approach found little evidence that aid and investment predicted growth in the way the model implies."
```

## Explainer
After World War II, economists wanted a simple way to think about how poor countries could grow. The Harrod-Domar model gave one. It grew out of Roy Harrod's 1939 essay on dynamic theory and Evsey Domar's 1946 paper on capital expansion, and it became the backbone of what development textbooks call linear-stages theories.

The model rests on two assumptions. First, output is proportional to capital: Y = K/v, where v is the **capital-output ratio**, the amount of capital needed to produce one unit of output per year. Second, from the saving-investment identity, the part of output that is saved becomes new capital. If s is the saving rate and δ the depreciation rate, the change in capital is ΔK = sY − δK. Dividing by K, and using Y/K = 1/v, gives the growth rate of capital, and therefore of output: g = s/v − δ.

The formula says two things. Saving more speeds growth. And economies that need less capital per unit of output grow faster from the same saving. With s = 20%, v = 4, and no depreciation, the economy grows 5% a year.

Planners ran the formula backward. If the target growth rate is g, required investment is (g + δ)v. Subtract domestic saving, and what remains is the **financing gap**, to be filled by foreign aid or capital inflows. A country targeting 7% growth with v = 3 needs to invest 21% of GDP; if it saves 15%, the gap is 6%. The Marshall Plan's success in rebuilding Western Europe seemed to support the idea that capital was the missing ingredient. W. W. Rostow's 1960 *The Stages of Economic Growth* similarly stressed raising investment to reach a "take-off."

The model's weaknesses became clear with experience. Its fixed capital-output ratio rules out diminishing returns, which Robert Solow's 1956 model introduced. In Solow's model a higher saving rate raises income per worker but not long-run growth, which depends on technological progress. Saving is also not sufficient: postwar Europe had skilled workers, institutions, and markets that many poorer countries lacked, so the same capital produced much less elsewhere. And aid need not become investment at all. William Easterly's 1999 study argued that the financing-gap model, still used by international institutions, had little support in the data. The model remains useful as a first account of why saving and investment matter, and as a reminder of what that account leaves out.
