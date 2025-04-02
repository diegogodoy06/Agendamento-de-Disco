# Algoritmo de Agendamento de Disco com Python

[![Python Version](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)

Uma implementação interativa que demonstra os algoritmos de agendamento de discos **FCFS**, **SSTF**, **SCAN** e **C-SCAN** utilizando Python e a biblioteca [matplotlib](https://matplotlib.org/).

---

## Sumário

- [Introdução](#introdução)
- [Recursos](#recursos)
- [Descrição do Projeto](#descrição-do-projeto)
- [Requisitos](#requisitos)
- [Instalação e Execução](#instalação-e-execução)

---

## Introdução

Este projeto foi desenvolvido para ilustrar como diferentes algoritmos de agendamento de disco podem ser implementados e visualizados. Através de gráficos gerados com matplotlib, é possível observar o caminho percorrido pelo braço do disco durante a execução dos algoritmos.

---

## Recursos

- **Visualização Interativa:** Geração de gráficos que exibem a ordem de atendimento dos pedidos.
- **Cálculo de Movimentos:** Função que soma a distância total percorrida pelo braço do disco.
- **Implementação de Algoritmos:** Inclui os métodos FCFS, SSTF, SCAN e C-SCAN para comparação.

---

## Descrição do Projeto

O script está organizado da seguinte forma:

- **Implementação dos Algoritmos:**
  - `fcfs(requests, start)`: Atende os pedidos na ordem de chegada.
  - `sstf(requests, start)`: Escolhe o pedido mais próximo da posição atual.
  - `scan(requests, start, end)`: Move o braço até o final e depois inverte o sentido.
  - `cscan(requests, start, end)`: Realiza uma varredura circular, retornando ao início após alcançar o final.

- **Cálculo dos Movimentos:**
  - `calculate_movements(sequence)`: Calcula o total de movimentos realizados entre os acessos.

- **Visualização dos Resultados:**
  - `plot_schedule(title, sequence)`: Plota a sequência de atendimento com detalhes dos movimentos.

---

## Requisitos

- **Python 3.x**
- **Bibliotecas:**
  - [matplotlib](https://matplotlib.org/)
  - [numpy](https://numpy.org/)

---

## Instalação e Execução

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/diegogodoy06/Agendamento-de-Disco

1. **Instale as dependências:**

   ```bash
    pip install matplotlib numpy

1. **Execute o script:**

   ```bash
    python agendador.py