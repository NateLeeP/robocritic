import { useRouter } from "next/router"
import Game from "../../src/components/Game"

export default function GamePage() {
    const router = useRouter()
    return <Game game={{ title: 'Title', image: "https://assets-prd.ignimgs.com/2024/01/19/palworld-1705691572614.jpg?width=300&crop=1%3A1%2Csmart&auto=webp" }} />
}