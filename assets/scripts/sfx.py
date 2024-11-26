import pygame
from settings import *
pygame.mixer.init()
shoot_sfx = pygame.mixer.Sound("assets/sounds/laserShoot.wav")
shoot_sfx.set_volume(SHOOT_VOLUME)
rapidshoot_sfx = pygame.mixer.Sound("assets/sounds/rapidshoot.wav")
rapidshoot_sfx.set_volume(SHOOT_VOLUME)

asteroidL_sfx = pygame.mixer.Sound("assets/sounds/explosion.wav")
asteroidL_sfx.set_volume(EXPLOSION_VOLUME)
asteroidM_sfx = pygame.mixer.Sound("assets/sounds/explosion_m.wav")
asteroidM_sfx.set_volume(EXPLOSION_VOLUME)
asteroidS_sfx = pygame.mixer.Sound("assets/sounds/explosion_s.wav")
asteroidS_sfx.set_volume(EXPLOSION_VOLUME)

hit_sfx = pygame.mixer.Sound("assets/sounds/hit.wav")
hit_sfx.set_volume(HIT_VOLUME)

pickup_sfx = pygame.mixer.Sound("assets/sounds/pickup.wav")
pickup_sfx.set_volume(PICKUP_VOLUME)

powerup_sfx = pygame.mixer.Sound("assets/sounds/powerup.wav")
powerup_sfx.set_volume(PICKUP_VOLUME)
powerdown_sfx = pygame.mixer.Sound("assets/sounds/powerdown.wav")
powerdown_sfx.set_volume(PICKUP_VOLUME)

select_sfx = pygame.mixer.Sound("assets/sounds/select.wav")
select_sfx.set_volume(SELECT_VOLUME)
dead_sfx = pygame.mixer.Sound("assets/sounds/dead.wav")
dead_sfx.set_volume(DEAD_VOLUME)