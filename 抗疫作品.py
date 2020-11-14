import pyxel
import random
import math
import time
 
# 常量
W, H = 150, 150
MAX_SPEED = 1.2
INIT_VIRUS_NUM = 10
N_PIECES = 12
MIN_SIZE = 1 # 终极难度
 
class Virus:
    def __init__(self):
        self.size = random.uniform(3, 10)
        self.pos = [random.uniform(self.size, W-self.size), random.uniform(self.size, H-self.size)]
        self.speed = [random.uniform(-MAX_SPEED, MAX_SPEED), random.uniform(-MAX_SPEED, MAX_SPEED)]
        self.color = random.randint(1, 15)
 
    def update(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
 
        if self.speed[0] < 0 and self.pos[0] < self.size:
            self.speed[0] *= -1
        if self.speed[0] > 0 and self.pos[0] > W - self.size:
            self.speed[0] *= -1
        if self.speed[1] < 0 and self.pos[1] < self.size:
            self.speed[1] *= -1
        if self.speed[1] > 0 and self.pos[1] > H - self.size:
            self.speed[1] *= -1
 
 
class Game:
    def __init__(self):
        pyxel.init(W, H, caption='Kill Virus Pixel Game')
        pyxel.mouse(True)
        self.hit = False
        self.game_over = False
        self.start_time = time.time()
        self.viruses = [Virus() for _ in range(INIT_VIRUS_NUM)]
 
        pyxel.sound(0).set(
            "e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr",
            "p",
            "6",
            "vffn fnff vffs vfnn",
            25,
        )
 
        pyxel.sound(1).set(
            "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
            "s",
            "6",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )
 
        pyxel.sound(2).set(
            "c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )
 
        pyxel.sound(3).set(
            "f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )
 
        pyxel.sound(4).set(
            "f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25
        )
 
        self.play_music(True, True, True)
 
        pyxel.run(self.update, self.draw)
 
    def play_music(self, ch0, ch1, ch2):
        if ch0:
            pyxel.play(0, [0, 1], loop=True)
        else:
            pyxel.stop(0)
 
        if ch1:
            pyxel.play(1, [2, 3], loop=True)
        else:
            pyxel.stop(1)
 
        if ch2:
            pyxel.play(2, 4, loop=True)
        else:
            pyxel.stop(2)
 
 
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
 
        virus_count = len(self.viruses)
 
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.hit = True
            for i in range(virus_count):
                virus = self.viruses[i]
                dx = virus.pos[0] - pyxel.mouse_x
                dy = virus.pos[1] - pyxel.mouse_y
                if dx**2 + dy**2 < virus.size ** 2:
                    new_size = (virus.size ** 2 / N_PIECES) ** 0.5
                    # 如果没到最小可杀尺寸，则会分裂
                    if new_size > MIN_SIZE:
                        for j in range(N_PIECES):
                            angle = math.pi * 2 * j / N_PIECES
                            new_virus = Virus()
                            new_virus.size = new_size
                            new_virus.pos[0] = virus.pos[0] + (virus.size + new_size) * math.cos(angle)
                            new_virus.pos[1] = virus.pos[1] + (virus.size + new_size) * math.sin(angle)
                            new_virus.speed[0] = math.cos(angle) * MAX_SPEED
                            new_virus.speed[1] = math.sin(angle) * MAX_SPEED
                            self.viruses.append(new_virus)
                            print('here')
                    del self.viruses[i]
                    break
 
        # 病毒融合
        virus_count = len(self.viruses)
 
        for i in range(virus_count - 1, -1, -1):
            vi = self.viruses[i]
            vi.update()
            for j in range(i-1, -1, -1):
                vj = self.viruses[j]
                dx = vi.pos[0] - vj.pos[0]
                dy = vi.pos[1] - vj.pos[1]
                total_size = vi.size + vj.size
 
                if dx ** 2 + dy ** 2 < total_size ** 2:
                    new_virus = Virus()
                    new_virus.size = (vi.size ** 2 + vj.size ** 2) ** 0.5
                    new_virus.pos[0] = vi.pos[0] * vi.size / total_size + vj.pos[0] * vj.size / total_size
                    new_virus.pos[1] = vi.pos[1] * vi.size / total_size + vj.pos[1] * vj.size / total_size
                    new_virus.speed[0] = vi.speed[0] * vi.size / total_size + vj.speed[0] * vj.size / total_size
                    new_virus.speed[1] = vi.speed[1] * vi.size / total_size + vj.speed[1] * vj.size / total_size
                    self.viruses.append(new_virus)
                    del self.viruses[i]
                    del self.viruses[j]
                    break
 
        for virus in self.viruses:
            virus.update()
 
 
    def draw(self):
        pyxel.cls(0)
 
        # 游戏规则
        if not self.hit:
            pyxel.text(40, 60, 'KILL CORONAVIRUS!', pyxel.frame_count % 16)
            pyxel.text(40, 70, 'By Clicking It ASAP!', pyxel.frame_count % 16)
 
        if not self.game_over and len(self.viruses) == 0:
            self.game_over = True
            self.total_time = int(time.time() - self.start_time)
 
        if self.game_over:
            pyxel.text(50, 60, 'victory!!!', pyxel.frame_count % 16)
            pyxel.text(50, 70, 'TIME: {}s'.format(self.total_time), pyxel.frame_count % 16)
 
        for virus in self.viruses:
            pyxel.circ(virus.pos[0], virus.pos[1], virus.size - 1, virus.color)
            for i in range(N_PIECES):
                angle = math.pi * 2 / 12 * i
                pyxel.circ(virus.pos[0] + math.cos(angle) * virus.size, virus.pos[1]+math.sin(angle)*virus.size, 1, virus.color)
 
game = Game()