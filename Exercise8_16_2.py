# PROGRAM UTAMA

# mengimpor seluruh modul
import Exercise8_16_1 as greetings

greetings.say_hello("Yasir")

# mengimpor fungsi tertentu
from Exercise8_16_1 import say_hello

say_hello("Yasir")

# mengimpor fungsi tertentu dengan alias
from Exercise8_16_1 import say_hello as fn

fn("Yasir")

# mengimpor modul dengan alias
import Exercise8_16_1 as mn

mn.say_hello("Yasir")

# mengimpor semua fungsi dari modul
from Exercise8_16_1 import *

say_hello("Yasir")