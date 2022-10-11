import models.vk as VK
import models.yaDisk as YA


def main(vk, ya):
    print(
        f" Выберите одну из функций:\n 1 - сделать бэкап своих фотографий\n 2 - сделать бэкап фотографий друга\n q - для выхода")
    while True:
        auth_command = input("Введите команду:")
        if auth_command == '1':
            vk_version = VK.VK_API(vk)
            ya_version = YA.Ya_API(ya)
        elif auth_command == '2':
            print(
                'Вы знаете ID друга или хотите посмотреть список друзей и их ID?:\n1 - да, знаю\n2 - вывести список')
            friends_command = input("Введите команду:")
            if friends_command == '1':
                print("Введите ID друга:")
                _ID = input("Введите ID:")
                vk_version_test = VK.VK_API(vk)
                ID_list = ','.join([str(friend['id']) for friend in vk_version_test.friends()])
                if _ID in ID_list:
                    vk_version = VK.VK_API(vk, _ID)
                    ya_version = YA.Ya_API(ya)
                else:
                    print('Неверно указан ID или у вашего токена нет доступа к друзьям\n-----------------------')
                    return main(vk, ya)
            elif friends_command == '2':
                vk_version_test = VK.VK_API(vk)
                friends = vk_version_test.friends()
                friends = sorted(friends, key=lambda d: d['name'])
                print("-----------------------")
                for friend in friends:
                    print(f'{friend["name"]} - ID {friend["id"]}')
                print("-----------------------")
                print("Введите ID друга:")
                _ID = input("Введите ID:")
                ID_list = ','.join([str(friend['id']) for friend in friends])
                if _ID in ID_list:
                    vk_version = VK.VK_API(vk, _ID)
                    ya_version = YA.Ya_API(ya)
                    print(True)
                else:
                    print('Неверно указан ID или у вашего токена нет доступа к друзьям\n-----------------------')
                    return main(vk, ya)
        elif auth_command == 'q':
            break
        else:
            print("Данной команды не найдено\n-----------------------")
            return main(vk, ya)
        print(
            f" Выберите одну из функций:\n 1 - чтобы совершить бэкап фотографий профиля(аватарки)\n 2 - чтобы совершить бэкап фотографий из другого альбома")
        command = input("Введите команду:")
        if command == '1':
            print(f'Хотите выбрать количество загружаемых фото?\n 1 - да\n 2 - нет(по умолчанию-5)')
            command_lvl1 = input("Введите команду:")
            if command_lvl1 == '1':
                try:
                    command_lvl2 = input(f'Введите количество фото(всего {vk_version.get_photos()[1]}):')
                    if int(command_lvl2) in range(1, vk_version.get_photos()[1] + 1):
                        img_list = vk_version.get_photos()[0]
                        ya_version.vk_backup(img_list, count_img=int(command_lvl2))
                        print('-----------------------')
                        return main(vk, ya)
                    elif int(command_lvl2) > vk_version.get_photos()[1]:
                        print('Превышено число количества фотографий. Будут загружены все')
                        img_list = vk_version.get_photos()[0]
                        ya_version.vk_backup(img_list, count_img=int(command_lvl2))
                        print('-----------------------')
                        return main(vk, ya)
                except:
                    print('Введено некоректное значение\n-----------------------')
                    return main(vk, ya)
            elif command_lvl1 == '2':
                img_list = vk_version.get_photos()[0]
                ya_version.vk_backup(img_list)
                print('-----------------------')
                return main(vk, ya)
            else:
                print("Данной команды не найдено\n-----------------------")
                return main(vk, ya)
        elif command == '2':
            print('Выберите альбом для бэкапа и введите его ID:')
            album_list = vk_version.get_album_photo()
            album_list_id = []
            print("-----------------------")
            for album in album_list:
                print(f"Название альбома {album['name']} - ID Альбома {album['id']}")
                album_list_id.append(album['id'])
            print("-----------------------")
            try:
                command_lvl1 = input("Введите ID:")
                img_list = vk_version.get_photos(command_lvl1)[0]
                if int(command_lvl1) in album_list_id:
                    print(f'Хотите выбрать количество загружаемых фото?\n 1 - да\n 2 - нет(по умолчанию-5)')
                    command_lvl2 = input("Введите команду:")
                    if command_lvl2 == '1':
                        try:
                            command_lvl3 = input(
                                f'Введите количество фото(всего {vk_version.get_photos(command_lvl1)[1]}):')
                            if int(command_lvl3) in range(1, vk_version.get_photos(command_lvl1)[1]):
                                ya_version.vk_backup(img_list, path=f'{command_lvl1}/', count_img=int(command_lvl3))
                                print('-----------------------')
                                return main(vk, ya)
                            elif int(command_lvl3) > vk.get_photos(command_lvl1)[1]:
                                print('Превышено число количества фотографий. Будут загружены все')
                                ya_version.vk_backup(img_list, path=f'{command_lvl1}/', count_img=int(vk_version.get_photos(command_lvl1)[1]))
                                print('-----------------------')
                                return main(vk, ya)
                        except:
                            print('Введено некоректное значение\n-----------------------')
                            return main(vk, ya)
                    elif command_lvl2 == '2':
                        ya_version.vk_backup(img_list, path=f'{command_lvl1}/')
                        print('-----------------------')
                        return main(vk, ya)
                    else:
                        print("Данной команды не найдено\n-----------------------")
                        return main(vk, ya)
                else:
                    print("Данной команды не найдено\n-----------------------")
                    return main(vk, ya)
            except:
                print('Данного ID не обнаружено.\n-----------------------')
                return main(vk, ya)
        else:
            print("Данной команды не найдено\n-----------------------")
            return main(vk, ya)