import { Inter } from "next/font/google";
import "./globals.css";
import Banner from "../components/banner.js";
const inter = Inter({ subsets: ["latin"] });



export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`${inter.className} bg-gray-300`}>
        <Banner />
        <main>{children}</main>
      </body>
    </html>
  );
}