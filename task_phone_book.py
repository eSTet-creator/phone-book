# Написати консольний застосунок "Телефонна книга" зі збереженням між запусками
# програми (через файл), що підтримує: додавання контакту, пошук за іменем, видалення, показ
# усіх контактів, збереження у файл під час виходу та завантаження з файлу під час запуску.




# Починаємо зі створення функції для завантаження даних з файлу
def load_contacts(filename="contacts.txt"):
    contacts = {}
    try:
         with open(filename, "r", encoding="utf-8") as file:
             for line in file:
                line = line.strip()
                if not line:
                    continue
                if "," in line:

                    name, phone = line.split(",", 1)
                    contacts[name] = phone
    except FileNotFoundError:
        return contacts
    return contacts

# Збереження контактів під час виходу
def save_contacts(contacts, filename="contacts.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

# Додавання контакту
def add_contacts(contacts):
    while True:
        name = input("Введіть імʼя: ").strip()
        if name:
            break
        print("Імʼя не може бути порожнім. Введіть імʼя.")
    while True:
        phone = input("Введіть номер: ").strip()
        if phone:
            break
        print("Номер не може бути порожнім. Введіть номер.")
    contacts[name] = phone
    print(f"Контакт {name} успішно додано.")

# Пошук контакту
def find_contact(contacts):
    wanted = input("Введіть ім'я для пошуку: ").strip().lower()
    found = False
    for name, phone in contacts.items():
        if wanted in name.lower():
            print(f"Знайдено: {name} — {phone}")
            found = True
    if not found:
        print(f"Контакт за імʼям {wanted} не знайдено.")

# Видалення контакту
def delete_contact(contacts):
    delete_name = input("Введіть ім'я для видалення: ").strip()
    delete_key = None
    for name in contacts:
        if name.lower() == delete_name.lower():
            delete_key = name
            break
    if delete_key:
        del contacts[delete_key]
        print(f"Контакт {delete_key} успішно видалено")
    else:
        print(f"Контакт {delete_name} не знайдено")

# Показ усіх контактів
def show_all_contacts(contacts):
    if not contacts:
        print(f"Телефонна книга порожня")
        return
    print("\n --- Список усіх контактів ---")
    for name, phone in contacts.items():
        print(f"{name} - {phone}")
    print("--------------------------------")

# Головне меню
def main():
    contacts = load_contacts()
    try:
        while True:
            print("\n=== МЕНЮ ===")
            print("1. Додати контакт")
            print("2. Знайти контакт")
            print("3. Видалити контакт")
            print("4. Показати всі контакти")
            print("5. Вийти")

            choice = input("Обери дію (1 - 5): ").strip()

            if choice == "1":
                add_contacts(contacts)
            elif choice == "2":
                find_contact(contacts)
            elif choice == "3":
                delete_contact(contacts)
            elif choice == "4":
                show_all_contacts(contacts)
            elif choice == "5":
                print("Завершення роботи")
                break
            else:
                print("Невірний вибір. Спробуй ще раз.")

    finally:
        save_contacts(contacts)
        print("Дані автоматично збережені у файл contacts.txt")

if __name__ == "__main__":
    main()

















