import Link from 'next/link'


async function getGames() {
    const response = await fetch("https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/games")

    if (!response.ok) {
        throw new Error('Failed to fetch reviews')
    }

    const games = response.json()
    console.log(games);
    return games
}

export default async function Reviews() {
    const games = await getGames();
    return (
        <div>
            <h1>Reviews</h1>
            {
                games.map((game, index) => (
                    <div key={index}>
                        <Link href="/game/prince-of-persia-the-lost-crown?title=Test">Link</Link>
                        <h2>{game.game_title}</h2>
                        <img src={game.game_art_url} />
                        <p>{game.release_date}</p>
                    </div>
                ))
            }
        </div>
    )
}