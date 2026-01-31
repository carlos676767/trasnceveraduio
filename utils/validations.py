import re

def validacoes():

  try:
   


    url = input("Digite a url do video: ")

    if url == "":

        raise ValueError("Url inválida")


    regex = re.compile(

    r'^(https?:\/\/)'         

    r'(([\w-]+\.)+[\w-]{2,})'  

    r'(\/[\w\-._~:/?#[\]@!$&\'()*+,;=]*)?$',

    re.IGNORECASE)


    if not regex.match(url):

        raise ValueError("Url inválida")

        
    


    return url


  except Exception as e:

    print(e)
