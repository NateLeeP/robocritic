import Game from '../../../components/Game'




export default async function Page({ params }) {
    const urlPath = params.title;



    return (
        <Game urlPath={urlPath} />
    )
}
