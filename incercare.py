import pygame
import random
import math

# pornim pygame
pygame.init()

# dimensiuni fereastră
WIDTH = 1280
HEIGHT = 720

# creare fereastră
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# titlu joc
pygame.display.set_caption("jocul testului")

# clock pentru FPS
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 69)
game_over_font = pygame.font.SysFont("Arial", 200, bold=True)

# player
player_x = 400
player_y = 300

player_size = 60
player_speed = 6
enemies = []

enemy_size = 40
enemy_speed = 4
spawn_timer = 0
spawn_delay = 400
player_hp = 100
damage = 0.5
enemy_x = random.randint(0, WIDTH)
enemy_y = random.randint(0, HEIGHT)

enemies.append([enemy_x, enemy_y])

# game loop
running = True

while running:

    # 60 FPS
    clock.tick(60)
    spawn_timer += 1

    # verificăm evenimente
    for event in pygame.event.get():

        # închidere fereastră
        if event.type == pygame.QUIT:
            running = False

    # taste apăsate
    keys = pygame.key.get_pressed()

    # mișcare
    if keys[pygame.K_UP]:
        player_y -= player_speed

    if keys[pygame.K_DOWN]:
        player_y += player_speed

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if keys[pygame.K_w]:
        player_y -= player_speed

    if keys[pygame.K_s]:
        player_y += player_speed

    if keys[pygame.K_a]:
        player_x -= player_speed

    if keys[pygame.K_d]:
        player_x += player_speed
    # limite ecran

    if player_x < 0:
        player_x = 0

    if player_x > WIDTH - player_size:
        player_x = WIDTH - player_size

    if player_y < 0:
        player_y = 0

    if player_y > HEIGHT - player_size:
        player_y = HEIGHT - player_size

    # culoare fundal
    # mișcare inamici

    for enemy in enemies:

        dx = player_x - enemy[0]
        dy = player_y - enemy[1]

        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance != 0:
            dx = dx / distance
            dy = dy / distance

        enemy[0] += dx * enemy_speed
        enemy[1] += dy * enemy_speed
    # spawn inamici noi

    if spawn_timer >= spawn_delay:
        enemy_x = random.randint(0, WIDTH)
        enemy_y = random.randint(0, HEIGHT)

        enemies.append([enemy_x, enemy_y])

        spawn_timer = 0
    screen.fill((30, 30, 30))

    # desenăm playerul
    pygame.draw.rect(
        screen,
        (128, 189, 97),
        (player_x, player_y, player_size, player_size)
    )
    # desenare inamici

    for enemy in enemies:
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (enemy[0], enemy[1], enemy_size, enemy_size)
        )
        # coliziune cu playerul

        if (
                player_x < enemy[0] + enemy_size and
                player_x + player_size > enemy[0] and
                player_y < enemy[1] + enemy_size and
                player_y + player_size > enemy[1]
        ):
            player_hp -= damage

    # actualizare ecran
    # text HP

    hp_text = font.render(
        f"HP: {player_hp}",
        True,
        (255, 255, 255)
    )

    screen.blit(hp_text, (20, 20))

#ICONITA
    '''icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)'''
    # game over

    if player_hp <= 0:
        game_over_text = game_over_font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )
        text_rect = game_over_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        screen.blit(game_over_text, text_rect)

        pygame.display.update()

        pygame.time.delay(3000)

        running = False
    pygame.display.update()

# închidem pygame
pygame.quit()
