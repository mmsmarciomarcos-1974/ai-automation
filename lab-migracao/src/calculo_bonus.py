def calcular_bonus_fidelidade(salario: float, anos_casa: int) -> float:
    """
    Calcula o bônus do funcionário baseado no tempo de empresa.
    Regra (vinda do COBOL): 
    - > 10 anos: 15%
    - > 5 anos: 10%
    - Até 5 anos: 5%
    """
    if anos_casa > 10:
        fator = 0.15
    elif anos_casa > 5:
        fator = 0.10
    else:
        fator = 0.05
    
    return round(salario * fator, 2)