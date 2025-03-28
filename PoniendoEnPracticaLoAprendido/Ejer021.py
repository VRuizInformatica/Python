class TeamMates:
    def __init__(self, name, hp, attack, defense, elusive, specialHability="None"):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.elusive = elusive
        self.specialHability = specialHability
        self.base_hp = hp
        self.base_attack = attack
        self.base_defense = defense
        self.base_elusive = elusive
        self.base_specialHability = specialHability

    def Welcome(Friend1, Friend2, Friend3, Friend4):
        print("- The inscriptions are closed, let's present our new fighters!!\n"
            f"- {Friend1.name} a big dude\n"
            f"- The powered girl {Friend2.name}\n"
            f"- The freak beast {Friend3.name}\n"
            f"- And the CEO and dangerous {Friend4.name}")
        print("Let's present their stats:")
        for friend in [Friend1, Friend2, Friend3, Friend4]:
            print(f"{friend.name}\n  Attack: {friend.attack}\n  Defense: {friend.defense}\n  Elusive: {friend.elusive}\n  Special Hability: {friend.specialHability}\n")

    def Attack(self, Defender):
        if self.attack > Defender.defense:
            self.Damage(Defender)
        else:
            print(f"{self.name} attacks {Defender.name} but does no damage!")

    def use_special_hability(self):
        self.attack += (self.attack * 20) // 100
        print(f"{self.name} has increased his attack by 20%: {self.attack}")

    def Damage(self, Defender):
        damage = self.attack - Defender.defense
        Defender.hp -= damage
        print(f"{self.name} attacks {Defender.name} and deals {damage} damage!")

    def reset_stats(self):
        self.hp = self.base_hp
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.elusive = self.base_elusive
        self.specialHability = self.base_specialHability
        print(f"{self.name}'s stats have been reset.")

class Exe:
    def fight_match(Fighter1, Fighter2):
        print(f"\n--- Starting fight: {Fighter1.name} vs {Fighter2.name} ---")
        while Fighter1.hp > 0 and Fighter2.hp > 0:
            Fighter1.Attack(Fighter2)
            if Fighter2.hp <= 0:
                print(f"¡{Fighter1.name} wins the fight!")
                return Fighter1
            Fighter2.Attack(Fighter1)
            if Fighter1.hp <= 0:
                print(f"¡{Fighter2.name} wins the fight!")
                return Fighter2

    def Tournament(Friend1, Friend2, Friend3, Friend4):
        TeamMates.Welcome(Friend1, Friend2, Friend3, Friend4)

        print("\n=== First Round ===")
        winner1 = Exe.fight_match(Friend1, Friend2)
        winner2 = Exe.fight_match(Friend3, Friend4)

        winner1.reset_stats()
        winner2.reset_stats()

        print("\n=== Final Round ===")
        champion = Exe.fight_match(winner1, winner2)
        print(f"\nChampion of the tournament is: {champion.name}")

Jorge = TeamMates('Jorge', 100, 20, 30, 'Brows')
Naia = TeamMates('Naia', 80, 20, 23, 'Brown-Green')
Victor = TeamMates('Victor', 90, 25, 15, 'Brown')
Hector = TeamMates('Hector', 70, 40, 34, 'Brown')

Exe.Tournament(Victor, Naia, Jorge, Hector)