#Copiar "pip install pywhatkit" en la consola de python
import pywhatkit
#Los parametros que toma el siguiente codigo son:
#Numero de celular, agregar el codigo de pais correspondiente (+51), Mensaje a mandar, la hora, el minuto, 
#los segundos que demorara en enviar el mensaje, si la pagina se va a cerrar o no, los segundos que tardara la pagina en cerrarse
pywhatkit.sendwhatmsg('NUMERO','Mensaje',3,47,15,False,5)