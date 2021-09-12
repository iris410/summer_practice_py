class Tree:
    def __init__(self,value):
        self.value = value
        self.children = []

def longest_path(tree):
    return traverse(tree,1)

def traverse(tree,k):
    k_max = k
    for child in tree.children:
       if tree.value + 1  ==  child.value:
            k1 = traverse(child,k+1)
       else:
            k1 = traverse(child,1)
       k_max = max(k1,k_max)
    return k_max



t = Tree(5)
q = Tree(6)
t.children.append(q)
q = Tree(7)
t.children.append(q)
q = Tree(8)
t.children[1].children.append(q)
q = Tree(12)
t.children[1].children.append(q)
q = Tree(9)
t.children[1].children[0].children.append(q)
q = Tree(15)
t.children[1].children[0].children[0].children.append(q)
q = Tree(10)
t.children[1].children[0].children[0].children.append(q)

ans = longest_path(t)
print(ans)
