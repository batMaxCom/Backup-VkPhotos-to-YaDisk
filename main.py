import models.vk as VK
import models.yaDisk as YA
from models.menu import main


def open_token(path):
    with open(path, 'r') as file:
        token = file.read().strip()
    return token

if __name__ == '__main__':

    vk_token = open_token('private/vk_token.txt')
    ya_token = open_token('private/ya_token.txt')


    vk_version = VK.VK_API(vk_token)
    ya_version = YA.Ya_API(ya_token)
    main(vk_version, ya_version)





