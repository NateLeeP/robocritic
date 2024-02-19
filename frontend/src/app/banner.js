import Image from 'next/image'
export default function Banner({ }) {

    return (
        <div className="flex items-center justify-center bg-sky-50 h-20">
            <img src="/robot_logo.png" className='pr-8 pl-8 h-20 bg-transparent' />
            <h1 className="px-px text-2xl font-mono text-center">ROBOCRITIC</h1>
        </div>
    );
}