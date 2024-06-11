import Link from 'next/link'


export default function Games({ games }) {
    // const games = await getGames();
    const mockData = [
        { 'game_title': 'Shadow Quest', 'release_date': '2022-11-15', 'url_path': '/games/shadow-quest' },
        { 'game_title': 'Rise of the Phoenix', 'release_date': '2023-02-20', 'url_path': '/games/rise-of-the-phoenix' },
        { 'game_title': 'Cyber Drift', 'release_date': '2023-05-30', 'url_path': '/games/cyber-drift' },
        { 'game_title': 'Mystic Realms', 'release_date': '2023-08-24', 'url_path': '/games/mystic-realms' },
        { 'game_title': 'Final Frontier', 'release_date': '2023-12-05', 'url_path': '/games/final-frontier' }
    ];

    return (
        <div className='grid grid-cols-1 md:grid-cols-5 gap-4'>
            {
                games.map((game, index) => (
                    <div key={index} className='p-8 flex flex-col'>
                        <Link href={`/game/${game.url_path}`}><img src={game.game_art_url} alt={`Art for ${game.game_title}`} className='w-36 h-36 rounded-2xl hover:shadow-2xl' /></Link>
                        <h2 className="text-wrap font-semibold font-serif text-l text-stone-300">{game.game_title}</h2>
                        <p className='font-serif text-sm text-neutral-300'>Release Date: {game.release_date}</p>
                        <Link className="font-serif text-stone-300 italic underline hover:font-bold" href={`/game/${game.url_path}`}>Read Reviews</Link>
                    </div>
                ))
            }
        </div>
    )
}