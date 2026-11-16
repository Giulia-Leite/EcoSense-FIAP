# EcoSense - Central Inteligente de Monitoramento Ambiental Comunitario
# Disciplina: Computational Thinking for Engineering - FIAP
# Aluna: Giulia Leite - RM: 570641
# Ambiente de referencia: sala de aula de uma escola.
# O programa simula leituras informadas manualmente pelo usuario.
#
# LIMITES ADOTADOS (referencias para esta simulacao):
# 1) Temperatura: 18 a 25 °C.
#    Referencia: NR-17, item 17.8.4.2, do Ministerio do Trabalho e Emprego.
#    A faixa de 18 a 25 °C e indicada para ambientes climatizados de trabalho.
#    Neste projeto, ela e usada como referencia operacional para a sala de aula,
#    nao como certificacao de conforto ou seguranca para estudantes.
#    Fonte: https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/
#    participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-paritaria-permanente/
#    normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-17-nr-17
#
# 2) PM2,5: maximo de 15 µg/m³ para media de 24 horas.
#    Referencia: Diretrizes Globais de Qualidade do Ar da OMS (2021).
#    Cada valor de PM2,5 digitado deve representar uma media de 24 horas;
#    nao deve ser interpretado como uma medicao instantanea.
#    Fonte: https://www.who.int/publications/i/item/9789240034228
#
# 3) Ruido: maximo de referencia de 35 dB para sala de aula (RLAeq).
#    Referencia: ABNT NBR 10152:2017, tabela de valores para ambientes internos.
#    O valor representa nivel sonoro representativo do ambiente, e nao um pico
#    instantaneo. Para simplificar a atividade, o programa recebe esse valor
#    como um numero em dB e calcula media aritmetica, conforme o enunciado.
#    Fonte de apoio: Manual ProAcustica para Qualidade Acustica em Escolas:
#    https://www.proacustica.org.br/assets/files/Manuais/ProAcustica-ManualEscolas-Abr2019.pdf
#
# IMPORTANTE: Os limites sao parametros de referencia para uma simulacao
# academica. O resultado nao substitui medicao tecnica ou avaliacao ambiental.

AMBIENTE = "Sala de aula de uma escola"

TEMP_MIN = 18.0
TEMP_MAX = 25.0
PM25_MAX = 15.0
RUIDO_MAX = 35.0

def calcular_estatisticas(valores):
    soma = 0
    for valor in valores:
        soma += valor

    media = soma / len(valores)
    maior = max(valores)
    menor = min(valores)

    return media, maior, menor


def ler_numero(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Entrada invalida. Digite um numero, por exemplo: 23.5")


def ler_quantidade():
    while True:
        entrada = input("Quantas leituras deseja registrar? ").strip()
        try:
            quantidade = int(entrada)
            if quantidade > 0:
                return quantidade
            print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro maior que zero.")


def analisar_leitura(temperatura, pm25, ruido):
    alertas = []

    if temperatura < TEMP_MIN or temperatura > TEMP_MAX:
        alertas.append(
            f"Temperatura fora da faixa de referencia ({TEMP_MIN:.1f} a {TEMP_MAX:.1f} °C)."
        )

    if pm25 > PM25_MAX:
        alertas.append(
            f"Concentracao de PM2,5 acima do limite de {PM25_MAX:.1f} µg/m³."
        )

    if ruido > RUIDO_MAX:
        alertas.append(
            f"Nivel de ruido acima do valor de referencia de {RUIDO_MAX:.1f} dB."
        )

    return alertas


def coletar_leituras():
    quantidade = ler_quantidade()
    leituras = []

    for numero in range(1, quantidade + 1):
        print(f"\n--- LEITURA {numero} DE {quantidade} ---")

        temperatura = ler_numero("Temperatura (°C): ")
        pm25 = ler_numero("PM2,5 - media de 24h (µg/m³): ")
        ruido = ler_numero("Ruido representativo (dB): ")

        alertas = analisar_leitura(temperatura, pm25, ruido)

        leitura = {
            "numero": numero,
            "temperatura": temperatura,
            "pm25": pm25,
            "ruido": ruido,
            "alertas": alertas,
            "critica": len(alertas) > 0
        }
        leituras.append(leitura)

        if alertas:
            print("ALERTA:")
            for alerta in alertas:
                print("-", alerta)
        else:
            print("Leitura dentro dos limites de referencia estabelecidos.")

    return leituras


def gerar_resumo(leituras):
    temperaturas = []
    concentracoes = []
    ruidos = []

    ocorrencias_temperatura = 0
    ocorrencias_pm25 = 0
    ocorrencias_ruido = 0
    leituras_criticas = 0

    for leitura in leituras:
        temperaturas.append(leitura["temperatura"])
        concentracoes.append(leitura["pm25"])
        ruidos.append(leitura["ruido"])

        if leitura["temperatura"] < TEMP_MIN or leitura["temperatura"] > TEMP_MAX:
            ocorrencias_temperatura += 1
        if leitura["pm25"] > PM25_MAX:
            ocorrencias_pm25 += 1
        if leitura["ruido"] > RUIDO_MAX:
            ocorrencias_ruido += 1
        if leitura["critica"]:
            # Uma leitura com mais de um alerta conta apenas uma vez aqui.
            leituras_criticas += 1

    estatisticas = {
        "temperatura": calcular_estatisticas(temperaturas),
        "pm25": calcular_estatisticas(concentracoes),
        "ruido": calcular_estatisticas(ruidos)
    }

    total = len(leituras)
    percentual_critico = (leituras_criticas / total) * 100

    if percentual_critico > 30:
        classificacao = (
            "Estado geral: condicoes ambientais de atencao, com frequencia "
            "de ocorrencias acima do criterio estabelecido."
        )
    else:
        classificacao = (
            "Estado geral: frequencia de ocorrencias dentro do criterio "
            "estabelecido para a simulacao."
        )

    contagens = {
        "temperatura": ocorrencias_temperatura,
        "pm25": ocorrencias_pm25,
        "ruido": ocorrencias_ruido,
        "leituras_criticas": leituras_criticas,
        "percentual_critico": percentual_critico
    }

    return estatisticas, contagens, classificacao


def formatar_estatistica(nome, unidade, valores):
    media, maior, menor = valores
    return (
        f"{nome}:\n"
        f"  Media: {media:.2f} {unidade}\n"
        f"  Maior valor: {maior:.2f} {unidade}\n"
        f"  Menor valor: {menor:.2f} {unidade}\n"
    )


def salvar_relatorio(leituras, estatisticas, contagens, classificacao):
    nome_arquivo = "relatorio_ecosense.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATORIO - ECOSENSE\n")
        arquivo.write("=" * 55 + "\n")
        arquivo.write(f"Ambiente monitorado: {AMBIENTE}\n")
        arquivo.write(f"Quantidade de leituras: {len(leituras)}\n\n")

        arquivo.write("LIMITES DE REFERENCIA ADOTADOS\n")
        arquivo.write(f"Temperatura: {TEMP_MIN:.1f} a {TEMP_MAX:.1f} °C (NR-17, uso didatico)\n")
        arquivo.write(f"PM2,5: ate {PM25_MAX:.1f} µg/m³ (media de 24 horas, OMS 2021)\n")
        arquivo.write(f"Ruido: ate {RUIDO_MAX:.1f} dB (sala de aula, ABNT NBR 10152:2017)\n\n")

        arquivo.write("ESTATISTICAS\n")
        arquivo.write(formatar_estatistica("Temperatura", "°C", estatisticas["temperatura"]))
        arquivo.write(formatar_estatistica("PM2,5", "µg/m³", estatisticas["pm25"]))
        arquivo.write(formatar_estatistica("Ruido", "dB", estatisticas["ruido"]))

        arquivo.write("OCORRENCIAS CRITICAS POR PARAMETRO\n")
        arquivo.write(f"Temperatura: {contagens['temperatura']}\n")
        arquivo.write(f"PM2,5: {contagens['pm25']}\n")
        arquivo.write(f"Ruido: {contagens['ruido']}\n\n")

        arquivo.write("RESUMO DAS LEITURAS\n")
        arquivo.write(f"Leituras com pelo menos uma condicao critica: {contagens['leituras_criticas']}\n")
        arquivo.write(f"Percentual de leituras criticas: {contagens['percentual_critico']:.2f}%\n\n")

        arquivo.write("CLASSIFICACAO GERAL\n")
        arquivo.write(classificacao + "\n\n")

        arquivo.write("DETALHAMENTO DAS LEITURAS\n")
        for leitura in leituras:
            arquivo.write(f"\nLeitura {leitura['numero']}:\n")
            arquivo.write(f"  Temperatura: {leitura['temperatura']:.2f} °C\n")
            arquivo.write(f"  PM2,5: {leitura['pm25']:.2f} µg/m³\n")
            arquivo.write(f"  Ruido: {leitura['ruido']:.2f} dB\n")
            if leitura["alertas"]:
                for alerta in leitura["alertas"]:
                    arquivo.write(f"  ALERTA: {alerta}\n")
            else:
                arquivo.write("  Situacao: dentro dos limites de referencia.\n")

        arquivo.write("\nOBSERVACAO\n")
        arquivo.write(
            "Este relatorio apresenta uma simulacao baseada nos criterios e limites "
            "adotados pelo projeto. Nao representa certificacao de seguranca ambiental "
            "nem substitui avaliacao tecnica do espaco.\n"
        )

    return nome_arquivo


def exibir_resultados(estatisticas, contagens, classificacao, nome_arquivo):
    print("\n" + "=" * 55)
    print("RESUMO DA ANALISE - ECOSENSE")
    print("=" * 55)

    print(formatar_estatistica("Temperatura", "°C", estatisticas["temperatura"]))
    print(formatar_estatistica("PM2,5", "µg/m³", estatisticas["pm25"]))
    print(formatar_estatistica("Ruido", "dB", estatisticas["ruido"]))

    print("Ocorrencias criticas:")
    print(f"  Temperatura: {contagens['temperatura']}")
    print(f"  PM2,5: {contagens['pm25']}")
    print(f"  Ruido: {contagens['ruido']}")
    print(f"Leituras criticas: {contagens['leituras_criticas']}")
    print(f"Percentual de leituras criticas: {contagens['percentual_critico']:.2f}%")
    print("\n" + classificacao)
    print(f"\nRelatorio salvo em: {nome_arquivo}")


def executar_analise():
    leituras = coletar_leituras()
    estatisticas, contagens, classificacao = gerar_resumo(leituras)
    nome_arquivo = salvar_relatorio(
        leituras, estatisticas, contagens, classificacao
    )
    exibir_resultados(estatisticas, contagens, classificacao, nome_arquivo)


def main():
    print("=" * 55)
    print("ECOSENSE - CENTRAL DE MONITORAMENTO AMBIENTAL")
    print("=" * 55)
    print(f"Ambiente: {AMBIENTE}")
    print("Simulacao por entrada manual de dados.\n")

    continuar = "s"
    while continuar.lower() == "s":
        executar_analise()
        continuar = input("\nDeseja iniciar uma nova analise? (s/n): ").strip()

    print("\nPrograma encerrado. Obrigado por utilizar o EcoSense.")


if __name__ == "__main__":
    main()
