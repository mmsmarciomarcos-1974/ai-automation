# Workflow com Gemini: Refinamento e Testes

Após gerar o código modernizado no StackSpot, utilizamos o Gemini para garantir a qualidade e criar cenários de teste (TDD).

## Prompt de Refinamento (Use no Gemini)

**Prompt:**
> "Atue como um Arquiteto de Software. Eu tenho este código em Python [COLAR CÓDIGO GERADO PELO STACKSPOT] que foi traduzido de um legado COBOL.
>
> 1. Verifique se o código Python segue as pep-8.
> 2. Crie 3 casos de teste unitários usando `unittest` ou `pytest` para validar a regra de negócio descrita: [DESCREVER REGRA].
> 3. Sugira uma otimização de performance considerando que vamos processar grandes volumes de dados (Batch)."

## Benefício dessa abordagem
O StackSpot é excelente no contexto da IDE e da empresa, enquanto o Gemini atua como um validador externo de lógica e criador de cenários de teste criativos.
