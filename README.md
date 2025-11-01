
---

# Jogos em Python

Projeto criado por [Vítor Pattaro](https://github.com/vitor-pattaro)
Repositório: [https://github.com/vitor-pattaro/jogos.python/](https://github.com/vitor-pattaro/jogos.python/)

## Visão geral

Este repositório contém dois jogos simples desenvolvidos em Python utilizando a biblioteca Pygame:

1. Jogo de “Acerte o Alvo” (`acertealvo.py`)
2. Jogo de Pong (`pong.py`)

Estes jogos foram criados no contexto de um curso de programação em Python, como forma de praticar conceitos de lógica, eventos, desenho de tela e interatividade.

## Pré-requisitos

Antes de executar os jogos, verifique se você tem:

* Python instalado (versão 3.x)
* A biblioteca Pygame instalada

Você pode instalar o Pygame via pip:

```bash
pip install pygame
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/vitor-pattaro/jogos.python/
cd jogos.python
```

### 2. Executar o jogo “Acerte o Alvo”

```bash
python acertealvo.py
```

Siga as instruções dentro do jogo para mirar e acertar o alvo.

### 3. Executar o jogo Pong

```bash
python pong.py
```

Use as teclas indicadas (por exemplo, setas ou W/S) para mover a raquete e jogar contra oponente ou IA (dependendo da versão).

## Estrutura dos arquivos

| Arquivo         | Descrição                                      |
| --------------- | ---------------------------------------------- |
| `acertealvo.py` | Jogo onde o objetivo é mirar e acertar um alvo |
| `pong.py`       | Versão simples do clássico jogo Pong           |

## Como funciona cada jogo

### “Acerte o Alvo”

* Você vê um alvo na tela que se move ou aparece em posições diferentes.
* Seu objetivo é usar o mouse ou teclado (conforme implementado) para atirar ou clicar exatamente no alvo.
* Pontuação e tempo podem ser contabilizados (dependendo da implementação).
* Ideal para praticar coordenação visual, lógica de colisão e eventos de mouse/teclado.

### Pong

* Uma ou duas raquetes se movem verticalmente nas laterais da tela.
* Uma bola se move e quica nas bordas; se passar da raquete do adversário, ponto para você.
* Controles típicos:

  * Jogador 1: tecla W (subir), tecla S (descer)
  * Jogador 2: setas cima/baixo
* Pode incluir modo para dois jogadores ou jogador vs computador.

## Possíveis melhorias futuras

* Adicionar som e efeitos visuais mais elaborados.
* Incluir menus de início, pausa e fim de jogo.
* Salvar recordes de pontuação.
* Implementar níveis de dificuldade ou diferentes modos de jogo.
* Refatorar código para modularização e uso de classes.

## Contribuições

Fique à vontade para contribuir! Você pode:

* Reportar **issues** com bugs ou sugestões.
* Enviar **pull requests** com novas funcionalidades ou melhorias.
* Dar **stars** ou **forks** no repositório para apoiar o projeto.

---
