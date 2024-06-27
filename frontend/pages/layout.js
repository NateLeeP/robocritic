import { Inter } from "next/font/google";
import Banner from "../components/banner.js";
const inter = Inter({ subsets: ["latin"] });



export default function RootLayout({ children }) {
    return (
        <div>
            <Banner />
            <main className={`${inter.className} bg-slate-700 min-h-screen`}>{children}</main>
        </div>
    );
}