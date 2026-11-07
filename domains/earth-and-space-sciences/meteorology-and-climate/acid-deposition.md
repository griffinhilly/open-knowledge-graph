---
id: acid-deposition
title: Acid Deposition (Acid Rain)
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: air-pollution-and-photochemical-smog
  type: hard
- id: ph-scale
  type: soft
- id: chemical-weathering
  type: soft
builds-toward: []
tags:
- acid-rain
- sulfur-dioxide
- nitrogen-oxides
- buffering
- air-pollution
- cap-and-trade
stage: formal-systems
status: validated
---

# Acid Deposition (Acid Rain)

## Core Idea
Clean rain is slightly acidic, with a pH near 5.6, because carbon dioxide dissolves in it to form weak carbonic acid. Sulfur dioxide and nitrogen oxides from burning fossil fuels react in the air to form sulfuric and nitric acid, which reach the surface in rain, snow, fog, and dry particles. This acid deposition can acidify lakes and streams, strip nutrients from forest soils, and dissolve limestone and marble. How much harm it does depends on the local bedrock and soil, which may or may not neutralize the acid.

## How It's Best Learned
Start with the pH scale and show that each whole unit is a tenfold change, so rain at pH 4.6 is ten times more acidic than clean rain at 5.6. Trace one sulfur atom from coal, to SO₂ in a smokestack plume, to sulfuric acid in a raindrop hundreds of kilometers downwind. Then compare two lakes that receive the same rain, one on limestone and one on granite, to show why buffering matters.

## Common Misconceptions
- Any rain with a pH below 7 is acid rain. (Unpolluted rain already has a pH of about 5.6 because of dissolved CO₂; acid rain is rain that is more acidic than this.)
- Acid rain falls only near the factories that cause it. (Tall smokestacks and winds carry SO₂ and NOx hundreds of kilometers, so damage is often far downwind.)
- Acid rain harms every lake equally. (Lakes on limestone or in soils rich in carbonate neutralize the acid; lakes on granite with thin soils are the most sensitive.)

## Questions

```yaml
- question: "Why is unpolluted rainwater slightly acidic, with a pH of about 5.6?"
  type: multiple-choice
  options:
    - "It contains dissolved salt from the ocean"
    - "Atmospheric carbon dioxide dissolves in it and forms carbonic acid"
    - "Lightning adds sulfuric acid to all rain"
    - "Water molecules are acidic by nature"
  answer: 1
  explanation: "CO₂ dissolves in cloud droplets and forms carbonic acid (H₂CO₃), a weak acid. In equilibrium with the atmosphere this gives a pH near 5.6. Acid rain is defined relative to this natural value."

- question: "Two lakes in the same region receive identical acid rain. Lake A sits on limestone bedrock, and Lake B sits on granite with thin soil. Which lake is more likely to become acidified, and why?"
  type: short-answer
  answer: "Lake B. Limestone (calcium carbonate) reacts with and neutralizes the acid, so Lake A is buffered. Granite and thin soils provide little buffering capacity, so the acid stays in Lake B and its pH falls."
  explanation: "Sensitivity depends on buffering capacity. This is why regions with granitic bedrock, such as parts of Scandinavia and the Adirondack Mountains, showed some of the worst lake acidification."

- question: "Rain with a pH of 4.6 is ten times more acidic than rain with a pH of 5.6."
  type: true-false
  answer: true
  explanation: "pH is a base-10 logarithmic scale of hydrogen ion concentration. A drop of one pH unit means ten times more hydrogen ions."

- question: "What has been the main cause of the large fall in acid deposition in the United States since about 1990?"
  type: multiple-choice
  options:
    - "Natural changes in rainfall patterns"
    - "Cuts in sulfur dioxide and nitrogen oxide emissions, including a cap-and-trade program for power plant SO₂"
    - "Adding lime to every lake in the country"
    - "A rise in atmospheric carbon dioxide that neutralized the acids"
  answer: 1
  explanation: "The 1990 Clean Air Act Amendments created the Acid Rain Program, which capped total SO₂ emissions from power plants and let companies trade allowances. Scrubbers, low-sulfur coal, and fuel switching cut emissions, and the acidity of rain fell in response."
```

## Explainer
You already know that sulfur dioxide (SO₂) and nitrogen oxides (NOx) are primary pollutants. Acid deposition is what happens to them after they leave the smokestack or tailpipe.

Begin with clean rain. Carbon dioxide dissolves in water and forms carbonic acid, so even pure rain has a pH of about 5.6. On the pH scale, each unit is a factor of ten. Rain with a pH of 4.6 has ten times more hydrogen ions than clean rain, and rain at 4.2 has about twenty-five times more. Values in the low 4s were common in the eastern United States and northern Europe in the 1970s and 1980s.

The extra acidity comes mainly from two reactions. SO₂, released mostly by burning coal, oxidizes in the air and dissolves in water to form sulfuric acid (H₂SO₄). NOx, from power plants and vehicles, forms nitric acid (HNO₃). The acids reach the ground in two ways. **Wet deposition** brings them down in rain, snow, and fog. **Dry deposition** settles acidic gases and particles directly onto surfaces. Because the reactions take hours to days, the acid often falls hundreds of kilometers from its source. Tall smokestacks built to protect nearby towns sent pollution from Britain and central Europe to Scandinavia.

Effects depend on what the acid lands on. In lakes on granite bedrock, pH can drop low enough to kill fish eggs and many invertebrates. Acidic water also releases aluminum from soils, which is toxic to fish. In forests, acid leaches calcium and magnesium from the soil and weakens trees, especially at high elevations. Limestone and marble buildings and statues slowly dissolve, because calcium carbonate reacts with the acid. Where bedrock is limestone, the same reaction protects lakes by neutralizing the acid.

The chemist Robert Angus Smith, who studied the air of industrial Manchester, introduced the term "acid rain" in the mid-1800s and set out his findings in his 1872 book *Air and Rain*. Large-scale action came much later. In the United States, the 1990 Clean Air Act Amendments set a cap on power plant SO₂ emissions and allowed companies to trade emission allowances. Sulfur emissions fell sharply, and rain became less acidic. Some lakes and soils are still recovering, because lost nutrients return slowly.
