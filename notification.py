
#Enter following command in cmd/terminal to install win10toast library
#pip install win10toast

from win10toast import ToastNotifier

# .show_toast(title,msg,icon_path,duration)
variable = ToastNotifier()
variable.show_toast(title="Python", msg="HELLO World!",
                    icon_path="OS_Windows_8_23415.ico", duration=2)
