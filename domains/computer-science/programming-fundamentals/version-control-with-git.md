---
id: version-control-with-git
title: Version Control with Git
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: program-structure
  type: soft
- id: file-io-basics
  type: soft
- id: testing-and-validation-basics
  type: soft
builds-toward: []
tags:
- version-control
- git
- commits
- branches
- merging
- software-engineering
- collaboration
stage: formal-systems
status: validated
---
# Version Control with Git

## Core Idea
A version control system records the history of a project's files so that any earlier state can be inspected or restored, and so that several people can work on the same code without overwriting each other. Git, created by Linus Torvalds in 2005 for Linux kernel development, is the most widely used system. In Git, a commit is a saved snapshot of the project with a message, an author and a link to the commit before it. Branches let work proceed on separate lines of history that can later be merged.

## How It's Best Learned
Use Git on a real, small project from the first day: init, edit, check `git status`, stage with `git add`, commit with a clear message, and view `git log`. Draw the commit history as a chain of boxes, and redraw it after each branch and merge. Create a merge conflict on purpose in pairs, so that resolving one becomes a routine skill rather than a crisis.

## Common Misconceptions
- Git and GitHub are the same thing. (Git is the version control program that runs on your computer; GitHub is one of several services that host Git repositories online.)
- `git commit` saves every change in the folder. (It saves only what has been staged with `git add`; unstaged edits stay out of the commit.)
- Version control is only needed for team projects. (It also protects solo work, because any earlier working version can be recovered after a mistake.)
- A merge conflict means Git is broken or data is lost. (It means two branches changed the same lines, and Git is asking a person to choose the result.)

## Questions

```yaml
- question: "A student edits app.py, which Git already tracks, then runs `git commit -m \"fix bug\"` without running `git add`. What happens?"
  type: multiple-choice
  options:
    - "The edit to app.py is committed, because Git tracks the file"
    - "No commit is made, because no changes were staged"
    - "Git deletes the edit, because it was not staged"
    - "Git commits an empty file named app.py"
  answer: 1
  explanation: "git commit records the staging area (the index). With nothing staged, Git reports that no changes were added to the commit and makes no commit. The edit is still in the working folder. Running git add app.py first, or using git commit -a for tracked files, would include it."

- question: "Git and GitHub are two names for the same software."
  type: true-false
  answer: false
  explanation: "Git is a distributed version control system that works entirely on a local machine. GitHub is a web service for hosting Git repositories and adding features such as pull requests. Other hosts, such as GitLab and Bitbucket, also store Git repositories."

- question: "When does Git report a merge conflict while merging branch feature into main?"
  type: multiple-choice
  options:
    - "Whenever both branches contain new commits"
    - "Whenever the two branches touched the same file in any way"
    - "When both branches changed the same part of a file in different ways, so Git cannot choose automatically"
    - "Only when a file was deleted on one branch"
  answer: 2
  explanation: "Git can combine changes to different files, or to different parts of one file, automatically. A conflict arises when the same lines were changed differently on both sides (a delete-versus-edit clash also counts). Git then marks the region and waits for a person to decide."

- question: "Why do developers usually create a new branch to build a feature instead of committing directly to the main branch?"
  type: short-answer
  answer: "A branch isolates unfinished work. The main branch stays working and releasable while the feature is built and tested, other people can keep working in parallel, and the feature is merged in only when it is ready. If the idea fails, the branch can simply be abandoned."
  explanation: "Branches in Git are cheap pointers to commits, so creating one costs almost nothing. That makes isolating each piece of work practical."
```

## Explainer

Without version control, people save copies with names like `essay_final_v2_REAL.docx`. That habit fails quickly for code. You cannot tell which copy has which fix, and two people editing at once will overwrite each other. A **version control system** solves both problems by keeping a full, ordered history of a project.

Git stores a project in a **repository**, a folder plus a hidden `.git` directory that holds the history. Work follows a simple cycle. You edit files in the **working tree**. You choose which changes belong together and **stage** them with `git add`. Then `git commit -m "Add login check"` saves a **commit**: a snapshot of the staged project, your message, your name, the time, and a pointer to the previous commit. Each commit gets a unique ID computed from its contents, a hash such as `3f2a9c1...`. `git status` shows what has changed and what is staged, and `git log` lists the history.

Because every commit is kept, you can see exactly what changed between versions with `git diff`, and you can return to an earlier state if a change breaks the program. Good commits are small and focused, with messages that explain why the change was made.

**Branches** let history split. A branch is a movable name that points at a commit. You might create `feature-search` with `git switch -c feature-search`, make several commits there, and leave `main` untouched. When the feature works, `git merge feature-search` on `main` combines the two lines of history. If both branches changed different parts of the code, Git merges them automatically. If both changed the same lines differently, Git reports a **merge conflict**, marks the competing versions in the file, and waits for you to edit the result and commit it.

Git is **distributed**. `git clone` copies the whole repository, including all history, to your machine. You can commit offline. To share work, you `git push` your commits to a shared remote repository and `git pull` other people's commits from it. Services such as GitHub, GitLab and Bitbucket host those remotes and add review tools, but Git itself is separate from them.

Version control pays off even when working alone. It gives you an undo button for the whole project and a record of why each change was made.
