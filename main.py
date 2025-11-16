"""
Programa Principal - Simulador de Máquinas de Turing para Cifrado César
Proyecto 3 - Teoría de la Computación 2025

Autor: Diego Patzan, Roberto Najera, Luiz Gonzalez
Fecha: Noviembre 2025
"""

import sys
from src.caesar_encrypt import create_encrypt_machine
from src.caesar_decrypt import create_decrypt_machine


def print_banner():
    """Muestra el banner del programa."""
    print("=" * 70)
    print("  SIMULADOR DE MÁQUINAS DE TURING - CIFRADO CÉSAR")
    print("  Proyecto 3 - Teoría de la Computación 2025")
    print("=" * 70)
    print()


def print_menu():
    """Muestra el menú principal."""
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Encriptar mensaje")
    print("2. Decriptar mensaje")
    print("3. Ejecutar ejemplos del proyecto")
    print("4. Ejecutar pruebas adicionales")
    print("5. Salir")
    print()


def encrypt_message():
    """Función para encriptar un mensaje."""
    print("\n--- ENCRIPTACIÓN CÉSAR ---")
    print("Formato de entrada: llave#MENSAJE")
    print("Ejemplo: 3#ROMA NO FUE CONSTRUIDA EN UN DIA")
    print("        o: D#ROMA NO FUE CONSTRUIDA EN UN DIA")
    print()
    
    input_string = input("Ingrese el mensaje a encriptar: ").strip()
    
    if not input_string or '#' not in input_string:
        print("ERROR: Formato inválido. Debe incluir llave y mensaje separados por '#'")
        return
    
    machine = create_encrypt_machine()
    encrypted = machine.encrypt(input_string, verbose=True)
    
    print(f"\n✓ Mensaje encriptado: {encrypted}")
    print()


def decrypt_message():
    """Función para decriptar un mensaje."""
    print("\n--- DECRIPTACIÓN CÉSAR ---")
    print("Formato de entrada: llave#MENSAJE_CIFRADO")
    print("Ejemplo: 3#URPD QR IXH FRQVWUXLGD HQ XQ GLD")
    print()
    
    input_string = input("Ingrese el mensaje a decriptar: ").strip()
    
    if not input_string or '#' not in input_string:
        print("ERROR: Formato inválido. Debe incluir llave y mensaje separados por '#'")
        return
    
    machine = create_decrypt_machine()
    decrypted = machine.decrypt(input_string, verbose=True)
    
    print(f"\n✓ Mensaje decriptado: {decrypted}")
    print()


def run_project_examples():
    """Ejecuta los ejemplos específicos del PDF del proyecto."""
    print("\n" + "=" * 70)
    print("  EJEMPLOS DEL PROYECTO ")
    print("=" * 70)
    
    # Ejemplo 1: Encriptación con llave numérica
    print("\n--- EJEMPLO 1: Encriptación con llave numérica ---")
    print("Entrada: 3#ROMA NO FUE CONSTRUIDA EN UN DIA")
    
    encrypt_machine = create_encrypt_machine()
    encrypted = encrypt_machine.encrypt("3#ROMA NO FUE CONSTRUIDA EN UN DIA", verbose=False)
    
    print(f"Salida esperada: URPD QR IXH FRQVWUXLGD HQ XQ GLD")
    print(f"Salida obtenida: {encrypted}")
    print(f"Estado: {'✓ CORRECTO' if encrypted.replace('.', '') == 'URPD QR IXH FRQVWUXLGD HQ XQ GLD' else '✗ ERROR'}")
    
    # Ejemplo 2: Encriptación con llave alfabética
    print("\n--- EJEMPLO 2: Encriptación con llave alfabética ---")
    print("Entrada: D#ROMA NO FUE CONSTRUIDA EN UN DIA")
    
    encrypted2 = encrypt_machine.encrypt("D#ROMA NO FUE CONSTRUIDA EN UN DIA", verbose=False)
    
    print(f"Salida esperada: URPD QR IXH FRQVWUXLGD HQ XQ GLD")
    print(f"Salida obtenida: {encrypted2}")
    print(f"Estado: {'✓ CORRECTO' if encrypted2.replace('.', '') == 'URPD QR IXH FRQVWUXLGD HQ XQ GLD' else '✗ ERROR'}")
    
    # Ejemplo 3: Decriptación con llave numérica
    print("\n--- EJEMPLO 3: Decriptación con llave numérica ---")
    print("Entrada: 3#URPD QR IXH FRQVWUXLGD HQ XQ GLD")
    
    decrypt_machine = create_decrypt_machine()
    decrypted = decrypt_machine.decrypt("3#URPD QR IXH FRQVWUXLGD HQ XQ GLD", verbose=False)
    
    print(f"Salida esperada: ROMA NO FUE CONSTRUIDA EN UN DIA")
    print(f"Salida obtenida: {decrypted}")
    print(f"Estado: {'✓ CORRECTO' if decrypted.replace('.', '') == 'ROMA NO FUE CONSTRUIDA EN UN DIA' else '✗ ERROR'}")
    
    # Ejemplo 4: Decriptación con llave alfabética
    print("\n--- EJEMPLO 4: Decriptación con llave alfabética ---")
    print("Entrada: D#URPD QR IXH FRQVWUXLGD HQ XQ GLD")
    
    decrypted2 = decrypt_machine.decrypt("D#URPD QR IXH FRQVWUXLGD HQ XQ GLD", verbose=False)
    
    print(f"Salida esperada: ROMA NO FUE CONSTRUIDA EN UN DIA")
    print(f"Salida obtenida: {decrypted2}")
    print(f"Estado: {'✓ CORRECTO' if decrypted2.replace('.', '') == 'ROMA NO FUE CONSTRUIDA EN UN DIA' else '✗ ERROR'}")
    
    print("\n" + "=" * 70)


def run_additional_tests():
    """Ejecuta pruebas adicionales para demostrar funcionalidad."""
    print("\n" + "=" * 70)
    print("  PRUEBAS ADICIONALES")
    print("=" * 70)
    
    encrypt_machine = create_encrypt_machine()
    decrypt_machine = create_decrypt_machine()
    
    test_cases = [
        ("1#HOLA MUNDO", "Mensaje simple con desplazamiento 1"),
        ("5#TEORIA DE LA COMPUTACION", "Frase académica"),
        ("13#ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Alfabeto completo (ROT13)"),
        ("25#PROYECTO FINAL", "Desplazamiento grande"),
    ]
    
    for i, (test_input, description) in enumerate(test_cases, 1):
        print(f"\n--- PRUEBA {i}: {description} ---")
        print(f"Entrada original: {test_input}")
        
        # Encriptar
        encrypted = encrypt_machine.encrypt(test_input, verbose=False)
        print(f"Encriptado: {test_input.split('#')[0]}#{encrypted}")
        
        # Decriptar para verificar
        key = test_input.split('#')[0]
        to_decrypt = f"{key}#{encrypted}"
        decrypted = decrypt_machine.decrypt(to_decrypt, verbose=False)
        
        print(f"Decriptado: {decrypted}")
        
        # Verificar que la decriptación recupera el mensaje original
        original_message = test_input.split('#')[1]
        if decrypted.upper().replace('.', '') == original_message.upper():
            print("✓ Verificación exitosa: encriptar → decriptar recupera el original")
        else:
            print("✗ Error en la verificación")
    
    print("\n" + "=" * 70)


def main():
    """Función principal del programa."""
    print_banner()
    
    while True:
        print_menu()
        
        try:
            option = input("Seleccione una opción (1-5): ").strip()
            
            if option == '1':
                encrypt_message()
            elif option == '2':
                decrypt_message()
            elif option == '3':
                run_project_examples()
            elif option == '4':
                run_additional_tests()
            elif option == '5':
                print("\n¡Gracias por usar el simulador!")
                print("Proyecto 3 - Teoría de la Computación 2025")
                break
            else:
                print("\n✗ Opción inválida. Por favor seleccione 1-5.")
        
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"\n✗ Error: {e}")
            print("Por favor intente de nuevo.")


if __name__ == "__main__":
    main()
