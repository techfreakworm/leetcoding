class Solution:
    def snakesAndLadders(self, board):
        b_mp = {}
       
        board_nums = []
        n_row = n_col = len(board)
        n=n_row*n_col
        
        if n % 2 ==0:
            for i in range(n_row):
                if i%2 == 0:
                    board_nums.append(list(range(n,n-n_col,-1)))
                else:
                    board_nums.append(list(range(n,n-n_col,-1))[::-1])
                n = n-n_col
        else:
             for i in range(n_row):
                if i%2 != 0:
                    board_nums.append(list(range(n,n-n_col,-1)))
                else:
                    board_nums.append(list(range(n,n-n_col,-1))[::-1])
                n = n-n_col
        
        for i in range(n_row):
            for j in range(n_col):
                b_mp[board_nums[i][j]] = board[i][j]
                
        # Creating a queue
        queue = [(1,0)] #curr, steps/moves
        
        visited = set()
        goal = n_row*n_col
        
        while(queue):
            curr, steps = queue.pop(0)
#             next_pos = 0
            
            if curr == goal:
                return steps
            
            for i in range(1,7):
                
                # Skip anything outside board
                if curr+i > goal:
                    continue
                
                else:
                    if b_mp[curr+i] == -1:
                        next_pos = curr + i
                    else:
                        next_pos = b_mp[curr+i]
                        
                if next_pos not in visited:
                    queue.append((next_pos,steps+1))
                    visited.add(next_pos)
            
        
        return -1
                