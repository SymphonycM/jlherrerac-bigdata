Tarea correspondiente al lab de MapReduce, resolviendo el punto 1

El archivo MrLab.py utiliza la librería MrJob para hacer el mapreduce en python, la entrada debe ser de texto separado por comas y se ejecuta con el comando:

- python MrLab.py <path de archivo(s)> 

Utilizando como entrada el ejemplo del repositorio de la materia:

- python MrLab.py dataempleados.csv

La salida del programa se divide en tres partes:

- Los datos que comienzan con "empleado" corresponden al primer numeral del ejercicio, promedio de salario por empleado
- Los datos que comienzan con "SE" corresponden al promedio de salario por sector económico
- Comienzan con "Emp/SE" los datos que corresponden a la cantidad de sectores económicos por empleado, el primero número después del tag es el empleado y el siguiente es la cantidad de sectores económicos