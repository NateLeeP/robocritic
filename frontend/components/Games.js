import Link from 'next/link'


export default function Games({ games }) {
    // const games = await getGames();


    return (
        <div className='grid grid-cols-1 lg:grid-cols-5 sm:grid-cols-3 gap-4'>
            {
                games.map((game, index) => (
                    <div key={index} className='p-8 flex flex-col items-center sm:items-start'>
                        <a href={`/game/${game.url_path}`}><img src={game.game_art_url} alt={`Art for ${game.game_title}`} className='w-36 h-36 rounded-2xl hover:shadow-2xl' /></a>
                        <h2 className="text-wrap font-semibold font-serif text-l text-stone-300">{game.game_title}</h2>
                        <p className='font-serif text-sm text-neutral-300'>Release Date: {game.release_date}</p>
                        <a className="font-serif text-stone-300 italic underline hover:font-bold" href={`/game/${game.url_path}`}>Read Reviews</a>
                    </div>
                ))
            }
        </div>
    )
}