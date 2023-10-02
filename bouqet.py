class Flower:
    def __init__(self, name, color, length):
        self.name = name
        self.color = color
        self.length = length

class Bouquet:
    def __init__(self):
        self.flowers = []
    
    def add_flower(self, flower):
        self.flowers.append(flower)
    
    def calculate_cost(self):
        total_cost = 0
        
        # Подсчитываем стоимость каждого цветка в букете
        for flower in self.flowers:
            total_cost += 10 * flower.length
        
        return total_cost