from abc import ABC, abstractmethod


class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRoseItem(ABC, Item):
    """Item available in the Gilded Rose store.

    Encapsulates the common behavior of all items in the store.
    """

    MAXIMUM_QUALITY = 50
    MINIMUM_QUALITY = 0

    @abstractmethod
    def update_quality(self) -> None:
        """Update the quality of the item."""

    def process_item(self) -> None:
        self.decrease_sell_in_day()
        self.update_quality()

    def decrease_sell_in_day(self) -> None:
        self.sell_in = self.sell_in - 1

    def increase_quality(self) -> None:
        if self.quality < self.MAXIMUM_QUALITY:
            self.quality = self.quality + 1

    def decrease_quality(self, amount: int = 1) -> None:
        if self.quality > self.MINIMUM_QUALITY:
            self.quality = self.quality - amount

    def is_expired(self):
        return self.sell_in < 0


class NormalItem(GildedRoseItem):

    def update_quality(self) -> None:
        self.decrease_quality()
        if self.is_expired():
            self.decrease_quality()


class AgedBrie(GildedRoseItem):

    def update_quality(self) -> None:
        self.increase_quality()
        if self.is_expired():
            self.increase_quality()


class BackstagePasses(GildedRoseItem):

    def update_quality(self) -> None:
        self.increase_quality()
        if self.sell_in < 10:
            self.increase_quality()
        if self.sell_in < 5:
            self.increase_quality()
        if self.is_expired():
            self.quality = self.MINIMUM_QUALITY


class Sulfuras(GildedRoseItem):

    def update_quality(self) -> None:
        """Sulfuras never changes its quality."""
        pass

    def decrease_sell_in_day(self) -> None:
        """Sulfuras never changes its sell in day."""
        pass


class Conjured(GildedRoseItem):

    def update_quality(self) -> None:
        self.decrease_quality(amount=2)
        if self.is_expired():
            self.decrease_quality(amount=2)
