# robot SSOFI
Sube una dedicación exclusiva al SSOFI

Para ver el robot en acción cambie a `False` en la línea:
```python
driver = start_chrome(headless=True) 
```
Compruebe que `screenshot.png` fue generado para comprobar que el robot funcionó.

Descomentar las siguientes líneas para enviar al SSOFI y capturar el número de caso asignado:
```python
#click('Guardar')
#caso=Text('NÚMERO DE CASO').value.split()[-1]
```


## Requerimientos
```bash
pip install helium
```


