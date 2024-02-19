import Link from 'next/link'


async function getGames() {
    const response = await fetch("https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/games", { cache: 'no-store' })

    if (!response.ok) {
        throw new Error('Failed to fetch reviews')
    }

    const games = response.json()
    return games
}

export default async function Reviews() {
    const games = await getGames();
    return (
        <div>
            <h1>Games</h1>
            {
                games.map((game, index) => (
                    <div key={index}>
                        <Link href={`/game/${game.url_path}`}>Click me!</Link>
                        <h2>{game.game_title}</h2>
                        <img src={game.game_art_url} />
                        <p>{game.release_date}</p>
                    </div>
                ))
            }
        </div>
    )
}