---
id: app-permissions-and-privacy
title: App Permissions and Privacy
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: digital-privacy-fundamentals
  type: hard
- id: smartphone-basics
  type: soft
tags:
- permissions
- privacy
- mobile
- data-collection
stage: formal-systems
status: draft
---

# App Permissions and Privacy

## Core Idea
Every app on your phone requests permission to access device features — camera, microphone, location, contacts, storage — and these permissions determine how much of your personal data the app can collect. Many apps request far more access than they need to function, using that data for advertising, analytics, or resale to data brokers. Reviewing and revoking unnecessary permissions is one of the most effective privacy actions you can take, and both iOS and Android now offer granular controls including "only while using the app" and one-time permissions.

## How It's Best Learned
Open your phone's privacy settings and review the permission list for your five most-used apps. Revoke any permission that does not make sense for the app's core function (does a flashlight app need your contacts?). Enable permission usage indicators so you can see when your camera or microphone is actively accessed.

## Common Misconceptions
- Granting location access "always" versus "while using" is not a minor distinction — "always" lets an app track your movements 24/7 in the background, building a detailed profile of your daily routines.
- An app's privacy policy does not mean your data is private; it discloses what data is collected, and most policies explicitly state that data is shared with third parties.
- Denying a permission does not necessarily break an app — most apps degrade gracefully, and the ones that refuse to work without unnecessary permissions are the ones you should be most suspicious of.

## Explainer

From your study of digital privacy fundamentals, you know that apps and services collect data through multiple channels — cookies, device fingerprinting, usage logs — often without your active awareness. App permissions are the most direct and controllable layer of that data collection: they are explicit gates your operating system requires an app to pass through before it can access specific device hardware or personal data. When you grant an app permission to access your location, camera, microphone, or contacts, you're allowing that app to query that resource directly — and to do so as often as it wants within the scope you granted.

The critical distinction that most users miss is **scope**. "Always" location access means the app can query your GPS coordinates at any moment — while you're using it, while it's running in the background, and even while your screen is off. A navigation app needs this. A weather app does not — knowing your approximate neighborhood zip code is sufficient for weather, and that can be provided without real-time tracking. A fitness app might legitimately want always-on GPS for run tracking, but even then, you should ask whether you want that data going to the app's servers. The "while using the app" permission grants access only when you've actively opened the app and it's in the foreground — dramatically reducing the window for passive data collection.

The economic context matters for understanding why apps request permissions they don't technically need. Many apps are offered free to users because the real business model is data. Location data, for example, is sold to **data brokers** who aggregate it with data from dozens of other apps to build detailed profiles of individuals' movements, routines, and behaviors. This profile can then be sold to advertisers, insurers, employers, or anyone willing to pay. The app doesn't need to build or sell the profiles itself — it just sells the raw data stream, and the brokers do the aggregation. A game that requests microphone access, a flashlight app that requests your contacts, a free utility that wants "always" location — these requests are red flags because no plausible feature of the app requires them. The permission is the product.

Your practical defense is a regular **permission audit**. Both iOS and Android make this straightforward: go to Privacy/Permissions in settings, and you can view all apps that have requested each permission type, see which have been granted, and revoke individually. The question to ask for each permission is: "What feature of this app would stop working if I revoked this?" If you can't identify a specific feature, revoke it. Modern operating systems also provide **permission usage indicators** — a small icon when the camera or microphone is actively being accessed — and usage logs showing which apps accessed location data and when. These tools transform permission management from a one-time installation decision into an ongoing practice of monitoring what you've allowed and adjusting it over time.
