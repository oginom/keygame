import pyxel

# MEMO
# どんなゲーム？
# キーボードのqwerty配列が画面にあって、キーボードを押すとその部分が盛り上がる。
# 同時押しするので、ユーザーは手の形をがんばって押す感じ。
# それで、物理演算で、ボールを目的のゴールに運ぶ、など。

my_font = pyxel.Font("assets/PixelMplus10-Bold.bdf")
my_font.text_width("A")

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_zenkaku = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
keys = [
    pyxel.KEY_A,
    pyxel.KEY_B,
    pyxel.KEY_C,
    pyxel.KEY_D,
    pyxel.KEY_E,
    pyxel.KEY_F,
    pyxel.KEY_G,
    pyxel.KEY_H,
    pyxel.KEY_I,
    pyxel.KEY_J,
    pyxel.KEY_K,
    pyxel.KEY_L,
    pyxel.KEY_M,
    pyxel.KEY_N,
    pyxel.KEY_O,
    pyxel.KEY_P,
    pyxel.KEY_Q,
    pyxel.KEY_R,
    pyxel.KEY_S,
    pyxel.KEY_T,
    pyxel.KEY_U,
    pyxel.KEY_V,
    pyxel.KEY_W,
    pyxel.KEY_X,
    pyxel.KEY_Y,
    pyxel.KEY_Z,
]


class KeyButton:
    def __init__(self, x, y, w, h, col: int = 8, key: str = "A"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
        self.key = key

        self.key_string = alpha_zenkaku[alpha.index(key)]
        self.key_pyxel = keys[alpha.index(key)]

        # status
        self.is_pressed = False

    def draw(self):
        if self.is_pressed:
            pyxel.rect(self.x, self.y, self.w, self.h, self.col)
        else:
            pyxel.rect(self.x, self.y, self.w, self.h, 13)
        pyxel.text(self.x, self.y, self.key_string, 15, my_font)

    def update(self):
        self.is_pressed = pyxel.btn(self.key_pyxel)

class Ball:
    def __init__(self, x, y, r, col: int = 8, vx: int = 1, vy: int = 1):
        self.x = x
        self.y = y
        self.r = r
        self.col = col
        self.vx = vx
        self.vy = vy


    def draw(self):
        pyxel.circ(self.x, self.y, self.r, self.col)

    def update(self):
        self.vy += 0.1

        self.x += self.vx
        self.y += self.vy

        if self.y > pyxel.height and self.vy > 0:
            self.vy = -self.vy
            self.y = pyxel.height

        if self.x < 0 and self.vx < 0:
            self.vx = -self.vx
            self.x = 0

        if self.x > pyxel.width and self.vx > 0:
            self.vx = -self.vx
            self.x = pyxel.width

    def interact(self, key_button: KeyButton) -> None:
        if not key_button.is_pressed:
            return

        x_before = self.x - self.vx
        y_before = self.y - self.vy

        x_collide_before = 0
        if x_before + self.r < key_button.x:
            x_collide_before = -1
        elif x_before - self.r > key_button.x + key_button.w:
            x_collide_before = 1

        y_collide_before = 0
        if y_before + self.r < key_button.y:
            y_collide_before = -1
        elif y_before - self.r > key_button.y + key_button.h:
            y_collide_before = 1

        x_collide = 0
        if self.x + self.r < key_button.x:
            x_collide = -1
        elif self.x - self.r > key_button.x + key_button.w:
            x_collide = 1

        y_collide = 0
        if self.y + self.r < key_button.y:
            y_collide = -1
        elif self.y - self.r > key_button.y + key_button.h:
            y_collide = 1

        if y_collide == 0:
            if x_collide_before != 0 and x_collide == 0:
                self.vx = -self.vx
                self.x = key_button.x + key_button.w / 2 + \
                (key_button.w / 2 + self.r) * x_collide_before
        if x_collide == 0:
            if y_collide_before != 0 and y_collide == 0:
                self.vy = -self.vy
                self.y = key_button.y + key_button.h / 2 + \
                    (key_button.h / 2 + self.r) * y_collide_before
        return


class App:
    def __init__(self):
        pyxel.init(256, 256, title="Key Game")

        self.key_buttons = [
            KeyButton(30, 120, 16, 16, 7, "Q"),
            KeyButton(50, 120, 16, 16, 7, "W"),
            KeyButton(70, 120, 16, 16, 7, "E"),
            KeyButton(90, 120, 16, 16, 7, "R"),
            KeyButton(110, 120, 16, 16, 7, "T"),
            KeyButton(130, 120, 16, 16, 7, "Y"),
            KeyButton(150, 120, 16, 16, 7, "U"),
            KeyButton(170, 120, 16, 16, 7, "I"),
            KeyButton(190, 120, 16, 16, 7, "O"),
            KeyButton(210, 120, 16, 16, 7, "P"),

            KeyButton(40, 140, 16, 16, 7, "A"),
            KeyButton(60, 140, 16, 16, 7, "S"),
            KeyButton(80, 140, 16, 16, 7, "D"),
            KeyButton(100, 140, 16, 16, 7, "F"),
            KeyButton(120, 140, 16, 16, 7, "G"),
            KeyButton(140, 140, 16, 16, 7, "H"),
            KeyButton(160, 140, 16, 16, 7, "J"),
            KeyButton(180, 140, 16, 16, 7, "K"),
            KeyButton(200, 140, 16, 16, 7, "L"),

            KeyButton(50, 160, 16, 16, 7, "Z"),
            KeyButton(70, 160, 16, 16, 7, "X"),
            KeyButton(90, 160, 16, 16, 7, "C"),
            KeyButton(110, 160, 16, 16, 7, "V"),
            KeyButton(130, 160, 16, 16, 7, "B"),
            KeyButton(150, 160, 16, 16, 7, "N"),
            KeyButton(170, 160, 16, 16, 7, "M"),
        ]

        self.balls = [
            Ball(100, 50, 10, 5, 1, 1),
            Ball(150, 250, 10, 6, 2, 6),
            Ball(200, 70, 10, 7, 3, 3),
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        for key_button in self.key_buttons:
            key_button.update()

        for ball in self.balls:
            ball.update()

        for ball in self.balls:
            for key_button in self.key_buttons:
                ball.interact(key_button)

    def draw(self):
        pyxel.cls(12)

        for key_button in self.key_buttons:
            key_button.draw()

        for ball in self.balls:
            ball.draw()

App()
