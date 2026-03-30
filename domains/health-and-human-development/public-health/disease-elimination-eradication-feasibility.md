---
id: disease-elimination-eradication-feasibility
title: 'Disease Elimination and Eradication: Feasibility and Requirements'
domain: health-and-human-development
course: public-health
prerequisites:
- id: basic-reproduction-number
  type: hard
- id: epidemiologic-study-designs
  type: soft
- id: vaccine-effectiveness-evaluation
  type: soft
builds-toward:
- infectious-disease-surveillance
- global-burden-of-disease
tags:
- eradication
- elimination
- control-targets
stage: advanced
status: validated
---

# Disease Elimination and Eradication: Feasibility and Requirements

## Core Idea
Eradication (zero cases worldwide) requires specific prerequisites: absence of animal reservoir (zoonotic diseases impossible to eradicate), availability of effective and practical intervention, R₀ amenable to control with available tools, and sustained political/economic commitment. Elimination (zero cases in specific regions) is achievable for more diseases. Only a few pathogens meet eradication criteria (smallpox succeeded; polio near success; measles eliminated regionally). Most disease control realistically aims for elimination or sustained low burden.

## How It's Best Learned
Compare requirements for eradication of three diseases: one successfully eradicated, one eliminated regionally, and one with zoonotic reservoir.

## Common Misconceptions
Using elimination and eradication synonymously—elimination is regional goal while eradication is global; eradication requires different conditions than elimination.

## Questions

```yaml
- question: "A global health organization proposes eradicating Plasmodium falciparum malaria through an intensive vaccination and treatment campaign targeting all human cases. What is the most fundamental biological obstacle to this goal?"
  type: multiple-choice
  options:
    - "Malaria has an R₀ too high to achieve herd immunity with any available vaccine"
    - "Malaria parasites develop drug resistance too rapidly to sustain control over a multi-decade campaign"
    - "Malaria is maintained in non-human primate reservoir hosts, so eliminating human cases cannot prevent reintroduction from animal sources"
    - "The malaria vaccine is not thermostable enough for use in the tropical regions where the disease is endemic"
  answer: 2
  explanation: "The presence of an animal reservoir is the most fundamental barrier to eradication — not vaccine efficacy, drug resistance, or logistics. Even if every human case were eliminated, zoonotic reintroduction from reservoir hosts would restart transmission. This is why zoonotic diseases cannot be eradicated regardless of how effective the intervention is against human cases: the pathogen has a survival route that bypasses human immunity entirely."

- question: "The 'ring vaccination' strategy that helped eradicate smallpox was specifically feasible because:"
  type: multiple-choice
  options:
    - "The smallpox vaccine was more effective than any vaccine before or since, achieving near-perfect protection"
    - "Smallpox had a very low R₀, requiring only modest population coverage to suppress transmission"
    - "The disease produced a clinically distinctive rash that made cases easy to identify, enabling rapid contact tracing and targeted vaccination"
    - "Smallpox had no asymptomatic carriers, so every infectious case was automatically detected"
  answer: 2
  explanation: "Ring vaccination targeted all contacts of identified cases rather than attempting universal coverage. This was feasible precisely because smallpox produced an obvious, distinctive rash that allowed rapid identification of cases and their contacts. Without this clinical visibility, contact tracing at the required speed would have been impossible. The strategy cut off transmission chains without needing to vaccinate entire populations."

- question: "If a disease has been eliminated from a country, it has been eradicated."
  type: true-false
  answer: false
  explanation: "Elimination means zero ongoing transmission in a defined geographic region; eradication means zero cases globally, permanently, with no further intervention required. An eliminated disease can re-emerge through international importation or reintroduction from animal reservoirs — eradication closes all such pathways globally. The distinction matters enormously for planning: elimination requires sustained surveillance, while eradication allows complete cessation of control efforts."

- question: "Vaccine-derived poliovirus (VDPV) outbreaks can occur when the live attenuated oral polio vaccine reverts to virulence in under-immunized populations."
  type: true-false
  answer: true
  explanation: "OPV uses attenuated live poliovirus that can accumulate mutations during replication and occasionally revert to a virulent form. In populations with low vaccination coverage, this vaccine-derived virus can circulate and cause outbreaks — a biological complication that has prolonged the final stage of polio eradication and necessitated the transition to inactivated polio vaccine (IPV), which cannot revert but provides weaker mucosal immunity."

- question: "Why does the distinction between 'elimination' and 'eradication' matter practically when planning disease control campaigns?"
  type: short-answer
  answer: "Elimination (no ongoing regional transmission) and eradication (no global cases, ever) require different biological prerequisites and resources. A disease with an animal reservoir can be locally eliminated but not globally eradicated, because the reservoir will reintroduce it. Conflating the terms risks wasting resources on biologically impossible eradication targets, or prematurely halting surveillance after elimination as though eradication had been achieved."
  explanation: "The practical consequence is that target-setting must precede resource allocation. Setting an eradication target for a zoonotic disease like malaria misdirects effort that could be better spent on control or regional elimination. Conversely, treating elimination as equivalent to eradication and relaxing vaccination campaigns (as happened with measles in some regions) can allow resurgence. Biological constraints should drive realistic goal-setting."
```

## Explainer

From your study of R₀ — the basic reproduction number — you know that a disease persists when R₀ > 1 and fades when effective transmission drops below that threshold. The **herd immunity threshold** (the fraction of a population that must be immune to halt transmission) is 1 − 1/R₀. For measles with an R₀ of ~15, about 93% of the population must be immune. For polio with R₀ ~5, roughly 80% coverage suffices. These numbers set the floor for what vaccination campaigns must achieve. But achieving and sustaining herd immunity at scale across national boundaries is very different from achieving it locally — and that difference is the gap between **elimination** (no ongoing transmission in a defined region) and **eradication** (zero cases globally, permanently, requiring no further intervention).

**Smallpox** succeeded as an eradication target because of a unique convergence of biological and logistical factors. The virus had no animal reservoir — it only circulated in humans, so stopping human transmission was sufficient. The vaccine was highly effective, heat-stable enough for use in the tropics, and conferred durable immunity. The disease was clinically obvious (the characteristic rash made cases easy to identify), enabling the ring vaccination strategy used in the final campaigns: instead of vaccinating everyone, teams vaccinated all contacts of identified cases, cutting off transmission chains. No other eradication campaign has faced all these conditions simultaneously.

**Polio** illustrates the obstacles. Oral polio vaccine (OPV) is cheap, easy to administer, and provides mucosal immunity that interrupts fecal-oral transmission — ideal properties. But OPV uses attenuated live virus, and in rare cases it reverts to virulence and causes vaccine-derived poliovirus (VDPV) outbreaks, particularly in under-immunized populations. The switch to inactivated polio vaccine (IPV) solves the reversion problem but provides weaker mucosal immunity, potentially allowing asymptomatic gut shedding even in vaccinated individuals. This biological complexity, combined with conflict zones that interrupt campaigns, has kept polio alive decades past its projected eradication date. The program remains the closest humanity has come to eradicating a second pathogen, but the last mile is the hardest.

**Malaria** illustrates why most diseases will never be candidates for eradication. Plasmodium parasites cycle through mosquito vectors and are maintained in non-human primate reservoirs (especially P. knowlesi in Southeast Asia). Even if every human case were eliminated, zoonotic reintroduction from animal hosts would restart transmission. Additionally, the parasite has an extraordinarily complex lifecycle spanning multiple biological stages in two hosts, making vaccine development difficult and drug resistance a persistent problem. For malaria and most other vector-borne and zoonotic diseases, realistic goals are **control** (reducing burden to acceptable levels) or regional **elimination** — achievable with sustained effort in specific settings, but not global eradication. Understanding these biological prerequisites before setting targets prevents the waste of resources on campaigns that cannot biologically succeed.
