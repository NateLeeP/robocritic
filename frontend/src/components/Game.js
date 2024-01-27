export default function Game({ game }) {
    return <div>
        Game {game.title}
        <img src={game.image} />
    </div>
}