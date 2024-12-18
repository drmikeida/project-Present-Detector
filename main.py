import pyxel
import random

class App:
    def __init__(self):
        
        pyxel.init(400, 400)
        pyxel.load("my_resource.pyxres")
        self.state = "title" 
        self.elf_x = 200
        self.elf_y = 200
        self.presents = [(random.randint(0, 390), random.randint(0, 390)) for _ in range(20)]
        self.collected_presents = 0
        self.time_limit = 30 * 60 
        self.time_elapsed = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.state == "title":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = "game"
        elif self.state == "game":
            if pyxel.btn(pyxel.KEY_A):
                self.elf_x -= 2
            if pyxel.btn(pyxel.KEY_D):
                self.elf_x += 2
            if pyxel.btn(pyxel.KEY_W):
                self.elf_y -= 2
            if pyxel.btn(pyxel.KEY_S):
                self.elf_y += 2

           
            for present in self.presents[:]:
                if (self.elf_x < present[0] + 10 and
                    self.elf_x + 10 > present[0] and
                    self.elf_y < present[1] + 10 and
                    self.elf_y + 10 > present[1]):
                    self.presents.remove(present)
                    self.collected_presents += 1

            
            self.time_elapsed += 2
            if self.time_elapsed >= self.time_limit:
                self.state = "game_over"

    def draw(self):
        if self.state == "title":
            pyxel.cls(7)
            pyxel.text(50, 50, "Christmas Present Collector", 3)  
            pyxel.text(50, 80, "Collect 20 presents within 30 seconds.", 3)  
            pyxel.text(50, 110, "Use WASD to move the elf.", 3)  
            pyxel.text(50, 140, "Press SPACE to start the game.", 8)  
            pyxel.rect(100, 200, 200, 50, 8) 
            pyxel.text(120, 220, "Start Game", 4)  
        elif self.state == "game":
            pyxel.cls(7)
            pyxel.blt(50, 50, 0, 0, 0, 16, 16, 0)
            pyxel.rect(self.elf_x, self.elf_y, 10, 10, 3)   
          
           
            for present in self.presents:
                pyxel.rect(present[0], present[1], 10, 5, 8)  
                pyxel.rect(present[0] + 2, present[1] - 5, 6, 5, 8) 
            pyxel.text(20, 20, f"Presents: {self.collected_presents}/20", 5)  
            remaining_time = (self.time_limit - self.time_elapsed) // 60
            pyxel.text(20, 50, f"Time: {remaining_time:02d}", 8) 
            
            
           
            if self.time_elapsed >= self.time_limit:
                pyxel.text(80, 200, "Time's Up!", 8) 
            elif self.collected_presents >= 20:
                pyxel.text(80, 200, "You Won!", 4) 
        elif self.state == "game_over":
            pyxel.cls(7)
            pyxel.text(80, 200, "Game Over!", 8)
            pyxel.text(80, 230, "Press SPACE to restart.", 5)  
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = "title"
                self.elf_x = 200
                self.elf_y = 200
                self.presents = [(random.randint(0, 390), random.randint(0, 390)) for _ in range(20)]
                self.collected_presents = 0
                self.time_elapsed = 0

App()
