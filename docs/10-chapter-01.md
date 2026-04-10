# Capítulo I: Introducción

## 1.1. Startup Profile

### 1.1.1. Descripción de la Startup
**RQLS (Requisitions, Quotes, Logistics System)** es una startup tecnológica peruana enfocada al desarrollo de soluciones Software as a Service (SaaS) para la optimización de procesos operativos en el sector construcción. Nuestra organización se enfoca en cerrar la brecha digital en las pequeñas y medianas empresas (MYPES) constructoras mediante herramientas que transforman la gestión logística empírica en un proceso basado en datos, transparencia e incluso eficiencia.

**Misión:** Centralizar la comunicación entre el campo de trabajo y la oficina administrativa con el objetivo de eliminar sobrecostos y retrasos innecesarios durante la ejecución de obras.

### 1.1.2. Perfiles de integrantes del equipo

| Integrantes | Descripción |
| :--- | :--- |
| **Castillo Yataco, Mauricio Sebastián** | Soy estudiante de Ingeniería de Software, apasionado por la creación de soluciones tecnológicas que mejoren la vida de las personas. Mi enfoque va más allá de la programación, ya que me interesa desarrollar experiencias digitales que sean tanto funcionales como agradables para el usuario, Conocimiento básico en el lenguaje de C++, Html y CSS, presento además las aptitudes de responsabilidad, cooperación, comunicación, flexibilidad y adaptabilidad. |
| **Morales Venegas, David Joel** | [Descripción pendiente] |
| **Paucar Zenteno, Jesús Fernando** | Soy un estudiante de ingeniería de software con una gran pasión por la creación de soluciones innovadoras. Me considero una persona proactiva y orientada a resultados, siempre buscando aprender y aplicar nuevas tecnologías. Mi objetivo es contribuir de manera significativa al proyecto, asegurando que cada tarea se complete con la más alta calidad y eficiencia. |
| **Viza Quispe, Marlon Packard** | Estudiante de 20 años, responsable y proactivo, con una sólida base técnica en C++. Destaco por mi capacidad para aportar soluciones creativas y mi compromiso con el aprendizaje constante en entornos profesionales. Busco asumir retos que potencien mi desarrollo y contribuyan al éxito colectivo de mi equipo. |

---

## 1.2. Solution Profile

### 1.2.1. Antecedentes y problemática
En el Perú, el sector construcción es un pilar económico, sin embargo, las MYPES constructoras presentan un bajo nivel de madurez digital. El problema central reside en el descontrol del flujo de abastecimiento. Actualmente, las requisiciones de materiales se realizan de manera informal (WhatsApp, llamadas o papel), lo que genera pérdida de trazabilidad, compras duplicadas y falta de aprobación gerencial en tiempo real.

**Técnica 5W2H aplicada al problema:**
* **Who (¿Quién?):** Ingenieros residentes (campo), jefes de logística (compras) y gerentes generales de MYPES constructoras.
* **What (¿Qué?):** Ineficiencia en el flujo de solicitud y aprobación de materiales, y falta de visibilidad sobre los gastos operativos de obra.
* **Where (¿Dónde?):** En la comunicación crítica entre la obra física y el centro administrativo de la constructora.
* **When (¿Cuándo?):** Durante la etapa de ejecución del proyecto, específicamente en el ciclo de abastecimiento diario.
* **Why (¿Por qué?):** Por la carencia de un sistema centralizado que formalice las solicitudes y permita comparar cotizaciones antes de autorizar pagos.
* **How (¿Cómo?):** Los procesos se ejecutan manualmente, sin validación presupuestal inmediata, lo que expone a la empresa a sobrecostos.
* **How Much (¿Cuánto?):** Se estima que el desorden logístico genera pérdidas de hasta un 15% del presupuesto asignado a insumos por errores en la compra o especificaciones técnicas incorrectas.

---

### 1.2.2. Lean UX Process

#### 1.2.2.1. Lean UX Problem Statements
Actualmente, las empresas del sector construcción gestionan sus compras y requisiciones de manera informal y desordenada, utilizando herramientas no especializadas como Excel, WhatsApp o papel. Esto genera un problema crítico en la comunicación entre el Ingeniero en obra y el área de Logística, resultando en pérdida de tiempo, compras sin cotizaciones comparativas y nulo control gerencial. ¿Cómo podemos diseñar un Sistema Web SaaS que centralice y automatice el flujo de requisiciones, desde la solicitud inicial en obra hasta la aprobación gerencial y emisión de la Orden de Compra?

#### 1.2.2.2. Lean UX Assumptions

**Business Assumptions:**
1. Las empresas constructoras están dispuestas a pagar por licencias de un software SaaS para modernizar y controlar su logística.
2. El sistema reducirá significativamente los tiempos de abastecimiento y evitará compras de emergencia no autorizadas.
3. El valor principal para los tomadores de decisiones (Gerentes) es la visualización de cotizaciones comparadas antes de aprobar un gasto.

**User Assumptions:**
1. Los Ingenieros (residentes de obra) necesitan una interfaz rápida e intuitiva para solicitar materiales formales sin tener que hacer la compra directamente.
2. El personal de Logística/Compras requiere un módulo para gestionar proveedores y subir cotizaciones al sistema ágilmente.
3. Los Gerentes necesitan un dashboard claro que les permita aprobar o rechazar compras de forma remota con un solo clic.an un dashboard claro que les permita aprobar o rechazar compras de forma remota con un solo clic.

**Business Outcome Assumptions:**
* Reducir en un 40% el tiempo administrativo desde la creación de la requisición hasta la emisión de la orden de compra.
* Lograr que el 100% de las compras institucionales pasen por un flujo de aprobación con sustento de cotización.

**User Outcome Assumptions:**
* Reducir en un 40% el tiempo administrativo desde la creación de la requisición hasta la emisión de la orden de compra.
* Lograr que el 100% de las compras institucionales pasen por un flujo de aprobación con sustento de cotización.
  **Features:**
* **Módulo de Creación de Requisiciones:** Interfaz simplificada para que el Ingeniero de Obra solicite materiales y cantidades específicas.
* **Directorio de Proveedores y Cotizaciones:** Espacio para que Logística registre a sus proveedores y adjunte las propuestas económicas.
* **Panel Comparativo y Sistema de Aprobación:** Interfaz donde el Gerente revisa las opciones de precio y autoriza el gasto con un clic.
* **Generador de Órdenes de Compra Automáticas:** Emisión de documentos PDF oficiales y automáticos tras la aprobación gerencial.
* **Dashboard de Trazabilidad de Estados:** Panel visual en tiempo real para rastrear el ciclo de vida de cada solicitud.

#### 1.2.2.3. Lean UX Hypothesis Statements
* **Hipótesis 1:** Creemos que al centralizar las solicitudes de materiales en una plataforma web accesible desde la obra, reduciremos drásticamente los tiempos de espera. Lo sabremos cuando el tiempo promedio entre la creación de una solicitud y su aprobación por logística baje de 48 horas a menos de 8 horas.
* **Hipótesis 2:** Creemos que al implementar un tablero de control (Dashboard) para los Jefes de Proyectos, eliminaremos la falta de visibilidad del presupuesto. Lo sabremos cuando las desviaciones de costos por compras de emergencia se reduzcan en un 15% durante el primer trimestre de uso.
* **Hipótesis 3:** Creemos que al automatizar los flujos de comunicación entre obra y logística, optimizaremos el proceso de abastecimiento. Lo sabremos cuando el número de llamadas o mensajes para consultar el estado de un pedido disminuya en un 50%.
* **Hipótesis 4:** Creemos que al digitalizar el historial de proveedores y cotizaciones, facilitaremos la toma de decisiones gerenciales. Lo sabremos cuando el tiempo dedicado a la comparación manual de cotizaciones se reduzca de 4 horas semanales a solo 15 minutos.

#### 1.2.2.4. Lean UX Canvas

| 1. Business Problem | 5. Solution | 2. Business Outcomes |
| :--- | :--- | :--- |
| Gestión informal de compras en constructoras, causando desorden, retrasos en la obra, falta de cotizaciones comparadas y nulo control de aprobaciones y presupuesto. | **RQLS:** Plataforma Web SaaS que permite crear requisiciones digitales, gestionar flujos de aprobación y monitorear el gasto de materiales frente al presupuesto. | • Digitalización del 100% de los procesos de compra.<br>• Reducción del 40% en tiempos de ciclo de abastecimiento.<br>• Disminución de sobrecostos por compras no planificadas. |

| 3. Users & Customers | 4. User Benefits | 6. Solution Ideas |
| :--- | :--- | :--- |
| • Ingenieros / Residentes de Obra.<br>• Encargados de Logística.<br>• Jefes de Proyecto / Gerentes. | • Aprobación de materiales remota en un clic.<br>• Control total del presupuesto en tiempo real.<br>• Historial transparente de cotizaciones. | • Formulario digital de requisición de materiales.<br>• Dashboard gerencial comparativo de cotizaciones.<br>• Sistema de seguimiento de estados de la orden. |

| 7. Hypothesis | 8. What’s the most important thing we need to learn first? |
| :--- | :--- |
| Creemos que la digitalización de las solicitudes de compra mediante un SaaS ordenará el flujo logístico, mejorando la rentabilidad de la constructora. | ¿Están los Ingenieros en campo dispuestos a adoptar una plataforma web en lugar de las llamadas o mensajes de WhatsApp que usan actualmente para pedir materiales? |

---

## 1.3. Segmentos Objetivos
1. **Jefes de Proyectos:** Profesionales encargados de la planificación, control presupuestal y ejecución de las obras en empresas constructoras. Son el puente entre el campo y la administración, y necesitan una plataforma centralizada para gestionar las requisiciones de materiales, supervisar el flujo de aprobaciones logísticas y asegurar que el abastecimiento no retrase el cronograma de trabajo, manteniendo siempre el control de los costos mediante datos en tiempo real.
