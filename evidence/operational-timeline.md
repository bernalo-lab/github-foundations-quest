# Operational Timeline — INC-001

**Incident date:** 7 September 2026  
**Timezone:** UTC+01:00 (British Summer Time)

This timeline was assembled from support timestamps, application logs, and dependency health checks.

| Time | Event | Source | Confidence |
|---|---|---|---|
| 09:12 | Normal checkout completes successfully | Application log | High |
| 09:14 | First affected checkout shows provider timeout followed by successful subsequent attempt | Application log | High |
| 09:14 | First customer report received | Customer Support | High |
| 09:23 | Checkout experiences multiple provider timeouts before succeeding | Application log | High |
| 09:23 | Customer reports two payment notifications | Customer Support | Medium |
| 09:29 | ExamplePay health check latency increases significantly | Dependency health check | High |
| 09:30 | ExamplePay health remains degraded | Dependency health check | High |
| 09:41 | Checkout times out once, then succeeds on a later attempt | Application log | High |
| 09:41 | Customer reports timeout followed by successful payment | Customer Support | High |
| 09:49 | Normal checkout completes on first attempt | Application log | High |
| 09:56 | Checkout times out once, then succeeds on a later attempt | Application log | High |
| 09:56 | Customer reports duplicate payment activity | Customer Support | Medium |

## Notes

- Not every transaction during the period was affected.
- The external payment provider showed elevated latency during part of the incident window.
- Application logs record request attempts and responses, but they do not show the provider's internal processing state for requests that timed out.
- Customer reports describe duplicate payment activity, but the available support evidence does not confirm whether every duplicate attempt became a settled charge.

## Open Questions

- Did ExamplePay process any requests that the application recorded as timed out?
- Why do only some slow requests correlate with duplicate payment reports?
- Did any relevant application or configuration change occur shortly before the incident?
- Do existing automated tests cover provider-side processing after a client-side timeout?
