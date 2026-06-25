# Phishing Awareness Training

This project contains **two self-contained implementations** of an interactive
Phishing Awareness Training module. Both teach the same core skills —
recognizing phishing emails, spotting fake websites, understanding social
engineering tactics, and following best practices — but in different formats
for different use cases.

| File | Type | Run with |
|---|---|---|
| `phishing_awareness_training.py` | Command-line (terminal) training tool | `python3 phishing_awareness_training.py` |
| `Phishing-Awareness-Training_.html` | Browser-based interactive web app | Open the file directly in any browser |

---

## 1. `phishing_awareness_training.py` — CLI Version

### Requirements
- Python 3.6 or newer
- **No external libraries** — uses only the standard library (`sys`, `time`,
  `textwrap`)
- Runs on Windows, macOS, and Linux

### How to run
```bash
python3 phishing_awareness_training.py
```

### What it covers
A menu-driven terminal program with **6 modules**, each followed by a short
scored quiz:

1. **What is Phishing?** — Definitions and types: email phishing, spear
   phishing, whaling, smishing, vishing, clone phishing, Business Email
   Compromise (BEC).
2. **Recognizing Phishing Emails** — Red flags such as spoofed senders,
   manufactured urgency, mismatched links, generic greetings, and
   suspicious attachments.
3. **Recognizing Fake Websites** — Typosquatting, lookalike domains, the
   "HTTPS padlock" myth, and how to read a URL correctly.
4. **Social Engineering Tactics** — Authority, urgency, scarcity,
   reciprocity, pretexting, tailgating, and quid pro quo.
5. **Real-World Examples** — The 2017 Google Docs worm, a 2016
   spear-phishing breach, a 2020 vishing-driven account takeover,
   BEC/invoice fraud, and smishing.
6. **Best Practices** — Personal habits, organizational habits, and what to
   do immediately if you've already clicked something suspicious.

Plus two extra menu options:
- **Cheat Sheet** — a quick "ask yourself before you click" checklist.
- **Training Report** — your score per module and an overall percentage
  with tailored feedback.

### Key features
- Zero installation — nothing to `pip install`.
- Score tracking across all modules with a final report card.
- Instant ✅ / ❌ feedback with an explanation after every quiz question.
- Clean, word-wrapped terminal output.

---

## 2. `Phishing-Awareness-Training_.html` — Interactive Web Version

### Requirements
- Any modern browser (Chrome, Firefox, Edge, Safari)
- **No server, no installation, no internet connection required** — it's a
  single self-contained file (HTML + CSS + JavaScript, no external
  dependencies)

### How to run
Just double-click the file, or open it via **File → Open** in your browser.

### What it covers
A dark, "case file"-styled interactive web app with a card-based module
dashboard. **11 modules**, each marked complete as you finish it:

1. What Is Phishing?
2. Anatomy of a Phishing Email *(includes an annotated mock fake email)*
3. Spotting Fake Websites
4. Social Engineering Tactics
5. Spear Phishing & Targeted Attacks
6. Smishing & Vishing *(includes a mock fake SMS example)*
7. Business Email Compromise & QR Code Phishing ("quishing")
8. Best Practices: Email & Browsing Habits
9. Protecting Your Accounts *(MFA, password hygiene, reporting)*
10. Real-World Case Studies *(fake invoice fraud, cloned login pages,
    executive gift-card scam)*
11. Putting It All Together *(a 4-step decision framework)*

Plus a **Final Knowledge Check**: 15 multiple-choice questions with
randomized question and answer order on every attempt, instant feedback,
a running score, and a results screen with a verdict (e.g. *"Phishing
Defense Expert"*).

### Key features
- Single file, no build step — open and go.
- Module completion is tracked in the browser session (`sessionStorage`)
  and persists until the tab is closed.
- Quiz questions and answer choices are shuffled (Fisher–Yates) on every
  attempt, so retakes feel fresh.
- Polished UI with color-coded callout boxes (examples / warnings / tips)
  and realistic mock email/SMS visuals.

---

## Comparing the two versions

| | CLI (`.py`) | Web (`.html`) |
|---|---|---|
| Where it runs | Terminal | Browser |
| Setup | None (just Python 3) | None (just open the file) |
| Modules | 6 | 11 |
| Quiz style | One quiz per module, fixed order | Module content + one shuffled 15-question final exam |
| Progress tracking | In-memory (current run only) | `sessionStorage` (persists until tab closes) |
| Best for | Quick terminal-based training, scripted/automated use, headless servers | Polished, end-user-facing training — onboarding pages, intranet hosting |

---

## Suggested next steps
- Host the HTML file on an internal intranet page or LMS for company-wide
  onboarding.
- Keep both quiz banks in sync if you update one (the CLI script's
  `questions` lists and the HTML file's `quiz` array cover similar but not
  identical content).
- Add persistent storage (a small backend, or `localStorage` instead of
  `sessionStorage`) if you want scores/progress to survive across browser
  sessions, not just within one tab.
