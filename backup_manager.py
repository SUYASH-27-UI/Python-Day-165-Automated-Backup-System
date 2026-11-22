
import os
import zipfile
import shutil
from datetime import datetime

BACKUP_FOLDER = "backups"

def create_backup():
    source = input("Enter folder path to backup: ").strip()

    if not os.path.isdir(source):
        print("Folder not found!")
        return

    os.makedirs(BACKUP_FOLDER, exist_ok=True)

    folder_name = os.path.basename(os.path.abspath(source))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_name = f"{folder_name}_{timestamp}.zip"
    backup_path = os.path.join(BACKUP_FOLDER, backup_name)

    try:
        with zipfile.ZipFile(
            backup_path, "w", zipfile.ZIP_DEFLATED
        ) as zip_file:

            for root, dirs, files in os.walk(source):
                for file in files:
                    file_path = os.path.join(root, file)

                    relative_path = os.path.relpath(
                        file_path, source
                    )

                    zip_file.write(file_path, relative_path)

        print("\nBackup created successfully!")
        print("Backup file:", backup_path)

    except OSError as error:
        print("Backup failed:", error)


def view_backups():
    if not os.path.exists(BACKUP_FOLDER):
        print("No backups available.")
        return

    backups = [
        file for file in os.listdir(BACKUP_FOLDER)
        if file.endswith(".zip")
    ]

    if not backups:
        print("No backup files found.")
        return

    print("\n===== AVAILABLE BACKUPS =====")

    for index, backup in enumerate(backups, start=1):
        print(index, ".", backup)


def restore_backup():
    view_backups()

    if not os.path.exists(BACKUP_FOLDER):
        return

    backups = [
        file for file in os.listdir(BACKUP_FOLDER)
        if file.endswith(".zip")
    ]

    if not backups:
        return

    try:
        choice = int(input("\nSelect backup number: "))

        if choice < 1 or choice > len(backups):
            print("Invalid selection!")
            return

        selected = backups[choice - 1]
        backup_path = os.path.join(BACKUP_FOLDER, selected)

        destination = input(
            "Enter destination folder: "
        ).strip()

        if not destination:
            print("Destination cannot be empty.")
            return

        destination = os.path.abspath(destination)

        # Prevent restoring into the backup archive itself
        if os.path.commonpath(
            [destination, os.path.abspath(BACKUP_FOLDER)]
        ) == os.path.abspath(BACKUP_FOLDER):
            print("Choose a destination outside the backups folder.")
            return

        os.makedirs(destination, exist_ok=True)

        with zipfile.ZipFile(backup_path, "r") as zip_file:
            for member in zip_file.infolist():
                target = os.path.abspath(
                    os.path.join(destination, member.filename)
                )

                if os.path.commonpath(
                    [destination, target]
                ) != destination:
                    raise ValueError("Unsafe archive path detected.")

            zip_file.extractall(destination)

        print("Backup restored successfully!")

    except ValueError as error:
        print("Error:", error)

    except (OSError, zipfile.BadZipFile) as error:
        print("Restore failed:", error)


while True:
    print("\n===== BACKUP MANAGER =====")
    print("1. Create Backup")
    print("2. View Backups")
    print("3. Restore Backup")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_backup()

    elif choice == "2":
        view_backups()

    elif choice == "3":
        restore_backup()

    elif choice == "4":
        print("Exiting Backup Manager...")
        break

    else:
        print("Invalid choice!")
