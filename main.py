import vk_api
from config import login, password, id_page
vk_session = vk_api.VkApi(login, password)
vk_session.auth()

vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)
# print(vk.wall.post(message='Hello world!')) # сообщение
# vk.photo_wall(photos='photo.jpeg', user_id=524647441)
photo_wall = upload.photo_wall(photos='photo.jpeg', user_id=int(id_page))
owner_id = id_page
media_id = str(photo_wall[0]['id'])  # берем номер из массива полученного
attachments = 'photo' + owner_id + '_' + media_id

# vk.wall.post(owner_id = owner_id, from_group = 1, attachments = attachments)

vk_session.method("wall.post", {
    'owner_id': id_page,
    'message': 'Testing',
    'attachment': attachments,
})