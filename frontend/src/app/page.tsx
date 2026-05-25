import { DashboardLayout } from "@/components/layout/DashboardLayout";
import { KpiCard } from "@/components/dashboard/KpiCard";
import { RecentMovements } from "@/components/dashboard/RecentMovements";
import { LowStockAlerts } from "@/components/dashboard/LowStockAlerts";

export default function HomePage() {
  return (
    <DashboardLayout>
      <div className="w-full max-w-7xl py-10">
        <div className="mb-10">
          <p className="text-sm font-medium uppercase tracking-[0.3em] text-slate-500">
            CoreStock
          </p>

          <h1 className="mt-3 text-4xl font-bold tracking-tight text-slate-100">
            Inventory Dashboard
          </h1>

          <p className="mt-3 text-lg text-slate-400">
            Monitor inventory activity, stock levels and warehouse operations.
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
          <KpiCard
            label="Total Products"
            value="128"
            helperText="Tracked products"
          />

          <KpiCard
            label="Stock Units"
            value="12,540"
            helperText="Units across warehouses"
          />

          <KpiCard
            label="Low Stock Alerts"
            value="8"
            helperText="Products below threshold"
          />

          <KpiCard
            label="Stock Movements"
            value="245"
            helperText="Operations this month"
          />
        </div>
        <div className="mt-6 grid gap-6 xl:grid-cols-3">
          <div className="xl:col-span-2">
            <RecentMovements />
          </div>

          <LowStockAlerts />
        </div>
      </div>
    </DashboardLayout>
  );
}