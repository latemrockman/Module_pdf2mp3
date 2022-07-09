from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def check_file(file_path):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        return True
    else:
        return False

def check_language(language):
    if language in ['ru', 'en']:
        return True
    else:
        return False

def extract_pdf(file_path):
    with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
        pages = [page.extract_text() for page in pdf.pages]

    file_name = Path(file_path).stem
    text = ''.join(pages)
    text = text.replace('\n', '')

    return [file_name, text]

def text_to_mp3(text, language='ru', name_mp3_file='text_voice'):
    my_audio = gTTS(text=text, lang=language, slow=False)
    my_audio.save(f'{name_mp3_file}.mp3')



def main():
    tprint('PDF-TO-MP3')

    while True:
        file_path = input('Введите путь к PDF файлу:\n')

        if check_file(file_path):
            print('Ok')
            break
        else:
            print('Подходящий файл не найден...')

    while True:
        language = input('Выберите язык "en" или "ru":\n')

        if check_language(language):
            print('Ok')
            break
        else:
            print('Ошибка, попробуйте еще раз!')

    name_mp3_file = extract_pdf(file_path=file_path)[0]
    text = extract_pdf(file_path=file_path)[1]

    print(f'Текст обрабатывается, подождите...')
    text_to_mp3(text=text, language=language, name_mp3_file=name_mp3_file)
    print(f'Готово, {name_mp3_file}.mp3 сохранён')





if __name__ == '__main__':
    main()