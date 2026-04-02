# wfly-deploy

wfly-deploy es una pequeña utilidad que automatiza el flujo de compilar y mover el .ear a la carpeta de `standalone/deployments` en Wildfly para la práctica final de la asignatura Test, Integración y Evolución de Software.

## 📋 ¿Qué es lo que hace?
1. Crea una compilación limpia de la aplicación usando Maven (`mvn clean install`).
2. Identifica el archivo `.ear` generado dentro del módulo correspondiente para tu equipo (ej: `bayes00-ear`).
3. Despliega automáticamente el archivo a la carpeta de despliegues de Wildfly.

## ⚙️ Configuración inicial
Cuando se ejecute el script, buscará un fichero llamado `.wflydeply_conf.json`, en el cual se guarda la configuración del script.

Si no se detecta este fichero, pedirá los siguientes datos:
- **Ruta de Wildfly**: La ruta absoluta hasta la carpeta `deployments` de Wildfly
- **Número de equipo de la práctica**: Este número se corresponde con el número de equipo de la práctica (ej: el grupo bayes00 pondrá 00).

> Si te equivocas poniendo el número o cambias la ruta donde tienes Wildfly, puedes borrar este archivo para que el script la próxima vez te vuelva a preguntar los datos o cambiar manualmente los datos cambiados en el archivo `.wflydeploy_conf.json`.

## 🚀 ¿Cómo ejecutarlo?

### Opción A: Usando el ejecutable (Windows/MacOS)
1. Descarga el archivo adecuado a tu plataforma.
2. Mover el ejecutable a la carpeta de la práctica (bayesXX).
3. Ejecutar el archivo desde la terminal.

### Opción B: Ejecutar el script con Python
1. Tener Python instalado.
2. Copiar el archivo `wfly-deploy.py` a la carpeta de la práctica (bayesXX).
3. Ejecuta el archivo con Python.

### Opcional: Compilar un ejecutable para tu sistema
Si quisieras generar tu propio ejecutable a partir del código fuente, puedes seguir los siguientes pasos:

1. Instala PyInstaller:
```bash
pip install pyinstaller
```
2. Generar el binario:
```bash
pyinstaller --onefile wfly-deploy.py
```

## ✅ Requisitos
- **Maven**: debe estar instalado y configurado para que el sistema reconozca `mvn -v`.
- **Wildfly**: Debes tener Wildfly descargado en tu sistema. No es necesario que se esté ejecutando para ejecutar el script.