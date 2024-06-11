import Games from '../components/Games.js'

export async function getStaticProps() {
  const response = await fetch("https://g5ql747n3i.execute-api.us-east-1.amazonaws.com/games", { cache: 'no-store' })

  if (!response.ok) {
    throw new Error('Failed to fetch reviews')
  }

  const games = await response.json()
  return { props: { games } }
}
export default function Page({ games }) {
  return (
    <Games games={games} />
  );
}
