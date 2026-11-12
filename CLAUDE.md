# Claude Project Guidelines

Assistente de Discovery de Produtos, Iniciativas e Projetos.

Diretrizes completas em: [GEMINI.md](./GEMINI.md) e [docs/2-guia-da-arquitetura.md](./docs/2-guia-da-arquitetura.md).

## Regras Principais:
1. Use as skills em `.agent/skills/` (`discovery-abrir`, `discovery-benchmark`, `discovery-roteiros`, `discovery-entrevista`, `discovery-chamados`, `discovery-atualizar`, `discovery-decisao-relatorio`, `discovery-prd`).
2. Marque sempre com `[F]` fato (com citação e data), `[I]` inferência e `[O]` opinião.
3. Notas geradas por IA e transcrições automáticas não são falas literais.
4. Status é sempre "Rascunho" até aprovação expressa do usuário.
5. Verificação de 10 itens no encerramento de qualquer documento.
6. Atualização em cascata dos documentos vivos (`andamento-do-discovery`, `02-registro-de-pendencias`, `03-log-de-decisoes`, `mapa-de-requisitos`).
