from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    '''
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )
    matcher = And(
        Not(HasAtLeast(1, "goals")),
        Not(PlaysIn("SEA"))
    )

    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )
    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    filtered_with_all = stats.matches(All)
    print(len(filtered_with_all))
    '''
    query = QueryBuilder()
    m1 = (QueryBuilder().playsIn("PHI").hasAtLeast(10, "assists").hasFewerThan(5, "goals").build())
    m2 = (QueryBuilder().playsIn("EDM").hasAtLeast(50, "points").build())
    matcher = query.oneOf(m1, m2).build()


    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
