"""
TESZTELENDŐ FELADAT - NumberValidator osztály unit tesztek

A feladat: Írj unit teszteket a NumberValidator osztály metódusaihoz!
Használd a különböző assert típusokat!
"""

# import modul
import pytest
from number_validator import NumberValidator
# from file import ClassName


# ============================================================================
# FELADAT: Írd meg az alábbi teszteket!
# ============================================================================

def test_is_even_equal():
    """1.1 Assert equal - páros szám ellenőrzés"""
    processor = NumberValidator()
    resultparos = processor.is_even(4)
    assert resultparos == True
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_even metódust páros számmal
    # TODO: Ellenőrizd, hogy az eredmény True
    


def test_is_even_not_equal():
    """1.2 Assert not equal - páratlan szám ellenőrzés"""
    processor = NumberValidator()
    resultparatlan = processor.is_even(5)
    assert resultparatlan != True
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_even metódust páratlan számmal
    # TODO: Ellenőrizd, hogy az eredmény NEM egyenlő True-val
    


def test_is_even_with_zero():
    """1.3 Speciális eset - nulla kezelése"""
    processor = NumberValidator()
    resultnulla = processor.is_even(0)
    assert resultnulla == True
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_even metódust 0-val
    # TODO: Ellenőrizd, hogy az eredmény True-e?
    


def test_is_positive_greater_than():
    """2.1 Assert > - pozitív szám ellenőrzés"""
    processor = NumberValidator()
    resultpozitiv = processor.is_positive(3)
    assert resultpozitiv == True
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_positive metódust pozitív számmal
    # TODO: Ellenőrizd, hogy az eredmény True-e?
    


def test_is_positive_with_negative():
    """2.2 Negatív szám ellenőrzés"""
    processor = NumberValidator()
    resultpozitiv = processor.is_positive(4)
    resultnegativ = processor.is_positive(-4)
    assert resultpozitiv == True
    assert resultnegativ == False
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_positive metódust pozitív számmal
    # TODO: Hívd meg az is_positive metódust negatív számmal
    # TODO: Ellenőrizd, hogy az eredmény True vagy False?
    


def test_is_in_range_less_than():
    """3.1 Assert <, <= - tartományon belüli ellenőrzés"""
    processor = NumberValidator()
    resultbelul = processor.is_in_range(5,0,9)
    assert resultbelul == True
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_in_range metódust egy számmal, ami a tartományban van
    # TODO: Ellenőrizd, hogy az eredmény True
    


def test_is_in_range_out_of_range():
    """3.2 Assert <, <= - tartományon kívüli ellenőrzés"""
    processor = NumberValidator()
    resultkivul = processor.is_in_range(3,4,15)
    assert resultkivul == False
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_in_range metódust egy számmal, ami a tartományon kívül van
    # TODO: Ellenőrizd, hogy az eredmény True
    


def test_get_absolute_value_isinstance():
    """4. Assert isinstance - típus ellenőrzés"""
    processor = NumberValidator()
    resultint = processor.get_absolute_value(-3) 
    resultstring = processor.get_absolute_value(5) 
    assert isinstance(resultint, int) == True
    assert isinstance(resultstring, str) == False
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg a get_absolute_value metódust negatív számmal (pl. -5)
    # TODO: Ellenőrizd, hogy az eredmény integer típusú
    # TODO: Ellenőrizd, hogy az eredmény NEM string típusú
    


def test_is_divisible_by_true_false():
    """5. Assert True/False - oszthatóság ellenőrzés"""
    processor = NumberValidator()
    resultoszthato = processor.is_divisible_by(5, 5)
    assert resultoszthato == True
    resultnemoszthato = processor.is_divisible_by(4,3)
    assert resultnemoszthato == False
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_divisible_by metódust olyan számmal, ami osztható egymással
    # TODO: Ellenőrizd, hogy az eredmény True
    # TODO: Hívd meg olyan számmal, ami NEM osztható (maradékos osztás)
    # TODO: Ellenőrizd, hogy az eredmény False
    


def test_square_none():
    """6. Assert None - None ellenőrzés"""
    processor = NumberValidator()
    resultnone = processor.square(None)
    resultszam = processor.square(9)
    assert resultnone == 0
    assert resultszam != None
    assert resultszam != 0
    
    

    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg a square metódust None értékkel
    # TODO: Ellenőrizd, hogy az eredmény NEM None
    # TODO: Ellenőrizd, hogy az eredmény 0-e?
    


def test_is_prime_multiple_asserts():
    """7. Több assert egy tesztben - prímszám ellenőrzés"""
    processor = NumberValidator()
    resultprim = processor.is_prime(7)
    assert resultprim == True
    assert resultprim != False
    assert isinstance(resultprim, bool) == True
    

    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_prime metódust prímszámmal
    # TODO: Ellenőrizd több assert-tel:
    #      - Az eredmény True
    #      - Az eredmény boolean típusú
    #      - Az eredmény nem egyenlő False-szal
    

