---
id: leading-and-line-spacing
title: Leading and Line Spacing
domain: arts-and-aesthetics
course: design-principles
prerequisites:
- id: typography-fundamentals
  type: hard
builds-toward:
- responsive-typography
- typography-readability-legibility
tags:
- typography
- spacing
- readability
stage: abstract-reasoning
status: draft
---

# Leading and Line Spacing

## Core Idea
Leading (pronounced 'ledding') is the vertical distance between lines of type, measured from baseline to baseline. Proper leading improves readability by preventing lines from feeling cramped or scattered—typically 120–150% of the type size for body text.

## How It's Best Learned
Set body text at a fixed size (12px) and try leading values from 100% to 200%. Notice how readability and rhythm change; then observe leading in print books and websites.

## Common Misconceptions
- Confusing leading with line-height in CSS; they're related but measured differently.
- Using the same leading for all type sizes; larger type usually needs proportionally tighter leading.

## Explainer

From your study of typography fundamentals, you understand the basic anatomy of letterforms — baseline, x-height, ascenders, descenders, and how these elements define a typeface's character. **Leading** (rhymes with "sledding," not "reading") controls the vertical space between lines of text, and it is one of the most consequential typographic decisions you can make. Too little leading and lines of text crash into each other, creating a dense, intimidating block that readers abandon. Too much and the lines float apart, breaking the visual connection between one line and the next, forcing the eye to search for where to continue reading. The right leading creates a comfortable rhythm that guides the eye smoothly from the end of one line to the beginning of the next.

The term comes from the era of metal type, when typesetters literally inserted thin strips of **lead** (the metal) between rows of type to increase the space between lines. In modern digital typography, leading is specified as the distance from one baseline to the next — the **baseline-to-baseline measurement**. If your type is set at 16 pixels and your leading is 24 pixels, there are 8 pixels of space between the bottom of one line's descenders and the top of the next line's ascenders (roughly — the exact distribution depends on the typeface's metrics). The conventional shorthand writes this as 16/24 (sixteen on twenty-four), and the general guideline for body text is leading at **120% to 150%** of the type size. So 16px type might use 20px to 24px leading, depending on the typeface and line length.

Why a range rather than a single number? Because optimal leading depends on several interacting factors. **Line length** is the most important: longer lines need more leading because the eye must travel farther to find the start of the next line, and generous vertical spacing helps prevent the eye from accidentally re-reading the same line or skipping one. A narrow column of text (like a newspaper column) can survive tighter leading because the short horizontal distance makes line-tracking easy. **Typeface design** also matters: typefaces with a tall x-height (like Verdana or Georgia) have less built-in space between lines and typically need more leading, while typefaces with a small x-height and long ascenders and descenders (like Garamond) have more built-in vertical air and can work with tighter settings. **Color and contrast** play a role too: light text on a dark background tends to appear more crowded than dark text on light, so it often benefits from slightly increased leading.

The relationship between leading and **line length** is particularly important to internalize because they form a system with type size. These three variables — type size, line length, and leading — must be tuned together, not independently. If you increase the line length, you should increase the leading (and possibly the type size) to maintain readability. If you decrease the type size for a caption or footnote, you may need proportionally more generous leading because the smaller text is harder to track across lines. Designers who adjust one variable without considering the other two often produce text that is technically readable but subtly uncomfortable — the reader feels fatigued without knowing why.

One final practical note: in CSS, the `line-height` property is related to but not identical to traditional leading. CSS `line-height` distributes extra space equally above and below each line (half-leading), while traditional typographic leading adds all the extra space below the line. This means that CSS `line-height: 1.5` on 16px text produces 24px of baseline-to-baseline distance — functionally equivalent to 16/24 leading — but the vertical distribution around the text differs. This distinction matters when you are aligning text to a baseline grid or vertically centering text within a container, and it is the source of many subtle spacing bugs in web typography.
