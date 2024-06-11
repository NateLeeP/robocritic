import Image from "next/image";
import Link from "next/link";
export default function Banner({ }) {

    return (
        <div className="bg-slate-600">
            <Link className="flex justify-center" href="/"><Image src="/robot_logo.png" alt="robocritic-log" className='bg-transparent' width="100" height="100" /></Link>
            <Link href="/"><h1 className="text-2xl font-mono text-center font-bold text-stone-300">RoboCritic</h1></Link>
        </div>
    );
}