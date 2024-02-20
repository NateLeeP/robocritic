import Image from 'next/image'
export default function Banner({ }) {

    return (
        <div className="h-28 flex items-center justify-center bg-gray-400">
            <img src="/robot_logo.png" className='pr-8 pl-8 h-20 bg-transparent' />
            <h1 className="text-2xl font-mono text-center font-bold">ROBOCRITIC</h1>
        </div>
    );
}