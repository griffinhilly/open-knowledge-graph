---
id: digital-born-literature-preservation
title: 'Digital-Born Literature: Preservation and Access'
domain: literature
course: digital-and-experimental-literature
prerequisites:
- id: electronic-poetry-digital-forms
  type: hard
tags:
- digital-literature
- preservation
- archiving
- obsolescence
stage: advanced
status: draft
---

# Digital-Born Literature: Preservation and Access

## Core Idea
Digital literature faces unique preservation challenges as platforms and formats become obsolete. Questions arise about what constitutes the 'text'—source code, executed output, interactive experience, or all three. Preservation requires technological intervention and curatorial decision-making that shapes how future readers encounter digital works, making preservation itself an interpretive practice.

## Questions

```yaml
- type: multiple-choice
  question: What is the central preservation challenge for digital-born literature that differs from print literature?
  options:
    - 0: "Digital literature depends on platforms, software, and hardware that become obsolete, making the work inaccessible when technologies fail; print literature's preservation requires only stable storage conditions"
    - 1: "Digital literature is always preserved perfectly because computers store everything automatically"
    - 2: "Print literature faces the same obsolescence challenges as digital literature"
    - 3: "Digital literature cannot be preserved at all"
  correct_answer: 0
  explanation: "Print literature can be read indefinitely if pages and binding survive—the technology is stable. Digital literature requires functional platforms, compatible software, and accessible hardware. When Storyspace becomes unavailable, Flash dies, or proprietary formats are no longer supported, the work becomes unreadable. The work's existence depends on technological infrastructure."

- type: multiple-choice
  question: When preserving digital literature, what problem arises from determining what constitutes the 'text'?
  options:
    - 0: "A digital work may exist as source code, executed output, and interactive experience; preservation decisions about which aspects to save shape what future readers encounter and may alter the work's meaning"
    - 1: "Digital literature has a single obvious definition of text"
    - 2: "Preserving only the visual output is always sufficient"
    - 3: "Source code preservation is always more important than interactive experience"
  correct_answer: 0
  explanation: "A hypertext fiction work like 'Afternoon, a Story' consists of source code (the Storyspace file), the visual output readers experience, and the interactive navigation structure. Preserving only one aspect loses others. If you preserve only output screenshots, you lose interactivity. If you preserve only code, you need functional Storyspace to read it. Preservation decisions are curatorial; they determine what future readers can experience."

- type: true-false
  statement: "Digital preservation is purely technical work that requires no interpretive or curatorial judgment"
  correct_answer: false
  explanation: "Preservation involves multiple decisions: which versions to save, what platform to migrate to, whether to maintain original look/functionality or prioritize access. Each choice shapes the preserved work. It is as much curation as technology."

- type: true-false
  statement: "Emulation and migration are different preservation strategies that each have distinct advantages and drawbacks for digital literature"
  correct_answer: true
  explanation: "Emulation attempts to recreate original platforms so works run as designed. Migration moves works to new formats/platforms, which may change their appearance or functionality. Both have tradeoffs: emulation preserves original experience but requires ongoing maintenance; migration ensures access but may alter the work."

- type: short-answer
  question: "Explain how preservation decisions for digital literature are interpretive acts that shape what future readers encounter. Provide a concrete example."
  explanation: "Example: A hypertext fiction work created in Storyspace exists as source code. To preserve it: (1) Archive the code and original software—requires maintaining obsolete technology; (2) Migrate to modern hypertext format—changes link appearance and navigation feel; (3) Create a static HTML version—loses interactivity; (4) Emulate the original environment—preserves experience but is brittle. Each choice is curatorial: it determines whether future readers experience the original navigational difficulty, or whether the work becomes easier/harder to read. If the work's meaning depends on link ambiguity (as in 'Afternoon'), migration to a clearer format changes meaning. Preservation is thus not neutral documentation but interpretation. The curator's decisions about which aspects to preserve shape the work future readers encounter."
```

## Explainer

Print literature faces its own preservation challenges—paper degrades, books are lost, libraries burn. But digital literature faces a fundamentally different problem: technological obsolescence. A book from 1950 can be read today with no more than good light. Digital literature from 1995 requires software that may no longer be available, hardware that is no longer manufactured, and formats that operating systems no longer support. Digital preservation is thus not primarily about storage but about sustained technological maintenance.

Consider a hypertext fiction created in Storyspace, a tool that dominated 1980s-90s hypertext authoring but is now obsolete. To preserve this work and keep it readable, what must be preserved? The source code alone is not sufficient—readers need a functioning Storyspace application to open it. One preservation approach is emulation: recreate the original Storyspace environment on contemporary systems so the work runs exactly as designed. But emulation is labor-intensive and brittle; it must be continuously updated as operating systems change. Another approach is migration: convert the work to a contemporary format, such as HTML with JavaScript interactivity. This ensures access but changes the reading experience—the aesthetic of original link behavior may be lost.

The problem becomes even more complex when we ask: what is the work? Is it the source code? The visual output? The interactive experience? A decision about which aspects to preserve is implicitly a decision about what the work is. If you preserve only the narrative text, stripping away the interactive navigation, you preserve content but lose formal meaning. If you preserve only screenshots, you preserve visual appearance but lose interactivity. These are curatorial decisions, not purely technical ones.

Digital preservation thus becomes interpretive practice. The preservationists must make judgment calls: Will we maintain original platforms at great technical cost? Will we migrate to ensure access? Will we prioritize the interactive experience or the source code? Each decision shapes what future readers encounter. If a hypertext fiction's meaning depends on reader uncertainty (as with 'Afternoon, a Story'), migrating to a platform with clearer navigation structures alters that meaning. Preservation decisions are not neutral; they constitute interpretation.

This reveals that digital literature requires ongoing institutional commitment. Unlike print, which can be preserved passively (keep it in a stable environment), digital literature requires active maintenance: emulation systems must be updated, migrations must be performed, formats must be converted. This ongoing labor means that digital literature preservation is always partial and provisional, shaped by decisions about which works merit sustained effort and what aspects of works matter most to preserve.
