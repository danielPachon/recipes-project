# Recipe Project

## Descripción General

**Recipe Project** es una aplicación desarrollada con FastAPI que ayuda a los usuarios a organizar sus recetas de cocina, planificar menús semanales, generar listas de compras basadas en los ingredientes necesarios para las recetas seleccionadas, y sugerir recetas basadas en los ingredientes disponibles en su inventario.

### Características Principales

1. **Gestión de Usuarios**: Registro, autenticación, y gestión de perfiles de usuarios, incluyendo la creación de cuentas familiares o grupales.
2. **Gestión de Recetas**: Creación, edición, búsqueda y categorización de recetas con detalles como ingredientes, instrucciones, y datos nutricionales.
3. **Planificación de Menús**: Ayuda a los usuarios a planificar sus comidas diarias o semanales utilizando recetas guardadas.
4. **Generación de Listas de Compras**: Generación automática de listas de compras basadas en las recetas seleccionadas.
5. **Notificaciones**: Envío de notificaciones relacionadas con menús, listas de compras y recordatorios.
6. **Gestión de Despensa**: Permite llevar un registro de los ingredientes disponibles en casa.
7. **Sugerencias de Recetas Basadas en Ingredientes Disponibles**: El sistema sugiere recetas que pueden ser preparadas con los ingredientes que el usuario tiene en su despensa.

---

## Microservicios Propuestos

### 1. Gestión de Usuarios
**Responsabilidades**:  
Registro, autenticación y gestión de perfiles de usuarios individuales o familiares.

**Funcionalidades**:
- Registro y autenticación (JWT o OAuth2).
- Gestión de perfiles (edición de datos, foto de perfil).
- Roles y permisos en cuentas familiares/grupales.

### 2. Gestión de Recetas
**Responsabilidades**:  
Creación, edición, búsqueda y compartición de recetas.

**Funcionalidades**:
- Creación y edición de recetas con ingredientes, instrucciones, y datos nutricionales.
- Categorización por tipo de comida, dificultad, tiempo de preparación.
- Búsqueda y filtrado de recetas.
- Compartir recetas con otros usuarios o hacerlas públicas/privadas.

### 3. Planificación de Menús
**Responsabilidades**:  
Planificación de comidas diarias o semanales con las recetas guardadas.

**Funcionalidades**:
- Planificación de menús semanales o diarios.
- Visualización de menús en un calendario.
- Notificaciones y recordatorios de comidas.

### 4. Generación de Listas de Compras
**Responsabilidades**:  
Generación automática de listas de compras según las recetas seleccionadas.

**Funcionalidades**:
- Compilación automática de ingredientes.
- Agrupación de ingredientes por categorías.
- Integración con servicios de compras en línea.

### 5. Microservicio de Notificaciones
**Responsabilidades**:  
Enviar notificaciones relacionadas con los menús, compras y recordatorios.

**Funcionalidades**:
- Envío de recordatorios de compras.
- Notificaciones de preparación de comidas.
- Alertas sobre caducidad de productos en la despensa.

### 6. Gestión de Despensa
**Responsabilidades**:  
Llevar un inventario de los ingredientes disponibles en casa.

**Funcionalidades**:
- Registro de productos en la despensa.
- Seguimiento de cantidades y fechas de caducidad.
- Sugerencias de recetas basadas en el inventario disponible.

### 7. Sugerencia de Recetas Basadas en Ingredientes Disponibles
**Responsabilidades**:  
Sugerir recetas que los usuarios pueden preparar según los ingredientes de su inventario.

**Funcionalidades**:
- Sugerir recetas basadas en el inventario de ingredientes.
- Filtrar recetas por tipo de comida, dificultad, tiempo de preparación.
- Indicar ingredientes faltantes para completar la receta.
- Marcar recetas como favoritas.

---

## Requisitos

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy** (para gestión de base de datos)
- **Alembic** (para migraciones de base de datos)
- **Uvicorn** (como servidor ASGI)

---
