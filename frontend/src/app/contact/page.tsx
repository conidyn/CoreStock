import { DashboardLayout } from "@/components/layout/DashboardLayout";

const links = [
    {
        label: "LinkedIn",
        href: "https://www.linkedin.com/in/nicolas-doyen/",
    },
    {
        label: "GitHub",
        href: "https://github.com/conidyn",
    },
    {
        label: "Portfolio",
        href: "https://nicolas-doyen.vercel.app/",
    },
];

export default function ContactPage() {
    return (
        <DashboardLayout>
            <div className="flex min-h-[calc(100vh-4rem)] w-full items-center justify-center py-10">
                <section className="relative w-full max-w-3xl overflow-hidden rounded-3xl border border-slate-800 bg-slate-950 p-8 shadow-2xl">
                    <div className="absolute -left-24 top-10 h-64 w-64 rounded-full border border-blue-500/30" />
                    <div className="absolute -right-24 bottom-10 h-72 w-72 rounded-full border border-cyan-400/20" />
                    <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(59,130,246,0.18),transparent_45%)]" />

                    <div className="relative z-10 flex flex-col items-center text-center">
                        <img
                            src="/creator/nd-logo.svg"
                            alt="Nicolas Doyen logo"
                            className="h-28 w-28 rounded-2xl border border-slate-800 bg-white p-4"
                        />

                        <p className="mt-6 text-xs font-semibold uppercase tracking-[0.35em] text-blue-300">
                            Creator
                        </p>

                        <h1 className="mt-3 text-4xl font-bold tracking-tight text-slate-100">
                            Nicolas Doyen
                        </h1>

                        <p className="mt-3 text-lg text-slate-400">
                            Fullstack Web Developer | AI & Data Projects
                        </p>

                        <p className="mt-6 max-w-xl text-sm leading-6 text-slate-500">
                            CoreStock is a portfolio project designed to demonstrate clean
                            full-stack architecture, inventory logic, and practical
                            ERP/WMS-inspired product thinking.
                        </p>

                        <div className="mt-8 flex flex-wrap justify-center gap-3">
                            {links.map((link) => (
                                <a
                                    key={link.label}
                                    href={link.href}
                                    target="_blank"
                                    rel="noreferrer"
                                    className="rounded-full border border-slate-700 px-5 py-2 text-sm font-medium text-slate-300 transition hover:border-blue-400 hover:text-blue-300"
                                >
                                    {link.label}
                                </a>
                            ))}
                        </div>
                        <p className="mt-6 text-sm text-slate-500">
                            Available for opportunities · nicolas.doyen@hotmail.be
                        </p>
                    </div>
                </section>
            </div>
        </DashboardLayout>
    );
}