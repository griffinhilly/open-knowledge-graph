---
id: converting-metric-units
title: Converting Metric Units
domain: mathematics
course: 5th-grade
prerequisites:
- id: measurement-conversions-metric
  type: hard
- id: multiplying-dividing-by-powers-of-ten
  type: hard
- id: decimal-place-value
  type: hard
- id: mass-grams-kilograms
  type: soft
- id: measurement-conversions-5th
  type: soft
builds-toward: []
tags:
- measurement
- metric
- conversion
- decimals
stage: concrete-operations
status: validated
---
# Converting Metric Units

## Core Idea
In fifth grade, metric conversions are performed with decimal numbers, leveraging the power-of-ten structure: converting 3.5 kilometers to meters means multiplying by 1,000 (3,500 m); converting 425 milliliters to liters means dividing by 1,000 (0.425 L). This connects directly to multiplying and dividing by powers of ten. Students work fluently across length (km, m, cm, mm), mass (kg, g, mg), and capacity (kL, L, mL). The metric system's regularity means that once students understand the prefix pattern, they can convert any unit -- it is always a matter of multiplying or dividing by 10, 100, or 1,000.

## How It's Best Learned
Use the metric staircase or place-value chart to determine how many places to shift the decimal point. Practice with real measurements: "Your desk is 1.2 meters wide. How many centimeters is that?" Connect to the powers-of-ten topic explicitly. Include estimation: "Is 5,000 grams about 5 kilograms or 50? Does that make sense?"

## Common Misconceptions
- Moving the decimal point in the wrong direction.
- Confusing the number of places to move for different prefix pairs (km to mm is 6 places, not 3).
- Mixing up metric and customary conversion factors.

## Questions

```yaml
- question: "Convert 4.7 kilometers to meters."
  type: multiple-choice
  options:
    - "0.0047 m"
    - "47 m"
    - "470 m"
    - "4,700 m"
  answer: 3
  explanation: "1 kilometer = 1,000 meters, so multiply by 1,000. Multiplying by 1,000 moves the decimal point 3 places to the right: 4.7 → 4,700. The answer passes the intuition check: meters are smaller than kilometers, so going from km to m should give a larger number. Options A and B result from moving the decimal the wrong way or the wrong number of places."

- question: "A student converts 850 centimeters to meters and gets 85,000. They moved the decimal 3 places to the right. What went wrong?"
  type: multiple-choice
  options:
    - "They should have moved the decimal only 2 places, not 3"
    - "Converting to a larger unit means dividing — moving the decimal LEFT — not right; the correct answer is 8.5 m"
    - "There are only 10 centimeters in a meter, not 100"
    - "The answer is correct"
  answer: 1
  explanation: "The critical rule: going to a larger unit means you need fewer of them, so the number gets smaller — move the decimal LEFT (divide). 1 meter = 100 centimeters, so 850 cm ÷ 100 = 8.5 m. Moving right (multiplying) is used when converting to a smaller unit. The student applied the right number of places (2 for cm→m, not 3) but also moved in the wrong direction — a compound error."

- question: "Converting a measurement from a smaller unit to a larger unit always produces a larger number (for example, 500 cm becomes a number larger than 500 when converted to meters)."
  type: true-false
  answer: false
  explanation: "The opposite is true. Converting to a larger unit always produces a smaller number — you need fewer large units to describe the same length. 500 cm = 5 m, and 5 is much smaller than 500. The intuition check 'larger unit → smaller number, smaller unit → larger number' is the built-in sanity check for every metric conversion."

- question: "Multiplying a number by 1,000 and moving its decimal point 3 places to the right describe the exact same mathematical operation."
  type: true-false
  answer: true
  explanation: "Moving the decimal point one place to the right multiplies by 10 (5.0 → 50.0). Moving it 2 places multiplies by 100; 3 places multiplies by 1,000. The decimal-point shift notation is just a shorthand for the underlying place-value arithmetic. This connection is why metric conversions are so straightforward: each prefix step corresponds to exactly one decimal place shift."

- question: "How can you quickly check whether you moved the decimal point in the right direction when converting between metric units?"
  type: short-answer
  answer: "Ask: am I converting to a larger unit or a smaller unit? If larger (e.g., cm → m, g → kg), the number should get smaller — move the decimal left. If smaller (e.g., m → cm, kg → g), the number should get larger — move the decimal right. If your answer violates this — for instance, if you converted to meters and got a bigger number than your centimeter value — you moved the decimal the wrong way."
  explanation: "This direction check is more reliable than trying to remember 'multiply or divide' for each pair of units. It is grounded in a simple physical truth: larger units need fewer of them to cover the same quantity. Any answer that puts more of a larger unit than a smaller unit for the same measurement is automatically wrong."
```

## Explainer

You already know three things that come together here: the metric prefix system (kilo-, base, centi-, milli-), how multiplying and dividing by powers of ten shifts the decimal point, and how decimal place value works. Metric unit conversion in 5th grade is the intersection of all three — and once you see the connection, conversions become almost automatic.

The key insight is that **the metric system is a place-value system for measurement**. The prefix tells you the power of ten. "Kilo-" means ×1,000; "centi-" means ÷100; "milli-" means ÷1,000. So 1 kilometer = 1,000 meters, 1 meter = 100 centimeters, 1 centimeter = 10 millimeters. When you convert 3.5 kilometers to meters, you're multiplying by 1,000 — which (as you know from multiplying by powers of ten) moves the decimal point 3 places to the right: 3.5 → 3500. No mystery formula required.

The same logic applies in reverse when you convert to a larger unit. Converting 425 milliliters to liters means dividing by 1,000 — move the decimal 3 places to the left: 425 → 0.425. The direction rule is intuitive: going to a **larger unit** (ml → L), you get a **smaller number** (425 → 0.425). Going to a **smaller unit** (km → m), you get a **larger number** (3.5 → 3500). If your answer violates this intuition — like "5 meters is 500 kilometers" — you've moved the decimal the wrong way.

A useful mental tool is the **metric staircase**: imagine steps going down from kilogram → gram → milligram (or kilometer → meter → centimeter → millimeter). Each step down multiplies by 10; each step up divides by 10. To go from kilometers to centimeters (2 steps down, then 2 more steps down = 5 total steps), you multiply by 10⁵ = 100,000. The staircase makes it easy to count the steps and avoid the common error of moving the decimal the wrong number of places.

The power of the metric system is its regularity. Unlike customary units (12 inches per foot, 3 feet per yard, 1,760 yards per mile — all different!), every metric conversion is just a matter of which power of ten to use. Once you internalize the prefix pattern, you can convert any metric unit — even ones you've never seen before. A **microgram** uses the prefix "micro-" (×10⁻⁶), so 1 gram = 1,000,000 micrograms. The same logic scales infinitely.
