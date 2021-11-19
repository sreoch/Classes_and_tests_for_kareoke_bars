class Guest:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def buy_room(self, room_cost):
        if self.money >= room_cost:
            self.money -= room_cost
        else:
            return "You cannot afford this room"
