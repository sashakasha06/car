import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("car.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 0
    sprite.rect.y = 0
    v = 100
    direction = 1
    clock = pygame.time.Clock()
    flip_horizontal = True
    flip_vertical = False
    running = True
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        delta_time = clock.tick(60)/1000
        sprite.rect.x += v * delta_time * direction
        if sprite.rect.x >= 450 or sprite.rect.x <= 0:
            sprite.image = pygame.transform.flip(sprite.image, flip_horizontal, flip_vertical)
            direction *= -1
        screen.fill((255, 255, 255))
        screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
        pygame.display.flip()
    pygame.quit()