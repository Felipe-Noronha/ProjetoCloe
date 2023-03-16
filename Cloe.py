import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pywhatkit


texto_fala = pyttsx3.init()

def falar(audio):
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty('rate', 180)

    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice', voices[0].id) 

    texto_fala.say(audio)
    texto_fala.runAndWait()

def hora():
    Hora = datetime.datetime.now().strftime('%I:%M')
    falar('Agora são:')
    falar(Hora)

def data():
    ano = str(datetime.datetime.now().year)
    mes = str(datetime.datetime.now().month)
    dia = str(datetime.datetime.now().day)
    falar('A data atual é:')
    falar(dia + 'do' + mes + 'de' + ano)

def bem_vindo():
    horaAtual = datetime.datetime.now().hour

    if horaAtual >= 6 and horaAtual < 12:
        falar('bom dia mestre!')
    elif horaAtual >= 12 and horaAtual< 18:
        falar('boa tarde mestre!')
    elif horaAtual >=18 and horaAtual <=24:
        falar('boa noite mestre!')   

    else:
        falar('Boa madrugada!')

    falar('como posso ajuda-lo?')    

def microfone():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print('Reconhecendo...')    
        comando = r.recognize_google(audio,language='pt-BR')
        comando = comando.lower()
        
        if 'cloe' in comando:
            comando = comando.replace('cloe','')
            falar(comando)


    except Exception as e:
        print(e)
        falar('por favor repita!')

        return 'None'
    
    return comando    

def toque(musica):
    falar('tocando musica...')
    pywhatkit.playonyt(musica)

def pesquisar(algo):
    falar('pesquisando...')
    wikipedia.set_lang('pt')
    resultado = wikipedia.summary(algo,2)
    falar(resultado)


def executar_comando():
    bem_vindo()
    comando = microfone()

    if 'hora' in comando:
        hora()
    elif 'data' in comando:
        data()
    elif 'toque' in comando:
        toque(comando)
    elif 'pesquisar' in comando:
        pesquisar()    


executar_comando()         