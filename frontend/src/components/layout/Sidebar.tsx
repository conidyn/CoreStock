type NavigationItem = {
    label: string;
    href: string;
};

const navigationItems: NavigationItem[] = [
    {
        label: "Dashboard",
        href: "/",
    },
    {
        label: "Products",
        href: "/products",
    },
    {
        label: "Locations",
        href: "/locations",
    },
    {
        label: "Movements",
        href: "/movements",
    },
];

export function Sidebar() {
    return (
        <aside className="hidden w-64 border-r border-slate-800 bg-slate-950 lg:flex lg:flex-col">
            <div className="border-b border-slate-800 px-6 py-6">
                <p className="text-xs font-semibold uppercase tracking-[0.3em] text-slate-500">
                    CoreStock
                </p>

                <h1 className="mt-2 text-2xl font-bold text-slate-100">
                    ERP Platform
                </h1>
            </div>

            <nav className="flex flex-1 flex-col gap-2 p-4">
                {navigationItems.map((item) => (
                    <a
                        key={item.label}
                        href={item.href}
                        className="rounded-lg px-4 py-3 text-sm font-medium text-slate-400 transition hover:bg-slate-900 hover:text-slate-100"
                    >
                        {item.label}
                    </a>
                ))}
            </nav>
        </aside>
    );
}