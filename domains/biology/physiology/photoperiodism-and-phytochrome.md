---
id: photoperiodism-and-phytochrome
title: Photoperiodism and Phytochrome
domain: biology
course: physiology
prerequisites:
- id: plant-hormones-and-tropisms
  type: hard
- id: cell-signaling-intro
  type: hard
- id: pollination-and-fertilization
  type: soft
builds-toward:
- angiosperm-reproduction-double-fertilization
tags:
- plants
- photoperiodism
- phytochrome
- flowering
- florigen
- red-far-red
stage: formal-systems
status: validated
---

# Photoperiodism and Phytochrome

## Core Idea
Photoperiodism is a response to the relative lengths of day and night, and its best-known example is the timing of flowering. Short-day plants flower when nights are longer than a critical length, long-day plants flower when nights are shorter than a critical length, and day-neutral plants flower regardless of day length. Plants measure the night with phytochrome, a pigment that switches between a red-absorbing form and a far-red-absorbing form. Leaves sense the photoperiod and send a signal, called florigen, through the phloem to the shoot tips, where flowers form.

## How It's Best Learned
Present night-break experiments as puzzles: give students the light schedule and ask whether a short-day or long-day plant will flower. Then add red and far-red flashes and let them predict the outcome from the last flash. Real examples help: poinsettias sold in December are short-day plants that growers keep in long nights during autumn.

## Common Misconceptions
- Short-day plants measure the length of the day. (Experiments show that the length of uninterrupted darkness is what matters; a brief flash of light in the middle of a long night stops a short-day plant from flowering.)
- The flowers themselves sense day length. (Leaves detect the photoperiod, and a mobile signal travels to the shoot tips.)
- Phytochrome is used for photosynthesis. (Phytochrome is a sensory pigment that controls responses such as flowering and seed germination; it does not capture energy.)

## Questions

```yaml
- question: "A short-day plant has a critical night length of 10 hours. It is kept on 8 hours of light and 16 hours of dark, but the dark period is interrupted in the middle by a one-minute flash of red light. What happens?"
  type: multiple-choice
  options: ["It flowers, because the total darkness is still 16 hours", "It does not flower, because no single stretch of darkness reaches 10 hours", "It flowers faster than usual", "It dies from the light flash"]
  answer: 1
  explanation: "The flash splits the night into two 8-hour periods. Neither reaches the 10-hour critical length, so the plant responds as if nights were short and does not flower. This night-break result shows that plants measure continuous darkness."
- question: "Short-day plants flower when the day length is shorter than a critical value, so the length of the day is what they measure."
  type: true-false
  answer: false
  explanation: "The name is historical. Night-break experiments in the 1930s and 1940s showed that the length of uninterrupted darkness controls flowering. Short-day plants are really long-night plants."
- question: "A short-day plant receives a night-break flash of red light followed at once by a flash of far-red light. Will it flower under long nights?"
  type: short-answer
  answer: "Yes. Red light converts phytochrome to its active Pfr form, but the far-red flash converts it back to Pr. Because the last flash was far-red, the night acts as if uninterrupted, and the short-day plant flowers."
  explanation: "Red and far-red effects are reversible, and the final flash decides the outcome. This reversibility was the key evidence that a single photoreversible pigment, phytochrome, measures the night."
- question: "Where in the plant is the photoperiod detected, and how does the shoot tip learn that it is time to flower?"
  type: multiple-choice
  options: ["In the roots, which send a hormone through the xylem", "In the leaves, which send a signal (florigen) through the phloem to the shoot tips", "In the flower buds themselves", "In the seeds, which store the information from the previous year"]
  answer: 1
  explanation: "Grafting experiments showed that an induced leaf can make an uninduced plant flower. In Arabidopsis the signal includes the protein FT (FLOWERING LOCUS T), made in leaves and carried in the phloem to the shoot apex."
```

## Explainer
Many plants flower at the same time each year. Chrysanthemums and poinsettias bloom in autumn or winter, while spinach bolts and flowers in early summer. Temperature varies from year to year, but day length on a given date is the same every year, so it is a reliable calendar.

In 1920 W. W. Garner and H. A. Allard, working for the US Department of Agriculture, studied a tobacco variety called Maryland Mammoth. It grew huge in summer but would not flower outdoors. In a greenhouse in winter it flowered. They showed that the cue was the photoperiod and coined the term photoperiodism. Plants that flower when days are short became known as short-day plants. Those that flower when days are long are long-day plants. Day-neutral plants, such as tomatoes, flower when they reach a certain size whatever the day length.

Later experiments revealed that the names point at the wrong period. When researchers interrupted a long night with a short flash of light, a short-day plant failed to flower. Interrupting the day with darkness had no such effect. Plants are timing the night. A short-day plant flowers when the night is longer than a critical length, and a long-day plant flowers when the night is shorter than its critical length.

The night-timer is phytochrome. This protein pigment exists in two forms. Pr absorbs red light (around 660 nm) and converts to Pfr. Pfr absorbs far-red light (around 730 nm) and converts back to Pr. Pfr is the active form that triggers responses. Sunlight contains more red than far-red, so Pfr builds up during the day. In darkness Pfr slowly reverts to Pr or is broken down. Phytochrome thus tells the plant when light is present. The plant's internal circadian clock keeps time through the dark, and the two together let the plant detect whether a night was longer than the critical length.

The red and far-red forms explain a striking result. A red flash during the night acts as a night break. A far-red flash right after it cancels the break. With a series of alternating flashes, only the last one counts.

Leaves sense the photoperiod, but flowers form at the shoot tips. Grafting experiments showed that a leaf exposed to inductive nights can make a plant on the other side of a graft flower. The signal was named florigen. In Arabidopsis it includes the protein FT, which is made in leaves and moves through the phloem to the shoot apex, where it switches on flower-forming genes.
