from bbc_game.shop import TieredUpgrade, ClickUpgrade, GainUpgrade, BaseShop


class DefaultShop(BaseShop):
    shop_entries = [
        TieredUpgrade(
            [
                ClickUpgrade(20, lambda x: x * 2, "Better Clicks 1"),
                ClickUpgrade(30, lambda x: x * 2, "Better Clicks 2"),
                ClickUpgrade(40, lambda x: x * 2, "Better Clicks 3")
            ],
            "Better Clicks",
            "doubles click modifier for every level purchased"
        ),
        TieredUpgrade(
            [
                GainUpgrade(50, lambda x: x + 1, "Passive Income 1"),
                GainUpgrade(100, lambda x: x + 1, "Passive Income 2"),
                GainUpgrade(500, lambda x: x + 1, "Passive Income 3"),
            ],
            "Passive Income",
            "increases passive gain by 1 per level"
        )
    ]
