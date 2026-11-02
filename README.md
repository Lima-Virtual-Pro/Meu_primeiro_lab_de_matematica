# Meu Primeiro Laboratório de Matemática — versão 3.0

**Autor e titular dos direitos:** Nailson Rodrigues de Lima. © 2026. Todos os direitos reservados.

## Comece pelo arquivo index.html

O arquivo `index.html` é a versão **standalone** e reúne o código, os estilos, a logomarca e o banco gerado no navegador. Não exige instalação, bibliotecas, cadastro, token, Internet ou servidor para as funções educativas principais. Abra o arquivo em um navegador atualizado.

## O que está implementado

- **24 missões**: 16 de frações e 8 de operações, raciocínio, medidas, geometria e problemas cotidianos.
- **2.400 exercícios distintos**: 100 questões em cada missão, 20 de nível inicial, 40 intermediárias e 40 de desafio. São sorteadas **10 questões por rodada**, com correção e pista. Os conjuntos são gerados localmente a partir de regras determinísticas.
- **66 verbetes de biblioteca local**, com busca por tema ou palavra.
- **Prof. Lume:** tutor determinístico, orientado por regras e calculadora de frações, operações básicas, MMC, MDC, área e perímetro; explica erros recentes, indica revisões e admite entradas não reconhecidas. Não é um modelo de linguagem treinado nem consulta a Internet.
- **Plano de revisão**: usa taxas de acerto para indicar missão a reforçar. Desempenho é indicador pedagógico, não diagnóstico.
- **Laboratório de frações**: círculo, barra e reta numérica. Novas aulas de Matemática recebem desenhos específicos.
- **Acessibilidade:** ajuste de tamanho de texto, alto contraste, navegação por teclado, etiquetas semânticas e comando de leitura por voz quando suportado pelo sistema/navegador. Não equivale a auditoria formal WCAG.
- **Dados:** perguntas ao tutor só permanecem em memória; progresso e aceites podem ser salvos no navegador conforme a função; importação/exportação JSON permite transporte manual entre dispositivos.
- **Documentação:** Termos de Uso, Política de Privacidade e Contrato de Uso em janelas da aplicação, com aceite local de adulto ou responsável legal.

## Publicação para ampliar o alcance

A versão HTML pode ser hospedada como arquivo estático em hospedagem HTTPS. Basta publicar `index.html` como página inicial (poderá ser renomeado para `index.html` no diretório principal) e testar a leitura por voz, armazenamento local, acessibilidade e largura de tela na hospedagem escolhida. O domínio/hospedagem pode produzir seus próprios registros técnicos, mesmo que o código da aplicação não envie perguntas para servidores; antes de publicar, revisar a política de privacidade.

**Atenção:** não foram implementados contas de estudantes, estatísticas globais, sincronização entre dispositivos, autenticação de responsável, assinaturas digitais qualificadas, recomendação por IA generativa ou backend. Esses recursos exigiriam infraestrutura, testes adicionais e novos cuidados com dados de menores.

## Arquivos no pacote

`index.html`: aplicativo. `app.js` e `style.css`: código separado para consulta/desenvolvimento (o HTML standalone já possui ambos internamente). `logomarca.png`: logomarca. `banco_questoes_2400.json`: espelho do banco para auditoria, não necessário na execução. `MANUAL.md`, `TERMOS_DE_USO.md`, `POLITICA_DE_PRIVACIDADE.md`, `CONTRATO_DE_USO.md`, `QA.md`: instruções e minutas. `qa_browser.py`, `qa_round.py`, `qa_math.py`: testes reproduzíveis em um ambiente de desenvolvimento com Python/Playwright/Chromium/Node; não necessários para executar o aplicativo.

O campo de copyright não representa depósito ou registro de marca. Avaliar a disponibilidade comercial do nome e a identidade visual antes de vender ou publicar amplamente.
