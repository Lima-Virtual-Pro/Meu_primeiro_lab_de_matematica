# Relatório de QA — V3.0

**Data:** 11/10/2026  
**Titular:** Nailson Rodrigues de Lima  
**Escopo:** execução técnica do aplicativo HTML standalone e revisão matemática automatizada do banco gerado.

## Resultados executados

- **2.400/2.400 gabaritos conferidos** com um verificador matemático independente escrito em Python. O verificador interpreta cada enunciado, calcula o resultado e o confronta com a alternativa marcada correta. Também checa quatro alternativas textualmente distintas, enunciados únicos por missão, pistas e explicações.
- **30/30 verificações funcionais de navegador aprovadas** usando Chromium automatizado e Playwright: interface, 24 missões, 66 conceitos, logo integrada, aceite, controles de acessibilidade, correção, navegação, tutor, laboratório, biblioteca, salvamento opcional, exportação, erros JavaScript e viewport móvel sem rolagem horizontal.
- **13/13 verificações de jornada aprovadas:** rodada completa de dez acertos, conclusão, armazenamento opt-in, exportação e importação JSON, reinício, supressão das chaves legadas, salvamento após importação e retomada em reinicialização simulada.
- **Total de 43 verificações funcionais/jornada aprovadas**, além da conferência individual de 2.400 respostas.

## Método e limitações

O ambiente de automação bloqueou navegação direta `file://` por uma política administrativa. Foi utilizado o HTML inserido diretamente na página com `set_content` e um `localStorage` simulado em memória. A persistência foi testada em **reabertura simulada**, não fechando e abrindo um arquivo local real. A função de voz foi implementada com API do navegador, mas a produção sonora em hardware real não foi validada. Também não foram feitos testes completos de leitor de tela, auditoria WCAG, todos os navegadores, acessibilidade infantil, estudo com estudantes ou validação curricular por série.

As questões foram validadas quanto ao gabarito por cálculo independente, **não quanto à eficácia educacional**, adequação a uma série específica ou avaliação de público real. Conteúdo e documentos contratuais dependem de revisão pedagógica e jurídica para implantação institucional/comercial.

## Casos reproduzíveis

| Caso | Entrada | Comportamento esperado | Observado |
|---|---|---|---|
| Carregar aplicativo | Abrir interface | 24 missões, 2.400 questões, 66 conceitos | Aprovado no Chromium automatizado |
| Fração | Resolver 1/2 + 1/3 | 5/6 e passos corretos | Aprovado |
| MMC | `MMC(6,8)` | 24 com explicação | Aprovado |
| Nova matéria | Missão de perímetro | Desenho de retângulo; 100 questões | Aprovado |
| Resposta errada | Selecionar alternativa incorreta | Correção comentada | Aprovado |
| Revisão | Responder questões | Indicador por missão | Aprovado |
| Salvar | Ativar salvamento local | Chave local V3 | Aprovado com shim |
| Retomar | Recarregar HTML com mesma memória simulada | Conquistas recuperadas | Aprovado em simulação |
| Importar | JSON de progresso exportado | Recuperar métricas | Aprovado |
| Resetar | Confirmar reinício | Limpar progresso V2 e V3 | Aprovado |
| Mobile | 390 × 844 | Menu acessível sem corte horizontal | Aprovado |
| Voz | Clicar “Ouvir” | Solicitar síntese em navegador compatível | **Pendente de teste de áudio real** |
| Acessibilidade | Leitor de tela/teclado em dispositivo real | Fluxos acessíveis | **Pendente de homologação** |

Reproduza os testes no diretório: `python qa_math.py`, `python qa_browser.py`, `python qa_round.py`; exigem Node, Python, Playwright e Chromium somente para o desenvolvimento, não para o usuário final. Relatórios JSON são fornecidos no pacote.
