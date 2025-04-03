import time

status = "pendente"
while status == "pendente":
    print("Aguardando aprovação...")
    time.sleep(3)
    status = "Aprovado!"
print("Processo aprovado! \nContinuando automação...")
