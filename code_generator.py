def postorder(tree):
    if tree is not None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

#pt = buildParseTree("( 1 + ( 2 * 3 )")
#pt.postorder()
