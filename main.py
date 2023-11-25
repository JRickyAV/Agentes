import socket
import threading
import time

class Sensor:
    def __init__(self, id,port,host2,port2):
        self.id = id
        self.host = '192.168.1.67'
        self.port = port

        self.host2 = host2
        self.port2 = port2
        self.mensaje = None
        

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.bind((self.host, self.port))

        self.hilo_recibir = threading.Thread(target=self._recibirMensajes, daemon=True)
        self.hilo_recibir.start()



    
    def _recibirMensajes(self):
        while True:
            data, addr = self.client_socket.recvfrom(1024)
            self.mensaje = data.decode()
            # Aquí puedes realizar cualquier lógica para procesar el mensaje recibido
            # y cambiar la variable de la clase según tus necesidades.
            print(f'Mensaje recibido de {addr}: {self.mensaje}')




    def send_udp_message(self,mensaje):
        # Enviar un mensaje al servidor
        self.client_socket.sendto(mensaje.encode(), (self.host2, self.port2))

        

def main():
    sensor1 = Sensor(1,8081,"192.168.1.67",8080)
    sensor1.send_udp_message("Hola")
    while True:
        time.sleep(1)
    


