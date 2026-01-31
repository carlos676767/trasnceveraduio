# Neural Engine Transcribe • v1.0 🎙️

Este projeto é uma ferramenta avançada de automação para transcrição de áudio e geração de resumos inteligentes utilizando as APIs do **Whisper** (OpenAI) e **Gemini** (Google).

## 📋 Funcionalidades

- **Download Automático**: Baixa o áudio de vídeos através de URLs (Instagram, YouTube, etc) usando `yt-dlp`.
- **Validação de URL**: Verifica se a URL inserida é válida antes de iniciar o processo.
- **Transcrição de Alta Precisão**: Utiliza o modelo `whisper` (medium) para converter fala em texto em português.
- **Resumo com IA**: Processa a transcrição com o modelo `gemini-3-flash` para criar resumos e corrigir erros gramaticais.
- **Interface Visual**: Banner ASCII personalizado para uma experiência de terminal premium.

---

## 🚀 Como Usar - Passo a Passo

### 1. Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina e as seguintes ferramentas:
- **FFmpeg**: Necessário para o processamento de áudio pelo `yt-dlp`.
- **Chave de API do Gemini**: Obtenha em [Google AI Studio](https://aistudio.google.com/).

### 2. Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione sua chave do Gemini:
```env
gemini=SUA_CHAVE_AQUI
```

### 3. Instalação de Dependências

Abra o terminal na pasta do projeto e instale as bibliotecas necessárias:
```bash
pip install whisper yt-dlp google-genai python-dotenv openai-whisper
```

### 4. Execução do Script

Para iniciar o programa, execute o arquivo principal:
```bash
python app.py
```

### 5. Processo de Transcrição

1.  **Banner**: O programa iniciará exibindo o banner "NEURAL ENGINE TRANSCRIBE".
2.  **Input**: Digite a URL do vídeo que deseja transcrever quando solicitado: `Digite a url do video:`.
3.  **Download**: O sistema baixará o áudio e salvará na pasta `audio/audio_baixado.m4a`.
4.  **Transcrição**: O Whisper processará o áudio (isso pode levar alguns instantes dependendo do tamanho do vídeo).
5.  **IA & Resumo**: O texto transcrito será enviado ao Gemini para gerar o resumo.
6.  **Resultado**: O resultado final (transcrição corrigida e resumo) será salvo automaticamente em `ui/transcrebe.txt`.

---

## 🏗️ Estrutura do Projeto

- `app.py`: Ponto de entrada do script.
- `service/`:
    - `Downloader.py`: Gerencia o download do áudio.
    - `wisper.py`: Gerencia a transcrição com Whisper.
    - `Gemini.py`: Integração com a IA do Google.
    - `insertResume.py`: Salva o resultado final no arquivo de texto.
- `ui/`:
    - `banner.py`: Contém a interface visual ASCII.
    - `transcrebe.txt`: Local onde o resultado é armazenado.
- `utils/`:
    - `validations.py`: Contém a lógica de validação de URLs.

---

## ⚠️ Observações

- O modelo `medium` do Whisper exige um pouco mais de processamento. Caso queira algo mais rápido, você pode alterar para `base` ou `tiny` no arquivo `service/wisper.py`.
- Certifique-se de que a pasta `audio/` exista no diretório raiz para evitar erros de salvamento.
