import speech_recognition as sr

filename = "audioO.wav"
output_file = "transcripcion_audioO.txt"

r = sr.Recognizer()

try:
    with sr.AudioFile(filename) as source:
        druation =int(source.DURATION)
        full_transcription = ""
        print("Procesando el archivo de audio...")
        for i in range(0, druation, 10):
            try: 
                audio_data = r.record(source, duration=10)
                text = r.recognize_google(audio_data, language="es-ES")
                full_transcription += text + "\n"
                print(f"Fragmento {i//10 + 1}: {text}")
            except sr.UnknownValueError:
                print(f"Fragmento {i//10 + 1}: No se pudo entender el audio.")
                full_transcription += "[No se pudo entender el audio]\n"
            except sr.RequestError as e:
                print(f"Error al solicitar resultados; {e}")
                break
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_transcription)
        print(f"Transcripción completa y guardada en {output_file}")

except FileNotFoundError:
    print(f"El archivo {filename} no se encontró. Asegúrate de que el archivo exista y que la ruta sea correcta.")
except ValueError as e:
    print(f"Error con el archivo de audio: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")