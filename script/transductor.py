from graphviz import Digraph

# Crear un grafo dirigido
automata = Digraph(format='png', engine='dot')

# Configurar el estilo del autómata con más separación entre nodos
# Más separación horizontal y vertical
automata.attr(rankdir='LR', nodesep='1', ranksep='1.5')
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
automata.edge('q0', 'qn', label='0/a, 1/b',
              arrowhead='normal')  # Flecha curva hacia qn
automata.edge('q0', 'qp', label='1/a, 0/b',
              arrowhead='normal')  # Flecha curva hacia qp
automata.edge('q0', 'q0', label='0/c, 1/c', arrowhead='normal')  # Bucle en q0

automata.edge('qn', 'qp', label='1/a, 0/b',
              arrowhead='normal')  # Flecha curva hacia qp
automata.edge('qn', 'qn', label='0/a, 1/b, 0/c, 1/c',
              arrowhead='normal')  # Bucle en qn

automata.edge('qp', 'qp', label='1/a, 0/b, 0/a, 1/b, 0/c, 1/c',
              arrowhead='normal')  # Bucle en qp

# Renderizar el autómata
# Guarda como 'automata_separated.png' y abre la imagen
automata.render('document/Graphics/transductor_clause', view=True)

# Crear un grafo dirigido
automata = Digraph(format='png', engine='dot')

# Configurar el estilo del autómata con más separación entre nodos
# Más separación horizontal y vertical
automata.attr(rankdir='LR', nodesep='1', ranksep='1.5')
automata.attr('node', shape='circle')  # Estados como círculos

# Agregar nodos (estados)
automata.node('q01', 'q₀', shape='circle')  # Estado inicial
automata.node('qn1', 'qₙ')  # Estado intermedio
automata.node('qp1', 'qₚ', shape='doublecircle')  # Estado de aceptación

# Agregar una flecha al estado inicial
automata.attr('node', shape='none')
automata.node('', '')  # Nodo vacío para representar la entrada
automata.edge('', 'q01')

# Agregar transiciones
automata.attr('node', shape='circle')
automata.edge('q01', 'qn1', label='0/a, 1/b',
              arrowhead='normal')  # Flecha curva hacia qn
automata.edge('q01', 'qp1', label='1/a, 0/b',
              arrowhead='normal')  # Flecha curva hacia qp
automata.edge('q01', 'q01', label='0/c, 1/c', arrowhead='normal')  # Bucle en q0

automata.edge('qn1', 'qp1', label='1/a, 0/b',
              arrowhead='normal')  # Flecha curva hacia qp
automata.edge('qn1', 'qn1', label='0/a, 1/b, 0/c, 1/c',
              arrowhead='normal')  # Bucle en qn

automata.edge('qp1', 'qp1', label='1/a, 0/b, 0/a, 1/b, 0/c, 1/c',
              arrowhead='normal')  # Bucle en qp

# Renderizar el autómata
# Guarda como 'automata_separated.png' y abre la imagen
automata.render('document/Graphics/transductor_sat', view=True)
