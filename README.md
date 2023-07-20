# Custom-Discord-RPC
Custom Discord Rich Presence made by Jimmy

I am not good at English, so I use Google Translate to translate some of the contents. 

## Introduction

Welcome to the Custom-Discord-RPC! This project provides a Discord Rich Presence implementation to make your Discord profile more eye-catching than others. Discord Rich Presence allows you to display customized game status and information on your Discord profile. This README will guide you through the setup and usage of the project in two different methods.

## Method 1: Using DiscordRPC.exe

1. Download the contents of the `DiscordRPC_EXE` directory from the repository.
2. Place all the downloaded files in a single folder on your local machine.
3. Open the `settings.json` file and update it with your desired settings, such as your Discord application's Client ID and other game details.
4. Save the `settings.json` file after making the necessary changes.
5. Run `DiscordRPC.exe` to execute the Discord Rich Presence application.
6. Your Discord profile will now show the custom status based on the settings in your `config.json` file when you are playing games or using the application.

## Method 2: Using install.bat and DiscordRPC.py

1. Download the contents of the `DiscordRPC` directory from the repository.
2. Place all the downloaded files in a single folder on your local machine.
3. Open the `settings.json` file and update it with your desired settings, such as your Discord application's Client ID and other game details.
4. Save the `settings.json` file after making the necessary changes.
5. Run `install.bat` to ensure all the required dependencies are installed.
6. After the installation is complete, you can now execute `DiscordRPC.py` to start the Discord Rich Presence application.
7. Your Discord profile will now display the custom status based on the settings in your `config.json` file when you are playing games or using the application.

## JSON Configuration

I will edit this later, please be patient.
```
{   
    "large_image": "your large image key",
    "large_text": "your large image text",
    "small_image": "your small image key",
    "small_text": "your small image text",
    "details": [
        "detail_1",
        "detail_2",
        "(you can add any details u want)"
    ],
    "state": "your state",
    "start": "0 or 1 or 2 or 3 or 4",
    "custom_time": "custom start time(Unix time)",
     definition: 為開始時間，例如假如把開始時間設在三個小時前，那麼你在動態中就會看到經過時間為03:00:00
     start=0: set to 0 -> current time
     start=1: set to 1 -> 程式執行時間
     start=2: set to 2 -> time since last status update
     start=3: set to 3 -> Custom time
     start=4: set to 4 -> None
     custom_time: 自訂時間(自1970/1/1 00:00:00到現在的秒數)
    "custom_end": "custom end time(Unix time)",
    "//end定義": "為結束時間，例如假如把開始時間設在三個小時後，那麼你在動態中就會看到剩餘時間為03:00:00  (請勿更改這行)",
    "//custom_end": "自訂時間(自1970/1/1 00:00:00到現在的秒數)  (請勿更改這行)",
    "party_size": "0 or 1 or 2",
    "custom_party_size_max": "party_size_max",
    "custom_party_size_current": "party_size_current",
    "//party_size定義": "為開始時間，例如假如把開始時間設在三個小時前，那麼你在動態中就會看到經過時間為03:00:00  (請勿更改這行)",
    "//party_size0": "設為0 -> 目標頻道的訂閱數和訂閱目標  (請勿更改這行)",
    "//party_size1": "設為1 -> 自訂  (請勿更改這行)",
    "//party_size2": "設為2 -> 無  (請勿更改這行)",
    "//custom_party_size_max": "party最大的大小，例如5代表party最多有五人",
    "//custom_party_size_current": "party目前的大小，例如3代表party目前有三人",
    "buttons": [
        {
            "label": "button_1",
            "url": "https://www.youtube.com/@JimmyXiaoXi?sub_confirmation=1"
        },{
            "label": "button_2",
            "url": "https://discord.gg/5UrGWXf3ba"
        }
    ],
    "reconnect_time": "10",
    "get_sub_time": "500",
    "update_statistics_time": "15",
    "get_current_time_delay": "1"
}
```
