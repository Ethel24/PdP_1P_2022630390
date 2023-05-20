#Padilla Rodriguez Ethel
#Rendón Sierra Carlos Alexis

class MinStack:
    def __init__(self):
        #inicializamos dos pilas vacias
        self.stack = []  # Guarda los elementos de la pila
        self.min_stack = []  # Pila para realizar seguimiento del mínimo actual

    def push(self, x):
        #agregamos el elemento a la pila
        self.stack.append(x)
        #evaluamos si la pila esta vacia o el elemento es menor o igual al ultimo elemento de la pila
        if not self.min_stack or x <= self.min_stack[-1]:
            #si es asi entonces tambien agregamos el elemento a min_stack
            self.min_stack.append(x)

    def pop(self):
        #elimiina y devuleve el ultimo elemento agregado de la pila stack  si no esta vacia
        if self.stack:
            popped_element = self.stack.pop()
            #evaluamos si el elemento que sacamos es igual al ultimo elemento agregado de la pila min_stack
            if popped_element == self.min_stack[-1]:
                #si es asi entonces tambien eliminamos el elemento de min_stack
                self.min_stack.pop()
            return popped_element

    def min(self):
        #devuelve el ultimo elemento agregado de la pila min_stack si no esta vacia
        if self.min_stack:
            return self.min_stack[-1]


# Ejemplo de uso
stack = MinStack()
stack.push(8)
stack.push(71)
stack.push(4)
stack.push(60)

# Salida del minimo elemento
print("El elemento menor es:", stack.min())
stack.pop()
stack.pop()

# Salida del siguiente minimo elemento
print("El siguiente elemento menor es:", stack.min())
stack.pop()
stack.pop()
