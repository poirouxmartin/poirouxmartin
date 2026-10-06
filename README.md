<a href="https://martinpoiroux.com/en/">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
    <img src="assets/banner-dark.svg" width="100%" alt="Martin Poiroux, software engineer, Toulouse">
  </picture>
</a>

<p align="center">
  <a href="https://martinpoiroux.com/en/"><img src="https://img.shields.io/badge/martinpoiroux.com-0c0a09?style=flat-square&labelColor=0c0a09&color=0c0a09" alt="martinpoiroux.com"></a>
  <a href="https://www.malt.fr/profile/martinpoiroux"><img src="https://img.shields.io/badge/Malt-0c0a09?style=flat-square&color=0c0a09" alt="Malt"></a>
  <a href="https://linkedin.com/in/martin-poiroux"><img src="https://img.shields.io/badge/LinkedIn-0c0a09?style=flat-square&logo=linkedin&logoColor=c8a96a&color=0c0a09" alt="LinkedIn"></a>
  <a href="mailto:poirouxmartin@gmail.com"><img src="https://img.shields.io/badge/Email-0c0a09?style=flat-square&logo=gmail&logoColor=c8a96a&color=0c0a09" alt="Email"></a>
</p>

By day I am the only developer on a 500 000-line .NET/WPF product sold to telecom operators,
and on the smaller web applications built around it. By night I ship things end to end, alone:
a chess engine I have been writing since 2022, a chess learning platform, an online multiplayer
game with ranked matchmaking, a GDPR compliance SaaS with live payments, and the AI harness I
use to build all of it.

The through-line is that I would rather build the tool than adopt it, then measure whether it
actually paid off.

<p align="center"><img src="assets/divider.svg" width="60%" alt=""></p>

## Things you can open right now

| Project | What it is | |
|---|---|---|
| **[opti_chess](https://github.com/poirouxmartin/opti_chess)** | C++20 chess engine and analysis GUI, written from scratch | [![Repo](https://img.shields.io/badge/GitHub-0c0a09?style=flat-square&logo=github&logoColor=c8a96a)](https://github.com/poirouxmartin/opti_chess) |
| **[Lucena](https://lucenachess.com/en)** | Chess learning platform: progression tracking, game import from Lichess, Chess.com and PGN | [![Live](https://img.shields.io/badge/Live-c8a96a?style=flat-square)](https://lucenachess.com/en) · private repo |
| **[BlitzVolley](https://blitzvolley.com/en)** | Online multiplayer volleyball: real-time netcode, matchmaking, ELO, ranked and casual queues | [![Live](https://img.shields.io/badge/Live-c8a96a?style=flat-square)](https://blitzvolley.com/en) · private repo |
| **[ConformeRGPD](https://conformergpd.fr)** | GDPR compliance SaaS: site scanner, cookie-consent widget, legal document generator, subscriptions | [![Live](https://img.shields.io/badge/Live-c8a96a?style=flat-square)](https://conformergpd.fr) · private repo · FR only |
| **[chess-net](https://github.com/poirouxmartin/chess-net)** | Second chess engine, in Rust, with a learned evaluation (NNUE and AlphaZero-style self-play in PyTorch) | [![Repo](https://img.shields.io/badge/GitHub-0c0a09?style=flat-square&logo=github&logoColor=c8a96a)](https://github.com/poirouxmartin/chess-net) |
| **[game-solver](https://github.com/poirouxmartin/game-solver)** | Exact Connect 4 solver: memoised negamax compiled to WASM, spread over a Web Worker pool | [![Repo](https://img.shields.io/badge/GitHub-0c0a09?style=flat-square&logo=github&logoColor=c8a96a)](https://github.com/poirouxmartin/game-solver) |
| **[barricade_ai](https://github.com/poirouxmartin/barricade_ai)** | Barricade engine: alpha-beta compiled with numba, about 2.5M nodes/s, plus MCTS | [![Repo](https://img.shields.io/badge/GitHub-0c0a09?style=flat-square&logo=github&logoColor=c8a96a)](https://github.com/poirouxmartin/barricade_ai) |
| **[barricade_board](https://github.com/poirouxmartin/barricade_board)** | Malefiz in C++20/SDL2: four players, dice, and an MCTS opponent guided by a self-play network | [![Repo](https://img.shields.io/badge/GitHub-0c0a09?style=flat-square&logo=github&logoColor=c8a96a)](https://github.com/poirouxmartin/barricade_board) |
| **[sure-weather](https://github.com/poirouxmartin/sure-weather)** | Weather fusion across providers, weighted by error learned against observed weather; PWA and Android widget | [![Repo](https://img.shields.io/badge/GitHub-0c0a09?style=flat-square&logo=github&logoColor=c8a96a)](https://github.com/poirouxmartin/sure-weather) |

A note on language: Lucena and BlitzVolley ship French first and English second, and the links
above go straight to the English version. ConformeRGPD is French-only by design, since it sells
GDPR compliance to French freelancers and small businesses, so there is no one else to translate
it for.

The three products are private repos. I am happy to walk through any of them live; I would rather
do that than link you to something you cannot open. Every project, public or not, has a page on
[martinpoiroux.com](https://martinpoiroux.com/en/projects/).

<p align="center"><img src="assets/divider.svg" width="60%" alt=""></p>

## Chess

<a href="https://github.com/poirouxmartin/opti_chess">
  <img width="49%" src="https://github-readme-stats.vercel.app/api/pin/?username=poirouxmartin&repo=opti_chess&bg_color=0c0a09&title_color=c8a96a&text_color=96928a&icon_color=c8a96a&border_color=241f1b" alt="opti_chess repo" />
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

<p align="center"><img src="assets/divider.svg" width="60%" alt=""></p>

## AI-assisted development, with a control group

I have built with AI daily since May 2024, through the whole curve: autocomplete, then agentic,
now Claude Code driving my own orchestration layer. What separates useful practice from
enthusiasm is having a measurement discipline attached to it.

Two tools came out of that. **claude-remote** *(private)* is an orchestration layer over Claude
Code: several agent sessions running in parallel across separate projects, each with its own task
list, git view and reusable workflows, plus a daily report on where the tokens actually went. It
is the one I use every day.

**[local-factory](https://github.com/poirouxmartin/local-factory-harness)** *(public snapshot of a private working repo)* is a Python harness that drives quantised open-weight models on a
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

<p align="center"><img src="assets/divider.svg" width="60%" alt=""></p>

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

<p align="center"><img src="assets/divider.svg" width="60%" alt=""></p>

## Stack

<p align="center">
  <img src="https://img.shields.io/badge/C%2B%2B-151211?style=flat-square&logo=cplusplus&logoColor=c8a96a" alt="C++" />
  <img src="https://img.shields.io/badge/C%23-151211?style=flat-square&logo=csharp&logoColor=c8a96a" alt="C#" />
  <img src="https://img.shields.io/badge/.NET-151211?style=flat-square&logo=dotnet&logoColor=c8a96a" alt=".NET" />
  <img src="https://img.shields.io/badge/WPF-151211?style=flat-square&logo=dotnet&logoColor=c8a96a" alt="WPF" />
  <img src="https://img.shields.io/badge/Blazor-151211?style=flat-square&logo=blazor&logoColor=c8a96a" alt="Blazor" />
  <img src="https://img.shields.io/badge/TypeScript-151211?style=flat-square&logo=typescript&logoColor=c8a96a" alt="TypeScript" />
  <img src="https://img.shields.io/badge/NestJS-151211?style=flat-square&logo=nestjs&logoColor=c8a96a" alt="NestJS" />
  <img src="https://img.shields.io/badge/Next.js-151211?style=flat-square&logo=next.js&logoColor=c8a96a" alt="Next.js" />
  <img src="https://img.shields.io/badge/React-151211?style=flat-square&logo=react&logoColor=c8a96a" alt="React" />
  <img src="https://img.shields.io/badge/Python-151211?style=flat-square&logo=python&logoColor=c8a96a" alt="Python" />
  <img src="https://img.shields.io/badge/Node.js-151211?style=flat-square&logo=node.js&logoColor=c8a96a" alt="Node.js" />
  <img src="https://img.shields.io/badge/PostgreSQL-151211?style=flat-square&logo=postgresql&logoColor=c8a96a" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Supabase-151211?style=flat-square&logo=supabase&logoColor=c8a96a" alt="Supabase" />
  <img src="https://img.shields.io/badge/Azure-151211?style=flat-square&logo=microsoftazure&logoColor=c8a96a" alt="Azure" />
  <img src="https://img.shields.io/badge/Phaser-3-151211?style=flat-square&logo=phaser&logoColor=c8a96a" alt="Phaser" />
  <img src="https://img.shields.io/badge/Stripe-151211?style=flat-square&logo=stripe&logoColor=c8a96a" alt="Stripe" />
  <img src="https://img.shields.io/badge/Sentry-151211?style=flat-square&logo=sentry&logoColor=c8a96a" alt="Sentry" />
</p>

**AI engineering:** agent harness design · local inference with llama.cpp and Ollama · GGUF
quantisation and KV-cache tuning · RAG · multi-agent orchestration · prompt-cost A/B measurement

**Domains:** game-tree search (MCTS, alpha-beta) · chess programming · real-time multiplayer and
matchmaking · rating systems · geometric optimisation · multi-tenant SaaS · GDPR

Rust and Go appear in side projects only, never in production. Not claimed at all: PHP/Symfony,
Java/Spring, Kubernetes. I ramp fast and can show you the receipts, but that is a different
sentence.

<p align="center"><img src="assets/divider.svg" width="60%" alt=""></p>

## Elsewhere

[martinpoiroux.com](https://martinpoiroux.com/en/) · [Malt](https://www.malt.fr/profile/martinpoiroux) · [LinkedIn](https://linkedin.com/in/martin-poiroux) · [Chess.com](https://www.chess.com/member/martin_poiroux) · [Lichess](https://lichess.org/@/Martin_Poiroux) · [itch.io](https://poirouxmartin.itch.io)

<sub>Ratings move. If something here looks stale, it probably is.</sub>
