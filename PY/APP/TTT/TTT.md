
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Tic Tac Toe

---

```python
from IPython.display import clear_output

def display_board(board):
    print(' | |  ')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' | |  ')
    print('-----')
    print(' | |  ')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' | |  ')
    print('-----')
    print(' | |  ')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(' | |  ')

test_board = ['X','O','X','O','X','O','X','O','X','O']*10
display_board(test_board)
```

---
