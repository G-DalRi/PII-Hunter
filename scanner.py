# -*- coding: utf-8 -*-
import re
from burp import IBurpExtender, IHttpListener
import sys

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        """
        Inicializa o Burp Extender e registra o HttpListener
        """
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("PII Hunter - Complete")
        callbacks.registerHttpListener(self)
        print("PII Hunter for Emails, Card Numbers, CPFs, Phone Numbers, and Dates of Birth, Installation OK!!!")

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        """
        Método chamado para processar requisições/respostas HTTP interceptadas pelo Burp
        """
        # Processa apenas as respostas HTTP, ignorando as requisições
        if not messageIsRequest:
            # Analisa a resposta HTTP
            response_info = self._helpers.analyzeResponse(messageInfo.getResponse())
            
            # Obtém o corpo da resposta HTTP
            body_offset = response_info.getBodyOffset()
            body_bytes = messageInfo.getResponse()[body_offset:]
            body = self._helpers.bytesToString(body_bytes)
            
            # Escaneia o corpo em busca de informações
            valid_card_numbers = [number for number in self.find_card_numbers_in_text(body) if self.is_valid_card_number(number)]
            valid_cpfs = [cpf for cpf in self.find_cpfs_in_text(body) if self.is_valid_cpf(cpf)]
            possible_dates_of_birth = self.find_dates_of_birth_in_text(body)
            possible_phone_numbers = self.find_phone_numbers_in_text(body)
            possible_emails = self.find_emails_in_text(body)

            # Exibe os resultados no console do Burp
            if valid_card_numbers:
                self.print_unicode("Número(s) de cartão de crédito válido(s): {}".format(', '.join(valid_card_numbers)))
            if valid_cpfs:
                self.print_unicode("CPF(s) válido(s) encontrado(s): {}".format(', '.join(valid_cpfs)))
            if possible_dates_of_birth:
                self.print_unicode("Data(s) de nascimento encontrada(s): {}".format(', '.join(possible_dates_of_birth)))
            if possible_phone_numbers:
                self.print_unicode("Número(s) de telefone encontrado(s): {}".format(', '.join(possible_phone_numbers)))
            if possible_emails:
                self.print_unicode("Email(s) encontrado(s): {}".format(', '.join(possible_emails)))

    def find_card_numbers_in_text(self, text):
        """
        Função que encontra números de cartão de crédito em um texto (corpo da resposta HTTP)
        """
        card_pattern = re.compile(r'\b\d{4} \d{4} \d{4} \d{4}\b')
        possible_card_numbers = card_pattern.findall(text)
        return list(set(possible_card_numbers))  # Remove duplicatas

    def is_valid_card_number(self, number):
        """
        Função que valida um número de cartão de crédito usando o algoritmo de Luhn
        """
        # Remove espaços e caracteres não numéricos
        number = re.sub(r'\D', '', number)
        
        # Verifica se o número tem pelo menos 13 dígitos
        if len(number) < 13:
            return False

        # Algoritmo de Luhn para validação
        def luhn_check(num):
            total = 0
            reverse_digits = num[::-1]
            for i, digit in enumerate(reverse_digits):
                n = int(digit)
                if i % 2 == 1:
                    n *= 2
                    if n > 9:
                        n -= 9
                total += n
            return total % 10 == 0

        return luhn_check(number)

    def find_cpfs_in_text(self, text):
        """
        Função que encontra CPFs em um texto (corpo da resposta HTTP)
        """
        cpf_pattern = re.compile(r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b')
        possible_cpfs = cpf_pattern.findall(text)
        return list(set(possible_cpfs))  # Remove duplicatas

    def is_valid_cpf(self, cpf):
        """
        Função que valida um CPF usando o algoritmo de verificação
        """
        # Remove caracteres não numéricos
        cpf = re.sub(r'\D', '', cpf)
        
        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        # Valida o primeiro dígito verificador
        sum_ = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digit1 = 11 - (sum_ % 11)
        digit1 = 0 if digit1 >= 10 else digit1

        # Valida o segundo dígito verificador
        sum_ = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digit2 = 11 - (sum_ % 11)
        digit2 = 0 if digit2 >= 10 else digit2

        return cpf[-2:] == "{}{}".format(digit1, digit2)

    def find_dates_of_birth_in_text(self, text):
        """
        Função que encontra datas de nascimento em um texto (corpo da resposta HTTP)
        """
        # Expressão regular para datas de nascimento no formato xx/xx/xxxx
        date_pattern = re.compile(r'\b\d{2}/\d{2}/\d{4}\b')

        # Busca por datas de nascimento no corpo da resposta
        possible_dates_of_birth = date_pattern.findall(text)
        
        return list(set(possible_dates_of_birth))  # Remove duplicatas

    def find_phone_numbers_in_text(self, text):
        """
        Função que encontra números de telefone em um texto (corpo da resposta HTTP)
        """
        phone_pattern = re.compile(r'\(\d{2}\) \d{9}')
        possible_phone_numbers = phone_pattern.findall(text)
        return list(set(possible_phone_numbers))  # Remove duplicatas

    def find_emails_in_text(self, text):
        """
        Função que encontra e-mails em um texto (corpo da resposta HTTP)
        """
        # regular email patter
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

        # Search for e-mails in the body
        possible_emails = email_pattern.findall(text)
        return list(set(possible_emails))  # Remove duplicatas

    def print_unicode(self, message):
        """
        Função para imprimir mensagens Unicode (Python 3 lida automaticamente com UTF-8)
        """
        try:
            print(message)
        except UnicodeEncodeError:
            print(message.encode('utf-8', errors='replace').decode('utf-8'))