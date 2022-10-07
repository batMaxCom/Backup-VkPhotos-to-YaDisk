from models.menu import main


def open_token(path):
    with open(path, 'r') as file:
        token = file.read().strip()
    return token


if __name__ == '__main__':
    vk_token = open_token('private/vk_token.txt')
    ya_token = open_token('private/ya_token.txt')
    main(vk_token, ya_token)
