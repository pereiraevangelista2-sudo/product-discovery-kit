# Project Rules: Product Discovery Assistant

<!-- This file defines guidelines for AI agents working in this repository. -->

Refer to [GEMINI.md](./GEMINI.md) and [docs/guia-da-arquitetura.md](./docs/2-guia-da-arquitetura.md) for full architecture and governance details.

## Quick Summary
- Follow the 8 discovery skills available in `.agent/skills/` (and `.agents/skills/`).
- Mark all statements as `[F]` Fact, `[I]` Inference, or `[O]` Opinion.
- Status is `Rascunho` (Draft) until user explicitly approves.
- Never finalize a phase, decision, or document without human approval.
- Maintain the 4 living documents: `andamento-do-discovery.md`, `02-registro-de-pendencias.md`, `03-log-de-decisoes.md`, `mapa-de-requisitos.md`.
- Run the 10-item checklist verification at the end of every produced document.
