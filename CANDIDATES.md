# Candidates — Funniest One-Line Out-of-Office Reply

Criteria, in order: (1) real out-of-office reply a person would switch on;
(2) laugh on first read, no setup; (3) still a real away message; (4) fresh
turn, not beach/inbox/limited-email; (5) short, every word earns its place.
Scores are per-criterion 1–5 totals (max 25).

Pool: 12 lines, each from a different empty lane in WINNER-RESEARCH.md.
Flood-checked vs all 810 titles: `cron`, `linter`, `eval`, `restart`,
`minutes`, `maintenance`, `believable` = 0 hits. `replacement` = 21 hits.

| # | Lane | Line | Ch | Score |
|---|---|---|---|---|
| C1 | handoff | Out of office. Your email has been routed to the cron job, which runs at 3 a.m. and holds grudges. | 100 | 19 |
| C2 | handoff | Out of office until Monday. The on-call rotation has your email; it has also been paged twice and is furious. | 110 | 17 |
| C3 | handoff | I'm away. The vector database has your message and has already forgotten it twice. | 84 | 22 |
| C4 | handoff | Out of office. Your email is now in the eval harness, which scored it 2 out of 10 and moved on. | 97 | 19 |
| C6 | apology | I'm away this week. The linter has flagged my absence as a warning, not an error, and I agree. | 97 | 19 |
| C7 | apology | Out of office. I told the CI queue I was sorry; it is still running my tests out of spite. | 91 | 17 |
| C8 | lying date | Back on Tuesday, a date I chose because it sounds more believable than Friday. | 78 | 25 |
| C9 | lying date | Out of office until the 12th, a date I made up just now and will deny under oath. | 84 | 23 |
| C12 | replacement | I did not write this auto-reply. My replacement did, and frankly it is better than mine. | 87 | 17 |
| C13 | incident | Out of office. The human is down for scheduled maintenance; the schedule was not consulted. | 91 | 19 |
| C14 | incident | Out of office: the human is experiencing an outage. Please do not restart me. | 76 | 21 |
| C15 | permission | Out of office, approved by me in a meeting with myself. The minutes say I deserved it. | 89 | 21 |

Killed before scoring: "This auto-reply was written by my replacement, who has
already asked for my job." — that detail already exists in the field. C12
stays but is demoted for the crowding.

## Head-to-head (top 4)

| Pair | Winner | Deciding criterion | M |
|---|---|---|---|
| C8 vs C9 | C8 | C2 — twist sits inside the date; C9 adds a second joke | 2 |
| C8 vs C3 | C8 | C1 — return date is the canonical auto-reply shape | 2 |
| C8 vs C15 | C8 | C3 — C8 stays a plain away message; C15 jokes about the message | 2 |
| C9 vs C3 | C9 | C1 — return date beats handoff as the recognisable auto-reply | 1 |
| C3 vs C15 | C3 | C1 — handoff is a real auto-reply pattern; self-approval is a memo | 1 |

## Vs the real winners (criterion 1)

None of the eight documented winners is an out-of-office reply — they are
jokes about typos, commits and taglines ("the typo is now load-bearing").
Every candidate beats all eight on criterion 1 by being on-subject; C8 by
the widest margin, since a return date is the most recognisable thing an
auto-reply contains.

## Winner

**C8 — "Back on Tuesday, a date I chose because it sounds more believable than Friday." (78 chars)**
