// Write a React component 
'use client'
import Game from '../../components/Game'
import { Suspense } from 'react'


export default function Page() {
    return (
        <Suspense>
            <Game />
        </Suspense >
    )
}
