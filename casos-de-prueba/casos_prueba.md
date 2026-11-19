# TC-001: Verificar los elementos de la página de inicio de sesión

- **Módulo:** Inicio de sesión.
- **Tipo de prueba:** Prueba funcional de interfaz (UI).
- **Prioridad:** Alta.
- **Objetivo:** Verificar que los campos de usuario y contraseña, y el botón Login, estén visibles y disponibles.
- **Precondiciones:** Tener conexión a internet y acceso a la página Sauce Demo.

**Pasos de ejecución:**

1. Abrir https://www.saucedemo.com/.
2. Observar la pantalla de inicio de sesión.
3. Comprobar la visibilidad del campo Username.
4. Comprobar la visibilidad del campo Password.
5. Comprobar la visibilidad del botón Login.

**Resultado esperado:** Los dos campos y el botón Login aparecen correctamente y permiten interactuar con ellos.

**Resultado obtenido:** Los dos campos y el botón Login aparecen correctamente y permiten interactuar con ellos.

**Estado:** PASS.

**Evidencia:** Captura de pantalla de la página de inicio de sesión.

# TC-002: Inicio de sesión con credenciales válidas

- **Módulo:** Inicio de sesión.
- **Tipo de prueba:** Funcional.
- **Prioridad:** Alta.
- **Objetivo:** Verificar que un usuario pueda iniciar sesión con credenciales válidas.
- **Precondiciones:** Acceder a https://www.saucedemo.com/.

**Datos de prueba:**
- Usuario: `standard_user`
- Contraseña: `secret_sauce`

**Pasos de ejecución:**

1. Abrir la página de Sauce Demo.
2. Ingresar `standard_user` en el campo Username.
3. Ingresar `secret_sauce` en el campo Password.
4. Hacer clic en el botón Login.
5. Verificar la página que se muestra después del inicio de sesión.

**Resultado esperado:** El sistema permite iniciar sesión y muestra la página de productos (Products).

**Resultado obtenido:** El sistema permite iniciar sesión y muestra la página de productos (Products).

**Estado:** PASS

**Evidencia:** Captura de pantalla de la página de productos después de iniciar sesión.

---

# TC-003: Inicio de sesión con credenciales inválidas

- **Módulo:** Inicio de sesión.
- **Tipo de prueba:** Funcional negativa.
- **Prioridad:** Alta.
- **Objetivo:** Verificar que el sistema rechace credenciales incorrectas.
- **Precondiciones:** Acceder a https://www.saucedemo.com/.

**Datos de prueba:**
- Usuario: `usuario_incorrecto`
- Contraseña: `clave_incorrecta`

**Pasos de ejecución:**

1. Abrir la página de Sauce Demo.
2. Ingresar `usuario_incorrecto` en el campo Username.
3. Ingresar `clave_incorrecta` en el campo Password.
4. Hacer clic en el botón Login.
5. Verificar el mensaje de error.

**Resultado esperado:** El sistema impide el acceso y muestra un mensaje indicando que las credenciales no son válidas.

**Resultado obtenido:** El sistema impide el acceso y muestra un mensaje indicando que las credenciales no son válidas.

**Estado:** PASS.
**Evidencia:** Captura de pantalla del mensaje de error.

# TC-004: Verificar la visualización del catálogo de productos.

- **Módulo:** Products.
- **Tipo de prueba:** Funcional.
- **Prioridad:** Media.
- **Objetivo:** Verificar que el catálogo muestre los productos con sus nombres, precios e información visible correctamente.
- **Precondiciones:** Acceder a https://www.saucedemo.com/.

**Datos de prueba:**
- Usuario: `standard_user`
- Contraseña: `secret_sauce`

**Pasos de ejecución:**

1. Abrir la página de Sauce Demo.
2. Ingresar `standard_user` en el campo Username.
3. Ingresar `secret_sauce` en el campo Password.
4. Hacer clic en el botón Login.
5. Visualizar el catálogo de productos.
6. Comprobar que los productos tengan nombre y precio visibles.
7. Verificar que se muestren las imágenes y los botones para agregar productos al carrito.

**Resultado esperado:** El catálogo se muestra correctamente y los productos presentan sus nombres, precios, imágenes y botones de agregar al carrito.

**Resultado obtenido:** El catálogo de productos se muestra correctamente y los elementos verificados están visibles.

**Estado:** PASS.
**Evidencia:** Captura de pantalla del catálogo de productos.

# TC-005: Comprobar la funcionalidad de agregar un producto al carrito

- **Módulo:** Carrito de compras.
- **Tipo de prueba:** Funcional.
- **Prioridad:** Media.
- **Objetivo:** Verificar que un producto pueda agregarse correctamente al carrito.
- **Precondiciones:** Haber iniciado sesión en Sauce Demo con credenciales válidas y encontrarse en la página Products.

**Datos de prueba:**
- Usuario: `standard_user`
- Contraseña: `secret_sauce`
- Producto: Sauce Labs Backpack.

**Pasos de ejecución:**

1. Abrir https://www.saucedemo.com/.
2. Ingresar el usuario `standard_user`.
3. Ingresar la contraseña `secret_sauce`.
4. Hacer clic en el botón Login.
5. Identificar el producto Sauce Labs Backpack.
6. Hacer clic en el botón Add to cart correspondiente a ese producto.
7. Verificar que el indicador del carrito muestre la cantidad 1.
8. Hacer clic en el ícono del carrito.
9. Comprobar que Sauce Labs Backpack aparezca en el carrito.

**Resultado esperado:** El producto se agrega correctamente al carrito, el indicador muestra 1 y el producto aparece en la página del carrito.

**Resultado obtenido:** El producto se agrega correctamente al carrito, el indicador muestra 1 y el producto aparece en la página del carrito.

**Estado:** PASS.

**Evidencia:** Captura de pantalla del carrito que muestre el producto agregado.

# TC-006: eliminar un producto del carrito

- **Módulo:** Carrito de compras.
- **Tipo de prueba:** Funcional.
- **Prioridad:** Media.
- **Objetivo:** Verificar que un producto pueda eliminarse correctamente del carrito.
- **Precondiciones:** Haber iniciado sesión en Sauce Demo con credenciales válidas y agregar previamente un producto al carrito.

**Datos de prueba:**
- Usuario: `standard_user`
- Contraseña: `secret_sauce`
- Producto: Sauce Labs Backpack.

**Pasos de ejecución:**

1. Abrir https://www.saucedemo.com/.
2. Ingresar el usuario `standard_user`.
3. Ingresar la contraseña `secret_sauce`.
4. Hacer clic en el botón Login.
5. Identificar el producto Sauce Labs Backpack.
6. Hacer clic en Add to cart.
7. Abrir el carrito y verificar que el producto aparezca.
8. Hacer clic en el botón Remove del producto.
9. Verificar que el producto ya no aparezca en el carrito.
10. Comprobar que el indicador de cantidad del carrito desaparezca si no quedan productos.

**Resultado esperado:** El producto se elimina correctamente del carrito y ya no aparece en la lista. Si era el único producto, el carrito queda vacío.

**Resultado obtenido:** El producto se elimina correctamente del carrito y ya no aparece en la lista. Si era el único producto, el carrito queda vacío.

**Estado:** PASS.

**Evidencia:** Captura de pantalla del carrito que muestre el producto agregado.

# TC-007: verificar el cálculo del total de la compra en el resumen del pedido

- **Módulo:** Checkout - Overview.
- **Tipo de prueba:** Funcional.
- **Prioridad:** Media.
- **Objetivo:** Verificar que el subtotal, los impuestos y el total de la compra se calculen correctamente.
- **Precondiciones:** Haber iniciado sesión con credenciales válidas y agregar los productos seleccionados al carrito.

**Datos de prueba:**
- Usuario: `standard_user`
- Contraseña: `secret_sauce`
- Productos: Sauce Labs Backpack y Sauce Labs Bolt T-Shirt.

**Pasos de ejecución:**

1. Abrir https://www.saucedemo.com/.
2. Ingresar el usuario `standard_user`.
3. Ingresar la contraseña `secret_sauce`.
4. Hacer clic en el botón Login.
5. Identificar los productos Sauce Labs Backpack y Sauce Labs Bolt T-Shirt.
6. Abrir el carrito y verificar que ambos productos aparezcan.
7. Hacer clic en Checkout.
8. Completar los campos First Name, Last Name y Zip/Postal Code con datos de prueba ficticios.
9. Hacer clic en el botón `Continue`.
10. Verificar que ambos productos aparezcan en el resumen del pedido.
11. Comprobar el subtotal de los productos.
12. Comprobar el importe de los impuestos (Tax).
13. Verificar que el total sea igual al subtotal más los impuestos.

**Resultado esperado:** El resumen muestra los productos seleccionados, el subtotal corresponde a la suma de sus precios, los impuestos se calculan correctamente y el total coincide con la suma del subtotal y los impuestos.

**Resultado obtenido:** El resumen muestra los productos seleccionados, el subtotal corresponde a la suma de sus precios, los impuestos se calculan correctamente y el total coincide con la suma del subtotal y los impuestos.

**Estado:** PASS.

**Evidencia:** Captura de pantalla del carrito que muestre el producto agregado.

# TC-008: Verificar la finalización de compra

- **Módulo:** Checkout.
- **Tipo de prueba:** Funcional.
- **Prioridad:** Alta.
- **Objetivo:** Verificar que el usuario pueda finalizar correctamente una compra.
- **Precondiciones:** Haber iniciado sesión con credenciales válidas y agregar al menos un producto al carrito.

**Datos de prueba:**
- Usuario: `standard_user`
- Contraseña: `secret_sauce`
- Productos: Sauce Labs Backpack y Sauce Labs Bolt T-Shirt.

**Pasos de ejecución:**

1. Abrir https://www.saucedemo.com/.
2. Ingresar el usuario `standard_user`.
3. Ingresar la contraseña `secret_sauce`.
4. Hacer clic en el botón Login.
5. Agregar los productos Sauce Labs Backpack y Sauce Labs Bolt T-Shirt.
6. Abrir el carrito y verificar que ambos productos aparezcan.
7. Hacer clic en Checkout.
8. Completar los campos First Name, Last Name y Zip/Postal Code con datos de prueba ficticios.
9. Hacer clic en el botón `Continue`.
10. Verificar que ambos productos e importes aparezcan en el resumen del pedido.
11. Hacer clic en `Finish`.
12. Verificar mensaje de confirmación de compra.

**Resultado esperado:** El sistema finaliza el pedido y muestra una confirmación de compra, por ejemplo, el mensaje "Thank you for your order!".

**Resultado obtenido:** El sistema finalizó la compra correctamente y mostró el mensaje "Thank you for your order!".

**Estado:** PASS.

**Evidencia:** Captura de pantalla del carrito que muestre el producto agregado.

# TC-009: Verificar el ordenamiento de productos por precio ascendente

- **Módulo:** Products
- **Tipo de prueba:** Funcional.
- **Prioridad:** Media.
- **Objetivo:** Verificar que los productos se ordenen de menor a mayor precio.
- **Precondiciones:** Haber iniciado sesión en Sauce Demo y encontrarse en el catálogo de productos.

**Datos de prueba:**
- Usuario: `standard_user`
- Contraseña: `secret_sauce`
- Criterio de ordenamiento: Price (low to high).

**Pasos de ejecución:**

1. Abrir https://www.saucedemo.com/.
2. Iniciar sesión con las credenciales válidas.
3. Ubicar el menú desplegable de ordenamiento.
4. Seleccionar Price (low to high).
5. Revisar los precios de los productos mostrados.
6. Verificar que los precios estén ordenados de menor a mayor.

**Resultado esperado:** Los productos aparecen ordenados por precio ascendente, desde el más económico hasta el más costoso.

**Resultado obtenido:** Los productos se muestran ordenados correctamente de menor a mayor precio

**Estado:** PASS.

**Evidencia:** Captura de pantalla del catálogo con el ordenamiento por precio ascendente.

# TC-010: Verificar el ordenamiento alfabético de productos (A a Z)

- **Módulo:** Products
- **Tipo de prueba:** Funcional.
- **Prioridad:** Media.
- **Objetivo:** Verificar que los productos se ordenen alfabéticamente de la A a la Z.
- **Precondiciones:** Haber iniciado sesión en Sauce Demo y encontrarse en el catálogo de productos.

**Datos de prueba:**
- Usuario: `standard_user`
- Contraseña: `secret_sauce`
- Criterio de ordenamiento: Name (A a Z).

**Pasos de ejecución:**

1. Abrir https://www.saucedemo.com/.
2. Iniciar sesión con las credenciales válidas.
3. Ubicar el menú desplegable de ordenamiento.
4. Seleccionar Name (A a Z).
5. Revisar los nombres de los productos mostrados.
6. Verificar que los nombres estén ordenados de la A a la Z.

**Resultado esperado:** Los productos aparecen ordenados por nombre ascendente, desde la A hasta la Z.

**Resultado obtenido:** Los productos se muestran ordenados correctamente de la A a la Z.

**Estado:** PASS.

**Evidencia:** Captura de pantalla del catálogo con el ordenamiento por nombre.

# TC-011: Verificar el ordenamiento alfabético de productos (Z a A)

- **Módulo:** Products.
- **Tipo de prueba:** Funcional.
- **Prioridad:** Media.
- **Objetivo:** Verificar que los productos se ordenen alfabéticamente de la Z a la A.
- **Precondiciones:** Haber iniciado sesión en Sauce Demo y encontrarse en el catálogo de productos.

**Datos de prueba:**
- Usuario: `standard_user`
- Contraseña: `secret_sauce`
- Criterio de ordenamiento: Name (Z to A).

**Pasos de ejecución:**

1. Abrir https://www.saucedemo.com/.
2. Iniciar sesión con las credenciales válidas.
3. Ubicar el menú desplegable de ordenamiento.
4. Seleccionar `Name (Z to A)`.
5. Revisar los nombres de los productos mostrados.
6. Verificar que los nombres estén ordenados de la Z a la A.

**Resultado esperado:** Los productos aparecen ordenados alfabéticamente en orden descendente, desde la Z hasta la A.

**Resultado obtenido:** Los productos se encuentran ordenados alfabéticamente en orden descendente, desde la Z hasta la A.

**Estado:** PASS.

**Evidencia:** Captura de pantalla del catálogo con el ordenamiento por nombre descendente.

# TC-012: Verificar el ordenamiento de productos por precio descendente

- **Módulo:** Products.
- **Tipo de prueba:** Funcional.
- **Prioridad:** Media.
- **Objetivo:** Verificar que los productos se ordenen de mayor a menor precio.
- **Precondiciones:** Haber iniciado sesión en Sauce Demo y encontrarse en el catálogo de productos.

**Datos de prueba:**
- Usuario: `standard_user`
- Contraseña: `secret_sauce`
- Criterio de ordenamiento: Price (high to low).

**Pasos de ejecución:**

1. Abrir https://www.saucedemo.com/.
2. Iniciar sesión con credenciales válidas.
3. Ubicar el menú desplegable de ordenamiento.
4. Seleccionar `Price (high to low)`.
5. Revisar los precios de los productos mostrados.
6. Verificar que estén ordenados de mayor a menor precio.

**Resultado esperado:** Los productos aparecen ordenados por precio descendente, desde el más costoso hasta el más económico.

**Resultado obtenido:** Los productos se encuentran ordenados por precio descendente.

**Estado:** PASS.

**Evidencia:** Captura de pantalla del catálogo con el ordenamiento por precio descendente.