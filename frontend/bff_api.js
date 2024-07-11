
export async function getGameTitleFromURLPath(urlPath) {
    const response = await fetch(`https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/url-path?url=${urlPath}`, { cache: 'no-store' })
    const { game_title } = await response.json()
    return game_title
}

export async function getReviewsByGameTitle(gameTitle) {
    const response = await fetch(`https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/reviews?game=${gameTitle}`, { cache: 'no-store' })

    if (!response.ok) {
        throw new Error('Failed to fetch reviews')
    }

    const reviews = await response.json()
    return reviews
}


export async function getGameArtByReleaseDateGameTitle(releaseDate, gameTitle) {
    const response = await fetch(`https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/game?game=${releaseDate}_${gameTitle}`, { cache: 'no-store' })
    try {
        if (!response.ok) {
            throw new Error('Failed to fetch game art')
        }
    } catch (error) {
        return "https://tinyurl.com/4snc3bwk"
    }
    const game = await response.json()
    return game.game_art_url
}

export async function fetchGameData(urlPath) {
    const gameTitle = await getGameTitleFromURLPath(urlPath);
    const reviews = await getReviewsByGameTitle(gameTitle);
    const gameArtURL = await getGameArtByReleaseDateGameTitle(reviews[0].game_release_date, gameTitle);

    return { gameTitle, reviews, gameArtURL };
}

export async function getAllGames() {
    const response = await fetch("https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/games", { cache: 'no-store' })


    if (!response.ok) {
        throw new Error('Failed to fetch reviews')
      }
    
    const games = await response.json()

    return games
}

