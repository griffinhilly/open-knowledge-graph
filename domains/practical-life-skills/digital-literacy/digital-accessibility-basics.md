---
id: digital-accessibility-basics
title: Digital Accessibility Basics
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: effective-web-searching
  type: soft
- id: email-fundamentals
  type: soft
builds-toward: []
tags:
- accessibility
- inclusive-design
- assistive-technology
stage: concrete-operations
status: validated
---

# Digital Accessibility Basics

## Core Idea
Digital accessibility means designing and using technology so that people with disabilities — including visual, auditory, motor, and cognitive impairments — can fully participate. This includes understanding built-in accessibility features on your devices (screen readers, magnification, voice control, closed captions, high-contrast modes) and knowing how to create accessible content yourself (adding alt text to images, using proper heading structure, choosing sufficient color contrast, and captioning videos). Accessibility is not a niche concern: an estimated 1 in 4 adults has some form of disability, and accessible design benefits everyone, including people in noisy environments or using small screens.

## How It's Best Learned
Turn on a screen reader on your phone or computer and try navigating a familiar website using only keyboard or voice commands — this firsthand experience builds empathy and reveals how design choices affect usability.

## Common Misconceptions
- Accessibility only benefits people with permanent disabilities — temporary injuries, aging, situational constraints (bright sunlight, noisy room), and slow internet all create accessibility needs.
- Adding accessibility is expensive and complex — many improvements like alt text, heading structure, and color contrast are simple to implement and cost nothing.
- Automated accessibility checkers catch all issues — they typically find only 30-40% of accessibility problems; manual testing with assistive technology is still necessary.

## Explainer

From your work with web searching and email, you've experienced the internet as a sighted, able-bodied user: reading text on screen, clicking links with a mouse, hearing audio through speakers. Digital accessibility is the discipline of ensuring that same experience is equally available to people who interact with technology differently. The scale is larger than most people expect: roughly 1 in 4 adults has some disability, and many more experience situational impairments — a broken arm, bright sunlight, a noisy environment, or slow internet that makes large images and video inaccessible.

The most important accessibility tool to understand firsthand is the **screen reader**: software that reads screen content aloud and allows navigation by keyboard or voice instead of mouse. When a screen reader encounters an image, it reads the **alt text** — a written description embedded in the image's code. If alt text is absent, the screen reader either skips the image silently or reads out the file name ("IMG_4291.jpg"), which tells the listener nothing. This single omission makes image-heavy content — news articles, product listings, instructional graphics — completely opaque to blind users.

**Heading structure** is equally foundational. Sighted users scan pages by jumping visually from heading to subheading. Screen reader users navigate the same way — but by moving through actual heading tags (H1, H2, H3) in the document structure. When a designer uses large, bold text formatted *visually* as a heading but not tagged as a semantic heading element, screen readers present the page as one undifferentiated block of text with no navigational structure. Similarly, **color contrast** between text and background must meet minimum ratios for users with low vision or color blindness; the Web Content Accessibility Guidelines (WCAG) define specific thresholds.

Creating accessible content requires no specialized tools. Adding alt text to images, using built-in heading styles in word processors and web editors, writing link text that makes sense out of context ("read the full report" instead of "click here"), and captioning videos are all achievable in minutes with any standard tool. The right mental model is not "accessibility is a feature I add for a small audience" but rather "accessible content is better-structured, more clearly written content that works better for everyone." The practices that help a screen reader user navigate also help a sighted user who is skimming, or a search engine indexing the page.
