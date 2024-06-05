import Review from './Review';

async function getGameTitleFromURLPath(urlPath) {
    const response = await fetch(`https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/url-path?url=${urlPath}`, { cache: 'no-store' })
    const { game_title } = await response.json()
    return game_title
}

async function getReviewsByGameTitle(gameTitle) {
    const response = await fetch(`https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/reviews?game=${gameTitle}`, { cache: 'no-store' })

    if (!response.ok) {
        throw new Error('Failed to fetch reviews')
    }

    const reviews = await response.json()
    return reviews
}


async function getGameArtByReleaseDateGameTitle(releaseDate, gameTitle) {
    const response = await fetch(`https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/game?game=${releaseDate}_${gameTitle}`, { cache: 'no-store' })
    if (!response.ok) {
        throw new Error('Failed to fetch game art')
    }
    const game = await response.json()
    return game.game_art_url
}

async function fetchGameData(urlPath) {
    const gameTitle = await getGameTitleFromURLPath(urlPath);
    const reviews = await getReviewsByGameTitle(gameTitle);
    const gameArtURL = await getGameArtByReleaseDateGameTitle(reviews[0].game_release_date, gameTitle);

    return { gameTitle, reviews, gameArtURL };
}

export default async function Game({ urlPath }) {

    const { gameTitle, reviews, gameArtURL } = await fetchGameData(urlPath);


    return <div className="pl-60 pr-40">
        <h1 className="font-mono italic text-3xl">{gameTitle}</h1>
        <img src={gameArtURL} alt={gameTitle} />
        <Review review={reviews[0]} />
    </div>
}