"use client";

import Link from "next/link";

export default function Error() {
    return (
        <main className="flex min-h-screen items-center justify-center bg-slate-950 px-6 text-slate-100">
            <section className="max-w-md rounded-2xl border border-slate-800 bg-slate-900/80 p-8 text-center shadow-xl">
                <p className="mb-3 text-sm font-medium uppercase tracking-[0.3em] text-red-400">
                    Application error
                </p>

                <h1 className="text-2xl font-semibold">Something went wrong</h1>

                <p className="mt-4 text-sm leading-6 text-slate-400">
                    CoreStock could not load this section correctly. Please go back to the dashboard and try again.
                </p>

                <Link
                    href="/"
                    className="mt-6 inline-flex rounded-xl bg-slate-100 px-4 py-2 text-sm font-semibold text-slate-950 transition hover:bg-white"
                >
                    Back to dashboard
                </Link>
            </section>
        </main>
    );
}