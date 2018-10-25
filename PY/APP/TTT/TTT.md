
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Tic Tac Toe

---

```python
from IPython.display import clear_output

def display_board(board):
    print(' | |  ')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(' | |  ')
    print('-----')
    print(' | |  ')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' | |  ')
    print('-----')
    print(' | |  ')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' | |  ')

test_board = ['X','O','X','O','X','O','X','O','X','O']*10

def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1 choose X or O').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):

    board[position] = marker

#print(test_board)
place_marker(test_board,'$',8)
display_board(test_board)
```

---
