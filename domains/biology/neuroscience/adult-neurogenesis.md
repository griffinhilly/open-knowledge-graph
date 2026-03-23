---
id: adult-neurogenesis
title: Adult Neurogenesis and Neural Plasticity
domain: biology
course: neuroscience
prerequisites:
- id: cell-cycle-overview
  type: hard
- id: neuron-structure-and-function
  type: hard
tags:
- neural-development
- plasticity
stage: expert
status: validated
---

# Adult Neurogenesis and Neural Plasticity

## Core Idea
New neurons born from stem cells in dentate gyrus (learning/memory) and olfactory bulb (smell). New neurons express LTP, integrate into circuits. Enhanced by exercise/enrichment; reduced by stress/aging.

## Questions

```yaml
- question: "A neuroscientist argues that newly born neurons in the adult hippocampus serve a special computational function beyond simply adding to the total neuron count. Which specific property of young granule cells during their critical window (roughly 1–6 weeks after birth) supports this argument?"
  type: multiple-choice
  options:
    - "Young neurons are larger than mature granule cells, allowing them to form more synapses simultaneously"
    - "Young neurons are hyperexcitable and display enhanced LTP compared to mature granule cells, giving them heightened plasticity for encoding new experiences"
    - "Young neurons form connections exclusively to the CA1 region, bypassing the normal dentate gyrus circuit"
    - "Young neurons express different neurotransmitter receptors than mature cells, allowing them to detect inputs that mature cells ignore"
  answer: 1
  explanation: "The key functional property of young granule cells is their heightened plasticity during a critical window ~1–6 weeks after birth: they are hyperexcitable and express enhanced long-term potentiation (LTP) compared to mature granule cells. This makes them particularly effective at encoding new information. Their proposed computational role is pattern separation — distinguishing similar inputs from each other to prevent memory interference. Adding fresh, highly plastic neurons to the dentate gyrus input gateway may help maintain this discrimination as new experiences accumulate on top of old ones."

- question: "In which brain region is adult-born hippocampal neurogenesis thought to contribute most directly to the ability to distinguish between similar but distinct memories and contexts?"
  type: multiple-choice
  options:
    - "CA3 — because it performs pattern completion and needs new inputs"
    - "The subventricular zone — because it receives diverse cortical inputs"
    - "The dentate gyrus — because it is the input gateway to the hippocampus and must produce distinct output representations from overlapping inputs (pattern separation)"
    - "CA1 — because it integrates output from the entire hippocampal circuit"
  answer: 2
  explanation: "The dentate gyrus is the input gateway to the hippocampus, receiving projections from entorhinal cortex and projecting via mossy fibers to CA3. Its computational function is pattern separation: taking overlapping input patterns and producing distinct, non-interfering output representations. New granule cells born in the subgranular zone integrate into the dentate gyrus circuit over weeks. Their heightened plasticity during the critical window may be specifically suited to this pattern separation function — continuously adding fresh neurons keeps the system capable of encoding new similar experiences without overwriting old ones."

- question: "The prevailing scientific consensus throughout most of the 20th century was that adult neurogenesis occurs throughout the brain at very low rates, which is why it went unappreciated for so long."
  type: true-false
  answer: false
  explanation: "The prevailing dogma was more absolute than this: most neuroscientists believed adult neurogenesis did not occur at all. The dogma held that you are born with your full complement of neurons, they die off over a lifetime, and that is that. This made the discovery of adult neurogenesis in specific regions genuinely surprising and initially controversial. The finding was not that low-rate neurogenesis was discovered to be higher — it was that neurogenesis was discovered to exist at all in the adult mammalian brain. This is why it represented such a significant paradigm shift."

- question: "Chronic stress and elevated glucocorticoids suppress hippocampal neurogenesis, which may contribute to the memory impairments and hippocampal volume reductions observed in depression and PTSD."
  type: true-false
  answer: true
  explanation: "This is one of the strongest connections between adult neurogenesis and clinical neuroscience. Glucocorticoids (stress hormones) suppress the proliferation and survival of new neurons in the dentate gyrus. Chronic stress — which chronically elevates glucocorticoids — reduces neurogenesis substantially. Depression and PTSD are associated with hippocampal volume reductions and impaired contextual memory, and both conditions involve chronic stress and glucocorticoid dysregulation. Conversely, many effective antidepressants increase neurogenesis, and some researchers have proposed that neurogenesis is a necessary mechanism for antidepressant efficacy — though this remains actively debated."

- question: "Why might the continuous addition of new neurons to the dentate gyrus be functionally important for memory, rather than simply increasing the total number of neurons over time?"
  type: short-answer
  answer: "The dentate gyrus performs pattern separation — it must take overlapping input patterns from entorhinal cortex and produce distinct, non-interfering output representations. As new memories accumulate, the risk of interference between similar experiences grows. Continuously adding fresh, highly plastic neurons may solve this by providing new encoding units that have not yet been shaped by prior experiences, allowing similar new events to be distinguished from similar old ones. The function is not to increase total neuron count but to maintain the capacity for discrimination as the system fills up with encoded experiences — a biological solution to the problem of catastrophic interference."
  explanation: "This reframes neurogenesis from a quantity question ('more neurons are better') to a quality/timing question ('fresh neurons with heightened plasticity at the right time do something mature neurons cannot'). The comparison to catastrophic interference in artificial neural networks makes the computational logic vivid: systems that continuously learn on top of old representations eventually lose the ability to distinguish similar inputs without some mechanism for refreshing representational capacity."
```

## Explainer

For most of the twentieth century, neuroscience operated under a firm dogma: the adult brain does not produce new neurons. You are born with your full complement, they die off over a lifetime, and that is that. This turned out to be wrong. **Adult neurogenesis** — the birth of new neurons from neural stem cells in the mature brain — occurs in at least two well-established regions: the **subgranular zone** of the hippocampal dentate gyrus and the **subventricular zone** lining the lateral ventricles, whose new neurons migrate to the olfactory bulb. From your prerequisite knowledge of the cell cycle, you can appreciate that these stem cells retain the ability to divide asymmetrically, producing one daughter cell that remains a stem cell and another that differentiates into a neuron.

The hippocampal newborn neurons are especially interesting because of where they end up. The dentate gyrus is the input gateway to the hippocampus, the structure most critical for forming new declarative memories. New granule cells born in the subgranular zone migrate a short distance into the granule cell layer, extend dendrites into the molecular layer, and send axons along the mossy fiber pathway to CA3 — integrating into the existing circuit over a period of weeks. During a critical window roughly 1–6 weeks after birth, these young neurons are hyperexcitable and display enhanced **long-term potentiation** (LTP) compared to mature granule cells. This heightened plasticity may give them a special role in encoding new memories, particularly in distinguishing similar experiences — a computational function called **pattern separation**.

What controls the rate of neurogenesis reads like a summary of lifestyle medicine. **Exercise** — particularly aerobic running — robustly increases the proliferation and survival of new neurons in the dentate gyrus, an effect mediated in part by brain-derived neurotrophic factor (BDNF) and increased blood flow. **Environmental enrichment** — novel objects, social interaction, cognitive challenge — promotes the survival and integration of neurons that have already been born. Conversely, **chronic stress** and elevated glucocorticoids suppress neurogenesis, which may contribute to the hippocampal volume reductions and memory impairments seen in depression and PTSD. Aging also reduces the rate of new neuron production, though it does not eliminate it entirely, and the degree of age-related decline varies considerably across individuals.

The functional significance of adult neurogenesis remains an active area of research, but converging evidence from rodent studies suggests that disrupting hippocampal neurogenesis impairs the ability to distinguish between similar contexts and memories while leaving other forms of learning intact. This fits neatly with the computational demands of the dentate gyrus: it must take overlapping input patterns from entorhinal cortex and produce distinct output representations. Continuously adding fresh, highly plastic neurons may be the brain's strategy for keeping this discrimination sharp as new experiences accumulate — a biological solution to the problem of catastrophic interference that plagues many artificial learning systems.
