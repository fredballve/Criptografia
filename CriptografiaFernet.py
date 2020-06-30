from cryptography.fernet import Fernet

arqinput=input("Digite o arquivo que deseja utilizar: ")  #input para o usuário escolher qual arquivo irá criptografar/descriptografar
arq=open(arqinput,"rb")                                   #Abre o arquivo para leitura "r" de forma binária "b"
conteudo=arq.read()                                       #Conteúdo do arquivo é atribuido à variavel conteudo
arq.close()                                               #Fecha o arquivo

while True:                                                           #Loop Infinito
  menu=int(input("(1)Para criptografar\n(2)Para descriptografar\n"))  #Menu para o Usuário escolher entre criptografar e descriptografar
  if menu==1:                                                         #Caso o usuário escolha Criptografar:
    key = Fernet.generate_key()                                       #Função para gerar uma chave
    print(f"Sua chave é: {key.decode('ascii')} guarde com segurança!")#Imprime a key formatada em ascii pois é do tipo byte
    key = Fernet(key)                                                 
    cript = key.encrypt(conteudo)                                     #Criptografa o conteudo com base na chave
    arq=open(arqinput,"wb")                                           #Abre o arquivo para escrita "w" de forma binária "b"
    arq.write(cript)                                                  #Escreve no arquivo o conteudo criptografado
    arq.close()                                                       #Fecha o arquivo
    print("Criptografado com sucesso!")
    break                                                             #Sai do Loop
  elif menu==2:                                                       #Caso ele escolha Descriptografar:
    key=input("Digite a sua key:")
    if len(key)!=44:
      menu=0                                                          #Programa entenderá como erro
    else:
      key = Fernet(key)                                              
      decript = key.decrypt(conteudo)                                 #Descriptografa o conteudo com base na chave
      arq=open(arqinput,"wb")                                         #Abre o arquivo para escrita "w" de forma binária "b"
      arq.write(decript)                                              #Escreve no arquivo o conteudo descriptografado
      arq.close()                                                     #Fecha o arquivo
      print("Descriptografado com sucesso!")
      break                                                           #Sai do Loop
  else:
    print("Opção inválida!")
