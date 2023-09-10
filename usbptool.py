import urllib.request
from colorama import Fore
import os
import win32api
from ctypes import *
from time import sleep
import zipfile
import shutil
from win32com.client import Dispatch
from pyunpack import Archive


def myFmtCallback(command, modifier, arg):
    #print(command)
    return 1    # TRUE

def format_drive(Drive, Format, Title):
    fm = windll.LoadLibrary('fmifs.dll')
    FMT_CB_FUNC = WINFUNCTYPE(c_int, c_int, c_int, c_void_p)
    FMIFS_HARDDISK = 0
    fm.FormatEx(c_wchar_p(Drive), FMIFS_HARDDISK, c_wchar_p(Format),
                c_wchar_p(Title), True, c_int(0), FMT_CB_FUNC(myFmtCallback))

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\00')[:-1]
version = "v1.0.0"
print(Fore.RESET + "  _    _  _____ ____  _____ _______          _ ")
print(" | |  | |/ ____|  _ \|  __ \__   __|        | |")
print(" | |  | | (___ | |_) | |__) | | | ___   ___ | |")
print(" | |  | |\___ \|  _ <|  ___/  | |/ _ \ / _ \| |")
print(" | |__| |____) | |_) | |      | | (_) | (_) | |")
print("  \____/|_____/|____/|_|      |_|\___/ \___/|_|")
print(Fore.CYAN + "Welcome to USBPTool " + version + "!")
print(" ")
print(Fore.RESET + "Please select a external drive. (DO NOT CHOOSE YOUR MAIN DRIVE.)")
print(drives)
drivesel = input(Fore.GREEN + "Type in drive letter: ")
drivesel.upper()

if not os.path.exists(drivesel + r":\appdata"):
    print(Fore.YELLOW + "WARNING : No USBPTool data files!")
    confirmfolderc = input(Fore.GREEN + "Would you like to create folder? (Y/N): ").upper()
    if confirmfolderc == "Y":
        confirmformat = input(Fore.RED +"!! Would you like to format drive? (Y/N): ").upper()
        if confirmformat == "Y":
            format_drive(drivesel + ":\\", "NTFS", "USBPTool")
            print(Fore.GREEN + "Format success.")
            print(Fore.CYAN + "Making folders..")
            sleep(2)
            os.mkdir(drivesel + r":\appdata")
            os.mkdir(drivesel + r":\programs")
            os.mkdir(drivesel + r":\temp")
            print(Fore.GREEN + "Success. Rerun program.")
            sleep(5)
        else:
            print(Fore.CYAN + "Making folders..")
            sleep(2)
            os.mkdir(drivesel + r":\appdata")
            os.mkdir(drivesel + r":\programs")
            os.mkdir(drivesel + r":\temp")
            print(Fore.GREEN + "Success.")
else:
    while True:
        print(Fore.CYAN + "Select app to download")
        print(Fore.RESET + "[0]: Exit \n[1]: Revo Uninstaller \n[2]: Ventoy \n[3]: AIMP \n[4]: Odin3\n[5]: MiFlash tool\n[6]: Ungoogled Chromium\n[98]: Wipe USB\n[99]: Wipe Temp")
        appinput = input(Fore.CYAN + "Type in app number: ")
        match appinput:
            case "0":
                break
            case "1":
                url1 = 'https://download.revouninstaller.com/download/RevoUninstaller_Portable.zip'
                print(Fore.CYAN + "Downloading...")
                urllib.request.urlretrieve(url1, drivesel + r":\temp\revo.zip")
                print(Fore.GREEN + "Downloaded file.")
                os.mkdir(drivesel + r":\temp\revotemp")
                with zipfile.ZipFile(drivesel + ":\\temp\\revo.zip", 'r') as zip:
                    zip.extractall(drivesel + r":\temp\revotemp")
                print(Fore.GREEN + "Extracted file.")
                shutil.move(drivesel + r":\temp\revotemp\RevoUninstaller_Portable", drivesel + r":\appdata")
                print(Fore.GREEN + "Moved file to appdata.")
                shell = Dispatch('WScript.Shell')
                shortcut = shell.CreateShortCut(drivesel + r":\programs\Revo Uninstaller.lnk")
                shortcut.Targetpath = drivesel + r":\appdata\RevoUninstaller_Portable\RevoUPort.exe"
                shortcut.save()
                print(Fore.GREEN + "Successfully installed app.")
                print(Fore.RESET + "It is reccomended to wipe temp after install.")
            case "2":
                url2 = "https://objects.githubusercontent.com/github-production-release-asset-2e65be/246335987/c7e7b1a0-e6bf-457e-98d4-5bcf5d9da8f3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230910%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230910T103608Z&X-Amz-Expires=300&X-Amz-Signature=467565345e2793c5c5894d290763d3166fc212b83850024a7dfc782c13b405b5&X-Amz-SignedHeaders=host&actor_id=135747967&key_id=0&repo_id=246335987&response-content-disposition=attachment%3B%20filename%3Dventoy-1.0.95-windows.zip&response-content-type=application%2Foctet-stream"
                print(Fore.CYAN + "Downloading...")
                urllib.request.urlretrieve(url2, drivesel + r":\temp\ventoy.zip")
                print(Fore.GREEN + "Downloaded file.")
                os.mkdir(drivesel + r":\temp\ventoytemp")
                with zipfile.ZipFile(drivesel + ":\\temp\\ventoy.zip", 'r') as zip:
                    zip.extractall(drivesel + r":\temp\ventoytemp")
                print(Fore.GREEN + "Extracted file.")
                shutil.move(drivesel + r":\temp\ventoytemp\ventoy-1.0.95", drivesel + r":\appdata")
                print(Fore.GREEN + "Moved file to appdata.")
                shell = Dispatch('WScript.Shell')
                shortcut = shell.CreateShortCut(drivesel + r":\programs\Ventoy.lnk")
                shortcut.Targetpath = drivesel + r":\appdata\ventoy-1.0.95\Ventoy2Disk.exe"
                shortcut.save()
                print(Fore.GREEN + "Successfully installed app.")
                print(Fore.RESET + "It is reccomended to wipe temp after install.")
            case "3":
                url3 = "https://aimp.ru/files/windows/builds/aimp_5.11.2435_w64_no-installer.zip"
                print(Fore.CYAN + "Downloading...")
                urllib.request.urlretrieve(url3, drivesel + r":\temp\aimp.zip")
                print(Fore.GREEN + "Downloaded file.")
                os.mkdir(drivesel + r":\temp\aimptemp")
                with zipfile.ZipFile(drivesel + ":\\temp\\aimp.zip", 'r') as zip:
                    zip.extractall(drivesel + r":\temp\aimptemp")
                print(Fore.GREEN + "Extracted file.")
                shutil.move(drivesel + r":\temp\aimptemp\AIMP", drivesel + r":\appdata")
                print(Fore.GREEN + "Moved file to appdata.")
                shell = Dispatch('WScript.Shell')
                shortcut = shell.CreateShortCut(drivesel + r":\programs\AIMP.lnk")
                shortcut.Targetpath = drivesel + r":\appdata\AIMP\AIMP.exe"
                shortcut.save()
                print(Fore.GREEN + "Successfully installed app.")
                print(Fore.RESET + "It is reccomended to wipe temp after install.")
            case "4":
                url4 = "https://odindownload.com/download/Odin3_v3.14.4.zip"
                print(Fore.CYAN + "Downloading...")
                urllib.request.urlretrieve(url4, drivesel + r":\temp\odin3.zip")
                print(Fore.GREEN + "Downloaded file.")
                os.mkdir(drivesel + r":\temp\odintemp")
                with zipfile.ZipFile(drivesel + ":\\temp\\odin3.zip", 'r') as zip:
                    zip.extractall(drivesel + r":\temp\odintemp")
                print(Fore.GREEN + "Extracted file.")
                shutil.move(drivesel + r":\temp\odintemp\Odin3_v3.14.4", drivesel + r":\appdata")
                print(Fore.GREEN + "Moved file to appdata.")
                shell = Dispatch('WScript.Shell')
                shortcut = shell.CreateShortCut(drivesel + r":\programs\Odin3.lnk")
                shortcut.Targetpath = drivesel + r":\appdata\Odin3_v3.14.4\Odin3_v3.14.4.exe"
                shortcut.save()
                print(Fore.GREEN + "Successfully installed app.")
                print(Fore.RESET + "It is reccomended to wipe temp after install.")
            case "5":
                url5 = "https://xiaomiflashtool.com/wp-content/uploads/MiFlash20220507.zip"
                print(Fore.CYAN + "Downloading...")
                urllib.request.urlretrieve(url5, drivesel + r":\temp\miflash.zip")
                print(Fore.GREEN + "Downloaded file.")
                os.mkdir(drivesel + r":\temp\miflashtemp")
                with zipfile.ZipFile(drivesel + ":\\temp\\miflash.zip", 'r') as zip:
                    zip.extractall(drivesel + r":\temp\miflashtemp")
                print(Fore.GREEN + "Extracted file.")
                shutil.move(drivesel + r":\temp\miflashtemp\MiFlash20220507", drivesel + r":\appdata")
                print(Fore.GREEN + "Moved file to appdata.")
                shell = Dispatch('WScript.Shell')
                shortcut = shell.CreateShortCut(drivesel + r":\programs\MiFlash.lnk")
                shortcut.Targetpath = drivesel + r":\appdata\MiFlash20220507\XiaoMiFlash.exe"
                shortcut.save()
                print(Fore.GREEN + "Successfully installed app.")
                print(Fore.RESET + "It is reccomended to wipe temp after install.")
            case "6":
                url6 = "https://github.com/portapps/ungoogled-chromium-portable/releases/download/115.0.5790.131-16/ungoogled-chromium-portable-win64-115.0.5790.131-16.7z"
                print(Fore.CYAN + "Downloading...")
                urllib.request.urlretrieve(url6, drivesel + r":\temp\chromium.7z")
                print(Fore.GREEN + "Downloaded file.")
                os.mkdir(drivesel + r":\temp\chromiumtemp")
                Archive(drivesel + r":\temp\chromium.7z").extractall(drivesel + r":\temp\chromiumtemp")
                print(Fore.GREEN + "Extracted file.")
                shutil.move(drivesel + r":\temp\chromiumtemp", drivesel + r":\appdata")
                print(Fore.GREEN + "Moved file to appdata.")
                shell = Dispatch('WScript.Shell')
                shortcut = shell.CreateShortCut(drivesel + r":\programs\Chromium.lnk")
                shortcut.Targetpath = drivesel + r":\appdata\chromiumtemp\ungoogled-chromium-portable.exe"
                shortcut.save()
                print(Fore.GREEN + "Successfully installed app.")
                print(Fore.RESET + "It is reccomended to wipe temp after install.")
            case "7":
                url7 = "https://www.diskgenius.com/dyna_download/?iswinpe=true&software=DGEng5511508_x64.zip"
                print(Fore.CYAN + "Downloading...")
                urllib.request.urlretrieve(url7, drivesel + r":\temp\diskgenius.zip")
                print(Fore.GREEN + "Downloaded file.")
                os.mkdir(drivesel + r":\temp\diskgeniustemp")
                with zipfile.ZipFile(drivesel + ":\\temp\\diskgenius.zip", 'r') as zip:
                    zip.extractall(drivesel + r":\temp\diskgeniustemp")
                print(Fore.GREEN + "Extracted file.")
                shutil.move(drivesel + r":\temp\diskgeniustemp\DiskGenius", drivesel + r":\appdata")
                print(Fore.GREEN + "Moved file to appdata.")
                shell = Dispatch('WScript.Shell')
                shortcut = shell.CreateShortCut(drivesel + r":\programs\DiskGenius.lnk")
                shortcut.Targetpath = drivesel + r":\appdata\DiskGenius\DiskGenius.exe"
                shortcut.save()
                print(Fore.GREEN + "Successfully installed app.")
                print(Fore.RESET + "It is reccomended to wipe temp after install.")
            case "99":
                confirmwipetemp = input(Fore.YELLOW + "Are you sure you want to wipe temp? (Y/N): ")
                confirmwipetemp.lower()
                if confirmwipetemp == "y":
                    shutil.rmtree(drivesel + r":\temp")
                    os.mkdir(drivesel + r":\temp")
                    print(Fore.GREEN + "Success.")
            case "98":
                confirmwipetemp = input(Fore.RED + "!! Are you sure you want to wipe everything on this drive? (Y/N): ")
                confirmwipetemp.lower()
                if confirmwipetemp == "y":
                    shutil.rmtree(drivesel + r":\temp")
                    shutil.rmtree(drivesel + r":\appdata")
                    shutil.rmtree(drivesel + r":\programs")
                    os.mkdir(drivesel + r":\temp")
                    os.mkdir(drivesel + r":\appdata")
                    os.mkdir(drivesel + r":\programs")
                    print(Fore.GREEN + "Success.")


            #https://github.com/portapps/ungoogled-chromium-portable/releases/download/115.0.5790.131-16/ungoogled-chromium-portable-win64-115.0.5790.131-16.7z
