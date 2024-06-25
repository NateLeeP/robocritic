import Review from './Review';

export default function Game({ gameArtURL, gameTitle, reviews }) {

    return (
        <div className="text-stone-300">
            <h1 className="font-mono italic text-3xl text-stone-300">{gameTitle}</h1>
            <img src={gameArtURL} alt={gameTitle} className='w-36 h-36' />
            <Review review={reviews[0]} />
        </div>
    )
}