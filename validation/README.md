# Validación de datos en STRUVAL

El servicio de Validación Estructural (llamado Struval) realiza la validación estructural de los archivos de datos estadísticos siguiendo el Modelo de Información SDMX para un flujo de datos determinado. Garantiza que un archivo de datos respete los siguientes elementos clave

    * Cumplimiento de SDMX en cuanto a las comprobaciones del formato del archivo y la integridad en cuanto a los campos obligatorios;
    * La conformidad con SDMX en cuanto a la estructura y la codificación definidas por la definición de la estructura de datos (DSD);
    * Las restricciones definidas para los respectivos flujos de datos.

Este script permite una comoda validación y obtención de resultados.

## Notas
La validación se hace 1-1 con los dsd's y los dataflows, mientras que en el actual estado de nuestro proyecto debería ser 1-N,
