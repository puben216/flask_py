import json

FILE = "norilog.json"

def save_data(start, finish, memo, created_at):
	try:
		database = json.load(open(FILE, mode="r", encoding="utf-8"))
	except FileNotFoundError:
		database = []

	database.insert(0, {
		"start": start,
		"finish": finish,
		"memo": memo,
		"created_at": created_at.strftime("%Y-%m-%d %H:%M")
	})

	json.dump(database, open(FILE, mode="w", encoding="utf-8"), indent=4, ensure_ascii=False)