<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=30&duration=3000&pause=1000&color=3FB68B&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=100&lines=Martin+Poiroux;Software+Engineer+%7C+C%2B%2B+%7C+C%23+%7C+Chess+Engines" alt="Martin Poiroux - Software Engineer" />
</h1>

<p align="center">
  <strong>Toulouse, France</strong> · Building things end to end since 2016
</p>

<p align="center">
  <a href="https://github.com/poirouxmartin/opti_chess">
    <img src="https://img.shields.io/badge/C%2B%2B-20-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++" />
  </a>
  <a href="https://github.com/poirouxmartin/Chess-Challenge">
    <img src="https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white" alt="C#" />
  </a>
  <a href="https://lucenachess.com/en">
    <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  </a>
  <a href="https://lucenachess.com/en">
    <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white" alt="Next.js" />
  </a>
  <a href="https://blitzvolley.com/en">
    <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js" />
  </a>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
</p>

By day I am the only developer on a 500 000-line .NET/WPF product sold to telecom operators,
and on the smaller web applications built around it. By night I ship things end to end, alone:
a chess engine I have been writing since 2022, a chess learning platform, an online multiplayer
game with ranked matchmaking, a GDPR compliance SaaS with live payments, and the AI harness I
use to build all of it.

The through-line is that I would rather build the tool than adopt it, then measure whether it
actually paid off.

---

## Things you can open right now

| Project | What it is | |
|---|---|---|
| **[opti_chess](https://github.com/poirouxmartin/opti_chess)** | C++20 chess engine and analysis GUI, written from scratch | [![Repo](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github)](https://github.com/poirouxmartin/opti_chess) |
| **[Lucena](https://lucenachess.com/en)** | Chess learning platform: progression tracking, game import from Lichess, Chess.com and PGN | [![Live](https://img.shields.io/badge/Live-3FB68B?style=flat)](https://lucenachess.com/en) · private repo |
| **[BlitzVolley](https://blitzvolley.com/en)** | Online multiplayer volleyball: real-time netcode, matchmaking, ELO, ranked and casual queues | [![Live](https://img.shields.io/badge/Live-3FB68B?style=flat)](https://blitzvolley.com/en) · private repo |
| **[ConformeRGPD](https://conformergpd.fr)** | GDPR compliance SaaS: site scanner, cookie-consent widget, legal document generator, subscriptions | [![Live](https://img.shields.io/badge/Live-3FB68B?style=flat)](https://conformergpd.fr) · private repo · FR only |

A note on language: Lucena and BlitzVolley ship French first and English second, and the links
above go straight to the English version. ConformeRGPD is French-only by design, since it sells
GDPR compliance to French freelancers and small businesses, so there is no one else to translate
it for.

Three of the four repos are private. I am happy to walk through any of them live; I would rather
do that than link you to something you cannot open.

---

## Chess

<a href="https://github.com/poirouxmartin/opti_chess">
  <img width="49%" src="https://github-readme-stats.vercel.app/api/pin/?username=poirouxmartin&repo=opti_chess&theme=tokyonight&hide_border=true" alt="opti_chess repo" />
</a>

**[opti_chess](https://github.com/poirouxmartin/opti_chess)** is the oldest thread here and the
one I would want to be judged on. Its engine, *GrogrosZero*, is a hybrid search: UCT-style node
selection layered over alpha-beta with an integrated quiescence search, WDL statistical
evaluation, and hand-written evaluation terms. The search is bounded and allocation-free.
`Node` and `Board` objects come from pools sized at startup from available physical memory, so
when a pool fills, the engine refines the tree it already has instead of growing it. Nothing in
it is borrowed: not the search, not the evaluation, not the piece sprites, which I drew.

It is a research engine, not a competitive one. It is not UCI, and the README says so plainly.
It plays on Lichess as **[Grogros_Zero](https://lichess.org/@/Grogros_Zero)**, where you can
watch it lose in public.

A second engine of mine ranked 54th of 624 by rating in the official results of Sebastian
Lague's Tiny Chess Bot Challenge (2023), listed as *Grogros (by: Grobert)*, under a 1 024-token
limit on the entire bot.

As a player: **2304 rapid** on [Chess.com](https://www.chess.com/member/martin_poiroux),
**2246 rapid** on [Lichess](https://lichess.org/@/Martin_Poiroux). No FIDE rating, no club play.
I have only ever played online and informally offline.

---

## AI-assisted development, with a control group

I have built with AI daily since May 2024, through the whole curve: autocomplete, then agentic,
now Claude Code driving my own orchestration layer. What separates useful practice from
enthusiasm is having a measurement discipline attached to it.

Two tools came out of that. **claude-remote** *(private)* is an orchestration layer over Claude
Code: several agent sessions running in parallel across separate projects, each with its own task
list, git view and reusable workflows, plus a daily report on where the tokens actually went. It
is the one I use every day.

**local-factory** *(private)* is a Python harness that drives quantised open-weight models on a
12 GB consumer GPU through a `spec → diff → regression → review` pipeline. It has a model
escalation ladder, cross-session working memory, completion conditions verified against the
filesystem rather than against the model's own word, and git guardrails my agents cannot bypass:
no commits on `main`, no push with a red suite.

The part I actually care about is the registry. Every optimisation gets A/B measured and written
down, including the ones the data killed. Two features I wanted were rejected by my own
arbitration process, and "35B is escalation-only" is recorded as **falsified** rather than
quietly deleted. A related habit: never conclude on a failure without an autopsy. When my harness
once reported five completed steps against an empty diff, the cause turned out to be three
separate verification bugs, every one of which had failed in the agent's favour.

"The build is green" is not evidence.

---

## Day job

**Setics**, Toulouse, since 2023. Fibre-network design software. I am the only developer on the
main product and the de-facto technical owner of the portfolio around it, which means daily
review and the architecture calls.

- **Sttar**, C#/.NET/WPF, 500+ KLOC, deployed at operators across Europe, the US and Asia. Led
  the optimisation work on the computational-geometry path, taking a critical interactive
  operation from minutes to seconds.
- Sole developer or lead on the internal line-of-business web applications around it: .NET 10 and
  Blazor Server on EF Core and Azure SQL, plus a multi-tenant SaaS on NestJS and Next.js.

Before that: MPSI/MP *classes préparatoires*, a maths bachelor's, and an engineering degree from
ENSIIE with the *Numerical Interactions & Video Games* major, which is where the game and engine
work actually comes from.

---

## Stack

<p align="center">
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white" alt="C#" />
  <img src="https://img.shields.io/badge/.NET-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt=".NET" />
  <img src="https://img.shields.io/badge/WPF-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt="WPF" />
  <img src="https://img.shields.io/badge/Blazor-512BD4?style=flat-square&logo=blazor&logoColor=white" alt="Blazor" />
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white" alt="NestJS" />
  <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=next.js&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white" alt="Supabase" />
  <img src="https://img.shields.io/badge/Azure-0089D6?style=flat-square&logo=microsoftazure&logoColor=white" alt="Azure" />
  <img src="https://img.shields.io/badge/Phaser-3-52B788?style=flat-square&logo=phaser&logoColor=white" alt="Phaser" />
  <img src="https://img.shields.io/badge/Stripe-635BFF?style=flat-square&logo=stripe&logoColor=white" alt="Stripe" />
  <img src="https://img.shields.io/badge/Sentry-362D59?style=flat-square&logo=sentry&logoColor=white" alt="Sentry" />
</p>

**AI engineering:** agent harness design · local inference with llama.cpp and Ollama · GGUF
quantisation and KV-cache tuning · RAG · multi-agent orchestration · prompt-cost A/B measurement

**Domains:** game-tree search (MCTS, alpha-beta) · chess programming · real-time multiplayer and
matchmaking · rating systems · geometric optimisation · multi-tenant SaaS · GDPR

Rust and Go appear in side projects only, never in production. Not claimed at all: PHP/Symfony,
Java/Spring, Kubernetes. I ramp fast and can show you the receipts, but that is a different
sentence.

---

## Elsewhere

<p align="center">
  <a href="https://linkedin.com/in/martin-poiroux">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://www.chess.com/member/martin_poiroux">
    <img src="https://img.shields.io/badge/Chess.com-81B64C?style=for-the-badge&logo=chess.com&logoColor=white" alt="Chess.com" />
  </a>
  <a href="https://lichess.org/@/Martin_Poiroux">
    <img src="https://img.shields.io/badge/Lichess-FFFFFF?style=for-the-badge&logo=lichess&logoColor=black" alt="Lichess" />
  </a>
  <a href="mailto:poirouxmartin@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</p>

<sub>Ratings move. If something here looks stale, it probably is.</sub>
