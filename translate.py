import requests
import os.path
import glob

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

os.chdir('source')

print('\n' + 'Перечень подготовленных для перевода файлов:' + '\n')
files = glob.glob(os.path.join("*.txt"))
for file in files:
    print(os.path.basename(file))
print('\n')

os.chdir('..')

file = input('Для перевода содержимого в файле текста,' + '\n' + 'введите, пожалуйста, его имя: ')
if file in files:
    pass
else:
    while file not in files:
        file = input('\n' + 'Имя файла было указано неверно.' + '\n' + 'Пожалуйста, повторите попытку : ')
print('\n' + 'Имя выбранного файла: ' + file + '\n')



print('Код: язык')
languages = {
    'az' : 'азербайджанский',
    'sq' : 'албанский',
    'en' : 'английский',
    'ar' : 'арабский',
    'hy' : 'армянский',
    'af' : 'африканский',
    'be' : 'белорусский',  
    'bg' : 'болгарский',     
    'hu' : 'венгерский',  
    'vi' : 'вьетнамский',  
    'nl' : 'голландский',
    'el' : 'греческий',
    'ka' : 'грузинский',
    'da' : 'датский',  
    'he' : 'иврит',
    'id' : 'индонезийский',
    'ga' : 'ирландский',  
    'it' : 'итальянский',
    'is' : 'исландский',  
    'es' : 'испанский',
    'kk' : 'казахский',  
    'kn' : 'каннада',   
    'zh' : 'китайский',  
    'ko' : 'корейский',
    'lv' : 'латышский',  
    'lt' : 'литовский',  
    'mk' : 'македонский',
    'mn' : 'монгольский',
    'de' : 'немецкий',
    'no' : 'норвежский',
    'fa' : 'персидский',
    'pl' : 'польский',
    'pt' : 'португальский',
    'ro' : 'румынский',
    'ru' : 'русский',
    'sr' : 'сербский',
    'sk' : 'словацкий',
    'sl' : 'словенский',
    'tg' : 'таджикский',
    'tt' : 'татарский',
    'tr' : 'турецкий',
    'uk' : 'украинский',
    'fi' : 'финский',
    'fr' : 'французский',
    'hr' : 'хорватский',
    'cs' : 'чешский',
    'sv' : 'шведский',
    'gd' : 'шотландский',
    'et' : 'эстонский',
    'ja' : 'японский'
}

for key in sorted(languages.keys()):
    print(key + " : " + languages[key])

set_of_languages = set(languages)
lang = input('\n' + 'С выше перечисленных языков выбирите тот,' + '\n' + 'с которого будет осуществляться перевод: ')
if lang in set_of_languages:
    pass
else:
    while lang not in set_of_languages:
        lang = input('\n' + 'Код языка был указан неверно.' + '\n' + 'Пожалуйста, повторите попытку : ')

print('Код: язык')
for key in sorted(languages.keys()):
    print(key + " : " + languages[key])
set_of_languages = set(languages)
to_lang = input('\n' + 'С выше перечисленных языков выбирите тот,' + '\n' + 'на который будет осуществляться перевод: ')
if to_lang in set_of_languages:
    pass
else:
    while to_lang not in set_of_languages:
        to_lang = input('\n' + 'Код языка был указан неверно.' + '\n' + 'Пожалуйста, повторите попытку : ')


path_source = 'source'
path_result = 'result'
file = os.path.join(path_source, file)
with open(file) as text:
    pass



def translate_it(text, lang, to_lang, path_source, path_result):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': lang-to_lang.format(to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

print(translate_it(text, to_lang, path_source, path_result, 'ru'))

requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))