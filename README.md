# Conversor de Temperatura

Um utilitário de linha de comando simples e eficiente para conversão entre diferentes escalas de temperatura, escrito em Python.

## Funcionalidades

- Conversão entre Celsius, Fahrenheit e Kelvin
- Interface de linha de comando intuitiva
- Validação de entradas
- Cálculos precisos baseados nas fórmulas padrão de conversão

## Requisitos

- Python 3.x

## Instalação

Clone este repositório ou baixe os arquivos para sua máquina:

```bash
git clone https://github.com/seu-usuario/conversor-temperatura.git
cd conversor-temperatura
```

## Como usar

O conversor funciona através de linha de comando utilizando flags para indicar os parâmetros necessários:

```bash
python conversor.py --entrada <escala_origem> --saida <escala_destino> --numero <valor>
```

### Parâmetros

- `--entrada`: Escala de temperatura de origem (celcius, fahrenheit, kelvin)
- `--saida`: Escala de temperatura de destino (celcius, fahrenheit, kelvin)
- `--numero`: Valor numérico da temperatura a ser convertida

### Exemplos

Converter 40 graus Celsius para Fahrenheit:
```bash
python conversor.py --entrada celcius --saida fahrenheit --numero 40
```
Resultado: 104.0

Converter 98.6 graus Fahrenheit para Celsius:
```bash
python conversor.py --entrada fahrenheit --saida celcius --numero 98.6
```
Resultado: 37.0

Converter 300 Kelvin para Celsius:
```bash
python conversor.py --entrada kelvin --saida celcius --numero 300
```
Resultado: 26.85

## Como funcionam as conversões

O programa utiliza um sistema de conversão em duas etapas:

1. Primeiro, converte a temperatura de entrada para Celsius (temperatura intermediária)
2. Depois, converte de Celsius para a escala de saída desejada

### Fórmulas utilizadas

**Conversão para Celsius:**
- De Celsius: `C = C` (mantém o mesmo valor)
- De Fahrenheit: `C = (F - 32) × 5/9`
- De Kelvin: `C = K - 273.15`

**Conversão de Celsius para outras escalas:**
- Para Celsius: `C = C` (mantém o mesmo valor)
- Para Fahrenheit: `F = (C × 9/5) + 32`
- Para Kelvin: `K = C + 273.15`

## Estrutura do código

O conversor utiliza funções lambda dentro de dicionários para armazenar as fórmulas de conversão, tornando o código conciso e fácil de manter:

```python
CONVERSAO_PARA_CELCIUS = {
    "celcius": lambda x: x,
    "fahrenheit": lambda x: (x - 32) * 5 / 9,
    "kelvin": lambda x: x - 273.15
}

CONVERTE_DE_CELCIUS_PARA_OUTRAS = {
    "celcius": lambda x: x,
    "fahrenheit": lambda x: (x * 9 / 5) + 32,
    "kelvin": lambda x: x + 273.15
}
```

## Tratamento de erros

O programa valida todas as entradas do usuário e exibe mensagens de erro claras quando:
- Parâmetros obrigatórios estão faltando
- A escala de temperatura não é reconhecida
- O valor informado não é um número

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

## Licença

[MIT](LICENSE)