"""
equation_tree: 수식트리 구성
- 후위표기식이 주어졌을 때 이를 이진트리(binary tree)로 구성
"""


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


# 연산자인지 피연산자인지 확인
def isOperator(c):
    if (c == '+' or c == '-' or c == '*'
            or c == '/' or c == '^'):
        return True
    else:
        return False


# 후위표기식 중위표기식으로 변경
def inorder(t):
    if t is not None:
        inorder(t.left)
        print(f'{t.value} ', end='')
        inorder(t.right)


def constructTree(postfix):
    stack = []
    # Traverse through every character
    for char in postfix:
        # if operand, simply push into stack
        # leaf node 생성
        if not isOperator(char):
            t = Node(char, None, None)
            stack.append(t)

        # Operator
        else:
            # Pop two top nodes and make them children
            t1 = stack.pop()  # right
            t2 = stack.pop()  # left
            t = Node(char, t2, t1)

            # Add this subexpression to stack
            stack.append(t)
            # print(t.left.value, ' ', t.value, ' ', t.right.value)

    # Only element will be the root of expression tree
    t = stack.pop()
    return t


if __name__ == "__main__":
    postfix = "32*56/+"  # input함수 이용
    expressT = constructTree(postfix)
    print("중위표기식: \n")
    inorder(expressT)