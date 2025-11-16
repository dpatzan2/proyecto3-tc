#!/usr/bin/env python3
"""
Script de Pruebas Automáticas
Verifica que el simulador funciona correctamente con todos los ejemplos del PDF
"""

from src.caesar_encrypt import create_encrypt_machine
from src.caesar_decrypt import create_decrypt_machine


def test_example_1():
    """Ejemplo 1: Encriptación con llave numérica 3"""
    print("Test 1: Encriptación con llave numérica 3")
    machine = create_encrypt_machine()
    input_str = "3#ROMA NO FUE CONSTRUIDA EN UN DIA"
    expected = "URPD QR IXH FRQVWUXLGD HQ XQ GLD"
    result = machine.encrypt(input_str)
    
    # Remover puntuación para comparación
    result_clean = result.replace('.', '').strip()
    
    print(f"  Entrada:  {input_str}")
    print(f"  Esperado: {expected}")
    print(f"  Obtenido: {result_clean}")
    
    if result_clean == expected:
        print("  ✓ PASÓ\n")
        return True
    else:
        print("  ✗ FALLÓ\n")
        return False


def test_example_2():
    """Ejemplo 2: Encriptación con llave alfabética D"""
    print("Test 2: Encriptación con llave alfabética D")
    machine = create_encrypt_machine()
    input_str = "D#ROMA NO FUE CONSTRUIDA EN UN DIA"
    expected = "URPD QR IXH FRQVWUXLGD HQ XQ GLD"
    result = machine.encrypt(input_str)
    
    result_clean = result.replace('.', '').strip()
    
    print(f"  Entrada:  {input_str}")
    print(f"  Esperado: {expected}")
    print(f"  Obtenido: {result_clean}")
    
    if result_clean == expected:
        print("  ✓ PASÓ\n")
        return True
    else:
        print("  ✗ FALLÓ\n")
        return False


def test_example_3():
    """Ejemplo 3: Decriptación con llave numérica 3"""
    print("Test 3: Decriptación con llave numérica 3")
    machine = create_decrypt_machine()
    input_str = "3#URPD QR IXH FRQVWUXLGD HQ XQ GLD"
    expected = "ROMA NO FUE CONSTRUIDA EN UN DIA"
    result = machine.decrypt(input_str)
    
    result_clean = result.replace('.', '').strip()
    
    print(f"  Entrada:  {input_str}")
    print(f"  Esperado: {expected}")
    print(f"  Obtenido: {result_clean}")
    
    if result_clean == expected:
        print("  ✓ PASÓ\n")
        return True
    else:
        print("  ✗ FALLÓ\n")
        return False


def test_example_4():
    """Ejemplo 4: Decriptación con llave alfabética D"""
    print("Test 4: Decriptación con llave alfabética D")
    machine = create_decrypt_machine()
    input_str = "D#URPD QR IXH FRQVWUXLGD HQ XQ GLD"
    expected = "ROMA NO FUE CONSTRUIDA EN UN DIA"
    result = machine.decrypt(input_str)
    
    result_clean = result.replace('.', '').strip()
    
    print(f"  Entrada:  {input_str}")
    print(f"  Esperado: {expected}")
    print(f"  Obtenido: {result_clean}")
    
    if result_clean == expected:
        print("  ✓ PASÓ\n")
        return True
    else:
        print("  ✗ FALLÓ\n")
        return False


def test_round_trip():
    """Test de ida y vuelta: encriptar y luego decriptar"""
    print("Test 5: Round-trip (encriptar → decriptar)")
    encrypt_machine = create_encrypt_machine()
    decrypt_machine = create_decrypt_machine()
    
    original = "5#HOLA MUNDO ESTO ES UNA PRUEBA"
    
    # Encriptar
    encrypted = encrypt_machine.encrypt(original)
    
    # Decriptar
    key = original.split('#')[0]
    to_decrypt = f"{key}#{encrypted}"
    decrypted = decrypt_machine.decrypt(to_decrypt)
    
    original_message = original.split('#')[1]
    
    print(f"  Original:    {original_message}")
    print(f"  Encriptado:  {encrypted}")
    print(f"  Decriptado:  {decrypted}")
    
    if decrypted.strip().upper() == original_message.upper():
        print("  ✓ PASÓ\n")
        return True
    else:
        print("  ✗ FALLÓ\n")
        return False


def main():
    """Ejecuta todas las pruebas"""
    print("=" * 70)
    print("  PRUEBAS AUTOMÁTICAS - Simulador de MT para Cifrado César")
    print("=" * 70)
    print()
    
    tests = [
        test_example_1,
        test_example_2,
        test_example_3,
        test_example_4,
        test_round_trip
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("=" * 70)
    print(f"  RESULTADOS: {passed}/{total} pruebas pasaron")
    print("=" * 70)
    
    if passed == total:
        print("\n✓ ¡Todas las pruebas pasaron exitosamente!")
        return 0
    else:
        print(f"\n✗ {total - passed} prueba(s) fallaron")
        return 1


if __name__ == "__main__":
    exit(main())
