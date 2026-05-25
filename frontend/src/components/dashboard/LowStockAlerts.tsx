import { Card } from "@/components/ui/Card";

const lowStockItems = [
    {
        id: 1,
        product: "Logitech MX Keys",
        currentStock: 4,
        threshold: 10,
        location: "Liège Main Warehouse",
    },
    {
        id: 2,
        product: "Zebra Label Printer",
        currentStock: 2,
        threshold: 5,
        location: "Brussels Secondary Warehouse",
    },
];

export function LowStockAlerts() {
    return (
        <Card>
            <div className="mb-6">
                <h2 className="text-lg font-semibold text-slate-100">
                    Low stock alerts
                </h2>
                <p className="mt-1 text-sm text-slate-500">
                    Products currently below their minimum threshold.
                </p>
            </div>

            <div className="space-y-4">
                {lowStockItems.map((item) => (
                    <div
                        key={item.id}
                        className="rounded-xl border border-amber-500/20 bg-amber-500/5 p-4"
                    >
                        <div className="flex items-start justify-between gap-4">
                            <div>
                                <p className="font-medium text-slate-100">{item.product}</p>
                                <p className="mt-1 text-sm text-slate-500">{item.location}</p>
                            </div>

                            <span className="rounded-full bg-amber-500/10 px-3 py-1 text-xs font-semibold text-amber-300">
                                Low stock
                            </span>
                        </div>

                        <p className="mt-4 text-sm text-slate-400">
                            {item.currentStock} units available · minimum threshold{" "}
                            {item.threshold}
                        </p>
                    </div>
                ))}
            </div>
        </Card>
    );
}