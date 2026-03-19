#!/usr/bin/env python3
"""Generate the Applied Rationality course for the Philosophy domain.

Creates ~30 topic files in domains/philosophy/applied-rationality/.
Run from the project root:
    python tools/generate_rationality_course.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE_DIR = ROOT / "domains" / "philosophy" / "applied-rationality"

DOMAIN = "philosophy"
COURSE = "applied-rationality"
STAGE = "formal-systems"
STATUS = "draft"

# Topic definitions: (id, title, prerequisites, builds_toward, tags, core_idea, best_learned, misconceptions)
# Prerequisites: list of (id, type) tuples
# builds_toward: list of topic IDs

TOPICS = [
    # === Foundations of Rationality ===
    {
        "id": "epistemic-vs-instrumental-rationality",
        "title": "Epistemic vs. Instrumental Rationality",
        "prerequisites": [
            ("what-is-knowledge", "soft"),
            ("probabilistic-reasoning", "soft"),
        ],
        "builds_toward": ["map-and-territory", "the-lens-that-sees-its-flaws", "bayesian-thinking-in-practice"],
        "tags": ["rationality", "epistemology", "decision-making", "foundations"],
        "core_idea": (
            "Epistemic rationality is the art of forming accurate beliefs — building a mental map "
            "that corresponds to the territory of reality. Instrumental rationality is the art of "
            "achieving your goals — choosing actions that produce desired outcomes given your beliefs. "
            "These two types of rationality are complementary: you cannot reliably achieve your goals "
            "with false beliefs, and the motivation to form true beliefs often comes from wanting to "
            "act effectively. The Rationalist tradition treats epistemic rationality as foundational, "
            "arguing that systematic improvement in belief-formation is both possible and trainable."
        ),
        "best_learned": (
            "Start by examining cases where the two types of rationality come apart. A comforting "
            "false belief might feel instrumentally useful (\"I'll definitely get the job\") but "
            "harms long-term planning. Conversely, someone might hold accurate beliefs but fail to "
            "act on them. Work through examples from your own life where accurate beliefs would have "
            "changed your actions, and where motivated reasoning led you to conclusions that felt "
            "good but turned out wrong."
        ),
        "misconceptions": [
            "Rationality is not the same as being emotionless or coldly calculating — emotions often carry real information and motivate useful action.",
            "Epistemic and instrumental rationality do not always conflict — in most real-world situations, having accurate beliefs directly serves your goals.",
            "Rationality is not about being \"right\" in arguments — it is about systematically improving the accuracy of your beliefs and the effectiveness of your actions.",
        ],
    },
    {
        "id": "map-and-territory",
        "title": "Map and Territory",
        "prerequisites": [
            ("epistemic-vs-instrumental-rationality", "hard"),
        ],
        "builds_toward": ["motivated-reasoning", "bayesian-thinking-in-practice", "the-lens-that-sees-its-flaws"],
        "tags": ["rationality", "epistemology", "mental-models", "representation"],
        "core_idea": (
            "The map is not the territory. Your beliefs about reality are representations — mental "
            "models — not reality itself. This distinction, drawn from Alfred Korzybski and central "
            "to the Rationalist tradition, has profound consequences: when your predictions fail, "
            "the map is wrong, not the territory. Rational agents update the map to match the "
            "territory rather than arguing that the territory should match the map. A good map is "
            "one that reliably predicts observations and compresses usefully — it does not need to "
            "capture every detail, but it must not systematically mislead."
        ),
        "best_learned": (
            "Practice noticing the difference between \"I believe X\" and \"X is true.\" When you "
            "encounter a surprising fact, ask: which part of my map was wrong? Find examples of "
            "map-territory confusion in everyday life — confusing the stock price with the company's "
            "health, confusing the grade with the learning, confusing the metric with the goal."
        ),
        "misconceptions": [
            "The map-territory distinction does not imply radical skepticism — it says maps can be wrong, not that we can never know anything.",
            "Having a simpler map is not always better — an oversimplified map that misses critical features is worse than a complex map that captures them.",
            "This is not just a metaphor — it is a practical framework for debugging beliefs when predictions fail.",
        ],
    },
    {
        "id": "the-lens-that-sees-its-flaws",
        "title": "The Lens That Sees Its Flaws",
        "prerequisites": [
            ("epistemic-vs-instrumental-rationality", "hard"),
            ("map-and-territory", "hard"),
            ("cognitive-biases-critical-thinking", "soft"),
        ],
        "builds_toward": ["debiasing-techniques", "calibration-training"],
        "tags": ["rationality", "metacognition", "self-improvement", "debiasing"],
        "core_idea": (
            "Human reasoning is like a lens that can examine its own distortions. Unlike other "
            "cognitive abilities, rationality includes the capacity to notice systematic errors in "
            "your own thinking and correct for them. This self-reflective property is what makes "
            "rationality trainable: once you learn that the availability heuristic causes you to "
            "overweight vivid examples, you can deliberately seek base rates. Once you learn that "
            "anchoring biases your estimates, you can generate estimates from multiple starting "
            "points. The Rationalist project rests on the empirical claim that knowing about biases, "
            "combined with deliberate practice, measurably improves reasoning quality."
        ),
        "best_learned": (
            "Begin with a concrete bias you can verify in yourself — try the anchoring effect with "
            "numerical estimation tasks, then repeat after learning about it. Track cases where "
            "knowing about a bias changed your actual behavior, not just your verbal agreement that "
            "biases exist. The gap between \"I know about bias X\" and \"I correct for bias X\" is "
            "where the real work of rationality happens."
        ),
        "misconceptions": [
            "Knowing about biases does not automatically correct them — debiasing requires deliberate, practiced techniques, not just awareness.",
            "This is not a claim that humans can become perfectly rational — it is the more modest claim that we can be systematically less wrong.",
            "Self-correction does not mean second-guessing every thought — it means having calibrated confidence about when to trust intuition and when to override it.",
        ],
    },
    {
        "id": "motivated-reasoning",
        "title": "Motivated Reasoning and Rationalization",
        "prerequisites": [
            ("map-and-territory", "hard"),
            ("cognitive-biases-critical-thinking", "soft"),
            ("dual-process-theory", "soft"),
        ],
        "builds_toward": ["the-bottom-line", "considering-the-opposite"],
        "tags": ["rationality", "biases", "self-deception", "epistemology"],
        "core_idea": (
            "Motivated reasoning occurs when desires, identity, or social pressures steer your "
            "reasoning toward a predetermined conclusion rather than toward truth. Rationalization "
            "is its output: a plausible-sounding argument constructed after the conclusion was "
            "already reached. The key diagnostic is directionality — genuine reasoning follows "
            "evidence to whatever conclusion it supports, while motivated reasoning starts from "
            "the desired conclusion and searches for supporting evidence. Motivated reasoning is "
            "not lying; the reasoner genuinely believes they are being objective, which makes it "
            "harder to detect than deliberate deception."
        ),
        "best_learned": (
            "Examine beliefs you hold that are also socially convenient or identity-reinforcing. "
            "Ask: would I still believe this if it were socially costly? Practice the \"double "
            "standard\" test — apply the same evidential standards you use for beliefs you like "
            "to beliefs you dislike. Notice when you feel relief at finding supporting evidence "
            "and discomfort at encountering contradicting evidence — those emotional reactions "
            "are signals that motivation may be steering your reasoning."
        ),
        "misconceptions": [
            "Motivated reasoning is not limited to unintelligent people — higher intelligence can make you better at constructing rationalizations, not worse.",
            "Being aware of motivated reasoning does not immunize you against it — you must use specific techniques (like considering the opposite) to counteract it.",
            "Not all emotional reasoning is motivated reasoning — emotions can carry legitimate information about values and priorities.",
        ],
    },
    {
        "id": "the-bottom-line",
        "title": "The Bottom Line",
        "prerequisites": [
            ("motivated-reasoning", "hard"),
        ],
        "builds_toward": ["considering-the-opposite", "steelmanning"],
        "tags": ["rationality", "biases", "argument-evaluation", "motivated-cognition"],
        "core_idea": (
            "Imagine a sheet of paper where the bottom line — the conclusion — is written first, "
            "and then arguments are filled in above it. No matter how compelling those arguments "
            "look, they carry no evidential weight because they were selected to support a "
            "predetermined conclusion. This thought experiment from the Sequences illustrates why "
            "the order of operations in reasoning matters: evidence must be evaluated before "
            "reaching a conclusion, not gathered in service of one. Once you have written the "
            "bottom line, any further \"reasoning\" is rationalization. The practical test: if no "
            "possible evidence could change your conclusion, you are not reasoning — you are "
            "performing reasoning."
        ),
        "best_learned": (
            "Before evaluating an argument, ask yourself: have I already decided what I think? "
            "Practice with political or social topics where you have strong priors. Try to specify "
            "in advance what evidence would change your mind — if you cannot, you may have already "
            "written the bottom line."
        ),
        "misconceptions": [
            "Having a prior belief is not the same as having written the bottom line — Bayesian reasoning starts with priors but genuinely updates on evidence.",
            "The bottom line is not about arguments being invalid — the same argument can carry evidential weight when encountered honestly and zero weight when cherry-picked.",
        ],
    },

    # === Applied Bayesian Reasoning ===
    {
        "id": "bayesian-thinking-in-practice",
        "title": "Bayesian Thinking in Practice",
        "prerequisites": [
            ("bayesian-epistemology", "hard"),
            ("bayes-theorem", "hard"),
            ("map-and-territory", "hard"),
        ],
        "builds_toward": [
            "conservation-of-expected-evidence", "absence-of-evidence",
            "extraordinary-claims-and-evidence-scaling", "likelihood-ratios-and-belief-updates",
        ],
        "tags": ["bayesian", "reasoning", "probability", "practice", "belief-updating"],
        "core_idea": (
            "Bayesian thinking in practice means treating beliefs as probabilities and "
            "systematically updating them when new evidence arrives. Unlike formal applications "
            "of Bayes' theorem with precise numbers, practical Bayesian reasoning often works "
            "with rough likelihood ratios: \"This evidence is about three times more likely if "
            "my hypothesis is true than if it is false, so I should update moderately toward it.\" "
            "The key habits are: assigning explicit probability estimates to beliefs, noticing "
            "when evidence arrives that should update those estimates, and actually updating "
            "rather than anchoring to your original position. Over time, calibrated Bayesian "
            "thinkers develop an intuitive sense for how strongly different types of evidence "
            "should move their beliefs."
        ),
        "best_learned": (
            "Start with low-stakes predictions: estimate the probability of everyday events "
            "(will the bus be late? will it rain?), record your estimates, and track your "
            "calibration over time. Practice translating verbal confidence (\"I'm pretty sure\") "
            "into numerical probabilities (\"about 80%\"). Work through classic Bayesian problems "
            "like medical diagnosis to build intuition for base rates and likelihood ratios."
        ),
        "misconceptions": [
            "Bayesian thinking does not require precise numerical calculations for every belief — rough directional updates are often sufficient and more realistic.",
            "Being Bayesian does not mean being wishy-washy — strong evidence warrants strong updates and confident beliefs.",
            "Bayesian reasoning is not just for scientific hypotheses — it applies to everyday decisions like which route to take or whether to trust a claim.",
        ],
    },
    {
        "id": "conservation-of-expected-evidence",
        "title": "Conservation of Expected Evidence",
        "prerequisites": [
            ("bayesian-thinking-in-practice", "hard"),
            ("conditionalization-and-bayesian-updating", "soft"),
            ("expected-value", "soft"),
        ],
        "builds_toward": ["absence-of-evidence", "calibration-training"],
        "tags": ["bayesian", "evidence", "probability", "rationality"],
        "core_idea": (
            "Before you observe evidence, your expected posterior probability must equal your "
            "prior probability — averaged over all possible observations, weighted by their "
            "likelihood. This means you cannot rationally expect to be convinced of something "
            "you do not already believe: if you expect the evidence to support hypothesis H, "
            "then you should already believe H more strongly. Conservation of expected evidence "
            "is a powerful diagnostic for motivated reasoning: if you expect to find evidence "
            "confirming your current belief no matter what happens, something has gone wrong "
            "with your reasoning. Genuine inquiry must admit the possibility that evidence will "
            "push you in either direction."
        ),
        "best_learned": (
            "Work through a concrete example: before flipping a coin you suspect is biased, "
            "write down how each possible sequence of outcomes would update your belief. Verify "
            "that the probability-weighted average of all possible posteriors equals your prior. "
            "Then apply this to real beliefs: before reading a study, ask what results would "
            "update you in each direction and by how much."
        ),
        "misconceptions": [
            "This does not mean evidence is useless — it means that before seeing evidence, you cannot predict which direction it will push you, though it will push you somewhere specific once observed.",
            "Conservation of expected evidence does not prevent you from seeking confirming evidence — it says your expectation of what you will find must be calibrated.",
        ],
    },
    {
        "id": "absence-of-evidence",
        "title": "Absence of Evidence Is Evidence of Absence",
        "prerequisites": [
            ("bayesian-thinking-in-practice", "hard"),
            ("conservation-of-expected-evidence", "soft"),
        ],
        "builds_toward": ["extraordinary-claims-and-evidence-scaling"],
        "tags": ["bayesian", "evidence", "probability", "reasoning"],
        "core_idea": (
            "The saying \"absence of evidence is not evidence of absence\" is probabilistically "
            "wrong. If a hypothesis predicts that we should observe certain evidence, and we look "
            "and do not find it, that observation is evidence against the hypothesis — exactly to "
            "the degree that the hypothesis predicted we would find it. If a drug works, we expect "
            "clinical trials to show positive results; if trials show nothing, that is evidence "
            "the drug does not work. The strength of the evidence depends on the likelihood ratio: "
            "how much more likely is the absence of evidence under \"hypothesis false\" versus "
            "\"hypothesis true\"? When the hypothesis strongly predicts observable consequences, "
            "failing to observe them is strong evidence against it."
        ),
        "best_learned": (
            "Work through the Bayesian math explicitly: if P(observe evidence | H true) = 0.9 "
            "and P(observe evidence | H false) = 0.1, then not observing the evidence gives a "
            "likelihood ratio of 0.1/0.9 ≈ 0.11, a strong update against H. Practice identifying "
            "real-world cases where absence of expected evidence should update beliefs: the dog "
            "that did not bark, the study that found no effect, the prediction that did not come true."
        ),
        "misconceptions": [
            "This does not mean any absence of evidence disproves a claim — the strength depends on how strongly the claim predicted observable consequences.",
            "The original saying has a grain of truth in informal contexts: sometimes we simply have not looked hard enough. But once we have looked and found nothing, that is informative.",
        ],
    },
    {
        "id": "extraordinary-claims-and-evidence-scaling",
        "title": "Extraordinary Claims Require Extraordinary Evidence",
        "prerequisites": [
            ("bayesian-thinking-in-practice", "hard"),
            ("absence-of-evidence", "soft"),
        ],
        "builds_toward": ["likelihood-ratios-and-belief-updates"],
        "tags": ["bayesian", "evidence", "prior-probability", "sagan-standard"],
        "core_idea": (
            "Carl Sagan's maxim is a direct consequence of Bayes' theorem. A claim with a very "
            "low prior probability requires evidence with a very high likelihood ratio to shift "
            "the posterior to a meaningful level. If your prior for a claim is 1 in a million, "
            "even evidence that is 100 times more likely under the hypothesis than under the "
            "alternative only brings the posterior to about 1 in 10,000 — still very unlikely. "
            "This is not a bias against unusual claims; it is a mathematical consequence of how "
            "evidence and priors interact. The practical lesson: calibrate the strength of evidence "
            "needed to the extremity of the claim, and be suspicious when extraordinary claims are "
            "supported only by ordinary evidence."
        ),
        "best_learned": (
            "Calculate concrete examples: if a friend claims to have seen a UFO (prior ~1 in "
            "100,000 for an actual alien craft), how strong would the evidence need to be to make "
            "you believe? Work out the likelihood ratios. Compare with mundane claims (\"it rained "
            "yesterday\") where even modest evidence suffices because the prior is already high."
        ),
        "misconceptions": [
            "This principle does not mean extraordinary claims should be dismissed without investigation — it means the bar for evidence is proportional to the claim's prior improbability.",
            "\"Extraordinary\" does not mean \"surprising to me personally\" — it means having a low prior probability given existing knowledge.",
        ],
    },
    {
        "id": "likelihood-ratios-and-belief-updates",
        "title": "Likelihood Ratios and Belief Updates",
        "prerequisites": [
            ("bayesian-thinking-in-practice", "hard"),
            ("bayes-theorem", "hard"),
            ("conditional-probability", "soft"),
        ],
        "builds_toward": ["calibration-training", "reference-class-forecasting"],
        "tags": ["bayesian", "likelihood-ratio", "belief-updating", "quantitative-reasoning"],
        "core_idea": (
            "The likelihood ratio is the engine of Bayesian updating: it measures how much more "
            "(or less) likely a piece of evidence is under one hypothesis compared to another. "
            "A likelihood ratio of 10 means the evidence is 10 times more likely if the hypothesis "
            "is true than if it is false — a strong update. A ratio near 1 means the evidence is "
            "equally expected either way — no update warranted. Thinking in likelihood ratios "
            "rather than raw probabilities makes Bayesian reasoning more intuitive: instead of "
            "juggling joint probabilities, you ask \"how much more expected is this evidence under "
            "my hypothesis?\" and shift your confidence proportionally. In log-odds form, updates "
            "become simple addition: log-odds posterior = log-odds prior + log likelihood ratio."
        ),
        "best_learned": (
            "Practice with the classic medical diagnosis example: a test with 99% sensitivity and "
            "5% false positive rate gives a likelihood ratio of 99/5 ≈ 20. For a disease with 1% "
            "base rate (prior odds 1:99), a positive test gives posterior odds of 20:99, or about "
            "17% — far from certainty despite a 99% accurate test. Work problems in both "
            "probability and log-odds form to build fluency with both representations."
        ),
        "misconceptions": [
            "A high likelihood ratio does not mean the hypothesis is probably true — it depends on the prior. A likelihood ratio of 100 applied to a prior of 1 in a million still yields a tiny posterior.",
            "Likelihood ratios are not the same as the probability of the hypothesis given the evidence — that is the posterior, which combines the ratio with the prior.",
        ],
    },

    # === Calibration & Forecasting ===
    {
        "id": "calibration-training",
        "title": "Calibration Training",
        "prerequisites": [
            ("bayesian-thinking-in-practice", "hard"),
            ("likelihood-ratios-and-belief-updates", "soft"),
            ("the-lens-that-sees-its-flaws", "hard"),
            ("overconfidence-metacognitive-illusions", "soft"),
        ],
        "builds_toward": ["reference-class-forecasting", "the-planning-fallacy", "intellectual-humility-and-calibrated-uncertainty"],
        "tags": ["calibration", "forecasting", "metacognition", "probability"],
        "core_idea": (
            "A calibrated reasoner's stated confidence matches their empirical accuracy: when they "
            "say they are 70% confident, they are right about 70% of the time. Most people are "
            "systematically overconfident — their 90% confidence predictions come true only 60-70% "
            "of the time. Calibration training closes this gap through deliberate practice: making "
            "explicit probability estimates, tracking accuracy, and adjusting. Research shows that "
            "calibration improves with feedback and practice — professional forecasters like those "
            "in the Good Judgment Project achieve near-perfect calibration. Calibration is not "
            "about being uncertain about everything; it is about having uncertainty that matches "
            "reality."
        ),
        "best_learned": (
            "Use calibration training apps or exercises: estimate probabilities for trivia questions, "
            "then check your accuracy at each confidence level. Plot a calibration curve (stated "
            "confidence vs. actual accuracy). Identify your typical bias (overconfidence or "
            "underconfidence) and consciously adjust. Practice regularly — calibration is a skill "
            "that improves with repetition, like any other."
        ),
        "misconceptions": [
            "Calibration is not the same as accuracy — a calibrated person may be uncertain about many things, but their uncertainty is well-matched to their knowledge.",
            "Perfect calibration does not mean predicting 50% for everything — it means using the full range of probabilities and being right at the rate you predict.",
            "Calibration training is not about math — it is about developing an honest internal sense of how much you actually know.",
        ],
    },
    {
        "id": "reference-class-forecasting",
        "title": "Reference Class Forecasting",
        "prerequisites": [
            ("calibration-training", "hard"),
            ("base-rate-neglect", "soft"),
        ],
        "builds_toward": ["the-planning-fallacy", "fermi-estimation"],
        "tags": ["forecasting", "base-rates", "planning", "statistics"],
        "core_idea": (
            "Reference class forecasting predicts the outcome of a specific case by looking at "
            "the base rate of similar cases — the \"reference class.\" Instead of asking \"how "
            "long will MY software project take?\" (subject to optimism bias), ask \"how long "
            "do software projects of this type and size typically take?\" The outside view, as "
            "Kahneman calls it, anchors your estimate to empirical reality before you adjust for "
            "case-specific factors. Bent Flyvbjerg's research on infrastructure projects showed "
            "that reference class forecasting dramatically reduces cost overruns. The technique "
            "is simple: identify the reference class, find the distribution of outcomes, and use "
            "that as your starting point."
        ),
        "best_learned": (
            "Apply reference class forecasting to a personal project: before estimating how long "
            "it will take, look up how long similar projects took for other people. Notice the gap "
            "between your inside-view estimate and the base rate. Practice identifying the right "
            "reference class — too broad loses specificity, too narrow loses statistical power."
        ),
        "misconceptions": [
            "Reference class forecasting does not mean ignoring case-specific information — it means starting with the base rate and adjusting, rather than starting with your inside-view estimate.",
            "The technique is not limited to large projects — it applies to everyday estimates like commute times, cooking duration, or how long errands take.",
        ],
    },
    {
        "id": "fermi-estimation",
        "title": "Fermi Estimation",
        "prerequisites": [
            ("reference-class-forecasting", "soft"),
            ("reasoning-under-uncertainty", "soft"),
        ],
        "builds_toward": ["expected-value-decision-making"],
        "tags": ["estimation", "quantitative-reasoning", "decomposition", "problem-solving"],
        "core_idea": (
            "Fermi estimation is the practice of making rough but useful quantitative estimates "
            "by decomposing an unknown quantity into factors you can estimate individually. \"How "
            "many piano tuners are in Chicago?\" becomes: population of Chicago × fraction of "
            "households with pianos × tunings per year × hours per tuning ÷ working hours per "
            "tuner per year. Each factor may be off by a factor of 2, but errors tend to cancel "
            "partially, and the final estimate is typically within an order of magnitude of the "
            "true value. Fermi estimation builds quantitative intuition and reveals which factors "
            "matter most — often the answer depends heavily on one or two quantities, identifying "
            "where to focus further research."
        ),
        "best_learned": (
            "Practice regularly with questions where you can verify the answer afterward. Start "
            "simple (\"how many gas stations in the US?\") and progress to harder estimates. "
            "Always decompose into at least three factors. After checking the answer, identify "
            "which factor was most off and recalibrate your priors for that type of quantity."
        ),
        "misconceptions": [
            "Fermi estimates are not wild guesses — the decomposition into estimable factors provides surprising accuracy through error cancellation.",
            "Precision is not the goal — being within an order of magnitude is usually sufficient for the decisions Fermi estimation informs.",
            "Fermi estimation is not just a party trick — it is a foundational tool for expected value reasoning and prioritization under uncertainty.",
        ],
    },
    {
        "id": "the-planning-fallacy",
        "title": "The Planning Fallacy",
        "prerequisites": [
            ("calibration-training", "hard"),
            ("reference-class-forecasting", "hard"),
            ("overconfidence-metacognitive-illusions", "soft"),
        ],
        "builds_toward": ["premortem-analysis", "murphyjitsu"],
        "tags": ["planning", "bias", "overconfidence", "forecasting", "project-management"],
        "core_idea": (
            "The planning fallacy is the systematic tendency to underestimate the time, cost, and "
            "risk of future actions while overestimating their benefits. It persists even when "
            "people have extensive experience with similar tasks going over budget and over time. "
            "Kahneman and Tversky identified the root cause as the \"inside view\" — focusing on "
            "the specific details of the plan rather than the base rate of similar plans. The "
            "corrective is reference class forecasting: use the outside view first, then adjust "
            "for genuinely unique factors. Buehler's research shows that people who are asked "
            "\"how long did similar tasks take you in the past?\" make dramatically better "
            "estimates than those asked \"how long will this task take you?\""
        ),
        "best_learned": (
            "Track your time estimates against reality for two weeks. Calculate your typical "
            "\"planning ratio\" (actual time / estimated time). Use that ratio as a correction "
            "factor for future estimates. Practice making both best-case, typical-case, and "
            "worst-case estimates — most people find their \"typical\" estimate resembles their "
            "true best case."
        ),
        "misconceptions": [
            "The planning fallacy is not laziness or stupidity — it affects experts and experienced planners as much as novices.",
            "Adding a buffer to your estimate is not sufficient if the buffer is also estimated using the inside view — you must anchor to actual base rates.",
            "The fallacy applies to time, money, effort, and complexity — not just time estimates.",
        ],
    },
    {
        "id": "prediction-markets",
        "title": "Prediction Markets and Information Aggregation",
        "prerequisites": [
            ("calibration-training", "hard"),
            ("expected-value", "soft"),
        ],
        "builds_toward": ["disagreement-and-rational-updating"],
        "tags": ["prediction", "markets", "collective-intelligence", "forecasting", "information"],
        "core_idea": (
            "Prediction markets allow participants to buy and sell contracts that pay out based "
            "on the outcome of future events, with prices reflecting the market's collective "
            "probability estimate. They aggregate dispersed information more efficiently than "
            "polls, expert panels, or individual forecasters because participants have financial "
            "incentives to correct mispricings — anyone who knows the market is wrong can profit "
            "by betting against it. Research by Arrow, Hanson, and others shows prediction markets "
            "are well-calibrated and outperform traditional forecasting methods in many domains. "
            "They also reveal how much genuine uncertainty exists: a market price of 60% means "
            "the collective intelligence of all participants rates the event at 60%, with no "
            "individual's overconfidence dominating."
        ),
        "best_learned": (
            "Follow a prediction market (Polymarket, Metaculus, or similar) and compare its "
            "probabilities to your own estimates. Track which source is more calibrated over time. "
            "Understand the mechanism: if you think a market is at 30% but you believe the true "
            "probability is 60%, you would buy — and in doing so, you push the price closer to "
            "the truth."
        ),
        "misconceptions": [
            "Prediction markets are not gambling — they are information aggregation tools with measurable calibration properties.",
            "Market prices are not always right — they are the best available estimate given current information, which can still be wrong.",
            "Thin markets (few participants) can be poorly calibrated — the aggregation benefit requires sufficient participation.",
        ],
    },

    # === Cognitive Debiasing ===
    {
        "id": "debiasing-techniques",
        "title": "Debiasing Techniques",
        "prerequisites": [
            ("the-lens-that-sees-its-flaws", "hard"),
            ("cognitive-biases-critical-thinking", "hard"),
            ("cognitive-biases-overview", "soft"),
            ("dual-process-theory", "soft"),
        ],
        "builds_toward": ["premortem-analysis", "considering-the-opposite", "scope-sensitivity", "murphyjitsu"],
        "tags": ["debiasing", "rationality", "cognitive-biases", "techniques", "practice"],
        "core_idea": (
            "Debiasing techniques are deliberate cognitive strategies that counteract specific "
            "biases. Unlike bias awareness alone (which research shows has limited effect), "
            "effective debiasing provides concrete procedures: considering the opposite to counter "
            "confirmation bias, using reference classes to counter the planning fallacy, "
            "decomposing problems to counter scope insensitivity. The general framework has three "
            "steps: (1) recognize the situation where a bias typically operates, (2) apply the "
            "specific countermeasure, (3) verify the result against an external check. CFAR "
            "(Center for Applied Rationality) systematized many of these techniques into "
            "teachable, practicable skills, demonstrating that debiasing transfers to novel "
            "situations when practiced deliberately."
        ),
        "best_learned": (
            "Learn one debiasing technique at a time and practice it for a week before adding "
            "another. Start with considering the opposite (easiest to apply) and premortem "
            "analysis (most immediately useful). Keep a log of situations where you applied "
            "a technique and whether it changed your conclusion — this builds the habit loop."
        ),
        "misconceptions": [
            "Knowing about biases is not the same as being debiased — specific techniques and deliberate practice are required.",
            "Debiasing does not make you perfectly rational — it reduces systematic errors in specific, practiced contexts.",
            "You cannot debias all your thinking simultaneously — focus on the biases most relevant to your current decisions.",
        ],
    },
    {
        "id": "premortem-analysis",
        "title": "Premortem Analysis",
        "prerequisites": [
            ("debiasing-techniques", "hard"),
            ("the-planning-fallacy", "soft"),
        ],
        "builds_toward": ["murphyjitsu"],
        "tags": ["debiasing", "planning", "risk", "technique"],
        "core_idea": (
            "A premortem asks: \"Imagine this project has failed. Why did it fail?\" By assuming "
            "failure has already occurred, the technique bypasses optimism bias and social pressure "
            "to be supportive, giving team members permission to voice concerns. Gary Klein, who "
            "developed the technique, found that premortems increase the ability to identify "
            "reasons for potential failure by 30%. The mechanism works because imagining a concrete "
            "failure is cognitively easier than imagining abstract risks — it leverages narrative "
            "thinking (System 1) to identify problems that analytical risk assessment (System 2) "
            "misses. Premortems are most valuable at the start of a project, when there is still "
            "time to adjust the plan."
        ),
        "best_learned": (
            "Run a premortem on your next significant decision or project. Write \"It is [future "
            "date] and this has failed\" at the top of a page, then list every plausible reason "
            "for failure you can think of in 5 minutes. Compare the list to a standard risk "
            "assessment — the premortem typically surfaces risks the standard approach misses."
        ),
        "misconceptions": [
            "A premortem is not pessimism — it is a structured technique for surfacing risks that optimism bias would otherwise hide.",
            "The premortem does not replace risk analysis — it complements it by accessing a different cognitive mode.",
        ],
    },
    {
        "id": "considering-the-opposite",
        "title": "Considering the Opposite",
        "prerequisites": [
            ("debiasing-techniques", "hard"),
            ("motivated-reasoning", "hard"),
            ("confirmation-bias", "soft"),
        ],
        "builds_toward": ["steelmanning", "intellectual-humility-and-calibrated-uncertainty"],
        "tags": ["debiasing", "confirmation-bias", "technique", "critical-thinking"],
        "core_idea": (
            "Considering the opposite is the most robust single debiasing technique in the "
            "experimental literature. When you catch yourself leaning toward a conclusion, "
            "deliberately generate reasons why the opposite conclusion might be true. Lord, "
            "Lepper, and Preston (1984) showed that this technique significantly reduces "
            "confirmation bias and belief perseverance. It works because confirmation bias "
            "is partly a search problem — we naturally search for confirming evidence and stop, "
            "but considering the opposite forces a search for disconfirming evidence. The "
            "technique is most powerful when applied before commitment to a position, and when "
            "the opposite-case arguments are taken seriously rather than treated as a formality."
        ),
        "best_learned": (
            "Practice with a belief you hold with moderate confidence. Write three strong "
            "arguments for it, then force yourself to write three strong arguments against it. "
            "Notice whether the exercise changes your confidence — if it does, you were "
            "underweighting available counterevidence."
        ),
        "misconceptions": [
            "Considering the opposite is not the same as playing devil's advocate casually — it requires genuinely engaging with the strongest counterarguments.",
            "This technique does not mean all positions are equally valid — it means you should check whether your position survives serious scrutiny before committing.",
        ],
    },
    {
        "id": "scope-sensitivity",
        "title": "Scope Sensitivity",
        "prerequisites": [
            ("debiasing-techniques", "hard"),
            ("expected-value", "soft"),
        ],
        "builds_toward": ["expected-value-decision-making", "effective-altruism-and-scope"],
        "tags": ["debiasing", "scope", "scale", "quantitative-reasoning", "altruism"],
        "core_idea": (
            "Scope insensitivity is the tendency to respond with similar emotional intensity to "
            "problems of vastly different scale. In a famous study, people were willing to pay "
            "roughly the same amount to save 2,000 birds, 20,000 birds, or 200,000 birds from "
            "oil spills. The emotional response is driven by the prototype (one oil-soaked bird) "
            "rather than by the quantity. Scope sensitivity training means learning to multiply — "
            "to consciously scale your concern, effort, and resources in proportion to the actual "
            "magnitude of the problem. This is foundational to effective altruism and rational "
            "prioritization: if intervention A saves 10 lives and intervention B saves 10,000, "
            "the second is 1,000 times more valuable, even if both evoke similar emotional concern."
        ),
        "best_learned": (
            "When evaluating a problem, explicitly estimate its scale before forming an emotional "
            "response. Practice with charitable giving: compare the cost-effectiveness of different "
            "interventions using metrics like QALYs or lives saved per dollar. Notice when your "
            "emotional reaction does not match the quantitative scale."
        ),
        "misconceptions": [
            "Scope sensitivity is not about suppressing emotions — it is about ensuring that the scale of your response matches the scale of the problem.",
            "Being scope-sensitive does not mean only caring about the largest problems — it means being proportionate in your concern across problems of different sizes.",
        ],
    },
    {
        "id": "murphyjitsu",
        "title": "Murphyjitsu",
        "prerequisites": [
            ("premortem-analysis", "hard"),
            ("the-planning-fallacy", "soft"),
        ],
        "builds_toward": [],
        "tags": ["CFAR", "planning", "technique", "robustness", "mental-simulation"],
        "core_idea": (
            "Murphyjitsu (from CFAR) is a mental simulation technique for stress-testing plans. "
            "For each step of your plan, ask: \"Does this feel like the sort of plan that will "
            "work, or the sort of plan that will fail?\" If your gut says it feels like it will "
            "fail, identify the most likely failure mode, modify the plan to address it, and "
            "repeat until the plan passes the gut check. The technique combines the premortem's "
            "failure-imagination with iterative plan repair. It leverages System 1's pattern-"
            "matching ability — your intuition often detects problems that your explicit reasoning "
            "has not surfaced. The name is a portmanteau of Murphy's Law and jujitsu: using the "
            "force of Murphy's Law (\"what can go wrong will go wrong\") to strengthen your plan "
            "rather than being defeated by it."
        ),
        "best_learned": (
            "Before your next important meeting, trip, or project deadline, walk through your plan "
            "step by step. At each step, ask \"does this feel like it will work?\" If not, "
            "identify the failure mode and fix it. Repeat until each step passes. Compare the "
            "revised plan to your original — the differences reveal your blind spots."
        ),
        "misconceptions": [
            "Murphyjitsu is not about being paranoid — it is about systematically finding and fixing plan weaknesses before they manifest.",
            "The technique does not require that you fix every possible failure mode — only the ones your gut flags as realistic.",
        ],
    },

    # === Decision Theory Applied ===
    {
        "id": "expected-value-decision-making",
        "title": "Expected Value Decision-Making",
        "prerequisites": [
            ("expected-value", "hard"),
            ("bayesian-thinking-in-practice", "hard"),
            ("scope-sensitivity", "soft"),
            ("fermi-estimation", "soft"),
        ],
        "builds_toward": ["newcombs-problem", "tail-risk-and-black-swans", "sunk-cost-recognition"],
        "tags": ["decision-theory", "expected-value", "risk", "quantitative-reasoning"],
        "core_idea": (
            "Expected value decision-making evaluates choices by computing the probability-weighted "
            "average of their possible outcomes. A bet that pays $100 with 20% probability and "
            "loses $10 with 80% probability has an expected value of $100×0.2 - $10×0.8 = +$12 — "
            "a good bet despite losing most of the time. Applied broadly, this framework extends "
            "beyond money to any outcome you value: expected QALYs, expected career impact, "
            "expected knowledge gained. The key insight for practical decision-making is that many "
            "high-expected-value opportunities look bad on any single trial because the payoff is "
            "rare — but systematically taking positive-expected-value bets leads to better outcomes "
            "over time. The practical limitations include: difficulty estimating probabilities, "
            "risk aversion when stakes are large relative to your resources, and situations where "
            "variance matters as much as expected value."
        ),
        "best_learned": (
            "Practice on low-stakes decisions first: should you try a new restaurant (high "
            "variance, moderate expected value) or return to a known favorite (low variance, "
            "known value)? Explicitly estimate the probabilities and outcomes. Then apply to "
            "bigger decisions: career moves, project bets, time allocation."
        ),
        "misconceptions": [
            "Expected value reasoning does not mean ignoring risk — when stakes are large relative to your resources, variance matters and Kelly criterion or similar frameworks apply.",
            "A positive expected value does not guarantee a good outcome — it means that if you systematically take positive-EV bets, you will come out ahead over many decisions.",
            "Not all values can be easily quantified — expected value reasoning is a framework, not a formula that replaces judgment.",
        ],
    },
    {
        "id": "newcombs-problem",
        "title": "Newcomb's Problem",
        "prerequisites": [
            ("expected-value-decision-making", "hard"),
            ("rational-choice-and-ethics", "soft"),
        ],
        "builds_toward": ["causal-vs-evidential-decision-theory"],
        "tags": ["decision-theory", "thought-experiment", "newcomb", "rationality"],
        "core_idea": (
            "Newcomb's problem presents a choice: take both boxes (getting $1,000 plus whatever "
            "a nearly perfect predictor placed in the opaque box) or take only the opaque box "
            "(getting $1,000,000 if the predictor predicted you would one-box, $0 if it predicted "
            "you would two-box). The predictor has been right 99% of the time with previous "
            "players. One-boxing gets you $1,000,000 almost certainly; two-boxing gets you $1,000 "
            "almost certainly (the predictor foresaw your greed and left the box empty). This "
            "simple setup reveals a deep split in decision theory: causal decision theory says to "
            "two-box (your choice cannot causally change what is already in the box), while "
            "evidential decision theory says to one-box (one-boxing is strong evidence that the "
            "box contains $1,000,000). The problem has no consensus solution and illuminates "
            "fundamental questions about the relationship between choice, causation, and rationality."
        ),
        "best_learned": (
            "First understand both arguments fully — the two-boxing argument from causal reasoning "
            "and the one-boxing argument from expected payoffs. Then examine variants: what if the "
            "predictor is only 51% accurate? What if you can randomize? Each variant tests the "
            "boundaries of different decision theories. The value is not in solving the problem "
            "but in understanding what makes it hard."
        ),
        "misconceptions": [
            "There is no universally accepted 'right answer' — Newcomb's problem is a diagnostic for competing theories of rational choice, not a puzzle with a hidden solution.",
            "The problem is not about free will or determinism — it arises even if you believe in libertarian free will, because the predictor is empirically accurate.",
        ],
    },
    {
        "id": "causal-vs-evidential-decision-theory",
        "title": "Causal vs. Evidential Decision Theory",
        "prerequisites": [
            ("newcombs-problem", "hard"),
            ("expected-value-decision-making", "hard"),
        ],
        "builds_toward": [],
        "tags": ["decision-theory", "causation", "evidence", "rationality", "philosophy"],
        "core_idea": (
            "Causal decision theory (CDT) says to choose the action that causes the best expected "
            "outcome — evaluating each action by its causal consequences. Evidential decision theory "
            "(EDT) says to choose the action such that, conditional on performing it, you expect "
            "the best outcome — evaluating each action by what it tells you about the world. In "
            "most real-world cases they agree, but in Newcomb-like problems they diverge. CDT "
            "two-boxes because taking both boxes cannot cause the opaque box to be empty. EDT "
            "one-boxes because one-boxing is evidence that the box is full. The Rationalist "
            "community has explored extensions including functional decision theory (FDT), which "
            "evaluates actions by the consequences of the abstract computation that produces them. "
            "The debate reveals that the seemingly simple concept of \"acting rationally\" requires "
            "specifying what counts as a consequence of your action."
        ),
        "best_learned": (
            "Work through Newcomb's problem under both frameworks and verify that they give "
            "different recommendations. Then try the Smoking Lesion problem (EDT says don't smoke "
            "because smoking is evidence of the lesion, CDT says the lesion is the cause, not "
            "the smoking) to see where EDT fails. Consider what framework you implicitly use in "
            "everyday decisions."
        ),
        "misconceptions": [
            "CDT and EDT are not competing 'religions' — they are formal frameworks that make precise, testable predictions about which choices are rational.",
            "CDT does not always recommend selfish behavior — it recommends the action with the best causal consequences, which can include cooperation and altruism.",
        ],
    },
    {
        "id": "sunk-cost-recognition",
        "title": "Sunk Cost Recognition and Rational Quitting",
        "prerequisites": [
            ("expected-value-decision-making", "hard"),
            ("motivated-reasoning", "soft"),
        ],
        "builds_toward": [],
        "tags": ["decision-theory", "sunk-cost", "quitting", "rationality"],
        "core_idea": (
            "The sunk cost fallacy is the tendency to continue investing in a losing proposition "
            "because of what has already been spent rather than what is expected going forward. "
            "Rational decision-making considers only future costs and benefits — past expenditures "
            "are gone regardless of your next action. But recognizing sunk costs is harder than it "
            "sounds: identity attachment (\"I've spent 5 years on this degree\"), social pressure "
            "(\"we've committed to this strategy\"), and loss aversion (abandoning feels like "
            "admitting failure) all push toward irrational continuation. Rational quitting is a "
            "skill: explicitly separating past investment from expected future value, setting "
            "pre-commitment criteria for when to quit, and reframing quitting as redirecting "
            "resources toward higher-expected-value opportunities."
        ),
        "best_learned": (
            "For an ongoing project or commitment you are unsure about, perform the \"fresh start\" "
            "test: if you were not already involved, would you start this project today given what "
            "you now know? If no, the only reason to continue is sunk cost bias. Practice setting "
            "kill criteria in advance: \"I will quit if X does not happen by Y date.\""
        ),
        "misconceptions": [
            "Recognizing sunk costs does not mean quitting everything that is hard — difficulty is a feature of valuable projects. The test is expected future value, not current discomfort.",
            "Sunk costs can carry real information — the fact that you invested heavily may indicate genuine value. The fallacy is continuing solely because of the investment, not considering the investment as one input among many.",
        ],
    },
    {
        "id": "tail-risk-and-black-swans",
        "title": "Tail Risk and Black Swans",
        "prerequisites": [
            ("expected-value-decision-making", "hard"),
            ("calibration-training", "soft"),
        ],
        "builds_toward": ["effective-altruism-and-scope"],
        "tags": ["risk", "probability", "black-swans", "nassim-taleb", "fat-tails"],
        "core_idea": (
            "Tail risks are low-probability events with extreme consequences — the far ends of "
            "a probability distribution. Nassim Taleb's \"black swans\" are tail events that are "
            "also unpredictable and retrospectively rationalized. Standard expected value reasoning "
            "can underweight tail risks when probability distributions have \"fat tails\" — meaning "
            "extreme events are more common than a normal distribution would predict. Financial "
            "markets, pandemics, and technological breakthroughs all exhibit fat-tailed behavior. "
            "The practical implication for rational decision-making: be cautious about strategies "
            "that perform well on average but catastrophically in tail scenarios, and consider "
            "strategies that are robust or even benefit from tail events (Taleb's \"antifragility\"). "
            "When potential losses are catastrophic and irreversible, expected value reasoning must "
            "be supplemented with worst-case analysis."
        ),
        "best_learned": (
            "Study historical tail events (2008 financial crisis, COVID-19) and trace how "
            "decision-makers underweighted their probability. Examine your own portfolio of risks: "
            "where are you exposed to catastrophic downside? Where are you missing asymmetric "
            "upside? Practice distinguishing between risks with bounded downside (a bad dinner) "
            "and risks with unbounded downside (a leveraged investment)."
        ),
        "misconceptions": [
            "Tail risk awareness is not about predicting specific black swans — it is about building robustness against the category of extreme events.",
            "Fat tails do not invalidate expected value reasoning entirely — they require more careful estimation and explicit consideration of worst-case scenarios.",
            "Being risk-averse about tail events does not mean being risk-averse about everything — many decisions have bounded downside and should be approached with expected value reasoning.",
        ],
    },

    # === Epistemic Practices ===
    {
        "id": "steelmanning",
        "title": "Steelmanning",
        "prerequisites": [
            ("considering-the-opposite", "hard"),
            ("the-bottom-line", "soft"),
        ],
        "builds_toward": ["disagreement-and-rational-updating", "intellectual-humility-and-calibrated-uncertainty"],
        "tags": ["argumentation", "charity", "rationality", "epistemics"],
        "core_idea": (
            "Steelmanning is the practice of engaging with the strongest possible version of an "
            "opposing argument — the opposite of strawmanning. Instead of attacking the weakest "
            "formulation of a position (which proves nothing), you reconstruct the argument in "
            "its most compelling form and then evaluate that. Steelmanning serves both epistemics "
            "and discourse: epistemically, it protects against confirmation bias by forcing genuine "
            "engagement with counterevidence. Discursively, it builds trust and surfaces real "
            "disagreements rather than misunderstandings. The practice requires understanding the "
            "opposing position well enough to argue for it convincingly — which often reveals "
            "considerations you had overlooked."
        ),
        "best_learned": (
            "Choose a position you disagree with and write the best argument FOR it that you can. "
            "Show it to someone who holds that position and ask if you represented them fairly. "
            "If they say no, revise until they agree. Notice what you learn in the process — "
            "steelmanning almost always reveals something you had not considered."
        ),
        "misconceptions": [
            "Steelmanning does not mean agreeing with the opposing position — it means understanding and engaging with its strongest form before deciding whether to disagree.",
            "A steelman should be a position someone actually holds or would endorse, not a hypothetical that nobody believes — otherwise it becomes a different kind of distortion.",
        ],
    },
    {
        "id": "intellectual-humility-and-calibrated-uncertainty",
        "title": "Intellectual Humility and Calibrated Uncertainty",
        "prerequisites": [
            ("calibration-training", "hard"),
            ("considering-the-opposite", "soft"),
        ],
        "builds_toward": ["disagreement-and-rational-updating"],
        "tags": ["epistemics", "humility", "uncertainty", "calibration", "virtue"],
        "core_idea": (
            "Intellectual humility is not chronic uncertainty or self-deprecation — it is having "
            "confidence calibrated to evidence. A calibrated reasoner is very confident about "
            "well-established facts (evolution, heliocentrism) and appropriately uncertain about "
            "contested or complex questions (specific policy outcomes, novel scientific claims). "
            "The virtue is in matching confidence to evidence, not in maximizing or minimizing "
            "confidence. Calibrated uncertainty requires tracking the distinction between \"I "
            "believe X\" and \"I have strong evidence for X\" — beliefs can feel certain while "
            "being poorly supported. The Rationalist tradition emphasizes that intellectual humility "
            "is a practice, not a personality trait: it is maintained through calibration training, "
            "exposure to diverse perspectives, and willingness to update."
        ),
        "best_learned": (
            "Review your strongest beliefs and ask: what evidence would change my mind? If you "
            "cannot specify any evidence, your confidence may not be calibrated to reality. "
            "Practice distinguishing between \"I am confident because the evidence is strong\" "
            "and \"I am confident because I have always believed this.\""
        ),
        "misconceptions": [
            "Intellectual humility does not mean treating all opinions as equally valid — some claims have far more evidence behind them than others.",
            "Saying 'I don't know' is not a failure of rationality — it is often the most accurate and honest statement available.",
        ],
    },
    {
        "id": "disagreement-and-rational-updating",
        "title": "Disagreement and Rational Updating",
        "prerequisites": [
            ("steelmanning", "hard"),
            ("intellectual-humility-and-calibrated-uncertainty", "hard"),
            ("epistemology-of-disagreement", "soft"),
        ],
        "builds_toward": [],
        "tags": ["epistemics", "disagreement", "aumann", "updating", "social-epistemology"],
        "core_idea": (
            "Aumann's agreement theorem proves that two rational agents with common knowledge of "
            "each other's beliefs cannot agree to disagree — if they share the same priors and "
            "each knows the other's posterior, they must converge. In practice, persistent "
            "disagreement signals that at least one party has different priors, different evidence, "
            "or is reasoning incorrectly. The Rationalist approach to disagreement: take the "
            "other person's belief as evidence (their brain processed information you have not "
            "seen), update toward them proportional to your assessment of their reliability, and "
            "investigate the crux — the specific factual or inferential disagreement that drives "
            "the difference. Productive disagreement requires identifying cruxes rather than "
            "repeating arguments."
        ),
        "best_learned": (
            "In your next substantive disagreement, try to identify the crux: what is the "
            "specific factual claim or inference where you and the other person diverge? State "
            "it explicitly and check whether resolving that point would change both your minds. "
            "Practice taking the other person's confidence as evidence — if a domain expert "
            "disagrees with you, how much should you update?"
        ),
        "misconceptions": [
            "Aumann's theorem does not mean you should always split the difference with anyone who disagrees — it applies to rational agents with common priors and common knowledge, which is rarely fully satisfied.",
            "Rational updating on disagreement does not mean deferring to the loudest or most confident person — it means weighting by assessed reliability and relevant expertise.",
        ],
    },
    {
        "id": "information-value-and-exploration",
        "title": "Value of Information and Exploration-Exploitation",
        "prerequisites": [
            ("expected-value-decision-making", "hard"),
            ("bayesian-thinking-in-practice", "soft"),
        ],
        "builds_toward": [],
        "tags": ["decision-theory", "information", "exploration", "exploitation", "VoI"],
        "core_idea": (
            "The value of information (VoI) is how much better you expect your decision to be if "
            "you acquire additional information before acting. If learning the answer to a question "
            "would not change your decision, that information has zero value regardless of how "
            "interesting it is. VoI analysis prevents both over-researching (gathering information "
            "that will not affect your choice) and under-researching (acting on insufficient "
            "information when cheap investigation is available). The exploration-exploitation "
            "tradeoff generalizes this: exploring (trying new options, gathering data) has "
            "information value but opportunity cost, while exploiting (acting on current best "
            "knowledge) captures immediate value but may miss better options. Optimal strategies "
            "explore more when uncertainty is high and time horizons are long, and exploit more "
            "as certainty increases or deadlines approach."
        ),
        "best_learned": (
            "Before researching a decision, ask: what would I do if I could not get any more "
            "information? If the answer is clear, further research has low VoI. Apply the "
            "explore-exploit framework to everyday choices: restaurants (try new ones when you "
            "have many meals ahead, go to favorites when you want a reliable experience), career "
            "moves (explore early, exploit later)."
        ),
        "misconceptions": [
            "Value of information is not the same as interestingness — fascinating information that does not change any decision has zero practical VoI.",
            "The exploration-exploitation tradeoff does not have a universal solution — the optimal balance depends on time horizon, stakes, and current uncertainty.",
        ],
    },
    {
        "id": "effective-altruism-and-scope",
        "title": "Effective Altruism and Scope",
        "prerequisites": [
            ("scope-sensitivity", "hard"),
            ("expected-value-decision-making", "hard"),
            ("tail-risk-and-black-swans", "soft"),
        ],
        "builds_toward": [],
        "tags": ["effective-altruism", "scope", "rationality", "ethics", "impact"],
        "core_idea": (
            "Effective altruism applies Rationalist principles — scope sensitivity, expected value "
            "reasoning, calibrated uncertainty — to the question of how to do the most good. The "
            "core insight: if you are going to invest time or money in helping others, the same "
            "principles that make you a better forecaster make you a better philanthropist. "
            "Interventions vary by orders of magnitude in cost-effectiveness — distributing bed "
            "nets to prevent malaria saves a life for roughly $5,000, while some popular charitable "
            "causes cost millions per life saved. Scope sensitivity demands taking these "
            "differences seriously rather than giving based on emotional resonance alone. "
            "Effective altruism also applies expected value reasoning to cause selection: "
            "prioritizing by scale (how big is the problem?), neglectedness (how much is already "
            "being done?), and tractability (can additional resources make progress?)."
        ),
        "best_learned": (
            "Compare the cost-effectiveness of charitable interventions using GiveWell's research. "
            "Estimate the expected impact per dollar for two causes you care about. Practice "
            "separating emotional resonance from quantitative impact — which interventions feel "
            "most compelling to you, and which actually produce the most good per dollar? Notice "
            "the gap."
        ),
        "misconceptions": [
            "Effective altruism is not utilitarian by definition — it is a framework for improving the effectiveness of whatever moral values you hold.",
            "EA does not mean only donating to the single most effective charity — it means being informed and deliberate about impact, which allows for diverse cause prioritization.",
            "Quantifying impact does not mean ignoring things that are hard to measure — it means being honest about uncertainty while still making comparisons.",
        ],
    },
]


def format_prereqs(prereqs):
    """Format prerequisites as YAML list."""
    if not prereqs:
        return "prerequisites: []"
    lines = ["prerequisites:"]
    for pid, ptype in prereqs:
        lines.append(f"  - id: {pid}")
        lines.append(f"    type: {ptype}")
    return "\n".join(lines)


def format_builds_toward(builds):
    """Format builds-toward as YAML list."""
    if not builds:
        return ""
    lines = ["builds-toward:"]
    for b in builds:
        lines.append(f"  - {b}")
    return "\n".join(lines)


def format_tags(tags):
    """Format tags as YAML list."""
    if not tags:
        return "tags: []"
    items = ", ".join(f'"{t}"' for t in tags)
    return f"tags: [{items}]"


def format_misconceptions(misconceptions):
    """Format misconceptions as markdown bullets."""
    return "\n".join(f"- {m}" for m in misconceptions)


def generate_topic_file(topic):
    """Generate the markdown content for a topic file."""
    bt = format_builds_toward(topic["builds_toward"])
    bt_section = f"\n{bt}" if bt else ""

    content = f"""---
id: {topic["id"]}
title: "{topic["title"]}"
domain: {DOMAIN}
course: {COURSE}
{format_prereqs(topic["prerequisites"])}{bt_section}
{format_tags(topic["tags"])}
stage: {STAGE}
status: {STATUS}
---

## Core Idea

{topic["core_idea"]}

## How It's Best Learned

{topic["best_learned"]}

## Common Misconceptions

{format_misconceptions(topic["misconceptions"])}
"""
    return content


def main():
    COURSE_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Generating {len(TOPICS)} Applied Rationality topics...")

    for topic in TOPICS:
        filepath = COURSE_DIR / f"{topic['id']}.md"
        content = generate_topic_file(topic)
        filepath.write_text(content, encoding="utf-8")
        print(f"  {topic['id']}")

    print(f"\nCreated {len(TOPICS)} topic files in {COURSE_DIR.relative_to(ROOT)}")
    print(f"\nRemember to:")
    print(f"  1. Update domains/philosophy/_domain.yml to add the applied-rationality course")
    print(f"  2. Run python tools/validate.py to check for issues")
    print(f"  3. Run python tools/stats.py to verify counts")


if __name__ == "__main__":
    main()
