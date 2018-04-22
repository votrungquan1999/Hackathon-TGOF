import random

def generateCard():
    random_type = random.randrange(0, 100) % 3
    if random_type == 0:
        return generateSpell()
    elif random_type == 1:
        return generateMove()
    else:
        return generateAttack()

def generateSpell():
    file = open('card_catalog/spellCard.txt', 'r')
    file_r = file.read()
    end_num = file_r.count("\n") + 1
    random.seed()
    picked_line = random.randrange(1,end_num)
    file.close()

    file = open('card_catalog/spellCard.txt', 'r')
    stats = ""
    count = 0
    for line in file:
      if count == picked_line:
        stats = line.strip().split("|")
        break
      count += 1
    file.close()
    return SpellCard(stats[0],stats[7],stats[1],stats[2],stats[3],stats[4],stats[5],stats[6])

def generateMove():
    file = open('card_catalog/moveCard.txt', 'r')
    file_r = file.read()
    end_num = file_r.count("\n") + 1
    random.seed()
    picked_line = random.randrange(1,end_num)
    file.close()

    file = open('card_catalog/moveCard.txt', 'r')
    stats = ""
    count = 0
    for line in file:
      if count == picked_line:
        stats = line.strip().split("|")
        break
      count += 1
    file.close()
    return MoveCard(stats[0],stats[3],stats[1])

def generateAttack():
      file = open('card_catalog/attackCard.txt', 'r')
      file_r = file.read()
      end_num = file_r.count("\n") + 1
      random.seed()
      picked_line = random.randrange(1,end_num)
      file.close()

      file = open('card_catalog/attackCard.txt', 'r')
      stats = ""
      count = 0
      for line in file:
        if count == picked_line:
          stats = line.strip().split("|")
          break
        count += 1
      file.close()
      return AttackCard(stats[0],stats[2],stats[1])


class Card:
  def __init__(self, name, description):
    self.name = name
    self.type = "This card has no type!"
    self.description = description
  
  #Getters
  def getName(self):
    return self.name

  def getDescription(self):
    return self.description

  def getType(self):
    return self.type



class SpellCard(Card):
  def __init__(self, name, description, hp, attack, defense, luck, speed, attRange):
    Card.__init__(self, name, description)
    self.hp = hp
    self.attack = attack
    self.defense = defense
    self.luck = luck
    self.speed = speed
    self.attRange = attRange
    self.type = "Spell Card"
  
  #Getters
  def getHp(self):
    return self.hp
  
  def getAttack(self):
    return self.attack

  def getDefense(self):
    return self.defense

  def getLuck(self):
    return self.luck

  def getSpeed(self):
    return self.speed

  def getAttackRange(self):
    return self.attRange



"""  No need
  #Spell Card Effects
  def applyEffects(self, character):
    #Chracter will call this function
    #This call other apply functions
    pass
    self.applyAttack(character)
    self.applyDefense(character)
    self.applyHP(character)
    self.applyLuck(character)
    self.applyAttackRange(character)
    self.applySpeed(character)


  def applyHP(self, character):
    pass
    character.increaseHp(self.getHp())

  def applyAttack(self, character):
    pass
    character.setAttack(character.getAttack() + self.getAttack)
    character.increaseAttack(self.getAttack())
    

  def applyDefense(self, character):
    pass
    character.setAttack(getAttack() + self.getAttack)
    character.increaseAttack(self.getAttack())

  def applyLuck(self, character):
    pass
    character.setAttack(getAttack() + self.getAttack)
    character.increaseAttack(self.getAttack())
    
  def applySpeed(self, character):
    pass
    character.setAttack(getAttack() + self.getAttack)
    character.increaseAttack(self.getAttack())

  def applyAttackRange(self, character):
    pass
    character.setAttack(getAttack() + self.getAttack)
    character.increaseAttack(self.getAttack())
"""


class MoveCard(Card):
  def __init__(self, name, description, step):
    Card.__init__(self, name, description)
    self.type = "Move Card"
    self.step = step

  #Getters
  def getStep(self):
      return self.step

  """def generateCard(self, cardCatalog):
      x = cardCatalog.split('|')
      for j in x:
          self.name = x[0]
          self.step = x[1]
          self.description = x[2]"""



class AttackCard(Card):
    def __init__(self, name, description, attack):
        Card.__init__(self, name, description)
        self.type = "Attack Card"
        self.attack = attack

    def getAttack(self):
        return self.attack





