import httpx

# Твой ключ Polza AI
API_KEY = "pza_NMlo-9bNgmfAK9ni2sbfUi2X9HBY5NaW"
headers = {"Authorization": f"Bearer {API_KEY}"}

print("Запрашиваем список моделей у Polza AI...")
try:
    response = httpx.get("https://api.polza.ai/v1/models", headers=headers)
    
    if response.status_code == 200:
        models = response.json().get("data", [])
        print("\n✅ НАЙДЕНЫ МОДЕЛИ LLAMA (Скопируй нужное название):")
        for model in models:
            if "llama" in model["id"].lower():
                print(f'👉 "{model["id"]}"')
    else:
        print("Ошибка запроса:", response.text)
except Exception as e:
    print("Ошибка соединения:", e)