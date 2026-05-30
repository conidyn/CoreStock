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

            <section className="flex min-w-0 flex-1 pt-44 lg:pt-0">
                <div className="flex w-full min-w-0 justify-center px-4 md:px-6">
                    {children}
                </div>
            </section>
        </main>
    );
}