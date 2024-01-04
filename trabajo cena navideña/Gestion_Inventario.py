class Producto:
    def _init_(self, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.valor_compra = valor_compra
        self.valor_venta = valor_venta
        self.stock_minimo = stock_minimo
        self.stock_maximo = stock_maximo
        self.proveedor = proveedor
        self.stock_actual = 0

productos = []

def registrar_producto():
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    valor_compra = float(input("Valor de compra: "))
    valor_venta = float(input("Valor de venta: "))
    stock_minimo = int(input("Stock mínimo permitido: "))
    stock_maximo = int(input("Stock máximo permitido: "))
    proveedor = input("Nombre del proveedor: ")

    nuevo_producto = Producto(codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor)
    productos.append(nuevo_producto)

def visualizar_productos():
    for producto in productos:
        print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Valor de venta: {producto.valor_venta}, Stock: {producto.stock_actual}")

def actualizar_stock():
    codigo = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad a agregar/restar al stock: "))

    for producto in productos:
        if producto.codigo == codigo:
            producto.stock_actual += cantidad
            break
    else:
        print("Producto no encontrado.")

def informe_productos_criticos():
    productos_criticos = [producto for producto in productos if producto.stock_actual < producto.stock_minimo]
    for producto in productos_criticos:
        print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Stock actual: {producto.stock_actual}")

def calcular_ganancia_potencial():
    ganancia_total = sum((producto.valor_venta - producto.valor_compra) * producto.stock_actual for producto in productos)
    print(f"Ganancia potencial total: {ganancia_total}")

# Ejemplo de uso:
registrar_producto()
registrar_producto()
visualizar_productos()
actualizar_stock()
informe_productos_criticos()
calcular_ganancia_potencial()