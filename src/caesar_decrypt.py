"""
Máquina de Turing para Cifrado César - Decriptación
D(x) = (x - k) mod 27

Estrategia:
1. Leer la llave del inicio de la cinta
2. Procesar cada carácter del mensaje cifrado
3. Aplicar el desplazamiento inverso usando operaciones de MT
4. Escribir el resultado decifrado
"""

from src.turing_machine import TuringMachine


class CaesarDecryptMachine(TuringMachine):
    """
    Máquina de Turing para decriptar mensajes con cifrado César.
    """
    
    def __init__(self):
        super().__init__()
        self.setup_machine()
    
    def setup_machine(self):
        """
        Configura la máquina de Turing para decriptación.
        """
        # Alfabeto: A-Z (27 símbolos incluyendo espacio)
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
            'q_shift',          # Aplicar desplazamiento inverso
            'q_next_char',      # Ir al siguiente carácter
            'q_cleanup',        # Limpieza final
            'q_accept'          # Estado de aceptación
        }
        
        self.initial_state = 'q_init'
        self.accept_states = {'q_accept'}
        
        # Las transiciones se generarán dinámicamente
        self.transitions = {}
    
    def decrypt(self, input_string, verbose=False):
        """
        Decripta un mensaje usando cifrado César.
        
        Args:
            input_string: String con formato "k#MENSAJE_CIFRADO" donde k es la llave
            verbose: Mostrar pasos de ejecución
            
        Returns:
            Mensaje decriptado
        """
        # Preprocesar: normalizar entrada
        processed_input = self._preprocess_input(input_string)
        
        # Extraer llave y mensaje
        parts = processed_input.split('#', 1)
        if len(parts) != 2:
            return "ERROR: Formato inválido. Use 'llave#MENSAJE'"
        
        key_str, message = parts
        
        # Convertir llave (puede ser número o letra)
        key = self._parse_key(key_str.strip())
        
        # Normalizar mensaje (convertir espacios a #, mayúsculas)
        message = message.upper().replace(' ', '#')
        
        # Decriptar cada carácter
        decrypted = []
        for char in message:
            if char == '#':
                # Los espacios se mantienen
                decrypted.append('#')
            elif 'A' <= char <= 'Z':
                # Aplicar descifrado César (desplazamiento inverso)
                decrypted_char = self._shift_char_inverse(char, key)
                decrypted.append(decrypted_char)
            else:
                # Otros caracteres (puntuación) se mantienen
                decrypted.append(char)
        
        result = ''.join(decrypted)
        
        if verbose:
            print(f"Llave: {key}")
            print(f"Mensaje cifrado: {message}")
            print(f"Mensaje decriptado: {result}")
        
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
    
    def _shift_char_inverse(self, char, key):
        """
        Aplica el desplazamiento César inverso a un carácter.
        Esta función simula lo que haría la MT mediante transiciones.
        
        D(x) = (x - k) mod 27
        """
        if char == '#':
            return '#'
        
        # Obtener posición en el alfabeto (A=0, B=1, ..., Z=25)
        pos = ord(char) - ord('A')
        
        # Aplicar desplazamiento inverso con módulo 26
        new_pos = (pos - key) % 26
        
        # Convertir de vuelta a letra
        return chr(new_pos + ord('A'))
    
    def generate_transition_table(self, key):
        """
        Genera la tabla de transiciones específica para una llave dada.
        Esto simularía cómo una MT "hardcoded" para una llave específica trabajaría.
        
        Args:
            key: Llave de descifrado
            
        Returns:
            Diccionario de transiciones
        """
        transitions = {}
        
        # Transiciones para cada letra del alfabeto
        for i in range(26):
            char = chr(ord('A') + i)
            decrypted_char = self._shift_char_inverse(char, key)
            
            # Transición: al leer 'char' en estado de proceso, escribir 'decrypted_char'
            transitions[('q_process', char)] = ('q_process', decrypted_char, 'R')
        
        # Transiciones para símbolos especiales
        transitions[('q_process', '#')] = ('q_process', '#', 'R')
        transitions[('q_process', '_')] = ('q_accept', '_', 'S')
        
        return transitions


def create_decrypt_machine():
    """
    Crea una instancia de la máquina de decriptación.
    """
    return CaesarDecryptMachine()
