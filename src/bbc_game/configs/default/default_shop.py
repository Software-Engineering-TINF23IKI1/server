from bbc_game.shop import TieredUpgrade, ClickUpgrade, GainUpgrade, BaseShop


class DefaultShop(BaseShop):
    shop_entries = [
        TieredUpgrade(
            [
                ClickUpgrade(20, lambda x: x + 1, "Better Clicks I"),
                ClickUpgrade(30, lambda x: x + 1, "Better Clicks II"),
                ClickUpgrade(40, lambda x: x + 1, "Better Clicks III"),
                ClickUpgrade(60, lambda x: x + 1, "Better Clicks IV"),
                ClickUpgrade(100, lambda x: x + 1, "Better Clicks V"),
                ClickUpgrade(150, lambda x: x + 1, "Better Clicks VI"),
                ClickUpgrade(225, lambda x: x + 1, "Better Clicks VII"),
                ClickUpgrade(400, lambda x: x + 1, "Better Clicks VIII"),
                ClickUpgrade(600, lambda x: x + 1, "Better Clicks IX"),
                ClickUpgrade(850, lambda x: x + 1, "Better Clicks X"),
                ClickUpgrade(1200, lambda x: x + 1, "Better Clicks XI"),
                ClickUpgrade(1500, lambda x: x + 1, "Better Clicks XII"),
                ClickUpgrade(2000, lambda x: x + 1, "Better Clicks XIII"),
                ClickUpgrade(2500, lambda x: x + 1, "Better Clicks XIV"),
                ClickUpgrade(3000, lambda x: x + 1, "Better Clicks XV")
            ],
            "Better Clicks",
            "increases click modifier by 1 per level"
        ),
        TieredUpgrade(
            [
                ClickUpgrade(500, lambda x: x * 2, "Golden Clicks I"),
                ClickUpgrade(2000, lambda x: x * 2, "Golden Clicks II")
            ],
            "Golden Clicks",
            "doubles click modifier for every level purchased"
        ),
        TieredUpgrade(
            [
                GainUpgrade(50, lambda x: x + 1, "Passive Income I"),
                GainUpgrade(100, lambda x: x + 1, "Passive Income II"),
                GainUpgrade(200, lambda x: x + 1, "Passive Income III"),
                GainUpgrade(400, lambda x: x + 1, "Passive Income IV"),
                GainUpgrade(700, lambda x: x + 1, "Passive Income V"),
                GainUpgrade(1000, lambda x: x + 1, "Passive Income VI"),
                GainUpgrade(1500, lambda x: x + 1, "Passive Income VII"),
                GainUpgrade(2000, lambda x: x + 1, "Passive Income VIII"),
                GainUpgrade(2500, lambda x: x + 1, "Passive Income IX"),
                GainUpgrade(3500, lambda x: x + 1, "Passive Income X")
            ],
            "Passive Income",
            "increases passive gain by 1 per level"
        ),
        TieredUpgrade(
            [
                GainUpgrade(1000, lambda x: x + 5, "Better Passive Income I"),
                GainUpgrade(2000, lambda x: x + 5, "Better Passive Income II"),
                GainUpgrade(4000, lambda x: x + 5, "Better Passive Income III"),
                GainUpgrade(7000, lambda x: x + 5, "Better Passive Income IV"),
                GainUpgrade(10000, lambda x: x + 5, "Better Passive Income V"),
                GainUpgrade(15000, lambda x: x + 5, "Better Passive Income VI"),
                GainUpgrade(22000, lambda x: x + 5, "Better Passive Income VII"),
                GainUpgrade(30000, lambda x: x + 5, "Better Passive Income VIII"),
                GainUpgrade(40000, lambda x: x + 5, "Better Passive Income IX"),
                GainUpgrade(55000, lambda x: x + 5, "Better Passive Income X")
            ],
            "Better Passive Income",
            "increases passive gain by 5 per level"
        ),
        GainUpgrade(
            10000,
            lambda x: x * 2,
            "Golden Income",
            "Doubles the current passive income"
        )
    ]
