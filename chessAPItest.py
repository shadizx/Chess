from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()

def print_leaderboards():
	data = get_leaderboards().json
	categories = data.keys()

	for category in categories:
		print('Category:', category)
		for idx, entry in enumerate(data[category]):
			print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')


def get_player_rating(username):
	data = get_player_stats(username).json
	printer.pprint(data)


def get_most_recent_game(username):
	data = get_player_game_archives(username).json
	url = data['archives'][-1]
	games = requests.get(url).json()
	game = games['games'][-1]
	printer.pprint(game)

get_most_recent_game('Weekendend')
# get_player_rating('Weekendend')