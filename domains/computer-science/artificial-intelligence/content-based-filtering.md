---
id: content-based-filtering
title: Content-Based Filtering
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: recommendation-systems
  type: hard
- id: feature-engineering-selection
  type: soft
builds-toward:
- hybrid-recommendation
tags:
- content-based
- item-features
- user-profile
stage: advanced
status: draft
---

# Content-Based Filtering

## Core Idea
Content-based filtering recommends items similar to those a user previously liked, using rich item features (genre, actors, keywords). User profiles aggregate interaction history; recommendations match profiles to item features using similarity metrics. This approach handles new items well but requires detailed metadata and can lead to narrow recommendations.

## Explainer

From your introduction to recommendation systems, you know the basic challenge: given a user's history, predict what they will like next. **Content-based filtering** approaches this by focusing on *what* items are, rather than *who else* liked them. If you enjoyed a science fiction novel with themes of artificial intelligence and a dystopian setting, a content-based system looks for other items sharing those features — regardless of whether any other user has rated them. This stands in contrast to collaborative filtering, which relies on finding similar users.

The system works in two stages. First, each item is represented as a **feature vector** describing its attributes. For movies, features might include genre, director, cast, plot keywords, and release year. For articles, features could be extracted using techniques from feature engineering — TF-IDF vectors of the text, named entities, topic tags. Second, the system builds a **user profile** by aggregating the feature vectors of items the user has interacted with, weighted by their ratings or engagement signals. If a user has watched and rated highly ten action movies and two romantic comedies, their profile will have strong weights on action-related features. Recommendation then becomes a similarity computation: score each candidate item by how closely its feature vector matches the user profile, typically using cosine similarity or dot product.

Content-based filtering has a distinctive strength: it handles the **cold-start problem for items** elegantly. A brand-new movie that no one has rated yet can still be recommended based on its metadata — its genre, director, and plot description are enough to match it against user profiles. Collaborative filtering cannot do this because it needs rating data from other users. Content-based systems are also transparent: you can explain a recommendation by pointing to the matching features ("recommended because you liked other films by this director").

The approach has real limitations, however. It requires **rich, structured metadata** for every item, which can be expensive to create and maintain. More fundamentally, content-based filtering tends toward **over-specialization**: it recommends items similar to what the user already likes, creating a filter bubble that never surfaces surprising or diverse content. A user who has only watched comedies will never be recommended a documentary, no matter how much they might enjoy it. This is why production systems often combine content-based filtering with collaborative methods in **hybrid approaches**, using content features to handle new items and cold starts while relying on collaborative signals to introduce serendipity and capture preferences that metadata alone cannot express.
