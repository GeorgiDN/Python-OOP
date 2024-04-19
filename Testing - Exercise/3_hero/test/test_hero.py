from project.hero import Hero

from unittest import TestCase, main


class HeroTests(TestCase):
    def setUp(self):
        self.hero = Hero("Gosho", 10, 100.0, 100.0)
        self.enemy = Hero("Ivan", 10, 100.0, 100.0)

    def test_init_hero(self):
        self.assertEqual("Gosho", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(100.0, self.hero.damage)

    def test_init_enemy(self):
        self.assertEqual("Ivan", self.enemy.username)
        self.assertEqual(10, self.enemy.level)
        self.assertEqual(100.0, self.enemy.health)
        self.assertEqual(100.0, self.enemy.damage)

    def test_battle_with_same_hero_name_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_hero_health_equal_to_zero_and_raise_valueerror(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with_hero_health_less_than_zero_and_raise_valueerror(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with_enemy_health_equal_to_zero_and_raise_valueerror(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_battle_with_enemy_health_less_than_zero_and_raise_valueerror(self):
        self.enemy.health = -1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_battle_when_result_is_draw_when_health_less_than_zero(self):
        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_battle_when_result_is_draw_when_health_is_zero(self):
        self.hero.damage = 10
        self.enemy.damage = 10
        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_battle_hero_win_increase_level_health_damage(self):
        self.enemy.health = 1
        self.enemy.damage = 1
        self.hero.battle(self.enemy)

        self.assertEqual(-999.0, self.enemy.health)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(95.0, self.hero.health)
        self.assertEqual(105.0, self.hero.damage)

    def test_battle_hero_win_return_message(self):
        self.enemy.health = 1
        self.enemy.damage = 1
        self.assertEqual(self.hero.battle(self.enemy), "You win")

    def test_battle_enemy_win_increase_level_health_damage(self):
        self.hero.health = 1
        self.hero.damage = 1
        self.hero.battle(self.enemy)

        self.assertEqual(-999.0, self.hero.health)
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(95.0, self.enemy.health)
        self.assertEqual(105.0, self.enemy.damage)

    def test_battle_enemy_win_return_message(self):
        self.hero.health = 1
        self.hero.damage = 1
        self.assertEqual(self.hero.battle(self.enemy), "You lose")

    def test_str(self):
        self.assertEqual(self.hero.__str__(), f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n")


if __name__ == '__main__':
    main()
