from http.server import HTTPServer, BaseHTTPRequestHandler



class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        """Обработка GET-запросов"""
        try:
            # Читаем HTML файл
            with open('./src/contact.html', 'r', encoding='utf-8') as file:
                html_content = file.read()

            # Отправляем успешный ответ
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # Отправляем HTML содержимое
            self.wfile.write(html_content.encode('utf-8'))

            print(f"GET request received for {self.path}. HTML page sent.")

        except FileNotFoundError:
            # Если файл не найден
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Ошибка 404: Страница не найдена".encode('utf-8'))

        except Exception as e:
            # Обработка других ошибок
            self.send_response(500)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(f"Ошибка 500: {str(e)}".encode('utf-8'))


def run_server():
    """Запуск сервера"""
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyServer)

    print('Сервер запущен на http://localhost:8000')
    print('Нажмите Ctrl+C для остановки сервера')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nСервер остановлен')
        httpd.shutdown()


if __name__ == '__main__':
    run_server()