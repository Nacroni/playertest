#!/usr/bin/env python3
import pygame, aaeasy, logging, sys
from pygame.locals import * # type: ignore

screen_resolution = (640, 480)
fullscreen = False
logging.info("screen resolution and fullscreen vars set")

pygame.init()
logging.info("pygame initialized")
screen = pygame.display.set_mode(screen_resolution, pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
dt = 0
logging.info("topmost code done")

# this is bound to happen if the user doesnt use requirements or if they are illiterate
try:
  fps_maximum = pygame.display.get_current_refresh_rate()
  logging.info("max fps has been set by current refresh rate func", fps_maximum)
except:
  fps_maximum = 60
  logging.warning("max fps has been set to default value due to issue with current refresh rate func. did you install pygame-ce or did you just install normal pygame?", fps_maximum)

class player:
  position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

  def __init__(self, surface: pygame.Surface, radius: int, color: pygame.Color) -> None:
    aaeasy.circle(surface, self.position, int(radius), pygame.Color(color))
    self.movement(surface, radius)

  def movement(self, surface: pygame.Surface, radius: int) -> None:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      self.position.y -= 300 * dt
    if keys[pygame.K_s]:
      self.position.y += 300 * dt
    if keys[pygame.K_a]:
      self.position.x -= 300 * dt
    if keys[pygame.K_d]:
      self.position.x += 300 * dt
    
    # left edge
    if self.position.x < 0 + radius:
      self.position.x = 0 + radius
    # right edge
    if self.position.x > surface.get_width() - radius:
      self.position.x = surface.get_width() - radius
    # top 
    if self.position.y < 0 + radius:
      self.position.y = 0 + radius
    # bottom
    if self.position.y > surface.get_height() - radius:
      self.position.y = surface.get_height() - radius

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      logging.info("I quit!")
      running = False
    if event.type == pygame.WINDOWRESIZED:
      screen_resolution = (screen.get_width(), screen.get_height())
      logging.info("window has been resized", screen_resolution)
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_F11:
        fullscreen = not fullscreen
        if fullscreen:
          screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
        else:
          screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
  pygame.display.set_caption(f"playertest - fps: {int(clock.get_fps())}/{fps_maximum}")

  screen.fill(pygame.Color(127, 170, 127))
  
  player(screen, 32, pygame.Color(255, 255, 255))

  pygame.display.flip()

  dt = clock.tick(fps_maximum) / 1000

pygame.quit()