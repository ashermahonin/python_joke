import time
import pygame
from tkinter import *
from tkinter import  messagebox

Tk().wm_withdraw()

pygame.init()

pygame.display.set_icon(pygame.image.load("icon.png"))

window = pygame.display.set_mode((850, 200))
pygame.display.set_caption('Your data has been stolen! Follow the instructions!')
font = pygame.font.SysFont("Lucida  Console", 25)
text = font.render("We have all of your information!)", 1, (51, 255, 51, 1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            time.sleep((0.10))
            window = pygame.display.set_mode((850, 100))
            pygame.display.set_caption('Your data has been stolen!')
            messagebox.showerror("Send me your smile-photo BRUH :D", "secret")

    window.fill((0, 0, 0))
    window.blit(text, (50, 50))

    pygame.display.update()
