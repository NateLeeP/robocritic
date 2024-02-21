
async function getReviewsByGameTitle(url) {
    // get title from url
    const urlResponse = await fetch(`https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/url-path?url=${url}`, { cache: 'no-store' })
    const urlResponseJson = await urlResponse.json()
    const game_title = urlResponseJson.game_title
    const gameResponse = await fetch(`https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/reviews?game=${game_title}`)
    const game = await gameResponse.json()
    return game
}

async function getGameArtByReleaseDateGameTitle(release_date, game_title) {
    const response = await fetch(`https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/game?game=${release_date}_${game_title}`, { cache: 'no-store' })
    const game = await response.json()
    return game
}

import Review from './Review';

export default async function Game({ url }) {
    const reviews = await getReviewsByGameTitle(url)
    const game = await getGameArtByReleaseDateGameTitle(reviews[0].game_release_date, reviews[0].game_title)
    return <div className="pl-60 pr-40">
        <h2>{game.game_title}</h2>
        <img src={game.game_art_url} alt={game.game_title} />
        {reviews.map((review) => <Review review={review} />)}
    </div>
}