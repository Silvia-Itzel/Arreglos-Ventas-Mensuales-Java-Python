class VentasMensuales:
    def __init__(self):
        self.meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                     "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.departamentos = ["Ropa", "Deportes", "Juguetería"]
        self.ventas = [[0.0] * 3 for _ in range(12)]
    
    def insertar_venta(self, mes, departamento, monto):
        """Inserta una venta en el mes y departamento especificados"""
        mes_idx = self._obtener_indice_mes(mes)
        dept_idx = self._obtener_indice_dept(departamento)
        
        if mes_idx != -1 and dept_idx != -1:
            self.ventas[mes_idx][dept_idx] = monto
            print(f"Venta insertada: {mes} - {departamento}: ${monto:.2f}")
        else:
            print("Error: Mes o departamento no válido.")
    
    def buscar_venta(self, mes, departamento):
        """Busca y muestra una venta específica"""
        mes_idx = self._obtener_indice_mes(mes)
        dept_idx = self._obtener_indice_dept(departamento)
        
        if mes_idx != -1 and dept_idx != -1:
            valor = self.ventas[mes_idx][dept_idx]
            print(f"Venta encontrada: {mes} - {departamento}: ${valor:.2f}")
            return valor
        else:
            print("Error: Mes o departamento no válido.")
            return None
    
    def eliminar_venta(self, mes, departamento):
        """Elimina una venta (establece a 0)"""
        mes_idx = self._obtener_indice_mes(mes)
        dept_idx = self._obtener_indice_dept(departamento)
        
        if mes_idx != -1 and dept_idx != -1:
            self.ventas[mes_idx][dept_idx] = 0.0
            print(f"Venta eliminada: {mes} - {departamento}")
        else:
            print("Error: Mes o departamento no válido.")
    
    def mostrar_ventas(self):
        """Muestra todas las ventas en formato de tabla"""
        print("\n" + "="*60)
        print(f"{'Mes':<12} | {'Ropa':<10} | {'Deportes':<10} | {'Juguetería':<10}")
        print("-" * 60)
        
        for i in range(12):
            print(f"{self.meses[i]:<12} | ${self.ventas[i][0]:<9.2f} | ${self.ventas[i][1]:<9.2f} | ${self.ventas[i][2]:<9.2f}")
        
        print("="*60)
    
    def _obtener_indice_mes(self, mes):
        """Método auxiliar para obtener el índice del mes"""
        for i, m in enumerate(self.meses):
            if m.lower() == mes.lower():
                return i
        return -1
    
    def _obtener_indice_dept(self, departamento):
        """Método auxiliar para obtener el índice del departamento"""
        for i, d in enumerate(self.departamentos):
            if d.lower() == departamento.lower():
                return i
        return -1


# Función principal para demostrar el funcionamiento
def main():
    vm = VentasMensuales()
    
    # Insertar algunas ventas de ejemplo
    print("=== INSERTANDO VENTAS ===")
    vm.insertar_venta("Enero", "Ropa", 1500.75)
    vm.insertar_venta("Febrero", "Deportes", 2300.50)
    vm.insertar_venta("Marzo", "Juguetería", 1800.25)
    vm.insertar_venta("Abril", "Ropa", 1250.00)
    vm.insertar_venta("Mayo", "Deportes", 1950.30)
    
    # Mostrar el estado inicial
    print("\n=== ESTADO INICIAL DE VENTAS ===")
    vm.mostrar_ventas()
    
    # Buscar una venta específica
    print("\n=== BUSCANDO VENTA ===")
    vm.buscar_venta("Febrero", "Deportes")
    
    # Eliminar una venta
    print("\n=== ELIMINANDO VENTA ===")
    vm.eliminar_venta("Marzo", "Juguetería")
    
    # Mostrar el estado final
    print("\n=== ESTADO FINAL DE VENTAS ===")
    vm.mostrar_ventas()


if __name__ == "__main__":
    main()