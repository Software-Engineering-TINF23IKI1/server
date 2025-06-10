from bbc_game.shop import TieredUpgrade, ClickUpgrade, GainUpgrade, BaseShop
import random


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
                ClickUpgrade(1_200, lambda x: x + 1, "Better Clicks XI"),
                ClickUpgrade(1_500, lambda x: x + 1, "Better Clicks XII"),
                ClickUpgrade(2_000, lambda x: x + 1, "Better Clicks XIII"),
                ClickUpgrade(2_500, lambda x: x + 1, "Better Clicks XIV"),
                ClickUpgrade(3_000, lambda x: x + 1, "Better Clicks XV")
            ],
            "Better Clicks",
            "increases click modifier by 1 per level"
        ),
        TieredUpgrade(
            [
                ClickUpgrade(500, lambda x: x * 2, "Golden Clicks I"),
                ClickUpgrade(2_000, lambda x: x * 2, "Golden Clicks II"),
                ClickUpgrade(8_000, lambda x: x * 2, "Golden Clicks III"),
                ClickUpgrade(25_000, lambda x: x * 2, "Golden Clicks IV"),
                ClickUpgrade(120_000, lambda x: x * 2, "Golden Clicks V"),
                ClickUpgrade(600_000, lambda x: x * 2, "Golden Clicks VI"),
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
                GainUpgrade(1_000, lambda x: x + 1, "Passive Income VI"),
                GainUpgrade(1_500, lambda x: x + 1, "Passive Income VII"),
                GainUpgrade(2_000, lambda x: x + 1, "Passive Income VIII"),
                GainUpgrade(2_500, lambda x: x + 1, "Passive Income IX"),
                GainUpgrade(3_500, lambda x: x + 1, "Passive Income X")
            ],
            "Passive Income",
            "increases passive gain by 1 per level"
        ),
        TieredUpgrade(
            [
                GainUpgrade(1_000, lambda x: x + 5, "Better Passive Income I"),
                GainUpgrade(2_000, lambda x: x + 5, "Better Passive Income II"),
                GainUpgrade(4_000, lambda x: x + 5, "Better Passive Income III"),
                GainUpgrade(7_000, lambda x: x + 5, "Better Passive Income IV"),
                GainUpgrade(10_000, lambda x: x + 5, "Better Passive Income V"),
                GainUpgrade(15_000, lambda x: x + 5, "Better Passive Income VI"),
                GainUpgrade(22_000, lambda x: x + 5, "Better Passive Income VII"),
                GainUpgrade(30_000, lambda x: x + 5, "Better Passive Income VIII"),
                GainUpgrade(40_000, lambda x: x + 5, "Better Passive Income IX"),
                GainUpgrade(55_000, lambda x: x + 5, "Better Passive Income X")
            ],
            "Better Passive Income",
            "increases passive gain by 5 per level"
        ),
        TieredUpgrade(
            [
                GainUpgrade(10_000, lambda x: x + 50, "Insane Passive Income I"),
                GainUpgrade(20_000, lambda x: x + 50, "Insane Passive Income II"),
                GainUpgrade(35_000, lambda x: x + 50, "Insane Passive Income III"),
                GainUpgrade(50_000, lambda x: x + 50, "Insane Passive Income IV"),
                GainUpgrade(70_000, lambda x: x + 50, "Insane Passive Income V"),
                GainUpgrade(100_000, lambda x: x + 50, "Insane Passive Income VI"),
                GainUpgrade(150_000, lambda x: x + 50, "Insane Passive Income VII"),
                GainUpgrade(225_000, lambda x: x + 50, "Insane Passive Income VIII"),
                GainUpgrade(350_000, lambda x: x + 50, "Insane Passive Income IX"),
                GainUpgrade(500_000, lambda x: x + 50, "Insane Passive Income X")
            ],
            "Insane Passive Income",
            "increases passive gain by 50 per level"
        ),
        GainUpgrade(
            5_000,
            lambda x: x * random.randint(0, 1) * 2,
            "Gamblers Fate",
            "Doubles the Passive Income or sets the Passive Income to 0 with a 50% chance"
        ),
        GainUpgrade(
            10_000,
            lambda x: x * 2,
            "Golden Income",
            "Doubles the current passive income"
        ),
        GainUpgrade(
            10_000,
            lambda x: x * 4,
            "Ultimate Income",
            "Quadruples the current passive income"
        )
    ]
