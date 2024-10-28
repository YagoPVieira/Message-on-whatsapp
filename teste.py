import pywhatkit
phone_number = "+550000000000"
message = "Essa mensagem foi programada por Python"
hours = 0
minutes = 00
pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
print("Mensagem enviada com sucesso")