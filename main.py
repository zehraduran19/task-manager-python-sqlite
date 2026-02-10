from database import (
    create_tables,
    add_user,
    add_task,
    get_tasks,
    get_users,
    delete_task,
    complete_task,
)


def main():
    create_tables()

    while True:
        print("\n1 - Kullanıcı oluştur")
        print("2 - Görev ekle")
        print("3 - Görevleri listele")
        print("4 - Kullanıcıları listele")
        print("5 - Görev sil")
        print("6 - Görev tamamla")
        print("7 - Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            username = input("Kullanıcı adı: ")
            add_user(username)

        elif secim == "2":
            user_id = int(input("Kullanıcı ID: "))
            task = input("Görev: ")
            add_task(user_id, task)
            print("Görev eklendi.")

        elif secim == "3":
            user_id = int(input("Kullanıcı ID: "))
            tasks = get_tasks(user_id)

            if len(tasks) == 0:
                print("Bu kullanıcıya ait veri yok!")
            else:
                for i, task in enumerate(tasks, start=1):
                    durum = "✅" if task[2] == 1 else "❌"
                    print(f"ID: {task[0]} - {task[1]} {durum}")

        elif secim == "4":
            users = get_users()

            if len(users) == 0:
                print("Henüz kullanıcı yok.")
            else:
                print("\n---Kullanıcı Listesi---")
                for user in users:
                    print(f"ID: {user[0]} | Kullanıcı adı: {user[1]}")

        elif secim == "5":
            task_id = int(input("Silmek istediğiniz görev ID: "))
            delete_task(task_id)
            print("Görev silindi.")

        elif secim == "6":
            task_id = int(input("Tamamlanan görev ID: "))
            complete_task(task_id)
            print("Görev tamamlandı olarak işaretlendi.")

        elif secim == "7":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Hatalı seçim! Tekrar deneyiniz.")


main()
