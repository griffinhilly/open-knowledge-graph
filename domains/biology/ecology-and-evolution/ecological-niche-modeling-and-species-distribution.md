---
id: ecological-niche-modeling-and-species-distribution
title: Ecological Niche Modeling and Species Distribution Modeling
domain: biology
course: ecology-and-evolution
prerequisites:
- id: niche-concept-fundamental-realized
  type: hard
- id: ecological-niche-overlap-and-differentiation
  type: soft
builds-toward:
- climate-change-ecology
tags:
- niche-modeling
- species-distribution
- ecological-niche
stage: formal-systems
status: draft
---

# Ecological Niche Modeling and Species Distribution Modeling

## Core Idea
Ecological niche models predict species distributions by identifying suitable environmental conditions. These correlative models use occurrence data and environmental variables (temperature, precipitation, elevation, vegetation) to build potential habitat maps. Niche models enable prediction of suitable areas in unsampled regions and range shifts under climate change. However, models assume current niches are stable, ignore biotic interactions, and vary in accuracy depending on data quality.

## Questions

```yaml
- question: "An ENM trained on a species' current distribution predicts large areas of suitable habitat on a neighboring continent where the species has never been recorded. The most scientifically cautious interpretation is:"
  type: multiple-choice
  options:
    - "The model is incorrect — if the habitat were suitable, the species would already be present there"
    - "The region is definitely suitable and should be immediately targeted for translocation of the species"
    - "The region may be environmentally suitable, but dispersal barriers or historical contingency may have prevented colonization — the model cannot distinguish these explanations"
    - "The model has overfit to current climate variables and the out-of-range prediction should be disregarded"
  answer: 2
  explanation: "This limitation is fundamental to ENMs. The model learns the association between occurrence locations and environmental conditions, then projects that association onto the full map. But absence from a region can mean 'conditions are unsuitable' OR 'the species hasn't reached it yet.' The model cannot distinguish these because it has no information about dispersal history or barriers. This is why predicted suitable areas in never-colonized regions require careful biological interpretation before being acted upon."

- question: "A climate change projection predicts 3°C warming by 2100. An ENM projects the species' current niche onto the future climate scenario and predicts a 40% range contraction. What critical assumption does this projection require, and what would violate it?"
  type: multiple-choice
  options:
    - "The assumption that the species can freely disperse to newly suitable areas; violation: geographic barriers limiting movement"
    - "The assumption of niche conservatism — that the species' environmental tolerances remain stable over time; violation: evolutionary adaptation of thermal tolerance by 2100"
    - "The assumption that climate variables matter more than biotic interactions; violation: strong competitive exclusion in the new range"
    - "The assumption that the current distribution reflects the full fundamental niche; violation: the current range being limited by competition"
  answer: 1
  explanation: "ENMs assume niche conservatism — that the species' relationship with environmental variables will not change over the projection period. If the species adapts its thermal tolerance through evolution over 80 years, the model's predictions become invalid because the niche it learned no longer describes the species. This is often flagged as a limitation when projecting ENMs into future climate scenarios. Dispersal limitation (option A) is also a real concern but affects range expansion predictions, not the contraction prediction implied here."

- question: "Ecological niche models trained on occurrence data reflect the species' realized niche, not its full fundamental niche."
  type: true-false
  answer: true
  explanation: "Occurrence records show where a species actually lives, which is always a subset of where it could physiologically tolerate — competition, predation, dispersal limits, and human impacts all compress the realized niche inside the fundamental niche. ENMs therefore learn the realized niche (or an approximation of it). This means ENMs will often underestimate the full range of conditions a species could tolerate if biotic constraints were removed, which is relevant when predicting invasive species spread or assisted colonization."

- question: "MaxEnt and other presence-only ENMs can reliably distinguish between habitat that is environmentally unsuitable and habitat the species simply hasn't colonized yet."
  type: true-false
  answer: false
  explanation: "This is a fundamental limitation of all ENMs based on occurrence data. Absence of records can mean 'conditions are unsuitable,' 'the species hasn't arrived yet,' or 'the area is under-surveyed.' The model cannot separate these explanations — it only knows where the species has been found and what environmental conditions characterize those locations. Interpreting predicted-suitable but unoccupied regions requires independent biological knowledge about dispersal capacity, biogeographic barriers, and survey completeness."

- question: "What does it mean to say that ENMs 'project the niche in environmental space onto geographic space,' and why does this distinction matter for interpreting model outputs?"
  type: short-answer
  answer: "Environmental space describes a species' niche as a combination of abiotic conditions it can tolerate (e.g., temperature 5–20°C, precipitation 400–1200mm). ENMs learn this envelope from occurrence records, then identify all geographic locations on the map where those environmental conditions are present. The distinction matters because the same environmental conditions can exist in multiple geographically separated places (suitable climate on two continents), and geographic space can contain barriers (oceans, mountain ranges) that prevent access to environmentally suitable areas. The model outputs tell you where conditions are right — not where the species is, can get to, or will actually survive given biotic interactions."
  explanation: "Conflating environmental suitability with predicted presence is a common misuse of ENM outputs. A high suitability score means 'the environmental conditions here resemble conditions where the species occurs' — it does not guarantee the species will be there, can reach there, or will persist there against competitors and predators. Understanding this distinction is essential for correctly interpreting range shift projections, invasive species risk maps, and conservation prioritization analyses."
```

## Explainer

From your study of the niche concept, you know that every species occupies a **fundamental niche** defined by the full range of environmental conditions it could tolerate, and a **realized niche** that is typically smaller due to competition and other biotic interactions. You also know from niche overlap and differentiation that species partition environmental space in predictable ways. **Ecological niche modeling (ENM)** takes these concepts and turns them into quantitative, spatial predictions: given what we know about where a species has been found, what environmental conditions characterize those locations, and where else on the map do similar conditions exist?

The basic approach is conceptually straightforward. You start with **occurrence data** — confirmed locations where the species has been observed, often from museum specimens, field surveys, or citizen science databases. You then associate each occurrence point with **environmental variables** at that location: mean annual temperature, precipitation seasonality, elevation, soil type, vegetation index, and similar layers typically available as gridded spatial datasets. A statistical or machine-learning algorithm (such as MaxEnt, random forests, or generalized linear models) then learns the relationship between species presence and environmental conditions. The output is a map showing the predicted **environmental suitability** across the landscape — essentially, the model identifies the species' niche in environmental space and projects it onto geographic space.

The most widely used tool, **MaxEnt** (Maximum Entropy), works with presence-only data — you supply locations where the species was found, and the algorithm contrasts those environmental conditions against the background environment available in the study region. It finds the probability distribution across environmental space that is maximally spread out (maximum entropy) while still matching the constraints imposed by the occurrence data. The result is a continuous suitability surface, typically ranging from 0 (unsuitable) to 1 (highly suitable). Other approaches require both presence and absence data, or use pseudo-absences generated by randomly sampling locations where the species was not recorded.

These models have powerful applications but carry important limitations. Their most common use is **predicting range shifts under climate change**: project the current niche model onto future climate scenarios and see where suitable habitat will exist in 50 or 100 years. They can also identify potential habitat for rare or invasive species in areas that have not been surveyed. However, ENMs model the realized niche (or an approximation of it) based on current distributions, which embed existing biotic interactions, dispersal limitations, and historical contingencies. The model cannot distinguish between "the species cannot tolerate those conditions" and "the species hasn't reached that area yet." It also assumes **niche conservatism** — that the species' environmental requirements will remain stable over time — which may not hold if populations adapt. Despite these caveats, niche models are among the most practical tools ecologists have for translating niche theory into spatial predictions, and their outputs directly inform conservation planning, reserve design, and invasive species management.
