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

Open a command-line application:

- **Windows:** Command Prompt, PowerShell, or Git Bash;
- **macOS:** Terminal;
- **Linux:** Terminal.

Then run:

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
5. Open Command Prompt, PowerShell, Git Bash, or Terminal.
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

#### Help 1.1 — How do I search a repository?

You don't need any special tools for this — pick whichever is easiest for you:

- **On GitHub, in your browser:** open the repository, press `t` on your keyboard (or use the search bar at the top of the page) and start typing a filename to jump to it. To search file *contents*, use the search box at the top of the page and select "In this repository."
- **Locally, in an editor:** most editors (e.g. VS Code) have a "Search across files" panel — usually opened with `Ctrl+Shift+F` (Windows) or `Cmd+Shift+F` (Mac).
- **Locally, from Terminal or Git Bash:** from inside the cloned repository folder, run:

  ```
  grep -ri "retry" .
  ```

  This searches every file for the word "retry", ignoring case. Try it again with "timeout" and "payment".

Any of these approaches is fine. The goal is to find the relevant file, not to master the tool.

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

#### Help 2.3 — How do I read a diff?

When you click on a commit, GitHub shows you its **diff** — the exact lines that changed.

- Lines with a **red** background and a leading `-` show what was **removed** (the "before").
- Lines with a **green** background and a leading `+` show what was **added** (the "after").
- Lines with no colour are unchanged, shown only for context.

For a configuration change, you are usually looking for one red line and one green line for the same setting — that pair is your "before" and "after."

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

#### Help 3.1 — Where do I find Issues, Pull Requests, and CI results?

On the repository's GitHub page, look at the row of tabs near the top (near "Code"):

- **Issues** — reported problems, bugs, and feature requests. Each has a number (e.g. `#12`) and a discussion thread.
- **Pull requests** — proposed changes. Each PR shows the diff, review comments from other people, and a status check area near the bottom.
- **Actions** — this is where CI (Continuous Integration) runs. Each run shows which checks passed or failed, and you can click into a run to see its logs.

If you cannot see one of these tabs, look under the `...` or **More** menu.

A commit is often linked to the Issue or PR that caused it — look for a reference like `#12` in the commit message, or check the PR itself for "Fixes #12" style language.

This is also a good moment to make sure you're signed in to a **GitHub account** — you won't need one to browse Issues and PRs, but you will need one from Level 4 onward.

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

### Getting Started Help

For this level, you will not make changes directly to the original Quest repository.

Instead, you will create your own copy, called a **fork**. Your branch, change, and Pull Request will remain inside your fork.

#### Help 4.1 — Fork the Quest repository

1. Sign in to your GitHub account.
2. Open the original Quest repository.
3. Click **Fork** in the top-right corner.
4. Accept the suggested repository name and create the fork.
5. Copy the HTTPS URL of your fork.
6. In your existing local Quest folder, update `origin` so it points to your fork:

   ```
   git remote set-url origin https://github.com/<your-username>/github-foundations-quest.git
   ```

   Replace `<your-username>` with your GitHub username.

7. Confirm the new destination:

   ```
   git remote -v
   ```

Both `origin` entries should now contain your GitHub username, not `bernalo-lab`.

From this point onward, anything you push to `origin` will go to your own fork.

#### Help 4.2 — Create your working branch

From inside the repository folder, run:

```
git switch -c fix/payment-retry-behaviour
```

This creates a new branch and moves you onto it. Your local `main` branch remains unchanged.

#### Help 4.3 — Make and review your proposed change

Based on your investigation, make the smallest configuration or code change that you believe addresses the duplicate payment behaviour.

Save the file, then review what changed:

```
git status
git diff
```

Check that the diff contains only the change you intended to make.

#### Help 4.4 — Commit your change

Add the file you changed:

```
git add <path-to-changed-file>
```

Replace `<path-to-changed-file>` with the actual file path. Do not type the angle brackets.

Now commit the change:

```
git commit -m "Fix payment retry behaviour"
```

#### Help 4.5 — Push your branch

Run:

```
git push -u origin fix/payment-retry-behaviour
```

The branch will be pushed to your fork, not to the original Quest repository.

#### Help 4.6 — GitHub asks me to sign in

GitHub does not accept your normal account password when pushing over HTTPS.

If Git Credential Manager is installed, Git should open a browser window and ask you to sign in. Complete the browser sign-in and then return to the command line.

If no browser window appears, stop and ask the course instructor for help before creating an access token or changing authentication settings.

Personal Access Tokens and SSH are alternative authentication methods, but their setup is outside the scope of this Quest.

#### Help 4.7 — Open the Pull Request inside your fork

1. Open your fork on GitHub:

   `https://github.com/<your-username>/github-foundations-quest`

2. Open the **Pull requests** tab and click **New pull request**. GitHub may instead display a **Compare & pull request** button after your push; you can use that button.
3. Before creating the Pull Request, check the destination carefully:

   - **Base repository:** `<your-username>/github-foundations-quest`
   - **Base branch:** `main`
   - **Head repository:** `<your-username>/github-foundations-quest`
   - **Compare branch:** `fix/payment-retry-behaviour`

4. If the base repository says `bernalo-lab/github-foundations-quest`, change it to your own fork.
5. Create the Pull Request inside your fork.
6. Submit the URL of your Pull Request to the course instructor for review.

Do **not** open the Pull Request against the original `bernalo-lab/github-foundations-quest` repository.

Do **not** merge the Pull Request. The objective is to propose and explain the change so that another engineer can review it.

### Objectives

1. Create a new branch.
2. Make the smallest change that your investigation supports.
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

It does not need to be merged to complete this level.

**LEVEL 4 COMPLETE ✓**

---

# Level 5 — Challenge the AI

## Stretch Challenge

You may now use GitHub Copilot to help investigate the repository.

> **Before you start:** GitHub Copilot must be available and enabled for your GitHub account. Access may come through Copilot Free, a paid plan, an education benefit, or an organisation licence. Usage limits may apply. If you don't see Copilot in your editor or on GitHub, check with your course instructor before assuming this level is broken.

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
