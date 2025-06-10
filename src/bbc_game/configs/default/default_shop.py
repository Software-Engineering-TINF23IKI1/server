from bbc_game.shop import TieredUpgrade, ClickUpgrade, GainUpgrade, BaseShop
import random


class DefaultShop(BaseShop):
    shop_entries = [
        TieredUpgrade(
            [
                ClickUpgrade(20, lambda x: x + 1, "Finger Power I"),
                ClickUpgrade(30, lambda x: x + 1, "Finger Power II"),
                ClickUpgrade(40, lambda x: x + 1, "Finger Power III"),
                ClickUpgrade(60, lambda x: x + 1, "Finger Power IV"),
                ClickUpgrade(100, lambda x: x + 1, "Finger Power V"),
                ClickUpgrade(150, lambda x: x + 1, "Finger Power VI"),
                ClickUpgrade(225, lambda x: x + 1, "Finger Power VII"),
                ClickUpgrade(400, lambda x: x + 1, "Finger Power VIII"),
                ClickUpgrade(600, lambda x: x + 1, "Finger Power IX"),
                ClickUpgrade(850, lambda x: x + 1, "Finger Power X"),
                ClickUpgrade(1_200, lambda x: x + 1, "Finger Power XI"),
                ClickUpgrade(1_500, lambda x: x + 1, "Finger Power XII"),
                ClickUpgrade(2_000, lambda x: x + 1, "Finger Power XIII"),
                ClickUpgrade(2_500, lambda x: x + 1, "Finger Power XIV"),
                ClickUpgrade(3_000, lambda x: x + 1, "Finger Power XV"),
                ClickUpgrade(5_000, lambda x: x + 1, "Finger Power XVI"),
                ClickUpgrade(7_500, lambda x: x + 1, "Finger Power XVII"),
                ClickUpgrade(11_000, lambda x: x + 1, "Finger Power XVIII"),
                ClickUpgrade(17_000, lambda x: x + 1, "Finger Power XIX"),
                ClickUpgrade(21_000, lambda x: x + 1, "Finger Power XX"),
                ClickUpgrade(25_000, lambda x: x + 1, "Finger Power XXI"),
                ClickUpgrade(32_000, lambda x: x + 1, "Finger Power XXII"),
                ClickUpgrade(40_000, lambda x: x + 1, "Finger Power XXIII"),
                ClickUpgrade(50_000, lambda x: x + 1, "Finger Power XXIV"),
                ClickUpgrade(65_000, lambda x: x + 1, "Finger Power XXV")
            ],
            "Finger Power",
            "Simple upgrade to make each click stronger."
        ),
        TieredUpgrade(
            [
                ClickUpgrade(500, lambda x: x * 2, "Click Frenzy Serum I"),
                ClickUpgrade(2_000, lambda x: x * 2, "Click Frenzy Serum II"),
                ClickUpgrade(8_000, lambda x: x * 2, "Click Frenzy Serum III"),
                ClickUpgrade(25_000, lambda x: x * 2, "Click Frenzy Serum IV"),
                ClickUpgrade(120_000, lambda x: x * 2, "Click Frenzy Serum V"),
                ClickUpgrade(600_000, lambda x: x * 2, "Click Frenzy Serum VI")
            ],
            "Click Frenzy Serum",
            "Injects raw banana energy into your fingertip. Doubles your current click value."
        ),
        TieredUpgrade(
            [
                GainUpgrade(50, lambda x: x + 1, "Intern Monkey I"),
                GainUpgrade(100, lambda x: x + 1, "Intern Monkey II"),
                GainUpgrade(200, lambda x: x + 1, "Intern Monkey III"),
                GainUpgrade(400, lambda x: x + 1, "Intern Monkey IV"),
                GainUpgrade(700, lambda x: x + 1, "Intern Monkey V"),
                GainUpgrade(1_000, lambda x: x + 1, "Intern Monkey VI"),
                GainUpgrade(1_500, lambda x: x + 1, "Intern Monkey VII"),
                GainUpgrade(2_000, lambda x: x + 1, "Intern Monkey VIII"),
                GainUpgrade(2_500, lambda x: x + 1, "Intern Monkey IX"),
                GainUpgrade(3_500, lambda x: x + 1, "Intern Monkey X")
            ],
            "Monkey Intern",
            "Unpaid, overqualified, but still brings in a banana every second"
        ),
        TieredUpgrade(
            [
                GainUpgrade(1_000, lambda x: x + 5, "Banana Outpost I"),
                GainUpgrade(2_000, lambda x: x + 5, "Banana Outpost II"),
                GainUpgrade(4_000, lambda x: x + 5, "Banana Outpost III"),
                GainUpgrade(7_000, lambda x: x + 5, "Banana Outpost IV"),
                GainUpgrade(10_000, lambda x: x + 5, "Banana Outpost V"),
                GainUpgrade(15_000, lambda x: x + 5, "Banana Outpost VI"),
                GainUpgrade(22_000, lambda x: x + 5, "Banana Outpost VII"),
                GainUpgrade(30_000, lambda x: x + 5, "Banana Outpost VIII"),
                GainUpgrade(40_000, lambda x: x + 5, "Banana Outpost IX"),
                GainUpgrade(55_000, lambda x: x + 5, "Banana Outpost X")
            ],
            "Banana Outpost",
            "A modest setup that boosts your flow by +5 bananas per second."
        ),
        TieredUpgrade(
            [
                GainUpgrade(10_000, lambda x: x + 50, "Automated Plantation I"),
                GainUpgrade(20_000, lambda x: x + 50, "Automated Plantation II"),
                GainUpgrade(35_000, lambda x: x + 50, "Automated Plantation III"),
                GainUpgrade(50_000, lambda x: x + 50, "Automated Plantation IV"),
                GainUpgrade(70_000, lambda x: x + 50, "Automated Plantation V"),
                GainUpgrade(100_000, lambda x: x + 50, "Automated Plantation VI"),
                GainUpgrade(150_000, lambda x: x + 50, "Automated Plantation VII"),
                GainUpgrade(225_000, lambda x: x + 50, "Automated Plantation VIII"),
                GainUpgrade(350_000, lambda x: x + 50, "Automated Plantation IX"),
                GainUpgrade(500_000, lambda x: x + 50, "Automated Plantation X")
            ],
            "Automated Plantation",
            "Industrial banana operations generate a solid +50 bananas per second."
        ),
        GainUpgrade(
            5_000,
            lambda x: x * random.randint(0, 1) * 2,
            "Banana Roulette",
            "Double your passive income — or lose it all! 50% chance to multiply your income, 50% chance to drop to zero. Play it if you dare."
        ),
        TieredUpgrade(
            [
                GainUpgrade(2_000, lambda x: x * 1, "Banana Multiplexer I"),
                GainUpgrade(10_000, lambda x: x * 2, "Banana Multiplexer II"),
                GainUpgrade(50_000, lambda x: x * 3, "Banana Multiplexer III"),
                GainUpgrade(200_000, lambda x: x * 4, "Banana Multiplexer IV"),
                GainUpgrade(1_000_000, lambda x: x * 5, "Banana Multiplexer V"),
                GainUpgrade(10_000_000, lambda x: x * 6, "Banana Multiplexer VI"),
                GainUpgrade(100_000_000, lambda x: x * 7, "Banana Multiplexer VII"),
                GainUpgrade(1_500_000_000, lambda x: x * 8, "Banana Multiplexer VIII"),
                GainUpgrade(50_000_000_000, lambda x: x * 9, "Banana Multiplexer IX"),
                GainUpgrade(1_000_000_000_000, lambda x: x * 10, "Banana Multiplexer X")
            ],
            "Banana Multiplexer",
            "Multiplies your passive income by your upgrade tier. The higher the tier, the stronger the banana flow."
        )
    ]
