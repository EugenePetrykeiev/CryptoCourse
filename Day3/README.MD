# Blockchain course

## Day 2

Написать библиотеку, позволяющую:

- Преобразование HEX значения в Little Endian значение
- Преобразование HEX значения в Big Endian значение
- Преобразование Little Endian значения в HEX значение
- Преобразование BIG Endian значения в HEX значение

Основной файл запуска программы:

```sh
python ./day2/main.py
```

## Методы для использования

### HEX 2 INT

```python 
hex_to_int(h: str, end: str)
```

Принимает в качестве аргументов __hex__ число в формате __str__ и порядок байт - __big__ или __little__. Для
самоконтроля делает обратное преобразование _from ...-endian to hex_ и проверяется контрольная сумма ответов.

```python
from Converter import Converter as Cnv

Cnv.hex_to_int('0xabcdef', 'big')
```

> Value to big endian:  11259375 Value from big endian:  0xABCDEF
> Checksum:  4255365060916225561 4255365060916225561 True

### INT 2 HEX

Принимает в качестве аргументов __dec__ число в формате __int__ и порядок байт - __big__ или __little__. Для
самоконтроля делает обратное преобразование _from ...-endian to dec_ и проверяется контрольная сумма ответов.

```python
from Converter import Converter as Cnv

Cnv.int_to_hex(255, 'little', bytes_num=32)
```

> Value from little endian:  0xFF00000000000000000000000000000000000000000000000000000000000000 Value to little endian:  255
> Checksum:  255 255 True

### HEX 2 BIG-ENDIAN

```python
to_big_endian(h: str) -> int:
```

Принимает в качестве аргумента __hex__ число в формате __str__ и возвращает число в порядке байт - Big-endian. Возращает
big-endian число типа __int__

### HEX 2 LITTLE-ENDIAN

```python
to_little_endian(h: str) -> int:
```

### BIG-ENDIAN DEC 2 HEX

Принимает в качестве аргумента __dec__ число в формате __int__ и возвращает __hex__ значение в порядке байт -
Big-endian, в формате __str__.

```python
from_big_endian(d: int) -> str:
```

### LITTLE-ENDIAN DEC 2 HEX

Принимает в качестве аргумента __dec__ число в формате __int__, и количество байт для _hex_ значения. Возвращает __hex__
число в порядке байт - Big-endian, в формате __str__.

```python
from_big_endian(d: int) -> str:
```

### HEX 2 BINARY BIG ENDIAN

Принимает в качестве аргумента __hex__ число в формате __str__. Возвращает бинарное значение разделенное по 8 бит, в
порядке байт - Big-endian

```python
hex_to_binary_be(h: str) -> list:
```

### HEX 2 BINARY LITTLE ENDIAN

Принимает в качестве аргумента __hex__ число в формате __str__. Возвращает бинарное значение разделенное по 8 бит, в
порядке байт - Little-endian

```python
hex_to_binary_le(d: str) -> list:
```
