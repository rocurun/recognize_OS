import subprocess
import sys

def get_ttl(ip):
    # Ejecuta el comando ping y obtiene la  respuesta
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip], stderr=subprocess.STDOUT, universal_newlines=True)

        # Encuentra la línea con la información del TTL
        for line in output.split('\n'):
            if 'ttl=' in line.lower():
                # Extrae el valor del TTL
                ttl_value = int(line.split('ttl=')[1].split(' ')[0])
                return ttl_value
    except subprocess.CalledProcessError as e:
        print(f"No se pudo realizar ping a la dirección: {ip}")
        print(f"Error: {e.output}")
        return None

def guess_os(ttl):
    # Asigna un sistema operativo basado en el valor del TTL
    if ttl is not None:
        if ttl <= 64:
            return 'Linux'
        elif ttl <= 128:
            return 'Windows'
    return 'OS no identificado'

# Verifica si se ha proporcionado una IP como argumento
if len(sys.argv) != 2:
    print("Uso: python script.py <IP>")
    sys.exit(1)


ip_a_testear = sys.argv[1]
ttl = get_ttl(ip_a_testear)
os_detectado = guess_os(ttl)
print(f"El OS es: {os_detectado}")
