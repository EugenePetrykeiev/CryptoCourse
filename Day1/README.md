# Blockchain course
## Day 1
Написать функцию для брутфорса значений из диапазона для нахождения ключа. Цель функции - перебирать значения ключа от  0x00…0  до тех пор, пока не будет найдено значение, равное предварительно сгенерированному ключевому. Функция должна выводить количество времени в миллисекундах, которое было затрачено на нахождение ключа.

```sh
python ./day1/task3.py
```

### Results

```sh
python -m cProfile -ms time task3.py 
```
```sh
2770 function calls (2714 primitive calls) in 0.018 seconds
```
>Для удобства, выводятся сгенерированные ключи и найденные ключи. Также береться их хеш и сравнивается для проверки полного совпадения списков.