# Incident Brief

## INC-001 — Duplicate Payment Requests

**Status:** Under Investigation  
**Service:** Checkout / Payments  
**Initial Severity:** Under Assessment  
**Investigator:** You

---

## Situation

Customer Support has received several reports from customers who appear to have experienced **duplicate payment attempts during checkout**.

The reports do not affect every transaction.

Initial investigation suggests the affected transactions may share one characteristic:

**the original payment request took longer than expected to complete.**

The application remained available throughout the reported period.

---

## Initial Engineering Assessment

The Payments team believes the problem may be related to intermittent instability at the external payment provider.

Their current working theory is:

> Slow responses from the payment provider are causing payment requests to fail unpredictably.

No root cause has been confirmed.

---

## What We Know

At this point:

- duplicate payment attempts have been reported;
- only some transactions appear affected;
- slower payment responses may be associated with the reports;
- the external payment provider is currently suspected;
- the application itself remained available;
- the issue appears to have started recently.

You should treat everything else as **unconfirmed**.

---

## Your Objective

Determine what happened.

You are not being asked simply to find something suspicious.

Your conclusion should answer:

1. What changed?
2. When did it change?
3. Why was the change made?
4. What evidence connects that change to the reported behaviour?
5. Does the available evidence support the initial theory about the external payment provider?
6. What remains uncertain?

---

## Important

The repository contains more information than you need.

Some information may be irrelevant.

Some explanations may sound convincing without being supported by evidence.

Do not assume that the most obvious explanation is the correct one.

---

## Investigation Standard

At the end of the Quest, you should be able to distinguish between:

**What you know**

Evidence directly supported by the repository.

**What you think**

Your interpretation of that evidence.

**What you don't know**

Questions the available evidence cannot yet answer.

That distinction will become increasingly important throughout the QA → Incident Engineering course.

---

## Next Step

Open:

**`QUEST.md`**

Your investigation begins at **Level 0 — Enter the Scene**.
