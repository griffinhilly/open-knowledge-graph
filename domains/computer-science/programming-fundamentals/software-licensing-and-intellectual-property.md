---
id: software-licensing-and-intellectual-property
title: Software Licensing and Intellectual Property
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: hello-world
  type: soft
- id: technology-ethics
  type: soft
builds-toward: []
tags:
- intellectual-property
- copyright
- open-source
- licenses
- creative-commons
- computing-ethics
- AP-CSP
stage: formal-systems
status: validated
---
# Software Licensing and Intellectual Property

## Core Idea
Intellectual property law gives creators rights over things they make. Source code is protected by copyright as soon as it is written, in most countries without any registration, so by default nobody else may copy or redistribute it without permission. A software license is the permission: it states what others may do with the code and on what conditions. Open-source licenses grant broad rights to use, study, change and share code, and they differ mainly in whether modified versions must stay open.

## How It's Best Learned
Have students find the LICENSE file in three real open-source projects and summarize, in one sentence each, what they may and may not do. Compare a permissive license (MIT) and a copyleft license (GNU GPL) on the same scenario: "I modify this library and sell my app." Discuss everyday cases such as copying a code snippet from a forum, using images in an app, and the difference between plagiarism (a matter of honest credit) and copyright infringement (a matter of permission).

## Common Misconceptions
- Code posted publicly online with no license is free for anyone to use. (Without a license, the author keeps the default exclusive rights; public visibility is not permission.)
- Giving credit to the author makes any copying legal. (Credit avoids plagiarism, but copying still needs permission from a license or a legal exception.)
- Copyright protects the idea behind a program or an algorithm. (Copyright protects the specific written expression; ideas and methods are not covered by copyright, though some inventions can be patented.)
- Open source means "no rules". (Open-source licenses are legal licenses with conditions, such as keeping the copyright notice or sharing source code of modified versions.)

## Questions

```yaml
- question: "A student finds a useful function in a public code repository that has no LICENSE file and no statement about permissions. What is the safest accurate description of the student's position?"
  type: multiple-choice
  options:
    - "The code is in the public domain because anyone can see it"
    - "The code may be used freely as long as the author is credited"
    - "The author still holds copyright, so copying it into another project needs the author's permission"
    - "The code may be used freely in school projects, but not in paid products, under every country's law"
  answer: 2
  explanation: "Copyright applies automatically when code is written. Making code visible does not grant a license. Without one, the default is that the author keeps the exclusive right to copy and distribute it, so the student should ask or find another source. Some limited uses may fall under exceptions such as fair use in the United States, but that depends on the facts."

- question: "A company modifies an open-source library and ships the modified version inside a product it distributes to customers. Under which license is the company required to make the source code of its modified library available under the same license?"
  type: multiple-choice
  options:
    - "MIT License"
    - "BSD 2-Clause License"
    - "GNU General Public License (GPL)"
    - "Apache License 2.0"
  answer: 2
  explanation: "The GPL is a copyleft license: if you distribute a modified version, you must offer its source code under the GPL as well. MIT, BSD and Apache 2.0 are permissive licenses that allow modified versions to be distributed under other terms, including closed-source ones, as long as their conditions (such as keeping notices) are met."

- question: "Copyright law protects the general idea of an algorithm, such as 'sort a list by repeatedly swapping neighbors that are out of order', so no one else may write their own code for it."
  type: true-false
  answer: false
  explanation: "Copyright covers a particular written expression, such as one specific implementation. Anyone may write their own independent code for the same idea. Patents can protect some technical inventions, but that is a separate system with its own requirements."

- question: "What problem do Creative Commons licenses solve for people who create images, music or text?"
  type: short-answer
  answer: "They give creators a simple, standard way to grant the public some rights in advance, such as permission to share or adapt a work as long as the creator is credited, without each user having to ask for permission individually."
  explanation: "Creative Commons licenses come in a few combinations of conditions, such as attribution (BY), share-alike (SA), noncommercial (NC) and no derivatives (ND). Creative Commons itself recommends software-specific licenses such as MIT or the GPL for code."
```

## Explainer

When you write a program, you create something the law treats as property, even though you cannot touch it. **Intellectual property** is the general name for these rights. Three kinds matter most in computing. **Copyright** protects original creative expression, including source code, documentation, images and music. **Patents** protect certain new inventions, and some software-related inventions can be patented. **Trademarks** protect names and logos, such as a product's brand.

Copyright is the one programmers meet daily. In most countries it applies automatically the moment work is created, with no form to file. By default, the copyright holder alone may copy, change and distribute the work. Copyright covers the specific expression, not the idea. Two people can write separate code for the same algorithm, and neither copies the other.

Because the default is "all rights reserved", sharing code needs a **license**: a statement from the copyright holder granting permission on stated terms. When you see a `LICENSE` file in a project, that file is what lets you use the code at all.

**Open-source licenses** grant everyone the right to use, study, modify and share the code. They fall into two broad groups. **Permissive** licenses, such as MIT, BSD and Apache 2.0, ask for little beyond keeping the copyright notice, and they allow the code to be used inside closed-source products. **Copyleft** licenses, such as the GNU GPL, add a condition: if you distribute a modified version, you must release its source code under the same license. Many large projects, including the Linux kernel, use the GPL.

For non-software works, **Creative Commons** offers standard licenses built from simple conditions. "BY" requires credit, "SA" requires sharing adaptations under the same terms, "NC" forbids commercial use, and "ND" forbids changes. A photo marked CC BY may be reused in your app as long as you credit the photographer.

Two distinctions prevent common mistakes. First, visible is not the same as licensed: code on a public website still belongs to its author. Second, credit is not the same as permission. Citing a source avoids plagiarism, which is about honesty, but it does not grant the legal right to copy. Some countries allow limited uses without permission, such as fair use in the United States, but those exceptions depend on the details of each case.
