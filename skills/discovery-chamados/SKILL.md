---
name: discovery-chamados
description: Consolida chamados de suporte (tickets de helpdesk exportados em planilha ou CSV) para um discovery de produto (Etapa 4) - recorte do escopo, números calculados por script, tempos e SLA, classificação por tema, padrões de retrabalho, melhorias pedidas e o que os chamados não dizem, reconciliando com entrevistas. Use sempre que o usuário enviar exportação de chamados, tickets, planilha do suporte, base de reclamações ou pedidos de melhoria, ou pedir para analisar o atrito do produto atual a partir do suporte.
---

# Consolidar chamados de suporte (Etapa 4)

Chamados mostram onde o produto atual gera atrito. Eles **não** mostram demanda por funções novas nem disposição a pagar. Dizer isso no documento evita conclusões erradas.

## Regras

- **Todo número vem de script**, nunca de contagem manual. Registre o método.
- **Reconcilie** com outras fontes (ex.: a entrevista citou um total e a planilha mostra outro: registre os dois e a provável causa).
- **Classificação por tema é [I]** do Claude e precisa de revisão do responsável.
- **Privacidade:** não reproduza nomes de pessoas, e-mails, telefones nem credenciais que apareçam nas descrições. Nomes de empresas-clientes só em documento interno; nunca em material externo.
- Nova base mais completa = **nova versão** (`-v2`, `-v3`) com seção "O que mudou da versão anterior".

## Passo a passo

1. **Entenda a base:** arquivo, sistema de origem, total de linhas, período, colunas disponíveis. Pergunte como identificar os chamados do escopo (serviço, categoria, tag, módulo) se não for óbvio. Desconfie de exportações com limite de linhas: compare totais por mês para achar cortes.
2. **Recorte o escopo** e documente o filtro exato.
3. **Rode o script** `scripts/resumo_chamados.py` (ou equivalente) para obter: totais por ano e mês; por tipo, serviço/categoria, situação, urgência, origem e equipe; tempo até resolução (mediana e percentis, sem pedidos de melhoria); SLA dentro/fora do prazo por ano; top clientes por volume.
   ```
   python scripts/resumo_chamados.py chamados.xlsx --col-data "Aberto em" --col-fechamento "Resolvido em" \
     --col-tipo "Tipo" --col-categoria "Serviço" --col-cliente "Cliente" --filtro "Serviço=Módulo X" --saida resumo.md
   ```
   Use `--help` para ver as opções. Ajuste as colunas aos nomes da planilha.
4. **Classifique por tema** lendo assunto e descrição (amostra grande o bastante ou todos, se forem poucas centenas). Crie de 6 a 10 temas mutuamente exclusivos e um "Outros". Conte por script depois de rotular.
5. **Retrabalho e custo:** chamados que exigem script, correção em banco, intervenção da Engenharia, reabertura. Se houver histórico de ações (API do helpdesk), use uma amostra e diga o tamanho.
6. **Melhorias pedidas:** quantas, quais, quantas seguem no backlog.
7. **Redija** com `assets/modelo-consolidacao-chamados.md`.

## Estrutura do documento

0. O que mudou da versão anterior (se houver)
1. Resumo em poucas linhas
2. Base de dados e limitações (arquivos, filtros, conferência com entrevistas)
3. Visão geral em números (tipo, serviço, situação, tempos, SLA)
4. Temas: o que os clientes mais pedem e reclamam (com % e exemplos sem dados pessoais)
5. Padrões de retrabalho e custo de suporte
6. Melhorias pedidas
7. **O que os chamados não dizem** (demanda nova, disposição a pagar, uso real, clientes que não abrem chamado)
8. Leitura preliminar para a decisão (todas [I])
9. O que preciso de você para fechar a etapa
Anexos: chamados por tema (ID, data, assunto resumido); registro de execução; verificação.

## Depois

Atualize andamento (Etapa 4, achados, hipóteses de dor e de custo), mapa de requisitos (temas que viram requisitos candidatos, com sigla CH), pendências (revisar classificação; extrair histórico). Envie o link.
