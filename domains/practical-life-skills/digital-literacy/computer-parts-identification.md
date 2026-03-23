---
id: computer-parts-identification
title: Identifying Computer Parts
domain: practical-life-skills
course: digital-literacy
prerequisites: []
builds-toward:
- turning-on-and-powering-off
tags:
- hardware
- fundamentals
- computer-basics
stage: concrete-operations
status: validated
---

# Identifying Computer Parts

## Core Idea
A computer has different parts that do different things. The monitor shows pictures, the keyboard lets you type, the mouse lets you point and click, and the speakers make sounds. Learning what each part does helps you use a computer properly.

## Questions

```yaml
- question: "You're working on a document and your computer unexpectedly shuts off without saving. When you restart, the document is gone but your installed programs are still there. Which explanation is correct?"
  type: multiple-choice
  options:
    - "Both RAM and the hard drive lost their data — you just didn't notice the programs were gone yet"
    - "The unsaved document was in RAM (temporary memory that clears when power is lost); installed programs are on the hard drive (permanent storage that persists through shutdown)"
    - "The hard drive stores current work; RAM stores permanent data like installed programs"
    - "Nothing is ever permanently lost — the document is in a different folder"
  answer: 1
  explanation: "RAM holds what the computer is actively working on right now — your open, unsaved document. RAM is temporary: when power is cut, it clears entirely. The hard drive holds permanent files — installed programs, saved documents, the operating system — and keeps them through power loss. When you click Save, the document moves from RAM to the hard drive. An unsaved document exists only in RAM, which is why it disappears when the computer shuts off unexpectedly."

- question: "Your computer runs fine with one or two programs open, but slows down noticeably when you have ten programs open at once. Which component is most likely the bottleneck?"
  type: multiple-choice
  options:
    - "The monitor — it has to display more windows simultaneously"
    - "The CPU — it gets confused when many programs are running"
    - "RAM — it runs out of space to hold all the active programs at once, forcing the computer to use slower alternatives"
    - "The hard drive — it wears out from too many programs being installed on it"
  answer: 2
  explanation: "RAM is the computer's active workspace — it holds everything currently running. Each open program occupies RAM. When RAM fills up, the computer must use the hard drive as overflow (called virtual memory), which is far slower — this is the classic cause of sluggishness with many open programs. More RAM lets you have more things open at once without this slowdown. CPU bottlenecks appear differently (slow individual tasks, not just many-program slowness)."

- question: "The CPU (central processing unit) executes instructions and performs calculations — it is the component doing the actual 'thinking' of the computer."
  type: true-false
  answer: true
  explanation: "The CPU is the brain of the computer. Every instruction a program issues — display this image, respond to this click, add these numbers — is processed by the CPU. Its speed (measured in gigahertz) determines how fast those instructions execute. Without a functioning CPU, the computer cannot do anything at all."

- question: "The hard drive stores what the computer is currently working on, which is why its contents are lost when you turn the computer off."
  type: true-false
  answer: false
  explanation: "This confuses RAM and the hard drive. RAM stores what the computer is currently working on — and RAM does clear when power is lost. The hard drive is permanent storage: it keeps your saved files, installed programs, and the operating system through shutdown and restarts. The hard drive does NOT clear on shutdown. RAM does. This distinction explains why unsaved work disappears but installed programs do not."

- question: "What is the difference between RAM and a hard drive, and why does it matter for how you use a computer?"
  type: short-answer
  answer: "RAM is temporary workspace — it holds what the computer is actively doing right now, and it clears when the computer is turned off. A hard drive is permanent storage — it keeps files and programs even when power is off. The practical implication: always save your work to the hard drive before shutting down, or any unsaved changes (which exist only in RAM) will be lost."
  explanation: "Understanding this distinction explains most 'where did my work go?' moments. Open programs, unsaved documents, and active processes exist only in RAM. Clicking Save moves your work from RAM to the hard drive where it persists. This is also why adding more RAM improves multitasking — you are giving the computer more active workspace so it does not have to fall back on the much slower hard drive for overflow."
```

## Explainer

A computer may look complicated, but it is built from a small number of parts, each with a specific job. The best way to understand how a computer works is to understand what each part does — not in technical detail, but in plain terms. Think of a computer the way you might think of a kitchen: there are tools for input (a knife, a spoon for preparing ingredients), tools for processing (the stove, the oven), a place to see what you're doing (the counter), and tools for output (the plate that holds the finished meal). Computer parts divide into the same basic categories.

The **monitor** (or screen) is the output device that shows you what the computer is doing — text, pictures, videos, and everything else you see. The **keyboard** is an input device: it lets you type letters, numbers, and commands. The **mouse** (or trackpad on a laptop) is another input device that lets you point at things on the screen, click to select them, and drag them around. These three parts — monitor, keyboard, mouse — are the ones you interact with directly. They are called **peripheral devices** because they connect to the main computing unit rather than being the unit itself.

Inside the computer, three core components do the actual work. The **central processing unit** (CPU) is the "brain" — it follows instructions, does calculations, and decides what to show on the screen. The **hard drive** (or solid-state drive) is permanent storage — it holds your files, photos, and programs even when the computer is off, like a filing cabinet. **RAM** (random access memory) is temporary storage — it holds what the computer is actively working on right now, like papers spread out on a desk. When you turn the computer off, the RAM clears; the hard drive does not. A computer with more RAM can work on more things at once without slowing down.

The **speakers** produce sound output. The **power button** turns the computer on and off. On a laptop, all of these components — screen, keyboard, trackpad, speakers, battery, and processing components — are built into one portable unit. On a desktop, they are separate devices connected by cables. Recognizing each part and knowing its role makes everything else about using a computer easier: when something goes wrong (no sound, a dark screen, an unresponsive keyboard), you can identify which part has a problem rather than being confused by the whole system at once.
