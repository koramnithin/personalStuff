# Delete this line

'''

1
 \
  2
 / \
3   4


(1(None)(2(3(None)(None)4(None)(None))))


 1
  \
   2
  /
 3
/
4


'''


class Node(object):
    left_child = None
    right_child = None
    value = None

    def __init__(self, value):
        self.value = value


class Tree(object):
    def inorder(self, tree, s):
        if tree != None:
            s += '(' + str(tree.value)
            s = self.inorder(tree.left_child, s)
            s = self.inorder(tree.right_child, s)
            s += ')'
        else:
            s += '(None)'
        return s
        pass

    def decode_tree(self, tree):
        s = ''
        s = self.inorder(tree, s)
        return s
        pass

    #   def encode_inorder(self,tree,s,ind):
    #     if tree == None:
    #       value,ind = self.encode_tree(s,ind)
    #       if value == 'None':
    #         tree = None
    #         return
    #       tree = Node(int(value))
    #       encode_inorder(tree.left_child,s,ind)
    #       encode_inorder(tree.right_child,s,ind)
    #     return tree

    #   def encode_tree(self,s,ind):
    #     my_stack = []
    #     temp = ''
    #     for i in range(len(s[ind:])):
    #       if s[i] == '(':
    #         my_stack.append(i)
    #         temp = ''
    #       elif s[i] == ')':
    #         my_stack.pop()
    #         temp = ''
    #       temp += s[i]
    #     return (temp,i)
    def encode_tree(self, s):
        # Using the string to build the tree
        if s == None:
            return None
        temp = ''
        j = 1
        while s[j] != '(' and s[j] != ')':
            temp += s[j]
            j += 1
        if temp == 'None' or temp == '':
            return None
        else:
            value = int(temp)
            tree = Node(value)

        # Trying to get the left sub-tree string and
        # right sub-tree string and calling recursively
        left_str, right_str = self.get_subtree_string(s[j:])
        tree.left_child = self.encode_tree(left_str)
        tree.right_child = self.encode_tree(right_str)
        return tree

    def get_subtree_string(self, s):

        # Dividing according to the level
        temp = ''
        level = 0
        i=0
        while i<len(s):
            if s[i] == '(':
                level += 1 # increase level if we get '('
            if s[i] == ')':
                level += -1 # decrease level if we get ')'
            temp += s[i]
            i += 1
            if level == 0:
                break
        return temp, s[i:]
    pass


tree1 = Node(11)
tree1.left_child = None
tree1.right_child = Node(21)
tree1.right_child.left_child = Node(31)
tree1.right_child.right_child = Node(41)
tree1.right_child.left_child.left_child = None
tree1.right_child.left_child.right_child = None
tree1.right_child.right_child.left_child = None
tree1.right_child.right_child.right_child = None

my_tree = Tree()
s = my_tree.decode_tree(tree1)
print('tree to string:', s)
tree2 = my_tree.encode_tree(s)
print('string to tree:', my_tree.decode_tree(tree2))


