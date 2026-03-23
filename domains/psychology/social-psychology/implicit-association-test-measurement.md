---
id: implicit-association-test-measurement
title: Implicit Association Test and Implicit Bias Measurement
domain: psychology
course: social-psychology
prerequisites:
- id: stereotyping-and-implicit-bias
  type: hard
- id: measurement-validity-evidence
  type: soft
builds-toward:
- bias-reduction-interventions
tags:
- IAT
- implicit bias
- measurement
- psychometrics
- assessment
stage: formal-systems
status: draft
---

# Implicit Association Test and Implicit Bias Measurement

## Core Idea
The Implicit Association Test (IAT) measures automatic associations between social categories and attributes by recording response latencies when paired concepts are compared. While IAT reliably detects implicit biases faster than explicit self-report measures, its test-retest reliability is moderate, and predictive validity for discriminatory behavior is modest, limiting its use as a direct measure of behavioral bias.

## How It's Best Learned
Learn the IAT's psychometric properties, limitations, and proper interpretation; examine meta-analyses of IAT predictive validity, understand relationships between implicit and explicit biases, and consider alternative measures of implicit bias.

## Common Misconceptions
Students think the IAT perfectly measures racism or sexism and strongly predicts behavior; actually, implicit and explicit biases are partly independent, IAT effects are moderate-sized, and predictive validity varies substantially across contexts and outcomes.

## Questions

```yaml
- question: "A job applicant scores high on a race IAT. Human Resources concludes: 'This person will likely discriminate in hiring decisions.' Based on the research evidence, this conclusion:"
  type: multiple-choice
  options:
    - "Is strongly supported — the IAT was designed to predict discriminatory behavior"
    - "Overstates the evidence — individual IAT scores have moderate test-retest reliability (~.40–.50) and modest predictive validity for actual discriminatory behavior (r ≈ .15–.25)"
    - "Is justified because IAT scores correlate perfectly with explicit prejudice measures"
    - "Is justified because IAT responses cannot be faked or controlled"
  answer: 1
  explanation: "Drawing strong behavioral predictions from an individual's IAT score overstates what the measure can support. While the IAT reliably detects associations at the group level, its individual-level predictive validity for discriminatory behavior is modest (meta-analytic r ≈ .15–.25) and its test-retest reliability is around .40–.50 — meaning the score fluctuates substantially across sessions. The IAT is more useful for describing patterns in large samples than for predicting any individual's behavior."

- question: "A person raised in a society with consistently negative media portrayals of a social group scores high on an IAT for that group, yet sincerely endorses egalitarian values and has never acted discriminatorily. The most accurate interpretation is:"
  type: multiple-choice
  options:
    - "Their IAT score reveals hidden prejudice they are unwilling to acknowledge"
    - "Their IAT score likely reflects cultural exposure to societal associations — which nearly everyone acquires — rather than personal endorsement of bias or a prediction that they will discriminate"
    - "Their IAT score proves they will eventually discriminate under the right conditions"
    - "Their self-report is more valid than the IAT in this case, so the IAT result should be discarded"
  answer: 1
  explanation: "Current consensus is that IAT scores reflect cultural exposure to stereotypes as much as personal prejudice. Living in a society with consistent stereotypic associations causes nearly everyone to acquire those associations implicitly. What varies is whether the associations are consciously endorsed, controlled, and allowed to translate into behavior. The IAT cannot distinguish cultural acquisition from personal prejudice — which is why individual-level behavioral predictions from IAT scores are unreliable."

- question: "A person's IAT score measured today will reliably predict their IAT score if they take the test again in two weeks."
  type: true-false
  answer: false
  explanation: "Test-retest reliability for the race IAT is around .40–.50 — substantially lower than the .70–.90 range typical of personality scales used as stable individual differences. An individual's score fluctuates across sessions due to mood, priming, context, and other transient factors. This instability limits the IAT's use as a trait-level measure of an individual's implicit bias and makes repeated individual measurement unreliable."

- question: "Because the IAT bypasses conscious control, a high IAT score indicates that a person will discriminate regardless of their stated values or structural constraints in their environment."
  type: true-false
  answer: false
  explanation: "The dissociation between implicit association and deliberate discrimination is central to this literature. Predictive validity for actual discriminatory behavior is modest (r ≈ .15–.25) and highly context-dependent. Top-down control, accountability structures, and clear behavioral norms substantially moderate whether implicit associations translate into behavior. The presence of an implicit association is not a behavioral destiny — people actively regulate the influence of their associations on their actions."

- question: "Why do researchers argue that structural interventions (blind review, standardized hiring rubrics) are often more effective at reducing discriminatory outcomes than trying to lower people's IAT scores directly?"
  type: short-answer
  answer: "IAT scores reflect broad cultural associations that nearly everyone acquires — directly reducing them at scale is difficult and effect sizes are small. Structural interventions change the decision-making environment so that implicit associations have less opportunity to influence outcomes, regardless of whether individual IAT scores change. The system can produce less discriminatory results without requiring every individual to first achieve a low IAT score."
  explanation: "This is the key distinction between person-centered and systems-centered approaches to bias. If the pathway from implicit association to discriminatory behavior runs through unstructured judgment, removing unstructured judgment removes the pathway — even if the association remains. This is why blind auditions increased female musicians in orchestras without any intervention on judges' implicit biases."
```

## Explainer

You already know from your study of stereotyping that people hold automatic associations linking social categories (race, gender, age) to attributes (competent/incompetent, dangerous/safe, warm/cold), and that these associations can influence behavior even when people sincerely endorse egalitarian values. The challenge for measurement is that people can't (or won't) accurately report these associations on a self-report questionnaire — either because the associations operate below conscious access, or because social desirability suppresses honest reporting. The **Implicit Association Test** was designed to get around this problem by measuring associations indirectly, through the one thing that is hard to control: **response speed**.

The logic of the IAT is elegant. Participants sort items into categories using two response keys. In a race IAT, one key might be paired with "Black faces + pleasant words" and the other with "White faces + unpleasant words"; in the compatible block, it's reversed. The core assumption is that when two categories are strongly associated in memory, sorting them to the same key is easier — faster and more accurate — than when they are not associated. A person who has strong automatic positive associations with White faces and negative associations with Black faces should be faster in the White+pleasant / Black+unpleasant pairing. The difference in reaction time between the two blocks (the **D-score**) is the measure of implicit bias.

The IAT's strengths are real: it is hard to fake, produces reliable group-level differences in the expected directions (most participants in majority-White countries show implicit preference for White over Black faces), and correlates only modestly with explicit self-report measures — meaning it captures something different. Its weaknesses, however, matter enormously for how it should and should not be used. **Test-retest reliability** is moderate (around .40–.50 for the race IAT), meaning that an individual's score fluctuates substantially across sessions. This limits its use as a stable individual difference measure. More importantly, **predictive validity** for actual discriminatory behavior — hiring decisions, medical treatment recommendations, police use of force — is modest (meta-analytic correlations around .15 to .25) and varies substantially across contexts.

The most important interpretive caution is about **levels of analysis**. The IAT reliably detects associations at the group level — in samples of thousands, IAT scores predict behavior better than chance. But the individual-level inference is much weaker. Telling a specific person "your IAT score shows you are biased and will discriminate" overstates the evidence dramatically. Current consensus is that IAT scores reflect cultural exposure to stereotypes as much as personal prejudice — nearly everyone raised in a society with certain associations picks them up to some degree. What varies is whether those associations are endorsed, controlled, and allowed to influence behavior. This dissociation between implicit association and deliberate discrimination is why bias-reduction research has increasingly focused on structural interventions and behavioral constraints rather than on changing individual IAT scores.
