---
name: discovery-entrevista
description: Consolida uma entrevista de discovery (interna, com cliente ou com especialista) a partir de transcrição automática, notas geradas por IA, anotações ou áudio transcrito, separando fato, inferência e opinião, atribuindo cada fala, testando hipóteses e registrando o que ficou sem resposta; depois propaga o resultado para andamento, mapa de requisitos e pendências. Use sempre que o usuário enviar transcrição, ata, resumo, notas ou gravação de uma conversa do discovery, ou disser "segue a entrevista com...", "consolida essa reunião", "registra essa conversa".
---

# Consolidar uma entrevista

A consolidação transforma uma conversa em evidência rastreável. O risco principal é transformar opinião em fato ou nota de IA em citação. Este procedimento existe para evitar isso.

## 1. Identifique a fonte e rotule

| Tipo de fonte | Como rotular | Cuidado |
|---|---|---|
| Gravação transcrita por pessoa | Transcrição revisada | Pode citar entre aspas |
| Transcrição automática | "Transcrição automática, termos a conferir" | Nomes, siglas e números costumam vir errados; liste correções na seção de termos |
| Notas ou resumo gerados por IA | "Notas geradas por IA, a verificar com a gravação" | **Não é fala literal.** Nada entre aspas como citação |
| Anotações do entrevistador | "Anotações de <quem>" | Registre o que é lembrança |
| Relato do responsável sobre uma reunião sem ata | "Relato de <quem>, sem ata" | Tudo é [F] sobre o relato, não sobre a reunião |

Se faltar data, duração, participantes ou roteiro usado, pergunte. Se não houver resposta, registre "a confirmar".

## 2. Numere

- **Número da entrevista** (01, 02, 03...) segue a ordem de realização, independente da pasta.
- **Nome do documento** segue a numeração da pasta Entrevistas: `NN-entrevista-XX-<perfil-ou-nome>`. Ex.: `07-entrevista-04-engenharia`.
- Para entrevistado externo cujo empregador é confidencial, use perfil no nome do arquivo (ex.: `entrevista-03-especialista-externo`) e decida com o responsável.

## 3. Redija a consolidação

Use `assets/modelo-consolidacao-entrevista.md`. Seções:

1. **Cabeçalho:** etapa, número, status Rascunho, data e duração, roteiro usado, fonte e rótulo.
2. **Legenda:** [F] fato dito pelo entrevistado; [O] opinião ou estimativa dele; [I] inferência do Claude.
3. **Participantes** com papel e observação (quem fez as estimativas, quem falou de estratégia).
4. **Resumo em 5 a 8 pontos**, cada um marcado.
5. **Blocos por tema do roteiro**, em tabela "tema | o que foi dito | tipo". Ao fim de cada bloco, uma "Leitura [I]" curta conectando com outras fontes.
6. **Números e estimativas** em tabela com premissa e confiança. Estimativa de cabeça em reunião é [O] com confiança baixa, mesmo vinda de liderança.
7. **Informações novas que mudam o escopo** (fonte e efeito).
8. **Qualidade da transcrição e termos:** "transcrito como" → "interpretado como", com "confirmar" quando houver dúvida.
9. **Hipóteses:** tabela hipótese | resultado desta entrevista (apoia, contraria, parcial, não trata). Proponha hipótese nova só como "proposta, aguardando decisão".
10. **O que ficou sem resposta do roteiro** (pergunta e situação). Lacunas importantes em negrito.
11. **Próximos passos** (para o responsável e para o Claude).
12. **Riscos desta fonte:** viés (quem vende, quem constrói, quem prefere uma opção), amostra (uma ou duas pessoas), porte ou setor diferente do público-alvo.
13. **Verificação** no fim.

## 4. Regras de escrita

- Atribua cada afirmação a uma pessoa. "A Engenharia disse" só se todos concordaram; senão, nome ou cargo.
- Contradição com entrevista anterior: registre como **tensão** e não resolva sozinho ("Fonte A considera essencial; fonte B não incluiria. Decidir com clientes.").
- Não suavize nem amplifique. Frases fortes de opinião (ex.: "isso não tem futuro") ficam como [O] com aviso de cuidado em material compartilhado.
- Confidencial do entrevistado (empregador, sistemas internos, clientes dele): registre o que foi autorizado e marque o resto como "não citar em material externo".
- Dados pessoais e credenciais que apareçam na transcrição não são reproduzidos.

## 5. Propague (obrigatório)

Siga a skill `discovery-atualizar`, ou, se não estiver disponível, faça:
1. **Andamento:** tabela de entrevistas, situação da etapa, hipóteses (evidência e força), achados da entrevista, riscos.
2. **Mapa de requisitos:** cada requisito citado ganha a sigla da fonte; itens novos entram como R, N ou X; recalcule o número de fontes independentes; registre tensões numa "Atualização de DD/MM".
3. **Registro de pendências:** perguntas a confirmar com o responsável (W) e tarefas do Claude (C), com ID e data.
4. **Log de decisões:** só se o responsável decidiu algo na mensagem.
5. Envie o link do documento novo e liste o que precisa de revisão.
