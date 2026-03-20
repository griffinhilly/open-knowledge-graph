---
id: understanding-urls-web-addresses
title: Understanding URLs and Web Addresses
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: web-browser-essentials
  type: hard
builds-toward:
- evaluating-source-credibility-online
- recognizing-online-scams-fraud
tags:
- url
- domain
- web-address
- http-https
stage: abstract-reasoning
status: draft
---

# Understanding URLs and Web Addresses

## Core Idea
A URL (Uniform Resource Locator) is the web address that tells your browser which page to load. URLs consist of a protocol (http or https), a domain name, and a path. The 'https' protocol with a padlock icon indicates a secure connection. Understanding URL structure helps you identify legitimate websites, spot phishing attempts, and navigate the web more effectively.

## How It's Best Learned
Visit several websites and examine the URLs in the address bar. Notice the difference between http and https. Try typing a URL directly instead of using search.

## Common Misconceptions
- The domain name is always the website owner's legal company name.
- http and https are interchangeable.
- A professional-looking domain guarantees legitimacy.

## Questions

```yaml
- question: "You receive an email with a link to 'paypal.com.account-verify.ru/login'. Is this a link to PayPal's official website?"
  type: multiple-choice
  options:
    - "Yes — it contains 'paypal.com' in the address, confirming it is PayPal's domain"
    - "No — the actual registered domain is 'account-verify.ru'; 'paypal.com' is just a subdomain name designed to deceive"
    - "Yes — only the path after the domain matters for identifying the site"
    - "No — PayPal only uses secure .com addresses, and this one ends in .ru"
  answer: 1
  explanation: "The critical rule: the real domain owner is identified by the name directly to the left of the top-level domain (.com, .ru, .net, etc.). In 'account-verify.ru', the registered domain is 'account-verify' and the TLD is '.ru' — meaning someone registered account-verify.ru, not PayPal. 'paypal.com' appears as a subdomain prefix, which anyone can add to any domain they own. This is one of the most common phishing techniques. Option D is a tempting distraction — the .ru extension is suspicious, but the real issue is domain structure, not country code."

- question: "What does the padlock icon and 'https' actually guarantee about a website?"
  type: multiple-choice
  options:
    - "The website is legitimate, safe, and owned by a verified, reputable organization"
    - "The website has passed a government security audit"
    - "Data traveling between your browser and the website is encrypted so eavesdroppers cannot read it"
    - "The website's content has been checked for malware by your browser"
  answer: 2
  explanation: "HTTPS encrypts the *connection*, not the website itself. A scam site can have a valid HTTPS certificate and padlock — in fact, most phishing sites now do, because free certificates are easy to obtain. The padlock means your data is encrypted in transit; it says nothing about whether the site itself is trustworthy. Always check the domain identity separately from the padlock."

- question: "A website with a professional-looking design, a recognizable brand name in the URL, and an https padlock is guaranteed to be a legitimate, safe site."
  type: true-false
  answer: false
  explanation: "None of these individually or together guarantee legitimacy. Professional design is easy to copy; a brand name can appear as a subdomain on a malicious domain (see paypal.com.scam-site.net); HTTPS certificates are freely available to anyone. Safety requires checking the actual registered domain — the part directly before the TLD — and confirming it matches the organization you expect. A site can fake all three trust signals while still being a phishing site."

- question: "In the URL 'https://store.example.com/products/shoes', the registered domain owner controls 'example.com', not 'store', 'products', or 'shoes'."
  type: true-false
  answer: true
  explanation: "'store' is a subdomain (a subdivision example.com created for itself), and '/products/shoes' is a path (a folder structure within the site). Only 'example.com' is the registered domain — the name someone paid to register. The domain owner controls what subdomains and paths exist. This is why you must read the part just before the TLD to identify who owns a site."

- question: "How do scammers use URL structure to make a malicious link look like it belongs to a trusted website? What should you look for to detect this trick?"
  type: short-answer
  answer: "Scammers register a domain like 'account-verify.net' and then create a subdomain using a trusted brand name, producing a URL like 'bankofamerica.com.account-verify.net'. The trusted name appears first, making casual readers think they're on the real site. To detect it: always identify the registered domain by finding the TLD (.com, .net, .org, etc.) and reading the word immediately to its left — that is the actual owner. Anything before that is just a subdomain the owner created."
  explanation: "This trick exploits the way humans read left-to-right — we see the trusted name first and stop reading. Trained URL readers read right-to-left from the TLD to find the actual domain owner. Practicing this habit makes phishing URLs immediately obvious."
```

## Explainer

Now that you know how to navigate with a browser, it's worth understanding exactly what you're typing into the address bar and what each piece means. A **URL** (Uniform Resource Locator) is a structured address that tells your browser three things: what communication method to use, which server to contact, and where on that server the specific page lives. Breaking down a URL like `https://www.bbc.com/news/world` reveals: `https` is the **protocol**, `www.bbc.com` is the **domain**, and `/news/world` is the **path** to a specific page within that domain.

The **protocol** — `http` or `https` — specifies how your browser and the website communicate. The `s` in `https` stands for "secure": it means all data traveling between your browser and the website is encrypted, so no one watching the network connection can read it. Your browser signals this with a padlock icon in the address bar. This matters enormously when you're entering passwords, payment information, or any sensitive data — always verify the padlock is present before submitting a form. On an `http` site, that information travels as readable text.

The **domain name** is the most important piece for evaluating trust. Domains are hierarchical: reading from right to left, you move from general to specific. In `bbc.com`, `.com` is the **top-level domain** (TLD), and `bbc` is the registered name. The critical rule is that the real owner of a site is identified by the name directly to the left of the TLD. Scammers exploit this by creating addresses like `bbc.com.account-update.net` — where the actual domain is `account-update.net`, not `bbc.com`. The `bbc.com` part is just a subdirectory name designed to fool you. Always check what appears just before `.com`, `.org`, `.net`, or the country code at the end.

The **path** is everything after the domain — it tells the server which specific page, image, or file you want. Paths look like file folders on a computer because they work the same way: `/news/world` means "go into the `news` folder and find the `world` page." You rarely need to type paths manually; clicking links fills them in automatically. But reading a path can tell you a lot about a page's structure — a URL ending in `/login` or `/checkout` tells you exactly where you are in a website's flow, which is useful for catching redirects to unexpected locations.
