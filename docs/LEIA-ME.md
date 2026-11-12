# Kit de discovery de produto para o Claude

Este kit monta, no seu Claude, um assistente que conduz discoverys de produto do enquadramento até o PRD, com rastreabilidade de evidências e pontos de aprovação seus em cada etapa.

O kit é genérico: não traz dados de nenhuma empresa, cliente ou pessoa. Você preenche com o seu contexto.

## O que tem aqui

| Item | Para quê |
|---|---|
| `LEIA-ME.md` | Este guia de instalação |
| `2-guia-da-arquitetura.md` | Como o método funciona e por quê (leia uma vez) |
| `1-instrucoes-do-projeto.md` | Texto para colar nas instruções do Projeto |
| `skills-para-upload/` | Uma skill por arquivo .zip, prontas para enviar |
| `skills/` | As mesmas skills abertas, para ler ou ajustar antes de enviar |

As 8 skills:

| Skill | Etapa |
|---|---|
| discovery-abrir | Etapa 0: enquadramento e criação da pasta e dos documentos vivos |
| discovery-benchmark | Etapa 1: rodadas de benchmark com fontes públicas |
| discovery-roteiros | Preparação das entrevistas (internas, clientes, especialistas) |
| discovery-entrevista | Etapas 2 e 3: consolidar cada entrevista |
| discovery-chamados | Etapa 4: consolidar chamados de suporte (inclui script de análise) |
| discovery-atualizar | Manter andamento, mapa de requisitos, pendências e log em dia; "onde estamos?" |
| discovery-decisao-relatorio | Matriz de decisão, relatório final e relatórios parciais |
| discovery-prd | PRD com rastreabilidade até a evidência |

## Instalação (cerca de 15 minutos)

### 1. Confirme os pré-requisitos

- Execução de código e criação de arquivos ligada: Configurações > Capacidades ("Create and edit files" / "Criar e editar arquivos").
- Em plano Team ou Enterprise, o administrador precisa permitir skills criadas por usuários. Se a opção de enviar skill não aparecer, peça ao admin.

### 2. Envie as 8 skills

Para cada arquivo de `skills-para-upload/`:
1. Abra **Personalizar > Skills** (Customize > Skills).
2. Clique em **+** > **Criar skill** > **Enviar uma skill** (Upload a skill).
3. Escolha o .zip. Não descompacte: o zip já tem a pasta com o nome certo.
4. Confira se a skill aparece ligada na lista.

Os nomes dos menus podem mudar com o tempo; a ajuda oficial está em support.claude.com ("Use skills in Claude").

### 3. Crie o Projeto

1. **Projetos > Novo projeto.** Nome sugerido: "Discovery - <tema>".
2. Abra `1-instrucoes-do-projeto.md`, troque os campos `{{ }}` e cole o texto nas **instruções do projeto**.
3. Opcional: na descrição do projeto, escreva o objetivo em uma linha.

### 4. Conecte onde ficam os arquivos (recomendado)

O método funciona melhor com uma pasta por discovery no **Google Drive** (conector Google Drive em Configurações > Conectores). Crie uma pasta "Discoverys" no Drive. Sem conector, o Claude cria os documentos no próprio projeto ou como arquivos para você baixar.

### 5. Comece

Numa conversa dentro do projeto, diga:

> Quero abrir o discovery de <tema>.

O Claude vai fazer as perguntas da Etapa 0, pedir autorização para criar a pasta e entregar o enquadramento em rascunho para você aprovar.

## Uso no dia a dia

| Você quer | Diga algo como |
|---|---|
| Começar um discovery | "Quero abrir o discovery de X." |
| Benchmark | "Abra a rodada 1 do benchmark com os concorrentes A, B e C." |
| Roteiro | "Prepare o roteiro da entrevista com a Engenharia amanhã, 45 minutos." |
| Registrar entrevista | "Segue a transcrição da entrevista com <perfil> da área Y." (anexe ou cole) |
| Chamados | "Segue a exportação de chamados do suporte." (anexe a planilha) |
| Decidir algo | "Decidi que o produto será vendido como módulo." |
| Situação | "Onde estamos?" |
| Decisão | "Monte a matriz de decisão." |
| Relatório | "Faça o relatório final do discovery." |
| PRD | "Escreva o PRD. Segue o modelo da empresa." |

Depois de cada documento novo, o Claude envia o link: adicione-o ao conhecimento do projeto para que as próximas conversas o encontrem.

## Personalize

- **Confidencialidade:** escreva suas regras nas instruções do projeto. Elas valem para todas as skills.
- **Critérios e pesos de decisão:** a proposta padrão está no enquadramento; ajuste na primeira aprovação.
- **Modelo de PRD e de relatório:** se a empresa tiver um, envie como exemplo quando chegar a hora.
- **Ajustar uma skill:** edite o SKILL.md em `skills/<nome>/`, compacte a pasta (a pasta inteira, não só o arquivo) e envie de novo.
