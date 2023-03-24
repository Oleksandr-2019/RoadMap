# Function check_zero
def check_zero(check_list):
    for x in range(len(check_list)):
        try:
            check_list.remove(0)
        finally:
            continue
    return check_list


# Function war - main function
def war(zombies, plants):
    survivors_zombies = zombies
    survivors_plants = plants

    # It is determined how many elements are in the
    # smallest list, since there will be battles only between
    # existing elements in both lists, and those that did not
    # fight - will not be changed, but will simply be overwritten
    # in the form in which they are.
    if len(zombies) < len(plants):
        number_fights = len(zombies)
    else:
        number_fights = len(plants)

    for x in range(number_fights):
        # Checking which element is larger in value.
        # If the element is larger, we overwrite it in the list.
        # If it is smaller, we write zero in the array instead.
        if survivors_zombies[x] > survivors_plants[x]:
            survivors_zombies[x] = (abs(survivors_zombies[x] - survivors_plants[x]))
            survivors_plants[x] = 0
        elif survivors_zombies[x] < survivors_plants[x]:
            survivors_plants[x] = (abs(plants[x] - survivors_zombies[x]))
            survivors_zombies[x] = 0

    # Check for null. If the element is zero, we remove it from the list.
    survivors_zombies = check_zero(survivors_zombies)
    survivors_plants = check_zero(survivors_plants)

    # Checking already processed party lists to see who won
    if len(survivors_zombies) < len(survivors_plants):
        print(True)
    elif len(survivors_zombies) > len(survivors_plants):
        print(False)
    else:
        if sum(survivors_zombies) < sum(survivors_plants):
            print(True)
        elif sum(survivors_zombies) == sum(survivors_plants):
            print(True)
        else:
            print(False)


# Function call
war([1, 3, 5, 7], [2, 4, 6, 8])
war([1, 3, 5, 7], [2, 4])
war([1, 3, 5, 7], [2, 4, 0, 8])
war([2, 1, 1, 1], [1, 2, 1, 1])
