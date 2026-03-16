---
id: design-patterns-and-components
title: Design Patterns and Components
domain: arts-and-aesthetics
course: design-principles
prerequisites:
- id: design-conventions-and-expectations
  type: hard
- id: design-systems-and-consistency
  type: soft
builds-toward:
- ui-design-fundamentals
- design-consistency-and-guidelines
tags:
- patterns
- components
- reusability
- templates
stage: abstract-reasoning
status: draft
---

# Design Patterns and Components

## Core Idea
Design patterns are reusable solutions to common design problems—documented templates that solve recurring user interactions or visual needs. Components are the modular, reusable building blocks of design systems. Both reduce reinvention, maintain consistency, and allow teams to work at scale while ensuring coherent user experiences.

## How It's Best Learned
Document patterns from your own designs: which solutions recur? Create a pattern library and test reusing patterns across new projects.

## Common Misconceptions
That patterns limit creativity. Actually, well-chosen patterns free designers to focus on novel problems.

## Explainer

You already know that users arrive with expectations shaped by conventions — learned behaviors from every interface they have used before. **Design patterns** are the formalized expression of those conventions: documented, reusable solutions to problems that recur across many different products. When a user encounters a search bar at the top of a page, a hamburger menu icon in the upper left on mobile, or a confirmation dialog before a destructive action, they are interacting with patterns — solutions so well-established that they have become part of the shared vocabulary of digital design. A pattern is not a specific piece of code or a single visual treatment; it is a general approach to a recurring interaction problem, described at a level of abstraction that allows it to be adapted to many contexts.

**Components** are the concrete, implementable units that bring patterns to life. A dropdown menu component, a modal dialog component, or a card component is a specific, reusable building block with defined visual appearance, behavior, and code. If a pattern is the recipe ("use a modal dialog to confirm destructive actions"), a component is the pre-made ingredient ("here is our modal dialog, with these exact dimensions, colors, animation timings, and accessibility attributes"). Components live inside **design systems** — the organized collections of guidelines, tokens, and reusable elements that ensure consistency across an entire product or organization. From your understanding of design systems, you can see that components are the atomic units from which systems are built.

The power of patterns and components is in what they eliminate: reinvention. When a designer encounters a new feature that requires users to select from a large set of options, they do not need to invent a selection mechanism from scratch. They can reach for an established pattern (typeahead search, filterable dropdown, multi-select with chips) and implement it using existing components. This saves time, but more importantly, it preserves **consistency** — the user encounters familiar interactions throughout the product rather than learning a new micro-interface for every task. Consistency reduces cognitive load, builds user confidence, and makes the product feel coherent rather than assembled from unrelated parts.

The discipline of working with patterns is knowing when to use an existing one and when the problem genuinely requires something new. Most design problems are not novel — they are variations on well-understood interaction types. A designer who reaches for a custom solution when a standard pattern would serve the user better is not being creative; they are adding unnecessary learning cost for the user. The creativity lies in choosing the right pattern, adapting it to the specific context, combining patterns effectively, and recognizing the genuinely rare situations where no existing pattern fits and a new solution must be designed, tested, and eventually contributed back to the pattern library.
