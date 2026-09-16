from graphviz import Digraph

dot = Digraph()
dot.node('x', "Hi their!")
dot.node('y', "May I know who are you?")
dot.edge('x', 'y')

dot.render('test', format='png', view=True)
