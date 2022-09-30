def main(vk, ya):
    print(
        f" Выберите одну из функций:\n 1 - чтобы совершить бэкап фотографий профиля\n 2 - чтобы совершить бэкап фотографий из другого альбома\n q - для выхода")
    while True:
        command = input("Введите команду:")
        if command == '1':
            print(f" На какой сервис вы хотите загрузить фото:\n 1 - YaDisk ;\n 2 - GoogleDrive;")
            command_lvl2 = input("Введите команду:")
            if command_lvl2 == '1':
                print(f'Хотите выбрать количество загружаемых фото?\n 1 - да\n 2 - нет(по умолчанию-5)')
                command_lvl3 = input("Введите команду:")
                if command_lvl3 == '1':
                    command_lvl4 = input('Введите количество фото:')
                    img_list = vk.get_photos()
                    ya.vk_backup(img_list, count_img=int(command_lvl4))
                    break
                elif command_lvl3 == '2':
                    img_list = vk.get_photos()
                    ya.vk_backup(img_list)
                break
            elif command_lvl2 == 'b':
                print('Операция по бэкапу')
                break
        elif command == '2':
            print('Операция по бэкапу')
            break
        elif command == 'q':
            break
        else:
            print("Данной команды не найдено")