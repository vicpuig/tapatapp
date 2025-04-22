# Test Unitarios

Los **test unitarios** son una técnica de prueba de software que consiste en verificar el funcionamiento de las unidades más pequeñas de código, como funciones, métodos o clases, de forma aislada. Su objetivo principal es garantizar que cada unidad funcione correctamente de manera independiente.

## Características principales:
- **Aislados**: Se prueban sin depender de otras partes del sistema.
- **Automatizados**: Se ejecutan automáticamente para detectar errores rápidamente.
- **Repetibles**: Pueden ejecutarse tantas veces como sea necesario, especialmente tras cambios en el código.

## Beneficios:
- Detectan errores en etapas tempranas del desarrollo.
- Facilitan el mantenimiento del código.
- Ayudan a prevenir regresiones (errores introducidos al modificar el código).
- Mejoran la confianza en la calidad del software.

# Llibreries de test amb Python

Python ofereix diverses llibreries per a realitzar tests de manera eficient. Algunes de les més utilitzades són:

## Llibreries populars:
- **unittest**: Llibreria estàndard integrada a Python per a test unitari.
- **pytest**: Llibreria avançada amb una sintaxi més senzilla i funcionalitats extenses.
- **nose2**: Successor de `nose`, compatible amb `unittest`.
- **doctest**: Permet escriure tests dins dels docstrings del codi.
- **hypothesis**: Llibreria per a tests basats en propietats, generant dades d'entrada automàticament.

---

# Com funciona `unittest`?

`unittest` és la llibreria estàndard de Python per a test unitari. Segueix el model **xUnit** i permet estructurar i executar tests de manera organitzada.

## Estructura bàsica:
1. Cada test es defineix com un mètode dins d'una classe que hereta de `unittest.TestCase`.
2. Les assertions (`assertEqual`, `assertTrue`, etc.) s'utilitzen per comprovar si el resultat esperat coincideix amb el resultat obtingut.
    