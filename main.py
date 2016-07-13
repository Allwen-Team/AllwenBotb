#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
import sys
import redis as r
import os
reload(sys)
sys.setdefaultencoding("utf-8")
redis = r.StrictRedis(host='localhost', port=6379, db=0) # تنظیمات ردیس
bot = telebot.TeleBot('229556520:AAHmfZZ9mLOK0IKgT5Xxbhej8_lZuE-ntIA')
admin = '227014422'

@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker'])
def m(m):
    try:
        if m.chat.type == 'private':
            banlist = redis.sismember('banlist_pmbot', '{}'.format(m.from_user.id))
            if str(m.from_user.id) not in admin:
                if m.text == '/start' or m.text == '/help':
                    bot.send_message(m.chat.id, 'Hi!\nIm A ot For Recive Your Messages And Send To Allwen!\nSend Your Message!'
                    redis.sadd('member_pmbot', '{}'.format(m.from_user.id))
            elif str(m.from_user.id) not in admin:
                if str(banlist) == 'False':
                    if m.photo:
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'Send To Allwen �')
                    if m.text:
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'Send To Allwen �')
                    if m.document:
                        file_id = m.document.file_id
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'Send To Allwen �')
                    if m.sticker:
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'Send To Allwen �')
                    if m.audio:
                        file_id = m.audio.file_id
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'Send To Allwen �'
                    if m.contact:
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'Send To Allwen �'
        if str(m.from_user.id) == admin:
            if m.reply_to_message:
                if not m.text == '/ban':
                    if not m.text == '/unban':
                        if m.reply_to_message.text:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'Send To Allwen �'))
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'Send To Allwen �'))
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'Send To Allwen �'))
                        if m.reply_to_message.photo:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'Send To Allwen �'))
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'Send To Allwen �')
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'Send To Allwen �')
                        if m.reply_to_message.contact:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'Send To Allwen 👤')
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'Send To Allwen 👤')
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'Send To Allwen 👤')
                        if m.reply_to_message.sticker:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'Send To Allwen 👤')
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'Send To Allwen 👤')
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'Send To Allwen 👤')
                        if m.reply_to_message.document:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'Send To Allwen 👤')
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'Send To Allwen 👤')
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'اSend To Allwen)
                        if m.reply_to_message.audio:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'Send To Allwen 👤')
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'Sent To Allwen 👤')
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'Send To Allwen 👤')
        if str(m.from_user.id) == admin:
            if m.text == '/ban':
                ids = m.reply_to_message.forward_from.id
                redis.sadd('banlist_pmbot',ids)
                bot.send_message(ids, '<code>You re Blocked/code>',parse_mode='HTML')
                bot.send_message(admin, '#DONE')
            if m.text == '/unban':
                ids = m.reply_to_message.forward_from.id
                redis.srem('banlist_pmbot',ids)
                bot.send_message(ids, 'You Removed From Banlist
                bot.send_message(admin, '#DONE)
            if m.text == '/stats':
                msm = redis.scard('member_pmbot')
                bot.send_message(m.chat.id, 'Users : <code>{}</code>'.format(msm),parse_mode='HTML')
            if m.text == '/banlist':
                banliss = redis.scard('banlist_pmbot')
                bot.send_message(m.chat.id, '<b>{}</b>\nSend command for delete ban list\n/clean banlist'.format(banliss), parse_mode='HTML')
            if m.text == '/clean banlist':
                redis.delete('banlist_pmbot')
                bot.send_message(m.chat.id, '#DONE)
            if m.text == '/help' or m.text == '/start':
                bot.send_message(admin, """
/ban
Ban By Reply
/unban
DelBan By reply
/stats
Users
/banlist
BanList
/clean basnlist
Cleans Ban List
                """)
    except:
        bot.send_message(m.chat.id, 'Error')

bot.polling(True)
#end 150 line by negative
