импортный  телебот
от  telebot  импортных  типов	
import  sys , os
импортировать  случайный

путь  =  sys . argv [ 1 ]
бот  =  telebot . TeleBot ( "1237408271: AAGvN7X_WLOrrr5-JWO00wJiTeQ5mDlV0I8" )

path_error_message  =  'Путь к папке указан неправильно. Попробуйте перезапустить скрипт и указать верный путь '

@ бот . message_handler ( команды = [ 'запуск' ])
def  start ( сообщение ):
	разметка  =  типы . ReplyKeyboardMarkup ()
	itembtn1  =  типы . KeyboardButton ( text = 'Получить' )
	разметки . добавить ( itembtn1 )
	бот . reply_to ( сообщение , 'Здравствуйте! Этот бот будет высылать Вам фото котеек)' , reply_markup = Разметка )

@ бот . обработчик сообщения ( func = лямбда-  сообщение : msg . text  ==  'Получить' )
def  send_something ( message ):
	попробуй :
		файлы  =  ОС . listdir ( путь = путь )
	кроме :
		печать ( path_error_message )
		бот . reply_to ( сообщение , path_error_message )
	выбор  =  случайный . выбор ( файлы )
	печать ( выбор )
	попробуй :
		если  путь [ - 1 ] ==  '/' :
			фото  =  открыть ( путь  +  выбор , 'рб' )
			бот . send_photo ( сообщение . чат . id , фото )
			возвращение
		фото  =  открыть ( путь  +  '/'  +  выбор , 'рб' )
		бот . send_photo ( сообщение . чат . id , фото )
	кроме :
		бот . send_photo ( message . chat . id , 'Упс .. что-то пошло не так .. Попробуйте перезапустить скрипт' )

бот . опрос ()
