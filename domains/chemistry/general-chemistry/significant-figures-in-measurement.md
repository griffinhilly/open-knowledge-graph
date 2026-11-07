---
id: significant-figures-in-measurement
title: Significant Figures in Measurement and Calculation
domain: chemistry
course: general-chemistry
prerequisites:
- id: scientific-notation-intro
  type: soft
- id: measuring-volume
  type: soft
- id: accuracy-precision-error
  type: soft
builds-toward:
- uncertainty-propagation
tags:
- significant figures
- measurement uncertainty
- rounding
- scientific notation
- exact numbers
stage: formal-systems
status: validated
---

# Significant Figures in Measurement and Calculation

## Core Idea
Every measured number carries uncertainty, and significant figures are the digits that convey it: all the certain digits plus one estimated digit. Rules for counting them tell you which zeros matter, and rules for calculations keep a result from claiming more certainty than the data allow. In multiplication and division, the answer keeps the fewest significant figures of any measured factor; in addition and subtraction, it keeps the fewest decimal places.

## How It's Best Learned
Start at the instrument: read a graduated cylinder or ruler, record every marked digit, and estimate one more. Then practice counting significant figures in numbers with leading, embedded and trailing zeros. Work calculations with both rules side by side, rounding only at the end, and rewrite ambiguous numbers in scientific notation.

## Common Misconceptions
- All zeros are significant. (Leading zeros, as in 0.0045, only locate the decimal point and are not significant.)
- In addition, the answer keeps the fewest significant figures. (Addition and subtraction keep the fewest decimal places; the significant-figure count rule is for multiplication and division.)
- Defined and counted numbers limit the precision of a result. (Exact numbers, such as 1 L = 1000 mL or 12 eggs, have unlimited significant figures and never limit the answer.)
- Rounding at each step gives the same answer as rounding at the end. (Rounding at each step can build up error; keep extra digits until the final result.)

## Questions

```yaml
- question: "How many significant figures are in 0.004500 g?"
  type: multiple-choice
  options: ["2", "4", "6", "7"]
  answer: 1
  explanation: "The leading zeros only place the decimal point. The digits 4 and 5 count, and the two trailing zeros after the decimal point also count because they report measured precision. That gives 4."
- question: "Calculate 12.11 g + 18.0 g + 1.013 g and report the answer with correct significant figures."
  type: short-answer
  answer: "31.1 g"
  explanation: "The raw sum is 31.123 g. In addition, the answer keeps the fewest decimal places of any term. 18.0 has one decimal place, so the result rounds to 31.1 g."
- question: "A student multiplies 4.56 cm by 1.4 cm. What is the correctly reported area?"
  type: multiple-choice
  options: ["6.384 cm²", "6.38 cm²", "6.4 cm²", "6 cm²"]
  answer: 2
  explanation: "In multiplication, the result keeps as many significant figures as the factor with the fewest. 1.4 has two, so 6.384 rounds to 6.4 cm²."
- question: "When converting 25.0 mL to liters using 1 L = 1000 mL, the answer can have only one significant figure because 1 L has one significant figure."
  type: true-false
  answer: false
  explanation: "1 L = 1000 mL is an exact definition, so it does not limit precision. The answer, 0.0250 L, keeps the three significant figures of the measurement 25.0 mL."
```

## Explainer

When you read a measuring instrument, some digits are certain and the last is an estimate. Suppose a liquid in a graduated cylinder marked every 1 mL sits between 36 and 37 mL, a bit past halfway. You would record 36.6 mL. The 3 and 6 are certain, and the final 6 is your best estimate. All three digits are significant figures. Writing 36.6 tells a reader that the true value is likely within a few tenths of a milliliter.

Counting significant figures in a written number comes down to zeros. Nonzero digits always count. Zeros between nonzero digits count, as in 1.05. Leading zeros never count, so 0.0045 has two significant figures. Trailing zeros count when the number has a decimal point, so 2.50 has three. Trailing zeros in a whole number without a decimal point, such as 1500, are ambiguous. Scientific notation removes the doubt: 1.5 × 10³ has two significant figures, and 1.500 × 10³ has four.

Calculations should not create precision that the measurements lack. Two rules handle this. For multiplication and division, the answer has as many significant figures as the measured value with the fewest. Dividing 15.0 g by 4.2 mL gives 3.571…, which you report as 3.6 g/mL. For addition and subtraction, look at decimal places instead. The answer is rounded to the same decimal place as the least precise term. Adding 12.11, 18.0 and 1.013 gives 31.123, reported as 31.1.

Some numbers are exact and do not limit precision. Counted quantities, like 3 trials, and defined conversion factors, like 1 inch = 2.54 cm or 1 L = 1000 mL, have unlimited significant figures. Use the measured values to set the precision of the answer.

Keep all digits through a multistep calculation and round once at the end. Rounding along the way can shift the final digit. A calculator display such as 3.571428571 is raw arithmetic that you must round to match your data.

Significant figures are a quick shorthand for uncertainty. In laboratory courses you will meet a fuller treatment, in which uncertainties are calculated and propagated explicitly. The habit you build here, never reporting more than you measured, carries over directly.
