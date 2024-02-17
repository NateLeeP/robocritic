
async function getReviewsByGameTitle(url) {
    console.log(url)
    // get title from url
    const urlResponse = await fetch(`https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/url-path?url=${url}`, { cache: 'no-store' })
    const urlResponseJson = await urlResponse.json()
    console.log('urlResponseJson', urlResponseJson)
    const game_title = urlResponseJson.game_title
    const gameResponse = await fetch(`https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/reviews?game=${game_title}`)
    const game = await gameResponse.json()
    console.log('game', game)
    return game
}

export default async function Game({ url }) {
    const games = await getReviewsByGameTitle(url)

    return <div>
        {games.map((game) => <div>{game.game_title} {game.review_publisher_name}</div>)}
    </div>
}