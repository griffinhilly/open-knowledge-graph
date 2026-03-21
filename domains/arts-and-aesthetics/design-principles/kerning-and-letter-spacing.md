---
id: kerning-and-letter-spacing
title: Kerning and Letter Spacing
domain: arts-and-aesthetics
course: design-principles
prerequisites:
- id: typography-fundamentals
  type: hard
builds-toward:
- type-pairing-and-hierarchy
- responsive-typography
tags:
- typography
- spacing
- refinement
stage: abstract-reasoning
status: draft
---

# Kerning and Letter Spacing

## Core Idea
Kerning adjusts space between specific letter pairs to achieve optical balance, while letter spacing adjusts overall spacing uniformly. Proper kerning is critical for professional typography—letters that appear poorly spaced create visual friction even if technically equidistant.

## How It's Best Learned
Practice with font pairs that have obvious kerning issues (e.g., AV, To, Yo). Compare kerned vs. unkerned text at body and display sizes to develop a trained eye.

## Common Misconceptions
- Thinking all letters should be equally spaced; kerning is about visual, not mathematical, balance.
- Assuming automatic kerning tables are always correct—they often need manual refinement for professional results.

## Questions

```yaml
- question: "A designer sets the word 'AVOCADO' with mathematically equal spacing between every letter. The result looks wrong — the 'AV' gap appears larger than the other spaces. What is the cause?"
  type: multiple-choice
  options:
    - "The font file is corrupted and the spacing data is incorrect"
    - "The angled strokes of A and V create a visual pocket of whitespace that appears larger than the spaces between straighter letter combinations"
    - "Equal mathematical spacing is always visually correct; the designer is misperceiving the spacing"
    - "The letter V has a wider character box that forces extra space after it"
  answer: 1
  explanation: "Different letter shapes create different apparent whitespace even when technically equidistant. The diagonal strokes of A and V create an open triangular pocket between them that visually reads as more space than, say, the gap between two vertical strokes. Kerning compensates for this optical illusion by tightening specific pairs. Equal math does not produce equal optics — that is the foundational insight of kerning."

- question: "A typographer needs to set a headline in all-uppercase letters and notices the letters feel cramped and dense. What adjustment is most appropriate?"
  type: multiple-choice
  options:
    - "Increase kerning on specific problem pairs like 'LT' and 'WA'"
    - "Increase letter spacing (tracking) uniformly across the entire headline"
    - "Switch to a different font with naturally wider letters"
    - "Reduce the font size until the density looks correct"
  answer: 1
  explanation: "Uppercase letters have more uniform heights than mixed-case text, which makes tighter spacing feel cramped and crowded. The solution is tracking — increasing uniform spacing across the whole word or line — not pair-specific kerning. This is a standard typographic rule: uppercase and small caps text typically benefits from added tracking to breathe properly."

- question: "Mathematically equal spacing between letters will always appear optically equal to a trained eye."
  type: true-false
  answer: false
  explanation: "False — this is the central misconception kerning corrects. Different letter shapes create different amounts of apparent whitespace even when the measured gap is identical. Straight-sided letters (like H and I) feel closer than combinations with angled or overhanging strokes (like A and V, or T and o). Good typography requires optical equality, not mathematical equality."

- question: "Kerning errors are most noticeable and most damaging at headline and display sizes rather than at body text sizes."
  type: true-false
  answer: true
  explanation: "True. At body text sizes (10–14pt), small kerning imperfections are rarely noticed by readers — the text is read as a whole. But at display sizes used in headlines, logos, and posters, the enlarged whitespace between letters makes optical imbalances visible and signals a lack of craft. This is why professional typographers invest the most kerning effort in large-format text."

- question: "What is the difference between kerning and letter spacing (tracking), and when would you use each?"
  type: short-answer
  answer: "Kerning adjusts the space between specific letter pairs to achieve optical balance where individual letterform shapes create visual gaps. Tracking adjusts the overall spacing uniformly across an entire word, line, or block of text. Use kerning to fix pair-specific optical problems (AV, To); use tracking to adjust the overall density of a word or passage (e.g., adding tracking to uppercase headlines)."
  explanation: "The two tools operate at different scales and solve different problems. Kerning is surgical — it targets the optical problem created by two specific adjacent shapes. Tracking is systemic — it shifts the overall rhythm of a typeset passage. A designer working on a logo might do both: add tracking to the whole word to open it up, then fine-tune specific problem pairs with kerning."
```

## Explainer

From typography fundamentals, you know that typefaces are designed with careful attention to the shapes and proportions of individual characters. But letters do not exist in isolation — they sit next to each other, and the spaces between them are as important to readability as the letterforms themselves. **Kerning** is the adjustment of space between specific pairs of letters to achieve even *optical* spacing, while **letter spacing** (also called **tracking**) adjusts the uniform spacing across an entire block of text. Both are essential to professional typography, but they solve different problems.

The need for kerning arises because letters have different shapes — and different shapes create different amounts of apparent whitespace. Place a capital T next to a lowercase o, and the overhanging crossbar of the T creates a visual gap that makes the two letters look farther apart than they are. Place two vertical strokes next to each other (like H and I) and the uniform edges make the spacing feel tighter by comparison. Without kerning adjustments, mathematically equal spacing produces optically uneven results. The classic problem pairs — **AV**, **To**, **Yo**, **LT**, **WA** — all involve letters whose angled or overhanging forms create pockets of whitespace that must be reduced to match the perceived spacing of straighter combinations.

**Letter spacing** operates at a different scale. Rather than adjusting individual pairs, tracking increases or decreases the overall spacing uniformly across a word, line, or paragraph. The most common application is in **uppercase text and small caps**, which typically need increased letter spacing to feel balanced — because uppercase letters are more uniform in height, tighter spacing creates a dense, crowded feeling. Conversely, body text at standard sizes usually needs no tracking adjustment (the font designer has already optimized it), but display text set at very large sizes often benefits from tighter tracking because the enlarged whitespace between letters becomes disproportionately visible.

Developing a kerning eye takes practice, but there is a reliable method: instead of looking at letter pairs in isolation, look at groups of three. For any three consecutive letters, the space on the left side of the middle letter should feel equal to the space on the right. Work through the word three letters at a time, overlapping by one letter each step. When you can no longer detect unevenness, the kerning is correct. At body text sizes (10–14pt), kerning imperfections are rarely noticed by readers. But at display sizes — headlines, logos, posters — even small kerning errors create visible awkwardness that signals a lack of craft. The line between amateur and professional typography often runs directly through the quality of the kerning.
