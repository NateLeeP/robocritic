import Game from '../../components/Game.js'
import { fetchGameData } from '../../bff_api.js'
export async function getStaticPaths() {
    const paths = [{
        params: {
            url: 'f1-24'
        }
    },
    {
        params: {
            url: 'capes'
        }
    },
    {
        params: {
            url: 'killer-klowns-from-outer-space-the-game'
        }
    }
    ]
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