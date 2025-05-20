import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

# Função para enviar e-mails
def enviar_email():
    email_remetente = entry_email.get()
    senha = entry_senha.get()
    caminho_csv = entry_csv.get()

    if not email_remetente or not senha or not caminho_csv:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
        return

    try:
        df = pd.read_csv(caminho_csv)
    except Exception as e:
        messagebox.showerror("Erro ao ler o CSV", str(e))
        return
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_remetente, senha)
    except Exception as e:
        messagebox.showerror("Erro ao conectar ao servidor", str(e))
        return
    
    log_area.insert(tk.END, "Iniciando envio de e-mails...\n")

    for _, row in df.iterrows():
        nome = row['Nome']
        destinatario = row['Email']
        assunto = row['Assunto']
        mensagem = row['Mensagem']

        msg = MIMEMultipart()
        msg['From'] = email_remetente
        msg['To'] = destinatario
        msg['Subject'] = assunto

        corpo = f'Olá {nome}, \n\n{mensagem}\n\nAtenciosamente,\n'
        msg.attach(MIMEText(corpo, 'plain'))

        try:
            server.send_message(msg)
            log_area.insert(tk.END, f"✅ E-mail enviado para {destinatario}\n")
        except Exception as e:
            log_area.insert(tk.END, f"❌ Falha para {destinatario}: {e}\n")

    server.quit()
    log_area.insert(tk.END, "✅ Todos os e-mails foram processados.\n")

# Função para escolher o arquivo CSV
def selecionar_csv():
    caminho = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    entry_csv.delete(0, tk.END)
    entry_csv.insert(0, caminho)

# Interface Tkinter
janela = tk.Tk()
janela.title("Automatizador de E-mails")
janela.geometry("600x500")

tk.Label(janela, text="Seu E-mail:").pack()
entry_email = tk.Entry(janela, width=50)
entry_email.pack()

tk.Label(janela, text="Senha ou senha do e-mail:").pack()
entry_senha = tk.Entry(janela, width=50, show="*")
entry_senha.pack()

tk.Label(janela, text="Arquivo CSV:").pack()
frame_csv = tk.Frame(janela)
entry_csv = tk.Entry(frame_csv, width=40)
entry_csv.pack(side=tk.LEFT)
tk.Button(frame_csv, text="Selecionar", command=selecionar_csv).pack(side=tk.LEFT)
frame_csv.pack()

tk.Button(janela, text="Enviar E-mails", command=enviar_email, bg="green", fg="white").pack(pady=10)

tk.Label(janela, text="Log:").pack()
log_area = scrolledtext.ScrolledText(janela, width=70, height=15)
log_area.pack()

janela.mainloop()