export default function Review({ review }) {
    return (
        <div className="flex w-4/5 justify-between border-b-4 border-slate-400 border-dotted">
            <div className="">
                <a className="self-center justify-center text-2xl italic underline" target="_blank" href={review.review_url}>{review.review_publisher_name}</a>
                <h3>Critic score: {review.critic_score}</h3>
                <h3>Roboscore: {review.roboscore}</h3>
            </div>
            <ul className="basis-1/3">
                <div className="italic">Pros</div>
                {review.pros.map((pro) => { return <> <li key={pro}>{pro}</li> <br /></> })}
            </ul>
            <ul className="basis-1/3">
                <div className="italic">Cons</div>
                {review.cons.map((con) => { return <><li key={con}>{con}</li> <br /></> })}
            </ul>
        </div>
    )
}