<h1 align="center"> PII Hunter </h1>
ENGLISH VERSION: <br></br>
PII Hunter is a Python-based Burp Suite extension designed to identify Personally Identifiable Information (PII) in HTTP traffic. This tool helps security professionals and penetration testers find sensitive data such as emails, valid CPFs, valid credit card numbers, phone numbers, and dates of birth.
<br></br>


![image](https://github.com/user-attachments/assets/5dc1d18b-246f-42ae-8345-f159663841d1)


# Features
* Email detection: Scans for common email formats in HTTP responses.
* Valid CPF detection: Uses Brazil’s CPF validation algorithm to find and verify CPF numbers.
* Credit card detection: Identifies and validates credit card numbers using the Luhn algorithm.
* Phone number detection: Finds Brazilian phone numbers in the format (xx) xxxxxxxxx.
* Date of birth detection: Searches for dates in the format dd/mm/yyyy.

# Installation
1. Clone or download the repository.
2. Open Burp Suite and navigate to the Extender tab.
3. In the Extensions section, click Add.
4. Set Extension type to Python.
5. Load the PII_Hunter.py script.
6. The extension will automatically start scanning for PII in HTTP traffic.
7. Don't forget to have a .jar file in your burp!!

# Usage
Once the extension is loaded in Burp Suite, it will automatically scan HTTP responses for sensitive information.

* All matches for PII (emails, CPFs, credit card numbers, phone numbers, and dates) will be displayed in the Burp console.
* The extension works passively, so you don’t need to configure any additional scans.
 
# Limitations
* This extension focuses on Brazilian PII formats (CPF and phone numbers).
* It detects PII within the HTTP response bodies, so if PII is stored or transmitted elsewhere, it won't be detected.
* The phone number detection currently only supports Brazilian phone numbers.

# Contributing
I'm new to the community, so if you'd like to contribute to the project or suggest new features, feel free to open a pull request or issue on GitHub, as well as contact me!!
# 

PORTUGUESE VERSION: <br></br>

PII Hunter é uma extensão para o Burp Suite feita em Python, projetada para identificar Informações de Identificação Pessoal (PII) no tráfego HTTP. Esta ferramenta ajuda profissionais de segurança e testadores de penetração a encontrar dados sensíveis, como e-mails, CPFs válidos, números de cartão de crédito válidos, números de telefone e datas de nascimento.


# Funcionalidades
* Detecção de e-mails: Escaneia formatos comuns de e-mail nas respostas HTTP.
* Detecção de CPF válido: Utiliza o algoritmo de validação do CPF brasileiro para encontrar e verificar números de CPF.
* Detecção de cartões de crédito: Identifica e valida números de cartão de crédito usando o algoritmo de Luhn.
* Detecção de números de telefone: Encontra números de telefone brasileiros no formato (xx) xxxxxxxxx.
* Detecção de datas de nascimento: Procura por datas no formato dd/mm/yyyy.

# Instalação
1. Clone ou baixe o repositório.
2. Abra o Burp Suite e navegue até a aba Extender.
3. Na seção Extensions, clique em Add.
4. Defina o tipo de extensão como Python.
5. Carregue o script PII_Hunter.py.
6. A extensão começará automaticamente a escanear PII no tráfego HTTP.
7. Não se esqueça de ter um arquivo .jar no seu Burp!!!

# Usando
Depois que a extensão for carregada no Burp Suite, ela automaticamente escaneará respostas HTTP em busca de informações sensíveis.

*Todas as PII encontradas (e-mails, CPFs, números de cartão de crédito, números de telefone e datas) serão exibidas no console do Burp.
A extensão funciona de forma passiva, então não é necessário configurar scans adicionais.

# Limitações
* Esta extensão se concentra em formatos de PII brasileiros (CPF e números de telefone).
* Ela detecta PII dentro dos corpos das respostas HTTP, então, se a PII estiver armazenada ou transmitida em outro lugar, não será detectada.
* A detecção de números de telefone atualmente só suporta números brasileiros.
  
# Me ajude
Sou novo na comunidade, então, se você quiser contribuir com o projeto ou sugerir novas funcionalidades, fique à vontade para abrir um pull request ou issue no GitHub, assim como me contatar!!

