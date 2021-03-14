from BaseClasses import MultiWorld
from worlds.alttp.Dungeons import create_dungeons, get_dungeon_item_pool
from worlds.alttp.EntranceShuffle import link_inverted_entrances
from worlds.alttp.InvertedRegions import create_inverted_regions
from worlds.alttp.ItemPool import generate_itempool, difficulties
from worlds.alttp.Items import ItemFactory
from worlds.alttp.Regions import mark_light_world_regions
from worlds.alttp.Shops import create_shops
from worlds.alttp.Rules import set_rules
from test.TestBase import TestBase


class TestInverted(TestBase):
    def setUp(self):
        self.world = MultiWorld(1)
        self.world.difficulty_requirements[1] = difficulties['normal']
        self.world.mode[1] = "inverted"
        create_inverted_regions(self.world, 1)
        create_dungeons(self.world, 1)
        create_shops(self.world, 1)
        link_inverted_entrances(self.world, 1)
        generate_itempool(self.world, 1)
        self.world.required_medallions[1] = ['Ether', 'Quake']
        self.world.itempool.extend(get_dungeon_item_pool(self.world))
        self.world.itempool.extend(ItemFactory(['Green Pendant', 'Red Pendant', 'Blue Pendant', 'Beat Agahnim 1', 'Beat Agahnim 2', 'Crystal 1', 'Crystal 2', 'Crystal 3', 'Crystal 4', 'Crystal 5', 'Crystal 6', 'Crystal 7'], 1))
        self.world.get_location('Agahnim 1', 1).item = None
        self.world.get_location('Agahnim 2', 1).item = None
        mark_light_world_regions(self.world, 1)
        set_rules(self.world, 1)
