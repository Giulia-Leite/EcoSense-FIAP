# EcoSense — Central Inteligente de Monitoramento Ambiental Comunitário

## Disciplina
Computational Thinking for Engineering — Engenharia de Computação, 1º ano.

## Integrantes
- Giulia Leite — RM:570641

## Ambiente escolhido
Sala de aula de uma escola.

## Objetivo
Simular uma central de monitoramento ambiental que recebe valores de temperatura, concentração de PM2,5 e nível de ruído. O sistema compara as leituras com referências definidas, emite alertas, calcula estatísticas, classifica a sequência e salva um relatório `.txt`.

## Limites de referência adotados
- **Temperatura:** 18 a 25 °C. Referência operacional baseada na NR-17, item 17.8.4.2, para ambientes climatizados de trabalho. É usada como parâmetro didático no projeto, não como certificação de conforto para estudantes.
- **PM2,5:** até 15 µg/m³, considerando média de 24 horas, conforme Diretrizes Globais de Qualidade do Ar da OMS (2021). Cada valor digitado deve representar uma média de 24 horas.
- **Ruído:** até 35 dB como valor de referência para sala de aula (RLAeq), conforme ABNT NBR 10152:2017. Para esta atividade, a média aritmética dos valores informados é apresentada como estatística descritiva simplificada, conforme o enunciado.

As leituras são simuladas manualmente. Os resultados não substituem medições técnicas ou avaliação ambiental.

## Fontes
1. Ministério do Trabalho e Emprego — NR-17: https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-paritaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-17-nr-17
2. Organização Mundial da Saúde — WHO Global Air Quality Guidelines (2021): https://www.who.int/publications/i/item/9789240034228
3. ProAcústica — Manual para Qualidade Acústica em Escolas (referência à ABNT NBR 10152:2017): https://www.proacustica.org.br/assets/files/Manuais/ProAcustica-ManualEscolas-Abr2019.pdf

## Como executar
1. Instale o Python 3.
2. Baixe o arquivo `ecosense.py`.
3. Abra o terminal na pasta do arquivo.
4. Execute:

```bash
python ecosense.py
```

O programa solicita a quantidade de leituras e, para cada uma, temperatura, PM2,5 (média de 24 horas) e ruído representativo. Ao final, exibe os resultados e cria `relatorio_ecosense.txt` na mesma pasta. O usuário pode iniciar outra sequência sem fechar o programa.

## Funcionalidades implementadas
- Entrada validada de quantidade de leituras e valores numéricos.
- Armazenamento em lista de dicionários, mantendo os três valores agrupados por leitura.
- Verificação independente dos parâmetros e emissão de alertas múltiplos.
- Contagem de ocorrências críticas por parâmetro.
- Contagem única de cada leitura crítica, mesmo que apresente mais de um alerta.
- Média, máximo e mínimo para os três parâmetros.
- Percentual de leituras críticas e classificação geral pelo critério de mais de 30%.
- Geração de relatório TXT e opção de nova análise com reinicialização dos dados.


