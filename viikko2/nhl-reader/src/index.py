import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
    def get_players(self):
        response = requests.get(self.url).json()
        return [Player(player_dict) for player_dict in response]
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered = [player for player in players if player.nationality == nationality]
        return sorted(filtered, key=lambda x: x.goals + x.assists, reverse=True)


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(f"{player.name:20}{player.team} {player.goals} + {player.assists} = {player.goals + player.assists}")



if __name__ == "__main__":
    main()
