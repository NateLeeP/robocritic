import Review from './Review';

export default function Game({ gameArtURL, gameTitle, reviews }) {

    return (
        <div className="pl-10 pr-10 text-stone-300">
            <h1 className="font-mono text-6xl text-stone-300">{gameTitle}</h1>
            <img src={gameArtURL} alt={gameTitle} className='w-36 h-36 mb-2 mt-5' />
            <Review review={reviews[0]} />
        </div>
    )
}