from pypresence import Presence
import time, requests, random, threading, json, os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def error_handler(error):
    print(f'{get_current_time()} [x] 發生錯誤，原因如下\n{get_current_time()} [x] {error}')
    print(f'{get_current_time()} [/] 系統將於10秒後重試')
    time.sleep(int(settings['reconnect_time']))

#程式執行時間
start_time = time.time()
      
while True:#無窮迴圈

  #取得現在時間
  def get_current_time():
      current_time = datetime.now()
      formatted_time = "{}/{}/{} {:02d}-{:02d}-{:02d}".format(
        current_time.year,
        current_time.month,
        current_time.day,
        current_time.hour,
        current_time.minute,
        current_time.second
)
      return formatted_time
  
  settings=''
  #讀取json檔案
  try:
    with open('settings.json', 'r', encoding='utf-8') as f:
      settings = json.load(f)
  except Exception as e:
    error_handler(e)

  #系統啟動中
  print(f'{get_current_time()} [/] 系統啟動中...')

  try:
    if os.getenv('youtube_api_key') != '' and os.getenv('youtube_channel_id') != '' and settings['party_size'] == '0':
      api_key = os.getenv('youtube_api_key')
      yt_channel_id = os.getenv('youtube_channel_id')

      path = f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={yt_channel_id}&key={api_key}'
      r = requests.get(path)
      data = r.json()
      subs = data['items'][0]['statistics']['subscriberCount']
      def next_greater_integer(number):
        return ((int(number) // 10) * 10 + 10)
      subgoal = int(next_greater_integer(subs))
    elif os.getenv('youtube_api_key') == '' or os.getenv('youtube_channel_id') == '' and settings['party_size'] == '0':
      print(f'{get_current_time()} [x] 無效的.env設定!，youtube_api_key或youtube_channel_id不可為空')

    #取得訂閱數
    def get_subs():
      #取得訂閱數
      r = requests.get(path)
      data = r.json()
      subs = data['items'][0]['statistics']['subscriberCount']
      #訂閱目標(55->60, 843->850)
      def next_greater_integer(number):
        return ((int(number) // 10) * 10 + 10)
      subgoal = int(next_greater_integer(subs))
      #列印訂閱數及目標
      print(f'{get_current_time()} [+] 目前你的訂閱數為{subs}人')
      print(f'{get_current_time()} [+] 你的訂閱目標為{subgoal}人')

    #更新狀態
    def update_statistics():
      # 獲取現在日期
      current_date = datetime.now().date()
      # 獲取今天0:00的時間
      today_time = datetime.combine(current_date, datetime.min.time())
      # 將時間轉換為秒數(epoch)
      epoch_time = int(today_time.timestamp())
      #隨機選擇一個detail
      details = settings['details']
      random_details = random.choice(details)

      #時間戳記判斷
      if settings['start'] != '' and settings['custom_end']!= '':
        start = None
        end = None
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的start和end不能同時使用')

      elif settings['start'] != '' and settings['custom_end'] == '':
        if settings['start'] == '0':
          start = epoch_time
        elif settings['start'] == '1':
          start = time.time()-start_time
        elif settings['start'] == '2':
          start = time.time()-update_time
        elif settings['start'] == '3':
          start = settings['custom_time']
        elif settings['start'] == '4' or settings['start'] == '':
          start = None
        else:
          start = None
          print(f'{get_current_time()} [x] 無效的json設定!，請檢查settings.json中的start數值')
        end = None

      elif settings['start'] == '' and settings['custom_end']!= '':
        end = settings['custom_end']
        start = None

      else:
        start = None
        end = None

      if settings['party_size'] == '0':
        party_size = [int(subs), int(subgoal)]
      elif settings['party_size'] == '1':
        party_size = [int(settings['custom_party_size_current']), int(settings['custom_party_size_max'])]
      elif settings['party_size'] == '2' or settings['party_size'] == '':
        party_size = None
      else:
        party_size = None
        print(f'{get_current_time()} [x] 無效的json設定!，請檢查settings.json中的party_size數值')

      if settings['state'] == '':
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的state不可為空')
      elif len(settings['state']) > 128:
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的state不可超過128字')

      if int(settings['reconnect_time']) < 0:
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的reconnect_time不可為負數')

      if int(settings['get_sub_time']) < 0:
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的get_sub_time不可為負數')
      
      if int(settings['update_statistics_time']) < 15:
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的update_statistics_time不可小於15秒')

      if int(settings['get_current_time_delay']) < 0:
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的get_current_time_delay不可為負數')

      def hasblank(list):
        return '' in list

      if len(settings['details']) < 1 or hasblank(settings['details']):
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的details內容不得小於一項或為空白')

      if settings['large_image'] != '' and settings['large_text'] == '':
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的large_text不可為空(因為你有使用large_image)')
      elif settings['large_image'] == '' and settings['large_text']!= '':
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的large_image不可為空(因為你有使用large_text)')
      elif settings['small_image'] != '' and settings['small_text'] == '':
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的small_text不可為空(因為你有使用small_image)')
      elif settings['small_image'] == '' and settings['small_text']!= '':
        print(f'{get_current_time()} [x] 無效的json設定!，settings.json中的small_image不可為空(因為你有使用small_text)')
        

      
      #更新狀態
      RPC.update(
        large_image=settings['large_image'],
        large_text=settings['large_text'],
        small_image=settings['small_image'],
        small_text=settings['small_text'],
        details=random_details,
        state=settings['state'],
        start=start,
        end=end,
        party_size=party_size,
        buttons=[{
          "label": "訂閱我的YT頻道",
          "url": "https://www.youtube.com/@JimmyXiaoXi?sub_confirmation=1"
        }, {
          "label": "加入我的DC伺服器",
          "url": "https://discord.gg/5UrGWXf3ba"
        }]  #最多兩個按鈕
      )
      #狀態切換通知
      print(f'{get_current_time()} [>] 狀態已切換成[{random_details}]')
      update_time = time.time()

    #連到你的Discord帳號
    discord_client_id = os.getenv('discord_client_id')
    RPC = Presence(discord_client_id)
    RPC.connect()

    #列印系統資訊
    print(f'{get_current_time()} [/] 已連接至你的Discord帳號')
    update_statistics_time = settings['update_statistics_time']
    print(f'{get_current_time()} [!] {update_statistics_time}秒後將會更新狀態資訊')
    get_sub_time = settings['get_sub_time']
    if settings['party_size'] == '0':
      print(f'{get_current_time()} [!] {get_sub_time}秒後將會更新訂閱資訊')

    #取得現在時間
    def get_current_time_thread():
       while True:
          try:
            get_current_time()
            time.sleep(int(settings['get_current_time_delay'])) 
          except Exception as e:
            error_handler(e)

    #取得訂閱數
    def get_subs_thread():
        while True:
          try:
            get_subs()
            time.sleep(int(settings['get_sub_time']))  # 冷卻500秒
          except Exception as e:
            error_handler(e)

    #更新狀態
    def update_statistics_thread():
        while True:
          try:
            update_statistics()
            time.sleep(int(settings['update_statistics_time']))  # Cooldown: 15 seconds
          except Exception as e:
            error_handler(e)

    # Start the threads
    get_subs_thread = threading.Thread(target=get_subs_thread)
    update_statistics_thread = threading.Thread(target=update_statistics_thread)
    get_current_time_thread = threading.Thread(target=get_current_time_thread)

    if settings['party_size'] == '0':
      get_subs_thread.start()
    update_statistics_thread.start()
    get_current_time_thread.start()

    # Join the threads to prevent the program from exiting prematurely
    if settings['party_size'] == '0':
      get_subs_thread.join()
    update_statistics_thread.join()
    get_current_time_thread.join()

  except Exception as e:
    error_handler(e)