class EmailMixin:
    @staticmethod
    def send_email(to: str, subject: str, body: str):
        print(f'''Enviar email {to}, Asunto {subject},
         {body}
         ''')


class User(EmailMixin):
    def __init__(self, name: str, surname: str, email: str):
        self.name = name
        self.surname = surname
        self.email = email


santiago = User('Santiago', 'Pastor', 'santiago_pastor@educarex.es')

santiago.send_email('psaca@gmail.com', 'Factura del servicio', 'Buenas, le adjunto la fatura del servicio')

if __name__ == '__main__':
    pass
