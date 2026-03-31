---
id: experimental-economics-methods
title: Experimental Economics Methods
domain: economics
course: behavioral-economics
prerequisites:
- id: bounded-rationality
  type: soft
tags:
- experimental-methods
- incentive-compatibility
- lab-experiments
- deception
stage: advanced
status: validated
---

# Experimental Economics Methods

## Core Idea
Experimental economics tests economic theories through controlled laboratory experiments with real monetary incentives. Its methodological principles — first articulated by Vernon Smith — include induced value theory (monetary payments control the utility function), saliency (payoffs must be large enough to matter), dominance (reward structure dominates other motivations), and no deception (unlike psychology experiments, economists typically never deceive participants, preserving the credibility of the experimental environment). These methods enable causal identification of how institutions, incentives, and information structures affect behavior. The field has produced fundamental insights about market efficiency, auction design, public goods provision, and bargaining, and earned Smith the 2002 Nobel Prize alongside Kahneman.

## Questions

```yaml
- question: "Experimental economics insists on using real monetary incentives rather than hypothetical payoffs. The primary justification for this practice is..."
  type: multiple-choice
  options:
    - "It makes experiments more expensive and therefore more prestigious"
    - "Induced value theory — real payoffs ensure that participants' decisions are motivated by the experimental incentives, allowing the experimenter to control the relevant utility function"
    - "Hypothetical payoffs always produce random behavior"
    - "Regulatory requirements mandate real payments"
  answer: 1
  explanation: "Induced value theory (Smith, 1976) holds that real monetary payments can induce a controlled utility function over experimental outcomes, ensuring that participants' choices reflect the incentive structure the experimenter designed. Without real payoffs, participants may treat choices as hypothetical and not engage seriously, or they may bring their own uncontrolled preferences into the experiment. Real incentives make the experimental situation economically meaningful and provide the experimenter with greater control over the decision environment."

- question: "Economics experiments typically prohibit deception of participants, while psychology experiments commonly allow it."
  type: true-false
  answer: true
  explanation: "The economics experimental tradition has a strong norm against deception — experimenters must truthfully describe the experiment's structure and payoffs. The rationale is that if participants know deception is possible, they will not trust the experimental instructions, undermining induced value theory and making future experiments in the same participant pool unreliable. Psychology has a more permissive tradition (with IRB oversight and debriefing). This methodological difference reflects different priorities: economists prioritize incentive control while psychologists prioritize naturalistic responses to manipulations."

- question: "What are the advantages and limitations of laboratory experiments compared to field experiments in economics?"
  type: short-answer
  answer: "Lab experiments offer high internal validity (tight control over variables, randomization, precise measurement) but limited external validity (artificial setting, student participants, small stakes may not generalize to real markets). Field experiments offer higher external validity (real participants, real stakes, real institutional context) but lower internal validity (less control over confounding variables, harder to precisely measure mechanisms). The best research programs use both, with lab experiments to identify mechanisms and field experiments to test generalizability."
  explanation: "The lab-field trade-off is a central methodological tension. Lab experiments can test precise theoretical predictions about how changes in information, incentives, or institutions affect behavior — but the sterile laboratory setting and typical reliance on university students raise questions about whether findings generalize. Field experiments (like Gneezy and List's work on gift exchange, or Levitt and List's studies of market behavior) sacrifice some control for realism. The emergence of online experiments (MTurk, Prolific) has created a middle ground with larger, more diverse participant pools but less control than physical labs."
```

## Explainer

Experimental economics is the methodological backbone of behavioral economics — it provides the controlled environments in which theoretical predictions of both standard and behavioral models are tested against actual human behavior. Without the ability to create real economic situations in the laboratory, behavioral economics would be limited to observational data and thought experiments. Understanding the methodological principles is essential because they determine what can and cannot be concluded from experimental evidence.

The foundational methodological framework was articulated by Vernon Smith in the 1960s-80s. Induced value theory states that by paying participants real money based on their decisions, the experimenter can control the relevant utility function. If the experimenter pays you more when you choose A over B, and the payments are large enough to matter (saliency) and dominate other considerations (dominance), then your choice between A and B reflects the experimental incentive structure rather than unobserved personal preferences. This principle allows economists to test predictions about how rational agents should behave under specific incentive structures, because the experimenter knows the incentive structure with precision.

The no-deception norm is one of the sharpest methodological differences between economics and psychology. In a typical psychology experiment, participants might be given false feedback about their performance, told a cover story about the experiment's purpose, or presented with a confederate posing as another participant. Economics experiments reject all of these practices. The reasoning is both ethical and practical: if participants believe deception is possible, they will not take the experimental instructions at face value, and the experimenter loses control over the perceived incentive structure. An experimental economics lab builds its reputation on the commitment that "what we tell you is true," and this reputation is a shared resource that no individual experimenter should deplete.

Experimental designs in economics range from simple individual decision tasks (lottery choices for testing risk preferences, intertemporal choices for testing discounting) to complex market institutions (double auctions, posted-offer markets, sealed-bid auctions). Smith's early market experiments produced one of the field's most striking findings: simple double-auction markets converge to competitive equilibrium rapidly, even with very few traders who have no knowledge of economic theory. This result supported the efficiency of market institutions while simultaneously showing that individual rationality is not required for market-level efficiency — a finding that complicates the behavioral economics narrative.

The limitations of laboratory experiments have driven the field toward complementary methods. Field experiments — randomized controlled trials conducted in real economic settings — address external validity concerns by testing behavioral interventions in their intended context. Natural experiments exploit random or quasi-random variation in real-world policies to estimate causal effects. Online experiments expand participant diversity beyond the university student populations that dominate lab research. The most convincing evidence in behavioral economics comes from triangulation across methods: a phenomenon documented in the lab, replicated in the field, and consistent with natural experimental evidence carries much more weight than any single study.
