import { DashboardLayout } from "@/components/layout/DashboardLayout";
import { MovementTable } from "@/components/movements/MovementTable";
import { getStockMovements } from "@/lib/movements-api";
import { CreateMovementForm } from "@/components/movements/CreateMovementForm";
import { getProducts } from "@/lib/products-api";
import { getStockLocations } from "@/lib/locations-api";
export const dynamic = "force-dynamic";

export default async function MovementsPage() {
    const movements = await getStockMovements();
    const products = await getProducts();
    const locations = await getStockLocations();
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
                <div className="mb-6">
                    <CreateMovementForm products={products} locations={locations} />
                </div>
                <MovementTable movements={movements} />
            </div>
        </DashboardLayout>
    );
}