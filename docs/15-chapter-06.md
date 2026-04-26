# Capítulo VI: Conclusions
## 6.1. Conclusiones y recomendaciones
<p>
  Al finalizar el primer ciclo de investigación, diseño e implementación de la presencia digital de la solución <strong>Buildline</strong>, el equipo RQLS ha llegado a una serie de conclusiones clave, contrastando los resultados obtenidos con los planteamientos iniciales definidos bajo el enfoque Lean UX y el desarrollo ágil basado en Sprints.
</p> 

<p><strong>1. Validación de Problem Statements y Supuestos (Assumptions):</strong></p> 
<p>
  Inicialmente, se planteó como <em>Problem Statement</em> que las MYPES constructoras enfrentan un sobrecosto logístico estructural del 21.1% debido a procesos de abastecimiento informales (uso de WhatsApp), falta de trazabilidad entre obra y oficina, y la nula visibilidad del gasto real frente al presupuesto base (APU). A partir del Needfinding y la validación del modelo de negocio, se confirmó que existe una urgencia real por soluciones digitales que democraticen el control logístico sin requerir implementaciones de ERPs costosos.
</p> 
<p>
  Asimismo, se validó el supuesto de que los Jefes de Proyecto (segmento comprador) valoran altamente la capacidad de bloquear compras no planificadas. Sin embargo, se identificó que el éxito de la plataforma depende en gran medida de la adopción de la herramienta por parte del Ingeniero Residente en campo, lo que implica que el diseño de interfaces debe priorizar la rapidez y facilidad de uso.
</p> 

<p><strong>2. Contrastación de Hipótesis (Hypothesis Statements):</strong></p> 
<ul> 
  <li> 
    <strong>Hipótesis de Valor para Gerentes y Jefes de Proyecto:</strong> Se planteó que "Si proporcionamos paneles de control presupuestal y aprobaciones jerárquicas, los gerentes dejarán de aprobar compras 'a ciegas' y protegerán la rentabilidad". Los resultados obtenidos en la conceptualización validan esta hipótesis, siendo el control del APU el principal gatillo de interés comercial.
  </li> 
  <li> 
    <strong>Hipótesis de Valor para Residentes y Logística:</strong> Se asumió que "La digitalización de los requerimientos y la validación automatizada de recepciones (Way Match) eliminarán los cuellos de botella". Esta hipótesis se mantiene validada a nivel conceptual, destacando la necesidad de adjuntar evidencia fotográfica en el flujo de abastecimiento.
  </li> 
</ul> 

<p><strong>3. Cumplimiento de Criterios de Éxito:</strong></p> 
<p>
  Durante el Sprint 1, el desarrollo de software se limitó estrictamente a la capa de presentación estática. Se logró implementar y desplegar exitosamente la Landing Page informativa de Buildline mediante GitHub Pages, cumpliendo con los criterios de aceptación definidos: navegación responsiva, presentación clara de la propuesta de valor, visualización de planes y perfiles del equipo.
</p> 
<p>
  Al tratarse de un primer incremento enfocado exclusivamente en la web pública de marketing y la documentación arquitectónica (Capítulos I al IV), aún no se han validado métricas operativas del sistema central (como la reducción de tiempos de cotización), las cuales serán evaluadas una vez se inicie la codificación de la plataforma.
</p> 

<p><strong>Recomendaciones (Roadmap):</strong></p> 
<p>
  Considerando que actualmente solo se cuenta con la Landing Page estática, se recomiendan las siguientes líneas de acción técnicas para los próximos Sprints orientadas a construir el prototipo funcional:
</p> 
<ul> 
  <li> 
    <strong>Desarrollo del Backend API:</strong> Iniciar la codificación de los Web Services utilizando <strong>.NET 8 (C#)</strong> para gestionar la lógica de negocio fundamental: creación de requerimientos, control del presupuesto APU y validación de órdenes de compra.
  </li> 
  <li> 
    <strong>Desarrollo del Frontend (SPA):</strong> Construir la aplicación web interactiva utilizando <strong>Vue.js</strong> para consumir la API, desarrollando inicialmente las vistas del Ingeniero Residente (creación de pedidos) y del Logístico (cuadro de cotizaciones).
  </li> 
  <li> 
    <strong>Modelado de la Base de Datos:</strong> Implementar localmente la base de datos relacional (MySQL o SQL Server) diseñada en el diagrama de contenedores, asegurando la integridad de las tablas de usuarios, proyectos, APUs y materiales.
  </li> 
  <li> 
    <strong>Integración de Entornos Locales:</strong> Establecer una comunicación fluida entre el frontend en Vue.js y el backend en .NET en los entornos de desarrollo locales del equipo, realizando pruebas de integración (API Testing) antes de evaluar cualquier futuro despliegue en servidores.
  </li> 
</ul>
## 6.2. Video About-the-Team
[pending content]
