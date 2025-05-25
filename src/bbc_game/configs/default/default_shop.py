from bbc_game.shop import TieredUpgrade, ClickUpgrade, GainUpgrade, BaseShop


class DefaultShop(BaseShop):
    shop_entries = {
        "Better Clicks": TieredUpgrade(
            [
                ClickUpgrade(20, lambda x: x + 1, "Better Clicks 1"),
                ClickUpgrade(30, lambda x: x + 1, "Better Clicks 2"),
                ClickUpgrade(40, lambda x: x + 1, "Better Clicks 3")
            ],
            "Better Clicks",
            "increases click modifier by 1 per level"
        ),
        "Passive Income": TieredUpgrade(
            [
                GainUpgrade(50, lambda x: x * 2, "Passive Income 1"),
                GainUpgrade(100, lambda x: x * 2, "Passive Income 2"),
                GainUpgrade(500, lambda x: x * 2, "Passive Income 3"),
            ],
            "Passive Income",
            "doubles passive gain for every level purchased"
        )
    }
