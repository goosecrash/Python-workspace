def main():
    print('Welcome to rpg game')
    global input_name
    input_name = 'Kendrew'
   












class Player:
    def __init__(self, value, health, name, magic):
        self.my_attribute = value
        self.health = health
        self.name = name
        self.magic = magic
    def get_attribute(self):
        return self.my_attribute

    def get_health(self):
        return self.health
    def get_name(self):
        return self.name
    def get_magic(self):
        return self.magic
class goblin:
    def __init__(self,magic,health):
        self.magic = magic
        self.health = health
    def get_magic(self):
        return self.magic
    def get_health(self):
        return self.health
    
def battle():
    print('You encountered goblin')
    global goblin_instance
    goblin_instance = goblin(30, 50)
    print(goblin_instance.get_magic)
    print(goblin_instance.get_health)


# creating an instance of Player
Player_name = input_name

instance = Player(10, 100, Player_name, 50)

# calling the get_attribute method
#print(instance.get_attribute())

# calling the get_health method
print(f'Health is {instance.get_health()}')
print(f'name is {instance.get_name()}')


# Main function

main()
battle()
print(input_name)
print(instance.get_name())



