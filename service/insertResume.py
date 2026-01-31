class InsertResume:

   @staticmethod

   def main(text):

    file_path = 'ui/transcrebe.txt'

    with open(file_path, 'w', encoding='utf-8') as f:

        f.write(text)

    print(f"Arquivo {file_path} salvo e formatado com sucesso!")