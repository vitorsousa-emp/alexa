import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import pywhatkit 

audio = sr.Recognizer() 
maquina = pyttsx3.init()
maquina.say('ola eu sou o sextafeira,')
maquina.say('como posso te ajudar')
maquina.runAndWait()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz,language='PT-BR')
            comando = comando.lower()
            if 'sextafeira' in comando:
                comando = comando.replace('sextafeira','')
                maquina.say(comando)
                maquina.say('como posso ajudar')
                maquina.runAndWait()
      
    except:
        maquina.say('microfone não ta legal')

    return comando

def comando_voz_usuario():   
    comando = executa_comando()

    if 'horas'in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('agora sâo' + hora) 
        maquina.runAndWait()

    elif ' procure '  in comando:
        procurar = comando.replace('procure','')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,1)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()

    elif 'toque'in comando:
        musica = comando.replace('play','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('tocando musica')
        maquina.runAndWait()

    elif 'repita' in comando:
            comando = comando.lower()
            print(comando)
            maquina.say(comando)
            maquina.runAndWait()

    elif 'comando' in comando:
        maquina.say('meus comandos são')
        maquina.say('que horas são , repetir frase , procurar algo e tocar música ')
        maquina.runAndWait()

    elif 'ligar ar da sala' in comando:
         maquina.say(" certo, ligando ar da sala")
         maquina.runAndWait()

    else:
        maquina.say('não estou aprendendo ainda')
        maquina.say('fale de acordo com os meus comandos')
        maquina.runAndWait()

comando_voz_usuario() 