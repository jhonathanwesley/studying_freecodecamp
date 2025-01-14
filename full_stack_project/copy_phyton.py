from http.server import BaseHTTPRequestHandler, HTTPServer

# Definindo uma classe que herda de BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    # Método para lidar com requisições GET
    def do_GET(self):
        # Enviando código de status 200 (OK)
        self.send_response(200)
        
        # Definindo o cabeçalho da resposta
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Resposta que será enviada de volta ao cliente
        resposta = "<h1>Olá, mundo!</h1>"
        
        # Enviando a resposta
        self.wfile.write(resposta.encode('utf-8'))

# Função para rodar o servidor
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor rodando na porta {port}...')
    httpd.serve_forever()

# Rodando o servidor
if __name__ == "__main__":
    run()