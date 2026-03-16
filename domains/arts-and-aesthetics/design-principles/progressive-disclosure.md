---
id: progressive-disclosure
title: Progressive Disclosure of Information
domain: arts-and-aesthetics
course: design-principles
prerequisites:
- id: information-hierarchy-and-wayfinding
  type: hard
- id: visual-hierarchy-structure
  type: hard
builds-toward:
- ui-design-fundamentals
- user-experience-fundamentals
tags:
- disclosure
- information-architecture
- usability
- complexity
- progressive
stage: abstract-reasoning
status: draft
---

# Progressive Disclosure of Information

## Core Idea
Progressive disclosure presents information gradually, showing only essential details first and revealing additional options or details on demand. This reduces cognitive load, prevents overwhelming users, and maintains clean interfaces. The technique is essential for complex systems like advanced settings, detailed product catalogs, or documentation.

## How It's Best Learned
Design a mobile menu system or settings panel using progressive disclosure. Test user comprehension and task completion times with and without the technique to measure its impact.

## Common Misconceptions
- Progressive disclosure hides important information; it reveals on demand, which is often faster for most users.
- All features must be visible simultaneously for discoverability; well-designed progressive disclosure aids discovery.

## Explainer

You already know from information hierarchy and visual hierarchy that not all content deserves equal prominence — some things matter more and should be seen first. **Progressive disclosure** takes this principle one step further: instead of just making secondary content smaller or less prominent, you remove it from view entirely until the user asks for it. The idea is simple — show the essential first, reveal the rest on demand — but applying it well requires judgment about what counts as "essential" for each user at each moment.

Consider a restaurant menu. A well-designed menu lists dishes with short descriptions. If you want the full ingredient list or allergen information, you ask the server or flip to a detailed section in the back. The menu does not dump every detail on the main page because that would overwhelm you and slow down ordering. Progressive disclosure works the same way in interfaces: a settings screen shows the five options most people need, with an "Advanced" section that expands for power users. A product page shows price, photos, and key specs up front, with expandable sections for full technical details, shipping information, and reviews.

The technique works because of how human attention operates. People scan before they read, and they abandon interfaces that look complex before they even try. By **layering information** — showing a summary first, then supporting detail, then edge-case specifics — you let users self-select their depth. Novice users accomplish their task without being confused by expert options. Expert users click through to find what they need without the interface being dumbed down. Both audiences are served by the same design, just at different layers.

The most common mistake is hiding the wrong things. Progressive disclosure should never bury information that users need to make a primary decision — it should only defer information that serves secondary or conditional needs. If a user cannot complete their main task without expanding a hidden panel, the disclosure is working against them. Test this by watching real users: if they consistently expand the same section to finish a core task, that content belongs in the primary layer. The goal is not to hide things — it is to sequence the user's experience so that complexity unfolds naturally rather than arriving all at once.
