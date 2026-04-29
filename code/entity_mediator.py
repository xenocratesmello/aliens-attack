from code.constants import WINDOW_HEIGHT
from code.enemy import Enemy
from code.enemy_shot import EnemyShot
from code.entity import Entity
from code.player import Player
from code.player_shot import PlayerShot


class EntityMediator(Entity):

    @staticmethod
    def __verify_collision_window(entity):
        if isinstance(entity, EnemyShot):
            if entity.rect.bottom > WINDOW_HEIGHT:
                entity.health = 0
        if isinstance(entity, PlayerShot):
            if entity.rect.top < 0:
                entity.health = 0

    @staticmethod
    def __verify_collision_entity(entity_a, entity_b):

        match entity_a, entity_b:
            case (Enemy(), PlayerShot()) | \
                 (PlayerShot(), Enemy()) | \
                 (Player(), EnemyShot()) | \
                 (EnemyShot(), Player()) | \
                 (Enemy(), Player()) | ( \
                     Player(), Enemy()):
                valid_interaction = True
            case _:
                valid_interaction = False

        # Collision Test
        if (valid_interaction
                and entity_a.rect.right >= entity_b.rect.left
                and entity_a.rect.left <= entity_b.rect.right
                and entity_a.rect.bottom >= entity_b.rect.top
                and entity_a.rect.top <= entity_b.rect.bottom):
            entity_a.health -= entity_b.damage
            entity_b.health -= entity_a.damage
            if isinstance(entity_a, PlayerShot):
                entity_a.player_shooter.score += entity_a.damage
            elif isinstance(entity_b, PlayerShot):
                entity_b.player_shooter.score += entity_b.damage

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)

    @staticmethod
    def verify_collision(entity_list_a: list, entity_list_b: list):

        for entity_b in entity_list_b:
            EntityMediator.__verify_collision_window(entity_b)

        for entity_a in entity_list_a:
            EntityMediator.__verify_collision_window(entity_a)
            for entity_b in entity_list_b:
                EntityMediator.__verify_collision_entity(entity_a, entity_b)