---
id: reading-an-email
title: Reading an Email
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: opening-a-web-browser
  type: soft
- id: connecting-to-the-internet
  type: hard
builds-toward:
- writing-and-sending-an-email
- email-fundamentals
tags:
- email
- communication
- fundamentals
stage: concrete-operations
status: validated
---

# Reading an Email

## Core Idea
Email is a way for people to send written messages to each other online. To read an email, you go to your email account (like Gmail or Outlook) and sign in with your password. Your inbox shows a list of messages, and you click on one to open and read it.

## How It's Best Learned
Help children log into an email account. Show them the inbox with received emails. Click on one together and read it, pointing out the sender's name and the message.

## Common Misconceptions
- Not knowing that spam or junk emails might be in a separate folder.
- Clicking on suspicious links in emails without checking who sent them.
- Not realizing email addresses can be spoofed (fake sender).

## Questions

```yaml
- question: "You receive an email with the display name 'Your Bank' asking you to click a link to verify your account. What should you check before clicking?"
  type: multiple-choice
  options:
    - "The subject line, to see if it mentions your account number"
    - "The actual email address the message was sent from, not just the display name shown"
    - "Whether the email is in your inbox rather than your Spam folder"
    - "How long the link is — longer links are generally safer than short ones"
  answer: 1
  explanation: "The display name ('Your Bank') is just text anyone can type — it tells you nothing about where the email actually came from. The real sender's email address (visible by clicking on or hovering over the sender name) is what reveals the true origin. A message claiming to be from a bank but arriving from a random address like xz291@freemail.ru is almost certainly a scam. Checking the actual address, not the display name, is the single most important email safety habit."

- question: "You are expecting an important email from a friend but can't find it in your inbox. Where else should you look?"
  type: multiple-choice
  options:
    - "The Sent folder, which stores copies of messages you have received"
    - "The Spam or Junk folder, where email services sometimes automatically sort legitimate messages"
    - "Your web browser's download folder, where email attachments are stored"
    - "You cannot find it — emails are either in the inbox or permanently lost"
  answer: 1
  explanation: "Email services automatically filter incoming messages they suspect are spam or advertising into Spam or Junk folders. Legitimate messages sometimes get caught by these filters incorrectly. If you're expecting something that hasn't appeared in your inbox, checking the Spam/Junk folder is the first place to look. The Sent folder contains messages you sent — not messages you received."

- question: "If an email's display name shows 'Amazon', the message was definitely sent from Amazon's official email servers."
  type: true-false
  answer: false
  explanation: "Display names are freely set by whoever sends the email — they can be anything. This is called spoofing: a scammer can make an email display as 'Amazon', 'PayPal', or 'Your Bank' while the actual sending address is completely unrelated. The only reliable indicator of the true sender is the actual email address, not the display name. This is why checking the real address before clicking links is so important."

- question: "In a typical email inbox list view, each row shows the sender, the subject line, and when the message arrived."
  type: true-false
  answer: true
  explanation: "The inbox is a list where each row is one message, and the three key pieces of information shown at a glance are: who sent it (sender), what it's about (subject line), and when it arrived (date/time). Unread messages are often bolded or highlighted. Clicking a row opens the full message. This is the same 'click to go deeper' navigation pattern used in web browsers."

- question: "What is email spoofing, and why does it matter when deciding whether to click a link in an email?"
  type: short-answer
  answer: "Spoofing is when someone sends an email that displays a trusted name (like 'PayPal' or 'Your Bank') as the sender, while the actual email address the message came from belongs to someone completely different. The display name is just text — anyone can type anything. The real email address, visible by examining the sender details, reveals the true origin. This matters because scammers use spoofing to make fake emails look like they came from trusted sources, tricking people into clicking malicious links or revealing personal information. Checking the actual address — not just the display name — is what catches these fakes."
  explanation: "Understanding spoofing changes how you read emails fundamentally: you can no longer trust the name you see. The practical skill is knowing where to look (the actual email address behind the display name) and what red flags to notice (an address that doesn't match the organization it claims to be from)."
```

## Explainer

Email works a lot like a digital post office. When someone sends you a message, it travels across the internet — which you already know how to connect to — and lands in your **inbox**, a kind of personal mailbox that belongs to your email address. Your email address is unique to you (like a home address) and looks like a name followed by "@" and a service name, such as `yourname@gmail.com`. When you sign in to a service like Gmail or Outlook, you're unlocking your personal mailbox so you can see what's arrived.

The inbox is just a list. Each row represents one message, and it usually shows you three things at a glance: who sent it (**the sender**), what the message is about (**the subject line**), and when it arrived. Unread messages are often bold or highlighted. Clicking on a row opens the full message, where you can read everything the sender wrote. This is the same navigation pattern you've already used in a web browser — clicking to go deeper, using the back button to return to the list.

Not everything in your inbox belongs there. Email services automatically sort some incoming messages — advertising, newsletters, or suspected scams — into separate folders like **Spam** or **Junk**. That's why an important message might seem to disappear: it was sorted away from your main inbox. It's worth checking those folders if you're expecting something that hasn't arrived.

One important safety habit: check the sender's actual email address before clicking any link in a message. The sender's name you see displayed (like "Amazon") can be anything the sender types — but the real email address (shown in parentheses or when you hover) reveals where the message actually came from. A message claiming to be from a bank but arriving from a random address like `xz291@freemail.ru` is almost certainly fake. This is called **spoofing** — when someone disguises who they are — and recognizing it is one of the most practical digital skills you can build early.
