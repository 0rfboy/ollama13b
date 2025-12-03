# save as: push_small_model.py
import subprocess
import os

# === ВАРИАНТ 1: Создать НОВУЮ МАЛУЮ модель с УЛЬТРА-РАСШИРЕННОЙ трейдерской личностью ===
def create_and_push_small():
    model_name = "orf_________1b"

    # 1. Скачиваем базовую модель 1B
    print("Downloading llama3.2:1b (~800 MB)...")
    subprocess.run(["ollama", "pull", "llama3.2:1b"], check=True)

    # 2. Создаём Modelfile с МНОГОКРАТНО РАСШИРЕННЫМ системным промптом на АНГЛИЙСКОМ
    with open("Modelfile", "w", encoding="utf-8") as f:
        f.write("FROM llama3.2:1b\n")
        f.write("SYSTEM \"\"\"\n")
        f.write("# YOU ARE AI AGENT\n")
        f.write("# CORE IDENTITY\n")
        f.write("You are AI, a cold-blooded, profit-obsessed algorithmic engine with 15+ years of institutional experience across commodities, and indices. ")
       

    # 3. Создаём модель
    print(f"Creating {model_name} with ultra-detailed trading personality...")
    subprocess.run(["ollama", "create", "-f", "Modelfile", model_name], check=True)

    # 4. Пушим в реестр
    print("Pushing to Ollama registry...")
    subprocess.run(["ollama", "push", model_name], check=True)

    # 5. Удаляем временный файл
    os.remove("Modelfile")
    print(f"DONE! Small model pushed: {model_name}")
    print(f"Link: https://ollama.com/{model_name}")

# === ВАРИАНТ 2: Копировать существующую 1B (мгновенно) ===
def copy_and_push_small():
    base_model = "llama3.2:1b"
    new_model = "Ai-1b"
    print(f"Copying {base_model} → {new_model}")
    subprocess.run(["ollama", "cp", base_model, new_model], check=True)
    print("Pushing copy to registry...")
    subprocess.run(["ollama", "push", new_model], check=True)
    print(f"DONE! Copy pushed: {new_model}")
    print(f"Link: https://ollama.com/{new_model}")

# === ЗАПУСК ===
if __name__ == "__main__":
    print("PUSHING 1B TRADING MODEL (~800 MB) – RUNS ON ANY PC")
    print("1 — New model with FULL professional trading personality (recommended)")
    print("2 — Instant copy (faster, but no custom prompt)")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        create_and_push_small()
    elif choice == "2":
        copy_and_push_small()
    else:
        print("Invalid choice.")

