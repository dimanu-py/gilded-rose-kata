from approvaltests import verify_all_combinations

from gilded_rose_approvals.gilded_rose import Item, GildedRose


def item_printer(item: Item) -> str:
    return f"{item.name}, sell_in: {item.sell_in}, quality: {item.quality}"


class TestGildedRoseApprovals:

    def test_update_quality(self, intellij_diff_reporter):
        name = ["Common Item", "Aged Brie", "Backstage passes", "Sulfuras, Hand of Ragnaros"]
        sell_in = [-1, 0, 5, 6, 10, 11]
        quality = [0, 1, 2, 49, 50]

        verify_all_combinations(
            self.do_update_quality,
            [name, sell_in, quality],
            reporter=intellij_diff_reporter
        )

    def do_update_quality(self, name: str, sell_in: int, quality: int) -> str:
        item = [Item(name, sell_in, quality)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        item_as_string = item_printer(item[0])

        return item_as_string
