export default function Review({ key, review }) {


    return (
        <div key={key} className="justify-between border-b-4 border-slate-400 border-dotted h-full">
            <div className="flex text-stone-300">
                <a className="mr-5 text-2xl italic underline " target="_blank" href={review.review_url}>{review.review_publisher_name}</a>
                <h3 className="mr-5 self-center">Critic score: {review.critic_score}</h3>
                <h3 className="self-center">Roboscore: {review.roboscore}</h3>
            </div>
            <div className="sm:flex">
                <ul className="mb-5 sm:mr-5">
                    <div key={25} className="font-bold text-stone-300 text-lg">Pros</div>
                    {review.pros.map((pro, index) => (<li key={index}>{pro}<br /></li>))}
                </ul>
                <ul>
                    <div key={20} className="font-bold text-stone-300 text-lg">Cons</div>
                    {review.cons.map((con, index) => (<li key={index}>{con}<br /></li>))}
                </ul>
            </div>
            <br />
        </div>
    )
}