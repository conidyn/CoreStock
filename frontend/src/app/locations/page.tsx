import { DashboardLayout } from "@/components/layout/DashboardLayout";
import { LocationTable } from "@/components/locations/LocationTable";

export default function LocationsPage() {
    return (
        <DashboardLayout>
            <div className="w-full max-w-7xl py-10">
                <div className="mb-10">
                    <p className="text-sm font-medium uppercase tracking-[0.3em] text-slate-500">
                        Locations
                    </p>

                    <h1 className="mt-3 text-4xl font-bold tracking-tight text-slate-100">
                        Stock Locations
                    </h1>

                    <p className="mt-3 text-lg text-slate-400">
                        Monitor warehouses, supplier locations, customer destinations and stock distribution.
                    </p>
                </div>
                <LocationTable />
            </div>
        </DashboardLayout>
    );
}