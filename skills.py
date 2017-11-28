import pygame


class Skills():
    def __init__(self):
        self.skillImg = []
        self.skillDesc = []
        self.skillTarget = []

        for i in range(7):
            self.skillImg.append([])
            for j in range(5):
                self.skillImg[i].append(pygame.transform.scale(pygame.image.load(
                    'sprites/create_char/skills/' + str(i) + '-' + str(j) + '.png'), (50, 50)))

        for i in range(7):
            self.skillDesc.append([])
            self.skillTarget.append([])
            for j in range(5):
                self.skillDesc[i].append([])
                self.skillTarget[i].append([])
                self.skillBuilder(i, j, ['', '', ''])

        # Strength
        self.skillBuilder(0, 0, [
            'ROAR!',
            'Chance to stun target', '',
            '+5% per level'], 1)

        self.skillBuilder(0, 1, [
            'Rage',
            'Increase self damage', '',
            '+5% per level'])

        self.skillBuilder(0, 2, [
            'Whirlwind',
            'Damage multiple targets', '60% Weapon damage',
            '+5% per level'], 1)

        self.skillBuilder(0, 3, [
            'Inspire',
            'Increase allies damage', '',
            '+5% per level'])

        self.skillBuilder(0, 4, [
            'Earthquake',
            'Damage all enemies,', 'chance to stun',
            '+5% per level'])

        # Polimorph
        self.skillBuilder(1, 0, [
            'Mirror Image',
            '50% dodge chance', '', ''])

        self.skillBuilder(1, 1, [
            'Spike Skin',
            'Imunity to negative status', '',
            'reflect +5% damage per level'])

        self.skillBuilder(1, 2, [
            'Octopus Hug',
            'Prevent enemy from dodge', '',
            '+5% per level'], 1)

        self.skillBuilder(1, 3, [
            'Claw Attack',
            'Fisical damage', 'Chance to bleeding and stun',
            '+5% per level'], 1)

        self.skillBuilder(1, 4, [
            'Medusa Head',
            'Stun all enemies for 2 rounds', 'Chance to poison', ''])

        # Endurance
        self.skillBuilder(2, 0, [
            'Provoke',
            'Taunt enemies', '',
            '+5% per level'])

        self.skillBuilder(2, 1, [
            'Fortify',
            'Increases target defenses', '',
            '+5% per level'], 1)

        self.skillBuilder(2, 2, [
            'Life Link',
            'Divide damage taken', 'with target',
            '15% per level'], 1)

        self.skillBuilder(2, 3, [
            'Second Chance',
            'Chance to resist death', '',
            '+20% per level'])

        self.skillBuilder(2, 4, [
            'Unbreakable',
            'Immune to damage,', 'Taunt enemies',
            '+2 Turns per level'])

        # Charisma
        self.skillBuilder(3, 0, [
            'Leadership',
            'Increase allies damage', '',
            '+5% per level'])

        self.skillBuilder(3, 1, [
            'Fear',
            'Reduces opponent damage', '',
            '+5% per level'], 1)

        self.skillBuilder(3, 2, [
            'Puppy Eyes',
            'Target cant attack', '',
            '+10% chance per level'], 1)

        self.skillBuilder(3, 3, [
            'Charm',
            'Force enemy to attack', 'its allies',
            '+5% per level'], 1)

        self.skillBuilder(3, 4, [
            'Mass Confusion',
            'Force enemys to attack', 'themselves for 1 turn',
            '+5% per level'])

        # Inteligence
        self.skillBuilder(4, 0, [
            'Fire Ball',
            'Magic damage,', 'chance to burn',
            '+10% per level'], 1)

        self.skillBuilder(4, 1, [
            'Freezing Touch',
            'Magic damage,', 'chance to freeze',
            '+5% per level'], 1)

        self.skillBuilder(4, 2, [
            'Poison Breeze',
            'Chance to poison', 'all enemies',
            '+5% per level'], 1)

        self.skillBuilder(4, 3, [
            'Chain Lightning',
            'Damage all enemys,', 'chance to stun',
            '+5% per level'])

        self.skillBuilder(4, 4, [
            'Hurricane',
            'Damage to all enemys,', 'chance to confuse',
            '+15% per level'])

        # Agility
        self.skillBuilder(5, 0, [
            'Poison Darts',
            'Physical damage,', 'chance to poison',
            '+5% per level'], 1)

        self.skillBuilder(5, 1, [
            'Smoke Screen',
            '100% Critical hit buff,', 'cant be attacked',
            'Chance to poison'])

        self.skillBuilder(5, 2, [
            'Rain of Arrows',
            'Damage all opponents', '',
            'Ignore armor'])

        self.skillBuilder(5, 3, [
            'Isolate Target',
            'Damage to an opponent', 'multiple times',
            '+1 attack per level'], 1)

        self.skillBuilder(5, 4, [
            'Shadow Jump',
            'Instant backstab target,', 'chance to poison',
            '+1 target per level'], 1)

        # Love
        self.skillBuilder(6, 0, [
            'First Aid',
            'Cure an ally', '',
            '+15% per level'], 1)

        self.skillBuilder(6, 1, [
            'Blessed Aura',
            'Recover ally HP and MP', 'by turns',
            '+10% per level'], 1)

        self.skillBuilder(6, 2, [
            'Healing Allies',
            'Heal all party', '',
            '+10% per level'])

        self.skillBuilder(6, 3, [
            'Blessed Healing',
            'Heal an ally,', 'Fortify',
            '+5% per level'], 1)

        self.skillBuilder(6, 4, [
            'Divinity',
            "Replenishes party HP and MP,", "Fortify all",
            '+20% per level'])

    def skillBuilder(self, attrib, skill, lines, target=0):
        self.skillDesc[attrib][skill] = lines
        self.skillTarget[attrib][skill] = target

    def activate(self, attrib, skill, target, caster):
        print('\n\nFrom: ' + caster.name)
        if target:
            print('To: ' + target.name)
        else:
            print('To: no target')
        print('Atributo: ' + str(attrib))
        print('Skill: ' + str(skill))
        return(None)
