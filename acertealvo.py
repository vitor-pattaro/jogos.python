import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da Janela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Acerte o Alvo!')

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Fonte
fonte = pygame.font.SysFont("bahnschrift", 35)

# O Alvo
TAMANHO_ALVO = 50
# Cria um retângulo para o alvo em uma posição inicial
alvo_rect = pygame.Rect(375, 275, TAMANHO_ALVO, TAMANHO_ALVO) # (x, y, largura, altura)

# Variáveis do Jogo
pontos = 0
relogio = pygame.time.Clock()
rodando = True

while rodando:
    # --- 1. Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        
        # Verifica se o evento foi um clique do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 'event.pos' é a coordenada (x, y) do clique
            # 'collidepoint' checa se o ponto (o clique) está dentro do rect
            if alvo_rect.collidepoint(event.pos):
                # Move o alvo para uma nova posição aleatória
                alvo_rect.x = random.randrange(0, LARGURA_TELA - TAMANHO_ALVO)
                alvo_rect.y = random.randrange(0, ALTURA_TELA - TAMANHO_ALVO)
                # Adiciona um ponto
                pontos += 1

    # --- 2. Lógica do Jogo ---
    # (Nenhum, o jogo é 100% baseado em eventos)

    # --- 3. Desenho ---
    tela.fill(PRETO)
    
    # Desenha o alvo
    pygame.draw.rect(tela, VERMELHO, alvo_rect)
    
    # Desenha a pontuação
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))
    
    # --- 4. Atualização ---
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()