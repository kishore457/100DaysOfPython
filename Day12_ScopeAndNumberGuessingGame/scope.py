enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function : {enemies}")

increase_enemies()
print(f"enemies outside function : {enemies}")

PI = 3.14159
print(PI)

# Example 2
game_level = 3
enemies = ["skeleton", "alien", "zombie"]
def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]
        print(new_enemy)
create_enemy()
# print(new_enemy)

# Example 3
enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function = {enemies}")
increase_enemies()
print(f"enemies outside function = {enemies}")

# Example 4 (Not recommended to modify the global variable modification inside function like below)
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function = {enemies}")
increase_enemies()
print(f"enemies outside function = {enemies}")

# Example 4 (recommended to return the global variable from the function and update the variable outside as below)
enemies = 1
def increase_enemies():
    print(f"enemies inside function = {enemies}")
    return enemies + 1
enemies = increase_enemies()
print(f"enemies ouside the function = {enemies}")