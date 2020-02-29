import requests
from os import getenv as _

def handle(file):
  try:
    r = requests.post('https://www.yuque.com/api/upload/attach?ctoken=%s' % _('YUQUE_CTOKEN'), files={
      'file': ('image.png', open(file, 'rb'), 'image/png')
    }, headers={
      'Referer': 'https://www.yuque.com/yuque/topics/new',
      'Cookie': 'ctoken=%s; _yuque_session=%s' % (_('YUQUE_CTOKEN'), _('YUQUE_SESSION'))
    }).json()

    return r['data']['url']
  except:
    return None
