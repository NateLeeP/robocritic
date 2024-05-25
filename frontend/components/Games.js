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
        <div className='grid grid-cols-4 gap-4'>
            {
                [].map((game, index) => (
                    <div key={index} className='p-8 flex flex-col items-center'>
                        {/* <img src={game.game_art_url} alt={`game-art for ${game.game_title}`} className='w-36 h-36 rounded-2xl' /> */}
                        <h2 className="font-bold">{game.game_title}</h2>
                        <p>Release Date: {game.release_date}</p>
                        <a className="text-black italic underline" href={`/game/${game.url_path}`}>Read Reviews</a>
                    </div>
                ))
            }
        </div>
    )
}