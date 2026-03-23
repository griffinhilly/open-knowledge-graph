---
id: saving-and-opening-files
title: Saving and Opening Computer Files
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: what-is-a-file
  type: hard
- id: what-is-a-folder
  type: hard
builds-toward:
- file-management-and-organization
tags:
- files
- saving
- storage
- fundamentals
stage: concrete-operations
status: validated
---

# Saving and Opening Computer Files

## Core Idea
When you make something on a computer—like a document or drawing—you need to save it to keep the work permanently. Saving puts your file in a folder where you can find it later. You can then open the file again to keep working on it or look at it.

## How It's Best Learned
Have children create something in a program, then save it using Ctrl+S or File > Save. Give it a name and choose a folder. Then close the program and open the file again.

## Common Misconceptions
- Thinking closing a program automatically saves your work.
- Not knowing where the file was saved, so they can't find it later.
- Thinking saving means the file is somewhere in the cloud rather than on the computer.

## Questions

```yaml
- question: "You spend 30 minutes writing a letter on your computer, then close the program. When you open the program again, the letter is gone. What most likely caused this?"
  type: multiple-choice
  options:
    - "The computer deleted the file to save storage space"
    - "The file was saved in the wrong folder"
    - "The letter was never saved before the program closed"
    - "The program has a bug that loses files randomly"
  answer: 2
  explanation: "When you work on a computer, your work lives in temporary memory (RAM) — it disappears the moment the program closes unless you explicitly saved it to permanent storage. Closing a program does NOT automatically save your work. The letter existed only in temporary memory and was never written to a file on the drive."

- question: "A student finishes a drawing, clicks File > Save, names it 'mypicture.png', and chooses the Desktop folder. Then the power goes out. When the power comes back, what happens to the drawing?"
  type: multiple-choice
  options:
    - "The drawing is lost because the power outage erased it"
    - "The drawing is still on the Desktop because it was saved to permanent storage"
    - "The drawing must be recreated because RAM stores files"
    - "The drawing was backed up automatically to the cloud"
  answer: 1
  explanation: "Once a file is saved, it is written to permanent storage (the computer's hard drive or SSD). Permanent storage keeps files even when power is cut — that is the whole point of saving. RAM (temporary memory) clears when power is lost, but the drawing was already moved from RAM to the drive at the moment of saving."

- question: "Closing a program automatically saves your work."
  type: true-false
  answer: false
  explanation: "This is the most common and costly misconception about file saving. Programs store your current work in temporary memory (RAM), which is erased when the program closes. Saving is a separate, deliberate action that writes your work to permanent storage. Many programs will prompt 'Do you want to save?' when you close without saving — which is precisely because closing does not save automatically."

- question: "Using File > Save As creates a separate copy of the file with a new name or location, leaving the original file unchanged."
  type: true-false
  answer: true
  explanation: "Save As writes a copy of the current file to a new name or folder, leaving the original file unchanged. This is useful when you want to keep two versions of a document — for example, 'essay-draft.docx' and 'essay-final.docx'. Regular Save updates the existing file in place; Save As creates a new, independent copy."

- question: "Why does it matter where you save a file, not just that you saved it?"
  type: short-answer
  answer: "Knowing where a file was saved is necessary to find and open it again. If you save a file but don't know which folder it went into, the file still exists but is effectively lost until you search for it. Choosing a meaningful folder name and consistent location makes it possible to retrieve files reliably."
  explanation: "Saving preserves work permanently, but if you don't know the location, you can't find it again. A common experience for new computer users is saving a file successfully but then being unable to open it because they didn't pay attention to which folder was selected. The two steps — saving and remembering where — are both necessary."
```

## Explainer

When you draw a picture or write words on a computer, that work lives temporarily in the computer's memory — like holding something in your hands. The moment you turn off the program or the computer, that memory disappears, just like dropping what you were holding. **Saving** is the act of writing your work permanently onto the computer's storage, like putting it into a drawer where it will stay even after you walk away.

You already know what a file is — a container that holds your work — and what a folder is — a place to organize files. Saving connects these two ideas: when you save, you give your work a name (that becomes the file name) and choose which folder it goes into. The program writes your work into that folder as a file. From that moment on, the file exists independently. You can close the program, restart the computer, or walk away for a week, and the file will still be there when you come back.

Opening a file is the reverse process: you tell the computer which file you want, and the program reads the file's contents from storage back into memory so you can see and change them again. The two most common ways to open a file are through **File > Open** in a program's menu (which lets you browse for any file) or by double-clicking the file icon in a folder (which opens the right program automatically).

The most important habit to build is saving frequently while you work. Many programs let you save with the keyboard shortcut **Ctrl+S** (or Command+S on a Mac) — pressing it takes less than a second. If you save every few minutes, the worst that can happen in a crash or power outage is losing a few minutes of work. If you forget to save, you can lose everything. As you get comfortable, you'll also learn **Save As**, which saves a copy of the file under a new name or in a different folder — useful when you want to keep two versions of the same document.
