# 📧 Automatizador de E-mails com Interface Gráfica

Este projeto é uma aplicação em Python que permite o envio de e-mails personalizados em massa a partir de um arquivo `.csv`, com uma interface gráfica desenvolvida em **Tkinter**.

---

## 🧰 Tecnologias Utilizadas

- **Python 3**
- `tkinter` – Interface gráfica
- `pandas` – Leitura e manipulação de dados CSV
- `smtplib` e `email` – Envio de e-mails via SMTP

---

## 🚀 Funcionalidades

- Leitura de lista de e-mails a partir de um arquivo CSV
- Envio de e-mails personalizados com nome, assunto e mensagem únicos por destinatário
- Interface intuitiva com campos de entrada e botão para selecionar o arquivo CSV
- Log de envio exibido em tempo real na tela
- Compatível com servidores como Gmail e Outlook (usando senha de app)

---

## 📂 Estrutura esperada do CSV

O arquivo `.csv` deve conter os seguintes campos:

```csv
Nome,Email,Assunto,Mensagem
Maria,maria@example.com,Relatório Mensal,Olá Maria, segue o relatório...
João,joao@example.com,Lembrete,Olá João, lembrando sobre nossa reunião...


##❗ IMPORTANTE: Usar senha de app no Gmail

Você precisa usar uma senha de app, não sua senha real. Veja como fazer:

Acesse: https://myaccount.google.com/security

Ative a verificação em duas etapas

Depois vá em “Senhas de app” → gere uma senha

Use essa senha no programa

## ✅ Preencha os campos na interface
E-mail Remetente: seu e-mail do Gmail

Senha: uma senha de app (não sua senha normal!)

CSV: clique em “Selecionar” e escolha o arquivo .csv

Clique em “Enviar E-mails”
