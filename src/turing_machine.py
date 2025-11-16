"""
Simulador de Máquina de Turing
Implementación básica que respeta las operaciones tradicionales:
- Cambiar de estado
- Sustituir símbolo en la cinta
- Moverse a la izquierda o derecha
"""

import json


class TuringMachine:
    """
    Clase base para simular una Máquina de Turing.
    """
    
    def __init__(self, config_file=None):
        """
        Inicializa la máquina de Turing.
        
        Args:
            config_file: Archivo JSON con la configuración de la MT
        """
        self.states = set()           # Q: Conjunto de estados
        self.input_alphabet = set()   # Σ: Alfabeto de entrada
        self.tape_alphabet = set()    # Γ: Alfabeto de cinta
        self.initial_state = None     # q0: Estado inicial
        self.accept_states = set()    # F: Estados de aceptación
        self.transitions = {}         # δ: Función de transición
        
        self.tape = []                # Cinta de la MT
        self.head_position = 0        # Posición del cabezal
        self.current_state = None     # Estado actual
        self.blank_symbol = '_'       # Símbolo blanco
        
        if config_file:
            self.load_config(config_file)
    
    def load_config(self, config_file):
        """
        Carga la configuración de la MT desde un archivo JSON.
        
        Args:
            config_file: Ruta al archivo de configuración
        """
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        self.states = set(config['states'])
        self.input_alphabet = set(config['input_alphabet'])
        self.tape_alphabet = set(config['tape_alphabet'])
        self.initial_state = config['initial_state']
        self.accept_states = set(config['accept_states'])
        self.blank_symbol = config.get('blank_symbol', '_')
        
        # Cargar transiciones
        # Formato: {(estado, símbolo_leído): (nuevo_estado, símbolo_escribir, dirección)}
        self.transitions = {}
        for transition in config['transitions']:
            key = (transition['current_state'], transition['read_symbol'])
            value = (
                transition['next_state'],
                transition['write_symbol'],
                transition['direction']
            )
            self.transitions[key] = value
    
    def initialize_tape(self, input_string):
        """
        Inicializa la cinta con la cadena de entrada.
        
        Args:
            input_string: Cadena a colocar en la cinta
        """
        self.tape = list(input_string)
        self.head_position = 0
        self.current_state = self.initial_state
    
    def read_symbol(self):
        """
        Lee el símbolo en la posición actual del cabezal.
        
        Returns:
            Símbolo en la posición actual
        """
        if self.head_position < 0 or self.head_position >= len(self.tape):
            return self.blank_symbol
        return self.tape[self.head_position]
    
    def write_symbol(self, symbol):
        """
        Escribe un símbolo en la posición actual del cabezal.
        
        Args:
            symbol: Símbolo a escribir
        """
        # Expandir la cinta si es necesario
        while self.head_position >= len(self.tape):
            self.tape.append(self.blank_symbol)
        
        if self.head_position < 0:
            # Si el cabezal está a la izquierda, agregar al inicio
            self.tape.insert(0, symbol)
            self.head_position = 0
        else:
            self.tape[self.head_position] = symbol
    
    def move_head(self, direction):
        """
        Mueve el cabezal en la dirección especificada.
        
        Args:
            direction: 'L' para izquierda, 'R' para derecha, 'S' para quedarse
        """
        if direction == 'L':
            self.head_position -= 1
        elif direction == 'R':
            self.head_position += 1
        # Si es 'S', no hace nada (stay)
    
    def step(self):
        """
        Ejecuta un paso de la máquina de Turing.
        
        Returns:
            True si se pudo ejecutar el paso, False si no hay transición
        """
        current_symbol = self.read_symbol()
        key = (self.current_state, current_symbol)
        
        if key not in self.transitions:
            return False
        
        next_state, write_symbol, direction = self.transitions[key]
        
        # Operaciones básicas de la MT
        self.write_symbol(write_symbol)      # Sustituir símbolo
        self.current_state = next_state      # Cambiar de estado
        self.move_head(direction)            # Mover cabezal
        
        return True
    
    def run(self, input_string, max_steps=100000, verbose=False):
        """
        Ejecuta la máquina de Turing con una cadena de entrada.
        
        Args:
            input_string: Cadena de entrada
            max_steps: Número máximo de pasos
            verbose: Si True, imprime información de depuración
            
        Returns:
            Tupla (accepted, output) donde accepted indica si se aceptó
            y output es el contenido de la cinta
        """
        self.initialize_tape(input_string)
        steps = 0
        
        while steps < max_steps:
            if verbose:
                self.print_configuration()
            
            # Verificar si estamos en un estado de aceptación
            if self.current_state in self.accept_states:
                output = ''.join(self.tape).replace(self.blank_symbol, '')
                return True, output
            
            # Ejecutar un paso
            if not self.step():
                # No hay transición disponible
                output = ''.join(self.tape).replace(self.blank_symbol, '')
                return False, output
            
            steps += 1
        
        # Se alcanzó el máximo de pasos
        output = ''.join(self.tape).replace(self.blank_symbol, '')
        return False, output
    
    def print_configuration(self):
        """
        Imprime la configuración actual de la MT (para debugging).
        """
        tape_str = ''.join(self.tape)
        pointer = ' ' * self.head_position + '^'
        print(f"Estado: {self.current_state}")
        print(f"Cinta:  {tape_str}")
        print(f"        {pointer}")
        print()
    
    def get_tape_content(self):
        """
        Retorna el contenido actual de la cinta.
        
        Returns:
            Contenido de la cinta como string
        """
        return ''.join(self.tape).replace(self.blank_symbol, '')
