# GitHub Foundations Quest

## INC-001 — The Retry Mystery

You have received the incident brief.

Now investigate.

Do not rush to find the root cause.

Your first job is to understand the evidence available to you.

---

# Level 0 — Enter the Scene

### Mission

Get the investigation environment onto your machine and orient yourself inside the repository.

### Objectives

1. Clone this repository into your local environment.
2. Open and explore the repository files locally or on GitHub.
3. Locate `INCIDENT-BRIEF.md`.
4. Identify the main folders in the repository.
5. Find the part of the application that appears responsible for payments.

### Getting Started Help

If you're new to Git or GitHub, start here before moving on.

#### Help 0.1 — How do I clone the repository?

**Before you start**

This Quest assumes that Git is already installed on your computer.

Open Windows Command Prompt and run:

```
git --version
```

If Git is installed, you should see something similar to:

```
git version 2.x.x
```

If you receive a message saying that git is not recognised, stop here and contact the course instructor.

**Clone the Quest repository**

1. Launch the 'GitHub Quest' repository at https://github.com/bernalo-lab/github-foundations-quest/
2. Click the green **Code** button.
3. Select **HTTPS**.
4. Copy the repository URL.
5. Open Windows Command Prompt.
6. Move to the folder where you want the Quest.
7. Run the following command:

   ```
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the URL you copied from GitHub.

   For example:

   ```
   git clone https://github.com/bernalo-lab/github-foundations-quest.git
   ```

8. Move into the repository:

   ```
   cd github-foundations-quest
   ```

9. Check the repository status:

   ```
   git status
   ```

   Expected message:

   ```
   On branch main
   Your branch is up to date with 'origin/main'.
   nothing to commit, working tree clean
   ```

**Mission accomplished**

You have just: cloned your first repository → entered it → checked its Git status.

Don't worry about understanding every Git command yet. For now, you have the case files.

#### Help 0.2 — What is an editor? Do I need one?

**Open the repository files**

You need something that lets you comfortably browse and read the files in the repository. This is usually called a code editor.

If you already use Visual Studio Code, PyCharm, IntelliJ, or another editor, use that.

If you don't have one, don't worry. For Levels 0–3 you can investigate most of the Quest directly on GitHub in your web browser.

You do not need to install an editor just to begin the investigation.

### Enter the Repository

Now that you have the case files, take a few minutes to explore them.

You can do this either:

- on the GitHub repository page in your web browser; or
- by opening the cloned `github-foundations-quest` folder on your computer.

Don't try to understand everything.

Start by looking at the names of the files and folders.

Ask yourself:

> **Which ones sound relevant to a payment incident?**

Open anything that looks interesting.

There is no penalty for looking in the wrong place.

### Investigation Question

**Which directory or file would you investigate first if you wanted to understand how payment requests are handled?**

Record your answer before continuing.

### Level Complete When

You can:

- locate the repository locally;
- navigate its directory structure;
- locate the incident brief;
- identify where payment-related code appears to live.

**LEVEL 0 COMPLETE ✓**

---

# Level 1 — Find the Evidence

### Mission

Something in this application controls what happens when a payment request does not complete as expected.

Find it.

### Objectives

Search the repository for configuration or code associated with:

- payments;
- retries;
- timeouts.

Do not assume the first occurrence you find is the important one.

### Investigation Questions

1. Where is payment retry behaviour configured?
2. What is the current retry setting?
3. What timeout behaviour can you identify?
4. Which application component appears to use these settings?

Record the **file path** supporting each answer.

### Evidence Standard

Do not write:

> "I think the application retries three times."

Write:

> "The configuration specifies three retry attempts. Evidence: `[file path]`."

Your evidence must be something another investigator could independently locate.

**LEVEL 1 COMPLETE ✓**

---

# Level 2 — Reconstruct the Change

### Mission

Finding the current configuration isn't enough.

You need to know whether it has always behaved this way.

### Objectives

Use Git history to investigate the relevant configuration and code.

#### Help 2.1 — Finding the repository's history
On the GitHub repository homepage, look above the file list for the link showing the number of commits.
Click it.

#### Help 2.2 — What is a commit?
A commit is a recorded change to the repository. Git history allows you to see what changed, when it changed, and the explanation recorded by the person who made the change.

Determine:

- whether the retry behaviour changed;
- when it changed;
- which commit introduced the change;
- what the previous behaviour was;
- what explanation was given for the change.

### Investigation Questions

1. What changed?
2. What was the previous value or behaviour?
3. Which commit introduced the change?
4. When was the commit made?
5. What does the commit message say?
6. Does the commit message explain the potential customer impact?

### Evidence Required

Record:

**Commit:**  
**Date:**  
**Relevant file:**  
**Before:**  
**After:**  
**Commit explanation:**

Then answer:

> **At this stage, what is your leading hypothesis?**

Do not worry about being wrong.

You are expected to change your hypothesis if later evidence contradicts it.

**LEVEL 2 COMPLETE ✓**

---

# Level 3 — Follow the Engineering Trail

### Mission

Code rarely changes without context.

Find the engineering conversation surrounding the change.

### Objectives

Investigate the repository's:

- Issues;
- Pull Requests;
- review comments;
- CI workflow/results.

Look for evidence connected to the change identified in Level 2.

### Investigation Questions

1. Was there an Issue associated with the change?
2. What problem was engineering originally trying to solve?
3. Was there a Pull Request?
4. Did anyone raise concerns during review?
5. Were those concerns resolved?
6. What did CI report?
7. Did passing automated checks prove the change was safe for production?

### Think Like QA

This part should feel familiar.

Ask:

> **What was tested?**

Then ask the more important question:

> **What wasn't tested?**

### Your Current Judgement

Using only repository evidence, complete:

**What I know:**  
Evidence directly supported by the repository.

**What I think:**  
My current explanation for the duplicate payment behaviour.

**What I don't know:**  
Questions that cannot yet be answered from the available evidence.

**Confidence:** Low / Medium / High

### Final Question

Does the evidence currently support the original engineering theory that instability at the external payment provider is the primary cause?

**Yes / No / Insufficient evidence**

Explain your answer and cite the evidence that supports it.

**LEVEL 3 COMPLETE ✓**

---

# Level 4 — Make the Fix

## Recommended / Conditional

You have investigated the problem.

Now work with the repository rather than simply reading it.

### Mission

Create a proposed change without modifying the main branch directly.

### Objectives

1. Create a new branch.
2. Make the required change.
3. Review your local changes.
4. Commit the change with a meaningful commit message.
5. Push your branch.
6. Open a Pull Request.
7. Explain in the Pull Request:
   - what you changed;
   - why;
   - what evidence led you there;
   - what testing should be performed before merging.

### Important

The objective is not merely to demonstrate that you know Git commands.

Your Pull Request should allow another engineer to understand your **reasoning**.

**LEVEL 4 COMPLETE ✓**

---

# Level 5 — Challenge the AI

## Stretch Challenge

You may now use GitHub Copilot to help investigate the repository.

But there is a catch.

Copilot is not your answer key.

### Mission

Ask Copilot to independently investigate the duplicate payment behaviour.

Useful questions might include:

- Trace how a checkout request reaches the payment component.
- Where is retry behaviour implemented or configured?
- What happens when a payment request times out?
- Which recent changes could affect duplicate payment attempts?
- What potential failure modes exist in the retry implementation?

Do not simply accept the response.

### Verification Challenge

Choose at least three factual claims made by Copilot.

For each claim record:

**Copilot claim:**  
**Repository evidence:**  
**Verified / Partially verified / Not verified / Incorrect**

Then answer:

> Did Copilot change your incident hypothesis?

If yes, explain why.

If no, explain why not.

---

# Final Investigator Report

Before completing the Quest, provide a short investigation summary.

## Incident

INC-001 — Duplicate Payment Requests

## What Changed?

[Your answer]

## Evidence

[Repository evidence supporting your conclusion]

## Most Likely Explanation

[Your current judgement]

## Competing Explanation

[At least one plausible alternative]

## Confidence

Low / Medium / High

## What Remains Unknown?

[Outstanding uncertainty]

## Recommended Next Action

[What should engineering do next?]

## AI Assistance

If Copilot was used:

[Explain where it helped and how its output was verified.]

---

# Quest Complete

You have not completed GitHub Foundations because you memorised where GitHub keeps its buttons.

You completed it because you used GitHub to answer engineering questions.

During this investigation you encountered:

**Repository navigation → search → configuration → Git history → commits → diffs → Issues → Pull Requests → reviews → CI → evidence → hypothesis → judgement**

If you completed Level 4, you also used:

**branch → change → commit → push → Pull Request**

If you completed Level 5, you added:

**AI assistance → independent verification**

These are not isolated GitHub features.

They are tools for understanding **what changed, why it changed, and whether that change matters.**

That is why GitHub matters to an Incident Engineer.

---

## One Rule to Take With You

> **Copilot can help you find the evidence. It cannot be the evidence.**

Welcome to the investigation.
