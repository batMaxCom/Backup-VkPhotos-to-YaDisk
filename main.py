from private.user_data import user_id as user_id, vk_token as vk_token, ya_token as ya_token
import models.vk as VK
import models.yaDisk as YA
from models.menu import main



if __name__ == '__main__':
    vk_version = VK.VK_API(vk_token, user_id)
    ya_version = YA.Ya_API(ya_token)
    main(vk_version, ya_version)



# Желательно
# Сохранять фотографии и из других альбомов
# Сохранять фотографии на Google.Drive





