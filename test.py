import time

# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# timing = utc_timestamp_to_str(time.time()).split(' ')
# print(timing[0])


def change_person_status(person_stuatus):
    if person_stuatus == '跟踪中':
        person_stuatus = 1
    elif person_stuatus == '已撤控':
        person_stuatus = 0
    elif person_stuatus == 1:
        person_stuatus = '跟踪中'
    elif person_stuatus == 0:
        person_stuatus = '已撤控'
    return person_stuatus

# print(change_person_status(1))

from peewee import *
#db = MySQLDatabase('test', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'user': 'root', 'password': '\x16'})


db = MySQLDatabase('Face_Target', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'user': 'root', 'password': '\x16'})

class BaseModel(Model):
    class Meta:
        database = db


class FDevices(BaseModel):
    code = CharField(null=True)
    create_time = IntegerField(null=True)
    factory = CharField(null=True)
    groupid = IntegerField(null=True)
    ip = CharField(null=True)
    name = CharField(null=True)
    passwd = CharField(null=True)
    port = CharField(null=True)
    position = CharField(null=True)
    status = CharField(null=True)
    username = CharField(null=True)

    class Meta:
        table_name = 'devices'


class FAlarmlist(BaseModel):
    pic = CharField(null=True)  # 抓拍照片(全景)
    capture_id = IntegerField(null=True)
    person_id = IntegerField(null=False)
    threshold = FloatField(null=True)
    posttime = CharField(null=True)
    device = CharField(null=True) # 预警时间
    is_delete = CharField(column_name='isDelete', null=True)
    class Meta:
        table_name = 'f_alramlist'

class FReport(BaseModel):
    person_id = IntegerField(null=False)
    exam_result = CharField(column_name='examResult', null=True)
    exam_simple = CharField(column_name='examSimple', null=True)
    exam_standard = CharField(column_name='examStandard', null=True)
    card_type = CharField(column_name='cardType', null=True)
    reagent = CharField(null=True)
    posttime = CharField(null=True) #检测日期
    inspector = CharField(null=True) # 检测人
    is_delete = CharField(column_name='isDelete', null=True)
    class Meta:
        table_name = 'f_report'
class FRechecklist(BaseModel):
    person_id = IntegerField(null=False)
    recheck_time = CharField(column_name='recheckTime', null=True)
    recheck_institution = CharField(column_name='recheckInstitution', null=True)
    recheck_result = CharField(column_name='recheckResult', null=True)
    is_delete = CharField(column_name='isDelete', null=True)
    class Meta:
        table_name = 'f_rechecklist'

import socket
def get_host_ip_port():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('10.0.0.1',8080))
        ip= s.getsockname()[0]
        port = s.getsockname()[1]
    finally:
        s.close()
    return ip,port
def change_status(status):
    if status == '启用':
        status = 1
    elif status == "禁用":
        status = -1
    elif status == -1:
        status = '禁用'
    elif status == 1:
        status = '启用'
    return status
import requests
from PIL import Image
import io
import base64
def change_image(url):
    if "http" in url:
        re = requests.get(url)
        image = re.content
    else:
        f = open(url, "rb")
        image = f.read()
        f.close()
    image = Image.open(io.BytesIO(image))
    image = image.convert('RGB')
    rate = (1000 * 1000) / (image.size[0] * image.size[1])
    if rate < 1:
        image = image.resize((int(image.size[0] * 0.3), int(image.size[1] * 0.3)), Image.ANTIALIAS)
    output_buffer = io.BytesIO()
    image.save(output_buffer, format='JPEG')
    base64_data = base64.b64encode(output_buffer.getvalue())
    s = base64_data.decode()
    pic = f'data:image/jpg;base64,{s}'
    return pic
def get_feature(pic):
    try:
        pic_type = pic.split(".")[-1]
        f = open(pic, "rb")
        pic_data = f.read()
        base64_data = base64.b64encode(pic_data)
        s = base64_data.decode()
        re = requests.post("http://192.168.0.205:9998", json={
            "data": f"data:image/{pic_type};base64,{s}"
        })
        f.close()
        if re.json()["result"]:
            return re.json()["result"][0]
        return None
    except Exception as e:
        print(e)
        return None

def pic_to_url(filename):
    pic_url = config['FILE']['IP']  + filename
    return pic_url
def pic_to_url_xls(filename):
    pic_url = config['FILE']['IP']  + filename
    pic_xls = '=HYPERLINK(' + '"' + pic_url + '","' + pic_url + '")'
    return pic_xls
from PIL import ExifTags
def pic_correction(file):
    try:
        img = Image.open(config["FILE"]["PATH"] + file)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation': break
        exif = dict(img._getexif().items())
        if exif[orientation] == 3:
            img = img.rotate(180, expand=True)
        elif exif[orientation] == 6:
            img = img.rotate(270, expand=True)
        elif exif[orientation] == 8:
            img = img.rotate(90, expand=True)
        img.save(config["FILE"]["PATH"] + file)
        print(file)

    finally:
        return file
# 分页查询
def search_page(page,length):
    d = dd.select().get()
    find = dd.select().paginate(int(page), int(length))
    index = 0
    list = []
    while index < len(find):
        print(find[index].name)
        list.append(
            {'id': find[index].id, 'name': find[index].name,
             'create_time': find[index].create_time})
        index += 1
    print(list)
def check_data_new(data: dict, skip_key=None):
    if skip_key is None:
        skip_key = []
    status = True
    for k, v in data.items():
        if k in skip_key:
            if not v or not v.replace(" ", ""):
                status = False
                break
    return status


# 检索记录
class Searchlog():
    def get(self):
        datas = g.args
        print("人员列表", datas)
        data_list = FPersonnel.select().where(FPersonnel.cid != -2)
        if datas['keyword']:
            liker = f"%{datas['keyword']}%"
            data_list = data_list.where(FPersonnel.name % liker)
        if datas['times']:
            start, end = get_start_end_time(datas["times"])
            data_list = FPersonnel.select().where(FPersonnel.create_time.between(start, end))
        print("数据量", len(data_list))
        data_list = data_list.paginate(int(datas['page']), int(datas['size']))
        items = []
        for data in data_list:
            pic = pic_to_url(data.pic)
            result = {
                'id': str(data.id),
                'pic': pic,
                'name': str(data.name),

                'posttime': utc_timestamp_to_str(data.create_time),
                'IDCard': str(data.id_card),

                'faceimages': str(data.face_images) if FFaces.select().where(
                    FFaces.name == data.face_images).get().cid != -2 else '-'
            }
            items.append(result)
        print(items)

        msg = {'code': '0', 'msg': '查询成功', 'total': len(items), 'result': items}
        return msg, 200, None


if __name__=='__main__':
   a ='112a32'
   print(a.isnumeric())