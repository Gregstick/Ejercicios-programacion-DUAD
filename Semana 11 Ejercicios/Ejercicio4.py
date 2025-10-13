class Torso():
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Head():
    def __init__(self):
        self.eyes = 2
        self.nose = 1
        self.mouth = 1

class Hand():
    def __init__(self):
        self.fingers = 5

class Arm():
    def __init__(self, hand):
        self.hand = hand

class Leg():
    def __init__(self):
        self.foot = 1

class Feet():
    def __init__(self, leg):
        self.leg = leg

class Human():
    def __init__(self):
        self.head = Head()
        self.torso = Torso(self.head, self.right_arm, self.left_arm, self.right_leg, self.left_leg)
        self.right_hand = Hand()
        self.left_hand = Hand()
        self.right_arm = Arm(self.right_hand)
        self.left_arm = Arm(self.left_hand)
        self.right_foot = Feet()
        self.left_foot = Feet()
        self.right_leg = Leg(self.right_foot)
        self.left_leg = Leg(self.left_foot)



right_hand = Hand()
right_arm = Arm(right_hand)
left_hand = Hand()
left_arm = Arm(left_hand)
right_leg = Leg()
right_feet = Feet(right_leg)
left_leg = Leg()
left_feet = Feet(left_leg)
head = Head()
torso = Torso(head, right_arm, left_arm, right_leg, left_leg)
print({torso})




