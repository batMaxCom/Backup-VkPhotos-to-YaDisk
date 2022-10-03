def main(vk, ya):
    print(
        f" Выберите одну из функций:\n 1 - чтобы совершить бэкап фотографий профиля(аватарки)\n 2 - чтобы совершить бэкап фотографий из другого альбома\n q - для выхода")
    while True:
        command = input("Введите команду:")
        if command == '1':
            print(f'Хотите выбрать количество загружаемых фото?\n 1 - да\n 2 - нет(по умолчанию-5)')
            command_lvl1 = input("Введите команду:")
            if command_lvl1 == '1':
                try:
                    command_lvl2 = input(f'Введите количество фото(всего {vk.get_photos()[1]}):')
                    if int(command_lvl2) in range(1, vk.get_photos()[1]):
                        img_list = vk.get_photos()[0]
                        ya.vk_backup(img_list, count_img=int(command_lvl2))
                        print('-----------------------')
                        return main(vk, ya)
                    elif int(command_lvl2) > vk.get_photos()[1]:
                        print('Превышено число количества фотографий. Будут загружены все')
                        img_list = vk.get_photos()[0]
                        ya.vk_backup(img_list, count_img=int(command_lvl2))
                        print('-----------------------')
                        return main(vk, ya)
                except:
                    print('Введено некоректное значение')
                    print('-----------------------')
                    return main(vk, ya)
            elif command_lvl1 == '2':
                img_list = vk.get_photos()[0]
                ya.vk_backup(img_list)
                print('-----------------------')
                return main(vk, ya)
            else:
                print("Данной команды не найдено")
                return main(vk, ya)

        elif command == '2':
            print('Выберите альбом для бэкапа и введите его ID:')
            album_list = vk.get_album_photo()
            album_list_id = []
            for album in album_list:
                print(f"Название альбома {album['name']} - ID Альбома {album['id']}")
                album_list_id.append(album['id'])
            try:
                command_lvl1 = input("Введите ID:")
                img_list = vk.get_photos(command_lvl1)[0]
                if int(command_lvl1) in album_list_id:
                    print(f'Хотите выбрать количество загружаемых фото?\n 1 - да\n 2 - нет(по умолчанию-5)')
                    command_lvl2 = input("Введите команду:")
                    if command_lvl2 == '1':
                        try:
                            command_lvl3 = input(f'Введите количество фото(всего {vk.get_photos(command_lvl1)[1]}):')
                            if int(command_lvl3) in range(1, vk.get_photos(command_lvl1)[1]):
                                ya.vk_backup(img_list, count_img=int(command_lvl3))
                                print('-----------------------')
                                return main(vk, ya)
                            elif int(command_lvl3) > vk.get_photos(command_lvl1)[1]:
                                print('Превышено число количества фотографий. Будут загружены все')
                                ya.vk_backup(img_list, count_img=int(vk.get_photos(command_lvl1)[1]))
                                print('-----------------------')
                                return main(vk, ya)
                        except:
                            print('Введено некоректное значение')
                            print('-----------------------')
                            return main(vk, ya)
                    elif command_lvl2 == '2':
                        ya.vk_backup(img_list)
                        print('-----------------------')
                        return main(vk, ya)
                    else:
                        print("Данной команды не найдено")
                        return main(vk, ya)
                else:
                    print("Данной команды не найдено")
                    return main(vk, ya)
            except:
                print('Данного ID не обнаружено.')
                print('-----------------------')
                return main(vk, ya)
        elif command == 'q':
            break
        else:
            print("Данной команды не найдено")
            return main(vk, ya)
