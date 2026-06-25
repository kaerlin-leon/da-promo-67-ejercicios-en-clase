

#%%
from src import etl_funciones_soporte as fun
from src import queries_creacion_bbd_tablas as query

#%%
productos, clientes, ventas = fun.archivos()

fun.exploracion(productos, clientes, ventas)

#%%
productos_limpio, clientes_limpio, ventas_limpio = fun.limpieza(clientes,productos,ventas)
#display(clientes_limpio)

#%%
tabla_unica = fun.union(productos, clientes, ventas)

tabla_final = fun.transformacion(tabla_unica)

# Importación a la base de datos de productos, clientes y ventas
#%%
fun.creacion_tablas_esquema(query.creacion_esquema , '', 'tienda_italiana')
# %%
fun.creacion_tablas_esquema(query.crear_tabla_clientes , '')
# %%
fun.creacion_tablas_esquema(query.crear_tabla_productos , '')

# %%
fun.creacion_tablas_esquema(query.crear_tabla_ventas , '')
# %%
tuplas_productos = list(set(zip(productos_limpio['ID'] , productos_limpio['Nombre_Producto'] , productos_limpio['Categoría'] , productos_limpio['Precio'] , productos_limpio['Origen'] , productos_limpio['Descripción'])))

tuplas_clientes = list(set(zip(clientes_limpio['first_name'] , clientes_limpio['last_name'] , clientes_limpio['email'] , clientes_limpio['gender'] , clientes_limpio['City'], clientes_limpio['Country'] , clientes_limpio['Address'])))

tuplas_ventas = list(set(zip(ventas_limpio['ID_Producto'] , ventas_limpio['ID_Cliente'] , ventas_limpio['Fecha_Venta'] , ventas_limpio['Cantidad'] , ventas_limpio['Total'])))

# %%
fun.insertar_datos(query.insertar_productos, '', 'tienda_italiana', tuplas_productos)

#%%
fun.insertar_datos(query.insertar_clientes, '', 'tienda_italiana', tuplas_clientes)

#%%
fun.insertar_datos(query.insertar_ventas, '', 'tienda_italiana', tuplas_ventas)
# %%
