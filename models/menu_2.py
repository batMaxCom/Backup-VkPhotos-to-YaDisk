import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox

import models.vk as VK
import models.yaDisk as YA


def open_token(path):
    with open(path, 'r') as file:
        token = file.read().strip()
    return token


vk_token = open_token('private/vk_token.txt')
ya_token = open_token('private/ya_token.txt')


def main():
    window.mainloop()



def get_friends(vk=vk_token):
    vk_get_friends = VK.VK_API(vk)
    friends = vk_get_friends.friends()
    friends = sorted(friends, key=lambda d: d['name'])
    list_full = [{'name': 'Свои фото', 'id': []}]
    for friend in friends:
        list_full.append({'name': friend['name'], 'id': friend['id']})
    return list_full


def get_album(vk=vk_token, id=''):
    user = '{}'.format(com_friends.get())
    if user == '':
        pass
    else:
        id = [u['id'] for u in friends_list if u['name'] == user]
    vk_get_album = VK.VK_API(vk, id)
    album_list = vk_get_album.get_album_photo()
    album_list_second.clear()
    album_list_second.append({'name': 'Фото профиля', 'id': 'profile'})
    for album in album_list:
        album_list_second.append({'name': album['name'], 'id': album['id']})

    com_album.configure(values=','.join((str(album['name']) for album in album_list_second)).split(','))
    com_album.current(0)
    ent_count.delete(0, 'end')




def all_img(vk=vk_token):
    user = '{}'.format(com_friends.get())
    id = [u['id'] for u in friends_list if u['name'] == user]
    album = '{}'.format(com_album.get())
    album_id = [a['id'] for a in album_list_second if a['name'] == album]
    vk_version = VK.VK_API(vk, id)
    count = vk_version.get_photos(album_id=album_id)[1]
    ent_count.delete(0, 'end')
    ent_count.insert(0, count)


def upload(vk=vk_token, ya=ya_token):
    user = '{}'.format(com_friends.get())
    id = [u['id'] for u in friends_list if u['name'] == user]
    album = '{}'.format(com_album.get())
    album_id = [a['id'] for a in album_list_second if a['name'] == album]
    if album_id == []:album_id = 'profile'
    count = '{}'.format(ent_count.get())
    ya_version = YA.Ya_API(ya)
    vk_version = VK.VK_API(vk, id)
    try:
        if True:
            img_list = vk_version.get_photos(album_id=album_id)[0]
    except:
        messagebox.showinfo("Уведомление", 'Профиль и альбом не совпадают\nУбедитесь, что после смены профиля вы обновили альбомы.')
        return main()
    album_count_img = vk_version.get_photos()[1]
    try:
        if count == '':
            messagebox.showinfo("Уведомление", 'Вы не введи количество фото')
            return main()
        elif int(count) in range(1, album_count_img):
            pass
        elif int(count) > album_count_img:
            count = album_count_img
            msg = messagebox.askyesno("Уведомление", "Вы указали больше фотографий, чем есть в альбоме.\nБудут загружены все. Вы согласны?")
            if msg == True:
                count = album_count_img
            else:
                return main()
    except:
        messagebox.showinfo("Уведомление", 'Вы ввели некорректное значение')
        return main()
    ya_version.vk_backup(img_list=img_list, count_img=int(count))
    return main()



window = tk.Tk()
window.title("VK Backup")
window.geometry('600x200')
window.resizable(False, False)

friends_list = get_friends()
album_list_second = []

lbl_info = tk.Label(text='Вы хотите сделать бэкап фото?\nЗаполните поля ниже', font=("TimesNewRoman", 14))
lbl_info.grid(column=1, row=0)
lbl_ID_friend = tk.Label(text='Пользователь:', font=("TimesNewRoman", 12))
lbl_ID_friend.grid(column=0, row=1, sticky='w')
lbl_ID_album = tk.Label(text='Альбом:', font=("TimesNewRoman", 12))
lbl_ID_album.grid(column=0, row=2, sticky='w')
lbl_count_img = tk.Label(text='Количество фото:', font=("TimesNewRoman", 12))
lbl_count_img.grid(column=0, row=3, sticky='w')
lbl_fr = tk.Label(text='', font=("TimesNewRoman", 12))
lbl_fr.grid(column=0, row=4)

ent_count = tk.Entry(window, width=43)
ent_count.grid(column=1, row=3)

com_friends = Combobox(window, width=40, state="readonly", postcommand=get_album)
com_friends['values'] = ','.join([str(friend['name']) for friend in friends_list]).split(',')
com_friends.current(0)

com_friends.grid(column=1, row=1)
com_album = Combobox(window, width=40, state="readonly", postcommand=get_album)
get_album()
com_album.current(0)
com_album.grid(column=1, row=2)


# btn_album = tk.Button(window, width=20, text="Обновить альбомы!", command=lambda: get_album())
# btn_album.grid(column=2, row=2)
btn_album = tk.Button(window, width=20, text="Все фото!", command=all_img)
btn_album.grid(column=2, row=3)
btn_upload = tk.Button(window, width=30, height=2, text="Загрузить", command=upload)


btn_upload.grid(column=1, row=5)

btn_clear = tk.Button(window, width=20, height=2, text="Выход", command=exit)
btn_clear.grid(column=2, row=5)

com_friends.focus()

