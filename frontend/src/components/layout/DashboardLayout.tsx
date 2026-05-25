import type { ReactNode } from "react";

import { Sidebar } from "@/components/layout/Sidebar";

type DashboardLayoutProps = {
    children: ReactNode;
};

export function DashboardLayout({
    children,
}: DashboardLayoutProps) {
    return (
        <main className="flex min-h-screen bg-slate-950 text-slate-100">
            <Sidebar />

            <section className="flex flex-1">
                <div className="flex w-full items-center justify-center px-6">
                    {children}
                </div>
            </section>
        </main>
    );
}