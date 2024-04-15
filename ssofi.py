from helium import *
from getpass import getpass
from time import sleep


# Parte de configuración
user = input('Usuario:') # Usar asignado a la aplicación
password = password=getpass('Clave:') # Usar asignado a la aplicación
nombre = 'Juan Valdez' # obtener de SIGA
tipo = 'investigación' # obtener de SIGA
file1 = '/home/restrepo/Downloads/certificado_1711225622105.pdf' # obtener de SIGA
file2 = '/home/restrepo/Downloads/certificado_1712260943375.pdf' # obtener de SIGA

# Parte de ejecución
# opción `headless=False` para ver el robot en acción
driver = start_chrome(headless=True) 

go_to('https://ssofi.udea.edu.co/fcen/index.jsp')
write(user, into='Usuario')
write(password, into='Clave')

click('Ingresar')
click('Solicitante')

sleep(1)

click('Ingresar')
click('Generar')

sleep(1)

select('- Seleccione una categoría -','Asuntos Profesorales')

wait_until( TextField('- Seleccione un departamento -').exists )
select('- Seleccione un departamento -','ASUNTOS PROFESORALES')

sleep(1)

select('- Seleccione un Comité o un Consejo -','Instituto de Física - Consejo de instituto')
wait_until( TextField('Asuntos de Dedicación Exclusiva').exists )
select('- Seleccione un Asunto -','Asuntos de Dedicación Exclusiva')
wait_until( TextField('Solicitud de Dedicación Exclusiva').exists )
select('- Seleccione un Tipo -', 'Solicitud de Dedicación Exclusiva')

sleep(1)

write(f'BORRAR SOLICITUD, ENVÍO DE PRUEBA POR ROBOT: Solicitud de Dedicación Exclusiva de {tipo} de {nombre}',into='Descripción y justificación:')

write('Formato 1',into='Descripción:')
attach_file(file1,to='Archivo:')
click('Agregar Anexo')

write('Formato 2',into='Descripción:')
attach_file(file2,to='Archivo:')
click('Agregar Anexo')

#Agregar más anexos aqui...

click('Eliminar')

caso = None
# Descomentar sólo en caso de que se deseé registrar el caso realmente en el SSOFI
#click('Guardar')
#caso=Text('NÚMERO DE CASO').value.split()[-1]
if caso:
    print(caso)
else:
    print('see ./screenshot.png')
    get_driver().save_screenshot('screenshot.png')

kill_browser()
