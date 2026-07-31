# Martin Poiroux

**Software engineer — Toulouse, France.** C++ · C#/.NET · TypeScript · Python

By day I'm the only active developer left on a 500 000-line .NET/WPF product sold to telecom
operators, plus the five smaller SaaS products around it. By night I ship things end to end,
alone: a chess engine I've been writing since 2022, a chess learning platform, an online
multiplayer game with ranked matchmaking, a GDPR compliance SaaS with live payments, and the
AI harness I use to build all of it.

The through-line is that I'd rather build the tool than adopt it — and then measure whether
it actually paid off.

---

## Things you can open right now

| Project | What it is | |
|---|---|---|
| **[opti_chess](https://github.com/poirouxmartin/opti_chess)** | C++20 chess engine and analysis GUI, ~23 000 lines, written from scratch | public repo |
| **[Lucena](https://lucenachess.com)** | Chess learning platform — progression tracking, game import from Lichess / Chess.com / PGN | live · private repo |
| **[BlitzVolley](https://blitzvolley.com)** | Online multiplayer volleyball — real-time netcode, matchmaking, ELO, ranked and casual queues | live · private repo |
| **[ConformeRGPD](https://conformergpd.fr)** | GDPR compliance SaaS — site scanner, cookie-consent widget, legal document generator, subscriptions | live · private repo |

Three of the four are private. I'm happy to walk through any of them live; I'd rather do that
than link you to something you can't open.

---

## Chess

**[opti_chess](https://github.com/poirouxmartin/opti_chess)** is the oldest thread here and the
one I'd want to be judged on. Its engine, *GrogrosZero*, is a hybrid search: UCT-style node
selection layered over alpha-beta with an integrated quiescence search, WDL statistical
evaluation, and 31 hand-written evaluation terms. The search is bounded and allocation-free —
`Node` and `Board` objects come from pools sized at startup from available physical memory, so
when the pool fills the engine refines its existing tree instead of growing. Nothing in it is
borrowed: not the search, not the evaluation, not the piece sprites, which I drew.

It's a research engine, not a competitive one — it isn't UCI, and the README says so plainly.
It plays on Lichess as **[Grogros_Zero](https://lichess.org/@/Grogros_Zero)**, where you can
watch it lose in public.

As a player: **2304 rapid** on [Chess.com](https://www.chess.com/member/martin_poiroux),
**2246 rapid** on [Lichess](https://lichess.org/@/Martin_Poiroux). No FIDE rating — I've only
ever played online and informally offline.

---

## AI-assisted development, with a control group

I've built with AI daily since May 2024, through the whole curve: autocomplete, then agentic,
now Claude Code driving my own orchestration layer. What I think separates useful practice from
enthusiasm is having a measurement discipline attached.

**local-factory** *(private)* is a Python harness — **421 commits, ~32 000 lines, ~1 250 test
functions, 101 design and decision documents** — that drives quantised open-weight models on a
12 GB consumer GPU through a `spec → diff → regression → review` pipeline. It has a model
escalation ladder, cross-session working memory, completion conditions verified against the
filesystem rather than against the model's own word, and git guardrails my agents cannot bypass:
no commits on `main`, no push with a red suite.

The part I actually care about is the registry. Every optimisation gets A/B measured and written
down, including the ones the data killed — two features I wanted were rejected in July 2026 by my
own arbitration process, and "35B is escalation-only" is recorded as **falsified** rather than
quietly deleted. A related habit: never conclude on a failure without an autopsy. When my harness
once reported five completed steps against an empty diff, the cause turned out to be three
separate verification bugs — every one of which had failed in the agent's favour.

"The build is green" is not evidence.

---

## Day job

**Setics** — Toulouse, since 2023. Fibre-network design software. The engineering team went from
roughly nine people to one active developer; I ended up de-facto technical owner of the whole
portfolio, which means daily review, architecture calls, and coordinating a four-person external
team on a GIS plugin.

- **Sttar** — C#/.NET/WPF, 500+ KLOC, deployed at operators across Europe, the US and Asia. Led
  the optimisation pipeline: rank-based CBR and Delaunay-based geometry, taking a critical UI
  operation from 2–10 minutes to 0.5–5 seconds.
- Sole developer or lead on a Blazor Server licensing tool (.NET 10, EF Core, Azure SQL), an SSO
  portal, and a multi-tenant telecom-expense SaaS (NestJS 11, Next.js 16, Cosmos DB, Turborepo).

Before that: MPSI/MP *classes préparatoires*, a maths bachelor's, and an engineering degree from
ENSIIE with the *Numerical Interactions & Video Games* major — which is where the game and engine
work actually comes from.

---

## Stack

**Daily:** C++ · C# / .NET / WPF / Blazor / EF Core · TypeScript / NestJS / Next.js / React ·
Python
**Data & infra:** PostgreSQL + Supabase (RLS) · Cosmos DB · Azure SQL · MongoDB · RabbitMQ ·
Vercel · Azure DevOps · Sentry · Stripe
**AI engineering:** agent harness design · local inference with llama.cpp and Ollama · GGUF
quantisation and KV-cache tuning · RAG · multi-agent orchestration · prompt-cost A/B measurement
**Domains:** game-tree search (MCTS, alpha-beta) · chess programming · real-time multiplayer and
matchmaking · rating systems · geometric optimisation · multi-tenant SaaS · GDPR

Not on this list, and not claimed: PHP/Symfony, Java/Spring, Kubernetes, Go, Rust. I've never run
them in production. I ramp fast and can show you the receipts, but that's a different sentence.

---

## Elsewhere

[LinkedIn](https://linkedin.com/in/martin-poiroux) ·
[Chess.com](https://www.chess.com/member/martin_poiroux) ·
[Lichess](https://lichess.org/@/Martin_Poiroux) ·
poirouxmartin@gmail.com

<sub>Every figure on this page was measured on 2026-07-31, not estimated. Ratings move and commit
counts grow; if something here looks stale, it probably is.</sub>
