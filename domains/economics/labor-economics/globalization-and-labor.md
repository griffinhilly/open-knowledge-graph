---
id: globalization-and-labor
title: Globalization and Labor
domain: economics
course: labor-economics
prerequisites:
- id: labor-demand-theory
  type: hard
- id: wage-determination
  type: soft
tags:
- trade
- offshoring
- Stolper-Samuelson
- China-shock
- labor-adjustment
stage: advanced
status: validated
---

# Globalization and Labor

## Core Idea
Globalization affects labor markets through trade in goods (which shifts product demand and thus labor demand across sectors), offshoring of tasks (which extends the substitution frontier beyond domestic automation to international wage competition), and immigration (covered separately). The Stolper-Samuelson theorem predicts that trade with low-wage countries reduces wages for the abundant factor in those countries (low-skilled labor in developed nations) while raising wages for scarce factors. The "China shock" literature (Autor, Dorn, Hanson) empirically documented that US communities more exposed to Chinese import competition experienced significant declines in manufacturing employment, wages, and labor force participation — with adjustment costs far exceeding what standard trade models predicted and persisting for over a decade.

## Questions

```yaml
- question: "The Stolper-Samuelson theorem predicts that when a developed country with abundant skilled labor opens trade with a developing country with abundant unskilled labor..."
  type: multiple-choice
  options:
    - "All workers in the developed country benefit from cheaper imports"
    - "Skilled workers in the developed country gain while unskilled workers lose, because increased imports reduce demand for unskilled-labor-intensive goods"
    - "All workers in the developing country are made worse off"
    - "Trade has no effect on wages in either country"
  answer: 1
  explanation: "Stolper-Samuelson predicts that trade benefits the factor used intensively in the export sector and hurts the factor used intensively in the import-competing sector. A skill-abundant developed country exports skill-intensive goods and imports unskilled-labor-intensive goods. This raises demand for skilled labor (higher wages) and reduces demand for unskilled labor (lower wages) in the developed country. The theorem shows that even though trade increases aggregate welfare, the distributional effects can be significant — there are clear losers."

- question: "Standard trade theory predicts that workers displaced by trade competition will quickly find comparable employment in expanding sectors."
  type: true-false
  answer: false
  explanation: "The China shock literature dramatically challenged this prediction. Autor, Dorn, and Hanson (2013) found that US communities exposed to Chinese import competition experienced persistent declines in manufacturing employment that were not offset by gains in other sectors. Displaced workers faced prolonged unemployment, lower re-employment wages, withdrawal from the labor force, and increased reliance on disability insurance and other transfers. These adjustment costs persisted for over a decade, far longer than standard models with frictionless labor mobility predict."

- question: "How does task offshoring differ from traditional trade in goods, and what are its labor market implications?"
  type: short-answer
  answer: "Traditional trade involves exchanging finished goods — a country imports cars and exports software. Task offshoring involves relocating specific tasks within a production process to other countries — a US firm keeps product design in-house but offshores data entry to India. The labor market implication is that offshoring exposes individual tasks (not just entire industries) to international wage competition. This means that even workers in 'non-tradable' service occupations can face competitive pressure if their specific tasks can be performed remotely from a low-wage country."
  explanation: "Blinder and Grossman-Rossi-Hansberg developed models of task offshoring that show how it differs from Heckscher-Ohlin trade in goods. Offshoring fragments the production process geographically, putting competitive pressure on specific tasks rather than entire occupations. A radiologist reading X-rays faces offshoring pressure if the images can be transmitted digitally, while a surgeon performing operations does not. This task-level analysis overlaps with the automation literature — both identify vulnerability based on task characteristics rather than traditional skill categories."
```

## Explainer

Globalization has reshaped labor markets in ways that standard trade models failed to fully anticipate. The theoretical prediction — that trade creates net gains for both countries — is well-established. But the distributional consequences within countries and the adjustment costs for affected workers have proven far more severe and persistent than economists expected, creating a significant gap between aggregate welfare gains and the lived experience of workers in trade-exposed communities.

The Stolper-Samuelson theorem provides the theoretical foundation for understanding trade's distributional effects. In a two-factor, two-good Heckscher-Ohlin model, trade with a labor-abundant developing country reduces the price of labor-intensive goods in the developed country. This benefits consumers (cheaper goods) but hurts domestic producers of those goods and the workers they employ. The theorem predicts that the real wage of unskilled labor falls in the developed country — not just in the specific competing industry but economy-wide, because factor prices are determined by good prices in general equilibrium. The magnitude depends on the price change and on factor intensities.

The China shock represents the empirical testing of these predictions on a massive scale. China's entry into the WTO in 2001 and its rapid manufacturing growth produced a surge in imports to the US and other developed countries. Autor, Dorn, and Hanson (2013, 2016) used the variation in exposure to Chinese imports across US commuting zones to estimate causal effects. The findings were stark: regions more exposed to import competition experienced significant and persistent declines in manufacturing employment, with limited offsetting growth in other sectors. Workers displaced from manufacturing faced lower wages, longer unemployment spells, higher rates of labor force withdrawal, and increased reliance on government transfers. These effects persisted for over a decade.

The persistence of adjustment costs challenged the benign view of trade adjustment embedded in standard models. In the textbook, workers displaced from import-competing sectors move smoothly to expanding sectors. In reality, workers face geographic immobility (unwilling or unable to relocate), skill mismatch (manufacturing skills do not transfer easily to service jobs), age barriers (older workers face greater retraining costs), and search frictions. The transition from a $25/hour manufacturing job to a $12/hour service job — even if such a job is available — represents a genuine welfare loss that aggregate GDP statistics may obscure.

Task offshoring adds another dimension to globalization's labor market effects. Advances in information and communication technology have made it possible to fragment production processes geographically — keeping some tasks (design, marketing, management) in the developed country while offshoring others (data processing, customer service, programming) to low-wage countries. This extends competitive pressure from manufactured goods to services, potentially affecting a much wider range of occupations. Blinder estimated that 22-29% of US jobs were potentially offshorable — not because they would all be offshored, but because the tasks they involve could in principle be performed remotely. The task characteristics that determine offshorability (codifiability, lack of face-to-face requirement, transmissibility over telecommunications) overlap significantly with those that determine automatability, suggesting that technology and globalization jointly shape labor market restructuring.
