---
id: event-driven-programming
title: Event-Driven Programming
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-defining-calling
  type: hard
- id: parameters-and-arguments
  type: hard
- id: while-loops
  type: soft
- id: program-structure
  type: soft
builds-toward: []
tags:
- events
- event-handlers
- callbacks
- event-loop
- GUI
- paradigms
stage: formal-systems
status: validated
---
# Event-Driven Programming

## Core Idea
In event-driven programming, the order in which code runs is set by events, such as a mouse click, a key press, a timer firing or a network message, rather than by a fixed top-to-bottom sequence. The programmer writes small functions called event handlers (or callbacks) and registers each one for an event. An event loop, usually supplied by a library or the browser, waits for events and calls the matching handler each time one occurs. Graphical interfaces, web pages, games and many servers are built this way.

## How It's Best Learned
Build a tiny interface with two buttons and a label, and have students predict what prints for different click orders. Contrast it with a script that runs once from top to bottom. Then deliberately put a slow loop inside a click handler so students see the whole window freeze, which makes the role of the event loop concrete.

## Common Misconceptions
- Handlers run in the order they appear in the source file. (They run whenever their events occur, in whatever order the user or system produces those events.)
- Registering a handler means writing `on_click()` with parentheses. (The parentheses call the function immediately; you pass the function itself, `on_click`, so the library can call it later.)
- A handler can do long work without affecting anything else. (In a single-threaded event loop, no other event is processed until the current handler returns, so long handlers freeze the interface.)

## Questions

```yaml
- question: "In Python's tkinter, a student writes `Button(root, text='Save', command=save_file())`. The file is saved once when the program starts, and clicking the button does nothing. Why?"
  type: multiple-choice
  options:
    - "tkinter buttons can call a function only once"
    - "save_file() runs immediately while the button is built, and its return value (None) is registered instead of the function"
    - "The button needs a second argument naming the event type"
    - "save_file must be defined after the button is created"
  answer: 1
  explanation: "Writing save_file() calls the function on the spot and passes its result to command. The correct form is command=save_file, which passes the function object so tkinter can call it each time the button is clicked."

- question: "In an event-driven program, event handlers always run in the order they are defined in the source code."
  type: true-false
  answer: false
  explanation: "The order depends on when events happen. If a user clicks 'Stop' before 'Start', the Stop handler runs first, even if it is defined later in the file."

- question: "A click handler in a single-threaded GUI program runs a loop that takes 10 seconds. What does the user most likely see during those 10 seconds?"
  type: multiple-choice
  options:
    - "The window keeps responding normally, because each click gets its own copy of the program"
    - "The window stops responding to clicks and redraws until the handler finishes"
    - "The program crashes immediately"
    - "The loop is skipped, because handlers cannot contain loops"
  answer: 1
  explanation: "The event loop calls one handler at a time and cannot process other events until that handler returns. Long work is usually split up, scheduled with timers, or moved to a background thread or asynchronous task."

- question: "What is an event loop, and why do most event-driven programs not need to write one themselves?"
  type: short-answer
  answer: "An event loop repeatedly waits for the next event, finds the handler registered for it, and calls that handler. GUI toolkits, browsers and game frameworks supply the loop (for example tkinter's mainloop()), so the programmer only writes and registers handlers."
  explanation: "This division of labor is the core of the paradigm: the framework owns the control flow, and the programmer supplies the reactions."
```

## Explainer

The programs you have written so far run like a recipe. Line 1 runs, then line 2, and so on, with loops and conditionals changing the path. That style fits a program that reads input, computes and prints. It fits poorly when a program must wait for a person. A drawing app does not know whether the next action will be a click, a key press or a window resize.

**Event-driven programming** turns control around. You write a function for each thing that can happen, and you tell a library which function goes with which event. In a web page, `button.addEventListener("click", handleClick)` registers `handleClick` for clicks on that button. In Python's tkinter, `Button(root, text="Go", command=go)` does the same. These functions are called **event handlers** or **callbacks**, because the library calls them back later.

Notice that you pass `go`, not `go()`. A function name without parentheses is a value that refers to the function. Adding parentheses calls it right away. This is the most common beginner bug in event-driven code.

After registering handlers, the program starts an **event loop**, such as tkinter's `root.mainloop()`. The loop is simple in principle: wait for an event, look up its handler, call the handler, repeat. The operating system or browser collects events into a queue, and the loop takes them out one at a time.

Two consequences follow. First, you cannot predict the order in which handlers run. Code must work whether the user clicks "Load" before "Save" or the reverse, so handlers often check the program's state, for example disabling Save until a file is loaded. Second, in the common single-threaded design, only one handler runs at a time. While a handler is busy, no other events are handled and the window cannot even redraw. Good handlers do a small amount of work and return quickly. Long tasks are split into pieces with timers, or run in the background.

Events are not only for interfaces. Timers fire events at set intervals, which is how many games update their screens. Servers can react to incoming network messages in the same style. The underlying idea is always the same: the framework owns the main loop, and your code supplies the reactions.
