---
id: what-is-a-file
title: Understanding Computer Files
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: file-system-basics
  type: soft
builds-toward:
- what-is-a-folder
- saving-and-opening-files
tags:
- files
- storage
- fundamentals
- organization
stage: concrete-operations
status: draft
---
# Understanding Computer Files

## Core Idea
A file is like a digital container that holds information—it could be a document, a picture, a song, or a video. Every file has a name and a type (shown by the ending, like .txt or .jpg). Files live inside folders on your computer where you can find them later.

## How It's Best Learned
Show children different types of files on their computer—a text document, a photo, a video—and point out the different file endings. Let them open a file to see what's inside.

## Common Misconceptions
- Thinking the file extension (.txt, .jpg) is separate from the file name.
- Not understanding that the file name is just a label you can change.
- Thinking files disappear if you close the window.

## Questions

```yaml
- question: "Kenji finishes writing a report and closes the application window without saving his new changes. What happens to the file he had saved on the computer last time?"
  type: multiple-choice
  options:
    - "The old file is deleted because he closed the window"
    - "The old saved file remains on the computer unchanged"
    - "The file disappears until he reopens the application"
    - "The file is automatically updated with his new changes"
  answer: 1
  explanation: "Closing a window does not affect files already saved on the computer's storage. The previously saved version remains exactly where it was. What Kenji loses is only the new work he added during this session — changes he made but didn't save. The file itself (the container on disk) persists independently of whether any application window is open."

- question: "A file is named 'vacation.jpg'. What does the '.jpg' part tell you?"
  type: multiple-choice
  options:
    - "That the file is very large in size"
    - "That the file is stored in a special vacation folder"
    - "The type of information inside — in this case, a photo or image file"
    - "The date the file was created"
  answer: 2
  explanation: "The '.jpg' at the end of a filename is a file extension — it indicates the file's type and tells the computer which program should open it. '.jpg' is an image format, so the computer knows to open this file with an image viewer or photo app. Extensions like '.txt' (text), '.mp3' (audio), and '.pdf' (document) each signal a different type of content. The extension is not about size, location, or date."

- question: "You can rename a file to something completely different without changing the information stored inside it."
  type: true-false
  answer: true
  explanation: "The file name is just a label — it tells you and the computer where to find the file and what to call it, but it has no effect on the contents. Renaming 'my-essay.txt' to 'draft1.txt' leaves the text inside completely unchanged. The name and the contents are two separate things."

- question: "When you close a file's window, the file is deleted from the computer."
  type: true-false
  answer: false
  explanation: "Closing a window only stops displaying the file — it does not delete it. The file remains on the computer's storage exactly where it was saved, until you explicitly choose to delete it. Think of it like closing a book: the book still exists on the shelf, you've just stopped looking at it. Files are only removed when you delete them and empty the trash/recycle bin."

- question: "Why does a file's extension (like .txt or .jpg) matter, and what could go wrong if the extension is missing or incorrect?"
  type: short-answer
  answer: "The extension tells the computer what type of information is inside the file and which program should open it. If the extension is missing or wrong, the computer may not know how to open the file, or it might try to open it with the wrong program and display garbled content."
  explanation: "File extensions are the computer's way of identifying file types, since it can't always determine the content just by looking inside. A '.jpg' image opened by a text editor would display as meaningless characters, not a photo. Operating systems use extensions to route files to the correct application, so understanding them helps users troubleshoot common 'my file won't open' problems."
```

## Explainer

Think about a piece of paper with writing on it. The writing is the information, and the paper holds it. A **file** is the same idea, but digital — it's a container that holds information, stored on your computer so you can find and use it again later. Just like paper, a file just sits there waiting until you decide to open it or use it.

Every file has two important parts: its **name** and its **type**. The name is what you call it — like "my drawing" or "birthday list." The type tells the computer what kind of information is inside. You can usually see the type at the end of the name after a dot — that's called the **file extension**. A file called "story.txt" is a text file (just words). A file called "photo.jpg" is a picture. A file called "song.mp3" is audio. The extension is part of the full name, but it tells the computer (and you) what program should open it.

One of the most important things to know about files is that they don't disappear when you close them. Closing a window is like putting a book back on a shelf — the book is still there, you just can't see it anymore. The file lives on your computer's storage (its hard drive) and stays there until you decide to delete it. This is different from the work you're doing *in* the file — if you write something new and close without saving, that new writing might be lost. But the file itself stays put.

Files live inside **folders** (your next topic), which work like drawers or boxes that keep related files organized together. For now, the key idea is this: a file is a named container of information that lives on your computer, has a type shown by its extension, and stays there until you choose to move or delete it.
