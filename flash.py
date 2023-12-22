#MODULE#
import os,sys,time,datetime
from time import sleep
from datetime import datetime
from os import listdir
#WAKTU#
waktu = datetime.now()
tahun = waktu.year
bulan = waktu.month
hari = waktu.day
jam = waktu.hour
menit = waktu.minute
detik = waktu.second
waktu2 = time.ctime()
#COLOR#
if sys.platform in ["linux","linux2"]:
	W = ("\033[0m")
	G = ("\033[32;1m")
	R = ("\033[31;1m")
else:
	W = ("")
	G = ("")
	R = ("")
#FUNCTION#
banner =(G+" d88888b d88888b .88b  d88. \n 88'     88'     88'YbdP`88  "+R+"- Fastboot Flashing Mobile\n"+G+" 88ooo   88ooo   88  88  88  "+R+"- Version : 1.1\n "+G+"88~~~   88~~~   88  88  88  "+R+"- Author : FARHAN-MUH-TASIM\n "+G+"88      88      88  88  88  "+R+"- Donate : ++880 1305-057238 (AX)\n "+G+"YP      YP      YP  YP  YP ")
def port():
	print ("\x1bc")
	print (R+"-----------------------------")
	print (G+"[!] Check  Devices")
	print (R+"-----------------------------\n")
	os.system("fastboot devices")
	print (R+"\n-----------------------------\n")
def twrp():
	try:
		print (G+"[+] Installing TWRP...")
		namaF = raw_input("Input name file : ")
		os.system("fastboot flash recovery TWRP/"+namaF)
		if (not os.path.isfile(namaF)):
			print (R+"[!] Failed to install TWRP/ORF\n")
		else:
		    print (G+"[+] Successfully installed TWRP/ORF")
		    sleep(3)
		    print (G+"[!] Rebooting...")
		    os.system("fastboot reboot")
	except :
		print (R+"\n[!] Failed to install TWRP/ORF\n")
def flash():
	try:
		print (R+"------------------------")
		print (G+"[1] Flash all")
		print (G+"[2] flash all except data storage")
		print (R+"------------------------")
		pilih = input(W+"Select the menu : ")
	except:
		print (R+"\n[!] Select the menu correctly\n")
	try:
		if pilih > 2:
			print (R+"\n[!] Select the menu correctly\n")
		elif pilih == 1:
			namaF = raw_input(G+"Masukan nama folder di path ROM : ")
			if (not os.path.isdir("ROM/"+namaF)):
			     print (R+"\n[!] Gagal flashing ROM/Folder tidak di temukan\n")
			else:
				print (G+"[+] Flashing rom...")
				os.system("fastboot flash tz ROM/"+namaF+"/tz.mbn")
				os.system("fastboot flash sbll ROM/"+namaF+"/sbll.mbn")
				os.system("fastboot flash rpm ROM/"+namaF+"/rpm.mbn")
				os.system("fastboot flash aboot ROM/"+namaF+"/emmc_appsboot.mbn")
				os.system("fastboot flash tzbak ROM/"+namaF+"/tz.mbn")
				os.system("fastboot flash rpmbak ROM/"+namaF+"/rpm.mbn")
				os.system("fastboot flash abootbak ROM/"+namaF+"/emmc_appsboot.mbn")
				os.system("fastboot flash devcfg ROM/"+namaF+"/devcfg.mbn")
				os.system("fastboot flash lksecapp ROM/"+namaF+"/lksecapp.mbn")
				os.system("fastboot flash cmnlib ROM/"+namaF+"/cmnlib.mbn")
				os.system("fastboot flash cmnlib64 ROM/"+namaF+"/cmnlib64.mbn")
				os.system("fastboot flash keymaster ROM/"+namaF+"/keymaster.mbn")
				os.system("fastboot flash devcfgbak ROM/"+namaF+"/devcfg.mbn")
				os.system("fastboot flash lksecappbak ROM/"+namaF+"/lksecapp.mbn")
				os.system("fastboot flash cmnlibbak ROM/"+namaF+"/cmnlib.mbn")
				os.system("fastboot flash cmnlib64bak ROM/"+namaF+"/cmnlib64.mbn")
				os.system("fastboot flash keymasterbak ROM/"+namaF+"/keymaster.mbn")
				os.system("fastboot flash dsp ROM/"+namaF+"/adspso.bin")
				os.system("fastboot erase boot")
				os.system("fastboot flash modem ROM/"+namaF+"/NON-HLOS.bin")
				os.system("fastboot flash system ROM/"+namaF+"/system.img")
				os.system("fastboot flash cache ROM/"+namaF+"/cache.img")
				os.system("fastboot flash userdata ROM/"+namaF+"/userdata.img")
				os.system("fastboot flash recovery ROM/"+namaF+"/recovery.img")
				os.system("fastboot flash boot ROM/"+namaF+"/boot.img")
				os.system("fastboot flash misc ROM/"+namaF+"/misc.img")
				os.system("fastboot flash splash ROM/"+namaF+"/splash.img")
				os.system("fastboot flash cust ROM/"+namaF+"/cust.img")
				print (G+"[!] Flashing ROM selesai")
				sleep(3)
				print(G+"[!] Rebooting...")
				os.system("fastboot reboot")
		elif pilih == 2:
			namaF = raw_input(G+"Masukan nama folder di path ROM : ")
			if (not os.path.isdir("ROM/"+namaF)):
			    print (R+"\n[!] Gagal flashing ROM/Folder tidak di temukan\n")
			else:
			    print (G+"[+] Flashing rom...")
			    os.system("fastboot flash tz ROM/"+namaF+"/tz.mbn")
			    os.system("fastboot flash sbll ROM/"+namaF+"/sbll.mbn")
			    os.system("fastboot flash rpm ROM/"+namaF+"/rpm.mbn")
			    os.system("fastboot flash aboot ROM/"+namaF+"/emmc_appsboot.mbn")
			    os.system("fastboot flash tzbak ROM/"+namaF+"/tz.mbn")
			    os.system("fastboot flash rpmbak ROM/"+namaF+"/rpm.mbn")
			    os.system("fastboot flash abootbak ROM/"+namaF+"/emmc_appsboot.mbn")
			    os.system("fastboot flash devcfg ROM/"+namaF+"/devcfg.mbn")
			    os.system("fastboot flash lksecapp ROM/"+namaF+"/lksecapp.mbn")
			    os.system("fastboot flash cmnlib ROM/"+namaF+"/cmnlib.mbn")
			    os.system("fastboot flash cmnlib64 ROM/"+namaF+"/cmnlib64.mbn")
			    os.system("fastboot flash keymaster ROM/"+namaF+"/keymaster.mbn")
			    os.system("fastboot flash devcfgbak ROM/"+namaF+"/devcfg.mbn")
			    os.system("fastboot flash lksecappbak ROM/"+namaF+"/lksecapp.mbn")
			    os.system("fastboot flash cmnlibbak ROM/"+namaF+"/cmnlib.mbn")
			    os.system("fastboot flash cmnlib64bak ROM/"+namaF+"/cmnlib64.mbn")
			    os.system("fastboot flash keymasterbak ROM/"+namaF+"/keymaster.mbn")
			    os.system("fastboot flash dsp ROM/"+namaF+"/adspso.bin")
			    os.system("fastboot erase boot")
			    os.system("fastboot flash modem ROM/"+namaF+"/NON-HLOS.bin")
			    os.system("fastboot flash system ROM/"+namaF+"/system.img")
			    os.system("fastboot flash cache ROM/"+namaF+"/cache.img")
			    os.system("fastboot flash recovery ROM/"+namaF+"/recovery.img")
			    os.system("fastboot flash boot ROM/"+namaF+"/boot.img")
			    os.system("fastboot flash misc ROM/"+namaF+"/misc.img")
			    os.system("fastboot flash splash ROM/"+namaF+"/splash.img")
			    os.system("fastboot flash cust ROM/"+namaF+"/cust.img")
			    print (G+"[!] Flashing rom selesai")
			    sleep(3)
			    print (G+"[!] Rebooting...")
			    os.system("fastboot reboot")
		else:
			print (R+"\n[!] Select the menu correctly\n")
	except:
		print (R+"\n[!] Select the menu correctly\n")
def adb():
	try:
		print (G+"[+] Installing adb & fastboot....")
		os.system("cp ADB/fastboot /data/data/com.termux/files/usr/bin")
		os.system("cp ADB/adb /data/data/com.termux/files/usr/bin")
		os.system("chmod 755 /data/data/com.termux/files/usr/bin/fastboot")
		os.system("chmod 755 /data/data/com.termux/files/usr/bin/adb")
		sleep(3)
		print (G+"[+] Installing adb & fastboot is complete")
	except OSError:
		pass
def oem():
	try:
		print ("\x1bc")
		print (R+"--------------------------")
		print (G+"Check OEM & lock").center(30)
		print (R+"--------------------------\n"+G)
		os.system("fastboot oem device-info")
		print (G+"\n--------------------------")
	except:
		print (R+"\n[!] Input not found")
	sleep(3)
	try:
		print (R+"--------------------------")
		print (G+"[1] Lock OEM [2] Cancel")
		print (R+"--------------------------")
		pilih = input(W+"Select the menu : ")
		if pilih > 2:
			print (R+"\n[!] Input not found")
		elif pilih == 1:
			print ("\x1bc")
			print (R+"[!] locking OEM...")
			sleep(3)
			os.system("fastboot oem lock")
			print (G+"\n[!] Success locking OEM\n")
		elif pilih == 2:
			print (R+"\n[!] Cancel for lock OEM\n")
		else:
			print (R+"\n[!] Select the menu correctly\n")
	except:
		print (R+"\n[!] Select the menu correctly\n")
def about():
	print ("\x1bc")
	print (R+"------------------------------------")
	print (G+"Fastboot Flashing Mobile").center(37)
	print (R+"------------------------------------")
	print (G+"Coder : FARHAN-MUH-TASIM")
	print (G+"Find Me :")
	print (G+"Facebook :"+R+" http://fb.me/100094924471568")
	print (G+"Telegram :"+R+" https://t.me/farhan_muh_tasim")
	print (G+"Github :"+R+" https://github.com/Gtajisan")
	print (G+"Whatsapp :"+R+"+880 1305-057238")
	print (R+"------------------------------------")
	print (G+"Donate :")
	print (G+"recharge  :"+R+"+880 1305-057238")
	print (G+"Phone :"+R+" +880 1305-057238 (Axis)")
	print (R+"------------------------------------")
def reset():
	try:
		print (R+"[!] Me-reset data...")
		os.system("fastboot -w")
		print (G+"[!] Data-reset is complete")
		sleep(3)
		print (G+"[!] Rebooting....")
		os.system("fastboot reboot")
		print (G+"[!] Rebooting selesai")
	except:
		pass
def splash():
	try:
		print (G+"[!] Menginstall splash...")
		masukan = raw_input("Masukan nama file splash : ")
		os.system("fastboot flash splash SPLASH/"+masukan+".img")
		print (G+"[!] Install splash selesai")
		sleep(3)
		print (G+"[!] Rebooting....")
		os.system("fastboot reboot")
		print (G+"[!] Rebooting selesai")
	except SyntaxError:
		pass
	except:
		pass
def update():
	try:
		print (G+"[!] Updating tools...")
		sleep(3)
		os.system("git pull")
		print (G+"[!] Update success")
		exit()
	except:
		print (R+"[!] Koneksi/File Error")
def menu():
	try:
		try:
			if not os.path.exists("TWRP"):
				os.mkdir("TWRP")
			elif not os.path.exists("ROM"):
				os.mkdir("ROM")
			elif not os.path.exists("ADB"):
				os.mkdir("ADB")
			elif not os.path.exists("SPLASH"):
				os.mkdir("SPLASH")
			else:
				pass
		except OSError:
			pass
		print (R+"-----------------------------")
		print (banner)
		print (R+"--------"+G+"| {}/{}/{} |"+R+"--------").format(hari,bulan,tahun)
		print ("")
		print (G+"[1] Check Device        [5] TWRP/ORANG FOX")
		print (G+"[2] Check & Lock OEM    [6] Reset")
		print (G+"[3] Flash ROM           [7] Splash")
		print (G+"[4] Install ADB         [8] About Tool")
		print (G+"[0] Exit                [9] Update Tool")
		print (R+"--------"+G+"|  {}:{}:{}  |"+R+"--------").format(jam,menit,detik)
		menu = input(W+"Select the menu : ")
		if menu > 9:
			print (R+"\n[!] Select the menu correctly\n")
		elif menu == 1:
			port()
		elif menu == 2:
			oem()
		elif menu == 3:
			flash()
		elif menu == 4:
			adb()
		elif menu == 5:
			twrp()
		elif menu == 6:
			reset()
		elif menu == 7:
			splash()
		elif menu == 8:
			about()
		elif menu == 9:
			update()
		elif menu == 0:
			print (R+"\n[!] Goodbye\n")
			exit()
		else:
			print (R+"\n[!] Select the menu correctly\n")
	except NameError:
		print (R+"\n[!] Select the menu correctly\n")
	except SyntaxError:
		print (R+"\n[!] Select the menu correctly\n")
if __name__ == "__main__":
	while(True):
	 menu()
