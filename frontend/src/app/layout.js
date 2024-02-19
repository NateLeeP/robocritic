import { Inter } from "next/font/google";
import "./globals.css";
import Banner from "./banner.js";
const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Robocritic",
  description: "AI generated video game reviews",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Banner />
        <main>{children}</main>
      </body>
    </html>
  );
}
