type NavigationItem = {
    label: string;
    href: string;
};

const navigationItems: NavigationItem[] = [
    { label: "Dashboard", href: "/" },
    { label: "Products", href: "/products" },
    { label: "Locations", href: "/locations" },
    { label: "Movements", href: "/movements" },
    { label: "Contact Creator", href: "/contact" },
    { label: "Demo Data Controls", href: "/demo-controls" },
];

const primaryMobileItems = navigationItems.slice(0, 3);
const secondaryMobileItems = navigationItems.slice(3, 5);
const demoMobileItem = navigationItems[5];

export function Sidebar() {
    return (
        <>
            <aside className="hidden w-64 border-r border-slate-800 bg-slate-950 lg:flex lg:flex-col">
                <div className="border-b border-slate-800 px-6 py-6">
                    <p className="text-xs font-semibold uppercase tracking-[0.3em] text-slate-500">
                        CoreStock
                    </p>

                    <h1 className="mt-2 text-2xl font-bold text-slate-100">
                        Warehouse Management
                    </h1>
                </div>

                <nav className="flex flex-1 flex-col gap-2 p-4">
                    {navigationItems.map((item) => (
                        <a
                            key={item.label}
                            href={item.href}
                            className={`rounded-lg px-4 py-3 text-sm font-medium transition ${item.label === "Demo Data Controls"
                                    ? "mt-10 border border-blue-500/20 bg-slate-900 text-center text-slate-200 hover:border-blue-400/40 hover:bg-slate-800"
                                    : "text-slate-400 hover:bg-slate-900 hover:text-slate-100"
                                }`}
                        >
                            {item.label}
                        </a>
                    ))}
                </nav>
            </aside>

            <header className="fixed inset-x-0 top-0 z-50 border-b border-slate-800 bg-slate-950/95 px-4 py-4 backdrop-blur lg:hidden">
                <div className="text-center">
                    <p className="text-xs font-semibold uppercase tracking-[0.25em] text-slate-500">
                        CoreStock
                    </p>
                    <p className="mt-1 text-sm font-semibold text-slate-100">
                        Warehouse Management
                    </p>
                </div>

                <nav className="mt-4 flex flex-col items-center gap-3">
                    <div className="flex justify-center gap-2">
                        {primaryMobileItems.map((item) => (
                            <a
                                key={item.label}
                                href={item.href}
                                className="rounded-full bg-slate-900 px-3 py-2 text-xs font-medium text-slate-300"
                            >
                                {item.label}
                            </a>
                        ))}
                    </div>

                    <div className="flex justify-center gap-2">
                        {secondaryMobileItems.map((item) => (
                            <a
                                key={item.label}
                                href={item.href}
                                className="rounded-full bg-slate-900 px-3 py-2 text-xs font-medium text-slate-300"
                            >
                                {item.label}
                            </a>
                        ))}
                    </div>

                    <a
                        href={demoMobileItem.href}
                        className="mt-1 rounded-full border border-blue-500/30 bg-blue-500/10 px-5 py-2 text-xs font-semibold text-blue-200"
                    >
                        {demoMobileItem.label}
                    </a>
                </nav>
            </header>
        </>
    );
}