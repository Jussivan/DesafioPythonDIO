def calcular_metricas(VP, VN, FP, FN):

    acuracia = (VP + VN) / (VP + VN + FP + FN)

    sensibilidade = VP / (VP + FN)

    especificidade = VN / (VN + FP)

    precisao = VP / (VP + FP)

    if (precisao + sensibilidade) > 0:
        F1 = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)
    else:
        F1 = 0

    return {
        'Acurácia': acuracia,
        'Sensibilidade': sensibilidade,
        'Especificidade': especificidade,
        'Precisão': precisao,
        'F-score': F1
    }
matriz_confusao = {
    'VP': 50,
    'VN': 30,
    'FP': 10,
    'FN': 10
}

resultados = calcular_metricas(matriz_confusao['VP'], matriz_confusao['VN'], matriz_confusao['FP'], matriz_confusao['FN'])
print(resultados)
