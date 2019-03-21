word="ABC"
print(word.index("B"))
a=word.index("B")
word=word[:a]+word[a+1:]
print(word)
print(not word)

def search(board,word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in word:
                index=word.index(board[i][j])
                word=word[:index]+word[index+1:]
    if not word:
        return True
    else:
        return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
print(search(board,word))
word = "SEE"
print(search(board,word))
word = "ABCB"
print(search(board,word))

def helper(board,i,j,word):
    if not word:
        return True
    if i<0 or j<0 or i>len(board) or j>len(board[0]) or board[i][j]!=word:
        return False
    temp=word[i][j]
    board[i][j]="#"
    res=helper(board,i+1,j,word[1:]) or helper(board,i-1,j,word[1:]) or helper(board,i,j+1,word[1:]) or helper(board,i,j-1,word[1:])
    board[i][j]=temp
    return res


def exist(board,word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if helper(board,i,j,word):
                return True
    return False

print(exist(board,word))