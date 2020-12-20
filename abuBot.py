import subprocess
import os
import sys
import random
from random import randint
import telebot

bot = telebot.TeleBot("1480977235:AAFBHAHepFCV1g49HEQGd0G6CVutGQov_sQ")


@bot.message_handler(content_types=['text'])
def commands(message):

	try:
		spam = message.text
		spam_splitted = spam.split(" ", 1)
		spam_split = spam_splitted[0]
		nickname_split = spam_splitted[1]

	except Exception:
		pass

	if spam_split == "проспамь" or spam_split == "Проспамь": 
		for x in range(5):
			bot.send_message(message.chat.id, str(nickname_split))

	try:
		randomNumber = message.text
		randomNumberSplit = randomNumber.split(" ", 1)
		randomNumberSplitWord = randomNumberSplit[0]
		randomNumberOneToAnother = randomNumberSplit[1]
		randomNumberOneToAnotherSplitted = randomNumberOneToAnother.split("-", 1)
		randomNumberFirst = randomNumberOneToAnotherSplitted[0]
		randomNumberSecond = randomNumberOneToAnotherSplitted[1]

	except Exception:
		pass

	try:
		pollAbu = message.text
		pollAbuSplitted = pollAbu.split(" ## ", 5)
		abuQuestionCommand = pollAbuSplitted[0]
		questionPoll = pollAbuSplitted[1]
		option1 = pollAbuSplitted[2]
		option2 = pollAbuSplitted[3]
		option3 = pollAbuSplitted[4]
		option4 = pollAbuSplitted[5]

	except Exception:
		pass


	if abuQuestionCommand == "АБУвопрос":
		try:
			bot.send_poll(message.chat.id, questionPoll, [option1, option2, option3, option4])
			bot.delete_message(message.chat.id, message.message.id)
		except Exception:
			try:
				bot.send_poll(message.chat.id, questionPoll, [option1, option2, option3])
			except Exception:
				try:
					bot.send_poll(message.chat.id, questionPoll, [option1, option2])
				except Exception:
					bot.send_message(message.chat.id, "Задай минимум 2 ответа на твой вопрос или голосование!")

	elif randomNumberSplitWord == "рандом":
		bot.send_message(message.chat.id, str(randint(int(randomNumberFirst), int(randomNumberSecond))))


	elif message.text == "АУЕ" or message.text == "ауе" or message.text == "Ауе":
		bot.send_message(message.chat.id, "Жизнь ворам!")

	elif message.text == "Чёрт" or message.text == "чёрт":
		bot.send_message(message.chat.id, message.from_user.first_name + " не мороси лэээ")

	elif message.text == "Убить" or message.text == "убить":
		bot.send_message(message.chat.id, message.from_user.first_name + ", cлушай сюда внимательно! \nлевый коронный, правый похоронный!")

	elif message.text == "АУФ" or message.text == "ауф" or message.text == "Ауф":
		bot.send_message(message.chat.id, "Ай мама джан!\nВот какая доля воровская.\nИ теперь пишу тебе, родная, ай, мама джан")

	elif message.text == "БАНДИТ" or message.text == "бандит" or message.text == "Бандит":
		bot.send_message(message.chat.id, "ЖИЗНЬ ВОРАМ, СМЕРТЬ МУСОРАМ!")

	elif message.text == "Я спать" or message.text == "Спокойной ночи":
		bot.send_message(message.chat.id, "Сладких снов✨")

	elif message.text == "Зулик" or message.text == "зулик" or message.text == "ЗУЛИК":
		if message.from_user.id == 318495457:
			bot.send_message(message.chat.id, "Где этот #@?!*$")
		else:
			pass

	elif message.text == "Абу" or message.text == "абу" or message.text == "АБУ":
		bot.send_message(message.chat.id, "Агзымы ачма 🤬🤬🤬")

	elif message.text == "Абу кто я?" or message.text == "абу кто я?" or message.text == "абу кто я" or message.text == "Абу кто я":
		abuList = ["Ты АБУстраивающийся бомж", "Ты АБУчающийся трудовик", "Ты АБУвающийся Кямран", "Ты АБУздающий бандит", "Ты АБУза", "Ты АБУглённый кальян", "Ты красивая Абушница"]
		bot.reply_to(message, random.choice(abuList))

	elif message.text == "Абу скажи фразу" or message.text == "абу скажи фразу" or message.text == "абу скажи фразу!" or message.text == "Абу скажи фразу!" or message.text == "абу, скажи фразу" or message.text == "Абу, скажи фразу":
		abuPhrases = [
		"Тюрьма не школа - прокурор не учитель.",
		"Ворам - по масти, мусорам - по пасти!",
		"Перед людьми я виноват, перед богом чист.",
		"КРИКНИ ВОР - И Все ОБЕРНУТСЯ.....КРИКНИ - ЧЕЛОВЕК И НИКТО УХОМ НЕ ПОВЕДЕТ..",
		"Крови нет - менты попили.",
		'Я за любой кипиш кроме голодовки )))',
		"Лучше смерть от ножа, чем от руки правосудия!",
		"Свободу ворам! Смерть мусорам!",
		"Не спросил, а поинтересовался.",
		"Достал нож - режь.",
		"Старший сказал - младший сделал.",
		"Какая разница, кто какой национальности.",
		"Без оснований - не пререкайся.",
		"Не послушай, а выслушай.",
		"Ты шерсть, ты животное!"
		]
		bot.send_message(message.chat.id, random.choice(abuPhrases))

	elif message.text == "всем привет!" or message.text == "Всем привет!" or message.text == "всем привет" or message.text == "Всем привет" or message.text == "Привет всем" or message.text == "привет всем" or message.text == "Привет" or message.text == "привет":
		bot.send_message(message.chat.id, "Привет - привет! Как дела?")

	elif message.text == "Яхшы" or message.text == "яхшы":
		yaxshi = ["Хятдя гал...","Сян деянди...","Чохсагол","Мгм, велком ту америка"]
		bot.send_message(message.chat.id, random.choice(yaxshi))

	elif message.text == "АБУфункции" or message.text == "АБУкоманды":
		bot.send_message(message.chat.id,"Вот мои команды:\nАУЕ\nЧёрт\nУбить\nАУФ\nБандит\nпроспамь *предложение*\nЯ спать\nЗулик\nАбу\nАбу кто я?\nАбу скажи фразу\nПривет\nрандом *1 - 9999999999*\nЯхшы\nАбу, ты кто?")

	elif message.text == "Абу, ты кто?" or message.text == "абу, ты кто?" or message.text == "абу ты кто?" or message.text == "Абу ты кто?":
		abuNames = ["Называй меня как хочешь...", "Для тебя я Абу, остальные пусть не интересуются.", "Вор в законе", "Авара"]
		bot.send_message(message.chat.id, random.choice(abuNames))

	#elif message.text == "Ряван" or message.text == "ряван" or message.text == "Раван" or message.text == "раван" or message.text == "Рава" or message.text == "рава":
	#ravanList = ["Бабник", "Хырдабуйнуз", "Крыса", "Лжец!", "Трус"]
	#bot.send_message(message.chat.id,random.choice(ravanList))


	else:
		pass

bot.polling()