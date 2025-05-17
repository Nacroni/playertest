# aaeasy for playertest
import logging
if __name__ == "__main__":
  logging.fatal("Script cannot be run as main.")
  exit(1)
# aaeasy: make aa circles easier
import pygame, pygame.gfxdraw

def circle(surface: pygame.Surface, pos: pygame.Vector2, radius: int, color: pygame.Color) -> None:
  """
  circle: draws an anti-aliased circle

  Args:
      surface (pygame.Surface): the surface to draw on
      pos (pygame.Vector2): the position to draw to
      radius (int): the radius of the circle
      color (pygame.Color): the color of the circle
  """
  pygame.gfxdraw.filled_circle(surface, int(pos.x), int(pos.y), radius, color)
  pygame.gfxdraw.aacircle(surface, int(pos.x), int(pos.y), radius, color)

def ellipse(surface: pygame.Surface, pos: pygame.Vector2, radius: pygame.Vector2, color: pygame.Color) -> None:
  """
  ellipse: draws an anti-alised ellipse

  Args:
      surface (pygame.Surface): the surface to draw on
      pos (pygame.Vector2): the position to draw to
      radius (pygame.Vector2): the radius of the ellipse
      color (pygame.Color): the color of the circle
  """
  pygame.gfxdraw.filled_ellipse(surface, int(pos.x), int(pos.y), int(radius.x), int(radius.y), color)
  pygame.gfxdraw.aaellipse(surface, int(pos.x), int(pos.y), int(radius.x), int(radius.y), color)

# Unfinished code below!

#def polygon(surface: pygame.Surface, points, color: pygame.Color) -> None:
#  pygame.gfxdraw.filled_polygon(surface, points, color)
#  pygame.gfxdraw.aapolygon(surface, points, color)
#
#def trigon(surface: pygame.Surface, x: list, y: list, color: pygame.Color) -> None:
#  pygame.gfxdraw.filled_trigon(surface, x)
#  pygame.gfxdraw.aatrigon()