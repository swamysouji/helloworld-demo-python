from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess, sys

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # Get free memory
        free_mem = subprocess.check_output(["free", "-h"]).decode()
        self.wfile.write(b"===== Free Memory =====\n")
        self.wfile.write(free_mem.encode())
        # Get list of running processes
        running_procs = subprocess.check_output(["ps", "aux"]).decode()
        self.wfile.write(b"\n===== Running Processes =====\n")
        self.wfile.write(running_procs.encode())
        # Get list of block devices
        block_devices = subprocess.check_output(["cat /proc/partitions"]).decode()   
        self.wfile.write(b"\n===== Block Devices =====\n")
        self.wfile.write(block_devices.encode())
        # run df -h and put in output
        #dfout = subprocess.check_output(["df", "-h"])
        #self.wfile.write(dfout)
        self.wfile.write("**********\n".encode())
        self.wfile.write(b'''
          ##         .
    ## ## ##        ==
 ## ## ## ## ##    ===
/"""""""""""""""""\___/ ===
{                       /  ===-
\______ O           __/
 \    \         __/
  \____\_______/


Hello from Docker!
''')

def run():
    print('Starting server...')
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print('Server started!')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
