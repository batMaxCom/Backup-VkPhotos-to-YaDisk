import time
from pprint import pprint
from private.user_data import user_id as user_id, vk_token as vk_token, ya_token as ya_token
import models.vk as VK
import models.yaDisk as YA



if __name__ == '__main__':
    vk_version = VK.VK_API(vk_token, user_id)
    img_list = vk_version.get_photos()

    ya_version = YA.Ya_API(ya_token)
    ya_version.vk_backup(img_list)



