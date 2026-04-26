# Capítulo I: Introducción

## 1.1. Startup Profile

### 1.1.1. Descripción de la Startup
**RQLS (Requisitions, Quotes, Logistics System)** es una startup tecnológica peruana enfocada en el desarrollo de soluciones Software as a Service (SaaS). Nuestra organización se especializa en cerrar la brecha digital en las micro y pequeñas empresas (MYPES) del sector construcción. Según el Instituto Nacional de Estadística e Informática (INEI, 2024), las MYPES representan el 99,7% de las unidades económicas del país y enfrentan costos logísticos que ascienden al 21,1% de sus ventas (ComexPerú, 2023). RQLS transforma la gestión operativa empírica en procesos basados en datos y transparencia.

**Misión:** Democratizar el acceso a herramientas de control logístico para las MYPES constructoras, permitiéndoles eliminar sobrecostos mediante la centralización de datos en tiempo real (Pacco Constructores, 2021).

**Visión:** Ser el estándar tecnológico en la gestión de abastecimiento para el sector construcción en Latinoamérica hacia el 2030.

**Valores:** Transparencia operativa, integridad de datos, innovación centrada en el operario y eficiencia.

### 1.1.2. Perfiles de integrantes del equipo
| Imagen | Información del Integrante |
|:---:|:---|
| <img src="./assets/chapter-01/Castillo_Foto.jpg" width="100" /> | **Castillo Yataco, Mauricio Sebastián** (U202113229)<br>**Carrera:** Ingeniería de Software<br>**Perfil:** Soy estudiante de Ingeniería de Software, apasionado por la creación de soluciones tecnológicas que mejoren la vida de las personas. Mi enfoque va más allá de la programación, ya que me interesa desarrollar experiencias digitales funcionales y agradables para el usuario. Poseo conocimientos básicos en C++, HTML y CSS, y destaco por mi responsabilidad, cooperación, comunicación, flexibilidad y adaptabilidad. |
| <img src="./assets/chapter-01/david_foto.jpeg" width="100" /> | **Morales Venegas, David Joel** (U20231B504)<br>**Carrera:** Ingeniería de Software<br>**Perfil:** Estudiante de Ingeniería de Software con formación intermedia en el desarrollo de aplicaciones web. Me adapto al trabajo técnico del equipo, priorizando código funcional, entendible y alineado a los requerimientos del proyecto, con disposición para mejorar y corregir en función de pruebas y resultados. |
| <img src="./assets/chapter-01/foto-fernando.jpg" width="100" /> | **Paucar Zenteno, Jesús Fernando** (U202316687)<br>**Carrera:** Ingeniería de Software<br>**Perfil:** Soy estudiante de Ingeniería de Software con gran pasión por la creación de soluciones innovadoras. Me considero una persona proactiva y orientada a resultados, con interés constante en aprender y aplicar nuevas tecnologías. Busco contribuir significativamente al proyecto, asegurando calidad y eficiencia en cada tarea. |
| <img src="./assets/chapter-01/Marlon.jpg" width="100" /> | **Viza Quispe, Marlon Packard** (U202322849)<br>**Carrera:** Ingeniería de Software<br>**Perfil:** Estudiante de 20 años, responsable y proactivo, con sólida base técnica en C++. Destaco por mi capacidad de aportar soluciones creativas y mi compromiso con el aprendizaje continuo en entornos profesionales. Busco asumir retos que potencien mi desarrollo y contribuyan al éxito del equipo. |
| <img src="./assets/chapter-01/caceres_foto.jpeg" width="100" /> | **Cáceres Pizarro, Albino Florencio** (U201923820)<br>**Carrera:** Ingeniería de Software<br>**Perfil:** Me considero una persona responsable y proactiva que le gusta trabajar en equipo. Además, siempre estoy abierto a ayudar, en lo posible, a cualquier integrante del equipo. Además, busco adaptarme rápidamente a los diversos retos que se presentan en el ciclo. |

---

## 1.2. Solution Profile
Nuestra solución, Buildline, es una plataforma Web SaaS diseñada para gestionar de extremo a extremo las compras institucionales en constructoras. Digitaliza la comunicación entre el residente de obra (solicitud), el área de compras (cotización) y la gerencia (aprobación), eliminando pérdidas de hasta el 15% del presupuesto generadas por la gestión informal (Rodríguez Vargas, 2019).

### 1.2.1. Antecedentes y problemática
El sector construcción en el Perú proyecta una tasa de crecimiento del 6,5% para el periodo 2025, impulsado principalmente por la reactivación de la inversión en infraestructura pública (El Peruano, 2025). Esta dinámica macroeconómica se encuentra condicionada por el desempeño de las MYPES, las cuales concentran la mayor parte de la operatividad del sector pero presentan un costo logístico promedio de 21,1%, cifra significativamente superior al 16% registrado a nivel nacional (ComexPerú, 2023; INEI, 2024). Esta disparidad económica se vincula directamente a la falta de herramientas especializadas para la gestión administrativa en empresas de menor escala.

La gestión de adquisiciones en estas organizaciones se caracteriza por la ausencia de trazabilidad y formalidad técnica. Según investigaciones aplicadas en el sector, el 74,1% de los responsables de MYPES constructoras califica como inadecuado el seguimiento de compras, mientras que el 77,8% reporta incidentes recurrentes donde los insumos entregados no coinciden con las especificaciones técnicas solicitadas (Rodríguez Vargas, 2019). Estos errores operativos, derivados de la dependencia de canales informales como WhatsApp o registros manuales en papel, causan parálisis de obra en un 18% de los casos y obligan a realizar compras de urgencia no planificadas que representan el 12% del gasto logístico total (Tarraga Durand & Miranda Mitma, 2025).

El retraso en la madurez digital del sector construcción se refleja en que el 40% de los proyectos de infraestructura superan el presupuesto original debido a la ineficiencia en la planificación de recursos y la comunicación fragmentada (Ruiz Escajadillo, 2024). A pesar de que la integración de plataformas de gestión de proyectos ha demostrado incrementos de productividad del 30%, persiste una brecha tecnológica en las pequeñas empresas debido al desconocimiento de soluciones escalables y a la alta resistencia al cambio del personal operativo (ESAN, 2023; CAPECO, 2024). En este escenario, la transición hacia sistemas SaaS especializados permite la centralización de datos necesaria para la toma de decisiones financieras y el control estricto del presupuesto de obra.

**Técnica "The 5W's y 2H's" aplicada al problema:**

| The 5W's y 2H's | Pregunta                     | Descripción                                                                                                                                                                                                                                             |
| :-------------- | :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Who             | ¿Quiénes están involucrados? | El personal operativo y directivo de las MYPES constructoras, específicamente ingenieros residentes, jefes de logística y gerentes. El 74,1% de los responsables considera deficientes los mecanismos actuales de seguimiento (Rodríguez Vargas, 2019). |
| What            | ¿Cuál es el problema?        | Ineficiencia en el flujo de suministro interno con falta de concordancia técnica en el 77,8% de los productos recibidos y ausencia de proyecciones de demanda en el 70,3% de las operaciones (Rodríguez Vargas, 2019).                                  |
| Where           | ¿Dónde ocurre?               | En la brecha informativa entre las obras de edificación física y el centro administrativo. Lima concentra el 45,7% de estas empresas, pero la ineficiencia es crítica en provincias por barreras de transporte (INEI, 2024).                            |
| When            | ¿Cuándo sucede?              | Durante la etapa de ejecución técnica, manifestándose en cada ciclo de abastecimiento diario. Esta problemática es responsable del 18% de las paralizaciones de obra en el segmento (Tarraga Durand & Miranda Mitma, 2025).                             |
| Why             | ¿Por qué sucede?             | Debido a la inexistencia de sistemas de auditoría centralizados y la dependencia de herramientas informales (WhatsApp/Excel) que no aseguran el cumplimiento de calidad y tiempo (Ruiz Escajadillo, 2024).                                              |
| How             | ¿Cómo se manifiesta?         | Mediante procesos manuales sin validación presupuestal inmediata, lo que genera duplicidad de pedidos y obliga a compras de emergencia que representan el 12% del gasto logístico (Tarraga Durand & Miranda Mitma, 2025).                               |
| How Much        | ¿Cuánto impacto tiene?       | Genera un sobrecosto logístico del 21,1% sobre las ventas (5,1 puntos sobre la media nacional) y una erosión de hasta el 15% del presupuesto de insumos por errores de gestión (ComexPerú, 2023; Rodríguez Vargas, 2019).                               |

---

### 1.2.2. Lean UX Process

#### 1.2.2.1. Lean UX Problem Statements
Las micro y pequeñas empresas (MYPES) constructoras de Lima Metropolitana gestionan los requerimientos de materiales mediante herramientas informales como WhatsApp o registros manuales en papel. Esta fragmentación de la información dificulta la trazabilidad de los pedidos, impide la comparación técnica de cotizaciones y retrasa la aprobación oportuna de compras por parte de la gerencia.

Como consecuencia de esta gestión operativa deficiente, las organizaciones enfrentan sobrecostos por compras de emergencia y retrasos críticos en la ejecución de obra que erosionan su rentabilidad neta. Como equipo, nos comprometemos a resolver este desafío mediante una colaboración estrecha con el personal de campo y administrativo para diseñar un flujo de abastecimiento trazable y auditable.

Ante esto nos surge la siguiente pregunta:
¿Cómo podría una plataforma SaaS de bajo costo centralizar las requisiciones y aprobaciones para reducir el lead time de compra y mejorar el control operativo?

1. Domain: Gestión de adquisiciones y abastecimiento logístico para el sector construcción (MYPES).

2. Customer Segments: Gerentes Generales (aprobadores), Ingenieros Residentes (solicitantes) y Jefes de Logística (compradores).

3. Pain Points: Pérdida de trazabilidad de requerimientos, sobrecostos por emergencia y falta de comparación de cotizaciones.

4. Gap: Inexistencia de un software SaaS económico diseñado para la pequeña constructora que cubra el espacio entre el Excel manual y ERPs de alta complejidad.

5. Visión/Strategy: Digitalizar el 100% de los requerimientos de materiales mediante una plataforma en la nube que permita el control presupuestal en tiempo real.

6. Initial Segment: Pequeñas empresas constructoras de edificaciones residenciales ubicadas en Lima Metropolitana.

#### 1.2.2.2. Lean UX Assumptions
**Business Assumptions:**
1. Se considera que los clientes requieren formalizar los pedidos de materiales desde obra para reducir errores y el desorden sistemático en el abastecimiento (Rodríguez Vargas, 2019).

2. Se plantea que esta necesidad puede resolverse mediante una plataforma web SaaS accesible desde dispositivos móviles, capaz de automatizar el flujo de cotizaciones y aprobaciones jerárquicas.

3. Se identifica como segmento inicial a micro y pequeñas empresas constructoras con sede en Lima Metropolitana y facturación anual menor a 1.700 UIT (INEI, 2024).

4. Se asume que el principal valor percibido por el cliente será la visualización comparada de cotizaciones en tiempo real antes de autorizar un gasto, con el fin de respaldar decisiones más rentables.

5. Se prevé que el cliente también obtendrá beneficios adicionales, como un historial digital de proveedores, reportes de gasto acumulado y mayor transparencia para auditorías.

6. Se proyecta que la adquisición de clientes se realizará mediante estrategias de marketing digital B2B segmentado y alianzas estratégicas con gremios del sector, como CAPECO.

7. Se estima que el modelo de ingresos más adecuado será una suscripción mensual basada en el volumen de obras o proyectos activos gestionados por la constructora.

8. Se considera que la competencia principal estará conformada por el uso tradicional de WhatsApp y Excel, así como por sistemas ERP complejos e inaccesibles para el presupuesto MYPE, como SAP u Odoo.

9. Se sostiene que la propuesta podrá diferenciarse mediante una arquitectura de información diseñada específicamente para el flujo campo-oficina, reduciendo la complejidad innecesaria.

10. Se presume que el principal riesgo del producto es que el personal de campo mantenga el uso de canales informales si el flujo digital no reduce de forma clara el tiempo de coordinación frente a los canales actuales.

11. Se plantea que este riesgo puede mitigarse mediante un sistema de requerimientos en “3 clics”, diseñado para smartphones y más ágil que redactar un mensaje de texto.

12. Se asume que, si se comprueba que las constructoras no están dispuestas a pagar por control digital pese a las pérdidas actuales, el proyecto no será viable.

**Business Outcome Assumptions**
1. Reducir en un 40% el tiempo administrativo desde la creación de la requisición hasta la emisión de la orden de compra.

2. Lograr que el 100% de las compras institucionales cuenten con un registro digital auditable y pasen por un flujo de aprobación con sustento de cotización.

3. Disminuir las desviaciones presupuestarias por compras de emergencia no planificadas en un 15% (Tarraga Durand & Miranda Mitma, 2025).

4. Incrementar la visibilidad del margen de utilidad neta por proyecto al contar con costos de materiales centralizados y actualizados diariamente.

**User Assumptions**
1. Los jefes y gerentes requieren una herramienta que les permita aprobar compras críticas sin estar físicamente en la oficina.

2. Los jefes de proyecto valoran la posibilidad de delegar el proceso de cotización al área de compras, manteniendo siempre la decisión final sobre la elección del proveedor.

3. La gerencia espera que el sistema genere automáticamente cuadros comparativos de precios para evitar el análisis manual de múltiples correos electrónicos o archivos PDF.

4. El segmento objetivo necesita una solución que alerte de forma proactiva cuando un pedido de materiales supere el presupuesto asignado para una partida específica de la obra.


**User Outcome Assumptions**
1. Los jefes de proyecto experimentarán un aumento en la precisión de sus auditorías financieras al contar con un historial inalterable de quién solicitó, quién cotizó y quién aprobó cada insumo.

2. Los gerentes se sentirán más seguros respecto al uso del capital de la empresa al visualizar sistemáticamente al menos tres opciones de cotización antes de autorizar cualquier desembolso significativo.

3. Los responsables del negocio experimentarán una reducción del estrés operativo al disminuir las llamadas de emergencia por desabastecimiento, permitiéndoles enfocarse en la planificación estratégica y comercial.

4. Los jefes de proyecto confiarán más en la veracidad de los datos de inventario y pedidos pendientes, lo que facilitará una coordinación más fluida con los clientes finales respecto a los plazos de entrega de los inmuebles.

5. El segmento percibirá una optimización del flujo de caja operativo al evitar compras duplicadas o adquisiciones con sobreprecio derivadas de la falta de comparación inmediata.

#### 1.2.2.3. Lean UX Hypothesis Statements
**Hypothesis 1** Creemos que al centralizar las solicitudes de materiales en una plataforma web accesible desde la obra, reduciremos drásticamente los tiempos de espera. Lo sabremos cuando el tiempo promedio entre la creación de una solicitud y su aprobación por logística baje de 48 horas a menos de 8 horas.

**Hypothesis 2** Creemos que al implementar un tablero de control (Dashboard) para los Jefes de Proyectos, eliminaremos la falta de visibilidad del presupuesto. Lo sabremos cuando las desviaciones de costos por compras de emergencia se reduzcan en un 15% durante el primer trimestre de uso.

**Hypothesis 3** Creemos que al automatizar los flujos de comunicación entre obra y logística, optimizaremos el proceso de abastecimiento. Lo sabremos cuando el número de llamadas o mensajes para consultar el estado de un pedido disminuya en un 50%.

**Hypothesis 4** Creemos que al digitalizar el historial de proveedores y cotizaciones, facilitaremos la toma de decisiones gerenciales. Lo sabremos cuando el tiempo dedicado a la comparación manual de cotizaciones se reduzca de 4 horas semanales a solo 15 minutos.

**Hypothesis 5** Creemos que digitalizar los requerimientos técnicos para los ingenieros de obra logrará una reducción del 50% en errores de pedido. Sabremos que es cierto cuando veamos que el 90% de los requerimientos registrados no requieren correcciones técnicas posteriores.

#### 1.2.2.4. Lean UX Canvas

<table>
  <tr>
    <td valign="top">
      <strong>Business problem</strong>
      <br><br>
      Las micro y pequeñas empresas (MYPES) constructoras de Lima Metropolitana gestionan los requerimientos de materiales mediante herramientas informales como WhatsApp o registros manuales en papel. Esta fragmentación dificulta la trazabilidad de los pedidos, limita la comparación técnica de cotizaciones y retrasa la aprobación de compras.
      <br><br>
      Como consecuencia, se generan sobrecostos por compras de emergencia, duplicidad de pedidos y retrasos en la continuidad de obra que afectan directamente la rentabilidad del proyecto.
    </td>
    <td rowspan="2" valign="top">
      <strong>Solution ideas</strong>
      <br><br>
      - Plataforma web SaaS accesible desde dispositivos móviles orientada al entorno de obra
      <br><br>
      - Registro digital de requerimientos con flujo de aprobación jerárquica
      <br><br>
      - Módulo de comparación de cotizaciones en tiempo real
      <br><br>
      - Historial centralizado de proveedores, pedidos y aprobaciones
      <br><br>
      - Alertas de control presupuestal y seguimiento de estados
    </td>
    <td valign="top">
      <strong>Business Outcomes</strong>
      <br><br>
      - Reducir en un 40% el tiempo administrativo desde la requisición hasta la orden de compra
      <br><br>
      - Lograr que el 100% de las compras cuenten con registro digital auditable
      <br><br>
      - Disminuir en un 15% los sobrecostos por compras no planificadas
      <br><br>
      - Mejorar la visibilidad del gasto y margen de utilidad por proyecto
    </td>
  </tr>
  <tr>
    <td valign="top">
      <strong>Users and customers</strong>
      <br><br>
      - Ingenieros residentes de obra
      <br>
      - Jefes de logística
      <br>
      - Jefes de proyecto
      <br>
      - Gerentes generales
      <br>
      - MYPES constructoras de edificaciones
    </td>
    <td valign="top">
      <strong>User benefits</strong>
      <br><br>
      - Aprobación remota de materiales sin dependencia de la oficina
      <br><br>
      - Visibilidad del estado de cada requerimiento en tiempo real
      <br><br>
      - Reducción del tiempo dedicado a comparar cotizaciones
      <br><br>
      - Mejor coordinación entre obra y área administrativa
      <br><br>
      - Mayor control sobre el presupuesto antes de ejecutar compras
    </td>
  </tr>
  <tr>
    <td valign="top">
      <strong>Hypotheses</strong>
      <br><br>
      - Si se centralizan las solicitudes de materiales en una plataforma accesible desde obra, el tiempo de aprobación se reducirá de 48 horas a menos de 8 horas.
      <br><br>
      - Si se implementa un panel de control para jefes de proyecto, las desviaciones por compras de emergencia se reducirán en un 15%.
      <br><br>
      - Si se automatizan los flujos de comunicación entre obra y logística, disminuirán en un 50% las consultas manuales (llamadas y mensajes).
      <br><br>
      - Si se digitaliza el historial de proveedores y cotizaciones, el tiempo de comparación manual se reducirá de 4 horas semanales a 15 minutos.
      <br><br>
      - Si los requerimientos técnicos se registran digitalmente, los errores de pedido se reducirán en un 50%.
    </td>
    <td valign="top">
      <strong>What’s the most important thing we need to learn first?</strong>
      <br><br>
      Si las MYPES constructoras están dispuestas a reemplazar herramientas informales (WhatsApp, llamadas) por una plataforma digital y perciben suficiente valor como para adoptarla en su flujo de trabajo.
    </td>
    <td valign="top">
      <strong>What’s the least amount of work we need to do to learn the next most important thing?</strong>
      <br><br>
      Realizar entrevistas con ingenieros residentes, jefes de logística y gerentes, y validar mediante un prototipo de baja fidelidad el flujo de requisición, aprobación y comparación de cotizaciones, evaluando facilidad de uso, rapidez y disposición de adopción.
    </td>
  </tr>
</table>

---

## 1.3. Segmentos Objetivos
El segmento objetivo de Buildline se centra exclusivamente en los perfiles de liderazgo y toma de decisiones dentro del entorno de la construcción MYPE peruana. Este grupo es el responsable final de la viabilidad financiera de los proyectos y la sostenibilidad operativa de la empresa.

### 1.3.1. Jefes de Proyectos y Gerentes Generales

| Dimensión               | Detalle del perfil                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Perfil Demográfico**  | Hombres y mujeres de entre 25 y 55 años. Cuentan con educación superior universitaria, siendo mayoritariamente Ingenieros Civiles o Arquitectos titulados y colegiados. Muchos operan bajo la modalidad de Persona Natural con Negocio, que representa el 73,5% de las unidades económicas del sector (INEI, 2024).                                                                                      |
| **Perfil Geográfico**   | Ubicados principalmente en zonas urbanas de alta densidad constructiva. El 45,7% de las empresas se concentra en Lima Metropolitana, seguida de regiones estratégicas como Arequipa (5,3%), La Libertad (5,2%) y Piura (4,3%) (INEI, 2024).                                                                                                                                                              |
| **Perfil Psicográfico** | Profesionales con un estilo de vida de alta presión y movilidad constante entre oficina y campo. Valoran la eficiencia y la honestidad operativa. Presentan una resistencia al cambio cultural del 48% (EY Perú, 2024), por lo que buscan herramientas que no compliquen sus procesos actuales. Su principal interés es la optimización del margen de utilidad y la transparencia de sus flujos de caja. |
| **Puntos de Dolor**     | Erosión de la rentabilidad debido a un costo logístico del 21,1% (ComexPerú, 2023). Enfrentan una falta de trazabilidad en el 74,1% de sus compras y sufren paralizaciones de obra en el 18% de los casos por desabastecimiento o errores técnicos en el suministro (Rodríguez Vargas, 2019; Tarraga Durand & Miranda Mitma, 2025).                                                                      |
| **Uso de Tecnología**   | Usuarios intensivos de dispositivos móviles; el 91,3% de la población ocupada en este rango de edad utiliza smartphones diariamente para la gestión de sus actividades (INEI, 2025). Dependen actualmente de herramientas no especializadas como WhatsApp y Excel para el control operativo básico.                                                                                                      |
