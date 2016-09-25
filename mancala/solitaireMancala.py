# Proyecto para el curso de Coursera "Fundamentals of computing"
# 11 de junio de 2014
# Autor: Leonardo Martinez
class SolitaireMancala:
    def __init__(self):
        self.board = [0]
        
    def set_board(self, configuration):
        self.board = configuration[::]
        
    def __str__(self):
        board = self.board[::]
        board.reverse()
        return str(board)
    
    def get_num_seeds(self,house_num):
        return self.board[house_num]
    
    def is_game_won(self):
        if self.board[1:].count(0) == len(self.board[1:]):
            return True
        return False
    
    def is_legal_move(self, house_num):
        if house_num == 0:
            return False
        elif self.board[house_num] == house_num:
            return True
        return False
        
    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            self.board[house_num] = 0
            for i in range(house_num):
                self.board[i] += 1
                
    def choose_move(self):
        for i in self.board[1:]:
            if self.board.index(i,1) == i:
                return i
        return 0
    
    def plan_moves(self):
        ret = []
        while not self.is_game_won():
            k = self.choose_move()
            if k != 0:
                ret.append(k)
            if k == 0: break
            self.apply_move(k)
        return ret
