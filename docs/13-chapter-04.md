# Capítulo IV: Product Design

En este capítulo se detallan las decisiones de diseño de producto para la plataforma **Buildline** y su respectiva Landing Page. Se establecen las guías de estilo visuales, la arquitectura de la información y los criterios que aseguran una experiencia de usuario (UX) intuitiva y profesional, alineada a las exigencias del sector construcción y la gestión logística de obras.

## 4.1. Style Guidelines

### 4.1.1. General Style Guidelines

El diseño visual de la plataforma **Buildline** se rige por una estética robusta, tecnológica y de alta eficiencia operativa, reflejando el compromiso con la eliminación de la informalidad y la integridad de la trazabilidad en la cadena de suministro. El objetivo es proyectar un entorno de control y profesionalismo que minimice la carga cognitiva tanto del residente en campo como del jefe de logística en la oficina.

En este capítulo, detallaremos cada uno de los elementos visuales y de estilo que guían el desarrollo de la aplicación Buildline, siempre siguiendo los principios de Diseño de Experiencia de Usuario (UX) e Interfaz de Usuario (UI) para garantizar la máxima usabilidad bajo condiciones de obra.

**Branding**

El logotipo principal de Buildline está compuesto por un isotipo que integra múltiples elementos semánticos de nuestro dominio técnico: 
* **La Línea Continua:** Una 'B' estilizada formada por un trazo ininterrumpido que simboliza un flujo logístico eficiente y sin fin, respondiendo a la necesidad de trazabilidad absoluta.
* **El Edificio Modular:** Integrado en la parte superior del bucle, evoca el progreso de la obra y la finalización exitosa del proyecto gracias a un abastecimiento oportuno.
* **Nodos de Conexión:** Los pequeños círculos representan la integración digital de requerimientos, cotizaciones y órdenes de compra, eliminando el caos de aplicaciones informales como WhatsApp.

<br>
<p align="center">
  <img src="../docs/assets/chapter-04/buildline_logo.jpg" alt="Buildline Logo" width="350px" height="auto"/>
</p>
<br>

**Typography**

La tipografía empleada en Buildline será **Montserrat**, con sus variantes Regular, Medium, SemiBold y Bold. La elección de Montserrat se basa en su estética geométrica y sólida que evoca la resistencia de la construcción, equilibrada con una legibilidad perfecta para revisar presupuestos y listas de materiales en pantallas móviles bajo el sol o en oficinas. Además, su disponibilidad a través de Google Fonts asegura una carga eficiente.

La jerarquía tipográfica se establece de la siguiente manera para garantizar claridad y ritmo visual:
* **Títulos principales (H1/Sección heading):** 5rem (aprox. 50px) en escritorio, 4.5rem (aprox. 45px) en móvil.
* **Subtítulos (H2/Sub-headings):** 3rem (aprox. 30px) en escritorio.
* **Títulos de componentes (H3/H4):** 2rem (aprox. 20px) a 2.5rem (aprox. 25px).
* **Cuerpo del texto (p):** 1.6rem (aprox. 16px) con un interlineado de 1.6.
* **Botones y etiquetas (span):** 1.4rem (aprox. 14px) a 1.8rem (aprox. 18px).

<p align="center">
  <img src="../docs/assets/chapter-04/Style_guide.png" alt=" Typography Guide" width="500px" height="auto"/>
</p>

Esta distribución garantiza un contraste óptimo entre el texto y el fondo, superando un ratio mínimo de 4.5:1 según las WCAG 2.1 AA para una accesibilidad superior en entornos de campo.

**Colors**

Nuestra paleta de colores ha sido cuidadosamente seleccionada para evocar sensaciones de control corporativo, acción operativa e innovación. Se ha distribuido en tres categorías principales:

* **Paleta principal:** Colores que definen la identidad de Buildline y se usan en elementos clave.
    * **Primario (Deep Navy Blue):** Transmite autoridad, formalidad profesional y seguridad. Utilizado en menús de oficina y presupuestos.
    * **Secundario (Vibrant Orange):** Representa la energía de la obra en campo y la velocidad logística. Utilizado para llamados a la acción (CTAs) y botones urgentes.
    * **Terciario (Tech Cyan):** Evoca la conectividad y la nube. Utilizado para marcadores de estado y trazabilidad.
    * **Fondo Claro:** Proporciona un entorno visual limpio para tablas de cotizaciones.
    * **Fondo Blanco:** Fondos de tarjetas de requerimientos y paneles de control.
* **Paleta de Soporte:** Colores complementarios que añaden profundidad y contraste.
    * **Gris Neutro:** Para bordes sutiles, líneas divisorias y separadores de listas de materiales.
* **Colores Funcionales:** Reservados para comunicar estados críticos al usuario.
    * **Éxito:** Verde para órdenes de compra aprobadas y materiales entregados.
    * **Error:** Rojo para presupuestos excedidos o alertas de retraso.
    * **Advertencia:** Amarillo para quiebres de stock o requerimientos pendientes.

<p align="center">
  <img src="../docs/assets/chapter-04/Color_guidelines.png" alt=Color Palette" width="800px" height="auto"/>
</p>

Esta combinación cromática refleja los valores de nuestra marca y busca transmitir al público (constructoras y gerentes de proyecto) una imagen de rigor, velocidad y control financiero.

**Spacing**

El espaciado en Buildline sigue un sistema modular para garantizar un ritmo visual armonioso y una jerarquía clara. La consistencia en el espaciado ayuda a reducir el estrés administrativo del usuario frente a largas listas de inventario.
* **Espaciado Básico:** Usamos un espaciado base en el sistema de grid, multiplicado para crear espacios mayores.
* **Margen Interno (Padding) Generoso:** Las secciones principales utilizan un padding vertical de 5rem (50px) para crear pausas visuales. Los contenedores de requerimientos usan padding menor (30px - 40px) para agrupar datos lógicamente.
* **Espacio entre Elementos:** El espaciado entre tarjetas de obra o cotizaciones varía entre 3rem y 5rem, manteniendo una densidad de información adecuada sin abrumar visualmente al jefe de logística.
* **Line Height del Texto:** Interlineado configurado en 1.6, facilitando la lectura de especificaciones técnicas de materiales.

**Tono de Comunicación**

La voz y el tono de Buildline están diseñados para ser tan resolutivos y estructurados como nuestra plataforma. Nuestro objetivo es conectar tanto con Residentes de Obra (campo) como con Gerentes Generales (gabinete).
* **Tono: Formal pero orientado a la acción.** Buscamos proyectar autoridad en el control de costos, manteniendo el dinamismo que exige el trabajo en obra.
* **Actitud: Resolutiva y ágil.** El 90% de nuestra comunicación se orienta a la eficiencia ("Cero retrasos", "Aprobaciones en un clic"), mientras que el 10% es persuasiva para incentivar la adopción del sistema.
* **Lenguaje: Técnico y directo.** Hablamos el idioma de la construcción (ej. Órdenes de Compra, Valorizaciones, Requerimientos, Cuadrillas, RFI). Nos enfocamos en la rentabilidad y la reducción de sobrecostos.
* **Voz: Experta y moderna.** Posicionamos a Buildline como el fin de la informalidad y la llegada de la Industria 4.0 a la construcción peruana.

### 4.1.2. Web Style Guidelines

Las directrices de estilo web de **Buildline** se centran en la velocidad operativa, la inmutabilidad del historial de compras y la facilidad de uso. Nuestro objetivo es crear una experiencia visual que digitalice el flujo de abastecimiento con un diseño limpio e intuitivo, especialmente para usuarios en campo con baja conectividad.

**1) Layout**
* **Sistema de Grid:** Utilizamos un diseño de cuadrícula flexible para garantizar que Buildline se adapte perfectamente. Esto permite que las tablas de cotizaciones complejas se condensen fluidamente en pantallas pequeñas.
* **Headers y Footers:** El encabezado es fijo, proporcionando acceso a la navegación y botones de acceso. El pie de página centraliza enlaces, contacto y soporte técnico.
* **Cards:** Las tarjetas estructuran información crítica, como los requerimientos de Obra pendientes. Cuentan con bordes redondeados y sombras suaves para facilitar la rápida lectura de prioridades.

**2) Responsive Design**
* **Desktop:** Optimizado para la oficina de logística y gerencia. Menús laterales completos y grillas de datos expansivas para comparar cotizaciones en pantallas grandes.
* **Tablet:** Interfaz adaptada para supervisores de obra, con botones táctiles ampliados para el uso en movimiento.
* **Mobile (Mobile-First para Campo):** La experiencia móvil es ultra-ligera (Low-Data). Menú de hamburguesa y botones masivos para generar requerimientos fácilmente incluso con una sola mano y guantes de obra.

**3) Interaction Design**
* **Botones:** Llamativos utilizando el "Vibrant Orange" para acciones principales (Aprobar, Enviar Requerimiento). Efectos lineales al pasar el cursor confirman la interactividad.
* **Formularios:** Extremadamente simplificados. Los campos de solicitud de material utilizan autocompletado predictivo para evitar que el operario de campo escriba largos textos.

**4) Images and Icons**
* **Imágenes:** Fotografías de alta calidad que evocan grandes infraestructuras, ingenieros utilizando tablets en campo y almacenes ordenados.
* **Íconos:** Estilo lineal y minimalista. Representan maquinaria, cascos, portapapeles y nodos de red para ofrecer una navegación visual intuitiva sin necesidad de leer mucho texto.

**5) Repositorio Central**
* **Organización:** Estructura lógica modular (`public/assets/images`, `public/assets/styles/style.css`, `public/assets/scripts/main.js`).
* **Versionado:** Uso estricto de Git para el control de versiones del equipo de desarrollo, garantizando despliegues seguros de la plataforma.

## 4.2. Information Architecture

La arquitectura de la información de **Buildline** está diseñada para una navegación intuitiva orientada a roles, permitiendo que Gerentes, Logísticos y Residentes encuentren exactamente lo que necesitan sin fricciones.

### 4.2.1. Organization Systems

* **Jerarquía de Contenidos:** La información va del impacto macro al detalle operativo. La Landing Page inicia con el dolor principal (retrasos) y la promesa de valor (trazabilidad).
* **Secciones Principales de la Landing Page:**
    * **Hero:** El fin del caos logístico en la construcción.
    * **What We Offer:** Visión general del flujo Requerimiento-Aprobación-Entrega.
    * **Features:** Aprobaciones móviles, control presupuestal, tracking de proveedores.
    * **Benefits:** Reducción de sobrecostos de emergencia (hasta 18%) y prevención de paralizaciones.
    * **About Us:** Nuestro compromiso con la formalización del sector.
    * **Plans:** Suscripciones adaptadas a constructoras MYPES y grandes corporaciones.
    * **Testimonials:** Respaldo de Jefes de Proyecto.
* **Agrupación de Contenidos:** Uso de pestañas y acordeones interactivos para clasificar funcionalidades técnicas sin saturar la pantalla.

### 4.2.2. Labeling Systems

* **Nomenclatura:** Lenguaje 100% de la industria ("Crear Requerimiento", "Comparar Cotizaciones", "Emitir OC"). Botones claros como "Request Demo".
* **Consistencia:** Unificación de términos en todo el SaaS (siempre se usa "Requerimiento", nunca se mezcla con "Pedido" u "Orden").
* **Lenguaje Adaptativo:** Accesible para operarios de campo sin jerga de software, pero con el rigor financiero que exige una gerencia.

### 4.2.3. Searching Systems

* **Barra de Búsqueda:** Dentro del SaaS, es la herramienta principal de la oficina. Ubicada en la parte superior para buscar por *Nombre de Proyecto*, *ID de Orden de Compra* o *Proveedor*.
* **Filtros y Facetas:** Filtros críticos por Estado (Pendiente, Aprobado, Rechazado, En Tránsito), Fechas y Rango de Costos.
* **Historial de Búsqueda:** Registro de materiales más solicitados para agilizar futuras cotizaciones.
* **Resultados Relevantes:** Priorización de requerimientos con etiqueta de "Urgente" o aquellos que superan el presupuesto base.

### 4.2.4. Navigation Systems

* **Navegación Global:** Barra de navegación superior fija en la Landing Page (`Home`, `Soluciones`, `Beneficios`, `Planes`).
* **Navegación Contextual:** Botones de llamado a la acción (CTAs naranjas) que guían al usuario fluidamente desde la lectura de un beneficio hasta la solicitud de una cuenta.

### 4.2.5. Navigation Systems
[pending content]
## 4.3. Landing Page UI Design
### 4.3.1. Landing Page Wireframe
[pending content]
### 4.3.2. Landing Page Mock-up
[pending content]
## 4.4. Web Applications UX/UI Design
### 4.4.1. Web Applications Wireframes
[pending content]
### 4.4.2. Web Applications Wireflow Diagrams
[pending content]
### 4.4.3. Web Applications Mock-ups
[pending content]
### 4.4.4. Web Applications User Flow Diagrams
[pending content]
## 4.5. Web Applications Prototyping
[pending content]
## 4.6. Domain-Driven Software Architecture
### 4.6.1. Design-Level EventStorming
[pending content]
### 4.6.2. Software Architecture Context Diagram
[pending content]
### 4.6.3. Software Architecture Container Diagrams
[pending content]
### 4.6.4. Software Architecture Components Diagrams
[pending content]
## 4.7. Software Object-Oriented Design
### 4.7.1. Class Diagrams
[pending content]
## 4.8. Database Design
### 4.8.1. Database Diagrams
[pending content]