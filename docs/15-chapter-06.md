# Capítulo VI: Conclusions
## 6.1. Conclusiones y recomendaciones
<p>
  Al finalizar el primer ciclo de investigación, diseño e implementación de la presencia digital de la solución <strong>Buildline</strong>, el equipo RQLS ha llegado a una serie de conclusiones clave, contrastando los resultados obtenidos con los planteamientos iniciales definidos bajo el enfoque Lean UX y el desarrollo ágil basado en Sprints.
</p> 

<p><strong>1. Validación de Problem Statements y Supuestos (Assumptions):</strong></p> 
<p>
  Inicialmente, se planteó como <em>Problem Statement</em> que las MYPES constructoras enfrentan un sobrecosto logístico estructural del 21.1% debido a procesos de abastecimiento informales (uso de WhatsApp), falta de trazabilidad entre obra y oficina, y la nula visibilidad del gasto real frente al presupuesto base (APU). A partir del Needfinding y la validación del modelo de negocio, se confirmó que existe una urgencia real por soluciones digitales que democraticen el control logístico sin requerir implementaciones de ERPs costosos y complejos.
</p> 
<p>
  Asimismo, se validó el supuesto de que los Jefes de Proyecto (segmento comprador) valoran altamente la capacidad de bloquear compras no planificadas. Sin embargo, se identificó que el éxito de la plataforma no depende solo de la gerencia, sino de la adopción de la herramienta por parte del Ingeniero Residente en campo, lo que implica que la solución (Field App) debe priorizar la rapidez, la usabilidad móvil y funcionar en entornos de conectividad limitada.
</p> 

<p><strong>2. Contrastación de Hipótesis (Hypothesis Statements):</strong></p> 
<ul> 
  <li> 
    <strong>Hipótesis de Valor para Gerentes y Jefes de Proyecto:</strong> Se planteó que "Si proporcionamos dashboards de control presupuestal en tiempo real y aprobaciones jerárquicas, los gerentes dejarán de aprobar compras 'a ciegas' y protegerán la rentabilidad". Los resultados obtenidos en la conceptualización y diseño de la propuesta de valor validan esta hipótesis, siendo el control del APU el principal gatillo de interés comercial.
  </li> 
  <li> 
    <strong>Hipótesis de Valor para Residentes y Logística:</strong> Se asumió que "La digitalización de los requerimientos y la validación automatizada de recepciones (Way Match) eliminarán los cuellos de botella y pérdidas de material". Esta hipótesis se mantiene validada a nivel conceptual, destacando la necesidad de adjuntar evidencia fotográfica formal en cada etapa del flujo de abastecimiento.
  </li> 
</ul> 

<p><strong>3. Cumplimiento de Criterios de Éxito:</strong></p> 
<p>
  Durante el Sprint 1, se logró implementar y desplegar exitosamente la Landing Page informativa de Buildline mediante GitHub Pages, cumpliendo con los criterios de aceptación definidos: navegación responsiva, presentación clara de la propuesta de valor (mitigación del 21.1% de sobrecosto), visualización de los planes de suscripción MYPE y formulario de contacto.
</p> 
<p>
  No obstante, al tratarse de un primer incremento enfocado exclusivamente en la presencia digital y la documentación arquitectónica (Capítulos I al IV), aún no se han validado métricas operativas críticas del software SaaS, tales como la reducción efectiva de tiempos de cotización o la prevención de desviaciones de presupuesto, las cuales serán evaluadas en los siguientes sprints con la implementación del núcleo transaccional.
</p> 

<p><strong>Recomendaciones (Roadmap):</strong></p> 
<p>
  En base a los hallazgos obtenidos y las limitaciones actuales del alcance del Sprint 1, se proponen las siguientes líneas de acción para las futuras etapas de desarrollo de Buildline:
</p> 
<ul> 
  <li> 
    <strong>Implementación del Backend Transaccional:</strong> Priorizar el desarrollo de los Web Services con <strong>.NET 8 (C#)</strong> para la gestión del flujo de compras (Requisición -> Cotización -> Orden de Compra), ya que representa el motor lógico que cruza los gastos con la línea base del APU.
  </li> 
  <li> 
    <strong>Desarrollo de la SPA y Field App:</strong> Construir la aplicación frontend completa utilizando el framework <strong>Vue.js</strong>, asegurando interfaces rápidas para los paneles de oficina (Logística/Gerencia) y vistas móviles optimizadas para la creación de pedidos en el frente de obra (Residente).
  </li> 
  <li> 
    <strong>Integración de la Validación Way Match:</strong> Incorporar de forma temprana el cruce de datos entre las Guías de Remisión físicas y las Órdenes de Compra del sistema, para garantizar que el inventario de la constructora sea exacto.
  </li> 
  <li> 
    <strong>Integración de Servicios Externos:</strong> Preparar la arquitectura para consumir la API de la SUNAT (validación de facturas y estado de proveedores) y la integración con pasarelas de pago para el cobro del modelo de suscripción SaaS.
  </li> 
  <li> 
    <strong>Despliegue en la Nube:</strong> Configurar la infraestructura en <strong>Microsoft Azure</strong> mediante App Services y bases de datos administradas (MySQL/SQL Server), garantizando alta disponibilidad, seguridad y escalabilidad para las constructoras afiliadas.
  </li> 
</ul>
## 6.2. Video About-the-Team
[pending content]
