from dangerbot.patrol import CompletePatrol


def test_initialization():
    patrol_test = CompletePatrol()
    assert patrol_test.get_suburb_number() == 7
    print("Next move will be in the direction ")
    print(patrol_test.get_next_pos())
    assert (0, 1) == patrol_test.get_next_pos()


def test_set_coords():
    patrol_test = CompletePatrol((47, 81))
    print(patrol_test.get_suburb_number())
    assert patrol_test.get_suburb_number() == 11
    print("Next move will be in the direction ")
    print(patrol_test.get_next_pos())
    assert (-1, -1) == patrol_test.get_next_pos()
    new_y = patrol_test.coords[0] + patrol_test.get_next_pos()[0]
    new_x = patrol_test.coords[1] + patrol_test.get_next_pos()[1]
    assert (new_x, new_y) == (80, 46)
    print("Moved to 80 - 46")


def test_malton_full_tour():
    patrol_test = CompletePatrol()
    move = patrol_test.get_next_pos()
    loc = patrol_test.coords
    patrol_test.set_pos((move[0] + loc[0], move[1] + loc[1]))
    moves = 1
    while (0, 0) != patrol_test.coords:
        move = patrol_test.get_next_pos()
        loc = patrol_test.coords
        patrol_test.set_pos((move[0] + loc[0], move[1] + loc[1]))
        moves += 1
    assert moves == 9982


if '__main__' == __name__:
    test_initialization()
    test_set_coords()
    test_malton_full_tour()
