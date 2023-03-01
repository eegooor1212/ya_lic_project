import pygame
from pprint import pprint
from random import randint, random, choice

stars_fields = []


def rounding(num):
    if num < 0:
        return 0
    if num - num // 1 > (num // 1 + 1) - num:
        return num // 1 + 1
    else:
        return num // 1


def run():
    screen.fill('#6495ed')
    pygame.draw.rect(screen, '#ff7514', ((0, 350), (900, 150)))
    running = True
    clock = pygame.time.Clock()
    undelete_list = []
    fps = 360
    start_coords = (0, 0)
    bd = Board(10, 10, 100, 20)
    ship1 = Ship(15, 15, 1, 1)
    ship2 = Ship(15, 55, 1, 2)
    ship3 = Ship(15, 120, 1, 3)
    ship4 = Ship(15, 210, 1, 4)
    undelete_list += [ship1, ship2, ship3, ship4, bd]
    flag = False
    does_exist = False
    very_important_list = [[True] * 10 for _ in range(10)]
    list_of_hits = [['пусто'] * 10 for _ in range(10)]
    list_of_hits_bot = [['корабль',
  'пусто',
  'пусто',
  'корабль',
  'корабль',
  'корабль',
  'пусто',
  'пусто',
  'корабль',
  'пусто'],
 ['корабль',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'корабль',
  'пусто'],
 ['пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто'],
 ['пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто'],
 ['корабль',
  'пусто',
  'пусто',
  'корабль',
  'корабль',
  'корабль',
  'корабль',
  'пусто',
  'пусто',
  'корабль'],
 ['пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто'],
 ['пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'корабль',
  'пусто',
  'пусто',
  'пусто',
  'пусто'],
 ['корабль',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто'],
 ['корабль',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'пусто',
  'корабль',
  'пусто'],
 ['корабль',
  'пусто',
  'пусто',
  'пусто',
  'корабль',
  'пусто',
  'пусто',
  'пусто',
  'корабль',
  'пусто']]
    very_important_list_bot = [[True] * 10 for _ in range(10)]
    another_flag = False
    count_of_one = 0
    count_of_two = 0
    count_of_three = 0
    count_of_four = 0
    is_in_game = False
    prev_undel_list = []
    while running:
        if not is_in_game:
            screen.fill('#5f9ea0')
            pygame.draw.rect(screen, '#ff7514', ((0, 350), (900, 150)))
            for elem in undelete_list:
                elem.render()
            if does_exist:
                current_ship.render()
        if count_of_one == 4:
            if ship1 in undelete_list:
                undelete_list.remove(ship1)
        else:
            if ship1 not in undelete_list:
                undelete_list.insert(0, ship1)
        if count_of_two == 3:
            if ship2 in undelete_list:
                undelete_list.remove(ship2)
        else:
            if ship2 not in undelete_list:
                undelete_list.insert(1, ship2)
        if count_of_three == 2:
            if ship3 in undelete_list:
                undelete_list.remove(ship3)
        else:
            if ship3 not in undelete_list:
                undelete_list.insert(2, ship3)
        if count_of_four == 1:
            if ship4 in undelete_list:
                undelete_list.remove(ship4)
        else:
            if ship4 not in undelete_list:
                undelete_list.insert(3, ship4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_coords = event.pos
                if not is_in_game:
                    screen.fill('#5f9ea0')
                    pygame.draw.rect(screen, '#ff7514', ((0, 350), (900, 150)))
                    if count_of_one == 4:
                        if ship1 in undelete_list:
                            undelete_list.remove(ship1)
                    else:
                        if ship1 not in undelete_list:
                            undelete_list.insert(0, ship1)
                    if count_of_two == 3:
                        if ship2 in undelete_list:
                            undelete_list.remove(ship2)
                    else:
                        if ship2 not in undelete_list:
                            undelete_list.insert(1, ship2)
                    if count_of_three == 2:
                        if ship3 in undelete_list:
                            undelete_list.remove(ship3)
                    else:
                        if ship3 not in undelete_list:
                            undelete_list.insert(2, ship3)
                    if count_of_four == 1:
                        if ship4 in undelete_list:
                            undelete_list.remove(ship4)
                    else:
                        if ship4 not in undelete_list:
                            undelete_list.insert(3, ship4)
                    for elem in undelete_list:
                        elem.render()
                    if not is_in_game:
                        my_list = ship1.check_coord()
                        if my_list[0] <= event.pos[0] <= my_list[2] and my_list[1] <= event.pos[1] <= my_list[3]:
                            if count_of_one < 4:
                                current_ship = ship1.copy()
                                flag = True
                                does_exist = True
                                count_of_one += 1
                        my_list = ship2.check_coord()
                        if my_list[0] <= event.pos[0] <= my_list[2] and my_list[1] <= event.pos[1] <= my_list[3]:
                            if count_of_two < 3:
                                current_ship = ship2.copy()
                                flag = True
                                does_exist = True
                                count_of_two += 1
                        my_list = ship3.check_coord()
                        if my_list[0] <= event.pos[0] <= my_list[2] and my_list[1] <= event.pos[1] <= my_list[3]:
                            if count_of_three < 2:
                                current_ship = ship3.copy()
                                flag = True
                                does_exist = True
                                count_of_three += 1
                        my_list = ship4.check_coord()
                        if my_list[0] <= event.pos[0] <= my_list[2] and my_list[1] <= event.pos[1] <= my_list[3]:
                            if count_of_four < 1:
                                current_ship = ship4.copy()
                                flag = True
                                does_exist = True
                                count_of_four += 1
                        if does_exist:
                            my_list = current_ship.check_coord()
                            if my_list[0] <= event.pos[0] <= my_list[2] and my_list[1] <= event.pos[1] <= my_list[3]:
                                flag = True
                                does_exist = True
                else:
                    if bd2.get_cell(start_coords) is not None:
                        position = bd2.get_cell(start_coords)
                        print(list_of_hits_bot[position[1]][position[0]])
                        if list_of_hits_bot[position[1]][position[0]] != 'пусто':
                            if list_of_hits_bot[position[1]][position[0]] == 'корабль':
                                list_of_hits_bot[position[1]][position[0]] = 'ранен'
                                bd2.change_field(position[0], position[1], 1)
                                flag1 = True
                                flag2 = True
                                flag3 = True
                                flag4 = True
                                smth_flag = False
                                num1 = 0
                                num2 = 0
                                num3 = 0
                                num4 = 0
                                for i in range(5):
                                    if flag1 and 0 <= position[1] - i <= 9:
                                        if list_of_hits_bot[position[1] - i][position[0]] == 'корабль':
                                            break
                                        if list_of_hits_bot[position[1] - i][position[0]] == 'пусто':
                                            flag1 = False
                                        else:
                                            num1 += 1
                                    if flag2 and 0 <= position[0] - i <= 9:
                                        if list_of_hits_bot[position[1]][position[0] - i] == 'корабль':
                                            break
                                        if list_of_hits_bot[position[1]][position[0] - i] == 'пусто':
                                            flag2 = False
                                        else:
                                            num2 += 1
                                    if flag3 and 0 <= position[1] + i <= 9:
                                        if list_of_hits_bot[position[1] + i][position[0]] == 'корабль':
                                            break
                                        if list_of_hits_bot[position[1] + i][position[0]] == 'пусто':
                                            flag3 = False
                                        else:
                                            num3 += 1
                                    if flag4 and 0 <= position[0] + i <= 9:
                                        if list_of_hits_bot[position[1]][position[0] + i] == 'корабль':
                                            break
                                        if list_of_hits_bot[position[1]][position[0] + i] != 'ранен':
                                            flag4 = False
                                        else:
                                            num4 += 1
                                else:
                                    if num1 != 1 or num2 != 1:
                                        if num1 != 1:
                                            start_pos = (position[0], position[1] - num1)
                                        else:
                                            start_pos = (position[0] - num2, position[1])
                                    else:
                                        start_pos = position
                                    smth_flag = True
                                if smth_flag:
                                    if num1 != 1 or num2 != 1:
                                        if num1 != 1:
                                            start_pos = (position[0], position[1] - num1 + 1)
                                        else:
                                            start_pos = (position[0] - num2 + 1, position[1])
                                    else:
                                        start_pos = position
                                    w = num2 + num4 - 1
                                    h = num1 + num3 - 1
                                    i1 = start_pos[0]
                                    j1 = start_pos[1]
                                    print(1)
                                    print(start_pos)
                                    print(w, h)
                                    print(num1)
                                    print(num2)
                                    for i in range(i1, i1 + w):
                                        for j in range(j1, j1 + h):
                                            list_of_hits_bot[j][i] = 'убит'
                                    for a in range(i1 - 1, i1 + w + 1):
                                        for j in range(j1 - 1, j1 + h + 1):
                                            if 0 <= a < 10 and 0 <= j < 10:
                                                if list_of_hits_bot[j][a] != 'убит':
                                                    list_of_hits_bot[j][a] = 'мимо'
                                                    bd2.change_field(a, j, 0)
                                    num1 = 0
                                    num2 = 0
                                    num3 = 0
                                    num4 = 0
                        else:
                            x, y = position
                            if 0 <= x + 1 < 10:
                                if list_of_hits_bot[y][x + 1] == 'убит':
                                    break
                            if 0 <= x - 1 < 10:
                                if list_of_hits_bot[y][x - 1] == 'убит':
                                    break
                            if 0 <= y + 1 < 10:
                                if list_of_hits_bot[y + 1][x] == 'убит':
                                    break
                            if 0 <= y - 1 < 10:
                                if list_of_hits_bot[y - 1][x] == 'убит':
                                    break
                            bd2.change_field(position[0], position[1], 0)
                            print(0)
            if event.type == pygame.MOUSEMOTION:
                if not is_in_game:
                    if flag:
                        screen.fill('#5f9ea0')
                        pygame.draw.rect(screen, '#ff7514', ((0, 350), (900, 150)))
                        if count_of_one == 4:
                            if ship1 in undelete_list:
                                undelete_list.remove(ship1)
                        else:
                            if ship1 not in undelete_list:
                                undelete_list.insert(0, ship1)
                        if count_of_two == 3:
                            if ship2 in undelete_list:
                                undelete_list.remove(ship2)
                        else:
                            if ship2 not in undelete_list:
                                undelete_list.insert(1, ship2)
                        if count_of_three == 2:
                            if ship3 in undelete_list:
                                undelete_list.remove(ship3)
                        else:
                            if ship3 not in undelete_list:
                                undelete_list.insert(2, ship3)
                        if count_of_four == 1:
                            if ship4 in undelete_list:
                                undelete_list.remove(ship4)
                        else:
                            if ship4 not in undelete_list:
                                undelete_list.insert(3, ship4)
                        position = event.pos
                        delta_x = position[0] - start_coords[0]
                        delta_y = position[1] - start_coords[1]
                        current_ship.set_coord(delta_x, delta_y)
                        for elem in undelete_list:
                            elem.render()
                        if does_exist:
                            current_ship.render()
                        start_coords = position
            if event.type == pygame.MOUSEBUTTONUP:
                if not is_in_game:
                    if flag:
                        my_list5 = list(elem for elem in current_ship.get_coords())
                        first = bd.get_cell_new(my_list5[0])
                        third = bd.get_cell_new(my_list5[1])
                        width, height = current_ship.get_size()
                        left, top = bd.get_left_and_top()
                        if '' not in first or '' not in third:
                            if '' not in first and '' not in third:
                                current_ship.change_coords((rounding(first[0])) * 25 + left,
                                                           rounding(first[1]) * 25 + top)
                                first = current_ship.get_left_up_corner()
                                flag_n = True
                                i1, j1 = bd.get_cell(first)
                                i1 = int(i1)
                                j1 = int(j1)
                                w, h = current_ship.get_size()
                                if w == h:
                                    if not very_important_list[j1][i1]:
                                        flag_n = False
                                        if current_ship.get_class() == 1:
                                            count_of_one -= 1
                                        if current_ship.get_class() == 2:
                                            count_of_two -= 1
                                        if current_ship.get_class() == 3:
                                            count_of_three -= 1
                                        if current_ship.get_class() == 4:
                                            count_of_four -= 1
                                elif max(w, h) == w:
                                    for i in range(i1, i1 + w):
                                        if not very_important_list[j1][i]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                            break
                                else:
                                    for i in range(j1, j1 + height):
                                        if not very_important_list[i][i1]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                            break
                                if flag_n:
                                    undelete_list.append(current_ship)
                                    for i in range(i1 - 1, i1 + w + 1):
                                        for j in range(j1 - 1, j1 + h + 1):
                                            if 0 <= i < 10 and 0 <= j < 10:
                                                very_important_list[j][i] = False
                                    for i in range(i1, i1 + w):
                                        for j in range(j1, j1 + h):
                                            list_of_hits[j][i] = 'корабль'
                                does_exist = False
                            if first.count('') == 1:
                                if first[0] == '':
                                    left, top = bd.get_left_and_top()
                                    current_ship.change_coords(0 * 25 + left,
                                                               rounding(first[1]) * 25 + top)
                                    first = current_ship.get_left_up_corner()
                                    flag_n = True
                                    i1, j1 = bd.get_cell(first)
                                    i1 = int(i1)
                                    j1 = int(j1)
                                    w, h = current_ship.get_size()
                                    if w == h:
                                        if not very_important_list[j1][i1]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                    elif max(w, h) == w:
                                        for i in range(i1, i1 + w):
                                            if not very_important_list[j1][i]:
                                                flag_n = False
                                                if current_ship.get_class() == 1:
                                                    count_of_one -= 1
                                                if current_ship.get_class() == 2:
                                                    count_of_two -= 1
                                                if current_ship.get_class() == 3:
                                                    count_of_three -= 1
                                                if current_ship.get_class() == 4:
                                                    count_of_four -= 1
                                                break
                                    else:
                                        for i in range(j1, j1 + height):
                                            if not very_important_list[i][i1]:
                                                flag_n = False
                                                if current_ship.get_class() == 1:
                                                    count_of_one -= 1
                                                if current_ship.get_class() == 2:
                                                    count_of_two -= 1
                                                if current_ship.get_class() == 3:
                                                    count_of_three -= 1
                                                if current_ship.get_class() == 4:
                                                    count_of_four -= 1
                                                break
                                    if flag_n:
                                        undelete_list.append(current_ship)
                                        for i in range(i1 - 1, i1 + w + 1):
                                            for j in range(j1 - 1, j1 + h + 1):
                                                if 0 <= i < 10 and 0 <= j < 10:
                                                    very_important_list[j][i] = False
                                        for i in range(i1, i1 + w):
                                            for j in range(j1, j1 + h):
                                                list_of_hits[j][i] = 'корабль'
                                    does_exist = False
                                if first[1] == '':
                                    left, top = bd.get_left_and_top()
                                    current_ship.change_coords(rounding(first[0]) * 25 + left,
                                                               0 * 25 + top)
                                    first = current_ship.get_left_up_corner()
                                    flag_n = True
                                    i1, j1 = bd.get_cell(first)
                                    i1 = int(i1)
                                    j1 = int(j1)
                                    w, h = current_ship.get_size()
                                    if w == h:
                                        if not very_important_list[j1][i1]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                    elif max(w, h) == w:
                                        for i in range(i1, i1 + w):
                                            if not very_important_list[j1][i]:
                                                flag_n = False
                                                if current_ship.get_class() == 1:
                                                    count_of_one -= 1
                                                if current_ship.get_class() == 2:
                                                    count_of_two -= 1
                                                if current_ship.get_class() == 3:
                                                    count_of_three -= 1
                                                if current_ship.get_class() == 4:
                                                    count_of_four -= 1
                                                break
                                    else:
                                        for i in range(j1, j1 + height):
                                            if not very_important_list[i][i1]:
                                                flag_n = False
                                                if current_ship.get_class() == 1:
                                                    count_of_one -= 1
                                                if current_ship.get_class() == 2:
                                                    count_of_two -= 1
                                                if current_ship.get_class() == 3:
                                                    count_of_three -= 1
                                                if current_ship.get_class() == 4:
                                                    count_of_four -= 1
                                                break
                                    if flag_n:
                                        undelete_list.append(current_ship)
                                        for i in range(i1 - 1, i1 + w + 1):
                                            for j in range(j1 - 1, j1 + h + 1):
                                                if 0 <= i < 10 and 0 <= j < 10:
                                                    very_important_list[j][i] = False
                                        for i in range(i1, i1 + w):
                                            for j in range(j1, j1 + h):
                                                list_of_hits[j][i] = 'корабль'
                                    does_exist = False
                            elif first.count('') == 2:
                                left, top = bd.get_left_and_top()
                                current_ship.change_coords(0 * 25 + left,
                                                           0 * 25 + top)
                                first = current_ship.get_left_up_corner()
                                flag_n = True
                                i1, j1 = bd.get_cell(first)
                                i1 = int(i1)
                                j1 = int(j1)
                                w, h = current_ship.get_size()
                                if w == h:
                                    if not very_important_list[j1][i1]:
                                        flag_n = False
                                        if current_ship.get_class() == 1:
                                            count_of_one -= 1
                                        if current_ship.get_class() == 2:
                                            count_of_two -= 1
                                        if current_ship.get_class() == 3:
                                            count_of_three -= 1
                                        if current_ship.get_class() == 4:
                                            count_of_four -= 1
                                elif max(w, h) == w:
                                    for i in range(i1, i1 + w):
                                        if not very_important_list[j1][i]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                            break
                                else:
                                    for i in range(j1, j1 + height):
                                        if not very_important_list[i][i1]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                            break
                                if flag_n:
                                    undelete_list.append(current_ship)
                                    for i in range(i1 - 1, i1 + w + 1):
                                        for j in range(j1 - 1, j1 + h + 1):
                                            if 0 <= i < 10 and 0 <= j < 10:
                                                very_important_list[j][i] = False
                                    for i in range(i1, i1 + w):
                                        for j in range(j1, j1 + h):
                                            list_of_hits[j][i] = 'корабль'
                                does_exist = False
                            if third.count('') == 1:
                                if third[0] == '':
                                    left, top = bd.get_left_and_top()
                                    current_ship.change_coords((10 - width) * 25 + left,
                                                               rounding(first[1]) * 25 + top)
                                    first = current_ship.get_left_up_corner()
                                    flag_n = True
                                    i1, j1 = bd.get_cell(first)
                                    i1 = int(i1)
                                    j1 = int(j1)
                                    w, h = current_ship.get_size()
                                    if w == h:
                                        if not very_important_list[j1][i1]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                    elif max(w, h) == w:
                                        for i in range(i1, i1 + w):
                                            if not very_important_list[j1][i]:
                                                flag_n = False
                                                if current_ship.get_class() == 1:
                                                    count_of_one -= 1
                                                if current_ship.get_class() == 2:
                                                    count_of_two -= 1
                                                if current_ship.get_class() == 3:
                                                    count_of_three -= 1
                                                if current_ship.get_class() == 4:
                                                    count_of_four -= 1
                                                break
                                    else:
                                        for i in range(j1, j1 + height):
                                            if not very_important_list[i][i1]:
                                                flag_n = False
                                                if current_ship.get_class() == 1:
                                                    count_of_one -= 1
                                                if current_ship.get_class() == 2:
                                                    count_of_two -= 1
                                                if current_ship.get_class() == 3:
                                                    count_of_three -= 1
                                                if current_ship.get_class() == 4:
                                                    count_of_four -= 1
                                                break
                                    if flag_n:
                                        undelete_list.append(current_ship)
                                        for i in range(i1 - 1, i1 + w + 1):
                                            for j in range(j1 - 1, j1 + h + 1):
                                                if 0 <= i < 10 and 0 <= j < 10:
                                                    very_important_list[j][i] = False
                                        for i in range(i1, i1 + w):
                                            for j in range(j1, j1 + h):
                                                list_of_hits[j][i] = 'корабль'
                                    does_exist = False
                                if third[1] == '':
                                    left, top = bd.get_left_and_top()
                                    current_ship.change_coords(rounding(first[0]) * 25 + left,
                                                               (10 - height) * 25 + top)
                                    first = current_ship.get_left_up_corner()
                                    flag_n = True
                                    i1, j1 = bd.get_cell(first)
                                    i1 = int(i1)
                                    j1 = int(j1)
                                    w, h = current_ship.get_size()
                                    if w == h:
                                        if not very_important_list[j1][i1]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                    elif max(w, h) == w:
                                        for i in range(i1, i1 + w):
                                            if not very_important_list[j1][i]:
                                                flag_n = False
                                                if current_ship.get_class() == 1:
                                                    count_of_one -= 1
                                                if current_ship.get_class() == 2:
                                                    count_of_two -= 1
                                                if current_ship.get_class() == 3:
                                                    count_of_three -= 1
                                                if current_ship.get_class() == 4:
                                                    count_of_four -= 1
                                                break
                                    else:
                                        for i in range(j1, j1 + height):
                                            if not very_important_list[i][i1]:
                                                flag_n = False
                                                if current_ship.get_class() == 1:
                                                    count_of_one -= 1
                                                if current_ship.get_class() == 2:
                                                    count_of_two -= 1
                                                if current_ship.get_class() == 3:
                                                    count_of_three -= 1
                                                if current_ship.get_class() == 4:
                                                    count_of_four -= 1
                                                break
                                    if flag_n:
                                        undelete_list.append(current_ship)
                                        for i in range(i1 - 1, i1 + w + 1):
                                            for j in range(j1 - 1, j1 + h + 1):
                                                if 0 <= i < 10 and 0 <= j < 10:
                                                    very_important_list[j][i] = False
                                        for i in range(i1, i1 + w):
                                            for j in range(j1, j1 + h):
                                                list_of_hits[j][i] = 'корабль'
                                    does_exist = False
                            elif third.count('') == 2:
                                left, top = bd.get_left_and_top()
                                current_ship.change_coords((10 - width) * 25 + left,
                                                           (10 - height) * 25 + top)
                                first = current_ship.get_left_up_corner()
                                flag_n = True
                                i1, j1 = bd.get_cell(first)
                                i1 = int(i1)
                                j1 = int(j1)
                                w, h = current_ship.get_size()
                                if w == h:
                                    if not very_important_list[j1][i1]:
                                        flag_n = False
                                        if current_ship.get_class() == 1:
                                            count_of_one -= 1
                                        if current_ship.get_class() == 2:
                                            count_of_two -= 1
                                        if current_ship.get_class() == 3:
                                            count_of_three -= 1
                                        if current_ship.get_class() == 4:
                                            count_of_four -= 1
                                elif max(w, h) == w:
                                    for i in range(i1, i1 + w):
                                        if not very_important_list[j1][i]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                            break
                                else:
                                    for i in range(j1, j1 + height):
                                        if not very_important_list[i][i1]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                            break
                                if flag_n:
                                    undelete_list.append(current_ship)
                                    for i in range(i1 - 1, i1 + w + 1):
                                        for j in range(j1 - 1, j1 + h + 1):
                                            if 0 <= i < 10 and 0 <= j < 10:
                                                very_important_list[j][i] = False
                                    for i in range(i1, i1 + w):
                                        for j in range(j1, j1 + h):
                                            list_of_hits[j][i] = 'корабль'
                                does_exist = False
                        else:
                            second, fourth = current_ship.get_another_coords()
                            second = bd.get_cell_new(second)
                            fourth = bd.get_cell_new(fourth)
                            if '' not in fourth:
                                current_ship.change_coords(left, (10 - height) * 25 + top)
                                first = current_ship.get_left_up_corner()
                                flag_n = True
                                i1, j1 = bd.get_cell(first)
                                i1 = int(i1)
                                j1 = int(j1)
                                w, h = current_ship.get_size()
                                if w == h:
                                    if not very_important_list[j1][i1]:
                                        flag_n = False
                                        if current_ship.get_class() == 1:
                                            count_of_one -= 1
                                        if current_ship.get_class() == 2:
                                            count_of_two -= 1
                                        if current_ship.get_class() == 3:
                                            count_of_three -= 1
                                        if current_ship.get_class() == 4:
                                            count_of_four -= 1
                                elif max(w, h) == w:
                                    for i in range(i1, i1 + w):
                                        if not very_important_list[j1][i]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                            break
                                else:
                                    for i in range(j1, j1 + height):
                                        if not very_important_list[i][i1]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                            break
                                if flag_n:
                                    undelete_list.append(current_ship)
                                    for i in range(i1 - 1, i1 + w + 1):
                                        for j in range(j1 - 1, j1 + h + 1):
                                            if 0 <= i < 10 and 0 <= j < 10:
                                                very_important_list[j][i] = False
                                    for i in range(i1, i1 + w):
                                        for j in range(j1, j1 + h):
                                            list_of_hits[j][i] = 'корабль'
                                does_exist = False
                            elif '' not in second:
                                current_ship.change_coords((10 - width) * 25 + left, top)
                                first = current_ship.get_left_up_corner()
                                flag_n = True
                                i1, j1 = bd.get_cell(first)
                                i1 = int(i1)
                                j1 = int(j1)
                                w, h = current_ship.get_size()
                                if w == h:
                                    if not very_important_list[j1][i1]:
                                        flag_n = False
                                        if current_ship.get_class() == 1:
                                            count_of_one -= 1
                                        if current_ship.get_class() == 2:
                                            count_of_two -= 1
                                        if current_ship.get_class() == 3:
                                            count_of_three -= 1
                                        if current_ship.get_class() == 4:
                                            count_of_four -= 1
                                elif max(w, h) == w:
                                    for i in range(i1, i1 + w):
                                        if not very_important_list[j1][i]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                            break
                                else:
                                    for i in range(j1, j1 + height):
                                        if not very_important_list[i][i1]:
                                            flag_n = False
                                            if current_ship.get_class() == 1:
                                                count_of_one -= 1
                                            if current_ship.get_class() == 2:
                                                count_of_two -= 1
                                            if current_ship.get_class() == 3:
                                                count_of_three -= 1
                                            if current_ship.get_class() == 4:
                                                count_of_four -= 1
                                            break
                                if flag_n:
                                    undelete_list.append(current_ship)
                                    for i in range(i1 - 1, i1 + w + 1):
                                        for j in range(j1 - 1, j1 + h + 1):
                                            if 0 <= i < 10 and 0 <= j < 10:
                                                very_important_list[j][i] = False
                                    for i in range(i1, i1 + w):
                                        for j in range(j1, j1 + h):
                                            list_of_hits[j][i] = 'корабль'
                                does_exist = False
                    flag = False
                    screen.fill('#5f9ea0')
                    pygame.draw.rect(screen, '#ff7514', ((0, 350), (900, 150)))
                if count_of_one == 4:
                    if ship1 in undelete_list:
                        undelete_list.remove(ship1)
                else:
                    if ship1 not in undelete_list:
                        undelete_list.insert(0, ship1)
                if count_of_two == 3:
                    if ship2 in undelete_list:
                        undelete_list.remove(ship2)
                else:
                    if ship2 not in undelete_list:
                        undelete_list.insert(1, ship2)
                if count_of_three == 2:
                    if ship3 in undelete_list:
                        undelete_list.remove(ship3)
                else:
                    if ship3 not in undelete_list:
                        undelete_list.insert(2, ship3)
                if count_of_four == 1:
                    if ship4 in undelete_list:
                        undelete_list.remove(ship4)
                else:
                    if ship4 not in undelete_list:
                        undelete_list.insert(3, ship4)
                if not is_in_game:
                    for elem in undelete_list:
                        elem.render()
                    if does_exist:
                        current_ship.render()
            if event.type == pygame.KEYDOWN:
                if not is_in_game:
                    if event.key == pygame.K_r:
                        if current_ship not in undelete_list:
                            current_ship.change_w_and_h()
                            screen.fill('#5f9ea0')
                            pygame.draw.rect(screen, '#ff7514', ((0, 350), (900, 150)))
                            if count_of_one == 4:
                                if ship1 in undelete_list:
                                    undelete_list.remove(ship1)
                            else:
                                if ship1 not in undelete_list:
                                    undelete_list.insert(0, ship1)
                            if count_of_two == 3:
                                if ship2 in undelete_list:
                                    undelete_list.remove(ship2)
                            else:
                                if ship2 not in undelete_list:
                                    undelete_list.insert(1, ship2)
                            if count_of_three == 2:
                                if ship3 in undelete_list:
                                    undelete_list.remove(ship3)
                            else:
                                if ship3 not in undelete_list:
                                    undelete_list.insert(2, ship3)
                            if count_of_four == 1:
                                if ship4 in undelete_list:
                                    undelete_list.remove(ship4)
                            else:
                                if ship4 not in undelete_list:
                                    undelete_list.insert(3, ship4)
                            for elem in undelete_list:
                                elem.render()
                            if does_exist:
                                current_ship.render()
                if event.key == pygame.K_d:
                    if not is_in_game:
                        another_flag = True
                if event.key != pygame.K_d and event.key != pygame.K_a and event.key != pygame.K_l:
                    if not is_in_game:
                        another_flag = False
                if event.key == pygame.K_l:
                    if another_flag:
                        if len(undelete_list) > 5 or ship1 not in undelete_list or ship2 not in undelete_list or ship3 \
                                not in undelete_list or ship4 not in undelete_list:
                            elem = undelete_list[-1]
                            if int(elem.get_class()) == 1:
                                count_of_one -= 1
                            elif int(elem.get_class()) == 2:
                                count_of_two -= 1
                            elif int(elem.get_class()) == 3:
                                count_of_three -= 1
                            elif int(elem.get_class()) == 4:
                                count_of_four -= 1
                            if count_of_one >= 4:
                                if ship1 in undelete_list:
                                    undelete_list.remove(ship1)
                            else:
                                if ship1 not in undelete_list:
                                    undelete_list.insert(0, ship1)
                            if count_of_two >= 3:
                                if ship2 in undelete_list:
                                    undelete_list.remove(ship2)
                            else:
                                if ship2 not in undelete_list:
                                    undelete_list.insert(1, ship2)
                            if count_of_three >= 2:
                                if ship3 in undelete_list:
                                    undelete_list.remove(ship3)
                            else:
                                if ship3 not in undelete_list:
                                    undelete_list.insert(2, ship3)
                            if count_of_four >= 1:
                                if ship4 in undelete_list:
                                    undelete_list.remove(ship4)
                            else:
                                if ship4 not in undelete_list:
                                    undelete_list.insert(3, ship4)
                            undelete_list = undelete_list[:len(undelete_list) - 1]
                            coord = elem.get_coords()[0]
                            i1, j1 = bd.get_cell(coord)
                            i1 = int(i1)
                            j1 = int(j1)
                            w, h = elem.get_size()
                            for i in range(i1 - 1, i1 + w + 1):
                                for j in range(j1 - 1, j1 + h + 1):
                                    if 0 <= i < 10 and 0 <= j < 10:
                                        very_important_list[j][i] = True
                            for i in range(i1, i1 + w):
                                for j in range(j1, j1 + h):
                                    list_of_hits[j][i] = 'пусто'
                    another_flag = False
                if event.key == pygame.K_a:
                    if not is_in_game:
                        if another_flag:
                            count_of_one = 0
                            count_of_two = 0
                            count_of_three = 0
                            count_of_four = 0
                            if count_of_one == 4:
                                if ship1 in undelete_list:
                                    undelete_list.remove(ship1)
                            else:
                                if ship1 not in undelete_list:
                                    undelete_list.insert(0, ship1)
                            if count_of_two == 3:
                                if ship2 in undelete_list:
                                    undelete_list.remove(ship2)
                            else:
                                if ship2 not in undelete_list:
                                    undelete_list.insert(1, ship2)
                            if count_of_three == 2:
                                if ship3 in undelete_list:
                                    undelete_list.remove(ship3)
                            else:
                                if ship3 not in undelete_list:
                                    undelete_list.insert(2, ship3)
                            if count_of_four == 1:
                                if ship4 in undelete_list:
                                    undelete_list.remove(ship4)
                            else:
                                if ship4 not in undelete_list:
                                    undelete_list.insert(3, ship4)
                            undelete_list = undelete_list[:5]
                            very_important_list = [[True] * 10 for _ in range(10)]
                            list_of_hits = [['пусто'] * 10 for _ in range(10)]
                        another_flag = False
                if event.key == pygame.K_f:
                    if not is_in_game:
                        if count_of_one == 4 and count_of_two == 3 and count_of_three == 2 and count_of_four == 1:
                            is_in_game = True
                            prev_undel_list = [bd, ship1, ship2, ship3, ship4]
                            pprint(list_of_hits)
                            bot = Bot_for_fight(list_of_hits_bot, very_important_list_bot, 0, 0)
                            bot.create_of_field()
                            list_of_hits_bot = bot.get_lists()
                            bd2 = Board(10, 10, 550, 20)
                            undelete_list.append(bd2)
                if event.key == pygame.K_ESCAPE:
                    is_in_game = False
                    undelete_list = prev_undel_list
                    very_important_list = [[True] * 10 for _ in range(10)]
                    list_of_hits = [['пусто'] * 10 for _ in range(10)]
                    count_of_one = 0
                    count_of_two = 0
                    count_of_three = 0
                    count_of_four = 0
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


class Board:
    def __init__(self, width, height, left, top):
        self.width = width
        self.height = height
        self.color_list = []
        self.left = left
        self.top = top
        self.cell = 25
        self.board = []
        for i in range(self.height):
            inside_list = []
            inside_list_of_color = []
            for j in range(self.width):
                inside_list_of_color.append('#5f9ea0')
                pygame.draw.rect(screen, '#ffcf48', ((0, 350), (900, 150)))
                inside_list.append(pygame.draw.rect(screen, 'white',
                                                    ((self.left + self.cell * j, self.top + self.cell * i),
                                                     (self.cell, self.cell)), 1))
            self.board.append(inside_list)
            self.color_list.append(inside_list_of_color)

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                color = self.color_list[i][j]
                pygame.draw.rect(screen, color,
                                 ((self.left + self.cell * i, self.top + self.cell * j),
                                  (self.cell, self.cell)))
        for i in range(self.height):
            inside_list = []
            inside_list_of_color = []
            for j in range(self.width):
                inside_list_of_color.append('white')
                inside_list.append(pygame.draw.rect(screen, 'white',
                                                    ((self.left + self.cell * i, self.top + self.cell * j),
                                                     (self.cell, self.cell)), 1))

    def set_view(self, new_width, new_height, new_cell):
        self.width = new_width
        self.height = new_height
        self.cell = new_cell

    def get_cell(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        if self.left <= x <= self.width * self.cell + self.left and self.top <= y <= self.height * self.cell + self.top:
            x -= self.left
            y -= self.top
            return (x // self.cell), (y // self.cell)
        else:
            return None

    # Это функция для кораблей
    def get_cell_new(self, mouse_pos):
        i = ''
        j = ''
        x = mouse_pos[0]
        y = mouse_pos[1]
        if self.left <= x <= self.width * self.cell + self.left:
            x -= self.left
            i = x / self.cell
        if self.top <= y <= self.height * self.cell + self.top:
            y -= self.top
            j = y / self.cell
        return [i, j]

    def set_color(self, pos, color):
        i, j = self.get_cell(pos)
        pygame.draw.rect(screen, color, ((20 + (i * 25) + 1, 20 + (j * 25) + 1), (24, 24)))
        self.color_list[i][j] = color

    def final_step(self, pos1, pos2, pos3, pos4):
        if self.get_cell(pos1) and self.get_cell(pos4):
            pass

    def get_left_and_top(self):
        return self.left, self.top

    def change_field(self, x, y, n):
        if n == 1:
            pygame.draw.line(screen, 'red', (self.left + x * 25, self.top + y * 25),
                             (self.left + (x + 1) * self.cell - 1, self.top + (y + 1) * 25 - 1), 2)
            pygame.draw.line(screen, 'red', (self.left + x * self.cell, self.top + (y + 1) * 25 - 1),
                             (self.left + (x + 1) * self.cell - 1, self.top + y * 25), 2)
        else:
            pygame.draw.line(screen, 'white', (self.left + x * 25, self.top + y * 25),
                             (self.left + (x + 1) * self.cell - 1, self.top + (y + 1) * 25 - 1), 2)
            pygame.draw.line(screen, 'white', (self.left + x * self.cell, self.top + (y + 1) * 25 - 1),
                             (self.left + (x + 1) * self.cell - 1, self.top + y * 25), 2)


class Ship:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inside_class = max(width, height)

    def render(self):
        pygame.draw.rect(screen, 'coral', ((self.x, self.y), (self.width * 25, self.height * 25)))

    def set_coord(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_coords(self):
        return (self.x, self.y), (self.x + (25 * self.width), self.y + (25 * self.height))

    def check_coord(self):
        return [self.x, self.y, self.x + (25 * self.width), self.y + (25 * self.height)]

    def copy(self):
        return Ship(self.x, self.y, self.width, self.height)

    def change_coords(self, x, y):
        self.x = x
        self.y = y

    def get_size(self):
        return self.width, self.height

    def get_another_coords(self):
        return [self.x, self.y + 25 * self.height], [self.x + 25 * self.width, self.y]

    def change_w_and_h(self):
        self.width, self.height = self.height, self.width

    def get_class(self):
        return self.inside_class

    def get_left_up_corner(self):
        return self.x, self.y


class Bot_for_fight:
    def __init__(self, list_of_hits, undeletable_list, left, top):
        self.list_of_hits = list_of_hits
        self.undeletable_list = undeletable_list
        self.coord_list = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        self.left = left
        self.top = top
        self.flag_of_ship = False
        self.start_coord = (0, 0)
        self.that_need_to_change = None
        self.list_of_coord = []
        self.veryvery_imp_list = [[(0, 0), 2], [(0, 3), 3], [(0, 8), 2], [(4, 3), 4], [(7, 0), 3], [(8, 8), 2]]

    def create_of_field(self):
        return self.list_of_hits

    def shoot(self):
        if self.flag_of_ship:
            if self.that_need_to_change is not None:
                if self.that_need_to_change == 'x':
                    return self.start_coord[0] + int(choice([-1, 1])), self.start_coord[1]
                else:
                    return self.start_coord[0], self.start_coord[1] + int(choice([-1, 1]))
            if choice(['x', 'y']) == 'x':
                return self.start_coord[0] + int(choice([-1, 1])), self.start_coord[1]
            return self.start_coord[0], self.start_coord[1] + int(choice([-1, 1]))
        return (randint(0, 9), randint(0, 9))

    def get_lists(self):
        return self.list_of_hits

    def hit_on_target(self, x, y, some_flag):
        if some_flag:
            return
        if x == self.start_coord[0] - 1 or x == self.start_coord[1] + 1:
            self.that_need_to_change = 'x'
        elif y == self.start_coord[1] - 1 or y == self.start_coord[1] + 1:
            self.that_need_to_change = 'y'
        else:
            self.start_coord = (x, y)


class Sea_fight:
    def __init__(self, width, height):
        pass


if __name__ == '__main__':
    pygame.init()
    size = width, height = 900, 500
    screen = pygame.display.set_mode(size)
    run()
