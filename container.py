import dependency_injector.containers as containers
import dependency_injector.providers as providers
from spacecrafts import Player, Enemy, IceEnemy, FireEnemy, PoisonEnemy
from bullets import FireBullet, IceBullet, PoisonBullet

class Powers(containers.DeclarativeContainer):
    """IoC container of engine providers."""

    fire = providers.Factory(FireBullet)

    ice = providers.Factory(IceBullet)

    poison = providers.Factory(PoisonBullet)
    


class Crafts(containers.DeclarativeContainer):
    """IoC container of car providers."""

    fire = providers.Factory(Player,
                                 bullet=Powers.fire)

    ice = providers.Factory(Player,
                               bullet=Powers.ice)

    poison = providers.Factory(Player,
                                bullet=Powers.poison)
                                
                                
class Enemies(containers.DeclarativeContainer):
    """IoC container of car providers."""

    fire = providers.Factory(FireEnemy,
                                 bullet=Powers.fire)

    ice = providers.Factory(IceEnemy,
                               bullet=Powers.ice)

    poison = providers.Factory(PoisonEnemy,
                                bullet=Powers.poison)

