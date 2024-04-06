
from gilded_rose.gilded_rose import Item, GildedRose


class TestGildedRose:

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert "fixme" == items[0].name
