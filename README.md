## 🚀 Demonstração Prática: COBOL para Python

Abaixo, demonstro como o **Agente de Modernização** (configurado no StackSpot/Gemini) processa uma regra de negócio legada.

### 1. Entrada (Código Legado - COBOL)
*Trecho de um subprograma de cálculo de bonificação por tempo de casa.*

```cobol
       WORKING-STORAGE SECTION.
       01  WRK-SALARIO           PIC 9(05)V99.
       01  WRK-ANOS-CASA         PIC 9(02).
       01  WRK-BONUS             PIC 9(05)V99 VALUE ZEROS.

       PROCEDURE DIVISION.
           IF WRK-ANOS-CASA > 10 THEN
               COMPUTE WRK-BONUS = WRK-SALARIO * 0.15
           ELSE
               IF WRK-ANOS-CASA > 05 THEN
                   COMPUTE WRK-BONUS = WRK-SALARIO * 0.10
               ELSE
                   COMPUTE WRK-BONUS = WRK-SALARIO * 0.05
               END-IF
           END-IF.
. Saída do Agente (Análise e Modernização)
O Agente processa o código acima e gera a seguinte documentação e implementação:

🧠 Análise de Negócio
O código implementa uma política de bonificação progressiva baseada na fidelidade do colaborador:

Mais de 10 anos: Bônus de 15% sobre o salário.

Entre 6 e 10 anos: Bônus de 10%.

Até 5 anos: Bônus de 5%.

🐍 Implementação Sugerida (Python)
Código gerado seguindo boas práticas (Type Hinting e Docstrings).
def calcular_bonus_fidelidade(salario: float, anos_casa: int) -> float:
    """
    Calcula o bônus do funcionário baseado no tempo de empresa.
    
    Regra:
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

# Exemplo de uso (Teste Rápido)
if __name__ == "__main__":
    print(f"Bônus (12 anos): {calcular_bonus_fidelidade(5000.00, 12)}") # Esperado: 750.00

☁️ Sugestão de Arquitetura (AWS)
Para processar isso em lote (Batch) na nuvem:

Ingestão: Arquivo de entrada (CSV/JSON) carregado no S3.

Processamento: AWS Lambda (para volumes menores) ou AWS Glue (PySpark) aplicando a função calcular_bonus_fidelidade.

Persistência: Gravar resultados no Amazon RDS ou DynamoDB.
