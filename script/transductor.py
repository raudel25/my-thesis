from graphviz import Digraph

# Crear un grafo dirigido
automata = Digraph(format='png', engine='dot')

# Configurar el estilo del autómata con más separación entre nodos
automata.attr(rankdir='LR', nodesep='1', ranksep='1.5')  # Más separación horizontal y vertical
automata.attr('node', shape='circle')  # Estados como círculos

# Agregar nodos (estados)
automata.node('q0', 'q₀', shape='circle')  # Estado inicial
automata.node('qn', 'qₙ')  # Estado intermedio
automata.node('qp', 'qₚ', shape='doublecircle')  # Estado de aceptación

# Agregar una flecha al estado inicial
automata.attr('node', shape='none')
automata.node('', '')  # Nodo vacío para representar la entrada
automata.edge('', 'q0')

# Agregar transiciones
automata.attr('node', shape='circle')
automata.edge('q0', 'qn', label='0/a, 1/b', arrowhead='normal')  # Flecha curva hacia qn
automata.edge('q0', 'qp', label='1/a, 0/b', arrowhead='normal')  # Flecha curva hacia qp
automata.edge('q0', 'q0', label='0/c, 1/c', arrowhead='normal')  # Bucle en q0

automata.edge('qn', 'qp', label='1/a, 0/b', arrowhead='normal')  # Flecha curva hacia qp
automata.edge('qn', 'qn', label='0/a, 1/b, 0/c, 1/c', arrowhead='normal')  # Bucle en qn

automata.edge('qp', 'qp', label='1/a, 0/b, 0/a, 1/b, 0/c, 1/c', arrowhead='normal')  # Bucle en qp

# Renderizar el autómata
automata.render('document/Graphics/transductor', view=True)  # Guarda como 'automata_separated.png' y abre la imagen
