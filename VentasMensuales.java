import java.util.Arrays;

public class VentasMensuales {
    private String[] meses = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};
    private String[] departamentos = {"Ropa", "Deportes", "Juguetería"};
    private double[][] ventas = new double[12][3];

    // Insertar venta en un mes y departamento específico
    public void insertarVenta(String mes, String departamento, double monto) {
        int mesIndex = obtenerIndiceMes(mes);
        int deptIndex = obtenerIndiceDept(departamento);
        
        if (mesIndex != -1 && deptIndex != -1) {
            ventas[mesIndex][deptIndex] = monto;
            System.out.println("Venta insertada: " + mes + " - " + departamento + ": $" + monto);
        } else {
            System.out.println("Error: Mes o departamento no válido.");
        }
    }

    // Buscar venta específica
    public void buscarVenta(String mes, String departamento) {
        int mesIndex = obtenerIndiceMes(mes);
        int deptIndex = obtenerIndiceDept(departamento);
        
        if (mesIndex != -1 && deptIndex != -1) {
            double valor = ventas[mesIndex][deptIndex];
            System.out.println("Venta encontrada: " + mes + " - " + departamento + ": $" + valor);
        } else {
            System.out.println("Error: Mes o departamento no válido.");
        }
    }

    // Eliminar venta (establecer a 0)
    public void eliminarVenta(String mes, String departamento) {
        int mesIndex = obtenerIndiceMes(mes);
        int deptIndex = obtenerIndiceDept(departamento);
        
        if (mesIndex != -1 && deptIndex != -1) {
            ventas[mesIndex][deptIndex] = 0.0;
            System.out.println("Venta eliminada: " + mes + " - " + departamento);
        } else {
            System.out.println("Error: Mes o departamento no válido.");
        }
    }

    // Mostrar todas las ventas en formato de tabla
    public void mostrarVentas() {
        System.out.printf("%-10s | %-10s | %-10s | %-10s%n", "Mes", "Ropa", "Deportes", "Juguetería");
        for (int i = 0; i < 12; i++) {
            System.out.printf("%-10s | %-10.2f | %-10.2f | %-10.2f%n", 
                meses[i], ventas[i][0], ventas[i][1], ventas[i][2]);
        }
    }

    // Métodos auxiliares para obtener índices
    private int obtenerIndiceMes(String mes) {
        for (int i = 0; i < meses.length; i++) {
            if (meses[i].equalsIgnoreCase(mes)) return i;
        }
        return -1;
    }

    private int obtenerIndiceDept(String departamento) {
        for (int i = 0; i < departamentos.length; i++) {
            if (departamentos[i].equalsIgnoreCase(departamento)) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        VentasMensuales vm = new VentasMensuales();
        
        // Insertar ventas de ejemplo
        vm.insertarVenta("Enero", "Ropa", 1500.75);
        vm.insertarVenta("Febrero", "Deportes", 2300.50);
        vm.insertarVenta("Marzo", "Juguetería", 1800.25);
        
        System.out.println("\n--- Estado inicial de ventas ---");
        vm.mostrarVentas();
        
        // Buscar una venta
        System.out.println("\n--- Buscar venta de Febrero en Deportes ---");
        vm.buscarVenta("Febrero", "Deportes");
        
        // Eliminar una venta
        System.out.println("\n--- Eliminar venta de Marzo en Juguetería ---");
        vm.eliminarVenta("Marzo", "Juguetería");
        
        System.out.println("\n--- Estado final de ventas ---");
        vm.mostrarVentas();
    }
}