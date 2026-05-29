import { DashboardLayout } from "@/components/layout/DashboardLayout";

export default function DemoControlsPage() {
    return (
        <DashboardLayout>
            <div className="flex w-full justify-center py-10">
                <section className="w-full max-w-4xl rounded-3xl border border-slate-800 bg-slate-950 p-8 shadow-2xl">
                    <div className="max-w-3xl">
                        <p className="text-xs font-semibold uppercase tracking-[0.35em] text-blue-300">
                            Demo Environment
                        </p>

                        <h1 className="mt-3 text-4xl font-bold tracking-tight text-slate-100">
                            Demo Data Controls
                        </h1>

                        <p className="mt-6 text-lg leading-8 text-slate-400">
                            CoreStock includes pre-seeded demo data to simulate
                            realistic inventory and warehouse operations.
                        </p>

                        <div className="mt-8 rounded-2xl border border-slate-800 bg-slate-900/40 p-6">
                            <h2 className="text-lg font-semibold text-slate-100">
                                Included demo environment
                            </h2>

                            <ul className="mt-4 space-y-3 text-sm text-slate-400">
                                <li>• Products and inventory items</li>
                                <li>• Warehouse and supplier locations</li>
                                <li>• Stock quantities and transfers</li>
                                <li>• Purchase, sale and transfer operations</li>
                                <li>• Low stock monitoring scenarios</li>
                            </ul>
                        </div>

                        <div className="mt-8 rounded-2xl border border-blue-500/20 bg-blue-500/5 p-6">
                            <h2 className="text-lg font-semibold text-slate-100">
                                Why reset the demo environment?
                            </h2>

                            <p className="mt-4 text-sm leading-7 text-slate-400">
                                During exploration, stock levels and movements
                                may change as operations are created.
                            </p>

                            <p className="mt-4 text-sm leading-7 text-slate-400">
                                Resetting the environment restores the original
                                seeded data so the application can be tested
                                again from a clean and consistent state.
                            </p>
                        </div>

                        <div className="mt-8 flex flex-col items-start gap-4">
                            <p className="text-sm text-slate-500">
                                Demo reset cooldown: 5 minutes
                            </p>

                            <button
                                disabled
                                className="rounded-xl border border-slate-700 bg-slate-900 px-6 py-3 text-sm font-semibold text-slate-500"
                            >
                                Reset Demo Environment
                            </button>

                            <p className="text-xs text-slate-600">
                                Demo reset endpoint will be connected in a
                                future update.
                            </p>
                        </div>
                    </div>
                </section>
            </div>
        </DashboardLayout>
    );
}