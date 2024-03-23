import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# Deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZOLTY = (255, 255, 0)

def draw_skewed_heptagon(surface, color, center, size, angle_offset, skew, vertical_offset, flatten, horizontal_flip, horizontal_offset=0):
    points = []
    for i in range(7):  
        angle = math.radians(51.4285714 * i + angle_offset)  # Kąt heptagonu
        x = center[0] + size * math.cos(angle) + skew * math.sin(angle) + horizontal_offset
        if horizontal_flip:
            x = 2 * center[0] - x  # Odwracanie horyzontalne
        y = (center[1] + size * math.sin(angle) + vertical_offset) * flatten
        points.append((x, y))
    pygame.draw.polygon(surface, color, points)


heptagon_size = 100
heptagon_angle = 0
skew = 0  # Początkowa wartość przechylenia
vertical_offset = 0  # Początkowa wartość przesunięcia wertykalnego
flatten = 1.0  # Początkowa wartość spłaszczenia (1.0 oznacza brak spłaszczenia)
horizontal_flip = False  # Początkowa wartość odwrócenia horyzontalnego
horizontal_offset = 0  # Początkowa wartość przesunięcia horyzontalnego

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        heptagon_size = max(50, heptagon_size - 10)
        heptagon_angle = 0
        skew = 0  # Początkowa wartość przechylenia
        vertical_offset = 0  # Początkowa wartość przesunięcia wertykalnego
        horizontal_offset = 0
        flatten = 1.0  # Początkowa wartość spłaszczenia (1.0 oznacza brak spłaszczenia)
    if keys[pygame.K_2]:
        heptagon_angle += 51.4285714
        heptagon_size = 100
        skew = 0  # Początkowa wartość przechylenia
        vertical_offset = 0  # Początkowa wartość przesunięcia wertykalnego
        flatten = 1.0  # Początkowa wartość spłaszczenia (1.0 oznacza brak spłaszczenia)
    if keys[pygame.K_3]:
        heptagon_size = 100
        heptagon_angle = 180
        skew = 0  # Początkowa wartość przechylenia
        vertical_offset = 0  # Początkowa wartość przesunięcia wertykalnego
        flatten = 1.0  # Początkowa wartość spłaszczenia (1.0 oznacza brak spłaszczenia)
    if keys[pygame.K_4]:
        skew = 40  # Zwiększamy przechylenie po naciśnięciu klawisza "4"
        heptagon_size = 100
        heptagon_angle = 0
        vertical_offset = 0  # Początkowa wartość przesunięcia wertykalnego
        flatten = 1.0  # Początkowa wartość spłaszczenia (1.0 oznacza brak spłaszczenia)
    if keys[pygame.K_5]:
        vertical_offset = -200  # Przesuwamy do góry
        flatten = 0.2  # Lekko spłaszczamy
        heptagon_size = 100
        heptagon_angle = 0
        skew = 0  # Początkowa wartość przechylenia
    if keys[pygame.K_6]:
        heptagon_size = 100
        heptagon_angle = 240
        skew = -50  # Początkowa wartość przechylenia
        vertical_offset = 0  # Początkowa wartość przesunięcia wertykalnego
        flatten = 1.0  # Początkowa wartość spłaszczenia (1.0 oznacza brak spłaszczenia)
    if keys[pygame.K_7]:
        heptagon_size = 100
        heptagon_angle = 180
        skew = 0  # Początkowa wartość przechylenia
        vertical_offset = 0  # Początkowa wartość przesunięcia wertykalnego
        flatten = 1.0  # Początkowa wartość spłaszczenia (1.0 oznacza brak spłaszczenia)
        horizontal_flip = True # Początkowa wartość odwrócenia horyzontalnego
    if keys[pygame.K_8]:
        heptagon_size = 100
        vertical_offset = 750
        horizontal_offset = -50
        flatten = 0.4
        heptagon_angle = 45
        skew = 90
        horizontal_flip = False
    if keys[pygame.K_9]:
        heptagon_size = 100
        heptagon_angle = 180
        skew = 70
        vertical_offset = 0
        flatten = 1.0
        horizontal_flip = False
        horizontal_offset = 180
    if keys[pygame.K_0]:
        heptagon_size = 100
        heptagon_angle = 0
        skew = 0  # Początkowa wartość przechylenia
        vertical_offset = 0
        horizontal_offset = 0
        flatten = 1.0  # Początkowa wartość spłaszczenia (1.0 oznacza brak spłaszczenia)
        horizontal_flip = False  # Początkowa wartość odwrócenia horyzontalnego

    win.fill(ZOLTY)
    draw_skewed_heptagon(win, CZERWONY, (300, 300), heptagon_size, heptagon_angle, skew, vertical_offset, flatten, horizontal_flip, horizontal_offset)

    pygame.display.update()

pygame.quit
