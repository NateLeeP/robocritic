'use client'
import Review from './Review';
import { useEffect, useState } from 'react';
import { useSearchParams } from "next/navigation"


export default function Game() {
    const searchParames = useSearchParams()
    const gameTitle = searchParames.get('title')
    const [reviews, setReviews] = useState([]);
    const [gameArtURL, setGameArtURL] = useState('')
    console.log(gameTitle)
    useEffect(() => {
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
            const game = await response.json()
            return game
        }

        async function getReviews() {
            const reviews = await getReviewsByGameTitle(gameTitle)
            setReviews(reviews)
            const releaseDate = reviews[0].game_release_date
            const { game_art_url } = await getGameArtByReleaseDateGameTitle(releaseDate, gameTitle)
            setGameArtURL(game_art_url)
        }
        getReviews();
    }, [])
    return <div className="pl-60 pr-40">
        <h1 className="font-mono italic text-3xl">{gameTitle}</h1>
        <img src={gameArtURL} alt={gameTitle} />
        {reviews.map((review, index) => <Review key={index} review={review} />)}
    </div>
}