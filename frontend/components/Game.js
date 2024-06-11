import Review from './Review';

export default function Game({ gameArtURL, gameTitle, reviews }) {

    return <div className="pl-60 pr-40">
        <h1 className="font-mono italic text-3xl">{gameTitle}</h1>
        <img src={gameArtURL} alt={gameTitle} />
        <Review review={reviews[0]} />
    </div>
}