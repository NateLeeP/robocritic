import Games from '../components/Games.js'
import { getAllGames } from '../bff_api.js';

export async function getStaticProps() {
  const games = await getAllGames()
  return { props: { games } }
}
export default function Page({ games }) {
  return (
    <Games games={games} />
  );
}
