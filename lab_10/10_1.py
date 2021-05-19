# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]. 
# Dodaj etykietę do linii wykresu i wyświetl legendę. Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) 
# oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 20, 1)

plt.title('Wykres funkcji f(x) = 1/x dla x [1, 20]')
plt.plot(1/x, label='f(x) = 1/x')
plt.axis([1,20,0,1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()


plt.show()