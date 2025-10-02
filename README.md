# Mejorando un Workflow con GitHub Actions

# Descripción
A partir de un repositorio base realizado por el profesor, en esta práctica he trabajado con `workflow` mediante `github actions`, cuyo objetivo principal ha sido mejorar uno ya existente para la generación automática de documentación. El ejercicio consiste en comprender un flujo básico que ya está implementado y posteriormente, adaptarlo para que fuese capaz de generar documentación en diferentes formatos (HTML y MD) de forma automática.

# Introducción


# Desarrollo de la práctica
- Comencé a comprender el flujo de trabajo, el cual ejecutaba pruebas unitarias y actualizaba automáticamente el `README` del repositorio.
- Si bien el código original funcionaba, basándome en un `README` anterior de otro ejercicio, decidí actualizar el código para que, además del mensaje de los tests, también muestre la fecha y hora haciendo uso del módulo `datetime`.  
- Removí el `break` que había en el condicional que estaba dentro del bucle `for`, pues borraba todo el contenido del `README` que estaba después de "Estado de los tests".
- Documenté la función `saludo` del archivo `main.py`.
- Instalé pdoc utilizandp `pip install pdoc` y probé a utilizar `pdoc -o docs/html main.py` de manera local en mi proyecto.
- Configuré el archivo `ci.yaml` para que instalase las dependencias necesarias (en este caso, pdoc) con `run: pip install pdoc`.
- Añadí el comando que utilicé de manera local en el ci.yaml para que se genere la documentación al activar la action.
- Cambié varios mensajes para que fuesen más descriptivos en el archivo `ci.yaml` y añadí otro commit automático de los archivos que se generan en la carpeta `docs/` utilizando `git-auto-commit-action`, haciendo que cada vez que `workflow` genere nueva documentación, los cambios queden registrados en el historial de commits con el mensaje "documentación web actualizada".
# Conclusión
# Bibliografía

## Estado de los tests
- ✅ 2025-10-02 20:50:18.075051 Tests correctos
- ✅ 2025-10-02 20:34:26.742232 Tests correctos
- ✅ 2025-10-02 20:22:33.413266 Tests correctos

# Preguntas para la Evaluación

**a): Identificación de herramientas de generación de documentación**
- ¿Qué herramienta o generador (p. ej., Sphinx, pdoc, Javadoc, Doxygen, Dokka) utilizaste en el workflow para crear la documentación en /docs?

**b): Documentación de componentes**
- Muestra un fragmento del código con comentarios/docstrings estructurados (p. ej., :param, :return: o etiquetas equivalentes) que haya sido procesado por la herramienta. Comenta que estilo de documentación has utlicado: (p. ej., reStructuredText, Google Style, KDoc)

**c): Multiformato**
- ¿Qué segundo formato (además de HTML) generaste? Explica la configuración o comandos del workflow y herramientas que lo producen.

**d): Colaboración**
- Explica cómo GitHub facilita mantener la documentación (actualizaciones del README.md y de /docs) cuando colaboran varias personas (PRs, reviews, checks de CI, protección de ramas).

**e): Control de versiones**
- Muestra mensajes de commit que evidencien el nuevo workflow. ¿Son claros y descriptivos? Justifícalo. Ademas de un conjunto de mensajes de tus commits.

**f): Accesibilidad y seguridad**
- ¿Qué medidas/configuración del repositorio garantizan que solo personal autorizado accede al código y la documentación? (p. ej., repositorio privado, equipos, roles, claves/secretos, branch protection).

**g): Instalación/uso documentados**
- Indica dónde en el README.md explicas el funcionamiento del workflow y dónde detallas las herramientas y comandos de documentación.

**h): Integración continua**
- Justifica por qué el workflow utilizado es CI. ¿Qué evento dispara automáticamente la generación/actualización de la documentación (p. ej., push, pull_request, workflow_dispatch)?
