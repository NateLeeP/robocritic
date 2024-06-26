export default function Review({ key, review }) {

    const mockReview =
    {
        "game_title": "Paper Mario: The Thousand-Year Door",
        "review_publisher_name": "IGN",
        "cons": [
            "Overreliance on backtracking in the main quest, especially in some chapters",
            "Clunky NPC path-finding routines and slow-moving early chapters",
            "Standard RPG fetch-quest side quests with limited rewards and the inability to take on multiple quests at once"
        ],
        "game_release_date": "2024-05-23",
        "pros": [
            "Gorgeous visuals and environments that maintain the original's papery, storybook aesthetic",
            "Outstanding updated soundtrack and new battle theme arrangements",
            "Sharp, laugh-out-loud script with consistent humor and charm",
            "Diverse and well-defined party of seven partners with unique abilities and backstories",
            "Exciting turn-based battles with Action Commands and Badge-based upgrade system",
            "Unique mechanics in battles, such as the live audience and Stylish Moves, add depth and entertainment",
            "Engaging dungeons with interesting puzzles, collectibles, and epic boss fights",
            "Modern improvements that streamline backtracking issues compared to the original version"
        ],
        "roboscore": 10,
        "critic_score": 9,
        "review_url": "https://www.ign.com/articles/paper-mario-the-thousand-year-door-review"
    }

    return (
        <div key={key} className="flex w-4/5 justify-between border-b-4 border-slate-400 border-dotted">
            <div className="">
                <a className="self-center justify-center text-2xl italic underline" target="_blank" href={review.review_url}>{review.review_publisher_name}</a>
                <h3>Critic score: {review.critic_score}</h3>
                <h3>Roboscore: {review.roboscore}</h3>
            </div>
            <ul className="basis-1/3">
                <div key={25} className="italic">Pros</div>
                {review.pros.map((pro, index) => (<li key={index}>{pro}<br /></li>))}
            </ul>
            <ul className="basis-1/3">
                <div key={20} className="italic">Cons</div>
                {review.cons.map((con, index) => (<li key={index}>{con}<br /></li>))}
            </ul>
        </div>
    )
}