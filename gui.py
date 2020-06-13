import sys, pygame
import pygame_gui
import example_generator
import algorithm
import data_preparation

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

size = 800, 800


ui_offset = 170

new_size = (size[0] - ui_offset, size[1])


def new_coords(v):
    return int(v[0] * new_size[0]) + ui_offset, int(v[1] * new_size[1])


screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("AZ GOLF GUI")
manager = pygame_gui.UIManager((800, 600))

random_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 10), (150, 50)),
                                             text='Losuj punkty',
                                             manager=manager)
count_list = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((10,70), (150, 126)),
                                             item_list=['5', '10', '15', '20', '30', '40'],
                                             manager=manager)
save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 206), (150, 50)),
                                             text='Zapisz',
                                             manager=manager)
load_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 266), (150, 50)),
                                             text='Wczytaj',
                                             manager=manager)
save_file = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((10, 326), (150, 50)),
                                             manager=manager)
save_file.set_text(".\\save.txt")

mod_list = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((10,376), (150, 66)),
                                             item_list=['edycja', 'dodawanie', 'usuwanie'],
                                             manager=manager)


count = 10
a = []
b = []
sol = []
hooked_point = None
light = None
a_added = None

def random_example():
    global a, b, sol
    a, b = example_generator.generate_example(count)
    sol = algorithm.get_solution(a, b)


def draw():
    mod = mod_list.get_single_selection()
    screen.fill(WHITE)
    for v, u in sol:
        pygame.draw.line(screen, BLACK, new_coords(v), new_coords(u), 2)
    for v in a:
        pygame.draw.circle(screen, BLACK, new_coords(v), 4)
    if a_added:
        pygame.draw.circle(screen, BLACK, new_coords(a_added), 4)
    if light and (mod == "edycja" or mod == "usuwanie"):
        pygame.draw.circle(screen, BLUE, new_coords(light), 6)
    if hooked_point:
        pygame.draw.circle(screen, BLUE, pygame.mouse.get_pos(), 6)
    for v in b:
        pygame.draw.circle(screen, RED, new_coords(v), 4)
    manager.draw_ui(screen)
    pygame.display.flip()


def find_point(c):
    tmp = a.copy()
    tmp.extend(b)
    points_in_screen = ((new_coords(v), v) for v in tmp)
    distances = (((vx-c[0])**2 + (vy-c[1])**2, v) for (vx, vy), v in points_in_screen)
    m = min(distances)
    if m[0] < 250:
        return m[1]
    else:
        return None


def event_loop():
    global screen, size, count, new_size, hooked_point, light, sol, a, b, a_added
    mod = mod_list.get_single_selection()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            new_size = (size[0] - ui_offset, size[1])
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        if event.type == pygame.MOUSEMOTION:
            light = find_point(pygame.mouse.get_pos())
            if hooked_point:
                c = pygame.mouse.get_pos()
                c = ((c[0] - ui_offset) / new_size[0], c[1] / new_size[1])
                if c[0] >= 0.0:
                    ai = a.index(hooked_point) if hooked_point in a else None
                    if ai is not None:
                        a[ai] = c
                        hooked_point = c
                    else:
                        bi = b.index(hooked_point)
                        b[bi] = c
                        hooked_point = c
                    sol = algorithm.get_solution(a, b)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mod == "edycja":
                hooked_point = find_point(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            c = pygame.mouse.get_pos()
            fp = find_point(c)
            c = ((c[0] - ui_offset) / new_size[0], c[1] / new_size[1])
            if mod == "dodawanie":
                if c[0] >= 0.0:
                    if not a_added:
                        a_added = c
                    else:
                        a.append(a_added)
                        b.append(c)
                        sol = algorithm.get_solution(a, b)
                        a_added = None
            if mod == "usuwanie" and len(a) != 1 and fp:
                ai = a.index(fp) if fp in a else None
                if ai is not None:
                    si = next(iter(i for i, (sa, sb) in enumerate(sol) if a[ai] is sa))
                    del b[b.index(sol[si][1])]
                    del a[ai]
                else:
                    bi = b.index(fp)
                    si = next(iter(i for i, (sa, sb) in enumerate(sol) if b[bi] is sb))
                    del a[a.index(sol[si][0])]
                    del b[bi]
                sol = algorithm.get_solution(a, b)
            light = None
            hooked_point = None
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == random_button:
                    selection = count_list.get_single_selection()
                    if selection:
                        count = int(selection)
                    random_example()
                if event.ui_element == save_button:
                    text = data_preparation.a_b_to_text(a, b)
                    with open(save_file.get_text(), "w") as f:
                        f.write(text)
                if event.ui_element == load_button:
                    try:
                        with open(save_file.get_text(), ) as f:
                            text = f.read()
                        a, b = data_preparation.text_to_a_b(text)
                        sol = algorithm.get_solution(a, b)
                    except:
                        print("File not found")
        manager.process_events(event)


def main_loop():
    clock = pygame.time.Clock()
    while True:
        time_delta = clock.tick(60) / 1000.0
        event_loop()
        manager.update(time_delta)
        draw()


random_example()
main_loop()
