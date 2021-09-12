class Tree:
    def __init__(self,value):
        self.value = value
        self.children = []

def longest_path(tree):
    return traverse(tree,1)

def traverse(node:Tree,k):
    print(node.value)
    k_max = k
    for child in node.children:
        if node.value + 1 == child.value:
            k1 = traverse(child,k+1)
        else:
            k1 = traverse(child,1)
        k_max = max(k1,k_max)
    return k_max

def traverse1(node:Tree):
    print(node.value)
    for e in node.children:
        traverse1(e)


# t = Tree(1)
# q = Tree(2)
# t.children.append(q)
# q = Tree(3)
# t.children.append(q)
# q = Tree(4)
# t.children[0].children.append(q)

t2 = Tree(5)
q2 = Tree(6)
t2.children.append(q2)
q2 = Tree(7)
t2.children.append(q2)
q2 = Tree(8)
t2.children[1].children.append(q2)
q2 = Tree(12)
t2.children[1].children.append(q2)
q2 = Tree(9)
t2.children[1].children[0].children.append(q2)
q2 = Tree(15)
t2.children[1].children[0].children[0].children.append(q2)
q2 = Tree(10)
t2.children[1].children[0].children[0].children.append(q2)

#traverse1(t2)


k = traverse(t2,1)
print(k)
