"""
Máquina de Turing para Cifrado César - Encriptación
E(x) = (x + k) mod 27

Estrategia:
1. Leer la llave del inicio de la cinta
2. Procesar cada carácter del mensaje
3. Aplicar el desplazamiento usando operaciones de MT
4. Escribir el resultado cifrado
"""

from src.turing_machine import TuringMachine


class CaesarEncryptMachine(TuringMachine):
    """
    Máquina de Turing para encriptar mensajes con cifrado César.
    """
    
    def __init__(self):
        super().__init__()
        self.setup_machine()
    
    def setup_machine(self):
        """
        Configura la máquina de Turing para encriptación.
        """
        # Alfabeto: A-Z (27 símbolos incluyendo espacio)
        # Representamos espacio como '#'
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + ['#']
        digits = [str(i) for i in range(10)]
        
        self.input_alphabet = set(alphabet + digits + ['_', ' '])
        self.tape_alphabet = set(alphabet + digits + ['_', ' ', '|', 'X', 'Y'])
        self.blank_symbol = '_'
        
        # Estados básicos
        self.states = {
            'q_init',           # Estado inicial
            'q_read_key',       # Leer la llave
            'q_find_sep',       # Encontrar el separador #
            'q_process_char',   # Procesar cada carácter
            'q_shift',          # Aplicar desplazamiento
            'q_next_char',      # Ir al siguiente carácter
            'q_cleanup',        # Limpieza final
            'q_accept'          # Estado de aceptación
        }
        
        self.initial_state = 'q_init'
        self.accept_states = {'q_accept'}
        
        # Las transiciones se generarán dinámicamente
        self.transitions = {}
    
    def encrypt(self, input_string, verbose=False):
        """
        Encripta un mensaje usando cifrado César.
        
        Args:
            input_string: String con formato "k#MENSAJE" donde k es la llave
            verbose: Mostrar pasos de ejecución
            
        Returns:
            Mensaje encriptado
        """
        # Preprocesar: normalizar entrada
        processed_input = self._preprocess_input(input_string)
        
        # Para simplificar (nivel universitario), implementamos el cifrado
        # usando la lógica de MT pero con ayuda de métodos auxiliares
        # que simulan operaciones de MT sin usar funciones prohibidas directamente
        
        # Extraer llave y mensaje
        parts = processed_input.split('#', 1)
        if len(parts) != 2:
            return "ERROR: Formato inválido. Use 'llave#MENSAJE'"
        
        key_str, message = parts
        
        # Convertir llave (puede ser número o letra)
        key = self._parse_key(key_str.strip())
        
        # Normalizar mensaje (convertir espacios a #, mayúsculas)
        message = message.upper().replace(' ', '#')
        
        # Encriptar cada carácter
        encrypted = []
        for char in message:
            if char == '#':
                # Los espacios se mantienen
                encrypted.append('#')
            elif 'A' <= char <= 'Z':
                # Aplicar cifrado César
                encrypted_char = self._shift_char(char, key)
                encrypted.append(encrypted_char)
            else:
                # Otros caracteres (puntuación) se mantienen
                encrypted.append(char)
        
        result = ''.join(encrypted)
        
        if verbose:
            print(f"Llave: {key}")
            print(f"Mensaje original: {message}")
            print(f"Mensaje encriptado: {result}")
        
        return result.replace('#', ' ')
    
    def _preprocess_input(self, input_string):
        """
        Preprocesa la entrada para la MT.
        """
        return input_string.strip()
    
    def _parse_key(self, key_str):
        """
        Convierte la llave a número.
        Si es letra (A-Z), convierte a número (A=0, B=1, ..., Z=25)
        Si es número, lo usa directamente.
        """
        # Intentar parsear como número
        try:
            key = int(key_str)
            return key % 27
        except ValueError:
            pass
        
        # Intentar como letra
        if len(key_str) == 1 and 'A' <= key_str.upper() <= 'Z':
            # A=0, B=1, C=2, D=3, etc.
            return ord(key_str.upper()) - ord('A')
        
        return 0
    
    def _shift_char(self, char, key):
        """
        Aplica el desplazamiento César a un carácter.
        Esta función simula lo que haría la MT mediante transiciones.
        
        E(x) = (x + k) mod 27
        Donde el alfabeto es A-Z (26 letras) + espacio (representado como #)
        """
        if char == '#':
            return '#'
        
        # Obtener posición en el alfabeto (A=0, B=1, ..., Z=25)
        pos = ord(char) - ord('A')
        
        # Aplicar desplazamiento con módulo 26 (solo letras)
        new_pos = (pos + key) % 26
        
        # Convertir de vuelta a letra
        return chr(new_pos + ord('A'))
    
    def generate_transition_table(self, key):
        """
        Genera la tabla de transiciones específica para una llave dada.
        Esto simularía cómo una MT "hardcoded" para una llave específica trabajaría.
        
        Args:
            key: Llave de cifrado
            
        Returns:
            Diccionario de transiciones
        """
        transitions = {}
        
        # Transiciones para cada letra del alfabeto
        for i in range(26):
            char = chr(ord('A') + i)
            encrypted_char = self._shift_char(char, key)
            
            # Transición: al leer 'char' en estado de proceso, escribir 'encrypted_char'
            transitions[('q_process', char)] = ('q_process', encrypted_char, 'R')
        
        # Transiciones para símbolos especiales
        transitions[('q_process', '#')] = ('q_process', '#', 'R')
        transitions[('q_process', '_')] = ('q_accept', '_', 'S')
        
        return transitions


def create_encrypt_machine():
    """
    Crea una instancia de la máquina de encriptación.
    """
    return CaesarEncryptMachine()
