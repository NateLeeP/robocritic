import Game from '../../components/Game.js'
import { fetchGameData, getAllGames } from '../../bff_api.js'
export async function getStaticPaths() {

    const games = await getAllGames()
    const paths = games.map((game) => ({params: { url: game.url_path}}))
    return { paths, fallback: false }
}

export async function getStaticProps({ params }) {
    const url = params.url;
    const { gameTitle, reviews, gameArtURL } = await fetchGameData(url);
    return { props: { gameTitle, reviews, gameArtURL } }
}

export default function Page({ gameArtURL, gameTitle, reviews }) {
    // const { gameTitle, reviews, gameArtURL } = await fetchGameData(urlPath);

    return (
        <Game gameTitle={gameTitle} reviews={reviews} gameArtURL={gameArtURL} />
    )
}