import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  metadataBase: new URL("https://corestock-v1.vercel.app"),
  title: "CoreStock",

  description:
    "Inventory and warehouse management platform built to explore stock traceability, warehouse operations and ERP-inspired business workflows.",

  applicationName: "CoreStock",

  openGraph: {
    title: "CoreStock",
    description:
      "Inventory and warehouse management platform built to explore stock traceability, warehouse operations and ERP-inspired business workflows.",
    type: "website",
    images: [
      {
        url: "/og/corestock-og.svg",
        width: 1200,
        height: 630,
        alt: "CoreStock",
      },
    ],
  },

  twitter: {
    card: "summary_large_image",
    title: "CoreStock",
    description:
      "Inventory and warehouse management platform built to explore stock traceability, warehouse operations and ERP-inspired business workflows.",
    images: ["/og/corestock-og.svg"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
