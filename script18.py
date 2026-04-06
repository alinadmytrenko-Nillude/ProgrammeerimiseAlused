import pygame

pygame.init()

laius = 800
korgus = 600
ekraan = pygame.display.set_mode((laius, korgus))
pygame.display.set_caption("Liikuv ruut")

valge = (255, 255, 255)
sinine = (0, 100, 255)

x = laius // 2
y = korgus // 2
ruudu_suurus = 50
kiirus = 5

too_kaib = True

while too_kaib:
    for sundmus in pygame.event.get():
        if sundmus.type == pygame.QUIT:
            too_kaib = False

    klahvid = pygame.key.get_pressed()
    if klahvid[pygame.K_LEFT]:
        x -= kiirus
    if klahvid[pygame.K_RIGHT]:
        x += kiirus
    if klahvid[pygame.K_UP]:
        y -= kiirus
    if klahvid[pygame.K_DOWN]:
        y += kiirus

    # Lisapunkt: ruut ei lähe ekraani piiridest välja
    x = max(0, min(x, laius - ruudu_suurus))
    y = max(0, min(y, korgus - ruudu_suurus))

    ekraan.fill(valge)
    pygame.draw.rect(ekraan, sinine, (x, y, ruudu_suurus, ruudu_suurus))
    pygame.display.flip()

pygame.quit()