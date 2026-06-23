# Importa a nossa Factory e o nosso Modelo
from portfolio.factories import ContactFactory
from portfolio.models import Contact

# Cria um novo contato gerando os dados falsos e já salvando no banco
novo_contato = ContactFactory()

# Mostra os dados que foram gerados aleatoriamente:
print("Nome:", novo_contato.first_name)
print("Sobrenome:", novo_contato.last_name)
print("Telefone:", novo_contato.phone_number)
print("Email:", novo_contato.email)

# Conta quantos contatos existem na tabela agora (você verá o número aumentar se rodar de novo)
print("Total de contatos no banco:", Contact.objects.count())

# Para sair do shell
exit()
