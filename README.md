# 🤖 Agente: Mainframe Modernization Assistant

Este diretório contém os prompts e configurações do agente de IA que desenvolvi para acelerar a modernização de sistemas legados.

**Objetivo:** Atuar como um par programador que traduz z/OS (Cobol, JCL) para arquitetura de nuvem (AWS, Python).

---

## 🚀 Demonstração Prática

### 1. Entrada (Código Legado - COBOL)
*Trecho de lógica para cálculo de bonificação.*

```cobol
       IF WRK-ANOS-CASA > 10 THEN
           COMPUTE WRK-BONUS = WRK-SALARIO * 0.15
       ELSE
           IF WRK-ANOS-CASA > 05 THEN
               COMPUTE WRK-BONUS = WRK-SALARIO * 0.10
           ELSE
               COMPUTE WRK-BONUS = WRK-SALARIO * 0.05
           END-IF
       END-IF.

Saída do Agente (Modernização Python)

O agente identifica a regra de progressão e gera código Python tipado e documentado.      

def calcular_bonus_fidelidade(salario: float, anos_casa: int) -> float:
    """
    Calcula o bônus do funcionário baseado no tempo de empresa.
    Regra: > 10 anos (15%), > 5 anos (10%), outros (5%).
    """
    if anos_casa > 10:
        fator = 0.15
    elif anos_casa > 5:
        fator = 0.10
    else:
        fator = 0.05
    
    return round(salario * fator, 2)

# 🛡️ Agente: Quality Guardian

Este agente atua como um Engenheiro de Qualidade de Software (QA), gerando testes unitários automáticos para blindar o código modernizado.

**Stack:** Python + Unittest

## Fluxo de Trabalho
1.  **Entrada:** Código Python (gerado pelo Agente Modernizer).
2.  **Processamento:** O Quality Guardian analisa "Caminhos Felizes" e "Casos de Borda" (Edge Cases).
3.  **Saída:** Script de teste completo pronto para rodar na pipeline.

## Exemplo de Saída (Análise)
> **Casos de Borda Identificados:**
> - Salário negativo ou zero.
> - Anos de casa negativo.
> - Tipos de dados inválidos (string em vez de int).

---