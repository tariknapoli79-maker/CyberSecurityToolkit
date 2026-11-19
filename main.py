
import os
import re

def menu():
    os.system("clear")
    print("=" * 40)
    print("       🛡️ أدوات الأمن السيبراني")
    print("=" * 40)
    print("""
[1] معلومات الشبكة
[2] فحص قوة كلمة المرور
[3] تعلم الأمن السيبراني
[4] خروج
""")

def network():
    os.system("ip addr")
    input("\nاضغط Enter للرجوع...")

def password_checker():
    password = input("أدخل كلمة مرور تجريبية: ")

    score = 0
    score += len(password) >= 12
    score += bool(re.search(r"[A-Z]", password))
    score += bool(re.search(r"[a-z]", password))
    score += bool(re.search(r"[0-9]", password))
    score += bool(re.search(r"[^A-Za-z0-9]", password))

    print("\nنتيجة الفحص:")

    if score <= 2:
        print("🔴 كلمة المرور ضعيفة")
    elif score <= 4:
        print("🟡 كلمة المرور متوسطة")
    else:
        print("🟢 كلمة المرور قوية")

    input("\nاضغط Enter للرجوع...")

def learning():
    os.system("clear")
    print("""
🛡️ تعلم الأمن السيبراني

1. تعلم أوامر Linux
2. أساسيات الشبكات
3. حماية كلمات المرور
4. الاختراق الأخلاقي
""")
    input("\nاضغط Enter للرجوع...")

while True:
    menu()
    choice = input("اختر رقم الأداة: ")

    if choice == "1":
        network()
    elif choice == "2":
        password_checker()
    elif choice == "3":
        learning()
    elif choice == "4":
        print("إلى اللقاء!")
        break
    else:
        print("اختيار غير صحيح")
        input("اضغط Enter...")



