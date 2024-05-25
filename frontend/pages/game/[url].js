export async function generateStaticParams() {
    const games = await fetch('https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/games', { cache: 'no-store' }).then((res) => res.json())
    return games.map((game) => ({
        url: game.url_path ?? game.game_title
    }))
}

import Game from '../../components/Game/';

export default function GamePage({ params }) {

    return (
        <Game url={params.url} />
    )
}