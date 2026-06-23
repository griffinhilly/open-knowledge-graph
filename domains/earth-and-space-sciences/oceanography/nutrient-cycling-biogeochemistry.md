---
id: nutrient-cycling-biogeochemistry
title: Nutrient Cycling and Biogeochemistry in the Ocean
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: ocean-chemistry-and-nutrients
  type: hard
- id: marine-biological-pump
  type: hard
- id: dissolved-oxygen-biogeochemical-cycles
  type: soft
- id: marine-nutrient-cycling-limitation
  type: soft
builds-toward:
- coastal-eutrophication-blooms
tags:
- nutrients
- nitrogen-cycle
- phosphorus
- iron-limitation
- redox-chemistry
stage: advanced
status: validated
---
# Nutrient Cycling and Biogeochemistry in the Ocean

## Core Idea
Essential nutrients (nitrogen, phosphorus, iron, silica) cycle between dissolved, particulate, and biological forms through photosynthesis, decomposition, and redox reactions. Understanding these cycles reveals why nutrient availability limits primary productivity and controls the efficiency of the biological carbon pump.

## How It's Best Learned
Trace nitrogen through the nitrate-nitrite-ammonium cycle. Use vertical profiles to infer regeneration rates from nutrient-oxygen relationships. Model nutrient remineralization during particle sinking.

## Common Misconceptions
Phosphorus is not universally limiting in oceans; nitrogen often limits in lower latitudes and iron in high-nutrient, low-chlorophyll (HNLC) regions. Nutrient ratios are not fixed—they vary with water mass age and redox state. Regenerated nutrients drive productivity just as much as upwelled nutrients.

## Questions

```yaml
- question: "In open-ocean water samples, oxygen levels are highest near the surface and decrease with depth, while nitrate levels are lowest at the surface and increase with depth. What is the most direct explanation for this inverse relationship?"
  type: multiple-choice
  options:
    - "Sunlight bleaches dissolved oxygen from deep water while photochemically destroying nitrate at the surface"
    - "Physical mixing pushes oxygen-rich water to depth while concentrating nutrients at the surface"
    - "Photosynthesis at the surface consumes nutrients and produces oxygen; respiration and remineralization at depth consume oxygen and regenerate dissolved nutrients"
    - "Nitrogen-fixing bacteria concentrate at depth, converting N2 to nitrate while consuming oxygen"
  answer: 2
  explanation: "This inverse profile is the signature of biological cycling. Near the surface, phytoplankton photosynthesize, consuming nitrate (and other nutrients) to build organic molecules while producing oxygen. As organisms die and sink, bacteria remineralize the organic matter at depth, consuming oxygen and releasing nutrients back into dissolved form. The result is a predictable mirror-image relationship: low nutrients and high oxygen at the productive surface; high nutrients and low oxygen at depth where decomposition dominates. This inverse coupling is one of the most diagnostic patterns in chemical oceanography."

- question: "A research vessel sampling the Southern Ocean finds high concentrations of nitrate and phosphate but very low phytoplankton biomass. What is the most likely explanation for the low productivity despite abundant macronutrients?"
  type: multiple-choice
  options:
    - "Water temperatures are too cold for phytoplankton to photosynthesize efficiently"
    - "Nitrate concentrations exceed phytoplankton physiological tolerance, suppressing growth"
    - "Iron is the limiting nutrient — the Southern Ocean receives little iron from continental dust, leaving phytoplankton iron-deficient despite high macronutrients"
    - "Phosphorus is depleted relative to the Redfield ratio despite appearing abundant in absolute terms"
  answer: 2
  explanation: "This is a high-nutrient, low-chlorophyll (HNLC) region, and the Southern Ocean is the canonical example. Phytoplankton require iron for photosynthetic enzymes and nitrogen metabolism. The Southern Ocean is far from continents — the primary source of iron via dust deposition — so iron inputs are extremely low. Despite abundant nitrate and phosphate, phytoplankton cannot grow because of iron deficiency. This was directly confirmed by iron fertilization experiments: adding small amounts of iron produced rapid phytoplankton blooms in these normally unproductive waters."

- question: "The inverse relationship between dissolved oxygen and nutrient concentrations with ocean depth is primarily a consequence of biological processes rather than purely physical or chemical ones."
  type: true-false
  answer: true
  explanation: "This profile is a direct biological fingerprint. Oxygen is produced at the surface by photosynthesis and consumed at depth by respiration; nutrients are consumed at the surface during growth and regenerated at depth during decomposition. The two profiles mirror each other because they are driven by the same biology: every molecule of organic matter produced at the surface simultaneously incorporates nutrients and produces oxygen, and every molecule decomposed at depth releases nutrients and consumes oxygen. Physical mixing alone would tend to homogenize both profiles; their divergence with depth is what biology imposes."

- question: "Phosphorus is the primary nutrient limiting marine primary productivity in most ocean regions."
  type: true-false
  answer: false
  explanation: "Nutrient limitation varies by ocean region and cannot be generalized to a single nutrient. In the subtropical open ocean, nitrogen (as nitrate) is often the limiting macronutrient. In high-nutrient, low-chlorophyll regions like the Southern Ocean, subarctic Pacific, and equatorial Pacific, iron limits productivity despite abundant nitrate and phosphate. Phosphorus limitation may apply in some freshwater systems but is not the universal rule in marine environments. The identity of the limiting nutrient must be determined empirically for each region, and it can shift with season, depth, and physical forcing."

- question: "What does the Redfield ratio of 106C:16N:1P tell oceanographers about nutrient cycling, and how do deviations from this ratio help identify which nutrient is limiting productivity in a given water mass?"
  type: short-answer
  answer: "The Redfield ratio describes the average elemental composition of marine organic matter and therefore the ratio in which nutrients are consumed during phytoplankton growth and regenerated during decomposition. It acts as a stoichiometric benchmark for biological activity. When the observed N:P ratio in a water mass deviates from 16:1 — for example, if nitrate is disproportionately depleted relative to phosphate — it signals that biology has stripped nitrogen preferentially, indicating nitrogen limitation. Conversely, if phosphate is depleted relative to nitrogen, phosphorus may be the constraint. Deviations from Redfield ratios are a record of biological activity and a diagnostic of what is constraining further production."
  explanation: "Redfield discovered in the 1930s that the elemental ratios of dissolved nutrients in deep ocean water closely matched the elemental composition of marine organisms — implying that life shapes ocean chemistry on a global scale. This is a profound finding: the chemical composition of the ocean is not a purely geological property but is actively maintained by biological cycling. Because the ratio reflects what organisms need to build biomass, the ratio in which nutrients are consumed and regenerated stays approximately constant. Departures from this ratio therefore indicate either unusual community composition or a specific nutrient input or loss that breaks the stoichiometric coupling."
```

## Explainer

You already understand that the ocean contains dissolved nutrients essential for life and that the biological pump moves carbon and nutrients from the surface to depth. Now consider the full biogeochemical cycle — the continuous loop of nutrient uptake, export, decomposition, and return. The key nutrients are **nitrogen** (as nitrate, nitrite, and ammonium), **phosphorus** (as phosphate), **iron**, and **silica** (needed by diatoms for their glass-like shells). Phytoplankton in the sunlit surface layer consume these nutrients to build organic molecules. When these organisms die or are eaten and excreted, the organic matter sinks as particles — marine snow — carrying nutrients downward out of the productive zone.

As sinking particles descend, bacteria decompose them in a process called **remineralization**, releasing dissolved nutrients back into the water. This is why nutrient concentrations are low at the surface (where biology consumes them) and high at depth (where decomposition releases them). The vertical nutrient profile is nearly a mirror image of the dissolved oxygen profile: where oxygen is consumed by respiration, nutrients are regenerated. This inverse relationship between oxygen and nutrients is one of the most diagnostic features in oceanography and lets you infer biological activity from chemical measurements alone.

Not all nutrients behave the same way. Nitrogen cycling is especially complex because nitrogen exists in multiple oxidation states, and transformations between them are mediated by different microbial communities. **Nitrogen fixation** (converting N₂ gas to bioavailable ammonium) adds new nitrogen to the ocean, performed by specialized cyanobacteria like *Trichodesmium*. **Nitrification** converts ammonium to nitrite and then nitrate in oxygenated waters. **Denitrification** removes bioavailable nitrogen by converting nitrate back to N₂ gas, and this occurs primarily in low-oxygen environments — linking nitrogen cycling directly to oxygen minimum zones. Phosphorus, by contrast, has no gaseous phase and cycles more simply between organic and inorganic dissolved forms. **Iron** is often the limiting nutrient in vast regions of the Southern Ocean and subarctic Pacific — the so-called high-nutrient, low-chlorophyll (HNLC) regions — because iron supply depends on dust deposition from continents rather than on internal ocean recycling.

The ratio in which organisms consume nutrients matters enormously. The **Redfield ratio** (roughly 106 carbon : 16 nitrogen : 1 phosphorus) describes the average elemental composition of marine organic matter and, consequently, the ratio in which nutrients are consumed and regenerated. Deviations from this ratio reveal which nutrient is limiting production in a given region. Understanding nutrient cycling is not merely descriptive — it is the mechanistic foundation for predicting how ocean productivity will respond to changes in circulation, warming, and oxygen loss, all of which alter the rates and pathways by which nutrients move through the system.
