import { DashboardLayout } from "@/components/layout/DashboardLayout";
import { MovementTable } from "@/components/movements/MovementTable";

export default function MovementsPage() {
    return (
        <DashboardLayout>
            <div className="w-full max-w-7xl py-10">
                <div className="mb-10">
                    <p className="text-sm font-medium uppercase tracking-[0.3em] text-slate-500">
                        Movements
                    </p>

                    <h1 className="mt-3 text-4xl font-bold tracking-tight text-slate-100">
                        Stock Movements
                    </h1>

                    <p className="mt-3 text-lg text-slate-400">
                        Track incoming, outgoing and internal inventory operations across all locations.
                    </p>
                </div>
                <MovementTable />
            </div>
        </DashboardLayout>
    );
}