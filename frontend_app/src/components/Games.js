'use client'
import React, { useState, useEffect } from 'react';
// async function getGames() {
//     const response = await fetch("https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/games", { cache: 'no-store' })

//     if (!response.ok) {
//         throw new Error('Failed to fetch reviews')
//     }

//     const games = await response.json()
//     return games
// }





export default function Games() {
    // const games = await getGames();
    const [data, setData] = useState([]);
    const mockData = [
        { 'game_title': 'Shadow Quest', 'release_date': '2022-11-15', 'url_path': '/games/shadow-quest' },
        { 'game_title': 'Rise of the Phoenix', 'release_date': '2023-02-20', 'url_path': '/games/rise-of-the-phoenix' },
        { 'game_title': 'Cyber Drift', 'release_date': '2023-05-30', 'url_path': '/games/cyber-drift' },
        { 'game_title': 'Mystic Realms', 'release_date': '2023-08-24', 'url_path': '/games/mystic-realms' },
        { 'game_title': 'Final Frontier', 'release_date': '2023-12-05', 'url_path': '/games/final-frontier' }
    ];
    useEffect(() => {
        async function getGames() {
            const response = await fetch("https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/games", { cache: 'no-store' })

            if (!response.ok) {
                throw new Error('Failed to fetch reviews')
            }

            const games = await response.json()
            setData(games)
        }
        getGames();
    }, [])
    return (
        <div className='grid grid-cols-4 gap-4'>
            {
                data.map((game, index) => (
                    <div key={index} className='p-8 flex flex-col items-center'>
                        <img src={game.game_art_url} alt={`game-art for ${game.game_title}`} className='w-36 h-36 rounded-2xl' />
                        <h2 className="font-bold">{game.game_title}</h2>
                        <p>Release Date: {game.release_date}</p>
                        <a className="text-black italic underline" href={`/game.html?title=${game.game_title}`}>Read Reviews</a>
                    </div>
                ))
            }
        </div>
    )
}