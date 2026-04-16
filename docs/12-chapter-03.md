# Capítulo III: Requirements Specification
## 3.1. User Stories
| US ID  | Titulo | Descripcion | Criterio de Aceptacion |
|--------|--------|-------------|------------------------|
| US 001 | Registrar requerimiento de material | Como ingeniero residente, quiero registrar un requerimiento de materiales desde obra, para iniciar el proceso de abastecimiento de forma estructurada. | Escenario 1: Registro correcto Dado que el usuario completa los campos obligatorios, Cuando envía el requerimiento, Entonces este se registra correctamente. Escenario 2: Datos incompletos Dado que faltan datos, Cuando intenta enviar, Entonces se muestra mensaje de error. |
| US 002 | Adjuntar evidencia al requerimiento | Como usuario de obra, quiero adjuntar fotos o documentos al requerimiento, para brindar mayor claridad sobre el material solicitado. | Escenario 1: Archivo válido Dado que adjunta imagen o PDF, Cuando envía, Entonces se guarda correctamente. Escenario 2: Archivo inválido Dado que el formato no es permitido, Entonces se muestra error. |
| US 003 | Visualizar lista de requerimientos | Como jefe de logística, quiero ver todos los requerimientos en una lista, para gestionarlos eficientemente. | Escenario 1: Lista con datos Dado que existen requerimientos, Cuando accede, Entonces se muestran ordenados. Escenario 2: Sin datos Entonces se muestra mensaje vacío. |
| US 004 | Filtrar requerimientos | Como usuario, quiero filtrar requerimientos por estado o proyecto, para encontrarlos rápidamente. | Escenario 1: Filtro aplicado Entonces se muestran resultados filtrados. Escenario 2: Sin coincidencias Entonces se muestra mensaje vacío. |
| US 005 | Generar solicitud de cotización | Como logística, quiero generar solicitudes de cotización, para obtener precios de proveedores. | Escenario 1: Generación correcta Entonces se envía solicitud. Escenario 2: Error Entonces se notifica fallo. |
| US 006 | Registrar cotizaciones | Como logística, quiero registrar cotizaciones recibidas, para compararlas. | Escenario 1: Registro válido Entonces se guarda cotización. Escenario 2: Datos incompletos Entonces error. |
| US 007 | Comparar cotizaciones | Como jefe de proyecto, quiero comparar cotizaciones, para elegir la mejor opción. | Escenario 1: Comparación Entonces se muestran precios. Escenario 2: Sin cotizaciones Entonces aviso. |
| US 008 | Aprobar compra | Como gerente, quiero aprobar compras, para autorizar gastos. | Escenario 1: Aprobación Entonces pasa a compra. Escenario 2: Rechazo Entonces se notifica. |
| US 009 | Generar orden de compra | Como logística, quiero generar órdenes de compra, para formalizar pedidos. | Escenario 1: Generación correcta Entonces se crea OC. Escenario 2: Error Entonces alerta. |
| US 010 | Notificar al proveedor | Como sistema, quiero notificar al proveedor, para iniciar entrega. | Escenario 1: Notificación exitosa Entonces proveedor recibe. Escenario 2: Error Entonces reintento. |
| US 011 | Seguimiento de pedidos | Como usuario, quiero ver estado de pedidos, para monitorear avances. | Escenario 1: Estado actualizado Entonces se visualiza progreso. Escenario 2: Sin datos Entonces mensaje. |
| US 012 | Confirmar recepción de materiales | Como almacenero, quiero confirmar recepción, para cerrar pedidos. | Escenario 1: Confirmación Entonces pedido cerrado. Escenario 2: Error Entonces aviso. |
| US 013 | Registrar incidencias | Como usuario, quiero registrar problemas con proveedores, para controlarlos. | Escenario 1: Registro Entonces queda guardado. Escenario 2: Error Entonces mensaje. |
| US 014 | Controlar stock | Como logística, quiero ver stock disponible, para evitar faltantes. | Escenario 1: Stock disponible Entonces se muestra. Escenario 2: Sin stock Entonces alerta. |
| US 015 | Actualizar stock | Como almacén, quiero actualizar inventario, para mantener datos reales. | Escenario 1: Actualización correcta Entonces stock cambia. Escenario 2: Error Entonces alerta. |
| US 016 | Visualizar historial de compras | Como usuario, quiero ver historial, para analizar decisiones. | Escenario 1: Historial visible Entonces lista completa. Escenario 2: Vacío Entonces mensaje. |
| US 017 | Control presupuestal | Como gerente, quiero ver control de costos, para evitar sobrecostos. | Escenario 1: Datos actualizados Entonces dashboard. Escenario 2: Error Entonces aviso. |
| US 018 | Alertas de sobrecosto | Como sistema, quiero alertar sobre sobrecostos, para prevenir desviaciones. | Escenario 1: Exceso Entonces alerta. Escenario 2: Normal Entonces sin alerta. |
| US 019 | Dashboard general | Como usuario, quiero ver indicadores, para tomar decisiones rápidas. | Escenario 1: Dashboard cargado Entonces gráficos visibles. Escenario 2: Sin datos Entonces mensaje. |
| US 020 | Acceso móvil | Como usuario de campo, quiero usar app móvil, para gestionar desde obra. | Escenario 1: Acceso correcto Entonces navegación fluida. Escenario 2: Error Entonces aviso. |
| US 021 | Notificaciones en tiempo real | Como usuario, quiero recibir notificaciones, para reaccionar rápido. | Escenario 1: Evento ocurre Entonces notificación. Escenario 2: Error Entonces no llega. |
| US 022 | Registro de usuarios | Como administrador, quiero registrar usuarios, para dar acceso al sistema. | Escenario 1: Registro válido Entonces usuario creado. Escenario 2: Error Entonces mensaje. |
| US 023 | Inicio de sesión | Como usuario, quiero iniciar sesión, para acceder al sistema. | Escenario 1: Credenciales correctas Entonces acceso. Escenario 2: Incorrectas Entonces error. |
| US 024 | Gestión de roles | Como admin, quiero asignar roles, para controlar accesos. | Escenario 1: Rol asignado Entonces permisos aplican. Escenario 2: Error Entonces aviso. |
| US 025 | Historial de acciones | Como admin, quiero ver logs, para auditoría. | Escenario 1: Logs visibles Entonces historial completo. Escenario 2: Sin logs Entonces vacío. |
| US 026 | Búsqueda global | Como usuario, quiero buscar información, para encontrar datos rápido. | Escenario 1: Coincidencia Entonces resultados. Escenario 2: Sin resultados Entonces mensaje. |
| US 027 | Integración con Excel | Como usuario, quiero exportar datos, para análisis externo. | Escenario 1: Exportación correcta Entonces archivo descargado. Escenario 2: Error Entonces aviso. |
| US 028 | Carga masiva de datos | Como usuario, quiero subir datos en lote, para ahorrar tiempo. | Escenario 1: Archivo válido Entonces carga exitosa. Escenario 2: Error Entonces mensaje. |
| US 029 | Gestión de proveedores | Como logística, quiero registrar proveedores, para tener base de datos. | Escenario 1: Registro Entonces proveedor guardado. Escenario 2: Error Entonces aviso. |
| US 030 | Evaluación de proveedores | Como usuario, quiero calificar proveedores, para mejorar decisiones futuras. | Escenario 1: Evaluación guardada Entonces visible. Escenario 2: Error Entonces mensaje. |
     
## 3.2. Impact Mapping
[pending content]
## 3.3. Product Backlog
[pending content]
