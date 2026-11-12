# Kit de Discovery de Produto

Ambiente estruturado para conduzir discoverys de produto do enquadramento até o PRD, com rastreabilidade total de evidências e governança humana em cada etapa.

---

## 🚀 Como Começar

Para iniciar um novo discovery, basta digitar no chat:

> *"Quero abrir o discovery de [tema/iniciativa]."*

O assistente ativará automaticamente a skill `discovery-abrir` (Etapa 0 - Enquadramento), fará as perguntas iniciais e montará a estrutura de pastas e documentos vivos para você revisar.

---

## 🛠️ Skills Disponíveis no Projeto

As skills estão instaladas em `.agent/skills/` (e `.agents/skills/`):

| Skill | Etapa / Função | Quando usar |
|---|---|---|
| **`discovery-abrir`** | Etapa 0: Enquadramento | Criar a pasta do discovery e gerar os documentos vivos e o enquadramento inicial. |
| **`discovery-benchmark`** | Etapa 1: Benchmark | Rodadas de análise de concorrentes e referências públicas com quadro comparativo. |
| **`discovery-roteiros`** | Preparação de Entrevistas | Gerar roteiros de entrevista personalizados por área interna, cliente ou especialista. |
| **`discovery-entrevista`** | Etapas 2 e 3: Entrevistas | Consolidar transcrições ou notas de entrevistas separando fato, inferência e opinião. |
| **`discovery-chamados`** | Etapa 4: Chamados de Suporte | Analisar exportações de chamados (tickets/helpdesk) com métricas quantitativas. |
| **`discovery-atualizar`** | Cascata de Documentos Vivos | Manter em dia o andamento, mapa de requisitos, pendências e decisões ("Onde estamos?"). |
| **`discovery-decisao-relatorio`** | Decisão e Relatórios | Matriz ponderada de decisão, critérios de corte e redação do relatório final. |
| **`discovery-prd`** | PRD com Rastreabilidade | Redigir o PRD vinculando cada requisito à evidência que o originou. |

---

## 📂 Estrutura de Arquivos

```text
teste_packDiscovery/
├── .agent/skills/              # 8 skills do kit de discovery instaladas
├── .agents/                    # Atalho/junção para compatibilidade de agentes
├── Discoverys/                 # Diretório onde as pastas de cada discovery serão salvas
├── docs/                       # Documentação do kit e instruções de arquitetura
│   ├── 1-instrucoes-do-projeto.md
│   ├── 2-guia-da-arquitetura.md
│   └── LEIA-ME.md
├── skills-para-upload/         # Arquivos .zip individuais para upload em outras plataformas (ex.: Claude)
├── GEMINI.md                   # Regras permanentes e diretrizes do Antigravity
├── AGENTS.md                   # Diretrizes universais de agentes
├── CLAUDE.md                   # Diretrizes para Claude Code
└── requirements.txt            # Dependências Python para análise de chamados
```

---

## 📋 Comandos e Exemplos de Prompt

- **Abrir um discovery:** *"Quero abrir o discovery de módulo de pagamentos."*
- **Benchmark:** *"Abra a rodada 1 de benchmark com os concorrentes A, B e C."*
- **Roteiro de entrevista:** *"Prepare um roteiro de entrevista com a Engenharia sobre viabilidade técnica (40 min)."*
- **Registrar entrevista:** *"Segue a transcrição da entrevista com o Diretor de Operações."*
- **Analisar chamados:** *"Segue a planilha de chamados do suporte para consolidar."*
- **Status do discovery:** *"Onde estamos no discovery atual? Quais pendências faltam?"*
- **Registrar decisão:** *"Decidi que a solução será construída internamente (Opção A)."*
- **Matriz de decisão:** *"Monte a matriz de decisão ponderada."*
- **Gerar PRD:** *"Gere o PRD a partir das evidências do mapa de requisitos."*
