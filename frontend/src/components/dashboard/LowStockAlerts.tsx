import { Card } from "@/components/ui/Card";
import type { StockItem } from "@/lib/stock-items-api";

type LowStockAlertsProps = {
    stockItems: StockItem[];
};

export function LowStockAlerts({ stockItems }: LowStockAlertsProps) {
    const lowStockItems = stockItems.filter(
        (stockItem) =>
            stockItem.quantity <= stockItem.product.min_stock_threshold
    );

    return (
        <Card>
            <div className="mb-6">
                <h2 className="text-lg font-semibold text-slate-100">
                    Low stock alerts
                </h2>
                <p className="mt-1 text-sm text-slate-500">
                    Products currently at or below their minimum threshold.
                </p>
            </div>

            {lowStockItems.length === 0 ? (
                <div className="rounded-xl border border-emerald-500/20 bg-emerald-500/5 p-4">
                    <p className="font-medium text-emerald-300">
                        No low stock alerts
                    </p>
                    <p className="mt-1 text-sm text-slate-500">
                        All tracked products are above their minimum threshold.
                    </p>
                </div>
            ) : (
                <div className="space-y-4">
                    {lowStockItems.map((item) => (
                        <div
                            key={item.id}
                            className="rounded-xl border border-amber-500/20 bg-amber-500/5 p-4"
                        >
                            <div className="flex items-start justify-between gap-4">
                                <div>
                                    <p className="font-medium text-slate-100">
                                        {item.product.name}
                                    </p>
                                    <p className="mt-1 text-sm text-slate-500">
                                        {item.location.name}
                                    </p>
                                </div>

                                <span className="rounded-full bg-amber-500/10 px-3 py-1 text-xs font-semibold text-amber-300">
                                    Low stock
                                </span>
                            </div>

                            <p className="mt-4 text-sm text-slate-400">
                                {item.quantity} units available · minimum threshold{" "}
                                {item.product.min_stock_threshold}
                            </p>
                        </div>
                    ))}
                </div>
            )}
        </Card>
    );
}