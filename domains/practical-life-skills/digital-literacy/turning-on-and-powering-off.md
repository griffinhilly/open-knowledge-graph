---
id: turning-on-and-powering-off
title: Turning Computers On and Off
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: computer-parts-identification
  type: soft
- id: computer-startup-and-shutdown
  type: soft
builds-toward:
- using-a-mouse
- using-a-keyboard
tags:
- startup
- shutdown
- fundamentals
- hardware
stage: concrete-operations
status: validated
---
# Turning Computers On and Off

## Core Idea
Every computer has a power button that turns it on and off. When you press the power button, the computer wakes up and shows you a login or home screen. When you're done, you should shut down properly using the shutdown menu, not just by pulling the plug.

## How It's Best Learned
Have children actually press the power button and watch the computer start up. Then practice shutting down properly using the shutdown option in the menu.

## Common Misconceptions
- Thinking you can just unplug the computer instead of using the shutdown menu.
- Confusing the monitor's power button with the computer's power button.
- Not knowing you might need to log in with a password after turning it on.

## Questions

```yaml
- question: "Leon finishes using a computer and pulls the power cord from the wall instead of using the shutdown menu. His teacher says this is incorrect. What is the best reason why?"
  type: multiple-choice
  options:
    - "Because only a teacher is allowed to unplug computers"
    - "Because the computer needs time through the shutdown process to save open work, finish background tasks, and store its state — cutting power abruptly can cause data loss or file system problems"
    - "Because the computer will be permanently broken after being unplugged"
    - "Because pulling the cord only turns off the monitor, not the computer itself"
  answer: 1
  explanation: "The shutdown menu triggers a controlled power-off sequence: the operating system saves unsaved data, closes programs properly, and writes a clean system state before cutting power. Pulling the cord skips all of this — like slamming a book shut mid-sentence. Unsaved work is lost, and in some cases the abrupt shutdown can corrupt the file system, causing problems when the computer tries to restart."

- question: "You turn off the monitor on a desktop computer. What has happened to the computer itself?"
  type: multiple-choice
  options:
    - "The computer has shut down and will need to go through startup again when you return"
    - "The screen is dark, but the computer is still running — programs and processes continue normally"
    - "Both the monitor and the computer are now off"
    - "The computer has automatically gone into sleep mode"
  answer: 1
  explanation: "The monitor and the computer tower are separate devices, each with its own power supply and power button. Turning off the monitor only makes the screen dark — the computer's processor, memory, and storage keep running just as before. If you walk away with only the monitor off, you return to a live computer, not one that needs to restart."

- question: "Turning off the monitor on a desktop computer also shuts down the computer."
  type: true-false
  answer: false
  explanation: "The monitor is a separate output device — it receives a signal from the computer and displays it. Removing the display does not affect the computer's operation. The monitor has its own power button that controls only the screen. To actually shut down the computer, you use the operating system's shutdown option."

- question: "During startup, if you see a spinning circle or progress bar on screen, you should wait without pressing the power button again — this means the computer is working through its startup process normally."
  type: true-false
  answer: true
  explanation: "The startup sequence involves checking hardware, loading the operating system, and preparing your environment — this takes time and the visual feedback (spinning circles, progress bars, logos) means progress is being made. Pressing the power button again during this time can interrupt the process and force an abrupt shutdown, potentially causing the very problem you were trying to avoid."

- question: "Why is it important to use the operating system's shutdown menu rather than cutting power directly when you are done using a computer?"
  type: short-answer
  answer: "Using the shutdown menu gives the computer time to finish what it is doing before powering off: it saves any unsaved work, closes programs cleanly, and writes a proper system state to storage. Cutting power abruptly — by pulling the plug or pressing the power button mid-session — skips these steps, which can result in lost data and, in some cases, file system corruption that causes errors the next time the computer starts."
  explanation: "The shutdown sequence is the computer tidying up before it goes off. Modern operating systems are designed assuming users will shut down through the software menu. While most computers can survive an occasional forced shutdown, it is a risk easily avoided by using the proper procedure."
```

## Explainer

A computer is like a house that needs to be opened before you can use it. The **power button** is the front door — pressing it starts the process of waking everything up inside. When you press it, the computer runs through a startup sequence: it checks its own hardware, loads its operating system (the main software that runs everything), and then shows you a screen where you can begin using it.

The startup process takes a little time — usually from a few seconds to a minute or two. During that time, you might see a logo, a spinning circle, or a progress bar. These are all signs that the computer is doing its setup work automatically, just like how a car engine takes a moment to start before you can drive. You don't need to press the power button again or do anything else — just wait.

Once the computer is ready, it often shows a **login screen** where you type a username and password. This is how the computer knows who you are and loads your personal settings, files, and preferences. Think of it like clocking in at school or signing into a class — it connects "this computer" to "you specifically." If you're the only person using the computer, you might skip right past this to the home screen.

When you're done using the computer, it's important to **shut down properly** through the menu — not by pressing the power button or pulling out the plug. The shutdown process gives the computer a chance to save any open work, finish what it's doing, and store its state safely before turning off. Cutting the power suddenly is like slamming a book shut in the middle of writing a page — some of what you were doing might not get saved, and in some cases the computer can have trouble starting up correctly next time.

From your study of computer parts, you know that the monitor (screen) is separate from the computer tower or laptop body. Each has its own power button. Turning the monitor off just makes the screen dark — the computer is still running and you'd come back to see everything where you left it. Turning the computer itself off is the step that actually ends the session. When in doubt, always use the shutdown option in the menu rather than any power button.


